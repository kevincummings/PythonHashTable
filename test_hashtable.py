from hashtable import HashTable

def print_table(table):
    for item in table.get_table():
        print(item)

class TestHashTable():
    def __init__(self):
        self.hashtable = HashTable(size=5)

        items = ['wind', 'solar']

        for item in items:
            self.hashtable.add(item)

    def test_add(self):
        print('========== Testing HashTable.add() ==========')
        self.hashtable.add('geothermal')
        print('Get item by index ("geothermal" Expected): {}'.format(self.hashtable.get(1)))

    def test_get(self):
        print('========== Testing HashTable.get() ==========')
        print('Get item by index ("wind" Expected): {}'.format(self.hashtable.get(2)))
        print('Get item by index ("solar" Expected): {}'.format(self.hashtable.get(3)))    

    def test_get_item_index(self):
        print('========== Testing HashTable.get_item_index() ==========')
        print('Get index by item ("2" Expected): {}'.format(self.hashtable.get_item_index('wind')))
        print('Get index by item ("3" Expected): {}'.format(self.hashtable.get_item_index('solar')))
        print('Get index by item ("-1" Expected): {}'.format(self.hashtable.get_item_index('nonexistent item')))

    def test_get_number_of_items(self):
        print('========== Testing HashTable.get_number_of_items() ==========')
        print('Get number of items ("3" Expected): {}'.format(self.hashtable.get_number_of_items()))

    def test_get_size(self):
        print('========== Testing HashTable.get_size() ==========')
        print('Get size ("5" Expected): {}'.format(self.hashtable.get_size()))

    def test_get_table(self):
        print('========== Testing HashTable.get_table() ==========')
        print('Get table ("[\'\', \'geothermal\', \'wind\', \'solar\', \'\']" Expected): {}'.format(self.hashtable.get_table()))

    def test_resize(self):
        print('========== Testing HashTable.resize() ==========')
        print('Get number of items ("3" Expected): {}'.format(self.hashtable.get_number_of_items()))
        print('Get size ("5" Expected): {}'.format(self.hashtable.get_size()))
        self.hashtable.add('hydroelectric')
        print('Get number of items ("4" Expected): {}'.format(self.hashtable.get_number_of_items()))
        print('Get size ("10" Expected): {}'.format(self.hashtable.get_size()))

    def run(self):
        for method in sorted(dir(self)):
            if method[0] != '_' and callable(getattr(self, method)) and method != 'run':
                getattr(self, method)()

class __main__():
    tests = TestHashTable()
    tests.run()
