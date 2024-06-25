class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def average_grade(self, subject=None):
        if subject:
            if subject in self.grades:
                grades = self.grades[subject]
                return sum(grades) / len(grades) if grades else 0
            else:
                return 0
        else:
            all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
            return sum(all_grades) / len(all_grades) if all_grades else 0

    def display_info(self):
        print(f"Student: {self.name}")
        print("Grades:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")


class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def remove_student(self, student_name):
        if student_name in self.students:
            del self.students[student_name]

    def display_students(self):
        for student_name, student in self.students.items():
            student.display_info()
            print()  # Separate each student's info with a blank line

    def add_grade(self, student_name, subject, grade):
        if student_name in self.students:
            self.students[student_name].add_grade(subject, grade)
        else:
            print(f"Studentul {student_name} nu există în clasă.")

    def average_grade(self, student_name=None, subject=None):
        if student_name:
            if student_name in self.students:
                return self.students[student_name].average_grade(subject)
            else:
                return 0
        elif subject:
            total = 0
            count = 0
            for student in self.students.values():
                total += student.average_grade(subject)
                count += 1
            return total / count if count > 0 else 0
        else:
            total = 0
            count = 0
            for student in self.students.values():
                total += student.average_grade()
                count += 1
            return total / count if count > 0 else 0
def main():
    classroom = Classroom()

    while True:
        print("\nMeniu:")
        print("1. Adăugare student")
        print("2. Ștergere student")
        print("3. Adăugare notă")
        print("4. Afișare medie student")
        print("5. Afișare medie clasă")
        print("6. Afișare toți studenții")
        print("7. Ieșire")

        choice = input("Introduceți opțiunea: ")

        if choice == "1":
            name = input("Introduceți numele studentului: ")
            student = Student(name)
            classroom.add_student(student)
            print(f"Studentul {name} a fost adăugat.")

        elif choice == "2":
            name = input("Introduceți numele studentului de șters: ")
            classroom.remove_student(name)
            print(f"Studentul {name} a fost șters.")

        elif choice == "3":
            name = input("Introduceți numele studentului: ")
            subject = input("Introduceți materia: ")
            grade = float(input("Introduceți nota: "))
            classroom.add_grade(name, subject, grade)

        elif choice == "4":
            name = input("Introduceți numele studentului: ")
            average = classroom.average_grade(student_name=name)
            print(f"Media pentru studentul {name}: {average:.2f}")

        elif choice == "5":
            subject = input("Introduceți materia pentru care doriți media: ")
            average = classroom.average_grade(subject=subject)
            print(f"Media pentru materia {subject}: {average:.2f}")

        elif choice == "6":
            print("\nLista de studenți:")
            classroom.display_students()

        elif choice == "7":
            print("Programul a fost încheiat.")
            break

        else:
            print("Opțiune invalidă. Reîncercați.")


main()
