import time

def merge_sort(A):
    if len(A) < 2:
        return
    
    m = len(A) // 2 
    print("Divide Array")
    ax = A[0:m]
    print(ax)
    ay = A[m:len(A)]
    print(f"{ay}\n")
    time.sleep(1.5)

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

    print("Welcome to Arvin's merge sort visualizer!\n")
    i = 0
    while True:
        try:
            n = int(input("Enter the number of items: "))
            break
        except ValueError:
            print("Error: Input must be an integer.")
        
    A = [0] * n 

    while True:
        try:    
            if i < n:
                user_input = int(input(f"Item {i+1}:"))
                A[i] = user_input
                i += 1    
            else:
                break    
        except ValueError:
            print("Error: Input must be an integer.")
            
    merge_sort(A)
    print(A)
    
if __name__=='__main__': 
    main()