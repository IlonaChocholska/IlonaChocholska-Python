from math import pi
import random
"""
Poniższe zadania należy rozwiązać metodą list comprehension 

1 - imiona
Mając daną listę
names = ['Ada', 'Bill', 'Yen', 'Geralt', 'Ksawery', 'Candice', 'Esmeralda']
- utwórz nową listę name_lengths zawierającą długość (liczbę liter) każdego z imion.
- Dla tej samej listy names utwórz nową listę names_upper która zawierać będzie imiona zapisane dużymi literami.
2 - promienie i pola
Dla listy zawierającej promienie kół
radii = [12.1, 33, 9.3, 0.2, 190, 22.5]
- Utwórz drugą listę circle_areas która obliczy pole koła o danym promieniu
3 - Zniżki (dla chętnych, nieobowiązkowe)
mając daną listę 
discounts = [19, 21, -5.5, 7.8, 13.1, -10.2, -21, 10.1]
- utwórz nową listę która dla każdej ujemnej wartości wstawi 0.

Metody
1 - psi generator
Utwórz metodę o nazwie random_doggo, która zwraca losowe imię psa z listy
doggos = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
2 - matematyka
Utwórz metodę o nazwie greater_of_pair, która przyjmuje dwa argumenty: a, b będące liczbami. Metoda ma zwrócić większą z nich. Utwórz metodę average_of_3, która przyjmuje 3 liczby i zwraca ich średnią arytmetyczną.
3 - brzegi listy
Utwórz metodę margins, która jako argument przyjmuje dowolną listę input_list i zwraca jej pierwszy oraz ostatni element (zwraca dwie zmienne). Dodatkowo:
jeśli lista jest jednoelementowa -> zwraca pierwszy element oraz None jako drugą wartość
Jeśli lista jest pusta -> Zwraca obie wartości jako None i drukuje informację List is empty! Wykonaj metodę dla list:
['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
[12.1, 33, 9.3, 0.2, 190, 22.5]
[3, 5]
['Piłka']
[2]
[]
"""
print(f'1 - imiona')
names = ['Ada', 'Bill', 'Yen', 'Geralt', 'Ksawery', 'Candice', 'Esmeralda']
name_lengths = [len(name) for name in names]
print(name_lengths)

names_upper = [name.upper() for name in names]
print(names_upper)

print(f'\n2 - promienie i pola')
radii = [12.1, 33, 9.3, 0.2, 190, 22.5]
circle_areas = [round(radius * radius * pi, 2) for radius in radii]
print(circle_areas)

print('\n3 - Zniżki (dla chętnych)')
discounts = [19, 21, -5.5, 7.8, 13.1, -10.2, -21, 10.1]
discounts_not_negative = [0 if i < 0 else i for i in discounts]
print(discounts_not_negative)

print(f'\nMETODY: 1 - psi generator')
doggos = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']


def random_doggo(list):
    return random.choice(list)


print(f'losowe imię psa: {random_doggo(doggos)}')

print(f'\nMETODY: 2 - matematyka average_of_3')


def average_of_3(a, b, c):
    return (a + b + c) / 3


print(f'Średnia arytmetyczna liczb 4, 6 i 8 wynosi: {average_of_3(4, 6, 8)} '
      f'w zaokrągleniu do 2 miejsc po przecinku: {round(average_of_3(4, 6, 8), 2)}')
# nie podoba mi się, że round nie wymusza 2 miejsc po przecinku gdy wynik jest całkowity
# poszukałam, że można inaczej i teraz zawsze mam w zaokrągleniu 2 m-ca po przecinku
print(f'Średnia arytmetyczna liczb 5, 8 i 13 wynosi: {average_of_3(5, 8, 13)} '
      f'w zaokrągleniu do 2 miejsc po przecinku: {average_of_3(5, 8, 13):.2f}')

print(f'\nMETODY: 2 - matematyka greater_of_pair')


def greater_of_pair(a, b):
    return a if a > b else b


print(f'większą z liczb 2, 12 jest: {greater_of_pair(2, 12)}')
print(f'większą z liczb 13, 5 jest: {greater_of_pair(13, 5)}')
print(f'większą z liczb 7, 7 jest: {greater_of_pair(7, 7)}')

print(f'\nMETODY: 2 - matematyka greater_of_pair_bis')


def greater_of_pair_bis(a, b):
    return a if a > b else b if b > a else 'obie liczby są równe'


print(f'większą z liczb 2, 12 jest: {greater_of_pair_bis(2, 12)}')
print(f'większą z liczb 13, 5 jest: {greater_of_pair_bis(13, 5)}')
print(f'większą z liczb 7, 7 jest: {greater_of_pair_bis(7, 7)}')

print(f'\nMETODY: 3 - brzegi listy')
input_list_1 = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
input_list_2 = [12.1, 33, 9.3, 0.2, 190, 22.5]
input_list_3 = [3, 5]
input_list_4 = ['Piłka']
input_list_5 = [2]
input_list_6 = []


def margins(input_list):
    if len(input_list) == 0:
        print(f'List is empty!')
    return ('None', 'None') if len(input_list) == 0 \
        else (input_list[0], 'None') if len(input_list) == 1 \
        else (input_list[0], input_list[len(input_list) - 1])


print(f'Brzegi listy 1: {margins(input_list_1)}')
print(f'Brzegi listy 2: {margins(input_list_2)}')
print(f'Brzegi listy 3: {margins(input_list_3)}')
print(f'Brzegi listy 4: {margins(input_list_4)}')
print(f'Brzegi listy 5: {margins(input_list_5)}')
print(f'Brzegi listy 6: {margins(input_list_6)}')

print(f'\nMETODY: 3 - brzegi listy bis')
list_lists = [['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy'],
              [12.1, 33, 9.3, 0.2, 190, 22.5],
              [3, 5],
              ['Piłka'],
              [2],
              []]
for i in list_lists:
    print(f'Brzegi listy: {margins(i)}')