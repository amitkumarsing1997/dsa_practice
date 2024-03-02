# from typing import List
# def append_pi(lst: List[float]) -> None:
#     lst += [3.14]

# my_list = [1, 3, 5]  # type: List[int]

# append_pi(my_list)   # Naively, this should be safe...
# print(type(my_list[-1] << 5))

# # my_list[-1] << 5     # ... but this fails



# /             # rejected by the type checker


from typing import TypeVar

AnyStr = TypeVar('AnyStr', str, bytes)

def longest(first: AnyStr, second: AnyStr) -> AnyStr:
    return first if len(first) >= len(second) else second

result = longest('a', 'abc')  # The inferred type for result is str
print(result)
result = longest('a', b'abc')  # Fails static type check
print(result)