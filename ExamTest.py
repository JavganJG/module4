cash = 0
quantProducts ={"shovel": 23,"Pool": 456,"Axe":234}
priceProducts ={"shovel": 7,"Axe":12,"Pool":200}
def detectProduct(code):
    for i in priceProducts:
        if code == i:
            return True
    for i in quantProducts:
        if code == i:
            return True
    return False


def getPriceProduct(code):
    if detectProduct(code):
        return priceProducts[code]
    else: 
        return None
def getQuanityProduct(code):
    if detectProduct(code):
        return quantProducts[code]

def getDetailProduct(code):
    return priceProducts+": "+str(priceProducts[code])+"€, "+str(quantProducts[code])

def setPriceProduct(code, price):
    if detectProduct(code):
        priceProducts[code]=int(price)
        return True
    else:
        return False

def saleProduct(code):
    if detectProduct:
        newcash = cash + priceProducts[code]
        quant = quantProducts[code] -1
        quantProducts[code]=quant
        return True
    return False
def replaceProduct(code,quantity):
    if detectProduct(code):
        quant = getQuanityProduct(code)
        price = getPriceProduct(code)
        if cash >= quant+price:
            quantProducts[code]= quantProducts[code] + quant
            return True
        else:
            return False
    else:
        return False
def addQuantProduct(code, quantity):
    if detectProduct(code):
            quant = getQuanityProduct(code) +quantity
            quantProducts[code] = quant
def getFullStock():
    index = ("Code", "Units", "Price")
    stock = []
    stock.append(index)
    for i in priceProducts:
         stock.append(str([i, getQuanityProduct(i),getPriceProduct(i)]))
    return stock

def menu():
    print("=====================")
    print("1.-Show full store detail")
    print("2.-Sales")
    print("3.-Replace")
    print("4.-Change price of product")
    print("5.-Exit")
    print("=====================")
    return input("Choose a option: ")

    


while True:
    opcion = int(menu())
    if(opcion == 1):
        stock = getFullStock()
        for x in stock:
            print(x, end = "\n")
    elif(opcion == 2):
        product = input("Enter product code: ")
        if saleProduct(product):
             print("Successful sale!")
        else:
            print("Error, item does not exist or is out of stock!")

    elif (opcion == 3):
        product = input("Enter product code: ")
        units = input ("Units to replace: ")
        if replaceProduct(product,units):
            print("Correct replacement!")
        else:
            print("There is no cash in the box to replace!")
    elif (opcion == 4):
        product = input("Enter product code: ")
        price = input("New price for product: ")
        if setPriceProduct(product, price):
            print("Updated price!")
    elif (opcion == 5):
        break