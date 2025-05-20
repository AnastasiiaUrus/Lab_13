def log_function_call(func):

    def wrapper(*args, **kwargs):
        # Отримуємо ім'я функції
        func_name = func.__name__

        # Виводимо інформацію про виклик
        print(f"Викликано функцію/метод: {func_name}")

        # Викликаємо оригінальну функцію
        return func(*args, **kwargs)

    return wrapper


# Тестовий клас з декораторами
class TestClass:
    @log_function_call
    def test_method(self, x):
        return x * 2


# Тестові функції з декоратором
@log_function_call
def add_numbers(a, b):
    return a + b


@log_function_call
def greet(name):
    return f"Привіт, {name}!"


if __name__ == "__main__":
    with open('output03.txt', 'w', encoding='utf-8') as f:
        import sys
        from io import StringIO

        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        # Тестуємо функції
        result1 = add_numbers(3, 5)
        result2 = greet("Софіє")

        # Тестуємо метод класу
        test_obj = TestClass()
        result3 = test_obj.test_method(10)

        # Повертаємо stdout
        sys.stdout = old_stdout

        # Отримуємо захоплений вивід
        output = mystdout.getvalue()

        # Записуємо результати у файл
        f.write("=== Вивід декоратора ===\n")
        f.write(output)
        f.write("\n=== Результати виконання ===\n")
        f.write(f"add_numbers(3, 5) = {result1}\n")
        f.write(f"greet('Софіє') = {result2}\n")
        f.write(f"test_obj.test_method(10) = {result3}\n")