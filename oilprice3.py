# by pongsapak fungthawewong
from zeep import Client

from lxml import etree

client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

result = client.service.CurrentOilPrice("en")

root = etree.fromstring(result)

# define empty list

GasProduct = []
GasPrice = []

# traverse oil price list and print out


def Get_Oilprice():  # func ดึงราคาน้ำมันจาก เว็บไชต์
    for r in root.xpath('FUEL'):
        product = r.xpath('PRODUCT/text()')[0]
        price = r.xpath('PRICE/text()') or [0]
        GasProduct.append([product, float(price[0])])
        GasPrice.append(float(price[0]))
    return GasPrice, GasProduct


def Main_Show():  # func หน้า home
    print("\n\n********************************************************************************")
    print("****                                                                        ****")
    print("****                           OIL PRICE  PROGRAM                           ****")
    print("****                     BY   PONGSAPAK  FUNGTHAWEWONG                      ****")
    print("****                                                                        ****")
    print("********************************************************************************\n\n")


def Show_oilprice(list):  # func  เเสดง ค่าน้ำมัน
    print("\n\n********************************************************************************")
    print("****                                                                        ****")
    print("****                     1.Gasoline 95 ",
          GasPrice[0], "BATH                          ****", )
    print("****                     2.Gasoline 91 ",
          GasPrice[1], "BATH                            ****", )
    print("****                     3.Diesel      ",
          GasPrice[2], "BATH                          ****", )
    print("****                     4.Gasohol 91  ",
          GasPrice[3], "BATH                          ****", )
    print("****                     5.Gasohol E20 ", 
          GasPrice[4], "BATH                          ****", )
    print("****                     6.Gasohol 95  ",
          GasPrice[6], "BATH                          ****", )
    print("****                                                                        ****")
    print("********************************************************************************")


def Mains():
    print("\n\n********************************************************************************")
    print("****                                                                        ****")
    print("****                     1. money to litre                                  ****")
    print("****                     2. litre to money                                  ****")
    print("****                                                                        ****")
    print("********************************************************************************\n\n")


def Show_money(sums):  # func  เเสดง เงิน
    print("********************************************************************************")
    print("****                                                                        ****")
    print("****                        %.2f" %
          sums, "liter                                     ****")
    print("****                                                                        ****")
    print("********************************************************************************\n\n")


def Show_liter(sums):  # func  เเสดง ลิตร
    print(
        "********************************************************************************")
    print(
        "****                                                                        ****")
    print("****                        %4d" %
          sums, "bath                                     ****")
    print(
        "****                                                                        ****")
    print(
        "********************************************************************************\n\n")


def Select_num(list):  # เลือกระหว่าง เงินเป็นลิตร หรือ ลิตรเป็นเงิน
    cal = int(input("\nSelect number :"))
    if cal == 1:
        Money(list)
    elif cal == 2:
        Liter(list)
    else:
        print("choice error'")


def Money(list):  # func คำณวน จาก เงินเป็นลิตร
    print("\nMoney to litre")
    oil = int(input("Type of oil :"))
    while oil > 6:
        oil = int(input("Enter Type of oil Again:"))
    value = int(input("Money :"))
    if oil == 1:
        sums = value / GasPrice[0]
        Show_money(sums)

    elif oil == 2:
        sums = value / GasPrice[1]
        Show_money(sums)

    elif oil == 3:
        sums = value / GasPrice[2]
        Show_money(sums)
    elif oil == 4:
        sums = value / GasPrice[3]
        Show_money(sums)
    elif oil == 5:
        sums = value / GasPrice[4]
        Show_money(sums)
    elif oil == 6:
        sums = value / GasPrice[6]
        Show_money(sums)
    else:
        print("Error")


def Liter(list):  # func คำณวน จาก ลิตรเป็นเงิน
    print("\nlitre to money")
    oil = int(input("Type of oil :"))
    while oil > 6:
        oil = int(input("Enter Type of oil Again:"))
    value = int(input("Liter  :"))
    if oil == 1:
        sums = value * GasPrice[0]
        Show_liter(sums)
    elif oil == 2:
        sums = value * GasPrice[1]
        Show_liter(sums)
    elif oil == 3:
        sums = value * GasPrice[2]
        Show_liter(sums)
    elif oil == 4:
        sums = value * GasPrice[3]
        Show_liter(sums)
    elif oil == 5:
        sums = value * GasPrice[4]
        Show_liter(sums)
    elif oil == 6:
        sums = value * GasPrice[6]
        Show_liter(sums)
    else:
        print("Error")


def GoOut(list):  # func go out
    print("********************************************************************************")
    print("****                                                                        ****")
    print("****                        Do You Go Or Exit                               ****")
    print("****                                                                        ****")
    print("********************************************************************************")
    ex = input("\nExit : ")
    while True:
        if ex == "":
            print(
                "********************************************************************************")
            print(
                "****                                                                        ****")
            print(
                "****                          Exit Program                                  ****")
            print(
                "****                                                                        ****")
            print(
                "********************************************************************************")
            break
        else:
            Main_Show()
            Mains()
            Show_oilprice(Get_Oilprice())
            Select_num(list)
            GoOut(list)


Main_Show()
Mains()
Show_oilprice(Get_Oilprice())
Select_num(list)
GoOut(list)
