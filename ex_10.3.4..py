def log_instance_creation(cls):

    original_init = cls.__init__

    def __init__(self, *args, **kwargs):
        print(f"Створено новий екземпляр класу {cls.__name__}")
        # Викликаємо оригінальний конструктор
        original_init(self, *args, **kwargs)

    # Замінюємо конструктор класу
    cls.__init__ = __init__
    return cls


# Тестовий клас з декоратором
@log_instance_creation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Книга: '{self.title}', автор: {self.author}"


# Інший тестовий клас
@log_instance_creation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"


if __name__ == "__main__":
    with open('output04.txt', 'w', encoding='utf-8') as f:
        import sys
        from io import StringIO

        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        book1 = Book("1984", "Джордж Орвелл")
        book2 = Book("Гаррі Поттер", "Дж. К. Роулінг")
        person = Person("Нікіта", 30)

        sys.stdout = old_stdout

        output = mystdout.getvalue()

        f.write("=== Вивід декоратора при створенні екземплярів ===\n")
        f.write(output)
        f.write("\n=== Інформація про створені об'єкти ===\n")
        f.write(f"book1: {book1.info()}\n")
        f.write(f"book2: {book2.info()}\n")
        f.write(f"person: {person}\n")