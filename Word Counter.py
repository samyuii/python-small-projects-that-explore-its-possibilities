def count_words(text):
    word_count = {}
    words = text.split()

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

file_path = input("Enter the path to the text file: ")
with open(file_path, 'r') as file:
    content = file.read()

word_count = count_words(content)
total_words = sum(word_count.values())

print("Word Count:")
for word, count in word_count.items():
    print(f"{word}: {count}")

print(f"Total words: {total_words}")
