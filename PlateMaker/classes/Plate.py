#! /usr/bin/env python3

class Plate(object):
    """
    Represents a 1536 well plate

    """

    def __init__(self):

        self.rows = {}
        self.cols = {}
        self.wells = {}

        for r in base_rows:
            self.rows[r] = {
                    'layer' : None,
                    'wells' : []
                    }
        for c in base_cols:
            self.cols[c] = {
                    'layer' : None,
                    'wells' : []
                    }
        
        for r in self.rows:
            for c in self.cols:
                # this should contain null for every possible output
                self.rows[r]['wells'].append(r+c)
                self.cols[c]['wells'].append(r+c)

                self.wells[r+c] = {
                    'Source' : None,
                    'Source Plate Barcode' : None,
                    'Source Well' : None,
                    'Destination' : None,
                    'Destination Plate Barcode' : None,
                    'Destination Well' : None,
                    'Transfer Volume' : None,
                    'Concentration' : None,
                    'Reagent ID' : None,
                    'Printing ID' : None,
                    'Layer' : None,
                    'Updated At' : None,
                    'Printed At' : None,
                    'REC ID' : None,
                }
    
    def apply_layers(self, layers, by):
        """
        layers
            dict - {layer:[segment to add to]}
        by: 
            str - rows | columns
        """


        if by == 'columns':
            for layer in layers:
                for x in layers[layer]:
                    self.cols[x]['layer'] = layer

        if by == 'rows':
            for layer in layers:
                for x in layers[layer]:
                    self.rows[x]['layer'] == layer


base_rows = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE']

base_cols = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']


### full, without the edges removed
# base_rows = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF']

# base_cols = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48']