import numpy as np
import math

###_____________________PYTHON_FUNCTION_________________________###

n = int(input("Nhập số đỉnh của đồ thị:"))
def adjacency_matrix(n):
    adjacency_matrix = []
    for row in range(n):
        adjacency_matrix.append([])
        for column in range(n):
            place = int(input("Phần tử thứ djacency_matrix[%2d][%2d]:" % (row+1, column+1)))
            adjacency_matrix[row].append(place)

    # 0 là ko có đường đi và 1 là có đường đi, ex: a12 = 1 tức là có cạnh nối đỉnh 1 và đỉnh 2 :)))
    return np.array(adjacency_matrix)
def position_counter(n):        # Mặc định đỉnh đầu tiên của chu trình là đỉnh 1.
    arr_position_counter = np.full(n+1,0)
    arr_position_counter[0] = 1
    return arr_position_counter

def print_Hamilton(arr_position_counter):
    print("Chu trình Hamilton: ", end=' ')
    for i_ in range(len(arr_position_counter)):
        if i_ < len(arr_position_counter) - 1:
            print(arr_position_counter[i_],end=' => ')
        if i_ >= len(arr_position_counter) - 1:
            print(arr_position_counter[i_])

###____________________________________________________________________________###

count = 0
arr_position_counter = position_counter(n)
adjacency_matrix = adjacency_matrix(n)
def Backtracking_hamilton_process(adjacency_matrix, arr_position_counter, n, count):
    for idx_ in range(n):
        if ((count<n-1) and (adjacency_matrix[arr_position_counter[count]-1][idx_] == 1) and (((idx_+1) in arr_position_counter)==False )) or ((count>=n-1) and (adjacency_matrix[arr_position_counter[count]-1][idx_] == 1)):
            arr_position_counter[count+1] = idx_ + 1 
            if count < n-1:
                Backtracking_hamilton_process(adjacency_matrix, arr_position_counter, n, count+1)
            else:
                if arr_position_counter[count+1] == arr_position_counter[0]:
                    print_Hamilton(arr_position_counter)
            arr_position_counter[count+1] = 0
    return 'Chương trình đã thực hiện xong!!!!Ahihiii!!!'
    
print(adjacency_matrix)
print(Backtracking_hamilton_process(adjacency_matrix, arr_position_counter, n, count))