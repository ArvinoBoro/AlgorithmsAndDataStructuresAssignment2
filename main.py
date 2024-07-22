import time
from playsound import playsound

underline_start = '\033[4m'
underline_end = '\033[0m'

def merge_sort(A, level=0):
    print(f"\n{level * '  '}merge_sort({A})")
    print(f"{level * '  '}A = {A}")

    if len(A) < 2:
        print(f"{level * '  '}Length of A < 2.")
        return
    print(f"{level * '  '}Length of A ≥ 2.")
    
    m = len(A) // 2 
    print(f"{level * '  '}Divide A as evenly as possible.")
    a1 = A[:m]
    print(f"{level * '  '}a1 = {a1}")
    a2 = A[m:]
    print(f"{level * '  '}a2 = {a2}")

    merge_sort(a1, level + 1)
    merge_sort(a2, level + 1)

    merge(A, a1, a2, level)

def merge(A, a1, a2, level):
    print(f"\n{level * '  '}merge({A}, {a1}, {a2})")
    print(f"{level * '  '}A = {A}")
    print(f"{level * '  '}a1 = {a1}")
    print(f"{level * '  '}a2 = {a2}")
    i = 0
    j = 0 
    while i + j < len(A):
        print(f"\n{level * '  '}i = {i}")
        print(f"{level * '  '}j = {j}")
        if j == len(a2):
            print(f"{level * '  '}j = Length of a2")
            A[i+j] = a1[i]
            i += 1 
        elif i < len(a1) and a1[i] < a2[j]:
            print(f"{level * '  '}j ≠ Length of a2")
            print(f"{level * '  '}i < Length of a1")
            print(f"{level * '  '}a1[i] < a2[j]")
            A[i+j] = a1[i]
            i += 1
        else:
            print(f"{level * '  '}j ≠ Length of a2")
            if i >= len(a1):
                print(f"{level * '  '}i ≥ Length of a1")
            elif a1[i] >= a2[j]:
                print(f"{level * '  '}a1[i] ≥ a2[j]")
            A[i+j] = a2[j]
            j += 1 
        
        print(f"{level * '  '}[", end='')
        for k in range(len(A)):
            if k == i + j - 1:
                print(f"{underline_start}{A[k]}{underline_end}", end='')
            else:
                print(f"{A[k]}", end='')
            if k < len(A) - 1:
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