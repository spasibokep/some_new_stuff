#Запрашиваем число, если меньше 0, то перезапускаем 
money = float(input('Введите общую сумму для вычета НДС '))
if money < 0:
	print ('Отрицательное число. Опасность! Опасность!') 
	while money < 0:
		money = float(input('Введите общую сумму для вычета НДС '))

#Запрашиваем, какая ставка НДС
percent = input('Введите нужный % НДС ')

#Считаем 
def get_vat(money, percent):
	try:
		money = float(money) 
		percent = int(percent)
		vat = money / 100 * percent
		vat = (round(vat, 2))
		return ('НДС составит {} рублей при общей сумме {} и ставке в {}%'.format(vat, float(money), int(percent)))
	except (TypeError, ValueError):
		print("Очепятка. Опасность! Опасность!")

result = get_vat(money, percent)

print(result)