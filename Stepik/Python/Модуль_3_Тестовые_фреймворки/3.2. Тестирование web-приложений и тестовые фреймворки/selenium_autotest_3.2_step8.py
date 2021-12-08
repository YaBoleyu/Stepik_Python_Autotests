import sys

def test_input_text(expected_result, actual_result):
  assert(expected_result==actual_result), "expected {}, got {}".format(str(expected_result), str(actual_result))
    # ваша реализация, напишите assert и сообщение об ошибке


test_input_text(8,11)
test_input_text(11,11)
test_input_text(11,15)
"""
в одну строку    assert (x == y), f"........."

x , y - ваши переменные и наполняйте f-strings пример 2 из 3.2 шаг 7

print не нужен
"""