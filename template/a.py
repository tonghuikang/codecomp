class ThreeDChessRooks:
    def count(self, C, R, XP, YP, ZP, seed):
        
        X = [0 for _ in range(R)]
        Y = [0 for _ in range(R)]
        Z = [0 for _ in range(R)]
        
        for i in range(len(XP)):
            X[i] = XP[i]
            Y[i] = YP[i]
            Z[i] = ZP[i]

        state = seed
        for i in range(len(XP), R):
            state = (state * 1103515245 + 12345) % 2147483648
            X[i] = state%C
            state = (state * 1103515245 + 12345) % 2147483648
            Y[i] = state%C
            state = (state * 1103515245 + 12345) % 2147483648
            Z[i] = state%C
            
        print(X)
        print(Y)
        print(Z)