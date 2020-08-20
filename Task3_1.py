from datetime import datetime, date
class Student:
    __id = 0
    __name = ''
    __surname = ''
    __patronymic = ''
    __birth = ''
    __address = ''
    __telephone = ''
    __faculty = ''
    __course = 0
    __group = ''

    def __init__(self, id, name, surname, patronymic, birth, address, telephone, faculty, course, group):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__birth = birth
        self.__address = address
        self.__telephone = telephone
        self.__faculty = faculty
        self.__course = course
        self.__group = group

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_patronymic(self):
        return self.__patronymic
    def get_birth(self):
        return self.__birth
    def get_address(self):
        return self.__address
    def get_telephone(self):
        return self.__telephone
    def get_faculty(self):
        return self.__faculty
    def get_course(self):
        return self.__course
    def get_group(self):
        return self.__group
    def age_of_student(self):
        today = datetime.today()
        born = datetime.strptime(self.get_birth(), "%d %m %Y")
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))





def get_info(self):
        print('Student id: ' + str(Students[i].get_id()))
        print('Student name: ' + Students[i].get_name())
        print('Student surname: ' + Students[i].get_surname())
        print('Student patronymic: ' + Students[i].get_patronymic())
        print(str(Students[i].age_of_student()) + ' years old ')
        print('Student address: ' + Students[i].get_address())
        print('Student telephone: ' + Students[i].get_telephone())
        print('Student faculty: ' + Students[i].get_faculty())
        print('Student course: ' + str(Students[i].get_course()))
        print('Student group: ' + Students[i].get_group())
        print('---------------')

def get_info_group(self):
            print('Student id: ' + str(Students[i].get_id()))
            print('Student name: ' + Students[i].get_name())
            print('Student surname: ' + Students[i].get_surname())
            print('Student patronymic: ' + Students[i].get_patronymic())
            print('---------------')

Students =  [Student(1,'Karyna','Belaya','Aleksandrovna','04 06 1998','Gagarina 26-24 ','+375298541231','IEF',4,'673903'),
             Student(2,'Aleksandra','Kozlova','Aleksandrovna','22 04 1999',' Prydu 52-2 ','+375298589123','IEF',4,'673903'),
             Student(3,'Victoriya','Belaya','Vyacheslavovna','30 09 1999','prosp. Stroiteley 58-23 ','+375298754129','IEF',3,'774003'),
             Student(10,'Egor','Kozlov','Anatolyevich','02 08  1998','Microraion Zelenyi 45-89 ','+375292312546','FRE',2,'972502'),
             Student(20,'Pavel','Ivanov','Anatolyevich','03 12 1998','Microraion Zelenyi 78-58','+375298541222','FITU',4,'672708')]
b=Student(1,'Karynaaaaaa','Belaya','Aleksandrovna','04 06 1998','Gagarina 26-24 ','+375298541231','IEF',4,'673903')
a=int(input('Выбор действия: \n 1-вывести список студентов заданного факультета \n 2-вывести список учебной группы \n' ))
if a==1:
 i = 0
 fac = input('Введите название факультета \n')
 print('Cписок студентов заданного факультета')
 for i in range(len(Students)):
    if Students[i].get_faculty() == fac:
        get_info(i)
    i += 1
 print('-------------------------------------------------')
elif a==2:
 gr = input('Введите группу \n')
 print('Cписок группы')
 i=0
 for i in range(len(Students)):
    if Students[i].get_group() == gr:
        get_info_group(i)
    i+=1
 print('-------------------------------------------------')






