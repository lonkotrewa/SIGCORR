# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:15:31 2016

@author: AlvaroG (gonzalezreyesalvaro@gmail.com)
"""


def QT(x,y):
    from scipy import stats
    r=stats.t.ppf(x,y);  ## degrees of Fredom 
    return(r)   
    
def SIGCORR(x, y):
    from math import sqrt
    RES = range(x,y+1)
    T=len(RES)
    df=(T-2)
    ##### p-values
    P1=0.10
 ### P 0.10
    pbb1=(1-(P1/2))
    probb1=(1-P1)*100
    TT1 = QT(pbb1,df);
    denom1=sqrt(df+(TT1**2))
    RR1 =round((TT1/denom1),4); ### critical pearson r at 90 %
### P 0.05
    P2=0.05
    pbb2=(1-(P2/2))
    probb2=(1-P2)*100
    TT2 = QT(pbb2,df);
    denom2=sqrt(df+(TT2**2))
    RR2 =round((TT2/denom2),4); ### critical pearson r at 95 %
### P 0.01
    P3=0.01
    pbb3=(1-(P3/2))
    probb3=(1-P3)*100
    TT3 = QT(pbb3,df);
    denom3=sqrt(df+(TT3**2))
    RR3 =round((TT3/denom3),4); ### critical pearson r at 99 %    
### P 0.001
    P4=0.001
    pbb4=(1-(P4/2))
    probb4=(1-P4)*100
    TT4 = QT(pbb4,df);
    denom4=sqrt(df+(TT4**2))
    RR4 =round((TT4/denom4),4); ### critical pearson r at 99 %        
    EE = 'The correlation between {} - {} years are significant at {}% of CL when r = ± {}, at {}% for r = ± {}, at {}% for r = ± {} and at {}% for r = ± {}. Buena suerte huacho !!'.format(x, y, probb1, RR1, probb2, RR2,probb3, RR3,probb4, RR4)
    print(EE)
### PROBLEMAS CON LA ENTRADA DE DATOS: ARREGLAR 

def visor():
    x = int(input("Start year: "))
    y = int(input("End year: "))    
    SIGCORR(x, y)

visor() 



