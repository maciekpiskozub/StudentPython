from Przedmiot import Przedmiot
from Student import Student

if __name__ == '__main__':
    przedmiot = Przedmiot('bazy danych')
    uczen = Student('Henryk',' Heroiczny', '007', 2022)
    przedmiot.set_ects(10)
    uczen.dodaj_przedmiot(przedmiot)
