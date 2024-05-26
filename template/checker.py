import sys
import random

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        # Generate a random directed graph that adheres to the problem constraints
        graph = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                if random.choice([True, False]):
                    graph[i][j] = True
        
        # Ensure the reachability condition holds for every triplet
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if not (graph[i][j] or graph[i][k] or graph[j][k]):
                        choice = random.choice([(i, j), (i, k), (j, k)])
                        graph[choice[0]][choice[1]] = True

        queries = 2 * n
        while queries > 0:
            line = sys.stdin.readline().strip()
            if line.startswith('?'):
                _, i, j = line.split()
                i, j = int(i) - 1, int(j) - 1
                if graph[i][j]:
                    print("YES")
                else:
                    print("NO")
                sys.stdout.flush()
                queries -= 1
            elif line.startswith('!'):
                _, *colors = line.split()
                colors = list(map(int, colors))
                if validate_colors(colors, graph):
                    print("Accepted")
                else:
                    print("Wrong Answer")
                sys.stdout.flush()
                break

def validate_colors(colors, graph):
    n = len(colors)
    for i in range(n):
        for j in range(i + 1, n):
            if colors[i] == colors[j] and not graph[i][j]:
                return False
    return True

if __name__ == "__main__":
    main()