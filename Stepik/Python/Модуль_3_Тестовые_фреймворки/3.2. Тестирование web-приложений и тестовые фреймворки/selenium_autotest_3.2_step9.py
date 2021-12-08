import sys
"""
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Na')
if index != -1:
    print(f'Substring found at index {index}')
"""
def test_substring(full_string, substring):
  assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring,full_string)

    # ваша реализация, напишите assert и сообщение об ошибке


test_substring('some_text', 'some')
"""
в одну строку    assert (x == y), f"........."

x , y - ваши переменные и наполняйте f-strings пример 2 из 3.2 шаг 7

print не нужен
"""