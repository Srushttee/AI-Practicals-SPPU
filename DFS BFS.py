def dfs(visited,graph,node): 
    if node not in visited: #checks whether the current node has not been visited before. 
        #If it hasn't been visited, it prints the node, marks it as visited by adding it to the visited set, and proceeds to visit its neighbors.
        
        print(node,end = " ") #arguement to specify that space should be printed 
        visited.add(node) #adds current node to visited
        for neighbour in graph[node]: #iterates over the neighours of the current node
            dfs(visited, graph, neighbour) #makes recursive call for the function dfs for the neighbouring nodes

def bfs(visited,graph,node,queue):
    visited.add(node) #adds  starting node to visited 
    queue.append(node) #appends starting node to queue

    while queue:
        s = queue.pop(0) #deques the front element 
        print(s,end = " ") #prints the current value of s
        for neighbour in graph[s]: #the neigbouring node is denoted as s
            if neighbour not in visited: #if the neighouring nodeof the node is not in visited it will visit the node
                visited.add(neighbour) #it will mark the visited  neigbouring node as visited
                queue.append(neighbour) #enqueues the visited neigbour

def main():
    visited1 = set() # TO keep track of DFS visited nodes by initializing empty set
    visited2 = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict() #creating an empty dictionary in and assigning it to the variable graph 


    #loop for displaying iterative message to the user and taking user input

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i))) #taking user input for number of edges for a node
        graph[i] = list() # predefined data structure in python and appending the input given to a list

        #for loop for 
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i))) #enter the number of edges for a node 
            graph[i].append(node)  #storing the input in node 

    print("The following is DFS")
    dfs(visited1, graph, 1) # function that performs Depth-First Search on a graph, starting from the node with the value 1. 
    print()
    print("The following is BFS") 
    bfs(visited2, graph, 1, queue) # a function with four arguments: visited2, graph, 1, and queue.bfs() is a function that performs Breadth-First Search on a graph, starting from the node with the value 1


if __name__=="__main__": #for checking whether the scrip is imported as a module in another script
    main() #function call for the main function to execute.