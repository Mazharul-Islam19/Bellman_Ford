file = 'matrix_100_1_3_1.gr'
adj_list = {}
data = []
max_weight = 0
with open(file, 'r') as f:
    for line in f:
        line = line.strip('\n')
        if line[0] != 'c' and line[0] != 'p':
            data.append(line.split())
            adj_list[int(line.split()[1])] = []
            if int(line.split()[3]) > max_weight:
                max_weight = int(line.split()[3])
        elif line[0] == 'p':
            n = int(line.split()[2])
            m = int(line.split()[3])
for i in data:
    adj_list[int(i[1])].append((int(i[2]),int(i[3])))

dist = {}
pred = {}    
for i in range(1,n+1):
    dist[i] = n*max_weight
dist[1] = 0
for i in range(1,n+1):
    pred[i] = -1
pred[1] = 0

exist = {}
for i in range(1,n+1):
    exist[i] = False
Q = [1]

while len(Q) != 0:
    i = Q[0]
    for k in adj_list[i]:
        if dist[k[0]] > dist[i] + k[1]:
            dist[k[0]] = dist[i] + k[1]
            pred[k[0]] = i
            if exist[k[0]] == False:
                Q.append(k[0])
                exist[k[0]] = True
    exist[i] = False
    Q.pop(0)

field = ['Vertex','Distance','Predecessor']

with open(file[:-3]+'.csv','w+') as Output:
    header = str(field).lstrip("[").rstrip("]") + '\n'
    Output.write(header)
    for i in range(1,n+1):
        rows = str([i,dist[i],pred[i]]).lstrip("[").rstrip("]") + '\n'
        Output.write(rows)
