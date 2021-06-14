"""
Coursework for Generative Systems for Design, Fall 2019,
Carnegie Mellon University

Author: Michael Stesney mstesney@andrew.cmu.edu

L-system with node rewriting

"""

__author__ = "Michael"
__version__ = "2019.10.02" 

import rhinoscriptsyntax as rs

bucket = []
rule = rules.split(",")
bucket.extend([str(rule[1])] * int(rule[0]))

