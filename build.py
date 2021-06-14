"""
Coursework for Generative Systems for Design, Fall 2019,
Carnegie Mellon University

Author: Michael Stesney mstesney@andrew.cmu.edu

L-system with node rewriting

This GhPython component translates the node types into parameters necessary
to create Grasshopper primitives.

"""

__author__ = "mpste"
__version__ = "2019.10.02"

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

# structure types

def createSmallBox(structure):
    plane = rg.Plane.Clone(structure[1])
    rg.Plane.Rotate(plane, -math.pi/2, plane.XAxis)
    vec = (plane.XAxis * module/2) + (plane.YAxis * module/2)
    corner1 = plane.Origin + vec
    corner2 = plane.Origin - vec
    rec = rg.Rectangle3d(plane, corner1, corner2)
    return rec, module

def createWideBox(structure):
    plane = rg.Plane.Clone(structure[1])
    rg.Plane.Rotate(plane, -math.pi/2, plane.XAxis)
    vec = (plane.XAxis * module) + (plane.YAxis * module/2)
    corner1 = plane.Origin + vec
    corner2 = plane.Origin - vec
    rec = rg.Rectangle3d(plane, corner1, corner2)
    return rec, module

def createCylinder(structure):
    radius = module*11.5
    height = module*2    
    return structure[1], radius, height
    
def createBridge(structure):
    plane = rg.Plane.Clone(structure[1])
    rg.Plane.Rotate(plane, -math.pi/2, plane.XAxis)
    vec1 = plane.YAxis * (module*1.5)
    rg.Plane.Translate(plane, vec1)
    vec2 = (plane.XAxis * (module/4)) + (plane.YAxis * (module))
    corner1 = plane.Origin + vec2
    corner2 = plane.Origin - vec2
    rec = rg.Rectangle3d(plane, corner1, corner2)
    return rec, module/10
    
for structure in structures:
    if structure[0] == "A":
        A = createSmallBox(structure)
    elif structure[0] == "B":
        B = createWideBox(structure)
        M = createBridge(structure)
    elif structure[0] == "C":
        C = createCylinder(structure)
    elif structure[0] == "D":
        D = createWideBox(structure)
        M = createBridge(structure)
    elif structure[0] == "E":
        E = createWideBox(structure)
        N = createBridge(structure)
    elif structure[0] == "Z":
        Z = createSmallBox(structure)


