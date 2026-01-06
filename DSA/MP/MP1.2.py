# ERIC MANUEL MANZANERO
# BSCPE 2A
# MP #2
# PROGRAM USING 2D ARRAY
# PROBLEM: 
#     CREATE A PROGRAM THAT SOLVES SYSTEM OF LINEAR EQUATIONS USING CRAMER'S RULE
# INSPIRATION FOR CREATING THIS PROGRAM:
#     MY INSPIRATION FOR CREATING THIS PROGRAM IS TO SOLVE SYSTEM OF LINEAR EQUATIONS IN KIRCHHOFF'S LAW

# FUNCTION THAT COMPUTES DETERMINANT FOR 2X2 MATRIX
def twoByTwo(a,b,c,d):
    det = (a*d)-(b*c)
    return det 
# FUNCTION THAT COMPUTES DETERMINANT FOR 3X3 MATRIX
def threeByThree(a,b,c,d,e,f,g,h,i):
    A = a*(twoByTwo(e,f,h,i))
    B = b*(twoByTwo(d,f,g,i))
    C = c*(twoByTwo(d,e,g,h))
    return (A)-(B)+(C)
# FUNCTION THAT COMPUTES DETERMINANT FOR 4X4 MATRIX
def fourByFour(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    A = a*(threeByThree(f,g,h,j,k,l,n,o,p))
    B = b*(threeByThree(e,g,h,i,k,l,m,o,p))
    C = c*(threeByThree(e,f,h,i,j,l,m,n,p))
    D = d*(threeByThree(e,f,g,i,j,k,m,n,o))
    return (A)-(B)+(C)-(D)

import numpy as np # USING NUMPY IN CREATING ARRAYS

# MAIN FUNCTION
def main():
    print("This program solves system of linear equations using Cramer's Rule")
    print("To use this program convert first the system of equations in matrix form")
    print("The maximum order of matrix in this program is 4x4\n")
    print("Enter the order of the matrix")
    R = int(input("R: "))# R MEANS ROW
    C = int(input("C: "))# C MEANS COLUMN

    matrix = np.full((R,C), 0, dtype='float64')# INITIALIZE AN ARRAY WITH ZEROES
    print("\nMatrix:\n", matrix, "\n")
    
    # LOOPS THAT TAKES INPUT FOR EACH ELEMENTS IN THE MATRIX 
    for i in range(R):
        for j in range(C):
            e = float(input(f"Enter elemenent in Row{i},Column{j}: "))
            matrix[i,j] = e
        
    print("\nMatrix:\n", matrix)
    
    # SOLVE THE VALUES OF X AND Y IF THE MATRIX IS 2X3
    if R == 2:
        D = twoByTwo(matrix[0,0], matrix[0,1], 
                     matrix[1,0], matrix[1,1])
        Dx = twoByTwo(matrix[0,2], matrix[0,1], 
                      matrix[1,2], matrix[1,1])
        Dy = twoByTwo(matrix[0,0], matrix[0,2], 
                      matrix[1,0], matrix[1,2])
        
        x = Dx/D
        y = Dy/D
        
        print("\nx = ", x,)
        print("y = ", y)
        
    # SOLVE THE VALUES OF X, Y AND Z  IF THE MATRIX IS 3X4
    elif R == 3:
        D = threeByThree(matrix[0,0], matrix[0,1], matrix[0,2], 
                         matrix[1,0], matrix[1,1], matrix[1,2], 
                         matrix[2,0], matrix[2,1], matrix[2,2])
        
        Dx = threeByThree(matrix[0,3], matrix[0,1], matrix[0,2], 
                          matrix[1,3], matrix[1,1], matrix[1,2], 
                          matrix[2,3], matrix[2,1], matrix[2,2])
        
        Dy = threeByThree(matrix[0,0], matrix[0,3], matrix[0,2], 
                          matrix[1,0], matrix[1,3], matrix[1,2], 
                          matrix[2,0], matrix[2,3], matrix[2,2])
        
        Dz = threeByThree(matrix[0,0], matrix[0,1], matrix[0,3], 
                          matrix[1,0], matrix[1,1], matrix[1,3], 
                          matrix[2,0], matrix[2,1], matrix[2,3])
    
        x = Dx/D
        y = Dy/D
        z = Dz/D
        
        print("\nx = ", x,)
        print("y = ", y)
        print("z = ", z)
        
    # SOLVE THE VALUES OF X, Y, Z AND A  IF THE MATRIX IS 4X5 
    elif R == 4:
        D = fourByFour(matrix[0,0], matrix[0,1], matrix[0,2], matrix[0,3],
                       matrix[1,0], matrix[1,1], matrix[1,2], matrix[1,3],
                       matrix[2,0], matrix[2,1], matrix[2,2], matrix[2,3],
                       matrix[3,0], matrix[3,1], matrix[3,2], matrix[3,3])
        
        Dx = fourByFour(matrix[0,4], matrix[0,1], matrix[0,2], matrix[0,3],
                        matrix[1,4], matrix[1,1], matrix[1,2], matrix[1,3],
                        matrix[2,4], matrix[2,1], matrix[2,2], matrix[2,3],
                        matrix[3,4], matrix[3,1], matrix[3,2], matrix[3,3])
        
        Dy = fourByFour(matrix[0,0], matrix[0,4], matrix[0,2], matrix[0,3],
                        matrix[1,0], matrix[1,4], matrix[1,2], matrix[1,3],
                        matrix[2,0], matrix[2,4], matrix[2,2], matrix[2,3],
                        matrix[3,0], matrix[3,4], matrix[3,2], matrix[3,3])
        
        Dz = fourByFour(matrix[0,0], matrix[0,1], matrix[0,4], matrix[0,3],
                        matrix[1,0], matrix[1,1], matrix[1,4], matrix[1,3],
                        matrix[2,0], matrix[2,1], matrix[2,4], matrix[2,3],
                        matrix[3,0], matrix[3,1], matrix[3,4], matrix[3,3])
        
        Da = fourByFour(matrix[0,0], matrix[0,1], matrix[0,2], matrix[0,4],
                        matrix[1,0], matrix[1,1], matrix[1,2], matrix[1,4],
                        matrix[2,0], matrix[2,1], matrix[2,2], matrix[2,4],
                        matrix[3,0], matrix[3,1], matrix[3,2], matrix[3,4]) 
        
        x = Dx/D
        y = Dy/D
        z = Dz/D
        a = Da/D
        
        print("\nx = ", x,)
        print("y = ", y)
        print("z = ", z)
        print("a = ", a)
        
main()