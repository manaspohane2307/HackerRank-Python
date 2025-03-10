if __name__ == '__main__':
    N = int(input())
    list1 = [input().strip() for i in range(N)]
    list2=[]
    for i in range(N):
        command = list1[i].split()
        operation=command[0]#first word is operation
        if operation == "insert":
            index = int(command[1])
            value = int(command[2])
            list2.insert(index,value)
        elif operation == "print":
            print(list2)
        elif operation == "remove":
            element = int(command[1])
            list2.remove(element)
        elif operation == "append":
            element = int(command[1])
            list2.append(element)
        elif operation == "sort":
            list2.sort()
        elif operation == "pop":
            list2.pop()
        elif operation == "reverse":
            list2.reverse()
            
        
        