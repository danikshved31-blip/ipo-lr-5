text = input("Введите строку ")
word = text[0]
new_text = text.replace(text[0], text[-1], 1)
print(new_text)
