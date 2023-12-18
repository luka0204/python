# arr = [1,2,3,4]
# print ('original array = ' + str(arr))
# arr[0] = 2
# print ('modified array = ' + str(arr))
# print ('reversed array = ' + str(arr[::-1]))


# arrReversed = arr.reverse
# arrReversedStr = str(arrReversed)
# print (arrReversedStr)
 






# arr = [1,2,3]
# a,b,c = arr

# print (b)

# StrArr = ['1','2','3','4']
# StrArrJoin = ''.join(StrArr)
# StrArrList = list(StrArrJoin)

# # StrArrAppended = StrArr.insert(4,'5')
# # StrArrRemove = StrArr.remove('1')
# StrArrPop = StrArr.pop(0)

# print (StrArr)
# print (StrArrJoin)
# print (StrArrList)
# print (StrArr.count("1"))



# my_tuple = (1,)
# print (my_tuple)

# my_list = [1,2,3,4]
# my_list_first = my_list[0]
# my_list_last = my_list[-1]
# my_list[0] = my_list_last
# my_list[-1] = my_list_first
# print(my_list)


meal_list_lunch_dinner = {
247:'Burger King Hamburger',
300:'McDonalds Cheesy',
282:'Subway BLT',
300:'Small Steak',
543:'Medium Steak',
724:'Large Steak',
851:'Mac&Cheese large serving',
556:'Mac&Cheese medium serving',
298:'Mac&Cheese small serving',
183:'Greek salad',
370:'Caesar salad',
204:'Tuna salad'
}

meal_list_breakfast = {
333:'Medium serving of greek yogurt',    
190:'Plain croissant',
341:'Starbucks almond croissant',
162:'Peanut butter toast',
159:'Chocolate spread toast'
}

cal_input = int(input())
menu = [
    {"name":"Small serving of oats with milk", "cals": 400},
    {"name":"Medium serving of oats with milk", "cals": 800},
    {"name":"Small serving of greek yogurt", "cals": 166}
]

for i in menu:
    if i['cals']<cal_input:
        print(i["name"])

