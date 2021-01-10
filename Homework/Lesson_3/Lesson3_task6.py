

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def title_word(word):
    return word.title()

print(title_word('text'))
print(title_word('python'))
print(title_word('moscow'))