#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 sakakibara <sakakibara@dyana>
#
# Distributed under terms of the MIT license.
import gmsh
from fem.calc import set_element
from fem.calc import get_edge_node_num


class Fem:
    def __init__(self, model_name: str, param_dict: dict):

        gmsh.initialize()
        gmsh.model.add(model_name)

        self.element_order = param_dict["element_order"]
        self.interpolate_order = param_dict["interpolate_order"]
        self.elementType = gmsh.model.mesh.getElementType(
            "tetrahedron", self.element_order
        )

    def set_model(self, model):
        # gmsh.model.mesh.setOrder(self.element_order)
        model.create_cylinder()
        model.create_air_box()

        # # まっすぐな翼だけ
        # model.create_wing()

        # # 少し回転させた翼3Dの形状
        # model.rotate_wing()

        # # メッシュが荒くなった？
        # model.set_boundary()

        # # air_boxが生成された
        # model.create_air_box()

        # gmsh.model.geo.synchronize()
        gmsh.model.mesh.generate(3)

    def calc_model(self):
        elements = set_element(
            self.elementType, self.element_order, self.interpolate_order
        )

        edge_num, node_num = get_edge_node_num(elements)
        K = calc_K(elements, edge_num, node_num, elementType)
        C = calc_C(elements, edge_num, node_num, elementType)

    def write_model(self):
        gmsh.write("mesh.msh")

    def run(self):
        gmsh.fltk.run()

    def __del__(self):
        gmsh.finalize()
