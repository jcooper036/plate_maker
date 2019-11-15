# Plate Maker
v0.1
by Jacob Cooper
jcooper036@gmail.com
  
Plate maker is a tool for making Echo pick lists for plates. It holds data in projects such that a project can produce a pick list or a feature list in long-skinny format. It is meant to suppliment some of Recursion's tools like Experiment Delight, and is meant for doing more complicated tasks. For example:
  
Experiment: Testing the different methods of building CRISPR reagents using a combination of the Echo and EL406.
- In this experiment, I want to create a type of CRISPR / Cas9 reagent that is gene specific, and randomize it's distribution with the Echo over some number of wells in a plate.
- But, I also want to use the EL406 to dispense the second part of the reagent to all the wells in some columns. 
- So on each plate we need to pick random columns for the EL406 to dispense to.
- Then the Echo has to dispense specific types of reagents to each of those columns, but randomly scatter them on each plate.
- In short, Experimental Delight is not good at this.
## Inputs
### Source plate files
    - Source (source plate name)
    - Source Plate Barcode
    - Source Well
    - Concentration
    - Reagent ID
    - REC ID
### Experiment setup file
    - replicate plates
    - if have it, a list of plate barcodes
    - Layer names
    - source plates to look in
    - For each layer
        - list of reagent names : replicates
    - layer randomization scheme (rows, columns, wells)
## Outputs
- picklist (.csv) + a schema for how to randomize the layers with the EL406
- list of all the features for each well in long-skinny format.
### Output features
Features (based on a standard Echo picklist):
    - Source (source plate name)
    - Source Plate Barcode
    - Source Well
    - Destination (dest plate name)
    - Destination Plate Barcode
    - Destination Well
    - Transfer Volume (in nL)
    - Concentration
    - Reagent ID (for CRISPR, this is like "C107")
    - Printing ID (not sure how to generate this)
    - Layer ("disease", "treatment")
    - Updated At
    - Printed At (can be blank before printing)
    - REC ID (of the thing to be printed)


