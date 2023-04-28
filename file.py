import os 
c = 'Assigment_'
fi = []
for i in range(11,26):
    fi.append(c+str(i)+'.txt')

for j in fi:
    with open(os.path.join('Python Basic',j),'w') as f:
        pass 