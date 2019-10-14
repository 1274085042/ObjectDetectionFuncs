# Bacth Normalization  

## 梯度
*方向导数*   
三维空间中的曲面z=f(x,y)，p($x_0$,$y_0$)为f定义域中的一个点，x轴、y轴两个基向量为$\vec{i}$=(1,0),$\vec{j}$=(0,1)，  
搜索方向$\vec{u}=cos\theta\vec{i}+sin\theta\vec{j}$。  
点p沿$\vec{u}$方向移动距离t（沿x轴移动距离为$tcos\theta$，沿y轴移动距离为$tsin\theta$），函数f在$\vec{u}$方向上的的方向导数为:  
$$D_uf=\lim_{t\to 0}\frac{f(x_0+tcos\theta,y_0+tsin\theta)-f(x_0,y_0)}{t}$$
随着$\theta$的不同，我们可以求出任意方向的方向导数。  
方向导数的另一种形式，假设f(x,y)是一个可微分函数，则f沿着搜索方向$\vec{u}$的方向导数为：  
$$D_uf=f_x(x,y)cos\theta+f_y(x,y)sin\theta$$
证  根据z=f(x,y)在点p($x_0$,$y_0$)可微分的假定，函数的增量可以表达为：  
$$f(x_0+tcos\theta,y_0+tsin\theta)-f(x_0,y_0)=\frac{\partial f}{\partial x}tcos\theta+\frac{\partial f}{\partial y}tsin\theta+o(t)$$
两边都除以t，得到：  
$$\frac{f(x_0+tcos\theta,y_0+tsin\theta)-f(x_0,y_0)}{t}=\frac{\partial f}{\partial x}cos\theta+\frac{\partial f}{\partial y}sin\theta+\frac{o(t)}{t}$$  
$$因为\quad o(t)是t的高阶无穷小$$
$$所以\quad D_uf=\lim_{t\to 0}\frac{f(x_0+tcos\theta,y_0+tsin\theta)-f(x_0,y_0)}{t}=\frac{\partial f}{\partial x}cos\theta+\frac{\partial f}{\partial y}sin\theta$$
$$D_uf=f_x(x,y)cos\theta+f_y(x,y)sin\theta$$
$\vec{u}=(cos\theta,sin\theta)$,假设$\vec{A}=(f_x(x,y),f_y(x,y))$  
那么$D_uf=\vec{A}\cdot\vec{u}=|\vec{A}||\vec{u}|cos\alpha$ &nbsp;&nbsp;&nbsp;($\alpha为\vec{A}和\vec{u}之间的夹角$)   
如果$D_uf$要取得最大值，也就是当$\alpha$为0的时候，也就是向量$\vec{u}$（这个方向是一直在变，在寻找一个函数变化最快的方向）与向量$\vec{A}$（这个方向当点固定下来的时候，它就是固定的）平行的时候，方向导数最大.函数值朝这个方向变化最快.  
现在已经找到函数值变化最快的方向了，这个方向就是和$\vec{A}$向量相同的方向.那么此时我把$\vec{A}$向量命名为梯度（当一个点确定后，梯度方向是确定的）。  
  
  注：为什么求函数增量时要加o(t)  
  ![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/%E4%B8%80%E5%85%83%E5%87%BD%E6%95%B0%E5%A2%9E%E9%87%8F.gif)  
  由动图可以清晰看出，随着Δx变小，Δy与dy之间的误差error也越来越小。并且这个error的减小速度可以看出比Δx变化的要快，这也就是error是Δx的高阶无穷小量的几何意义。
# BN
## Feature Scaling
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/picture2.png)
假设$x_1$和$x_2$的数值差距很大，如图(a)  
$x_1$的值为1,2,3等  
$x_2$的值为100,200,300等  
$w_1$前面乘的值比较小，所以loss对$w_1$的偏导比较小  
$w_2$前面乘的值比较大，所以loss对$w_2$的偏导比较大   
  
把$w_1$,$w_2$对loss的值的影响做图（等值线），在$w_1$方向上的变化率比较小，在$w_2$方向上的变化率比较大。  
这会使training变得困难，因为要在不同方向上给不同的learing rate。  
而在图(b)中，$x_1$和$x_2$的数值差距不大时，我们只需要一个learning rate就可以。