if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)#convert to set so that it don't contain duplicates
    arr2 = sorted(arr1)
    print(arr2[-2])
    #print(arr2[n-2]) wont work as length of set might be different
