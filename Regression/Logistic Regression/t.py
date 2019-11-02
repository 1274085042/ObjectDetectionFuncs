#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
# 下面的代码，我不负责。因为是他们逼我写的，违背了我的意愿。

import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path="D:\PycharmProjects\Object_Detection_Funcs\Regression\Logistic Regression\data\ex2data1.txt"
data=pd.read_csv(path,header=None,names=['Exam 1','Exam 2','Admitted'])


positive=data[data['Admitted'].isin([1])]
negative=data[data['Admitted'].isin([0])]

def sigmoid(z):
    return  1/(1+(np.exp(-z)))


def cost(weight,X,y):
    weight=np.matrix(weight)
    X=np.matrix(X)
    y=np.matrix(y)
    first=np.multiply(-y,np.log(sigmoid(X*weight.T)))
    second=np.multiply((1-y),np.log(1-sigmoid(X*weight.T)))
    return np.sum(first-second)/(len(X))

data.insert(0,'Ones',1)
cols = data.shape[1]
X=data.iloc[:,0:3]
y=data.iloc[:,3:]
# print(X)
# print(y)
X=np.array(X.values)
y=np.array(y.values)
weights=np.zeros(3)

print(cost(weights,X,y))


def gradient(theta, X, y):
    theta = np.matrix( theta )
    X = np.matrix( X )
    y = np.matrix( y )
    parameters=theta.ravel()
    print(parameters)
    print(parameters.shape)
    parameters = parameters.shape[1]
    grad = np.zeros( parameters )

    error = sigmoid( X * theta.T ) - y

    for i in range( parameters ):
        term = error*X[:,i].T
        grad[i] = np.sum( term ) / len( X )

    return grad


print(gradient(weights, X,y))