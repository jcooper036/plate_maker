#! /usr/bin/env python3

class Ctl(object):
    """
    """
    
    def __init__(self, file):
        self.file = file
        self.replicate_plates = 1
        self.plate_barcodes = []
        self.layers = {}
        self.source_plates = []
        self.randomization_scheme = None
        self.parse_file()

    def parse_file(self):
        
        with open(self.file, 'r') as f:
            for line in f:
                line = line.rstrip()
                
                if 'replicate_plates' in line:
                    self.replicate_plates = int(line.split(':')[1])
                
                if 'plate_barcodes' in line:
                    self.plate_barcodes = line.split(':')[1].split(',')
                
                if 'layer_names' in line:
                    self.layer_keys = line.split(':')[1].split(',')
                    for key in self.layer_keys:
                        self.layers[key] = {
                            'source' : 'default',
                            'id' : 'all',
                            'vol' : 'default',
                            }
                if 'source_plates' in line:
                    self.source_plates = line.split(':')[1].split(',')
                
                if 'layer_reagent_mix' in line:
                    layers = line.split(':')[1].split(',')
                    layer_keys = [x.split('(')[0] for x in layers]
                    for idx, key in enumerate(layer_keys):
                        if key in self.layers:
                            ent = layers[idx].split('(')[1].split(')')[0].split(';')
                            for e in ent:
                                self.layers[key][e.split('=')[0]] = e.split('=')[1]

                if 'randomization_scheme' in line:
                    self.randomization_scheme = line.split(':')[1]
                            

