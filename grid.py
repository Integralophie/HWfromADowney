import math
def repeat_run(num):
    for i in range(int((num-1)/2)):
        print('|', ' '*int((num-1)/2),'|',' ' *int((num-1)/2),'|')

def grid(grid_num):
    print('+','-'*int((grid_num-1)/2),'+','-'*int((grid_num-1)/2),'+')
    repeat_run(grid_num)
    print('+','-'*int((grid_num-1)/2),'+','-'*int((grid_num-1)/2),'+')
    repeat_run(grid_num)
    print('+','-'*int((grid_num-1)/2),'+','-'*int((grid_num-1)/2),'+')

grid(9)
