d = {'class' : 1, 'number' : 5, 'class' : 2}

print(d)
print(d['class'])
print(d['number'])

d['name'] = 'minho'
print(d)

del d['class']
print(d)

d['number'] = 10
print(d)