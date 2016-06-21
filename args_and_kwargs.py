def my_function(*args, **kwargs):
    print 'Args: ', args
    print 'Kwargs: ', kwargs

my_function(1, 2)
my_function(first_arg=3, second_arg=4)
