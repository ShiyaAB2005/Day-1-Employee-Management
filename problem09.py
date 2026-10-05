text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

found = False

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        found = True
        break

if not found:
    print("No non-repeating character")