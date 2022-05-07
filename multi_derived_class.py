# 一个类可以继承多个类（从左到右）
# 父类1
class student():
    def __init__(self, name, grad):
        self.name = name
        self.grad = grad

    def studentinfo(self):
        print("Student info: name = {}, grade = {}.".format(self.name, self.grad))


# 父类2
class speaker():
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speechinfo(self):
        print("A speech about {} is delivered by {}.".format(self.topic, self.name))


# 多继承子类
class union(student, speaker):
    def __init__(self, name, grad, topic):
        # 这里如果用super()只能继承第一父类的__init__
        student.__init__(self, name, grad)
        speaker.__init__(self, name, topic)

    # 覆写其中一个父类的方法
    def speechinfo(self):
        print("A speech about {} is delivered by {} at grade {}.".format(self.topic, self.name, self.grad))


# 父类方法，未被覆写
a = speaker('a', 'tttopic')
a.speechinfo()
# 多继承子类方法，被覆写
x = union('x', '12', 'TTTOPIC')
x.speechinfo()
