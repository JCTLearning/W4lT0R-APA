import numpy as n
#sigmoid func
#used to make the weights no linear (sigmoid is curved)
def nonlin(x,deriv = False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+n.exp(-x))
#input
x = n.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
#output
y = n.array([[0,0,1,1]]).T

#seed random numbers to make calculation
n.random.seed(1)

#init synaptic weights randomly with mean of 0
syn0 = 2*n.random.random((3,1)) - 1
for iter in range(10000):
    #foward prop
    l0 = x
    l1 = nonlin(n.dot(l0,syn0))

    #how much we missed
    l1_error = y - l1
    #what we missed * slope of sigmoid
    l1d = l1_error * nonlin(l1, True)

    #update synaptic weights
    syn0 += n.dot(l0.T,l1d)
print("Output after synaptic training:")
print(l1)
#The weights never change, this signifies the actual connection of the neural networks nodes.
