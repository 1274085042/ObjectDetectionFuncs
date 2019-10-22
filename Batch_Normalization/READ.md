 # <font size=7>Bacth Normalization</font>  
## <font size=6>梯度</font> 
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
 ___
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
  - [<font size=6 color=#09A7A7>BN</font>](#bn)
    - [<font size=5 color=#09A7A7>Feature Scaling</font>](#feature-scaling)
    - [<font size=5 color=#09A7A7>Batch normalization at training stage</font>](#batch-normalization-at-training-stage)
    - [<font size=5 color=#09A7A7>Batch normalization at testing stage</font>](#batch-normalization-at-testing-stage)
    - [<font size=5 color=#09A7A7>Batch normalization benefit</font>](#batch-normalization-benefit)

## <font size=6 color=#09A7A7>BN</font>
### <font size=5 color=#09A7A7>Feature Scaling</font>
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/picture2.png)
假设$x_1$和$x_2$的数值差距很大，如图(a)  
$x_1$的值为1,2,3等  
$x_2$的值为100,200,300等  
$w_1$前面乘的值比较小，所以loss对$w_1$的偏导比较小  
$w_2$前面乘的值比较大，所以loss对$w_2$的偏导比较大   
  
把$w_1$,$w_2$对loss的值的影响做图（等值线），在$w_1$方向上的变化率比较小，在$w_2$方向上的变化率比较大。  
这会使training变得困难，因为要在不同方向上给不同的learing rate。  
而在图(b)中，$x_1$和$x_2$的数值差距不大时，我们只需要一个learning rate就可以。  
因此把不同的feature做normalization，让error等值线接近图(b).  
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Feature%20Scaling.png)  
Feature Scaling 做法：
$$x^r_i\leftarrow\frac{x^r_i-m_i}{\sigma _i}$$
$x^r_i$：第r个data的第i维特征 &nbsp;&nbsp;&nbsp;&nbsp;$m_i$：该维mean&nbsp;&nbsp;&nbsp;&nbsp;$\sigma _i$：该维度的standard deviation
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Batch_normalization1.png)  
input做完Feature Scaling 然后进入Layer1  
经过Layer1运算后的output在要进入Layer2之前也做Feature Scaling  
经过Layer2运算后的output在要进入Layer3之前也做Feature Scaling  
### <font size=5 color=#09A7A7>Batch normalization at training stage</font>
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Batch_normalization2.png)  
使用GPU加速运算时，假设Batch=3  
$x^1$,$x^2$,$x^3$代表三个输入样本，把这三个样本排在一起变成一个input matrix X和weight matrix W运算，得到一个output matrix Z。   
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Batch_normalization3.png)  
Normalization可以放在activation function之前，也可以放在activation function之后。通常把Normalization放在activation之前，因为有些activation function像是tanh或是sigmoid会有saturation region，我们不喜欢input 落在saturation region，所以先做normalization把数据变为标准正态分布再丢进activation function（因为标准正态分布在0附近的值很多，所以数据不容易掉进saturation region）。  
现在做Normalization，计算平均值$\mu$和标准差$\sigma$,$\mu$和$\sigma$都是依赖输入$z^1$,$z^2$和$z^3$，我们希望$\mu$和$\sigma$是代表整个training set上面的情况，因此Batch的size不能太小，否则无法从batch估测整个data的情况。  
![]()  
有Batch Normalization的时候该怎么train？  
反向传播的时候要经过$\mu$和$\sigma$，不要把$\mu$、$\sigma$当成常数。    
  
  ---
如果有的activation function不希望输入的data均值为0，标准差为1。  
我们可以加上$\gamma$和$\beta$来调整data的mean和standard deviation，调整完之后在丢进activation function。  
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Batch_normalization7.png)
$$\hat{Z}=\gamma \times\tilde{Z}+\beta$$  
$\gamma$和$\beta$为作为network参数，是可以被训练出来的。
### <font size=5 color=#09A7A7>Batch normalization at testing stage</font>
Testing的时候数据是一个一地进来的，所以没办法计算$\mu$和$\sigma$。  
解决方法：  
1. 计算整个training set的$\mu$和$\sigma$，显然如果training set比较大，该方法便行不通。  
2. $\mu$和$\sigma$是在训练过程中逐步更新的，计算训练过程中$\mu$和$\sigma$的平均值。   
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Batch_normalization8.png)  
### <font size=5 color=#09A7A7>Batch normalization benefit</font>  
1.  Batch normalization可以缓解internal covariate shift，所以可以使用一个比较大的学习率，从而缩短了训练时间。
2.  缓解vanishing gradients(因为如果激活函数是sigmoid，那么值很大或者很小的时候，梯度会很小，而batch normalization可以缓解数据落到saturation region)。  
3.  参数的initialization对训练影响比较小（假设$W^1$乘以k,那么该层的输出$Z^i\times k$,做normalization的时候,因为$\mu$和$\sigma$都乘以k,所以最后的结果不变），也就是说BN使模型训练对参数的初始化比较不敏感。
![](https://github.com/1274085042/Object_Detection_Funcs/blob/master/Batch_Normalization/Batch_normalization9.png)  
4.  防止过拟合（如果在测试的时候，进来一个数据和训练样本差距很大，那么做BN后，会使这个shift变小。）
    
    

    