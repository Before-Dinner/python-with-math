d = {"class" : 1, "number" : "28", "class" : 2}

print(d)
print(d['class'])
print(d["number"])

d["name"] = "Han"
print(d)

del d["class"]
print(d)

print(type(d["number"]))
d["number"] = 28.5
print(d)
print(type(d["number"]))
