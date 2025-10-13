with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
        
    # Подсчет слов
    words = text.split()
    word_count = len(words)
    print(f"Количество слов: {word_count}")        
