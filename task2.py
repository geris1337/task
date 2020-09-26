# Why does print_list() not correctly print out the elements a_list?
def print_list(a_list):
    for i in range(1, len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))

a_list = [1, 2, 3, 5, 7, 9]

print_list(a_list)

# Answer: wrong range index, first element index starts with 0 not 1
# To fix the function in line 3 (change 1 to 0) | for i in range(0, len(a_list)):
# or remove (1,) | for i in range(len(a_list)):