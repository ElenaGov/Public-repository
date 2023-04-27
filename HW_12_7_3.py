per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))
Bank1 = (money*per_cent.get('ТКБ')) / 100
Bank2 = (money*per_cent.get('СКБ')) / 100
Bank3 = (money*per_cent.get('ВТБ')) / 100
Bank4 = (money*per_cent.get('СБЕР')) / 100
deposit = [Bank1, Bank2, Bank3, Bank4]
p = list(map(int, deposit))
print('deposit = ', p)
print('Максимальная сумма, которую вы можете заработать: ', max(p))