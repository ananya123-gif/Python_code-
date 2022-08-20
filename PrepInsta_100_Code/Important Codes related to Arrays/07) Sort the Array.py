# Sort the Array
# Input : arr = [10, 40, 20, 30]
# Output : In ascending order = 10 20 30 40
#          In descending order = 40 30 20 10

def sort_array(arr):
    arr.sort()
    print("Ascending Order =",*arr)
    arr.sort(reverse=True)
    print("Descending Order =",*arr)

arr=list(map(int,input().split(" ")))
sort_array(arr)
