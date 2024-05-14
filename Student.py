import Przedmiot


class Student:
	def __init__(self, imie, nazwisko, indeks, rok):
		self.__imie = imie
		self.__nazwisko = nazwisko
		self.__indeks = indeks
		self.__rok = rok
		self.__przedmioty = []

	def get_imie(self):
		return self.__imie

	def get_nazwisko(self):
		return self.__nazwisko

	def get_indeks(self):
		return self.__indeks

	def get_rok(self):
		return self.__rok

	def get_przedmioty(self):
		return self.__przedmioty

	def __str__(self):
		return f'{self.__imie}, {self.__nazwisko}, {self.__indeks}, {self.__rok}'


	def dodaj_przedmiot(self, przedmiot: Przedmiot):
		self.__przedmioty.append(przedmiot)


