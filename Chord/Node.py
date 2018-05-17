#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import sys

totalNodes = 64


class myNode:
    def __init__(self, IdHash, hashT, successor, predecessor,fingerTable):
        self.idhash_ = IdHash
        self.hash_ = hashT
        self.successor_ = successor
        self.predecessor_ = predecessor
        self.fingertable_ = fingerTable

    def setHashT(hashT):
        self.hash_ = hashT

    def getHashT(self):
        return self.hash_

    def setSuccessor(successor):
        self.successor_ = successor

    def getSuccessor(self):
        return self.successor_

    def setPredecessor(predecessor):
        self.predecessor_ = predecessor

    def getPredecessor(self):
        return self.predecessor_

    def setFingerTable(fingerTable):
        self.fingertable_ = fingerTable

    def getFingerTable(self):
        return self.fingertable_

    def setIdHash(IdHash):
        self.idhash_ = IdHash

    def getIdHash(self):
        return self.idhash_