import numpy as np 


def linear_cost(theta,x,y):
    m,n=x.shape
    h = np.matmul(x,theta)
    sq = (h-y)
    return np.matmul(sq,m)