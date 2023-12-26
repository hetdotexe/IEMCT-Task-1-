def find_solutions():
    solutions = []
    for i in range(11):  
        for j in range(11): 
            for k in range(11):  
                if i + j + k == 10:
                    solutions.append((i, j, k))
    return solutions

answer = find_solutions()
for x in answer:
    print(f"Solution: x = {x[0]}, y = {x[1]}, z = {x[2]}")
