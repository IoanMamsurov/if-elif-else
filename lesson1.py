first = int(input())
second = int(input())
third = int(input())
if first==second==third:
    print(3)
elif first == second:# можно сократить с оператором or. Получится elif first==second or second==third or first==third:
    print(2)
elif second == third:
    print(2)
elif first == third:
    print(2)
elif first != second != third:
    print(0)