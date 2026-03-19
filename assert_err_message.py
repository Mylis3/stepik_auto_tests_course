# Задание_1: составные сообщения об ошибках и поиск подстроки
#
# Требуется проверить, что некий текст является подстрокой другого текста: с помощью ключевого слова in, либо с помощью функции find:

# s = 'My Name is Julia'

# if 'Name' in s:
#     print('Substring found')

# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')


# s = 'My Name is Julia'

# if 'Name' in s:
#     print('Substring found')

# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')

# Задание_1: Проверка для функции test_substring, которая принимает два значения: full_string и substring.

# Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и, в случае несовпадения, предоставить
# исчерпывающее сообщение об ошибке.

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


full_string, substring = "fulltext", "some_value"
# full_string, substring = '1', '1'
# full_string, substring = "some_text", "some"
test_substring(full_string, substring)
