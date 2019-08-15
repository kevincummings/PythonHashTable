import re

class HashTable():
	def __init__(self, size=16, resize_percent=0.75):
		self.table = [''] * size
		self.resize_percent = resize_percent
		self.numberOfItems = 0
		self.characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

	def __find_index__(self, character):
		# Iterate allowed character list until desired character's index is found
		for i in range(0, len(self.characters)):
			if self.characters[i] == character:
				return i

	def get(self, index):
		return self.table[index]

	def get_number_of_items(self):
		return self.numberOfItems

	def get_table(self):
		return self.table

	def get_size(self):
		return len(self.table)

	def get_item_index(self, item):
		# Get index of the first character of the item
		index = self.__find_index__(item[0])

		# Check if item is in the location it would be placed if the spot was empty when the item was added
		if self.table[index % len(self.table)] == item:
			return index % len(self.table)

		# If item is not in predicted location, continue searching from the most likely location to the least
		else:
			for i in range(index, len(self.table)):
				if self.table[i] == item:
					return i

			for i in range(0, index):
				if self.table[i] == item:
					return i

		return -1

	def resize(self):
		# Create a new table sized at double the size of the old table
		new_table = [''] * (len(self.table) * 2)

		# Store the data from the old table
		temp_table = self.table

		# Switch the table to the new, double sized table
		self.table = new_table

		# Reset the number of items because the items will be added and then counted again
		self.numberOfItems = 0

		# Add items from old table
		for item in temp_table:
			if item != '':
				self.add(item)

	def add(self, item):
		# Removes all non-alphanumeric characters
		item = re.sub(r'[\W_]+', '', item)

		# Check to see if table needs to be resized
		if float((self.numberOfItems + 1) / len(self.table)) >= self.resize_percent:
			self.resize()

		# Get the index of the first character of the item from a list of possible characters
		i = self.__find_index__(item[0])

		# Use linear probing to find the next open spot in the table
		while self.table[i % len(self.table)] != '':
			i += 1

		# Add item to table
		self.table[i % len(self.table)] = item

		# Add the new item to the count of items
		self.numberOfItems += 1
