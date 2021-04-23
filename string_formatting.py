def task_one():
    print("file_{:0>3d} :   {:.2f}, {:.2e},{:.2e})".format(2, 123.4567, 10000, 12345.67))
    pass

def task_two():
    s = (2, 123.4567, 1000, 12345.67)
    print("file_{:0>3d} :   {:.2f}, {:.2e},{:.2e})".format(*s))
    pass

def task_three(tuple):
    size = len(tuple)
    f_string = "The " + str(size) + " numbers are: "
    for step in range(0, size-1):
        f_string = f_string + "{:d}, "
    for step in range(size-1,size):
        f_string = f_string + "{:d}."

    return print(f_string.format(*tuple))
    pass

def task_four(tuple):


    pass

task_four(4,30,2017,2,27)


#task_one()
#task_two()
#tuple_task3 = (1,2,3,4,5,6)
#task_three(tuple_task3)