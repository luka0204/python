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

cal_input = int(input())
menu = [
    {"name":"Small serving of oats with milk", "cals": 400,"type": "breakfast"},
    {"name":"Medium serving of oats with milk", "cals": 800},
    {"name":"Chocolate spread toast", "cals": 159,"type": "breakfast"},
    {"name":"Peanut butter toast", "cals": 162,"type": "breakfast"},
    {"name":"Starbucks almond croissant", "cals": 341,"type": "breakfast"},
    {"name":"Plain croissant", "cals": 190,"type": "breakfast"},
    {"name":"Tuna salad'", "cals": 204},
    {"name":"Caesar salad", "cals": 370},
    {"name":"Greek salad", "cals": 183},
    {"name":"Mac&Cheese medium serving", "cals": 556},
    {"name":"Mac&Cheese large serving", "cals": 851},
    {"name":"Large Steak", "cals": 724},
    {"name":"Medium Steak", "cals": 543},
    {"name":"Small Steak'", "cals": 300},
    {"name":"Subway BLT", "cals": 282},
    {"name":"Burger King Hamburger", "cals": 247},
    {"name":"McDonalds Cheesy", "cals": 300},
]

for i in menu:
    if i['cals']<cal_input:
        print(i["name"])




