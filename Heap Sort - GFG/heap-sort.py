#User function Template for python3

class Solution:
    def swap(self,arr,i1,i2):
        arr[i1], arr[i2] = arr[i2], arr[i1]
        
    def left_child(self,arr, i):
        return(2*i + 1)
        
    def right_child(self,arr, i):
        return(2*i + 2)
        
    def parent(self,arr, i):
        return (i-1)//2
        
    def insert(self,arr, val):
        arr.append(val)
        self.heapify(arr,len(arr)-1)
        
    def remove(self,arr,n, i):
        self.swap(arr, i, n)
        self.heapifydown(arr, n, i)
        return
    def modify(self,arr, i, val):
        arr[i] = val
        self.heapify(arr,i)
        
    def get_min(self,arr,n):
        return arr[0]
    
    #Heapify function to maintain heap property.
    def heapifydown(self,arr,n,i):
        l_child = self.left_child(arr,i) 
        r_child = self.right_child(arr,i) 
        
        if l_child >= n:  
            l_child = i
        
        if r_child >= n:
            r_child = i
            
        maxi = max(arr[l_child], arr[r_child])
        
        if arr[i] < maxi:
            while i <= n and arr[i] < maxi:
                
                if arr[l_child] > arr[r_child]:
                    self.swap(arr,i,l_child)
                    i = l_child
                else:
                    self.swap(arr,i,r_child)
                    i = r_child
                    
                l_child = self.left_child(arr,i) 
                r_child = self.right_child(arr,i)
                
                if l_child >= n:  
                    l_child = i
        
                if r_child >= n:
                    r_child = i
                    
                maxi = max(arr[l_child],arr[r_child])
            
            return
        
    def heapify(self,arr, n, i):
        par = self.parent(arr,i)
        
        if par >= 0 and arr[i] > arr[par]:
            while par >= 0 and arr[i] > arr[par]:
                self.swap(arr, i, par)
                i = par
                par = self.parent(arr,i)
        return
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(len(arr)):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        
        for i in range(len(arr)):
            self.remove(arr,n-1, 0)
            n -= 1
            
            if  n == 1:
                break

        return
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends