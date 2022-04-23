# [["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]
# [["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]
# [["111","111","111"],["010","010","010"],["111","111","111"],["010","010","010"],["000","010","000"],["000","010","000"]]


class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
        # 30 * 8**6 / 2 * n
        
        shapes = [[[int(x) for x in row] for row in shape] for shape in shapes]
        
        def rot1(matrix):
            matrix = [list(col[::-1]) for col in zip(*matrix)]  # once
            return matrix
            
        def rot2(matrix):
            matrix = [list(col[::-1]) for col in matrix][::-1]  # twice
            return matrix
            
        def rot3(matrix):
            matrix = [list(col) for col in zip(*matrix)][::-1]  # thirce
            return matrix
            
        def flip(matrix):
            return matrix[::-1]
        
        @lru_cache(maxsize = 6*8*4)
        def get_length(idx, rotation, edge_idx):
            shape = [[x for x in row] for row in shapes[idx]]
            
            if rotation >= 4:
                shape = flip(shape)
            rotation = rotation%4
            if rotation == 0:
                shape = shape
            elif rotation == 1:
                shape = rot1(shape)
            elif rotation == 2:
                shape = rot2(shape)
            elif rotation == 3:
                shape = rot3(shape)
            else:
                assert False

            if edge_idx == 0:
                return shape[0][1:-1]
            if edge_idx == 2:
                return shape[-1][1:-1]
            if edge_idx == 1:
                return [row[-1] for row in shape[1:-1]]
            if edge_idx == 3:
                return [row[0] for row in shape[1:-1]]
            assert False

        @lru_cache(maxsize = 6*8*4*4)
        def get_corner(idx, rotation, a, b):
            a,b = sorted([a,b])
            
            shape = [[x for x in row] for row in shapes[idx]]
            
            if rotation >= 4:
                shape = flip(shape)
            rotation = rotation%4
            if rotation == 0:
                shape = shape
            elif rotation == 1:
                shape = rot1(shape)
            elif rotation == 2:
                shape = rot2(shape)
            elif rotation == 3:
                shape = rot3(shape)
            else:
                assert False
                
            if a == 0 and b == 1:
                return shape[0][-1]
            if a == 1 and b == 2:
                return shape[-1][-1]
            if a == 2 and b == 3:
                return shape[-1][0]
            if a == 0 and b == 3:
                return shape[0][0]
            assert False
            
        def form(arr, brr):
            for x,y in zip(arr, brr):
                if x + y != 1:
                    return False
            return True
        
        seen = set()
        
        def process(perm):
            for rotations in itertools.product(list(range(8)), repeat=6):                    
                if rotations[0] >= 4:
                    continue
                    
                flag = True
                                        
                for x,y in zip([0,1,2,3], [1,2,3,0]):
                    if not form(get_length(perm[x], rotations[perm[x]], 1), 
                                get_length(perm[y], rotations[perm[y]], 3)):
                        flag = False
                        break
                if not flag:
                    continue

                        
                if not form(get_length(perm[5], rotations[perm[x]], 2), 
                            get_length(perm[0], rotations[perm[y]], 0)):
                    continue
                    
                if not form(get_length(perm[5], rotations[perm[x]], 1)[::-1], 
                            get_length(perm[1], rotations[perm[y]], 0)):
                    continue

                if not form(get_length(perm[5], rotations[perm[x]], 2)[::-1], 
                            get_length(perm[2], rotations[perm[y]], 0)):
                    continue
                    
                if not form(get_length(perm[5], rotations[perm[x]], 3), 
                            get_length(perm[3], rotations[perm[y]], 0)):
                    continue
                    
                    
                if not form(get_length(perm[4], rotations[perm[x]], 0), 
                            get_length(perm[0], rotations[perm[y]], 2)):
                    continue
                    
                if not form(get_length(perm[4], rotations[perm[x]], 1), 
                            get_length(perm[1], rotations[perm[y]], 2)):
                    continue

                if not form(get_length(perm[4], rotations[perm[x]], 2)[::-1], 
                            get_length(perm[2], rotations[perm[y]], 2)):
                    continue
                    
                if not form(get_length(perm[4], rotations[perm[x]], 3)[::-1], 
                            get_length(perm[3], rotations[perm[y]], 2)):
                    continue
                    
                    
                if not (
                    get_corner(perm[0], rotations[perm[0]], 0, 1) +
                    get_corner(perm[1], rotations[perm[1]], 3, 0) +
                    get_corner(perm[5], rotations[perm[5]], 2, 1) == 1
                    and
                    get_corner(perm[0], rotations[perm[0]], 1, 2) +
                    get_corner(perm[1], rotations[perm[1]], 2, 3) +
                    get_corner(perm[4], rotations[perm[4]], 0, 1) == 1
                    and
                    get_corner(perm[0], rotations[perm[0]], 0, 3) +
                    get_corner(perm[5], rotations[perm[5]], 2, 3) +
                    get_corner(perm[3], rotations[perm[3]], 1, 0) == 1
                    and
                    get_corner(perm[0], rotations[perm[0]], 2, 3) +
                    get_corner(perm[3], rotations[perm[3]], 1, 2) +
                    get_corner(perm[4], rotations[perm[4]], 0, 3) == 1

                    and
                    
                    get_corner(perm[1], rotations[perm[1]], 0, 1) +
                    get_corner(perm[2], rotations[perm[2]], 0, 3) +
                    get_corner(perm[5], rotations[perm[5]], 0, 1) == 1
                    and
                    get_corner(perm[4], rotations[perm[4]], 1, 2) +
                    get_corner(perm[1], rotations[perm[1]], 2, 1) +
                    get_corner(perm[2], rotations[perm[2]], 2, 3) == 1
                    and
                    get_corner(perm[2], rotations[perm[2]], 2, 1) +
                    get_corner(perm[4], rotations[perm[4]], 2, 3) +
                    get_corner(perm[3], rotations[perm[3]], 2, 3) == 1
                    and
                    get_corner(perm[2], rotations[perm[2]], 0, 1) +
                    get_corner(perm[3], rotations[perm[3]], 0, 3) +
                    get_corner(perm[5], rotations[perm[5]], 0, 3) == 1
                ):
                    continue
                
                return True
            
            
        cnt = 0
        for prefix, suffix in [
            [[0,1,2], [3,4,5]],

            [[0,2,3], [4,5,1]],
            
            [[0,3,4], [5,1,2]],
            
            [[0,4,5], [1,2,3]],
            
            [[0,5,1], [2,3,4]],
        ]:
            for suffix_perm in itertools.permutations(suffix):
                perm = prefix + list(suffix_perm)
            
                if process(perm):
                    return True
                cnt += 1
        
        print(cnt)  # only getting 15, should get 30
        return False
        
        
        