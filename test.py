list = []
def isvoid():
    void = True
    if len(list) > 0:
        void = False
    return void

def addnum():
    number = int(input("Add a number: "))
    return number
def addpos():
    pos = int(input("Add a position: "))
    return pos

def option1():
    num = addnum()
    list.append(num)
    value = "Correct"
    return value
def option2():
    pos= addpos()
    num= addnum()
    if pos <= len(list):
        list.insert(pos,num)
        value = "Correct"
    else:
        value = "Incorrect position"
def option3():
    value = len(list)
    return value
def option4():
    if not isvoid():
        del list[-1]
        value = "Correct"
    else:
        value = "Any element in the list"
    return value

def option5():
    if not isvoid():
        position = addpos()
        if position <= len(list):
          list.pop(position)
          value = "Correct"
        else:
            value = "Incorrect position"   
    else:
        value = "Any element in the list"
def option6():
    value = list.count(int(input("Select the number: ")))
    return value
def option7():
    list2 = []
    if not isvoid():
        num = addnum()
        count = 0
        es = False
        for elem in list:    
            if num == elem:
                list2.append(list.index(num,count))
                es = True
            count += 1 
        if es == False:
            value = "This number isn't in the list"
        else:
            value = list2
    else:
        value ="Any element in the list"

    

def menu():
    print("MENU")
    print("------------------------------")
    print("1.-Add a number to the list")
    print("2.-Add a number in a position in the list")
    print("3.-Show the length of the list")
    print("4.-Delete the last number in the list")
    print("5.-Delete a number in the list")
    print("6.-Count numbers")
    print("7.-Positions of a numbers")
    print("8.-Show the list")
    print("9.-Exit")
    print("------------------------------")
    opcion = int(input("Choose an option: "))
    return opcion
       

while True:
    opcion = menu()
    if(opcion==1):
        value = option1()
        print(value)
    elif(opcion==2):
        value = option2()
        print(value)
    elif(opcion==3):
        value = option3()
        print(value)
    elif(opcion==4):
        value = option4()
        print(value)
    elif(opcion==5):
        value = option5()
        print(value)
    elif(opcion==6):
        value = option6()
        print(value)
    elif(opcion==7):
        value = option7()
        print(value)
    elif(opcion==8):
        print(list)
    elif(opcion==9):
        break
    else:
        print("Choose a correct option")
