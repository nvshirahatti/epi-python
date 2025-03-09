# O(n) time | O(1) space
def dutch_flag_partition(A):
   low, mid, high = 0, 0, len(A) - 1
   while(mid <= high):
       if A[mid] == 0:
           A[low], A[mid] = A[mid], A[low]
           low += 1
           mid += 1
       elif A[mid] == 1:
           mid += 1
       else:
           A[mid], A[high] = A[high], A[mid]
           high -= 1
   return A

if __name__ == "__main__":
    A = [0, 1, 2, 0, 2, 1, 1, 0, 2, 0]
    dutch_flag_partition(A)
    print(A)
