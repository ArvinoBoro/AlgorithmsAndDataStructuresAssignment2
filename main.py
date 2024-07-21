import time

underline_start = '\033[4m'
underline_end = '\033[0m'


def merge_sort(A):
    print(f"\nmerge_sort({A})")
    print(f"A = {A}")

    if len(A) < 2:
        print("Length of A < 2.")
        return
    print("Length of A ≥ 2.")
    
    m = len(A) // 2 
    print("Divide A as evenly as possible.")
    a1 = A[0:m]
    print(f"a1 = {a1}")
    a2 = A[m:len(A)]
    print(f"a2 = {a2}")

    merge_sort(a1)
    merge_sort(a2)

    merge(A, a1, a2)

def merge(A, a1, a2):
    print(f"\nmerge({A}, {a1}, {a2})")
    print(f"A = {A}")
    print(f"a1 = {a1}")
    print(f"a2 = {a2}")
    i = 0
    j = 0 
    while i + j < len(A):
        print(f"\ni = {i}")
        print(f"j = {j}")
        if j == len(a2):
            print("j = Length of a2")
            A[i+j] = a1[i]
            i += 1 
        elif i < len(a1) and a1[i] < a2[j]:
            print(f"j ≠ Length of a2")
            print(f"i < Length of a1")
            print(f"a1[i] < a2[j]")
            A[i+j] = a1[i]
            i += 1
        else:
            print(f"j ≠ Length of a2")
            if i >= len(a1):
                print(f"i ≥ Length of a1")
            elif a1[i] >= a2[j]:
                print(f"a1[i] ≥ a2[j]")
            A[i+j] = a2[j]
            j += 1 
        
        print("[", end='')
        for k in range(len(A)):
            if k == i+j-1:
                print(f"{underline_start}{A[k]}{underline_end}", end='')
            else:
                print(f"{A[k]}", end='')
            if k < len(A)-1:
                print(", ", end='')
        print("]")

def main():
    print("Welcome to Arvin's merge sort visualizer!\n")
    while True:
        try:
            n = int(input("Enter the number of items: "))
            break
        except ValueError:
            print("Error: Input must be an integer.")
        
    A = [0] * n 

    i = 0
    while i < n:
        try:
            user_input = int(input(f"Item {i+1}: "))
            A[i] = user_input
            i += 1    
        except ValueError:
            print("Error: Input must be an integer.")
    
    merge_sort(A)
    print(f"\nSorted array: {A}")

if __name__ == '__main__': 
    main()