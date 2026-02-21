
# class EarlySingleton:
#     __instance=None

#     def __init__(self):
#         if(EarlySingleton.__instance !=None):
#             raise Exception("This is a singleton")
#         self.count=0
        
#         EarlySingleton.__instance=self
    
#     def increment_cnt(self):
#         self.count+=1
#         print(self.count)

#     @staticmethod
#     def getinstance():
#         return EarlySingleton.__instance
    

# EarlySingleton._EarlySingleton__instance=EarlySingleton()

# print("Created")

import threading
class Singleton:
    __instance=None
    __lock=threading.Lock()
    def __init__(self):
        if(Singleton.__instance!=None):
            raise Exception("This is a singleton")
        self.cnt=0
        Singleton.__instance=self
    
    @staticmethod
    def getInstance():
        with Singleton.__lock:
            if(Singleton.__instance==None):
                Singleton()
        return Singleton.__instance

    def incrment_cnt(self):
        self.cnt+=1
        print(self.cnts)

    @staticmethod
    def getInstance():
        if(Singleton.__instance==None):
            with Singleton.__lock:
                if(Singleton.__instance==None):
                    Singleton()
        

        return Singleton.__instance