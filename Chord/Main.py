import Chord

if __name__ == "__main__":
    
    hash_ = converterSha1(1)
    hashT = {hash_:[43423,343]}
    hashT2 = {'dfdsss':[4342,3433]}
    fingerTable = [{'343443':'2343243'},{'32432':'23432423'}]
    predecessor = "asddfds"
    successor = "dfdsss"
    keyValue = [2,14,67,90]
    

    x = myNode(hashT,keyValue,successor,predecessor,fingerTable)
    print(x.hash_.keys())