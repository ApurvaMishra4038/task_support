number = 504678
number_str = str(number)
reversed_number_str = number_str[::-1]
result_str = ""

for i in range(len(reversed_number_str)):
    result_str += reversed_number_str[i]
    if (i + 1) % 2 == 0 and (i + 1) != len(reversed_number_str):
        result_str += ","
result_str = result_str[::-1]

print("input:", number)
print("output:", result_str)
