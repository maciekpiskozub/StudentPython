class Przedmiot:
	def __init__(self, nazwa = ''):
		self.__nazwa = nazwa
		self.__ects = 0

	def get_nazwa(self):
		return self.__nazwa

	def set_nazwa(self, nazwa):
		self.__nazwa = nazwa

	def get_ects(self):
		return self.__ects

	def set_ects(self, ects):
		self.__ects = ects

	def __str__(self):
		return f'{self.__nazwa}: {self.__ects}'






