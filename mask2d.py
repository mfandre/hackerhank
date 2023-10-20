#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

mask_m = 3
mask_n = 3
mask = [[1,1,1],    #(0,0), (0,1), (0,2)
        [0,1,0],    #(1,0), (1,1), (1,2)
        [1,1,1]]    #(2,0), (2,1), (2,2)
                  
# 6-3+1 = 4
# 6-5+1 = 2

arr_m = 6
arr_n = 6

def getValue(arr, i,j):
    return arr[i][j]
    
def indexIsAllowToMask(i,j):
    min_allowed_m = int((mask_m-1)/2)
    max_allowed_m = arr_m - min_allowed_m

    min_allowed_n = int((mask_n-1)/2)
    max_allowed_n = arr_n - min_allowed_n
    
    alloweds_i = range(min_allowed_m, max_allowed_m)
    alloweds_j = range(min_allowed_n, max_allowed_n)
    
    #print(alloweds_i)

    if i in alloweds_i and j in alloweds_j:
        return True
    
def applyMask(arr, arr_i, arr_j):
    #essa funçao está errada para mascaras maiores que 3!
    temp = []
    sum = 0
    for i in range(0, mask_m):
        if i < int((mask_m-1)/2):
            fix_i = arr_i - (i + 1)
        else:
            fix_i = arr_i + (i - 1)
        temp_l = []
        for j in range(0, mask_n):
            if j < int((mask_n-1)/2):
                fix_j = arr_j - (j + 1)
            else:
                fix_j = arr_j + (j -1)
            temp_l.append((fix_i,fix_j))
            print(f"arr={arr_i}, {arr_j}")
            print(f"fix_i={fix_i}")
            print(f"fix_j={fix_j}")
            #print(f"arr_fix={arr_i+fix_i}, {arr_j+fix_j} = {arr[arr_i+fix_i][arr_j+fix_j]}")
            sum += arr[fix_i][fix_j]*mask[i][j]
            print(f"sum={sum} ({arr_i}, {arr_j})")
            print(f"----")
        temp.append(temp_l)
    print(temp)
    print("####")
    return sum
    
def hourglassSum(arr):
    print(len(arr))
    max_sum = -9999999
    for i in range(0,arr_m):
        for j in range(0,arr_n):
            if indexIsAllowToMask(i,j):
                temp_sum = applyMask(arr, i,j)
                if temp_sum > max_sum:
                   max_sum = temp_sum
    return max_sum       

def main():
    arr = [
        [-9, -9, -9,  1, 1, 1],
        [0, -9,  0,  4, 3, 2], # (1,1) (1,4) => mask3 (3-1/2)(6-3+1)
        [-9, -9, -9,  1, 2, 3], # (2,2) (2,3) => mask5
        [0,  0,  8,  6, 6, 0], # (3,2) (3,3) => mask5
        [0, 0, 0, -2, 0, 0], # (4,1) (4,4) => mask3
        [0, 0, 1, 2, 4, 0]
    ]

    arr2 = [[1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]] # 19
    

    arr3 = [[0, -4, -6, 0, -7, -6],
            [-1, -2, -6, -8, -3, -1],
            [-8, -4, -2, -8, -8, -6],
            [-3, -1, -2, -5, -7, -4],
            [-3, -5, -3, -6, -6, -6],
            [-3, -6, 0, -8, -6, -7]]

    print(f"=> {hourglassSum(arr3)}")

# The 16 hourglass sums are:

# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18

if __name__ == "__main__":
    main()