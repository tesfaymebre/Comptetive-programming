class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        players.sort()
        trainers.sort()
        
        p_t = 0
        
        for x in players:
            while p_t < len(trainers) and x > trainers[p_t]:
                p_t += 1
                
            if p_t < len(trainers):
                count += 1
                p_t += 1
            else:
                break
                
        return count