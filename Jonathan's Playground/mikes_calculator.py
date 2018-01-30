from imports.electric import Electric
from imports.prettify import Prettify



calculator = Electric()
system = Prettify()
notifications = None
history = []

while True:
	system.clear_screen()
	if notifications:
		print(notifications)
	print('Please provide an option')
	print('a) Point Charge Calculator')
	print('Press "x" to clear the history\nPress "q" at any time to quit')
	if history:
		system.print_divider('-', 70)
	for result in history:
		print(result)
	response = input('>>> ').lower()
	if response == 'q':
		system.system_exit()
	elif response == 'a':
		system.clear_screen()
		history.append(calculator.point_charge())
	elif response == 'x':
		history = [];
	else:
		notifications = 'Please enter a valid option!!!'
