menu ={
    "coffe":150,
    "pizza":120,
    "coldrinks":40,
    "choclate":70,
    "dhosa":120
}
# print("welcome to my restarunt !")
print("coffe: Rs150\npizza: Rs120\ncoldrinks: Rs40\nchoclate: Rs70\ndhosa: Rs120")

order_total=0
 
item_1=input("enter the name of item you want to order:")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item has {item_1} been added to your order")
else:
    print(f"orderd item {item_1} is not avaialable in menu.")
another_order=input("would you like to order other item? (yes/no) ")
if another_order=="yes":
    item_2=input("enter your second item which you would to like eat or drink:")
    if item_1 in menu:
        order_total+=menu[item_2]
        print(f"item {item_2} is added in your order")
    else:
        print(f"your orderd item {item_2} is not in our restarunt ,sorry.")
print(f"your total amount is now {order_total} ,thank you, please give us feedback!")
