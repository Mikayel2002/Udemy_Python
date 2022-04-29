# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for i in args:
#         product *= i

#     return product / 100 * percent


# print(percent_of_product_with_args(20, 10, 20, 2, 1, 4, 345))


# def func_with_kwargs(**kwargs):
#     print(kwargs)


# func_with_kwargs(first=1, second=2, third=3)


# def hello_with_kwargs(**kwargs):
#     if "name" in kwargs:
#         print("Hello! Nice to meet you {}.".format(kwargs["name"]))
#     else:
#         print("Hello! What is your name?")


# hello_with_kwargs(name="Mikayel")


# def func_with_args_and_kwargs(*args, **kwargs):
#     print(args)
#     print(kwargs)


# func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')




# N1
# Создайте функцию is_cat_here(), которая принимает любое количество аргументов и проверяет 
# есть ли строка 'cat' среди них. Функция должна возвращать True, если такой параметр есть 
# и False в обратном случае. Буквы в строке 'cat' могут быть как большие, так и маленькие


# def is_cat_here(*args):
#     if "cat" in args:
#         return True
#     else:
#         return False


# print(is_cat_here("cat", "dog", "cow"))
# print(is_cat_here("dog", "cow"))


# with lower case
# def is_cat_here(*args):
#     args_in_lower_case = [str(argument).lower() for argument in list(args)]
#     if 'cat' in args_in_lower_case:
#         return True
#     else:
#         return False


# print(is_cat_here("CAT", "dog", "cow"))


# N2
# Создайте функцию is_item_here(item, *args), которая проверяет есть ли item среди args. 
# Функция должна возвращать True, если такой параметр есть и False в обратном случае.


# def is_item_here(item, *args):
#     if item in args:
#         return True
#     else:
#         return False


# print(is_item_here(5, 11, 20, 100, 5, 66))
# print(is_item_here(5, 11, 20, 100, 66))



# N3
# Создайте функцию your_favorite_color() с позиционным параметром my_color и параметрами
#  **kwargs, которая будет выводить на экран 'My favorite color is (значение my_color), 
# what is your favorite color?', если в параметрах kwargs нет ключа color, и 
# 'My favorite color is (значение my_color), but (значение по ключу color) is also pretty good!', 
# если в параметрах kwargs ключ color присутствует


def your_favorite_color(my_color, **kwargs):
    if "color" not in kwargs:
        print("My favorite color is {}, what is your favorite color?".format(my_color))
    else:
        print("My favorite color is {}, but {} is also pretty good!".format(my_color, kwargs["color"]))


your_favorite_color(my_color="Blue")
your_favorite_color(my_color="Blue", color="Green")
