#lists
'''
countries= ["uk", "usa", "uk", "uae"]
print dir(countries)
print countries.count("uk")

#Tuples excercises
t=(1,)
print t[-1]
l=range(100,200)
tup=tuple(l)

print tup[0], tup[-1]

out=[]

mylist= [23,"hi",2.4e-10]
for (count, item) in enumerate(mylist):
    print count, item
	
(first, middle, last) = mylist
print first, middle, last

first, middle, last = last, middle, first
print first, middle, last



#Input-Output
rain=[]
with open("weather.csv") as reader:
    header = reader.readline()
    for line in reader.readlines(): 
	r = line.strip().split(",")[-1]
        r = float (r)
        rain.append(r)
print rain
	
with open("myrain.txt", "w") as writer:
    for r in rain:
        writer.write(str(r) + "\n")



s= "I love to write python"
for i in s:
	print i
print s[4]
print s[-1]
print s[0],s[0][0],s[0][0][0]



s = "I love to write python"
split_s=s.split()
for word in split_s:
    if word.find("z") > -1:
	print "I found 'i' in: '{0}'".format(word)
    print word.find("I")
	    


something="Completely Different"


print something.split("e")
print something.count("t")
print something.find("plete")

thing2=something.replace("Different", "Silly")
something[0]="B"

#Functions excercises

def double_it(number):
    return number * 2

double_it("hello")
'''
print type(3)
def calc_hypo(a,b):
    if type(a) is not float and type(a) is not int:
        print "Bad argument a"
        return False 
    if type(b) is not float and type(b) is not int:
        print "Bad argument b"
        return False 
    hypo = (a**2+b**2)**0.5
    return hypo
print calc_hypo(3,2)




