from dealCsv import *
import numpy as np
import matplotlib.pyplot as plt

class LR:
    def __init__(self,X,Y) -> None:
        self.height=len(X)
        self.Xnum=X.shape[1]
        bias=np.ones((self.height,1),dtype=np.int32)
        X.insert(0,'bias',bias)
        self.X=np.mat(X)
        self.Y=np.mat(Y)

    def data_num(self):
        return self.height
    
    def x_num(self):
        return self.Xnum

    def conversion(self,matrix):
        return np.transpose(matrix)
    
    def inverse(self,matrix):
        return matrix.I
    
    def multiplication(self,A,B):
        return np.dot(A,B)

    def best_theta(self):
        X_t=self.conversion(self.X)
        X_tX=self.multiplication(X_t,self.X)
        X_tX_I=self.inverse(X_tX)
        X_tY=self.multiplication(X_t,self.Y)
        theta=self.multiplication(X_tX_I,X_tY)
        return theta
    
    def Y_(self):
        theta=self.best_theta()
        Y_=self.multiplication(self.X,theta)
        return Y_

    def avgY(self):
        avgy=self.Y.sum()/self.height
        avgY=np.ones((self.height,1))*avgy
        return avgY
    
    def Q(self):
        Y_=self.Y_()
        Y=self.Y
        Q=pow(np.linalg.norm(Y-Y_),2)
        return Q

    def U(self):
        Y_=self.Y_()
        avgY=self.avgY()
        U=pow(np.linalg.norm(Y_-avgY),2)
        return U
    
    
    # def best_Y_(self,F_1_a):

    
    def print_line_chart(self):
        plt.figure()
        x=np.arange(1,self.data_num()+1,1)
        y1=self.conversion(self.Y_()).tolist()[0]
        y2=self.conversion(self.Y).tolist()[0]
        plt.plot(x,y1,color='r',label='estimate value')
        plt.plot(x,y2,color='g',label='original')
        plt.xlabel('player')
        plt.ylabel('score')
        plt.legend()
        plt.show()


