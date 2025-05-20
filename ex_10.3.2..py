import inspect

def build_class_from_source(source_code):
    namespace = {}
    try:
        exec(source_code, namespace)
    except Exception as e:
        raise ValueError(f"Помилка виконання коду: {str(e)}")

    # Знаходимо перший клас у просторі імен
    for name, obj in namespace.items():
        if inspect.isclass(obj):
            return obj

    raise ValueError("У вихідному коді не знайдено класів")


if __name__ == "__main__":
    source = """
class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Значення: {self.value}")
"""

    # Перевірка роботи функції
    try:
        MyClass = build_class_from_source(source)

        obj = MyClass(42)

        obj.show()

        with open('output02.txt', 'w', encoding='utf-8') as f:
            f.write("Успішно створено клас MyClass з вихідного коду\n")
            f.write(f"Тип створеного об'єкта: {type(obj)}\n")
            f.write(f"Значення об'єкта: {obj.value}\n")

    except Exception as e:
        with open('output_task2.txt', 'w', encoding='utf-8') as f:
            f.write(f"Помилка: {str(e)}\n")