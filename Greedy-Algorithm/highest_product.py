class solution:
    # @param A: list of integers
    # @return: return an integer

    def maxp2(self, A):
        A = sorted(A)

        highest_3 = A[-1] * A[-2] * A[-3]
        low2_hi1 = A[0] * A[1] * A[-1]

        return max(highest_3, low2_hi1)
