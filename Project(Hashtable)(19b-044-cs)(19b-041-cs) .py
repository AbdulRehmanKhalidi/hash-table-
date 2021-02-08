class Direct_HashTable:
    def __init__(self, size):
        self.size= size
        self.Direct_Address_table = []
        for i in range(self.size):
            self.Direct_Address_table.append(None)

    def Direct_Address_Insert(self,k,v):
        self.Direct_Address_table[k]= v # Directly Inserting key in Direct_Address_table

    def Direct_Address_Search(self,k):
        k1= self.Direct_Address_table[k] #Searching for a key
        return k1

    def Direct_Address_Remove(self,k):
        self.Direct_Address_table[k]= None #The index will be marked as none


obj= Direct_HashTable(10)
print("DIRECT ADDRESS TABLE")
print("-"*170)
obj.Direct_Address_Insert(4,"Tommy Vercetti")
obj.Direct_Address_Insert(3,"Carl Johnson (CJ)")
obj.Direct_Address_Insert(1,"Big Smoke")
obj.Direct_Address_Insert(2,"Claude")
obj.Direct_Address_Insert(5,"Michael")
obj.Direct_Address_Insert(6,"Toni")
obj.Direct_Address_Insert(7,"Maria")
obj.Direct_Address_Insert(8,"Ryder")
obj.Direct_Address_Insert(9,"Lance")
obj.Direct_Address_Insert(0,"Trevor")
print("Inserting Elements in the Table:", obj.Direct_Address_table)
print("-"*170)
print("Searching for a Value at the following key: ",obj.Direct_Address_Search(4))
print("-"*170)
obj.Direct_Address_Remove(2)
print("Removing a value from the Direct_Address_Insert: ",obj.Direct_Address_table)
print("-"*170)

#Linear Probing
class LinearProbing:
    def __init__(self, size):
        self.size= size
        self.table = []
        for i in range(self.size):
            self.table.append(None)

    def __hashed(self,k): #For "Manahil"

        h=0 #ASCII value will be 698 for "Manahil"
        for i in k:
            h += ord(i)
        return h%self.size


    def hash(self,k):                       #Just to see where it is hashing
        return (self.__hashed(k))

    def Insert(self,k,v):
        #i= self.__hashed(k)           # calling hash function
        i = self.__hashed(k)
        while self.table[i] != None:            #while the given index is not equal to None
            if self.table[i]==k:            # if the element is equal to the given key then it will break
                break
            i=(i+1)%self.size               # It will look for the next index
        if self.table[i]==None:         # finding a none in self.table and if we find none then place the value.
            self.table[i]= (k,v)          # insert in hashtable in form of key valuepair


    def Search(self,k):
        i= self.__hashed(k)     #calling hash function
        while self.table[i] != None and self.table[i][0] != k:  #Searching for the key in the Table, if the table is NOne
            i = (i + 1) % self.size         # Then look for the key at the next index
        if self.table[i][0] == k:   #If the key is found at that index
            return self.table[i]    #Return that key.


    def Remove(self,k):
        i= self.__hashed(k)
        while self.table[i][0]!=k:  #If the given key is not found at that index in table
            i = (i + 1) % self.size    # Then look for the next index
        if self.table[i][0] == k:       #If the key is found
            self.table[i]=None          #Then mark the Index as None

obj= LinearProbing(8)
print("-"*170)
print("LINEAR PROBING")
print("-"*170)


keys = ["Carl Johnson","Big Smoke","Claude","Michael","Maria","Ryder","Tommy Vercetti","256"]
for i in keys:          #Just to see on which index our keys are stored.
    print(i,":",obj.hash(i),"Idx")

obj.Insert("Carl Johnson",19)
obj.Insert("Big Smoke",18)
obj.Insert("Claude",18)
obj.Insert("Michael",20)
obj.Insert("Maria",20)
obj.Insert("Ryder",30)
obj.Insert("Tommy Vercetti",36)
obj.Insert("256",36)
print("-"*170)
print("AFTER INSERTING USING LINEAR PROBING: ",obj.table)
print("-"*170)
print("SEARCHING FOR THE KEY: ", obj.Search("Carl Johnson"))
print("-"*170)
# obj.Remove(2)
obj.Remove("Maria")
print("AFTER REMOVING: ", obj.table)
print("-"*170)

