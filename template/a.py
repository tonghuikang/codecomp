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
        c = Counter(pool)
    
        for k,v in double_match.items():
            x,y,z = k
            
            if x == -1:
                if (0,y,z) in c and (1,y,z) in c:
                    res -= c[0,y,z]*c[1,y,z]
                if (C-1,y,z) in c and (C-2,y,z) in c:
                    res -= c[C-1,y,z]*c[C-2,y,z]
                    
            if y == -1:
                if (x,0,z) in c and (x,1,z) in c:
                    res -= c[x,0,z]*c[x,1,z]
                if (x,C-1,z) in c and (x,C-2,z) in c:
                    res -= c[x,C-1,z]*c[x,C-2,z]
                    
            if z == -1:
                if (x,y,0) in c and (x,y,1) in c:
                    res -= c[x,y,0]*c[x,y,1]
                if (x,y,C-1) in c and (x,y,C-2) in c:
                    res -= c[x,y,C-1]*c[x,y,C-2]
        
#         
#         for k,v in c.items():
#             res -= v*(v-1)
        
        return res        