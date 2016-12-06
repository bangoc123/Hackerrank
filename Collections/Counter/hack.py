from collections import Counter

myList = [2,3,4,5,6,8,7,6,5,18]

print Counter(myList)

def purchase(order, revenue):
    size = int(order[0])
    price = int(order[1])
    quantity = 1
    if Quantity.get(size) != None:
        actualQuantity = Quantity[size]
        if quantity <= actualQuantity:
            Quantity[size] = actualQuantity - quantity
            print Quantity
            revenue = price * quantity
            return revenue
        else:
            return 0
    else:
        return 0

revenue = 0


# X = raw_input("")
# if 0 < X < 10*10*10:
#     for i in range(0, X):


n = raw_input("")
purchase_list = {}

Quantity = {5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 7: 1, 8: 1, 18: 1}

for i in range(0, int(n)):
    order = raw_input("").split(" ")
    print order
    revenue = revenue + purchase(order, revenue)
    print revenue











