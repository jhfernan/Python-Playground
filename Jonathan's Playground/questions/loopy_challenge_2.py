# So here is what you wrote:
def mikes_loopy(items): # I renamed the function for document integrity
	# Code goes here
	loopy = []
	for item in items:
		if item in items.str.index('a') == 0:
			continue
	print(items)


# The only thing I can think that happened here is you may have overthought it a
# bit.

# For starters, the task was to create a function named loopy, not a variable
# creating a loopy variable within the loopy function serves no function to
# actually solving the problem

# So once you move past that, we want to go through each item in the list that
# the loopy function gets and do one of two things:
# if it starts with the letter 'a', we do nothing
# if it does not start with an a, print out that item

# See the following and tell me if that works:
def loopy(items):
	for item in items:
		if item[0] == 'a':
			continue
		print(item)


my_list = ['abc', 'def', 'ghi', 'abc', 'jkl']
loopy(my_list)
