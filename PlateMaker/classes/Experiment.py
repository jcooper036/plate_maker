#! /usr/bin/env python3

from datetime import datetime
import PlateMaker as plm

class Experiment(object):

    def __init__(self, name):
        
        self.name = name
        self.time = {
            'created' : datetime.now(),
            'last_save' : None
        }
        self.source_plates = []
        self.destination_plates = []
        self.replicate_plates = None
        self.design_stage = {
            'specifications' : 'INCOMPLETE',
            'design' : 'INCOMPLETE',
            'instructions' : 'INCOMPLETE' 
        }

    def __repr__(self):
        return self.name

    #################### loading information
    def load_data(self, file):
        self.ctl = plm.load_ctl_file(file)
        self.source_plates = plm.load_source_plates(self.ctl.source_plates)

    #################### processing


    ##################### outputs
    def write_outputs(self):
        self.save()
        self.make_picklist()
        self.make_protocol()
    
    def save(self):
        self.time['last_save'] = datetime.now()

    def make_picklist(self):
        pass

    def make_protocol(self):
        pass