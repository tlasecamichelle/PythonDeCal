#Homework3 Q7

def vowel_count(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1
    return count 
       
# Example usage:
string1 = "UC Berkeley"
result = vowel_count(string1)
print(result) 
