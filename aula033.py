def multplication(*args):
    x = 1
    for number in args:
        x *= number
    return x
def check_pair(number):
    x = number
    result = x % 2
    if result == 0:
       return f'o numero é {x} PAR'
    return f'o  numero é {x} IMPAR'

print(check_pair(8))

