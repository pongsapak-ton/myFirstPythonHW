ex = ""  # กำหนด ตัวเเปร ex ไห้เป็น ช่องว่าง
while True:
    if ex == "":  # ถ้า ตัวเเปร ex ว่าง ไห้ทำเงื่อนไข
        # Oil price requested from PTT
        #
        # Vara Varavithya Sept 08 2020
        #

        # import related library for HTTP and XML

        from zeep import Client
        from lxml import etree

        client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

        result = client.service.CurrentOilPrice("en")

        root = etree.fromstring(result)

        # define empty list

        GasProduct = []
        GasPrice = []

        # traverse oil price list and print out
        # ทำการดึง ราคาน้ำมันจาก เว็บไชต์
        for r in root.xpath('FUEL'):
            product = r.xpath('PRODUCT/text()')[0]
            price = r.xpath('PRICE/text()') or [0]

            GasProduct.append([product, float(price[0])])
            GasPrice.append(float(price[0]))

        print("\n\n********************************************************************************")
        print("****                                                                        ****")
        print("****                           OIL PRICE  PROGRAM                           ****")
        print("****                     BY   PONGSAPAK  FUNGTHAWEWONG                      ****")
        print("****                                                                        ****")
        print("********************************************************************************\n\n")

        # เเสดง ค่าน้ำมัน
        print("\n\n********************************************************************************")
        print("****                                                                        ****")
        print("****                     1.Gasoline 95 ",
              GasPrice[0], "BATH                          ****",)
        print("****                     2.Gasoline 91 ",
              GasPrice[1], "BATH                            ****",)
        print("****                     3.Diesel      ",
              GasPrice[2], "BATH                          ****",)
        print("****                     4.Gasohol 91  ",
              GasPrice[3], "BATH                          ****",)
        print("****                     5.Gasohol E20 ",
              GasPrice[4], "BATH                          ****",)
        print("****                     6.Gasohol 95  ",
              GasPrice[6], "BATH                          ****",)
        print("****                                                                        ****")
        print("********************************************************************************")

        print("\n\n********************************************************************************")
        print("****                                                                        ****")
        print("****                     1. money to litre                                  ****")
        print("****                     2. litre to money                                  ****")
        print("****                                                                        ****")
        print("********************************************************************************\n\n")

        # เลือกระหว่าง เงินเป็นลิตร หรือ ลิตรเป็นเงิน
        cal = int(input("\nSelect number :"))
        if cal == 1:  # คำณวน จาก เงินเป็นลิตร
            print("\nMoney to litre")
            oil = int(input("Type of oil :"))
            while oil > 6:
                oil = int(input("Enter Type of oil Again:"))
            value = int(input("Money :"))
            if oil == 1:
                sums = value / GasPrice[0]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %.2f" %
                      sums, "liter                                     ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")
            elif oil == 2:
                sums = value / GasPrice[1]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %.2f" %
                      sums, "liter                                     ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")
            elif oil == 3:
                sums = value / GasPrice[2]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %.2f" %
                      sums, "liter                                     ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")
            elif oil == 4:
                sums = value / GasPrice[3]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %.2f" %
                      sums, "liter                                     ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")
            elif oil == 5:
                sums = value / GasPrice[4]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %.2f" %
                      sums, "liter                                     ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")
            elif oil == 6:
                sums = value / GasPrice[6]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %.2f" %
                      sums, "liter                                     ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")

        elif cal == 2:  # คำณวน จาก ลิตร เป็น เงิน
            print("\nlitre to money")
            oil = int(input("Type of oil :"))
            while oil > 6:
                oil = int(input("Enter Type of oil Again:"))
            value = int(input("Liter  :"))
            if oil == 1:
                sums = value * GasPrice[0]
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
            elif oil == 2:
                sums = value * GasPrice[1]
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
            elif oil == 3:
                sums = value * GasPrice[2]
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
            elif oil == 4:
                sums = value * GasPrice[3]
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
            elif oil == 5:
                sums = value * GasPrice[4]
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
            elif oil == 6:
                sums = value * GasPrice[6]
                print(
                    "********************************************************************************")
                print(
                    "****                                                                        ****")
                print("****                        %4d" %
                      sums, "bath                                      ****")
                print(
                    "****                                                                        ****")
                print(
                    "********************************************************************************\n\n")

            else:
                print("choice error'")
        else:
            print("Error")

        print("********************************************************************************")
        print("****                                                                        ****")
        print("****                        Do You Go Or Exit                               ****")
        print("****                                                                        ****")
        print("********************************************************************************")
        ex = input("\nExit : ")
    elif ex != "":  # ถ้า ตัวเเปร ex มีการใส่ข้อมูล ไห้ ออกจากโปรเเกรม
        print("EXIT")
        break
