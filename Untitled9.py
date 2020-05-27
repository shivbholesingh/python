
# coding: utf-8

# # linear search:
# 

# In[ ]:

def linear_search(array,target):
    for i in range(len(array)):
        if target==array[i]:
            return i
    return None
array=list(map(int,input().split()))
target=int(input())
data=linear_search(array,target)
if data is not None:
    print('Value {} found at position {} using linear search'.format(target, data+1))

else:
    print("data is not found")
            
                    
    


# # binary search

# In[1]:

def binary_search(array,target):
    left=0
    right=len(array)-1
    
    while(left<=right):
        
        mid=(right+left)//2
        
        if(target==array[mid]):
            return mid
        
        elif(target>array[mid]):
            left=mid+1
            
        else:
            right= mid-1
    return None

array=list(map(int,input().split()))

array=sorted(array)

target=int(input())
data=binary_search(array,target)
if data is not None:
    print('Value {} found at position {} using linear search'.format(target, data+1))
else:
    print("data is not found")


# In[ ]:



