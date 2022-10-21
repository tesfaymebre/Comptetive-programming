class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
       
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(len(ingredients)):
            for element in ingredients[i]:
                graph[element].append(recipes[i])
                indegree[recipes[i]] += 1
                
        
        recipes = set(recipes)
        supplies = set(supplies)
        can_create = []
        queue = deque()
        
        for element in graph:
            if indegree[element] == 0 and element in supplies:
                queue.append(element)
                
        while queue:
            size = len(queue)
            
            for i in range(size):
                element = queue.popleft()
                
                for recipe in graph[element]:
                    indegree[recipe] -= 1
                    
                    if indegree[recipe] == 0 and recipe in recipes:
                        can_create.append(recipe)
                        queue.append(recipe)
                        
        return can_create