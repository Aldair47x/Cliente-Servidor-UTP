import Chord
import Node
import random


def initValues(idnumber_):
    keyValue = {}
    for i in range(Node.totalNodes-1):
        if(i==idnumber_):
            pass
        else:
            auxHashKey = Chord.converterSha1(i)
            keyValue[i] = auxHashKey
            #auxKeyValue = {i:auxHashKey}
            #keyValue.append(auxKeyValue)
    return keyValue   


if __name__ == "__main__":
    
    hash_ = Chord.converterSha1(1)
    hashT = {hash_:[43423,343]}
    hashT2 = {'dfdsss':[4342,3433]}
    fingerTable = [{'343443':'2343243'},{'32432':'23432423'}]
    predecessor = "asddfds"
    successor = "dfdsss"
    keyValue = initValues(10)

    

    x = Node.myNode(323,hashT,keyValue,successor,predecessor,fingerTable)
    #print(x.keyvalue_)

    nodesKeysList = list(x.keyvalue_.keys())
    m = [2,3]
    print(random.choice(m))


