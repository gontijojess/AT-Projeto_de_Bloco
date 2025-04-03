def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the sequence
    sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            sequence.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], ''.join(reversed(sequence))

X1 = "ABCDGHETMAU"
Y1 = "AEDFHRSTUI"
length, sequence = lcs(X1, Y1)
print(f"Sequência comum mais longa entre {X1} e {Y1}:")
print(f"LCS: {sequence}")
print(f"Comprimento LCS: {length}\n")

X2 = "AGGTAB"
Y2 = "GXTAAYB"
length, sequence = lcs(X2, Y2)
print(f"Sequência comum mais longa entre {X2} e {Y2}:")
print(f"LCS: {sequence}")
print(f"Comprimento LCS: {length}\n")

X3 = "ACADB"
Y3 = "CBDAC"
length, sequence = lcs(X3, Y3)
print(f"Sequência comum mais longa entre {X3} e {Y3}:")
print(f"LCS: {sequence}")
print(f"Comprimento LCS: {length}")