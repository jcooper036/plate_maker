#! /usr/bin/env python3

import pickle as pkl

def pickle_save(ob, file):
    with open(file, 'wb') as f:
        pickle.dump(ob, f, pickle.HIGHEST_PROTOCOL)

def pickle_load(file):
    with open(file, 'rb') as f:
        a = pickle.load(f)
    return a