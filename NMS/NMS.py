#coding=utf-8
import numpy as np

def nms(dets,thresh):
    x1=dets[:,0]
    y1=dets[:,1]
    x2=dets[:,2]
    y2=dets[:,3]
    scores=dets[:,4]

    #每一个检测框的面积
    areas=(x2-x1+1)*(y2-y1+1)

    order=scores.argsort()[::-1]    #np.argsort将数组从小到大排列，返回其索引数组，[::-1]将数组反向输出。

    D=[]

    while order.size>0:
        i=order[0]
        D.append(i)

        #以下计算置信度最大的框（order[0]）与其它所有的框（order[1:]，即第二到最后一个）框的IOU
        xx1 = np.maximum(x1[i],x1[order[1:]])
        yy1 = np.maximum( y1[i], y1[order[1:]] )
        xx2 = np.minimum( x2[i], x2[order[1:]] )
        yy2 = np.minimum( y2[i], y2[order[1:]] )

        w=np.maximum(0.0,xx2-xx1+1)
        h=np.maximum(0.0,yy2-yy1+1)

        inter=w*h
        IOU=inter/((areas[i]+areas[order[1:]])-inter)
        inds=np.where(IOU<thresh)[0]   #本轮，order仅保留IOU小于阈值的下标
        order=order[inds+1]            #删除IOU大于阈值的框

    return D


# test
if __name__ == "__main__":
    dets = np.array( [[50, 50, 260, 220, 0.9],
                      [430, 280, 460, 360, 0.7],
                      [210, 30, 420, 5, 0.8],
                      [30, 20, 230, 200,1]] )
    thresh = 0.35
    keep_dets = nms( dets, thresh )
    print( keep_dets )
    print( dets[keep_dets] )