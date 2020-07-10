import networkx as nx
import matplotlib.pyplot as plt
import heapq
g=nx.Graph()
place = ["Oradea","Zerind","Arad","Timisoara","Lugoj","Mehadia",
         "Drobeta","Craiova","Pitesti","Rimnicu Vilcea","Sibiu",
         "Fagaras","Bucharest","Giurgiu","Urziceni","Vaslui","Iasi","Neamt","Hirsova","Eforie"]
value = [380,374,366,329,244,241,242,160,100,193,253,176,0,77,80,199,226,234,151,161]
heruistic= zip(place,value)
g.add_node("Oradea")
g.add_node("Zerind")
g.add_node("Arad")
g.add_node("Timisoara")
g.add_node("Lugoj")
g.add_node("Mehadia")
g.add_node("Drobeta")
g.add_node("Craiova")
g.add_node("Pitesti")
g.add_node("Rimnicu Vilcea")
g.add_node("Sibiu")
g.add_node("Fagaras")
g.add_node("Bucharest")
g.add_node("Giurgiu")
g.add_node("Urziceni")
g.add_node("Vaslui")
g.add_node("Iasi")
g.add_node("Neamt")
g.add_node("Hirsova")
g.add_node("Eforie")


g.add_edge("Oradea","Zerind",weight=71)
g.add_edge("Zerind","Arad",weight=75)
g.add_edge("Arad","Timisoara",weight=118)
g.add_edge("Timisoara","Lugoj",weight=111)
g.add_edge("Lugoj","Mehadia",weight=70)
g.add_edge("Mehadia","Drobeta",weight=75)
g.add_edge("Drobeta","Craiova",weight=120)
g.add_edge("Craiova","Pitesti",weight=138)
g.add_edge("Pitesti","Rimnicu Vilcea",weight=97)
g.add_edge("Rimnicu Vilcea","Sibiu",weight=80)
g.add_edge("Sibiu","Fagaras",weight=99)
g.add_edge("Fagaras","Bucharest",weight=211)
g.add_edge("Bucharest","Giurgiu",weight=90)
g.add_edge("Bucharest","Urziceni",weight=85)
g.add_edge("Urziceni","Vaslui",weight=142)
g.add_edge("Vaslui","Iasi",weight=92)
g.add_edge("Iasi","Neamt",weight=87)
g.add_edge("Urziceni","Hirsova",weight=98)
g.add_edge("Hirsova","Eforie",weight=86)
g.add_edge("Pitesti","Bucharest",weight=101)
g.add_edge("Arad","Sibiu",weight=140)
g.add_edge("Craiova","Rimnicu Vilcea",weight=146)
g.add_edge("Sibiu","Oradea",weight=151)


#Algorithms
def print_path(parent,child,dest,source,graph):
    path = []
    path_cost =0
    index = child.index(dest)
    old = parent[index]
    path.append(dest)
    path.append(old)
    for i in range(index-1,-1,-1):
        if(child[i]==old):
            old = parent[i]
            path.append(old)
    path.reverse()
    for i in range(len(path)):
        print(path[i],end="->")
        if(i!=len(path)-1):
            data=graph.get_edge_data(path[i],path[i+1])
            path_cost+=data['weight']
    print("\nPath Cost: {}".format(path_cost))

# Uniform Cost Search

