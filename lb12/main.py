from TransportCompany import TransportCompany as T
from Client import Client as clint
from Vehicle import Vehicle as vh
from Ship import Ship as sp
from Van import Van as vn

f = ""
x = 1
TC = T("ТК 'Железо-стале-шлако-блок'")
while x==1:

    print(">>  Вывод клиентов << - 1")
    print(">>  Вывод транспорта << - 2")
    print(">>  Добавить клиента << - 3")
    print(">>  Добавить транспорт << - 4")
    print(">>  Оптимизировать груз по Транспортных Средствам << - 5")
    print(">>  Выход их программы << - 6")
    print(" ")


    comand = int(input("Выберите пункт(например:1): "))
    if(comand <= 0 or comand > 7):
        print("Неверное число")
        print(" ")
    else:
        match comand:
            case 1:
                if not TC.clients:
                    print("Клиентов нет")
                else:
                    for i in TC.clients:
                        if i.is_vip==True:
                            status = "Клиент ВИП"
                        else:
                            status = "Обычный клиент"
                        print(f"Имя клиента: {i.name}, вес груза: {i.cargo_weight}, {status}")

            case 2:
                if not TC.vehicles:
                    print("Транспортных средств нет")
                else:
                    for i in TC.vehicles:
                        if type(i) is sp:
                            print(f"Корабль; Имя: {i.name}")
                        else:
                            print(f"Фура; Есть ли холодильник: {i.is_refrigerated}")


            case 3: # Добавляем записи
                a = input("Введите ваше имя")
                b = int(input("Введите вес вашего груза") )
                c = input("Являетесь ли вы вип клиентом?(True/False)")
                if c=="True":
                    c=True
                else:
                    c=False
                d = clint(a, b, c)
                TC.add_client(d)

            case 4:
                cls = input("Корабль или грузовик(ship/van)")
                if cls == "ship":
                    a = input("Введите имя корабля")
                    b = int(input("Введите максимально перевозимый вес"))
                    z = sp(b, a)
                    TC.add_vehicle(z)
                else:
                    a = bool(input("Есть ли холодильник?(писать True/False)"))
                    b = int(input("Введите максимально перевозимый вес"))
                    z = vn(b, a)

            case 5:
                TC.optimize_cargo_distribution()
                print("\n--- Результат распределения ---")
                for i in TC.vehicles:
                    print(i)
                    if i.clients_list:
                        for c in i.clients_list:
                            print(f" - {c.name}, груз: {c.cargo_weight}т")
                    else:
                        print("(пусто)")
            case 6:
                print("Программа закончена")
                x=0