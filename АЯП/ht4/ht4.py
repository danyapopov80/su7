# №1
any_list = [1,2,3,4,5,6,7,8,9,969,27,7,35]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(any_list)

# №2
any_list = [1,2,3,4,5,6,7,8,9,969,27,7,35]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)

# №3
any_list = [1,2,3,4,5,6,7,8,9,969,27,7,35]
def replacement(list):
    i_of_max_el = list.index(max(list))
    i_of_min_el = list.index(min(list))
    list[i_of_max_el], list[i_of_min_el] = list[i_of_min_el], list[i_of_max_el]
    print(list)
replacement(any_list)

# №4
d = {1: 'сусемь)', 2: 'Адам Смит', 3: 'ключ', 4: 'John Cenaaa'}
key = int(input('Введите ключ, чтобы получить его значение: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(d)
