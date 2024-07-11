from crear_array import Array

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range (rows):
            self.data[row]= Array(columns, fill_value)
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])