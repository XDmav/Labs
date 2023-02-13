groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 2, 2]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Вася",
        "surname": "Горностаев",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Михаил",
        "surname": "Лукашевич",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [2, 3, 4]
    },
    {
        "name": "Дима",
        "surname": "Александров",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [2, 5, 5]
    },
    {
        "name": "Петя",
        "surname": "Махмутов",
        "exams": ["АиГ", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def sort_students(students):
    required_score = float(input())
    new_students = []
    for student in students:
        if (sum(student["marks"]) / 3) >= required_score:
            new_students.append(student)
    return new_students


print_students(sort_students(groupmates))
