from datetime import datetime

class Wezel():
    def __init__(self, dane = None) :
        self.dane = dane
        self.nastepny = None

class Lista() :
    def __init__(self) :
        self.head = None

    def append(self, dane) : 
        nowy_wezel = Wezel (dane)
        if self.head is None:
            self.head = nowy_wezel
            return
        licznik = self.head
        while licznik.nastepny != None:
            licznik = licznik.nastepny
        licznik.nastepny = nowy_wezel

    def dlugosc(self) :
        licznik = self.head
        if self.head is None:
            return 0
        wynik = 1
        while licznik.nastepny != None:
            licznik = licznik.nastepny
            wynik += 1
        return wynik

    def usun(self, i) :
        if self.head is None:
            print("Lista jest pusta")
            return
        if i >= self.dlugosc ()  or i < 0:
            print("Zły indeks")
            return
        if i == 0:
            self.head = self.head.nastepny
            return

        licznik = self.head
        pozycja = 0
        while licznik.nastepny != None:
            poprzednik = licznik
            licznik = licznik.nastepny
            if pozycja + 1 == i:
                poprzednik.nastepny = licznik.nastepny
                return
            pozycja += 1

    def wstaw(self, dane, miejsce):
        nowy_wezel = Wezel(dane)
        if miejsce == 0:
            nowy_wezel.nastepny = self.head
            self.head = nowy_wezel
            return
        licznik = self.head
        for i in range(miejsce - 1):
            licznik = licznik.nastepny
        nowy_wezel.nastepny = licznik.nastepny
        licznik.nastepny = nowy_wezel

    def wyswietl(self) : 
        if self.head is None:
            print("Lista jest pusta.")
            return
        licznik = self.head
        while licznik:
            print("Imię:",licznik.dane.imie,"|", "Nazwisko:", licznik.dane.nazwisko,"|","Pesel:", licznik.dane.pesel, "|","Wiek:", licznik.dane.wiek,"|","Płeć:", licznik.dane.plec,"|","Godzina przyjęcia:", licznik.dane.godz_przyjecia)
            licznik = licznik.nastepny

import re 

class Pacjent:
    def __init__(self, imie, nazwisko, pesel, wiek, plec, godz_przyjecia):
        self.imie = self.sprawdz_imie(imie)
        self.nazwisko = self.sprawdz_nazwisko(nazwisko)
        self.pesel = self.sprawdz_pesel(pesel)
        self.wiek = self.sprawdz_wiek(wiek)
        self.plec = self.sprawdz_plec(plec)

        try:
            datetime.strptime(godz_przyjecia, "%H:%M")
            self.godz_przyjecia = godz_przyjecia
        except ValueError:
            raise ValueError("Zły format czasu.")

    def sprawdz_imie(self, imie):
        if not re.match("^[a-zA-ZąĄęĘłŁńŃóÓśŚźŹżŻ]+$", imie):
            raise ValueError("Imię powinno zawierać tylko litery.")
        return imie[0].upper() + imie[1:].lower()

    def sprawdz_nazwisko(self, nazwisko):
        if not re.match("^[a-zA-ZąĄęĘłŁńŃóÓśŚźŹżŻ]+$", nazwisko):
            raise ValueError("Nazwisko powinno zawierać tylko litery.")
        return nazwisko[0].upper() + nazwisko[1:].lower()

    def sprawdz_pesel(self, pesel):
        if not re.match("^[0-9]{11}$", pesel):
            raise ValueError("Pesel powinien zawierać 11 cyfr.")
        return pesel

    def sprawdz_plec(self, plec):
        if not re.match("^[KMkm]{1}$", plec):
            raise ValueError("Nieprawidłowy format płci, wprowadź K lub M.")
        return plec.upper()
    
    def sprawdz_wiek(self, wiek):
        if not re.match("^\d{1,3}$", wiek):   
            raise ValueError("Wprowadź prawidłowy wiek.")
        wiek = int(wiek)
        if wiek > 130 or wiek == 0:
            raise ValueError("Wprowadź prawidłowy wiek.")
        return wiek
    

def wprowadzanie_danych():
    while True:
        try:
            imie = input("Wprowadź imię pacjenta: ")
            nazwisko = input("Wprowadź nazwisko pacjenta: ")
            pesel = input("Wprowadź pesel pacjenta: ")
            wiek = input("Wprowadź wiek pacjenta: ")
            plec = input("Wprowadź płeć pacjenta (K/M): ")
            godz_przyjecia = input("Wprowadź godzinę przyjęcia pacjenta w postaci 00:00: ")

            pacjent1 = Pacjent(imie, nazwisko, pesel, wiek, plec, godz_przyjecia)
            lista.append(pacjent1) 
            print("Pacjent", pacjent1.imie, pacjent1.nazwisko, "został dodany do listy o godzinie", pacjent1.godz_przyjecia)
            break
        except ValueError as e:
            print(e)
            print("Powtórz wprowadzenie danych.")

def wstaw_priorytet():
    while True:
        try:
            index = input("Podaj index listy, na który chcesz dodać pacjenta: ")
            if not re.match("^[0-9]$", index):
                print("Błędna wartość, wprowadź cyfrę.")
                wstaw_priorytet()
            index = int(index)
            if lista.dlugosc() == index:
                wprowadzanie_danych()
                break
            if lista.dlugosc() < index or index < 0:
                print("Kolejka jest mniejsza niż podany index.")
                return
               
            imie = input("Wprowadź imię pacjenta: ")
            nazwisko = input("Wprowadź nazwisko pacjenta: ")
            pesel = input("Wprowadź pesel pacjenta: ")
            wiek = input("Wprowadź wiek pacjenta: ")
            plec = input("Wprowadź płeć pacjenta (K/M): ")
            godz_przyjecia = input("Wprowadź godzinę przyjęcia pacjenta w postaci 00:00: ")

            pacjent1 = Pacjent(imie, nazwisko, pesel, wiek, plec, godz_przyjecia)
            lista.wstaw(pacjent1, index) 
            print("Pacjent", pacjent1.imie, pacjent1.nazwisko, "został dodany do listy o godzinie", pacjent1.godz_przyjecia)
            break
        except ValueError as e:
            print(e)
            print("Powtórz wprowadzenie danych.")

def usun_pacjenta():
    index = input("Podaj index pacjenta którego chcesz usunąć: ")
    if not re.match("^[0-9]$", index):
        print("Błędna wartość, wprowadź cyfrę.")
        usun_pacjenta()
    index = int(index)
    lista.usun(index)

def wybor_z_menu():
    menu()
    user_choice = input("Wybierz liczbę: ")

    if not re.match("^[0-9]$", user_choice):
        print("Błędna wartość, wprowadź cyfrę z zakresu 1-5.")
        wybor_z_menu()

    user_choice = int(user_choice)

    while user_choice != 5:
        if user_choice == 1:
            wprowadzanie_danych()
        
        if user_choice == 2:
            wstaw_priorytet()

        if user_choice == 3:
            usun_pacjenta()

        if user_choice == 4:
            lista.wyswietl()

        if user_choice > 5 or user_choice == 0:
            print("Błędna wartość, wprowadź cyfrę z zakresu 1-5.")
        
        wybor_z_menu()
        break

def menu():
    print()
    print("1. Dodaj pacjenta.")
    print("2. Dodaj pacjenta priorytetowego.")
    print("3. Usuń pacjenta z listy.")
    print("4. Wyświetl listę pacjentow.")
    print("5. Wyjdź.")

lista = Lista()
wybor_z_menu()

