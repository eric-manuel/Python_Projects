A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
n = 3
for i in range(1, n):
     for j in range(i+1, n):
          temp = A[i][j]
          A[i][j] = A[j][i]
          A[j][i] = temp

for i in range(n):
     for j in range(n):
          print(A[i][j], end="")
     print()
    