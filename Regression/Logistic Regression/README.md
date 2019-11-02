# 逻辑回归    
## 回顾线性回归
假设样本的特征有d个维度，$B$是参数，y是预测值。  
![][picture1]    
**上面公式为线性回归模型用来预测连续的值。**   
## Logistic Regression
![][picture4]  
**上面公式为逻辑回归模型用来分类，n为样本的特征数量，f(x)为分类超平面。**  

![][picture2]   
  
**但逻辑回归要怎么做分类（二分类）？**  
一个最简单的概念，将点带进回归线，回归线的输出值若是>=0，是一类（target），值<0是另一类（non-target）。    

![][picture3]  
这个判断法其实就是一个unit-step function,如下:   

![][picture5]    

这种模型就称为**感知机(Perceptron)**。     

![][picture6]       

unit-step function  

![][picture7]  
感知机模型能够进行二元分类，但我们只能知道预测结果是A还是B，没办法知道是A、是B的概率是多少。这种应用在我们生活中非常常见，比如说我们要根据今天的温度、湿度、风向来预测明天的天气，通常我们需要知道明天是晴天的概率以及雨天的概率，来决定是否带伞出门。如果使用Logistic Regression就可以实现这样的目的。当$w_0+w_1x_1+w_2x_2+...+w_nx_n$越大时判断成A类的概率越大，越小时判断成A类的概率越小。  
![][picture8]  
sigmoid function  
![][picture9]
$$\sigma(f(X))=\frac{1}{1+e^{-f(X)}}$$  
在Logistic Regression不一定要用sigmoid函数，也可以使用其它值域为0~1的函数。   
### 损失函数  
我们的目的是寻找一组$w$使得模型($w_0+w_1x_1+w_2x_2+...+w_nx_n$)的预测最符合训练样本的分布,因此用最大似然估计来求解这组参数。   
$$y=\sigma(f(X))$$ 
![][picture10]
###  利用SGD更新参数      
  
![][picture11]
$$w_j^{(t+1)}=w_j^{(t)}+\eta(-\frac{\partial L}{\partial w_j})$$  

[//]: # (Image reference)
[picture1]: ./example/1.png
[picture2]: ./example/2.png
[picture3]: ./example/3.png
[picture4]: ./example/4.png
[picture5]: ./example/5.png  
[picture6]: ./example/6.png
[picture7]: ./example/7.png  
[picture8]: ./example/8.png
[picture9]: ./example/9.png
[picture10]: ./example/10.png
[picture11]: ./example/11.png