import math
while True:
    print('This is program can help with matrix calculation')
    print('Choose that you want to do:')
    print('1) Calculate the determinant of the matrix')
    print('2) Find the matrix of algebraic complements')
    print("3) Find the minor of matrix's element")
    user_input = int(input('Choose: '))
    if user_input == 1:
        print('Now you can choose det of matrix: ')
        n = int(input('Choose det 1, 2 or 3: '))
        if n == 1:
            a11 = int(input('Enter a11:'))
            A = a11
            print(A)
            if A == 0:
                print('Degenerate')
            else:
                print('Nondegenerate')
        if n == 2:
            a11 = int(input('Enter a11:'))
            a12 = int(input('Enter a12:'))
            a21 = int(input('Enter a21:'))
            a22 = int(input('Enter a22:'))
            A = a11*a22 - a12*a21
            print(A)
            if A == 0:
                print('Degenerate')
            else:
                print('Nondegenerate')
        if n == 3:
            a11 = int(input('Enter a11:'))
            a12 = int(input('Enter a12:'))
            a13 = int(input('Enter a13:'))
            a21 = int(input('Enter a21:'))
            a22 = int(input('Enter a22:'))
            a23 = int(input('Enter a23:'))
            a31 = int(input('Enter a31:'))
            a32 = int(input('Enter a32:'))
            a33 = int(input('Enter a33:'))
            A = a11*a22*a33 + a21*a32*a13 + a12*a23*a31 - a13*a22*a31 - a23*a32*a11 - a12*a21*a33
            print(A)
            if A == 0:
                print('Degenerate')
            else:
                print('Nondegenerate')
    if user_input == 2:
        print('Enter your matrix')
        a11 = int(input('Enter a11:'))
        a12 = int(input('Enter a12:'))
        a13 = int(input('Enter a13:'))
        a21 = int(input('Enter a21:'))
        a22 = int(input('Enter a22:'))
        a23 = int(input('Enter a23:'))
        a31 = int(input('Enter a31:'))
        a32 = int(input('Enter a32:'))
        a33 = int(input('Enter a33:'))
        print('This is your matrix: ')
        print(a11, a12, a13)
        print(a21, a22, a23)
        print(a31, a32, a33)
        A11 = 1 * (a22*a33 - a23*a32)
        A12 = -1 * (a21*a33 - a23*a31)
        A13 = 1  * (a21*a32 - a22*a31)
        A21 = -1 * (a12*a33 - a13*a32)
        A22 = 1 * (a11*a33 - a13*a31)
        A23 = -1 * (a11*a32 - a12*a31)
        A31 = 1 * (a12*a23 - a13*a22)
        A32 = -1 * (a11*a23 - a13*a21)
        A33 = 1 * (a11*a22 - a12*a21)
        print('Now you have: ')
        print(A11, A12, A13)
        print(A21, A22, A23)
        print(A31, A32, A33)

                         
                
                 
                 






