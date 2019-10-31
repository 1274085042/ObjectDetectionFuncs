# 线性回归  
线性回归（Linear regression）是找多个自变量（independent variable）和因变量（dependent variable）之间的关系而建立的模型。  
只有一个自变量和一个因变量的情形称为简单线性回归，大于一个自变量的情形称为多元回归（multiple regerssion）。  
## Simple linear regression  
用线性回归来建立房屋面积（自变量）与房价（因变量）的关系，房价=y,房屋面积=x。   
简单线性回归：$y=\beta_0+\beta_1x$  
$\beta_0$:截距 &nbsp;&nbsp;&nbsp;&nbsp;$\beta_1$:斜率  
![][picture1]     
回归分析就是找$\beta_0$和$\beta_1$,但要怎么找？   
先收集一组训练集($x_i$,$y_i$), i=1,2,.....,n 将每个点都带回到公式内：   
$$\hat{y_i}=\beta_0+\beta_1x_i$$   
$\hat{y_i}$为预估出来的房价，和真实房价有误差(error):  
$\epsilon_i=y_i-\hat{y_i}$  
![][picture2]   
所以回归分析的损失函数就是希望找到的模型误差越小越好，统计上会用一个很专业的名词：最小平方(Least Square)来找参数$\beta_0$和$\beta_1$。  
为什么用最小平方，就是希望误差的平方越小越好，为什么是平方，因为误差有正有负，取平方后都为正值（防止了正负相互抵消），所以我们会很希望所有训练样本的误差平方和(Sum Square Error,SSE)接近0。  

![][picture3]    

为了推估$\beta_0$,对Loss做$\beta_0$偏微分等于0  
![][picture4]    
  
为了推估$\beta_1$,对Loss做$\beta_1$偏微分等于0    
![][picture5]

## Multiple regression    
假设有n个训练样本，d个自变量和1个因变量。   
X向量多一个1在向量的最前面，这个部分就是截距。  
![][picture6]  
回归公式：
$$Y_{(n,1)}=X_{(n,d+1)}\beta_{(d+1,1)}$$    
![][picture7]  
Loss function 定义为：  
$$\begin{aligned}
  Loss(\beta)&={(Y-\hat{Y})}^T(Y-\hat{Y})\\
\end{aligned}$$  
可以用最小二乘法，也可用随机梯度下降(Stochastic gradient descent,SGD)来求解。

[//]: # (Image reference)
[picture1]: ./example/1.png  
[picture2]: ./example/2.png
[picture3]: ./example/3.png  
[picture4]: ./example/4.png
[picture5]: ./example/5.png
[picture6]: ./example/6.png
[picture7]: ./example/7.png