#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 sakakibara <sakakibara@skk.local>
#
# Distributed under terms of the MIT license.
# from collections import defaultdict
from fem.simu import Fem
from fem.model import Model


fem = Fem(
    "fem_model",
    param_dict={
        "element_order": 1,
        "interpolate_order": 1,
    },
)

model = Model()

fem.set_model(model)
# fem.write_model()
# fem.view()
# fem.calc_model()
fem.run()
