def binary_search(array):
    low=0
    high= len(array)-1

    while(low<=high):
        mid=(low+high)//2

        if mid<len(array)-1 and array[mid]>array[mid+1]:
            return mid+1
        
        if array[mid]<array[]




if __name__=="__main__":
    array=[1,2,3,4,5]
    print(binary_search(array))