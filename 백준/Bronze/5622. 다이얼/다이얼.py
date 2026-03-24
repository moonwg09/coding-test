
chars = list(input())

total = 0

for char in chars:
    if char == 'W' or char == 'Z' or char == 'X' or char == 'Y':
        total += 10
    if char == 'T' or char == 'U' or char == 'V':
        total += 9
    if char == 'P' or char == 'Q' or char == 'R' or char == 'S':
        total += 8
    if char == 'M' or char == 'N' or char == 'O':
        total += 7
    if char == 'J' or char == 'K' or char == 'L':
        total += 6
    if char == 'G' or char == 'H' or char == 'I':
        total += 5
    if char == 'D' or char == 'E' or char == 'F':
        total += 4
    if char == 'A' or char == 'B' or char == 'C':
        total += 3
   

print(total)
