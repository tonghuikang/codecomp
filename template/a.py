from collections import Counter

class ThreeDChessRooks:
    def count(self, C, R, XP, YP, ZP, seed):
#         def print(*args):
#             pass
        
        pool = []
        
        for x,y,z in zip(XP, YP, ZP):
            pool.append((x,y,z))

        state = seed
        for i in range(len(XP), R):
            state = (state * 1103515245 + 12345) % 2147483648
            x = state%C
            state = (state * 1103515245 + 12345) % 2147483648
            y = state%C
            state = (state * 1103515245 + 12345) % 2147483648
            z = state%C
            pool.append((x,y,z))
            
#         print(pool)
        res = 0

        single_match = Counter()
        
        for x,y,z in pool:
            single_match[x,-1,-1] += 1
            single_match[-1,y,-1] += 1
            single_match[-1,-1,z] += 1
        
        for k,v in single_match.items():
            res += v*(v-1)
        
#         print(single_match)
#         print("single_match res", res)
        
        double_match = Counter()
        for x,y,z in pool:
            double_match[x,y,-1] += 1
            double_match[-1,y,z] += 1
            double_match[x,-1,z] += 1
        
        for k,v in double_match.items():
            res -= v*(v-1)

#         print(double_match)
#         print("double_match res", res)
            
        for k,v in double_match.items():
            x,y,z = k
            
            if x == -1:
                if (0,y,z) in pool and (1,y,z) in pool:
                    res -= 1
                if (C-1,y,z) in pool and (C-2,y,z) in pool:
                    res -= 1
                    
            if y == -1:
                if (x,0,z) in pool and (x,1,z) in pool:
                    res -= 1
                if (x,C-1,z) in pool and (x,C-2,z) in pool:
                    res -= 1
                    
            if z == -1:
                if (x,y,0) in pool and (x,y,1) in pool:
                    res -= 1
                if (x,y,C-1) in pool and (x,y,C-2) in pool:
                    res -= 1
        
#         c = Counter(pool)
#         for k,v in c.items():
#             res -= v*(v-1)
        
        return res        