import TransportCompany as TC
import Client as c
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
                    print(f"Имя клиента: {i.name}, вес груза: {i.cargo_weight}, {if i.is_vip==True: f="Клиент ВИП" else: f="Обычный клиент"} {f}")

        case 2:
            if not TC.vehicles:
                print("Клиентов нет")
            else:
                for i in TC.vehicles:
                    print(f"{if type(i) is Ship: f=(f"Имя: {i.name}, ID: {i.vehicle_id}, Грузоподъемность: {i.capacity}, Загруженность: {i.current_load}, Список клиентов: {i.clients_list}") else: f=(f"Есть ли холодильник: {i.is_refrigerated}, ID: {i.vehicle_id}, Грузоподъемность: {i.capacity}, Загруженность: {i.current_load}, Список клиентов: {i.clients_list}")}")

        case 3: # Добавляем записи
            a=input("Введите ваше имя")
            b=input("Введите вес вашего груза") 
            c=input("Являетесь ли вы вип клиентом?(True/False)")

        case 4:# Удаляем выбранную запись
            id_for_del = input("Введите id для удаления: ") # Запрашиваем id для удаления
            with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "r", encoding="utf-8") as file:
                fourth = json.load(file)

                lens = len(fourth)# Считываем длину файла для будущей прверки
                fourth = [star for star in fourth if str(star.get("id")) != id_for_del] # Перебираем список, но без элемента с выбранным id

                if len(fourth) < lens: # Проверяем удалился ли элемент
                    with open("C:\Users\KudlaIva_89\Desktop\Лабы Кудлаш\lr7\task3\dump.json", "w", encoding="utf-8") as file:
                        json.dump(fourth) # Сохраняем изменения
                    print("Запись удалена.")
                else:
                    print("Запись с таким id не найдена.")

        case 5:
            x=0 # Завершаем цикл