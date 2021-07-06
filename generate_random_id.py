import random
import sre_yield

korean = ['가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파', '하']
nums = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def generate_random_id():
    _id = ''
    _kr_key = random.choice(korean)
    for _ in range(2): _id += random.choice(nums)
    _id += _kr_key
    for _ in range(3): _id += random.choice(nums)

    return _id


def generate_easy_password():
    _id = ''
    for _ in range(8): _id += random.choice(nums)
    for _ in range(2):
        rand_v = random.randrange(0, 8)
        _id = list(_id)
        _id[rand_v] = random.choice(korean)
        _id = "".join(_id)

    return _id


print("test gen easy pass :" ,generate_easy_password())
print("test gen random id :",generate_random_id())
