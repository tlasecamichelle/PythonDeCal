#Homework3 Q8

def digital_root(n):
    digit_sum = 0

    while n>0:
        digit_sum += n % 10
        n //= 10

    return digit_sum

input_number = 12345
result = digital_root(input_number)
print(result)