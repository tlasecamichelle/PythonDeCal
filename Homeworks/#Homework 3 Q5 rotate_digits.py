#Homework 3 Q5 rotate_digits 

def rotate_digits(n):
    last_digit = n % 10
    remaining_digits = n // 10

    num_digits = 1
    temp = remaining_digits
    while temp > 0:
        temp //= 10
        num_digits += 1

    rotated_number = last_digit * (10 ** (num_digits - 1)) + remaining_digits
    return rotated_number 
input_number = 12345
result = rotate_digits(input_number)
print(result)

print (rotate_digits(12345))