def UCS(graph,source,dest):
    cost=0
    flag=1
    queue = []
    child = []
    visited = []
    parent = []
    queue.append(source)
    visited.append(source)
    parent.append(source)
    weight = []
    path_cost=0
    weight.append(0)
    while True:
        current = queue.pop(0)
        #print(current,end="=")
        old_weight = weight.pop(0)
        #print(old_weight)
        if current==dest:
            path_cost=old_weight
            break
        for neighbor in graph.neighbors(current):
            data=graph.get_edge_data(current,neighbor)
            if(neighbor in queue):
                index1 = queue.index(neighbor)
                index2= visited.index(neighbor)
                if data['weight']+old_weight<weight[index1]:
                    weight[index1]=data['weight']
                    parent[index2]=current 
            if(neighbor not in visited):
                weight.append(data['weight']+old_weight)
                cost+=data['weight']
                queue.append(neighbor)
                visited.append(neighbor)
                parent.append(current)
                child.append(neighbor)
                new =0
                for i in range(1,len(weight)):
                    if(weight[new]>weight[i]):
                        new=i
                 
                if new!=0:
                    tem = queue[new]
                    queue[new]= queue[0]
                    queue[0]=tem
                    tem = weight[new]
                    weight[new]=weight[0]
                    weight[0]=tem
                
        if(flag==0):
            break
    
    path_cost = 0
    path = []
    current = dest
    old = parent[visited.index(dest)]
    path.append(dest)
    path.append(old)
    while old!=source:
        index = visited.index(old)
        path.append(parent[index])
        old = parent[index]
    path.reverse()    
#    dindex = visited.index(dest)
#    old = parent[dindex] 
#    path = []
#    path.append(old)
#    start = len(visited)
#    for i in range(start-1,0,-1):
#        
#        if visited[i]==old:
#            old = parent[i]
#            path.append(old)
#    path_cost=0
#    path.reverse()
#    print(list(zip(parent,visited)))
#    print(path)
    for i in range(len(path)-1):
            data = graph.get_edge_data(path[i],path[i+1])
            path_cost+=data['weight']
            print(path[i],end="->")
    print(dest)
    print("Total Cost: {}".format(cost))
    print("\nPath Cost : {}".format(path_cost))
#    for i in range(len(path)):
#        if(i!=len(path)-1):
#            data = graph.get_edge_data(path[i],path[i+1])
#            path_cost+=data['weight']
#        print(path[i],end="->")
#    print(dest)
#    data = graph.get_edge_data(path[len(path)-1],dest)
#    path_cost+=data['weight']
#    print("Total Cost: {}".format(cost))
    

#=======================================]
def print_incomplete(parent,child,dest,source,graph):
    path = []
    path_cost =0
    index = len(child)-1;
    old = parent[index]
    path.append(dest)
    path.append(old)
    for i in range(index-1,-1,-1):
        if(child[i]==old):
            old = parent[i]
            path.append(old)
    path.reverse()
    for i in range(len(path)):
        print(path[i],end="->")
        if(i!=len(path)-1):
            data=graph.get_edge_data(path[i],path[i+1])
            path_cost+=data['weight']
    print("\nPath Cost: {}".format(path_cost))
    
    
    
#===============Greedy BFS======================    
def Greedy(graph,source,dest):
    parent = []
    child = []
    heru = []
    queue = []
    visited = []
    queue.append(source)
    cost = 0
    total_cost = 0
    heru.append(value[place.index(source)])
    current = source
    flag = 0
    while True:
        
        if(current in visited):
            print("Oops! Algortihm Just Stucked")
            queue.pop(0)
            heru.pop(0)
            print_incomplete(parent,child,child[len(child)-1],source,graph)
            return
        visited.append(current)

        for neighbor in graph.neighbors(current):
            
            queue.append(neighbor)
            parent.append(current)
            child.append(neighbor)
            if(neighbor == dest):
                flag=2
                break
            data = graph.get_edge_data(current,neighbor)
            total_cost += data['weight']
            index = place.index(neighbor)
            heru.append(value[index])
        if(flag==2):
            break
        min_in = None
        min_val = 9999999
        queue.pop(0)
        heru.pop(0)
        for i in range(len(heru)):
            if(heru[i]<min_val):
                min_val=heru[i]
                min_in=i
        if(len(queue)==0):
            print("No Path Found")
            break
        if(min_in!=None):
            tem = queue[min_in]
            queue[min_in]=queue[0]
            queue[0]=tem
            tem = heru[min_in]
            heru[min_in]=heru[0]
            heru[0]=tem
       
        current = queue[0]
    dindex = child.index(dest)
    old = parent[dindex] 
    path = []
    path.append(old)
    start = len(parent)
    for i in range(start-1,0,-1):
        
        if child[i]==old:
            old = parent[i]
            path.append(old)

    path.reverse()
    for i in range(len(path)):
        print(path[i],end="->")
    print(dest)
    for i in range(len(path)-1):
        data=graph.get_edge_data(path[i],path[i+1])
        cost+=data['weight']
    data = graph.get_edge_data(path[len(path)-1],dest)
    cost+=data['weight']
    print("Total Cost: {}".format(total_cost))
    #print("\nPath Cost : {}".format(path_cost))
    print("\nPath Cost : {}".format(cost))
    
    
