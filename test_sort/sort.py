def selectSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx = j
        
        arr[i],arr[min_idx] = arr[min_idx],arr[i]      
    return arr

def bubbleSort(arr):
    n = len(arr)
    for i  in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def main():
    a = [1,6,5,2,8,9]
    print(selectSort(a[:]))  
    print(sorted(a[:]))

if __name__ == "__main__":
    main()