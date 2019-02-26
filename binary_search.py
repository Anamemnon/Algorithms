# Алгоритм бинарного поиска

# пробный массив, не относится к алгоритму
# нужен только для проверки алгоритма, т.е. 
# для поиска значения в интервале от 0 до 10 000 включительно
in_arr = list([i for i in range(10001)])

start, end = 0, len(in_arr) - 1

# число которое хочет найти пользователь в интервале от 0 до 10 000
search = int(input())

# отслеживает сколько итерациий нужно для поиска search
index = 1

while start <= end:
    mid = (start + end) // 2
    print(f'[{index}]', 'index:', mid, 'value: ', in_arr[mid])
    if in_arr[mid] == search:
        break
    elif in_arr[mid] < search:
        start = mid
    else:
        end = mid
    index += 1
