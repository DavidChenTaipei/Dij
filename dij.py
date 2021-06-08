def dij(graph,vertex,start,dest,vehicle,answer):
    start = start-1
    dest = dest-1
    mark = [False for i in range(vertex)]
    MAX=99999999999
    sp = [MAX for i in range(vertex)]
    sp[start]=0
    first_in =True
    first_in_vehicle = True
    current_vehicle = -1
    go_to=[MAX for i in range(vertex)]
    
    while False in mark:
        first_set =True
        tmp=MAX
        if first_in:
            w = start
            mark[w]= True
            first_in=False
        else:
            for i in range(len(sp)):
                if mark[i]==False:
                    if first_set:
                        former_vehicle = go_to[i]
                        tmp = sp[i]
                        w=i
                        first_set = False
                    elif sp[i]<tmp:
                        former_vehicle = go_to[i]
                        tmp = sp[i]
                        w = i
            mark[w] =True
        
        for z in range(len(mark)):
            if w==start  and  graph[w][z]!=0:
                first_in_vehicle = False
                former_vehicle = vehicle[w][z]
                if isinstance(former_vehicle,int):
                    former_vehicle = str(former_vehicle)
                time = graph[w][z]
            elif graph[w][z]!=0:
                try:
                    former_vehicle.isdigit()
                except:
                    former_vehicle = str(former_vehicle)
                ## 數字是公車 字母是捷運
                if former_vehicle.isdigit() and vehicle[w][z].isdigit(): ##公車轉公車
                    ##看是不是同一台公車
                    if former_vehicle== vehicle[w][z]:
                        time = graph[w][z]
                    else: ## 公車轉公車
                        former_vehicle =  vehicle[w][z]
                        transfer_time = 5
                        time = graph[w][z]+transfer_time
                    
                elif not(former_vehicle.isdigit()) and vehicle[w][z].isdigit(): ##捷運轉公車
                    former_vehicle =  vehicle[w][z]
                    transfer_time = 5
                    time = graph[w][z]+transfer_time
                    
                elif not(former_vehicle.isdigit()) and not(vehicle[w][z].isdigit()): ##捷運轉捷運
                    if former_vehicle== vehicle[w][z]:
                        time = graph[w][z]
                        
                    else: ## 公車轉公車
                        former_vehicle =  vehicle[w][z]
                        transfer_time = 10
                        time = graph[w][z]+transfer_time
                    
                elif former_vehicle.isdigit() and not(vehicle[w][z].isdigit()): ##公車轉捷運
                    former_vehicle =  vehicle[w][z]
                    transfer_time = 10                    
                    time = graph[w][z]+transfer_time
            if mark[z]==False and graph[w][z]!=0:
                if sp[w]+time < sp[z]:
                    sp[z] = sp[w]+time
                    go_to[z] = vehicle[w][z]
    if sp[dest]!=MAX:
        answer.append(sp[dest])
    else:
        answer.append('-1')

    return answer


graph = [[0 for i in range(1000)]for i in range(1000)]
vehicle = [[0 for i in range(1000)]for i in range(1000)] 
largest = 0 
answer=[]
while True:
    x = input().split(' ')
    if x[0]=='L':
        for i in range(int(x[2])):
                line = input().split(' ')
                start = int(line[0])-1
                end = int(line[1])-1
                time = int(line[2])
                graph[start][end] = time
                vehicle[start][end] = x[1]
                largest = max(largest,start)
                largest = max(largest,end)
                
    elif x[0]=='Q':
        answer = dij(graph,largest+1,int(x[1]),int(x[2]),vehicle,answer) ##largest +1 因為0到6 有7個數
    elif x[0]=='E':

        for i in answer:
            print(i)
        break
