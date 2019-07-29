#A set is an unordered collection of items. Every element in the set is unique (no duplicates).
#Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
#Accessing Set : You cannot access items in a set by referring to an index, since sets are unordered and the items have NO INDEX.

dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}

print("------------")
print(dataScientist)
print(dataEngineer)

print("------------")
#union of sets dataScientist and dataScientist
print(dataScientist.union(dataEngineer))
print(dataScientist|dataEngineer)

print("------------")
#intersection of sets dataScientist and dataEngineer
print(dataScientist.intersection(dataEngineer))
print(dataScientist&dataEngineer)
print("------------")

#difference of sets dataScientist and dataEngineer
print(dataScientist-dataEngineer)
print(dataScientist.difference(dataEngineer))
print("------------")

#difference of sets dataEngineer and dataScientist
print(dataEngineer-dataScientist)
print(dataEngineer.difference(dataScientist))
print("------------")

#symmetric difference of dataScientist and dataEngineer
print(dataScientist.symmetric_difference(dataEngineer))
print(dataScientist^dataEngineer)
print("------------")

#set is mutable. does it allow adding elements to the set ?
my_set = {1,2.5,3,"hello world"}
my_set.add(12)
print(my_set)

#set are unordered collection, indexing has no meaning
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
dataScientist[1]