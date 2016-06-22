def add(arg_1, arg_2):
    result = arg_1 + arg_2
    print('%d + %d = %d' % (arg_1, arg_2, result))
    return result

# Arguments are passed in as args
first = add(1, 2)
# Prints: 1 + 2 = 3

# Arguments are passed in as kwargs
first = add(arg_2=1, arg_1=2)
# Prints: 2 + 1 = 3
