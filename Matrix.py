
print('''
███████████████████████████████
█─███─█────█───█────█───█──█──█
█──█──█─██─██─██─██─██─███───██
█─█─█─█────██─██────██─████─███
█─███─█─██─██─██─█─███─███───██
█─███─█─██─██─██─█─██───█──█──█
███████████████████████████████
''')
print('Version: 0.2')


def input_3_order():
    matrix_3_order_input = {}
    for i in range(3):
        matrix_3_order_input[f'a1{i + 1}'] = int(input(f'Enter matrix a1{i + 1} element: '))
        if len(matrix_3_order_input) == 3:
            break
    for i in range(3):
        matrix_3_order_input[f'a2{i + 1}'] = int(input(f'Enter matrix a2{i + 1} element: '))
        if len(matrix_3_order_input) == 6:
            break
    for i in range(3):
        matrix_3_order_input[f'a3{i + 1}'] = int(input(f'Enter matrix a3{i + 1} element: '))
        if len(matrix_3_order_input) == 9:
            break
    print(matrix_3_order_input)
    print('Your input: ')
    print(f'''
{matrix_3_order_input['a11']} | {matrix_3_order_input['a12']} | {matrix_3_order_input['a13']}
{matrix_3_order_input['a21']} | {matrix_3_order_input['a22']} | {matrix_3_order_input['a23']}
{matrix_3_order_input['a31']} | {matrix_3_order_input['a32']} | {matrix_3_order_input['a33']}
    ''')
    return matrix_3_order_input


def input_2_order():
    matrix_2_order_input = {}
    for i in range(2):
        matrix_2_order_input[f'a1{i + 1}'] = int(input(f'Enter matrix a1{i + 1} element: '))
        if len(matrix_2_order_input) == 2:
            break
    for i in range(2):
        matrix_2_order_input[f'a2{i + 1}'] = int(input(f'Enter matrix a2{i + 1} element: '))
        if len(matrix_2_order_input) == 4:
            break
    print(matrix_2_order_input)
    print('Your input:')
    print(f'''
     {matrix_2_order_input['a11']} | {matrix_2_order_input['a12']}
     {matrix_2_order_input['a21']} | {matrix_2_order_input['a22']}
         ''')
    return matrix_2_order_input


while True:
    print('''
    This is program can help with matrix calculation
    Choose that you want to do:
    1) Calculate the determinant of the matrix
    2) Find the matrix of algebraic complements
    3) Find the minor of matrix's element
    ''')
    user_input = int(input('Choose: '))

    if user_input == 1:
        print('Now you can choose det of matrix: ')
        n = int(input('Choose det 1, 2 or 3: '))
        if n == 1:
            a11 = int(input('Enter a11:'))
            A = a11
            print(A)
            print('Degenerate' if A == 0 else 'Non degenerate')
        if n == 2:
            matrix_2_order = input_2_order()
            A = matrix_2_order['a11'] * matrix_2_order['a22'] - matrix_2_order['a12'] * matrix_2_order['a21']
            print(A)
            print('Degenerate' if A == 0 else 'Non degenerate')
        if n == 3:
            matrix_3_order = input_3_order()
            A = matrix_3_order['a11'] * matrix_3_order['a22'] * matrix_3_order['a33'] + \
                matrix_3_order['a31'] * matrix_3_order['a12'] * matrix_3_order['a23'] + \
                matrix_3_order['a21'] * matrix_3_order['a32'] * matrix_3_order['a13'] - \
                matrix_3_order['a31'] * matrix_3_order['a22'] * matrix_3_order['a13'] - \
                matrix_3_order['a21'] * matrix_3_order['a12'] * matrix_3_order['a33'] - \
                matrix_3_order['a11'] * matrix_3_order['a23'] * matrix_3_order['a32']
            print(A)
            print('Degenerate' if A == 0 else 'Non degenerate')

    if user_input == 2:
        matrix_3_order = input_3_order()
        A11 = 1 * (matrix_3_order['a22'] * matrix_3_order['a33'] - matrix_3_order['a23'] * matrix_3_order['a32'])
        A12 = -1 * (matrix_3_order['a21'] * matrix_3_order['a33'] - matrix_3_order['a23'] * matrix_3_order['a31'])
        A13 = 1 * (matrix_3_order['a21'] * matrix_3_order['a32'] - matrix_3_order['a22'] * matrix_3_order['a31'])
        A21 = -1 * (matrix_3_order['a12'] * matrix_3_order['a33'] - matrix_3_order['a13'] * matrix_3_order['a32'])
        A22 = 1 * (matrix_3_order['a11'] * matrix_3_order['a33'] - matrix_3_order['a13'] * matrix_3_order['a31'])
        A23 = -1 * (matrix_3_order['a11'] * matrix_3_order['a32'] - matrix_3_order['a12'] * matrix_3_order['a31'])
        A31 = 1 * (matrix_3_order['a12'] * matrix_3_order['a23'] - matrix_3_order['a13'] * matrix_3_order['a22'])
        A32 = -1 * (matrix_3_order['a11'] * matrix_3_order['a23'] - matrix_3_order['a13'] * matrix_3_order['a21'])
        A33 = 1 * (matrix_3_order['a11'] * matrix_3_order['a22'] - matrix_3_order['a12'] * matrix_3_order['a21'])
        print('Now you have: ')
        print(f'''
{A11} | {A12} | {A13}
{A21} | {A22} | {A23}
{A31} | {A32} | {A33}
''')
    if user_input == 3:
        print('''
        ████─████─████─█───█─███─█──█─████
        █──█─█──█─█──█─██─██──█──██─█─█
        █────█──█─█──█─█─█─█──█──█─██─█─██
        █──█─█──█─█──█─█───█──█──█──█─█──█
        ████─████─████─█───█─███─█──█─████

        ███─████─████─█──█
        █───█──█─█──█─██─█
        ███─█──█─█──█─█─██
        ──█─█──█─█──█─█──█
        ███─████─████─█──█
        ''')
