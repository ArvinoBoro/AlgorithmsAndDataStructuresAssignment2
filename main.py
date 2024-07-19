def merge_sort(A):
    if len(A) < 2:
        return
    
    m = len(A) // 2 
    ax = A[0:m]
    ay = A[m:len(A)]

    merge_sort(ax)
    merge_sort(ay)

    merge(A, ax, ay)


def merge(A, ax, ay):
    i = 0
    j = 0 
    while i + j < len(A):
        if j == len(ay) or (i < len(ax) and ax[i] < ay[j]):
            A[i+j] = ax[i]
            i += 1 
        else:
            A[i+j] = ay[j]
            j += 1 


def main():

    A = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    merge_sort(A)
    print(A)
    
if __name__=='__main__': 
    main()