from random import randint


class Card:
	def __init__(self, name):
		bag = [x for x in range(1, 91)]  # Мешок с бочками.
		self.card = [
		    __class__.gen_string(bag),
		    __class__.gen_string(bag),
		    __class__.gen_string(bag)
		]
		self.name = name
		self.count_barrel = 15  # осталось бочек на карточке

	@staticmethod
	def gen_string(bag):
		string = ['' for _ in range(9)]
		for x in range(8, 3, -1):
			digit = randint(0, x)  # Номер элемента строки, который заполняю
			while string[digit] != '':  # если элемент уже не пустой
				digit += 1
			string[digit] = bag.pop(randint(0, len(bag) - 1))
		return string

	def __str__(self):
		rez = '{:-^26}\n'.format(self.name)
		for x in range(3):
			rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
		return rez + '--------------------------'


player = Card(' Игрок ')
computer = Card(' Компьютер ')

bag = [x for x in range(1, 91)]  # Мешок с бочками.
while True:
	if len(bag) < 1:
		print('Бочёнки закончились. Результат:\n'
		      'у компьютера осталось {} числа/чисел,\n'
		      'у игрока осталось {} числа/чисел.'.format(
		          computer.count_barrel, player.count_barrel))
		break
	barrel = bag.pop(randint(0, len(bag) - 1))
	print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag)))
	print(computer)
	print(player)
	reply = input('Зачеркнуть цифру? (y/n/q)')
	reply = reply.lower()
	while len(reply) == 0 or reply not in 'ynq':
		print('\n\nНезивестный ввод\n')
		print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
		print(computer)
		print(player)
		reply = input('Зачеркнуть цифру? (y/n/q)')
		reply = reply.lower()

	if reply == 'q':
		print('Выхожу')
		break
	elif reply == 'y':
		test = False 
		for x in range(3):
			if barrel in player.card[x]:
				test = True
				player.card[x][player.card[x].index(barrel)] = '-'
				player.count_barrel -= 1
			if barrel in computer.card[x]:
				computer.card[x][computer.card[x].index(barrel)] = '-'
				computer.count_barrel -= 1
		if test:
			if player.count_barrel < 1:
				print('Вы победили!')
				break
			elif computer.count_barrel < 1:
				print('Компьютер победил!')
				break
		else:
			print('Вы проиграли! Такого числа в вашей карточке нет')
			break
	elif reply == 'n':
		test = False
		for x in range(3):
			if barrel in player.card[x]:
				print('Вы проиграли! Такое число есть на вашей карточке!')
				test = True
				break
			if barrel in computer.card[x]:
				computer.card[x][computer.card[x].index(barrel)] = '-'
				computer.count_barrel -= 1
		if test:
			break
		if player.count_barrel < 1:
			print('Вы выиграли!')
			break
		elif computer.count_barrel < 1:
			print('Компьютер выиграл!')
			break
