from dealCsv import *
from LinearRecursion import *
import pandas as pd
import math


if __name__ == "__main__":
    fileAdr='./statistics/train.csv'
    deal = dealCsv(fileAdr)
    header=deal.header()
    header.remove('y')
    X=deal.data_by_index(header)
    Y=deal.data_by_index(['y'])
    lr=LR(X,Y)

    beta=lr.best_theta()
    n=lr.data_num()
    p=lr.x_num()
    n_p_1=n-p-1
    Q=lr.Q()
    U=lr.U()
    sigma_=math.sqrt(Q/n_p_1)
    X_t=lr.conversion(lr.X)
    C=lr.inverse(lr.multiplication(X_t,lr.X))

    print('回归系数ß的估计为：',pd.DataFrame(beta))
    print('残差平方和为：',Q)
    print('离差平方和为：',U)

    num1=n_p_1/p
    num2=U/Q
    F_p_np1=num1*num2
    print('F=',F_p_np1)


    for i in range(1,p+1):
        betai=beta[i,0]
        #print('betai=',betai)
        sqrtCii=math.sqrt(C[i,i])
        #print(sqrtCii)
        num3=sigma_*sqrtCii
        #print(num3)
        absTi=betai/num3
        print('absTi=',absTi)

        

    

