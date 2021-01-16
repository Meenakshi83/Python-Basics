#dictionary 
print("hello")


map={}

#key:value


map["a"]=24
#in 

print(map)

print("a" in map)
print("b" in map)

print("a" not in map)

#del
map[12]="abc"
map[13]=[1,2,"abcc"]
map["b"]=36
map["c"]=78
print(map)
del map["a"]
print(map)

for i in map:
    print(i,end=" ")
    print(map[i])
print(map.keys())
print(map.values())





