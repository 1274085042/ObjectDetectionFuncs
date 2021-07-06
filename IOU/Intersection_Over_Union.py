#coding=utf-8
from  collections import namedtuple
import numpy as np
import  cv2

Detection=namedtuple("Detection",["image_path","gt","pred"])    #三个属性的检测对象

def bb_intersection_over_union(boxA,boxB):
    #determine the (x,y)-coordinates of the intersection rectangle
    x1=max(boxA[0],boxB[0])
    y1=max(boxA[1],boxB[1])
    x2 = min( boxA[2], boxB[2] )
    y2 = min( boxA[3], boxB[3] )

    #compute the area of intersection rectangle
    interArea=max(0,x2-x1+1)*max(0,y2-y1+1)

    #compute the area of both the prediction and ground-truth  rectangles
    boxAArea=(boxA[2]-boxA[0]+1)*(boxA[3]-boxA[1]+1)
    boxBArea=(boxB[2]-boxB[0]+1)*(boxB[3]-boxB[1]+1)

    iou=interArea/(boxAArea+boxBArea-interArea)

    return iou

if __name__=="__main__":
    examples = [
    Detection("image_0002.jpg", [39, 63, 203, 112], [54, 66, 198, 114]),
    Detection("image_0016.jpg", [49, 75, 203, 125], [42, 78, 186, 126]),
    Detection("image_0075.jpg", [31, 69, 201, 125], [18, 63, 235, 135]),
    Detection("image_0090.jpg", [50, 72, 197, 121], [54, 72, 198, 120]),
    Detection("image_0120.jpg", [35, 51, 196, 110], [36, 60, 180, 108])]

    for detection in examples:
        iou=bb_intersection_over_union(detection.gt,detection.pred)
        print(detection.image_path," IOU:",iou)