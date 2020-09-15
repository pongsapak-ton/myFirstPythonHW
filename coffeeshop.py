def showspec(water, milk, coffee, money, cups):  # func เเสดงข้อมูล ของเครื่องกาเเฟ
    print("The coffee machine has : ")
    print(water, " of water ")
    print(milk, " of milk")
    print(coffee, " of coffee beans")
    print(cups, " of disposable cups")
    print(money, " of money")


def buys(water, milk, coffee, money, cups):  # func เลื่อก ประเภท ของกาเเฟ
    print("What do you want to buy  1- espresso, 2 - latte, 3 - cappuccino :")
    cof = int(input("> "))
    if cof == 1:  # เงื่อนใข การซื้อ กาเเฟดำ
        print("----Espresso----")
        water -= 250
        coffee -= 16
        money += 4
        cups -= 1

    elif cof == 2:  # เงื่อนใข การซื้อ กาเเฟ ลาเต้
        print("----Latte----")
        water -= 350
        milk -= 75
        coffee -= 20
        money += 7
        cups -= 1

    elif cof == 3:  # เงื่อนใข การซื้อ กาเเฟ คาปูชิโน่
        print("----Cappucino----")
        water -= 200
        milk -= 100
        coffee -= 12
        money += 6
        cups -= 1
    showspec(water, milk, coffee, money, cups)


def fills(water, milk, coffee, cups):  # func เติม วัตถุดิบ
    print("Write how many ml of water do you  want to add : ")
    water += int(input("> "))
    print("Write how many ml of milk do you  want to add : ")
    milk += int(input("> "))
    print("Write how many grams of coffee beans  do you  want to add : ")
    coffee += int(input("> "))
    print("Write  how many disposable cups of coffee do you  want to add : ")
    cups += int(input("> "))
    showspec(water, milk, coffee, money, cups)


def take(water, milk, coffee, money, cups):  # func เอาเงินออก
    money -= int(input("I gave you $ "))
    showspec(water, milk, coffee, money, cups)
    return money


if __name__ == '__main__':
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550
    showspec(water, milk, coffee, money, cups)
    # เลือก ซื่้อ เติมวัตถุดิบ หรือ เอาเงินออก
    print("Write action (buy, fill ,take):")
    ac = str(input("> "))
    if ac == 'buy':
        buys(water, milk, coffee, money, cups)
    if ac == 'fill':
        fills(water, milk, coffee, cups)
    if ac == 'take':
        take(water, milk, coffee, money, cups)
