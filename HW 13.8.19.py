print("\033[33m{}\033[0m".format('*** Если количество приобретаемых билетов больлше 3, то Вам положена скидка 10% от полной стоимости заказа! ***'))
try:
    number_of_tickets = int(input('Введите количество билетов (целое число больше 0): '))
    while number_of_tickets <= 0:
        print("\033[31m{}\033[0m".format('*** Вы ввели неккоректное количество билетов, повторите попытку! ***'))
        number_of_tickets = int(input('Введите количество билетов: '))
except ValueError:
    print("\033[31m{}\033[0m".format('*** Неккоректный ввод!!! Запустите программу заново! ***'))
else:
    full_price = 0
    print("\033[33m{}\033[0m".format('\n*** Введите количество полных лет каждого посетителя (0 - если ребенку нет года!). ***'))
    for i in range(1, number_of_tickets+1):
        while ValueError:
            try:
                age = int(input(f'    Возраст посетителя билета № {i}: '))
                while age < 0:
                    print("\033[31m{}\033[0m".format('    *** Возраст не может быть меньше нуля! ***'))
                    age = int(input(f'    Возраст посетителя билета № {i}: '))
            except ValueError:
                print("\033[31m{}\033[0m".format('    *** Ввод некорректный, повторите ввод! ***'))
            else:
                if 0 <= age < 18:
                    price = 0
                elif 18 <= age <= 25:
                    price = 990
                else:
                    price = 1390
                full_price = full_price + price
                break
    if number_of_tickets > 3:
        discount_price = full_price - (full_price * 0.01)
        print('\nВам положена скидка 10%. Полная стоимость вашего заказа с учетом скидки: ', float(discount_price))
    else:
        print('\nНа ваш заказ скидка не распространяется. Полная стоимость вашего заказа: ', full_price)