#=======================================
#===============BFS=====================    

def BFS(graph,source,dest):
    old = source
    cost=0
    path_cost=0
    flag=1
    queue = []
    visited = []
    parent = []
    queue.append(source)
    visited.append(source)
    parent.append(source)
    while True:
        current = queue.pop(0) 
        for neighbor in graph.neighbors(current):
            data=graph.get_edge_data(current,neighbor)
            if(neighbor not in visited):
                
                cost+=data['weight']
                queue.append(neighbor)
                visited.append(neighbor)
                parent.append(current)
                if neighbor==dest:
                    flag=0
                    break
        if(flag==0):
            break
    
    old = parent[len(visited)-1] 
    path = []
    path.append(old)
    for i in range(len(visited)-1,0,-1):
        if(visited[i]==old):
            old = parent[i]
            path.append(old)
    path.reverse()
    for i in range(len(path)):
        print(path[i],end="->")
        if(i!=len(path)-1):
            data=graph.get_edge_data(path[i],path[i+1])
            path_cost+=data['weight']
    data=graph.get_edge_data(path[len(path)-1],dest)
    path_cost+=data['weight']
    print(dest)
            

    print("Total Cost: {}".format(cost))
    print("\nPath Cost: {}".format(path_cost))
#===================================================
    #===================Iterative Deepnign DFS==================



    

def DFS(graph,source,dest):
    cost=0
    stackq = []
    level = []
    path= []
    parent = []
    child = []
    depth = -1
    c_depth = 0
    visited = []
    while True:
        depth+=1
        stackq.clear()
        level.clear()
        path.clear()
        visited.clear()
        stackq.append(source)
        level.append(0)
        c_depth = 0
        children = 1
        visited.append(source)
        child.clear()
        parent.clear()
        while True:
            if(len(stackq)==0):
                break
            current = stackq.pop()
            children-=1

            if(current==dest):
                print("Total Cost: {}".format(cost))
                print_path(parent,child,dest,source,graph)
                return
            if(children==0 and len(path)>0):
                path.pop()
                c_depth-=1
            if(level.pop()==depth):
                continue
            
            
            c_depth+=1
            path.append(current)
            for neighbor in graph.neighbors(current):
                if(neighbor not in path and neighbor not in visited):
                    data = graph.get_edge_data(current,neighbor)
                    cost+=data['weight']
                    children+=1
                    stackq.append(neighbor)
                    level.append(c_depth)
                    visited.append(neighbor)
                    parent.append(current)
                    child.append(neighbor)
            
            
        

    


while True:
    source = input("Enter Source Name: ")
    if(source in place):
        break
while True:   
    dest = input("Enter Destination Name: ")
    if(dest in place):
        break
print("\n\n             *************************************")
print("                   Breadth First Search Algorithm\n")
BFS(g,source,dest)
print("                  ##################################")

print("\n\n              **************************************")
print("                       Uniform Cost Search\n")
UCS(g,source,dest)
print("                  ##################################")

print("\n\n              ***********************************")
print("                     Greedy Best First Search\n")
Greedy(g,source,dest)
print("                  ##################################")
print("\n\n              ***********************************")
print("                      Iterative Depth First Search\n")
DFS(g,source,dest)
print("                  #################################")





# pos=nx.spectral_layout(g)
# fig, ax = plt.subplots(figsize=(40, 30),dpi=100)
# nx.draw_networkx_nodes(g,pos,with_labels=True,ax=ax)
# labels = nx.get_edge_attributes(g,'weight')
# nx.draw_networkx_labels(g,pos)
# nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
# nx.draw_networkx_edges(g,pos,edge_labels=labels,edge_color='r')
# plt.show()


