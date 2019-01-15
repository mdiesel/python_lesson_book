




"""
Задание 4.1
Обработать строку NAT таким образом, чтобы в имени интерфейса вместо
FastEthernet было GigabitEthernet.
Ограничение: Все задания надо выполнять используя только пройденные темы.
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

Ответ:

replace()
Замена последовательности символов в строке на другую последовательность (метод
replace() ):

"""


str_nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
print("old str:"+str_nat)

str_nat = str_nat.replace("FastEthernet","GigabitEthernet")

print("new str:"+str_nat)



"""


Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат
XXXX.XXXX.XXXX
Ограничение: Все задания надо выполнять используя только пройденные темы.
MAC = 'AAAA:BBBB:CCCC'

"""


MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.replace(":",".")

print(MAC)




"""
------------------------------------------------------------------------------------
Задание 4.3
Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
Ограничение: Все задания надо выполнять используя только пройденные темы.
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'


"""

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

#_config = (CONFIG.split())[-1].split(',')

#print(_config)

"""
split()
Метод split() разбивает строку на части, используя как разделитель какой-то символ
(или символы). По умолчанию, в качестве разделителя используются пробелы. Но в
скобках можно указать любой разделитель.
В результате, строка будет разбита на части по указанному разделителю и
представлена в виде частей, которые содержатся в списке:

----------------------------------------------------------------------------------------
"""


"""
Задание 4.4


Из строк command1 и command2 получить список VLANов, которые есть и в команде
command1 и в команде command2.
Для данного примера, результатом должен быть список: [1, 3, 100] Этот список
содержит подсказку по типу итоговых данных.
Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
command_1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command_2 = 'switchport trunk allowed vlan 1,3,100,200,300'

temp_temcommand_1 = (command_1.split())[-1].split(',')
temp_temcommand_2 = (command_2.split())[-1].split(',')

#print(temp_temcommand_1)
#print(temp_temcommand_2)

"""
Пересечение множеств можно получить с помощью метода intersection() или
оператора & :
"""

temp_1 = set(temp_temcommand_1)
temp_2 = set(temp_temcommand_2)

print(temp_1)
print(temp_2)

temp_3 = list(temp_1 & temp_2)

temp_str = int(temp_3[1])+int(temp_3[2])

print(temp_str)

print(temp_3)


"""

Задание 4.5
Список VLANS это список VLANов, собранных со всех устройств сети, поэтому в
списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по
возрастанию номеров.
Ограничение: Все задания надо выполнять используя только пройденные темы.
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
"""

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

VLANS = sorted(VLANS)

print(VLANS)

VLANS = sorted(list(set(VLANS)))

print(VLANS)



"""
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в
виде:
Protocol: OSPF
Prefix: 10.0.24.0/24
AD/Metric: 110/41
Next-Hop: 10.0.13.3
Last update: 3d18h
Outbound Interface: FastEthernet0/0

ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

"""


ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

temp_ospf_route = ospf_route.split()

print(temp_ospf_route)

print('Prefix:'+' '+temp_ospf_route[1])

print('AD/Metric:',(temp_ospf_route[2]).strip('[]'))
print('Next-Hop:',(temp_ospf_route[4]).strip(','))
print('Last update:',(temp_ospf_route[5]).strip(','))
print('Outbound Interface:',(temp_ospf_route[6]))














