# Первый способ создания Set
a = set('hello')
print(type(a))
print(a)

# Второй способ в фигурный скобках как map только без ключей
b = {12, 34, 12}  # 12 будет только одна.
b.add(24)
print(b)

# Неизменяемый Set
c = frozenset('immutable')
print(c)

# Удаление дубликатов при помощи set()
d = ['1', '1', '2']
print(d)
s = set(d)
print(s)

# Методы для множеств
print(len(d))

x = '1'
print(x in d)

# равенство множеств
t = {4, 6, 8}
r = {3, 5, 7}
print(t.isdisjoint(r))  # если нет не одного общего элемента то True. Если хоть 1 общий есть то False.

# Множества можно проверять на равенства через ==ю
e = {1, 3, 2}
m = {1, 2, 3}
print(e == m)  # Если все элементы равны порядок не важен.

# Объединение множеств.
p = {1, 5, 2}
l = {3, 5, 9}
p.update(l)
print(p)


# Оставляет только пересекающиеся значения.
p.intersection_update(l)
print(p)

# Удаление без ошибки если элемента нет.
p.discard(0)

# Удаляет первый элемент и возвращает его.
print(p.pop())