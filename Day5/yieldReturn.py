# def colors():
#     yield "red"
#     yield "blue"
#     yield "yellow"
#
# next_color = colors()
# print(type(next_color))  # <class 'generator'>
#
# print(next(next_color))
# print(next(next_color))
# print(next(next_color))


def something():
    for i in range(1, 10):
        yield i


next_number = something()
print(next(next_number))
print(next(next_number))
