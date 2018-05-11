#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import sys

totalNodes = 64


class myNode:
    def __init__(self, IdHash, hashT, keyValue, successor, predecessor,fingerTable):
        self.idhash_ = IdHash
        self.hash_ = hashT
        self.keyvalue_ = keyValue
        self.successor_ = successor
        self.predecessor_ = predecessor
        self.fingertable_ = fingerTable

    def setHashT(hashT):
        self.hash_ = hashT

    def getHashT():
        return self.hash_

    def setKeyValue(keyValue):
        self.keyvalue_ = keyValue

    def getKeyValue():
        return self.keyvalue_

    def setSuccessor(successor):
        self.successor_ = successor

    def getSuccessor():
        return self.successor_

    def setPredecessor(predecessor):
        self.predecessor_ = predecessor

    def getPredecessor():
        return self.predecessor_

    def setFingerTable(fingerTable):
        self.fingertable_ = fingerTable

    def getFingerTable():
        return self.fingertable_

    def setIdHash(IdHash):
        self.idhash_ = IdHash

    def getIdHash():
        return self.idhash_