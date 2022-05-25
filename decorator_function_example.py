# TODO you don't allow to change the value manually of function num which is returning the value of a 10


# TODO We're going to make a decorator function here (1 Way).
# def myDecorator(fun):
#     def add():
#         a = fun()
#         addition = a + 5
#         return addition
#     return add
#
# def num():
#     return 10
#
# result = myDecorator(num)
# print(result())

# TODO We're going to make a decorator function here (2 Way)
def myDecorator(fun):
    def add():
        a = fun()
        addition = a + 5
        return addition

    return add


def myDecorator2(fun):
    def multiply():
        a = fun()
        multi = a * 5
        return multi
    return multiply


# @myDecorator2
# @myDecorator
def num():
    return 10


result_fun = myDecorator2(myDecorator(num))
print(result_fun())
