
add_list = list(input().split('-'))

result = sum(map(int, add_list[0].split('+')))

for add_part in add_list[1:]:
    part_result = sum(map(int,add_part.split('+')))
    result -= part_result

print(result)
