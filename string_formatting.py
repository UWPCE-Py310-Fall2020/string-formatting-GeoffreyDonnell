def task_one():
    return print("file_{:0>3d} :   {:.2f}, {:.2e},{:.2e})".format(2, 123.4567, 10000, 12345.67))

def task_two():
    s = (2, 123.4567, 1000, 12345.67)
    return print("file_{:0>3d} :   {:.2f}, {:.2e},{:.2e})".format(*s))

def task_three(tuple):
    size = len(tuple)
    f_string = "The " + str(size) + " numbers are: "
    for step in range(0, size-1):
        f_string = f_string + "{:d}, "
    for step in range(size-1,size):
        f_string = f_string + "{:d}."
    return print(f_string.format(*tuple))

def task_four(s):
    f_string = "{:0>2d} {} {} {:0>2d} {}"
    return(print(f_string.format(s[3], s[4], s[2], s[0], s[1])))

def task_five(s):
    [fruit1, weight1, fruit2, weight2] = s[::]
    f_string = f'The weight of an {fruit1.upper()} is {weight1*1.2} ' \
               f'and the weight of a {fruit2.upper()} is {weight2*1.2}'
    return (print(f_string.format(*s)))

def task_six():
    Table = ['Item', 'Quantity','Units','Price',
             'Gas',21,'Gallons','$15.50',
             'Wax', 1,'Per Box','$8.00',
             'Exhuast', 1, 'Each', '$1200',
             'Rims', 4, 'Per Set', '$2999.95',
             'Car', 1,'Each','$32,995.00']

    size = int(len(Table)/4)

    for step in range(0,1):
        f_string = '{:15}{:20}{:20}{:20}'
        print(f_string.format(Table[step*4],Table[step*4+1],Table[step*4+2],Table[step*4+3]))
    for step in range (1,size):
        f_string = '{:15}{:<20d}{:20}{:20}'
        print(f_string.format(Table[step * 4], Table[step * 4 + 1], Table[step * 4 + 2],Table[step*4+3]))
    pass

def extratask_six():
    return print('{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}'.format(*tuple(range(0,10))))


print('Output of Task One:')
task_one()
print('Output of Task Two:')
task_two()
print('Output of Task Three:')
tuple_task3 = (1,2,3,4,5,6)
task_three(tuple_task3)
print('Output of Task Four:')
tuple_task4 = (4, 30, 2017, 2, 27)
task_four(tuple_task4)
print('Output of Task Five:')
tuple_task5 = ('orange', 1.3, 'lemon', 1.1)
task_five(tuple_task5)
print('Output of Task Six:')
task_six()
print('Output of Extra Task Six:')
extratask_six()