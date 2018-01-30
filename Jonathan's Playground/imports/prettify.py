import os
import sys


class Prettify:
	awesome = True

	def clear_screen(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def system_exit(self):
		sys.exit()

	def print_divider(self, mystring, amount):
		print(mystring * amount)
