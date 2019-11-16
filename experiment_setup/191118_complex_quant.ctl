# setup for the 191118 reagent tritration experiment

## how many replicates are in this experiment?
plates_per_replicate:1

## how many replicates are in this experiment?
replicates:6

## list the plate barcodes, comma seperated
# catalyst link : 
plate_barcodes:plate1,plate2,plate3,plate4,plate5,plate6

## provide a source plate file
source_plates:IB-genoCRISPR-stdv1.csv

## list the layer names, comma seperated
layer_names:1x,2x,4x,6x,8x,10x

## give the conditions for each layer : layer_name(tags)  See README for details
layer_reagent_mix:1x(id=all;vol=40),2x(id=all;vol=80),4x(id=all;vol=160),6x(id=all;vol=240),8x(id=all;vol=320),10x(id=all;vol=400)

## how should the layers get randomized?
randomization_scheme:columns