
digits = "23"
phone_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
numbers = list(phone_map[digits[0]])
print(numbers)

for digit in digits[1:]:
    numbers = [old + new for old in numbers for new in list(phone_map[digit])]
print(numbers)

print(digits[1:])