# self 参数是对类的当前实例的引用，用于访问属于该类的变量。 它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数
class Person():
    # 每次使用类创建新对象时，都会自动调用 __init__() 函数。
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.name = fname + ' ' + lname
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Bill", "Clinton", 63)
p1.age = 40

print(p1.name, p1.age)
p1.myfunc()

# 可以删除对象的属性或者对象本身
del p1.age
del p1


# 子类继承
class Student(Person):
    # 子类可以有不同于父类的启动
    def __init__(self, fname, lname, age, year):
        # 如果要保持与父类的启动方式一致，应当调用之
        Person.__init__(self, fname, lname, age)
        # 或者，Python 还有一个 super() 函数，它会使子类从其父继承所有方法和属性：
        # super().__init__(fname, lname, age)
        # 添加不同于父类的属性
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "at age", self.age, "to the class of", self.graduationyear)


x = Student('Elon', 'Musk', '36', '2001')
x.welcome()
