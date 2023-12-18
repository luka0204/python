#HW-1
#task-1
print ('введите числа для последовательности, ноль чтобы закончить')
my_list = []
while True:
    data = input()
    my_list.append(data)
    if data == "0":
        break

list_sorted = sorted(my_list)
list_sorted.pop(0)
print (list_sorted)

for x in list_sorted:
    print (x)

#task-2
print ('введите числа для последовательности, ноль чтобы закончить')
my_list = []
while True:
    data = input()
    my_list.append(data)
    if data == "0":
        break

    list_sorted = sorted(my_list)
list_sorted.pop(0)
list_sorted.pop(-1)
print (f'list without extremes {list_sorted}')
print (f'original list {my_list}')

