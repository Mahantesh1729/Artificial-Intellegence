def main():
    n=int(input("Enter the size of the n X n matrix: "))

    print("Enter the initial state of the matrix: \n")

    matrix = []

    for i in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)

    clean_initial_state(n ,matrix)

    while True:
        dx, dy = list(map(int, input("Enter the position to be inspected: \n").split()))
        dirt = input('does that cell have dirt: ')
        if dirt in ["yes", "Yes"]:
            matrix[dx][dy] = 1
        vx, vy = list(map(int, input("Enter the postion of vacuum cleaner: \n").split()))
        matrix[vx][vy] = 'v'
        print_matrix(matrix)
        while dx > vx:
            matrix[vx][vy] = 0
            vx += 1
            matrix[vx][vy] = 'v'
            print_matrix(matrix)

        while dy > vy:
            matrix[vx][vy] = 0
            vy += 1
            matrix[vx][vy] = 'v'
            print_matrix(matrix)

        while dx < vx:
            matrix[vx][vy] = 0
            vx -= 1
            matrix[vx][vy] = 'v'
            print_matrix(matrix)
        
        while dy < vy:
            vy -= 1
            matrix[vx][vy] = 'v'
            print_matrix(matrix)

        if input("Do you want to continue: ") not in ["y", "yes"]:
            break
        
        
def clean_initial_state(n, matrix):
    
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                if matrix[i][j] != 0:
                    print(f"dirt found at pos ({i}, {j})")
                    matrix[i][j] = 0
                    print_matrix(matrix)
        else:
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    print(f"dirt found at pos ({i}, {j})")
                    matrix[i][j] = 0
                    print_matrix(matrix)
                    
                    
    
def print_matrix(matrix):

    for i in matrix:
        print(i)




main()
