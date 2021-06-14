"""
Coursework for Generative Systems for Design, Fall 2019,
Carnegie Mellon University

Author: Michael Stesney mstesney@andrew.cmu.edu

L-system with node rewriting

The string output from the writing process and translates that relational
information into absolute locations within a three-dimensional space.
User defined length and angle modular dimensions, scaled as necessary,
are incorporated at this stage in the process. A list of nodes, along with
the positional state at that node, are output as a list. In addition to the
X, Y and Z coordinates, the positional state includes the X, Y and Z axis
vectors. All state information is included in a single Grasshopper Plane object.

"""

__author__ = "Michael"
__version__ = "2019.10.01"

import Rhino.Geometry as rg
import math
import copy

def getParameter(s):
    if (len(s) > 1) and (s[1] == "("):
        end = s.find(")")
        return float(s[2:end])
    else: return 1

def mechanism3D(s, length, angle):
    cur_plane = rg.Plane.WorldXY
    planes_ = [cur_plane]
    temp_planes = []
    
    lines_ = [] # for display
    structures_ = [] # types, points and planes
    
    for i in range(len(s)):
        
        parameter = getParameter(s[i:])
        
        # execute string commands
        if s[i] == "F": #move forward along z axis, draw line, set state
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Translate(new_plane, cur_plane.ZAxis * length * parameter)
            planes_.append(new_plane)
            lines_.append(rg.Line(cur_plane.Origin, new_plane.Origin))
            cur_plane = new_plane
        elif s[i] == "f": #move forward along z axis, set state
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Translate(new_plane, new_plane.ZAxis * length * parameter)
            planes_.append(new_plane)
            cur_plane = new_plane      
        elif s[i] == "+": #pitch up
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(-angle * parameter), new_plane.XAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "-": #pitch down
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(angle * parameter), cur_plane.XAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "&": #yaw left
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(angle * parameter), new_plane.YAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "^": #yaw right
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(-angle * parameter), new_plane.YAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "\\": #roll clockwise
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(angle * parameter), new_plane.ZAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "/": #roll counterclockwise
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(-angle * parameter), new_plane.ZAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "|": #turn around, reverse direction on z axis
            new_plane = rg.Plane.Clone(cur_plane)
            rg.Plane.Rotate(new_plane, math.radians(180), new_plane.XAxis)
            planes_.append(new_plane)
            cur_plane = new_plane
        elif s[i] == "[": #push
#            temp_pts.append(cur_pt)
            temp_planes.append(cur_plane)
        elif s[i]== "]": #pop
#            cur_pt = temp_pts.pop()
            cur_plane = temp_planes.pop()
        
        # structure building modules
        elif s[i] == "A":
            structures_.append(["A", cur_plane])
        elif s[i] == "B":
            structures_.append(["B", cur_plane])
        elif s[i] == "C":
            structures_.append(["C", cur_plane])
        elif s[i] == "D":
            structures_.append(["D", cur_plane])
        elif s[i] == "E":
            structures_.append(["E", cur_plane])
        elif s[i] == "M":
            structures_.append(["M", cur_plane])
        elif s[i] == "N":
            structures_.append(["N", cur_plane])
        elif s[i] == "Z":
            structures_.append(["Z", cur_plane])
            
        # other commands from ABOP that may be useful
        #             
        # $ rotate turtle to vertical
        # {  Start a polygon
        # G Move forward and draw a line. Do not record a vertex
        # . Record a vertex in the current polygon
        # } Complete a polygon
        # ~ Incorporate a predeﬁned surface
        # ! Decrement the diameter of segments
        # ' Increment the current color index
        # % Cut oﬀ the remainder of the branch
            
    return lines_, planes_, structures_

print(s)
lines, planes, structures = mechanism3D(s, length, angle)

