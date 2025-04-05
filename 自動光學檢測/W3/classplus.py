n_air = 1.0
n_lens = 1.37
R1 = 13.0    # 球面曲率半徑     
d  = 26.0    # 透鏡厚度

# 第一界面矩陣 M1
M1 = [
    [1, 0],
    [(n_air - n_lens) / (R1 * n_lens), n_air / n_lens]
]

# 透鏡內平移矩陣 M2
M2 = [
    [1, d],
    [0, 1]
]

# 第二界面矩陣 M3
M3 = [
    [1, 0],
    [(n_lens - n_air) / (-R1 * n_air), n_lens / n_air]
]

# 2×2 矩陣乘法
def multiply_matrices(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0],
         A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0],
         A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

# 計算整個系統的傳輸矩陣：M_total = M3 * M2 * M1
A = multiply_matrices(M2, M1)
M_total = multiply_matrices(M3, A)
f_effective = -1 / M_total[1][0]
f_truncated = int(f_effective * 100) / 100

print("球心到焦點的距離為: {:.5f}".format(f_effective))
