#! /usr/bin/env python3

import PlateMaker as plm

# name the experiment - should have a folder in 'experiments' and a .ctl file before starting
exper_name = '191118_complex_quant'

ex = plm.Experiment(exper_name)
ex.load_data(f'experiments/{exper_name}/{exper_name}.ctl')
ex.init_plates()
ex.assign_layers()
ex.randomize_samples()

# ex.write_outputs()
ex.save()
ex.make_picklist()
ex.make_protocol()
