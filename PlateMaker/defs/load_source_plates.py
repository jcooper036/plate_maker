#! /usr/bin/env python3

import pandas as pd
import os


def load_source_plates(source_plates):
    """
    Inputs:
        source_plates (list) : the source plates in this experiment
    Returns
        dict : {source_plate_name : pandas data frame of source plate}
    """
    s_plates = {}
    for splate in source_plates:
        p = 'source_plates/' + splate
        if os.path.isfile(p):
            s_plates[splate] = pd.read_csv(p)
    return s_plates