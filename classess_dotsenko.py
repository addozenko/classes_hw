class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def put_grade(self, lector):
        if isinstance(lector, Lecturer):
            for course in lector.courses_attached:
                if course in self.courses_in_progress:
                    if course in lector.students_grades:
                        lector.students_grades[course] += self.grades[course]
                    else:
                        lector.students_grades[course] = self.grades[course]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        return self.__calculate_average_grade()
    
    def __calculate_average_grade(self):
        average_grade = 0
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        average_grade = sum(all_grades)/len(all_grades)
        return average_grade
    
    def __str__(self):
        average_grade = self.get_average_grade()
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {average_grade}
        Курсы в процессе изучения: {" ".join(cours for cours in self.courses_in_progress)}
        Завершенные курсы: {" ".join(cours for cours in self.finished_courses)}"""
   
    def __eq__(self, student):
        return self.get_average_grade() == student.get_average_grade()
    
    def __lt__(self, student):
        return self.get_average_grade() < student.get_average_grade()
    
    def __gt__(self, student):
        return self.get_average_grade() > student.get_average_grade()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.students_grades = {}
        
    def get_average_rating(self):
        return self.__calculate_average_rating()
    
    def __calculate_average_rating(self):
        average_rate = 0
        all_grades = []
        for grades in self.students_grades.values():
            for grade in grades:
                all_grades.append(grade)
        average_rate = sum(all_grades)/len(all_grades)
        return average_rate
    

    def __str__(self):
        average_rating = self.get_average_rating()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}'
    
    def __eq__(self, lector):
        return self.get_average_rating() == lector.get_average_rating()
    
    def __lt__(self, lector):
        return self.get_average_rating() < lector.get_average_rating()
    
    def __gt__(self, lector):
        return self.get_average_rating() > lector.get_average_rating()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student_1 = Student('Jon','Snow', 'man')
student_2 = Student('Daenerys','Targaryen', 'girl')

lector_1 = Lecturer('Jaime','Lannister')
lector_2 = Lecturer('Cersei','Lannister')

reviewer_1 = Reviewer('Eddard','Stark')
reviewer_2 = Reviewer('Sansa','Stark')

student_1.courses_in_progress +=['Python', 'Java']
student_2.courses_in_progress +=['Python', 'Java']

student_1.finished_courses += ['CSS']
student_2.finished_courses += ['HTML']

reviewer_1.courses_attached +=['Python', 'Java']
reviewer_2.courses_attached +=['Python', 'Java']

lector_1.courses_attached +=['Python', 'Java']
lector_2.courses_attached +=['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 6)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Java', 8)

student_1.put_grade(lector_1)
student_2.put_grade(lector_2)

print(lector_1)
print(lector_2)
print(student_2)
print(student_1)

print(lector_1 > lector_2)
print(lector_1 < lector_2)
print(lector_1 == lector_2)
print(student_2 > student_1)
print(student_2 < student_1)
print(student_2 == student_1)

students = (student_1, student_2)
lectors = (lector_1, lector_2)

def calc_average_grade(students):
    summ = 0
    for student in students:
        summ += student.get_average_grade()
    print(summ/len(students))


def calc_average_rating(lectors):
    summ = 0
    for lector in lectors:
        summ += lector.get_average_rating()
    print(summ/len(lectors))

calc_average_grade(students)
calc_average_rating(lectors)