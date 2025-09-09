#массив
l = ['a','1','b','2','c','3'] 	#список в переменной
l_1 = l[0::2] 			#срезаем
l_2 = l[1::2]
del l 				#очищаем переменную
print(l_1,l_2,sep='\n\n') 	#вывод


#стек
from collections import deque	#импорт библиотеки
stack = deque()
stack.append('a')		#добавление объектов
stack.append('b')
stack.append('c')
print(f'Stack: {list(stack)}')	#вывод стека