def rotate90Clockwise(A):
    N = len(A[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp 
            
def reflectMatrixMain(mat):
    n = len(mat)
    for i in range(n): 
        for j in range(i + 1): 
            t = mat[i][j]; 
            mat[i][j] = mat[j][i] 
            mat[j][i] = t


def mutateMatrix(a, q):
    for x in q:
        if x == 0:
            rotate90Clockwise(a)
            #rotate natrix 90 degrees clockwise
        if x == 1:
            #reflect matrix in its main diagonal
            reflectMatrixMain(a)
        if x == 2:
            #reflect matrix in its secondary diagonal
            rotate90Clockwise(a)
            rotate90Clockwise(a)
            reflectMatrixMain(a)
        
    return a
            

