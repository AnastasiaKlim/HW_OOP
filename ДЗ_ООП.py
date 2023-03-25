#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Student:
   
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = 0

    def grade_s(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades_f_s:
                lecturer.grades_f_s[course] += [grade]
            else:
                lecturer.grades_f_s[course] = [grade]
        else:
            return 'Ошибка'


    def average_value(self, name, course, grade):
        print(f'{name} - {isinstance(name, Student)}')                                      
        print(f'{course} - {course in self.finished_courses} - {self.finished_courses}')       
        print(f'{course} - {course in self.courses_in_progress} - {self.courses_in_progress}') 


        print(f'\self.grades {self.grades}\n') 

        avg = sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        self.avg += avg
        
    def __str__(self):
        text = f'Имя: {self.name} \Фамилия: {self.surname} \Средняя оценказа ДЗ: \Курсы в процессе изучения: {self.courses_in_progress}'                f'\Завершенные курсы: {self.finished_courses}'
        return text


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Revewier(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


st = Student('Roy', 'Jhons', 'male')
st.courses_in_progress += ['Python']
st.finished_courses += ['C++']

re = Revewier('Alek', 'Bolduin')
re.courses_attached += ['Python']
re.rate_hw(st, 'Python', 9)
re.rate_hw(st, 'Python', 7)
re.rate_hw(st, 'Python', 4)

st.average_value('Roy','Python', [9, 7, 4])
print(f"среднее значение оценок ({st.grades['Python']}) / {round(st.avg,2)}")  


# In[ ]:





# In[ ]:




