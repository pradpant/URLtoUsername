#Insert your URL in below list seprated by , you can extract upto 100Million account in one go.abs
a=['URL1','URL']
l=[]
for i in a:
  x=i.split('/')
  l.append(x[3])
print(l)
  
