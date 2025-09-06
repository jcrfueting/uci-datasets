#!/usr/bin/env python

import numpy as np
import datasets


for cls in [
    datasets.POWER,
    datasets.GAS,
    datasets.HEPMASS,
    datasets.MINIBOONE,
    datasets.BSDS300,
]:
    name = cls.__name__
    dataset = cls()
    for subset in ["trn","val","tst"]:
        np.save(f"{name}_{subset}.npy", getattr(dataset, subset).x)


