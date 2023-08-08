# vim:fenc=utf-8
#
# Copyright © 2023 sakakibara <sakakibara@skk.local>
#
# Distributed under terms of the MIT license.
# from collections import defaultdict
from fem.simulation import Fem
from fem.model import Model, WingModel


param_dict={
    "element_order": 1,
    "interpolate_order": 1}

fem = Fem(
    "fem_model",
    param_dict=param_dict
)

model = Model()
# wing_model = WingModel()

fem.set_model(model)
# fem.set_model(wing_model)
# fem.write_model()
# fem.view()
# fem.calc_model()
fem.run()
