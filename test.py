# from singleton import EarlySingleton
from singleton import Singleton


def increment_1():
    obj1=Singleton.getinstance()
    obj1.incrment_cnt()
    print(obj1)