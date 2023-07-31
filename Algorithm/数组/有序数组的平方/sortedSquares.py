class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        return sorted([i**2 for i in A])

    def sortedSquares2(self, A: list[int]) -> list[int]:
        n = len(A)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] ** 2 > A[j] ** 2:
                ans[pos] = A[i] ** 2
                i += 1
            else:
                ans[pos] = A[j] ** 2
                j -= 1
            pos -= 1
        return ans

if __name__ == "__main__":
    print(Solution().sortedSquares([-4,-1,0,3,10]))
    print(Solution().sortedSquares2([-4,-1,0,3,10]))