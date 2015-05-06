# -*- coding:utf8 -*-  
import os  
import sys  
import math  
  
def halfSearch(arr=[1,2,3,4,5],find = 1):  
    mid=0  
    low=0   
    high=len(arr)+1  
    while(low<=high):  
        print(low,high)  
        mid=(low + high)/2  
        print(mid)  
        if(arr[mid]==find):  
            print ("find %s index is %s",find,mid)  
            return  
        else:  
            if(find > arr[mid]):  
                low = mid + 1  
            else:  
                high = mid - 1  
    print ("Not Find")  
    return None  
      
  
if __name__ =="__main__":  
    halfSearch()  
