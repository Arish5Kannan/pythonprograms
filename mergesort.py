def merge(arr,l,mid,r):
    n1 = mid-l+1
    n2 = r-mid
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0,n1):
        L[i] = arr[l +i]
    for j in range(0,n2):
        R[j] = arr[mid+1+j]
    i = 0
    j = 0
    k = l
    while i<n1 and j<n2:
        if L[i]<= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i< n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr,l,r):
    if l<r:
        mid = l+(r-l)//2
        mergesort(arr,l,mid)
        mergesort(arr,mid+1,r)
        merge(arr,l,mid,r)

