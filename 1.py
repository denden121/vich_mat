from math import *
from sympy import *


def first_method(func, start, finish, eps):
    #eval('from math import sin,cos')
    temp_start = start
    temp_finish = finish
    while True:
        center = (temp_start + temp_finish)/2
        result = eval(func.replace('x', str(center)))
        if abs(result) < eps:
            with open('result.txt','w') as f:
                f.write(f'The root of the function in the range from {start} to {finish} is {center}')
            break
        temp_result = eval(func.replace('x', str(temp_start)))
        if result*temp_result < 0:
            temp_finish = center
        else:
            temp_start = center


def second_method(func, start, finish, eps):
    temp_start = start
    temp_finish = finish
    left_result = result = eval(func.replace('x', str(temp_start)))
    right_result = result = eval(func.replace('x', str(temp_finish)))
    x = temp_start - ((left_result*(temp_finish-temp_start)) / (right_result-left_result))
    result_x = result = eval(func.replace('x', str(x)))
    last_x = x
    if result_x * right_result < 0:
        result = right_result
        dot = temp_finish
    else:
        result = left_result
        dot = temp_start
    while True:
        result_n = eval(func.replace('x', str(last_x)))
        x = last_x - (result_n/(result-result_n))*(dot-last_x)
        if abs(x - last_x) < eps:
            break
        last_x = x
    with open('result.txt','w') as f:
        f.write(f'The root of the function in the range from {start} to {finish} is {x}')


def third_method(func, start, finish, eps):
    temp_start = start
    temp_finish = finish
    left_result = eval(func.replace('x', str(temp_start)))
    x = symbols('x')
    diff2 = diff(func, x, x)
    left_diff2 = eval(str(diff2).replace('x', str(temp_start)))
    print(temp_start, temp_finish, left_result, left_diff2)
    if left_result * left_diff2 > 0:
        last_x = temp_start
    else:
        right_diff2 = eval(str(diff2).replace('x', str(temp_finish)))
        right_result = eval(func.replace('x', str(temp_finish)))
        print(right_result, right_diff2)
        if right_diff2*right_result > 0:
            last_x = temp_finish
        else:
            last_x = temp_start
            print("Error!")
    while True:
        diff1 = diff(func, x)
        result_diff1 = eval(str(diff1).replace('x', str(last_x)))
        result_last_x = eval(func.replace('x', str(last_x)))
        new_x = last_x - result_last_x/result_diff1
        new_result_x = eval(func.replace('x', str(new_x)))
        if abs(new_x-last_x) < eps and abs(new_result_x) < eps:
            break
        last_x = new_x
    with open('result.txt','w') as f:
        print(f'The root of the function in the range from {start} to {finish} is {new_x}')


with open('/home/den/Documents/universite/v_mat/1.txt') as f:
    func = f.readline().split('=')[1]
    start, finish = map(float, f.readline().split(' '))
    eps = float(f.readline())

while True:
    print('Select method(1,2,3) or exit', end=' ')
    method = input()
    if method == '1':
        first_method(func, start, finish, eps)
    elif method == '2':
        second_method(func, start, finish, eps)
    elif method == '3':
        third_method(func, start, finish, eps)
    else:
        print('Repeat enter')
