import sys,time
def print_slow(str):
    for letter in str + '\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
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
order = []
orders = [] 
print_slow('Hello, and welcome to the Los Pollos Hermanos family!')
def Waiter():
    while True:
        print_slow('Choose action: "add order" or "exit"')
        answer = str(input())
        match answer:
            case 'add order':
                print_slow('Type name of order')
                name = str(input())
                order.append({'name': name,})
            case 'exit':
                    break
def Chef():
    while True:
        print_slow('Choose action: "show order" or "exit"')
        answer = str(input())
        match answer.lower():
            case 'show order':
                if order == []:
                    print_slow('there are no orders')
                else:
                    print(order[order.index(order[0])])
                    print_slow('Enter order operation')
                    print_slow('"+" - the order is finished, "-" - the order is not finished')
                    order_operation = str(input())
                    match order_operation:
                        case '+':
                            order.pop(0)
                        case '-':
                            print_slow('come back when you are finished')
                            break
            case 'exit':
                break                                
while True:
    print_slow ('Who do you want to login as?, or type "exit" to exit program')
    print_slow ('"chef","waiter" or "exit"')
    answer = str(input())
    match answer.lower():
        case 'chef':
            print_slow('you have successfully logged in as a chef')
            Chef();
        case 'waiter':
            print_slow('you have successfully logged in as a waiter')
            Waiter();
        case 'exit':
            break                