from itertools import combinations
import numpy as np

def countUniquePaths(n: int, r: int) -> int:
    # Generate all r-combinations of indices
    result = []
    for comb in combinations(range(n), r):
        binary_str = ''.join('1' if i in comb else '0' for i in range(n))
        result.append(binary_str)
    return len([s for s in result if "000" not in s and "111" not in s])

print(countUniquePaths(10,4))


def printDp(n: int) -> None:
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = countUniquePaths(i+1, j+1)
    print(np.array(dp))