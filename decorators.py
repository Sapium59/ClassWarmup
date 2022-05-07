# source: https://www.runoob.com/w3cnote/python-func-decorators.html
from functools import wraps


def a_new_decorator(a_func):
    # 在这个函数内部被定义的函数是用来修饰作为变量被输入的函数的
    def wrapTheFunction():
        print("I am pre-func decoration of " + a_func.__name__)
        a_func()
        print("I am post-func decoration of " + a_func.__name__)

    return wrapTheFunction


method1 = 0  # execute decorator function explicitly
method2 = 0  # simply use @ instead
method3 = 1  # standard usage which makes .__name__ work correctly

if method1:
    # 修饰器的原理和一种朴素的实现
    def a_function_requiring_decoration():
        print("I am a_function_requiring_decoration")


    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    # decorate: now a_function_requiring_decoration is wrapped by wrapTheFunction()

    print('After decoration:')
    a_function_requiring_decoration()
    # outputs:I am doing some boring work before executing a_func()
    #        I am the function which needs some decoration to remove my foul smell
    #        I am doing some boring work after executing a_func()

# --------------------------------------- METHOD 2 --------------------------------------------------------------

if method2:
    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey you! Decorate me!"""
        print("I am a_function_requiring_decoration")


    a_function_requiring_decoration()
    # outputs: I am doing some boring work before executing a_func()
    #         I am the function which needs some decoration to remove my foul smell
    #         I am doing some boring work after executing a_func()

    # the @a_new_decorator is just a short way of saying:
    # a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# --------------------------------------- METHOD 3 --------------------------------------------------------------

if method3:
    def a_new_decorator(a_func):
        # @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
        @wraps(a_func)
        def wrapTheFunction():
            print("I am doing some boring work before executing a_func()")
            a_func()
            print("I am doing some boring work after executing a_func()")
        return wrapTheFunction


    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey yo! Decorate me!"""
        print("I am the function which needs some decoration.")


    print(a_function_requiring_decoration.__name__)
    # Output: a_function_requiring_decoration
