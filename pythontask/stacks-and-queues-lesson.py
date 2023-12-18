
# stack = []
# while True:
#     print (f'original stack {stack}')
#     print ('type "pop" to remove last element from stack, type "push" to add new element to stack,type "exit" to exit program')
#     answer = str(input())
#     match answer:
#         case 'pop':
#             stack.pop()
#             print(stack)

#         case 'push':
#             print('type number to append to stack')
#             inp = int(input())
#             print (inp)
#             stack.append(inp)

#         case 'exit':
#             break

queue = []
while True:
    print (f'original queue {queue}')
    print ('type "get" to remove last element from queue, type "put" to add new element to queue,type "exit" to exit program')
    answer = str(input())
    match answer:
        case 'get':
            print(queue[-1])
            queue.pop()
 

        case 'put':
            print('type number to append to queue')
            inp = int(input())
            print (inp)
            queue.insert(0,inp)

        case 'exit':
            break

        
