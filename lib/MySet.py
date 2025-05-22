class MySet:

    def __init__(self, list =[]):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        return self.dictionary.clear()
    
    def __str__(self):
        return f"MySet: {{{','.join(str(k) for k in self.dictionary.keys())}}}"
