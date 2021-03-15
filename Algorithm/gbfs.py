graph = {
    "S":{"G":9,"A":2,"B":1},
    "A":{"S":2,"C":2,"D":3},
    "B":{"S":1,"D":2,"E":4},
    "C":{"A":2,"G":4},
    "D":{"A":3,"G":4,"B":2},
    "E":{"B":4},
    "G":{"C":4,"D":4,"S":9}
}

heuristicSLD={
    "S":6,
    "A":0,
    "B":6,
    "C":4,
    "D":1,
    "E":10,
    "G":0
    }

class graphProblem:
    
    def __init__(self,initial,goal,graph): 
        self.initial=initial 
        self.goal=goal 
        self.graph=graph 
    def actions(self,state): 
        return list(self.graph[state].keys()) 
    def result(self,state,action): 
        return action 
    def goal_test(self,state): 
        return state == self.goal 
    def path_cost(self,cost_so_far,state1,action,state2): 
        return cost_so_far + self.graph[state1][state2]        
  

class Node: 

    def __init__(self,state,parent=None,action=None,path_cost=0): 
        self.state=state 
        self.parent=parent 
        self.action=action 
        self.path_cost=path_cost 
    def expand(self,graphProblem): 

        return [self.child_node(graphProblem,action) 

                for action in graphProblem.actions(self.state)] 
    def child_node(self,graphProblem,action): 
        next_state=graphProblem.result(self.state,action)         
        return Node(next_state,self,action, 
                    graphProblem.path_cost(self.path_cost,self.state,action,next_state)) 
    def path(self):         
        node, path_back = self, []        
        while node:             
            path_back.append(node)             
            node = node.parent       
        return list(reversed(path_back)) 
    def solution(self):         
        return [node.action for node in self.path()[1:]] 

gp=graphProblem("S","G",graph) 

def best_first_search(gp,f): 
    node=Node(gp.initial) 
    frontier=[] 
    explored=set() 
    child=list() 
    frontier.append(node)
    
    while frontier: 
        if len(frontier)==0:  return "Failure" 
        city=frontier.pop(0) 
        if(gp.goal_test(city.state)):  

            return city  

        else:  
            explored.add(city.state) 
            child=city.expand(gp) 

            for i in child: 
                if i.state not in explored and child not in frontier: 
                    frontier.append(i) 
                    frontier.sort(key=f) 

def ucs(gp,f):return best_first_search(gp,f) 
ucsresult=ucs(gp,f=lambda node:node.path_cost) 

print() 

def gbfs(gp,f):return best_first_search(gp,f) 
gbfsresult=gbfs(gp,f=lambda node:heuristicSLD[node.state]) 
print("BBFS Path :",gbfsresult.solution(),"\nPath cost:",gbfsresult.path_cost) 

print() 

def astar(gp,f):return best_first_search(gp,f) 
astarresult=astar(gp,f=lambda node:node.path_cost+heuristicSLD[node.state]) 
print("\nA* Path :",astarresult.solution(),"\nPath cost:\n",ucsresult.path_cost) 





