from typing import Any, Generator

new_list = (x ** 2 for x in [1, 2, 3, 4, 5, 6])
# new_list: Generator[Any, Any, None] = (x ** 2 for x in [1, 2, 3, 4, 5, 6])

print(type(new_list)) # <class 'generator'>

for item in new_list:
    print(item)