# Задача 2. 
# Реализовать абстрактный класс человек, а после создать классы профессий:
# менеджер
# программист
# бизнес аналитик
# тестировщик
# 4 проперти и 1 метод. Каждый из классов должен переопределять все проперти и методы.

# создать объекты каждого из классов и вывести все его атрибуты и методы при помощи цикла for.


class Human:
    def __init__(self , name, gender, profession_name):
        self.__name = name
        self.__gender = gender
        self.professions_list = {'manager': Manager.skills}
        self.__profession = profession_name

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, new_prof):
        self.__profession = new_prof

    def profile(self):
        return self.__gender, self.__name, self.__profession

    def prof_skills(self):
        a = Manager
        print(a.skills)
        return a.skills

    
class Manager:
    def __init__(self):
        self.__skills = ['responsibility', 'communication skills', 'marketing education']
    
    def __repr__(self):
        return 'Manager'

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, new):
        self.skills = (self.__skills).append(new)


a = Human('Sara', 'women', 'manager')
print(a.profession)
print(a.profile())
print(a.prof_skills())
b = Manager
# .skills(['responsibility', 'communication skills', 'marketing education'])
print(b.skills)