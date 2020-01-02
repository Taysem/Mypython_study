#班级内
class Classes:
    def __init__(self,name,school,kind):
        self.name = name #班级名称 例如python_s9期
        self.school = school #学校
        self.kind = kind #班级科目  linux  go
        self.setduent = ['setdent_obj']

#课程对象
class Course:
    def __init__(self,name,period,price):
        self.name = name #课程名称
        self.period = period#课程周期
        self.price = price#价格


class Teacher:
    def __init__(self,name,classes,course):
        self.name = name
        self.classes = ['classes_obj']#课程对象
        self.courses = course
        pass

