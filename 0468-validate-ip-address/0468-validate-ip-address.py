class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        IP4 = 'IPv4'
        IP6 = 'IPv6'
        none_of_them = 'Neither'
        
        if '.' in queryIP and ':' in queryIP:
        	return none_of_them
        elif '.' in queryIP:
        	Count = queryIP.split('.')
            
        	if len(Count) != 4:
        		return none_of_them
            
        	for i in Count:
        		if i.isdigit() == False or len(i) == 0 or int(i) > 255 or int(i) < 0 or (len(i) != 1 and i[0] == '0'):
        			return none_of_them
                
        	return IP4
        else:
        	Count = queryIP.split(':')
            
        	if len(Count) != 8:
        		return none_of_them
            
        	for i in Count:
        		if len(i) > 4 or len(i) == 0 or i.isalnum() == False:
        			return none_of_them
                
        		for j in i:
        			if j <= '9' and j >= '0':
        				continue
                        
        			if (j > 'f' and j <= 'z') or (j > 'F' and j <= 'Z'):
        				return none_of_them
                    
        	return IP6