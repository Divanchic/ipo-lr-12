import TransportCompany as TC
import Client as clint
import Vehicle as vh
#Кудлаш Иван
f = ""

while True:

print(">>  Вывод клиентов << - 1")
print(">>  Вывод транспорта << - 2")
print(">>  Добавить клиента << - 3")
print(">>  Добавить транспорт << - 4")
print(">>  Удалить клиента << - 5")
print(">>  Удалить транспорт << - 6")
print(">>  Выход их программы << - 7")
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
                    print(f"Имя клиента: {i.name}, вес груза: {i.cargo_weight}, {name}")

        case 2:
            if not TC.vehicles:
                print("Клиентов нет")
            else:
                for i in TC.vehicles:
                    if type(i) is Ship:
                        print(f"Имя: {i.name}, ID: {i.vehicle_id}, Грузоподъемность: {i.capacity}, Загруженность: {i.current_load}, Список клиентов: {i.clients_list}")
                    else:
                        print(f"Есть ли холодильник: {i.is_refrigerated}, ID: {i.vehicle_id}, Грузоподъемность: {i.capacity}, Загруженность: {i.current_load}, Список клиентов: {i.clients_list}")


        case 3: # Добавляем записи
            a=input("Введите ваше имя")
            b=int(input("Введите вес вашего груза") )
            c=input("Являетесь ли вы вип клиентом?(True/False)")
            d = clint(a ,b ,c)
            TC.add_client(d)

        case 4:
            cls = input("Корабль или грузовик(ship/van)")
            if cls == "ship":
                a = input("Введите имя корабля")
                b = int(input("Введите максимально перевозимый вес"))
                c = int(input("Введите загруженность вашего кораблся"))

                d = clint(a, b, c)
                TC.add_client(d)
            a = input("Введите ваше имя")
            b = int(input("Введите вес вашего груза"))
            c = input("Являетесь ли вы вип клиентом?(True/False)")
            d = clint(a, b, c)
            TC.add_client(d)

        case 5:
            x=0 # Завершаем цикл