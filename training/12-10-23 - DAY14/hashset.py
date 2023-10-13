class hashset:
    def __init__(self):
        self.s=set()

    def add(self,key):
        self.s.add(key)

    def remove(self,key):
        self.s.remove(key)
    def contains(self,key):
        if key in self.s:
            return True
        else:
            return False
obj=hashset()
obj.add(20)
obj.add(80)
obj.remove(80)
print(obj.contains(20))
