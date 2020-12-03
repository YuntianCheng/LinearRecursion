from dealCsv import *
from LinearRecursion import *
import pandas as pd
import math


if __name__ == "__main__":
    fileAdr='./statistics/train2.csv'
    deal = dealCsv(fileAdr)
    header=deal.header()
    header.remove('y')
    X=deal.data_by_index(header)
    Y=deal.data_by_index(['y'])
    lr=LR(X,Y)
    lr.print_line_chart()

    beta=lr.best_theta()
    for i in range(0,len(beta)):
        print('beta'+str(i)+'=',beta[i,0])

    
    

    n=lr.data_num()
    p=lr.x_num()
    n_p_1=n-p-1
    Q=lr.Q()
    U=lr.U()
    sigma_=math.sqrt(Q/n_p_1)
    X_t=lr.conversion(lr.X)
    C=lr.inverse(lr.multiplication(X_t,lr.X))
    print('size of data is',n)
    print('num of x is',p)
    for i in range(1,p+1):
        betai=beta[i,0]
        sqrtCii=math.sqrt(C[i,i])
        num3=sigma_*sqrtCii
        ti=betai/num3
        absTi=abs(ti)
        print('|t'+str(i)+'|=',absTi,absTi>1.960266)
    for i in range(1,p+1):
        betai=beta[i,0]
        betai_2=pow(betai,2)
        sigma_2=Q/n_p_1
        cii=C[i,i]
        F_i=betai_2/(sigma_2*cii)
        print('F'+str(i)+'=',F_i,F_i>=3.842643)
    
    


    # print('Beta=',pd.DataFrame(beta))
    # print('Q=',Q)
    # print('U=',U)
    # print('F=',F_p_np1)


    # print('Q=',Q)
    # print('U=',U)
    # num1=n_p_1/p
    # num2=U/Q
    # F_p_np1=num1*num2


    # for i in range(1,p+1):
    #     betai=beta[i,0]
    #     sqrtCii=math.sqrt(C[i,i])
    #     num3=sigma_*sqrtCii
    #     ti=betai/num3
    #     absTi=abs(ti)
    #     print(absTi)

        

    

