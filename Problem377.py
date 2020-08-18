# Author : Demetrios Lambropoulos
# DP: 377
# Asked By: Microsoft 
#
# Given an array of numbers arr and a window of size k, print out the median of each 
# window of size k starting from the left and moving right by one position each time.
#
# For example, given the following array and k = 3:
#
# [-1, 5, 13, 8, 2, 3, 3, 1]
#
# Your function should print out the following:
#
# 5 <- median of [-1, 5, 13]
# 8 <- median of [5, 13, 8]
# 8 <- median of [13, 8, 2]
# 3 <- median of [8, 2, 3]
# 3 <- median of [2, 3, 3]
# 3 <- median of [3, 3, 1]
#
# Recall that the median of an even-sized list is the average of the two middle numbers. 

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]
Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
Recall that the median of an even-sized list is the average of the two middle numbers.

def myMedian(arr):
    if (len(arr) == 0):
        return
    elif (len(arr) == 1):
        return arr[0]
    else:
        # Sort array elements
        x = sorted(arr)

        n = int(len(x)/2)

        # Find median
        if (len(x)%2 == 0):
            return (x[n] + x[n-1])/2
        else:
            return x[n]

a = [-1, 5, 13, 8, 2, 3, 3, 1]

k = 3

for i in range(0+int(k/2), len(a)-int(k/2)):
    tmp = a[i-int(k/2):i+int(k/2)+1]
    print(myMedian(tmp), "<- median of ", tmp)