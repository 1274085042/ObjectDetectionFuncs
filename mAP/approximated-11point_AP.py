#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

def preprocess_iris_data():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    # Add noisy features
    random_state = np.random.RandomState(0)
    n_samples, n_features = X.shape
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
    # 鸢尾花数据集有三类，取其中两类
    # Limit to the two first classes, and split into training and test
    X_train, X_test, y_train, y_test = train_test_split(X[y < 2], y[y < 2],
                                                        test_size=.5,
                                                        random_state=random_state)
    # Create a simple classifier
    classifier = svm.LinearSVC(random_state=random_state)
    classifier.fit(X_train, y_train)
    y_score = classifier.decision_function(X_test)
    return y_test, y_score


def precision_recall_curve(y_true, y_score):
    # 不同的排序方式，其结果也会有略微差别，
    # 比如 kind="mergesort" 的结果跟kind="quicksort"的结果是不同的，
    # 这是因为归并排序是稳定的，快速排序是不稳定的，sklearn中使用的是 kind="mergesort"
    desc_score_indices = np.argsort(y_score, kind="quicksort")[::-1]
    y_score = y_score[desc_score_indices]
    y_true = y_true[desc_score_indices]
    # 确定有多少个Rank
    rank_idxs = np.arange(y_score.size)
    # 按照阈值依次降低的顺序，确定当前rank下的true positives 个数，tps[-1]对应于所有的正例数量
    #tps = np.cumsum(y_true * 1.)[threshold_idxs]
    tps = np.cumsum( y_true * 1.)
    # 计算当前rank下的 false positives 个数，
    # 它与tps的关系为fps=1+threshold_idxs-tps，这个关系是比较明显的
    fps = 1 + rank_idxs - tps
    # y_score[rank_idxs]把当前rank下的分数取出
    score = y_score[rank_idxs]
    precision = tps / (tps + fps)
    recall = tps / tps[-1]
    # 这里与sklearn有略微不同，即样本点全部输出，令last_ind = tps.size，即可
    # last_ind = tps.size
    # sl = slice(0, last_ind)
    if precision[0]==1:
        precision=precision.tolist()
        precision.insert(0,1.)
        precision=np.array(precision)
        recall = recall.tolist()
        recall.insert( 0, 0. )
        recall = np.array( recall )
    #return np.r_[1, precision[sl]], np.r_[0, recall[sl]], score[sl]
    return  precision,recall,score


def average_precision_approximated(y_true, y_predict):
    """
    :param y_true: 标签
    :param y_predict: 预测得分
    :return: precision，recall，threshold，average precision
    """
    precision, recall, score = precision_recall_curve(y_true, y_predict)
    average_precision = np.sum(np.diff(recall) * precision[1:])
    return precision, recall, score, average_precision

def average_precision_11point_interpolated(y_true, y_predict):
    """
    计算 11point形式的 ap
    :param y_true: 标签
    :param y_predict: 预测得分
    :return: precision，recall，score，average precision
    """
    precision, recall, score = precision_recall_curve( y_true, y_predict)
    recall_11point = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    # 计算离11个阈值最近的样本点索引
    recall_cutoff_index = []
    for cutoff in recall_11point:
        recall_cutoff_index.append(np.where(recall >= cutoff)[0][0])
    precision_cutoff_index = []
    for index in recall_cutoff_index:
        precision_cutoff_index.append([x for x in np.where(precision==np.max(precision[index:]))[0] if x>=index][0])
        #precision_cutoff_index.append(max([x for x in np.where(precision == np.max(precision[index:]))[0] if x >= index]))
    precision_11point = precision[precision_cutoff_index]

    average_precision = np.mean(precision_11point)

    return precision_11point, recall_11point, average_precision

def main(data=None):
    y_test = []
    y_score = []
    if data is None:
        # 一个简单的示例，这个示例直接给定了y_test和y_score
        y_test = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1])
        y_score = np.array([0.23, 0.76, 0.01, 0.91, 0.13, 0.45, 0.12, 0.03, 0.38, 0.11, 0.03, 0.09, 0.65, 0.07, 0.12, 0.24, 0.1, 0.23, 0.46, 0.08])
    if data == 'iris':
        # 还可以导入鸢尾花数据集并构建一个简单的SVM分类器，通过一个完整的模型来理解 PR曲线的绘制
        # 使用鸢尾花数据集
        y_test, y_score = preprocess_iris_data()
    # 计算AP，并画图
    precision_approximated, recall_approximated, _, ap_approximated = average_precision_approximated(y_test, y_score)

    precision_11point, recall_11point, ap_11point = average_precision_11point_interpolated(y_test, y_score)

    print('Approximated average precision-recall score: {0:0.5f}'.format(ap_approximated))
    print('Interpolated at fixed 11 points average precision-recall score: {0:0.5f}'.format(ap_11point))

    # print the AP plot
    fig1 = plt.figure('fig1')
    plt.plot(recall_approximated, precision_approximated, color='r', marker='^', mec='m', ms=4)
    plt.step(recall_approximated, precision_approximated, color='c', where='pre')
    plt.fill_between(recall_approximated, precision_approximated, step='pre', alpha=0.2,color='b')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1])
    plt.title('2-class Precision-Recall curve(Approximated): AP={0:0.5f}'.format(ap_approximated))
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)
    plt.legend(('PR-curve', 'Approximated-PR-curve', 'Approximated-AP'),loc='upper right')
    plt.savefig( 'D:\PycharmProjects\Object_Detection_Funcs\mAP\example/6.png' )
    fig2 = plt.figure('fig2')
    plt.plot(recall_approximated, precision_approximated,color='r', marker='^', mec='m', ms=4)
    plt.plot(recall_11point, precision_11point,color='c', marker='o', mec='g', ms=3)
    #plt.fill_between(recall_11point, precision_11point, step='pre', alpha=0.2,color='b')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1])
    plt.title('2-class Precision-Recall curve(Interpolated_11point): AP={0:0.5f}'.format(ap_11point))
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)
    plt.legend(('PR-curve', '11point-PR-curve'),loc='upper right')
    # plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,
    #                     wspace=0.35)
    plt.savefig('D:\PycharmProjects\Object_Detection_Funcs\mAP\example/7.png')
    plt.show()

if __name__ == '__main__':
    main() # 用这个测试博客 “多标签图像分类任务的评价方法-mAP” 中的简单例程
    #main('iris')