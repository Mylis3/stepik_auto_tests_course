# Задание_1: Тестовые сценарии
# Созданные тесты нужно сохранить в файле, чтобы его было удобно запускать и хранить в системе контроля версий.
def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")


#
