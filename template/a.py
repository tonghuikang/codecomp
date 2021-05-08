from collections import Counter

class ThreeDChessRooks:
    def count(self, C, R, XP, YP, ZP, seed):
#         def print(*args):
#             pass
        
        pool = [(0,0,0) for _ in range(R)]
        
        for i,(x,y,z) in enumerate(zip(XP, YP, ZP)):
            pool[i] = (x,y,z)

        state = seed
        for i in range(len(XP), R):
            state = (state * 1103515245 + 12345) % 2147483648
            x = state%C
            state = (state * 1103515245 + 12345) % 2147483648
            y = state%C
            state = (state * 1103515245 + 12345) % 2147483648
            z = state%C
            pool[i] = (x,y,z)
            
#         print(pool)
        res = 0

        single_match_x = Counter()
        single_match_y = Counter()
        single_match_z = Counter()
        
        for x,y,z in pool:
            single_match_x[x] += 1
            single_match_y[y] += 1
            single_match_z[z] += 1
        
        for k,v in single_match_x.items():
            res += v*(v-1)

        for k,v in single_match_y.items():
            res += v*(v-1)

        for k,v in single_match_z.items():
            res += v*(v-1)
            
        del single_match_x
        del single_match_y
        del single_match_z
#         print(single_match)
#         print("single_match res", res)
        
        double_match = Counter()
        d = C+1
        for x,y,z in pool:
            double_match[x *d*d + y*d + C] += 1
            double_match[C *d*d + y*d + z] += 1
            double_match[x *d*d + C*d + z] += 1
        
        for k,v in double_match.items():
            res -= v*(v-1)

#         print(double_match)
#         print("double_match res", res)
        c = Counter(pool)
    
        for k,v in double_match.items():
            x,f = divmod(k,d*d)
            y,z = divmod(f,d)
#             x,y,z = k
            
            if x == C:
                if (0,y,z) in c and (1,y,z) in c:
                    res -= c[0,y,z]*c[1,y,z]
                if (C-1,y,z) in c and (C-2,y,z) in c:
                    res -= c[C-1,y,z]*c[C-2,y,z]
                    
            if y == C:
                if (x,0,z) in c and (x,1,z) in c:
                    res -= c[x,0,z]*c[x,1,z]
                if (x,C-1,z) in c and (x,C-2,z) in c:
                    res -= c[x,C-1,z]*c[x,C-2,z]
                    
            if z == C:
                if (x,y,0) in c and (x,y,1) in c:
                    res -= c[x,y,0]*c[x,y,1]
                if (x,y,C-1) in c and (x,y,C-2) in c:
                    res -= c[x,y,C-1]*c[x,y,C-2]
        
#         for k,v in c.items():
#             res -= v*(v-1)
        
        return res        