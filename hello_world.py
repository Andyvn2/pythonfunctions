words = "It's thanksgiving day. It's my birthday too!"
print words.find("day")
words.replace ("birthday", "day")
print words.replace ("day", "month")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print "min list : ", x.pop()
print "max list :", x.pop(0)

y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
print y
z = y[0:5]
print z
y.remove(-3)
y.insert(5,z)
print y[5:10]