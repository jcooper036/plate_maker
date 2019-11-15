#! /usr/bin/env python3

class Csv(object):
    """
    Csv object for loading and managing csv files
    """
    def __init__(self, file, header=True):
        self.file = file
        self.header = header
        self.read_csv(self.header)
    
    def read_csv(self, header):
        """
        Input: csv file, header bool (optional)
        Gives the object the .data property
        """
        self.data = []
        with open(self.file, 'r') as f:
            for line in f:
                line = line.rstrip()
                if header:
                    self.header = line.split(',')
                if not header:
                    line = line.split(',')
                    line = [x.lower() for x in line]
                    self.data.append(line)
                header = False