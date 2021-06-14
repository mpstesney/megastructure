"""
Coursework for Generative Systems for Design, Fall 2019,
Carnegie Mellon University

Author: Michael Stesney mstesney@andrew.cmu.edu

L-system with node rewriting

This code rewrites the l-system string. The axiom, productions (rules),
number of iterations and random seed are defined by user input. Length and
angle parameters can be included in the rules if scalar modification
of the modular dimensions is desired. Branch length can be limited
by specifying the maximum quantity of a given node in the branch.

"""

__author__ = "mpste"
__version__ = "2019.10.02"

import random

random.seed(seed)

def rollDie():
    return random.randint(0,9)

def getBranch(s, i):
    lefts = 0
    rights = 0
    j = i
    #find open right bracket
    while rights <= lefts:
        j += 1
        if s[j] == "[":
            lefts += 1
        if s[j] == "]":
            rights += 1
    end = j+1
    lefts = 0
    rights = 1
    k = j
    #find matching left bracket
    while lefts < rights:
        k -= 1
        if s[k] == "[":
            lefts += 1
        if s[k] == "]":
            rights += 1
    start = k
    branch = s[start:end]
    return branch

def numNodes(s, node):
    count = 0
    for c in s:
        if c == node:
            count +=1
    return count

def replaceString(s,n):
    for i in range(n):
        subS = ""
        for j in range(len(s)):
            if s[j] == "A":
                branch = getBranch(s,j)
                nodes = numNodes(branch, "A") + numNodes(branch, "Z")
                if nodes <= wing_length:
                    subS += rule_2[rollDie()]
                else:
                    subS += rule_2[0]
            elif s[j] == "B":
                branch = getBranch(s,j)
                nodes = numNodes(branch, "B") + numNodes(branch, "D")
                if nodes <= trunk_length:
                    subS += rule_1[rollDie()]
                else:
                    subS += rule_4[0]
            elif s[j] == "D":
                subS += rule_3[rollDie()]
            else:
                subS += s[j]
        s = subS        
    return s

outString = replaceString(axiom, iterations)
