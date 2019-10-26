# NMS   
**Input:** B={$b_1$,$b_2$,...,$b_m$,...,$b_n$},C={$c_1$,$c_2$,...,$c_m$,...,$c_n$},$IOU_t$    
B is the list of boundingbox  
C contains corresponding confidence  
$IOU_t$ is the NMS threshold  
___
**begin**  
&nbsp;&nbsp;&nbsp;&nbsp;D$\leftarrow${}     
&nbsp;&nbsp;&nbsp;&nbsp;while  B$\neq$empty do   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$c_m$$\leftarrow$argmax&nbsp;C  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D$\leftarrow$D&nbsp;$\bigcup b_m$  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B$\leftarrow$B&nbsp;-&nbsp;$b_m$  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for b in B do:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if $IOU_{bm}^b$>$IOU_t$  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B$\leftarrow$B&nbsp;-&nbsp;b  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C$\leftarrow$C&nbsp;-&nbsp;c      
&nbsp;&nbsp;&nbsp;&nbsp;return D,C  
**end**
___   
例：有两只狗，怎样用NMS去除冗余边界框，将两只狗定位出来。
![][picture1]    
算法步骤：  
1. 先找出置信度最高的BBox  
2. 其它的BBox和刚选出来的BBox计算IOU，将IOU大于阈值的BBox丢弃。  

重复1、2步，直到所有的BBox都被处理完。  
处理流程如下所示：   

![][picture2]    
1. 确定是目标={空集合}  
2. Run 1：先将BBox按照置信度排序，置信度最高的BBox（红色）放入确定是目标的集合内，其它BBox和该BBox计算IOU。因为粉红色边界框的IOU为0.6，大于阈值（0.5），所以将粉色BBox丢弃。
3. Run 2：在剩下的BBox中继续选出置信度最高的BBox（黄色）放入确定是目标的集合内，其它的BBox和该BBox计算IOU。因为其它的边界框的IOU都大于0.5，所以这些边界框都被丢弃。  
4. BBox集合为空，结束NMS
  
**实际做法**  
先设置一个置信度阈值去掉一些BBox，不然一张图检测出一万个BBox，然后用CPU计算NMS会很花时间。如下图所示：  
![][picture5]  

[//]: # (Image Reference)  
[picture1]: ./picture/picture1.png
[picture2]: ./picture/picture3.png
[picture5]: ./picture/picture5.png