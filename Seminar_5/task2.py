# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква, а значение - код буквы.
# Напишите преобразование в одну строку.

text = 'qweeeqwertyepoweudsnkljvnskdna'
res = {i: ord(i) for i in text}

iter_dict = iter(res.items())
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))
print(next(iter_dict))