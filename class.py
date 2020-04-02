import random

"""
Klasy

Model zawodnika 
Utwórz klasę Player, która będzie opisywać zawodnika piłki nożnej. Zawodnika charakteryzują następujące cechy:

"nazwa": imię i nazwisko
wiek
liczba strzelonych goli
nazwa klubu
numer na koszulce
pozycja na której gra
liczba kartek
W konstruktorze klasy wymagaj podania nazwy zawodnika. Nowo tworzony zawodnik ma wiek o wartości None i liczbę goli 0.
W trakcie tworzenia nowego zawodnika wymagamy podania jego "nazwy" (imienia i nazwiska w jednym stringu), wieku oraz pozycji na której gra. Nowo tworzony zawodnik nie ma klubu (domyślna wartość None) oraz numeru na koszulce (domyślna wartość 0). Nie strzelił także żadnych bramek ani nie ma czerwonych kartek. Dodatkowe gettery i settery:

field_number- getter i setter
cards - getter
club - getter
position - getter

Z pomocą dekoratorów property utwórz metody dla pól:

name - getter i setter (pobieranie i zmiana)
age - getter i setter (pobieranie i zmiana)
goals - getter
Utwórz dla zawodnika metodę score() służącą do strzelania goli, która z każdym wykonaniem zmienia liczbę strzelonych przez niego goli o 1.

Zawodnik ma następujące akcje, które może wykonać:

score() - oznacza strzelenie bramki. Akcja ta zwiększa liczbę strzelonych goli o 1. Akcja nie powinna być możliwa, jeśli zawodnik nie ma klubu. Drukujemy wtedy informację: Choose your club! i nie zmieniamy liczby goli.
change_position(new_position) - pozwala na zmianę pozycji zawodnika, ale zwiększa też jego wiek o 2 (czas potrzebny na wytrenowanie)
transfer(club) pozwala na zmianę klubu w którym gra zawodnik, ale kasuje wszystkie jego dotychczasowe bramki (ustawia na 0)
foul() - daje 50% szans na otrzymanie kartki. W przypadku otrzymania kartki liczba kartek na koncie zawodnika zwiększa się o 1 i drukowany jest napis Got a card!
"""

class Player:
    def __init__(self, name, position, age):
        self._name = name
        self._age = age
        self._goals = 0
        self._field_number = 0
        self._cards = 0
        self._club = None
        self._position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def goals(self):
        return self._goals

    @property
    def field_number(self):
        return self._field_number

    @field_number.setter
    def field_number(self, field_number):
        self._field_number = field_number

    @property
    def cards(self):
        return self._cards

    @property
    def club(self):
        return self._club

    @property
    def position(self):
        return self._position

    def score(self):
        if self._club == None:
            print(f'Choose your club!')
        else:
            self._goals += 1

    def change_position(self, new_position):
        self._position = new_position
        self._age += 2

    def transfer(self, club):
        self._club = club
        self._goals = 0

    def foul(self):
        if random.randint(1, 2) == 1: #50% szans na 1
            self._cards += 1
            print(f'Got a card!')

my_player = Player('Test Player', 'defender', 23)
print(my_player.age)  # powinno dać 23
print(my_player.goals)  # powinno dać 0
my_player.score()  # powinno wydrukować informację o braku klubu
print(my_player.goals)  # powinno dać dalej 0
my_player.transfer('Liverpool FC')
my_player.field_number = 7
my_player.score()
print(my_player.goals)  # powinno dać 1
my_player.change_position('attacker')
print(my_player.age)  # powinno dać 25
print(my_player.position)  # powinno dać 'attacker'
my_player.foul()
my_player.foul()
my_player.foul()
print(my_player.cards)

print(f'eksperyment')
eks = Player("Kryształowicz", 'attacker', 30)
print(f'{eks.field_number}')
eks.field_number = 89
print(f'{eks.field_number}')
