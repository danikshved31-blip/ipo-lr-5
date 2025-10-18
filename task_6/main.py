with open('text.txt', 'r', encoding = 'utf - 8') as a:
    lines = a.readlines()
    new_lines = lines.replace("а", "о")
with open('output.txt', 'w', encoding="utf - 8") as b:
    b.writelines(new_lines)
print("файл создан")
