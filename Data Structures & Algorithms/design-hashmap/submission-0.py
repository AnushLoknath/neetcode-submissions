class MyHashMap:

    def __init__(self):
        self.gg={}
        

    def put(self, key: int, value: int) -> None:
        self.gg[key]=value
        

    def get(self, key: int) -> int:
        if key  in self.gg:
            return self.gg[key]
        return -1    
        

    def remove(self, key: int) -> None:
        if key in self.gg:
            del self.gg[key]


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)