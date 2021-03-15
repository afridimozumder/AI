graph = { 

    "S": {"A": 2, "B": 1,"G": 9}, 

    "A": {"C": 2, "D": 3}, 

    "B": {"D": 2, "E": 4}, 

    "C": {"G": 4}, 

    "D": {"G": 4},
    
    "E": {},
    
    "G": {}, 


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

        if state == self.goal: 

            return True 

  

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
         


def ucs(gp,pop_index): 

    frontier =[] 

    node = Node(gp.initial) 

    actions=list() 

    frontier.append(node) 

    explored = set() 

    while frontier: 

        if len(frontier)==0: return "Fail" 

        leaf=frontier.pop(pop_index) 

        print("Current Location :",leaf.state) 

        test = gp.goal_test(leaf.state) 

        if test == True: 

            print("Destination Reached") 

            return leaf 

            break 

        else: 

            print("Not the Destination") 

            explored.add(leaf) 

            actions = leaf.expand(gp) 

            for a in actions: 

                if a not in explored: 

                    frontier.append(a) 

                    frontier.sort(key=lambda x:x.path_cost) 

  

                     

result  = ucs(gp,pop_index=0) 

print("\nFrom Starting State S, Result for UCS:", result.solution(),"\nPath cost :", result.path_cost)
