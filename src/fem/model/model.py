#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2023 sakakibara <sakakibara@dyana>
#
# Distributed under terms of the MIT license.
import gmsh
import math


class Model:
    def __init__(self):
        self.radius = 1.0
        self.height = 2.0
        self.lc1 = 0.1
        self.lc2 = 0.3

    def create_cylinder(self):
        radius = self.radius
        height = self.height

        gmsh.model.occ.addCylinder(0, 0, 0, 0, 0, self.height, self.radius)

        # Set mesh size on the cylinder
        gmsh.model.mesh.setSize(gmsh.model.getEntities(3), self.lc1)

        gmsh.model.occ.synchronize()

    def create_air_box(self):
        radius = self.radius
        height = self.height
        lc2 = self.lc2

        x = radius + lc2

        # Create the outer air box
        p1 = gmsh.model.occ.addPoint(-x, -x, -lc2)
        p2 = gmsh.model.occ.addPoint( x, -x, -lc2)
        p3 = gmsh.model.occ.addPoint( x,  x, -lc2)
        p4 = gmsh.model.occ.addPoint(-x,  x, -lc2)
        l1 = gmsh.model.occ.addLine(p1, p2)
        l2 = gmsh.model.occ.addLine(p2, p3)
        l3 = gmsh.model.occ.addLine(p3, p4)
        l4 = gmsh.model.occ.addLine(p4, p1)
        cl1 = gmsh.model.occ.addCurveLoop([l1, l2, l3, l4])
        s1 = gmsh.model.occ.addPlaneSurface([cl1])

        p5 = gmsh.model.occ.addPoint(-x, -x, height + lc2)
        p6 = gmsh.model.occ.addPoint( x, -x, height + lc2)
        p7 = gmsh.model.occ.addPoint( x,  x, height + lc2)
        p8 = gmsh.model.occ.addPoint(-x,  x, height + lc2)
        l5 = gmsh.model.occ.addLine(p5, p6)
        l6 = gmsh.model.occ.addLine(p6, p7)
        l7 = gmsh.model.occ.addLine(p7, p8)
        l8 = gmsh.model.occ.addLine(p8, p5)
        cl2 = gmsh.model.occ.addCurveLoop([l5, l6, l7, l8])
        s2 = gmsh.model.occ.addPlaneSurface([cl2])

        l9 = gmsh.model.occ.addLine(p1, p5)
        l10 = gmsh.model.occ.addLine(p2, p6)
        l11 = gmsh.model.occ.addLine(p3, p7)
        l12 = gmsh.model.occ.addLine(p4, p8)

        cl3 = gmsh.model.occ.addCurveLoop([l1, l10, -l5, -l9])
        cl4 = gmsh.model.occ.addCurveLoop([l2, l11, -l6, -l10])
        cl5 = gmsh.model.occ.addCurveLoop([l3, l12, -l7, -l11])
        cl6 = gmsh.model.occ.addCurveLoop([l4, l9, -l8, -l12])
        s3 = gmsh.model.occ.addPlaneSurface([cl3])
        s4 = gmsh.model.occ.addPlaneSurface([cl4])
        s5 = gmsh.model.occ.addPlaneSurface([cl5])
        s6 = gmsh.model.occ.addPlaneSurface([cl6])

        sl = gmsh.model.occ.addSurfaceLoop([s1, s2, s3, s4, s5, s6])
        v = gmsh.model.occ.addVolume([sl])

        # # Set mesh size on the air box
        # gmsh.model.mesh.setSize(gmsh.model.getEntities(3), lc2)

        gmsh.model.occ.synchronize()
