import numpy as np
import math

# 定義參數
n_air = 1.0
n_lens = 1.37
R1 = 13.0         # 球面曲率半徑     
d  = 26.0         # 透鏡厚度

# 第一界面
M1 = np.array([
    [1, 0],
    [(n_air - n_lens) / (R1 * n_lens), n_air / n_lens]
])

# 透鏡內平移
M2 = np.array([
    [1, d],
    [0, 1]
])

# 第二界面
M3 = np.array([
    [1, 0],
    [(n_lens - n_air) / (-R1 * n_air), n_lens / n_air]
])

M_total = M3 @ M2 @ M1

#計算距離
f_effective = -1 / M_total[1, 0]
f_truncated = math.floor(f_effective * 100) / 100


print("球心到焦點的距離為: {:.5f}".format(f_truncated))
