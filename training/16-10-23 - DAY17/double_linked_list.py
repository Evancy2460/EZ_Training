class node:
    def __init__(self,val=0):
        self.val=val
        self.prev=None
        self.next=None
class sas:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
            new.prev=curr
    def deleteatbegin(self):
        if self.head==None:
            return 
        temp=self.head
        self.head.prev=None
        self.head=temp.next
        temp.next=None
        return temp.val
    def deleteatend(self):
        if self.head==None:
            return
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.prev=None
            temp.next=None
            return temp.val
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next
        '''#reverse
        temp=self.head
        while(temp.next):
            temp=temp.next 
        while(temp):
            print(temp.val,end=" ")
            temp=temp.prev'''
obj=sas()
l=list(map(int,input().split()))
for i in l:
    obj.insertatbegin(i)
obj.printing()
print()
print(obj.deleteatbegin())
print(obj.deleteatend())