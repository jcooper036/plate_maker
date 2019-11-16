#! /usr/bin/env python3

import random

def assign_divisions(layers, div_per_layer, total_options):
    plate = {}
    for layer in layers:
        plate[layer] = []
        for _ in range(div_per_layer):
            idx = random.randint(0, len(total_options)-1)
            plate[layer].append(total_options.pop(idx))
        plate[layer] = sorted(plate[layer])
    return plate