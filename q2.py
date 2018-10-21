t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
    N, Q = [int(s) for s in input().split(" ")]
    X1, X2, A1, B1, C1, M1 = [int(s) for s in input().split(" ")]
    Y1, Y2, A2, B2, C2, M2 = [int(s) for s in input().split(" ")]
    Z1, Z2, A3, B3, C3, M3 = [int(s) for s in input().split(" ")]
    
    X = [X1, X2]
    Y = [Y1, Y2]
    Z = [Z1, Z2]

    for i in range(2,N):
        X.append((A1 * X[i - 1] + B1 * X[i - 2] + C1) % M1)
        Y.append((A2 * Y[i - 1] + B2 * Y[i - 2] + C2) % M2)

    for i in range(2,Q):
        Z.append((A3 * Z[i - 1] + B3 * Z[i - 2] + C3) % M3)
    Z = Z[:Q]

    L = []
    R = []
    K = []
    for i in range(N):
        L.append(min(X[i],Y[i]) + 1)
        R.append(max(X[i],Y[i]) + 1)

    K = [z + 1 for z in Z]

    num_students = sum([R[i]-L[i]+1 for i in range(N)])

    counter = 0
    for i,k in enumerate(K):
        lock = True
        desired_rank = k
        lower_score = 0
        upper_score = max(R) + 1
        score = 0

        if desired_rank > num_students:
            score = 0
        else:
            while lock:

                rank_L = sum([max(0, R[i] - score + 1) 
                              if L[i] < score else R[i] - L[i] + 1 
                              for i in range(N)])
                rank_U = sum([max(0, R[i] - (score+1) + 1) 
                              if L[i] < (score+1) else R[i] - L[i] + 1 
                              for i in range(N)])

                # print(rank_L, rank_U)

                if desired_rank > rank_L: # score too low
                    upper_score = score
                    score = int((lower_score + upper_score)/2)
                elif desired_rank < rank_U + 1:
                    lower_score = score
                    score = int((lower_score + upper_score)/2)
                else:
                    lock = False
        # print(score)
        counter += score*(i+1)
    
    result = counter
    print("Case #{}: {}".format(case, result))