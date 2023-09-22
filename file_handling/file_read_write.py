with open("/home/ali.zaidi/Documents/Clean_code/Advanced_TDD_part_1.txt") as file:
    lines = [line.rstrip() for line in file]

lines = lines[0].split(".")

with open('/home/ali.zaidi/Documents/Clean_code/Advanced_TDD_part_1.txt', 'w') as the_file:
    for line in lines:
        the_file.write(line+".\n\n")



