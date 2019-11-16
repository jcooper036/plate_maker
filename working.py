#! /usr/bin/env python3

import PlateMaker as plm

ex = plm.Experiment('name')
ex.load_data('experiment_setup/191118_complex_quant.ctl')
ex.init_plates()
ex.assign_layers()
ex.randomize_samples()
