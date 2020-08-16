import sys

targets = [0]
triangle = [[0]]

for i in range(8):
    targets = [2*target for target in targets]
    targets.append(targets[-1] + 1)
        
    new_arr = []
    for i,target in enumerate(targets[:-1]):
        new_arr.append(target - sum(frame[i] for x,frame in enumerate(triangle) if x >= i) - sum(new_arr))
    new_arr.append(targets[-1] - sum(new_arr))
    
    triangle.append(new_arr)
    
new_triangle = [[] for _ in triangle]
for _,column in enumerate(triangle[::-1]):
    for j,cell in enumerate(column):
        new_triangle[j].append(cell)
    

length = int(input())
grid = [row[:length] for row in new_triangle[:length]]
supplementary_path = sum(new_triangle[length-1][length:])

# print(new_triangle)
# print(new_triangle[length-1][length:])

for row in grid:
    print(" ".join(str(x) for x in row),flush = True)

 
for i in range(int(input())):
    inp = int(input()) + supplementary_path

    x,y = 1,1
    print("{} {}".format(x,y), flush=True)
    bin_string = format(inp, '0{}b'.format(2*length-1))
    print(bin_string)
    for b in bin_string:
        if b == '1':
            y += 1
        else:
            x += 1
        print("{} {}".format(x,y), flush=True)

    