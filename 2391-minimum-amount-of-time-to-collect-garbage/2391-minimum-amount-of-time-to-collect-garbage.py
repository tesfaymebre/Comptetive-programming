class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(1,len(travel)):
            travel[i] += travel[i-1]
            
        total_pick = 0
        P_truck,G_truck,M_truck = 0,0,0
        
        for index,assortment in enumerate(garbage):
            num_p = assortment.count('P')
            num_G = assortment.count('G')
            num_M = assortment.count('M')
            
            total_pick += num_p + num_G + num_M
            
            if index > 0:
                if num_p:
                    P_truck = travel[index-1]

                if num_G:
                    G_truck = travel[index-1]
                    
                if num_M:
                    M_truck = travel[index-1]
                    
        total_time = total_pick + P_truck + G_truck + M_truck
        return total_time
                
            