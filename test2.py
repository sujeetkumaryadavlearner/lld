from singleton import EarlySingleton

def increment_2():
    obj1=EarlySingleton.getinstance()
    obj1.incrment_cnt()
    print(obj1)

