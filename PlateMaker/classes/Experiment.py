#! /usr/bin/env python3

from datetime import datetime
import PlateMaker as plm
import random
import copy

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
        self.plates = {}

    def __repr__(self):
        return self.name

    #################### loading information
    def load_data(self, file):
        self.ctl = plm.load_ctl_file(file)
        self.source_plates = plm.load_source_plates(self.ctl.source_plates)

    #################### processing
    
    def init_plates(self):
        """
        Builds a dicitonary of {plates:Plate()}, keys are the plate barcode
        """
        assert (self.ctl.replicates * self.ctl.platesper) == len(self.ctl.plate_barcodes), "Not enough destination plate barcodes"

        for plate in self.ctl.plate_barcodes:
            self.plates[plate] = plm.Plate()

    def assign_layers(self):
        """
        How many rows/cols does each layer get per plate?
        For each plate, randomly choose the rows/cols that each layer will have
        Apply that layer to the rows/cols in the plates
        """
        assert self.ctl.layers
        assert self.ctl.replicates
        assert self.ctl.randomization_scheme
        assert self.ctl.replicates
        assert self.plates

        # how many rows/cols, assuming 1 empty around the entire plate
        totals = {
            'columns' : (46, base_cols),
            'rows' : (30, base_rows),
        }
        self.div_per_layer = int(totals[self.ctl.randomization_scheme][0] / len(self.ctl.layers.keys()))
        

        # for each plate, randomly choose
        self.div_assign = {}
        for plate in self.plates:
            self.div_assign[plate] = plm.assign_divisions(list(self.ctl.layers.keys()), self.div_per_layer, copy.deepcopy(totals[self.ctl.randomization_scheme][1]))

        # apply that layer to the rows / columns
        for plate in self.plates:
            self.plates[plate].apply_layers(self.div_assign[plate], self.ctl.randomization_scheme)
    
    def randomize_samples(self):
        """
        Divide the samples from the source plate to wells in each layer
        Assign the correct data to each well
        """

        # find the wells that are in each layer
        self.layer_wells = {}
        for plate in self.plates:
            divtype = {'columns':self.plates[plate].cols, 'rows':self.plates[plate].rows}
            self.layer_wells[plate] = {}
            for layer in self.ctl.layers.keys():
                self.layer_wells[plate][layer] = []
                for div in self.div_assign[plate][layer]:
                    self.layer_wells[plate][layer].append(divtype[self.ctl.randomization_scheme][div]['wells'])
                self.layer_wells[plate][layer] = [y for x in self.layer_wells[plate][layer] for y in x]

        # find how many of each sample is in each layer
        for plate in self.plates:
            for layer in self.layer_wells[plate]:
                # layer_source is the pandas df that has all the info for that source plate
                layer_source = self.source_plates[self.ctl.layers[layer]['source']]
                reps_for_layer = int((len(self.layer_wells[plate][layer]) / len(layer_source)))

        # assign the information to each well based on the layer it's in and source it comes from
        for plate in self.plates:
            for layer in self.layer_wells[plate]:
                temp_list = copy.deepcopy(self.layer_wells[plate][layer])
                for idx, source_well in layer_source.iterrows():
                    for _ in range(0, reps_for_layer):
                        n = random.randint(0, len(temp_list)-1)
                        well = temp_list.pop(n)

                        # give all that info to the well
                        self.plates[plate].wells[well]['Source'] = self.ctl.layers[layer]['source']
                        self.plates[plate].wells[well]['Source Plate Barcode'] = None
                        self.plates[plate].wells[well]['Source Well'] = source_well['address']
                        self.plates[plate].wells[well]['Destination'] = plate
                        self.plates[plate].wells[well]['Destination Plate Barcode'] = plate
                        self.plates[plate].wells[well]['Destination Well'] = well
                        self.plates[plate].wells[well]['Transfer Volume']= self.ctl.layers[layer]['vol']
                        self.plates[plate].wells[well]['Concentration']= source_well['concentration']
                        self.plates[plate].wells[well]['Reagent ID']= source_well['reagent_id']
                        self.plates[plate].wells[well]['Printing ID']= None
                        self.plates[plate].wells[well]['Layer']= 'disease'
                        self.plates[plate].wells[well]['Updated At']= str(datetime.now())
                        self.plates[plate].wells[well]['Printed At']= None
                        self.plates[plate].wells[well]['REC ID']= source_well['rec_id']

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


base_rows = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE']

base_cols = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']