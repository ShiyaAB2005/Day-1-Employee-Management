numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("After removing duplicates:", result)