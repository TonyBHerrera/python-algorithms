def sum1(n):
    final_sum = 0 
    for x in range(n+1):
        final_sum+= x

        return final_sum

def sum2(n):
    return(n *(n + 1))/2


def Bigo(n):
    return 45*n**3 + 20*n**2 + 19
Bigo(1)    

from math import log
import numpy as np 
import matplotlib.pyplot as plt 
%matplotlib inline
plt.style.use('bmh')

# Set up runtime comparisons
n = np linspace(1,10)
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponntial']
big_o = [np.onces(n.shape),np.log(n),n,n*np.log(n),n**2,n**3,2**n]

# Plot setup
plt.figure(figsize=(12,10))
plt.ylim(0,50)

for i in range(len(big_o)):
    plt.plot(n,big_o[i],label = labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')    

def func_constant(values):
"""
Takes in list and prints out all values
"""
    print(values[0])
func_constant([1,2,3,4,5,6,7,8,9,10])    


def func_line(lst):
    for val in lst:
        print(val)

func_lin([1,2,3])

def func_quad(lst):

    for item_1 in lst:
        for item_2 in lst:
            print (item_1,item_2)

lst = [1,2,3,4,5,6]

func_quad(lst)

def print_once(lst):

    for val in lst:
        print(val)

print_once(lst)

def print_3(lst):

    for val in lst:
        print(val)

    for val in lst:
        print(val)    

    for val in lst:
        print(val)        


pirnt_3(lst)        



def comp(lst):
     """
     this cuntion prints the first item 0(1) it is a constant
     Then is prints the first 1/2 of the list 0(n/2)
     Then prints a string 10 times 0(10) it is a constant
     """
     print (lst[0])

     midpoint = len(lst)

    for val in lst[:midpoint]:
         print (val)

    for x in range(10):
        print("nubmer")


def matcher(lst,match):
    """
    Given a list lst, return a boolean indicating if match item is in the list
    """
    for item in lst:
        if item == match:
            return True
    return False         

def memory(n=10):
    # Prints "hello world" n times

    for x in range(n):
        print('Memory')

memory(10)        