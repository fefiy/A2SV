class Solution: 
    def select(self, arr, i):
        # code here 
        for k in range(i,len(arr)):
            minindex = k #
            for j in range(k+1, len(arr)):
                if arr[j] < arr[minindex]:
                    minindex = j

            arr[k], arr[minindex] = arr[minindex], arr[k]

        return arr
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minindex = i  #
            for j in range(i+1, n):
                if arr[j] < arr[minindex]:
                    minindex = j

            arr[i], arr[minindex] = arr[minindex], arr[i]

        return arr
