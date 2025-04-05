import numpy as np
import matplotlib.pyplot as plt


size = 180  
a = np.zeros((size, size))  

# 1. 建立一個 180x180 的全黑影像，並在上面畫出白色的十字線
for i in range(0, size, 10):
    a[:, i] = 1
for j in range(0, size, 10):
    a[j, :] = 1

# 2. 計算中心點與最大半徑，用於後續畸變計算
cx, cy = size // 2, size // 2
longaxis = np.sqrt(cx**2 + cy**2)  # 從中心到四角的最長距離(約 127.28)

# 3. 建立「枕型畸變」(Pincushion Distortion) - 放射狀收縮
b = np.zeros_like(a)
for i in range(size):
    for j in range(size):
        # 計算該像素距離中心的半徑
        dist = np.sqrt((i - cx)**2 + (j - cy)**2)
        # 設計一個收縮比例，可自行調整 0.9 來改變畸變強度
        scale = 0.9 * dist / longaxis
        # 計算新的座標 (m, n)
        m = int(round(cx + scale * (i - cx)))
        n = int(round(cy + scale * (j - cy)))
        # 若新的座標仍在影像範圍內，則把原始像素值搬過去
        if 0 <= m < size and 0 <= n < size:
            b[m, n] = a[i, j]

# 4. 建立「桶狀畸變」(Barrel Distortion) - 放射狀擴張
c = np.zeros_like(a)
for i in range(size):
    for j in range(size):
        dist = np.sqrt((i - cx)**2 + (j - cy)**2)
        # 設計一個擴張比例，可自行調整公式使變形更明顯或更細微
        # 下面示範：scale = 1 + 0.4*(longaxis - dist)/longaxis
        # 也可換成例如: scale = 1 + 0.5*(dist/longaxis)**2 等等
        scale = 1 + 0.4 * (longaxis - dist) / longaxis
        m = int(round(cx + scale * (i - cx)))
        n = int(round(cy + scale * (j - cy)))
        if 0 <= m < size and 0 <= n < size:
            c[m, n] = a[i, j]

# 5. 使用 Matplotlib 同時顯示三張圖
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(a, cmap='gray')
axes[0].set_title('原始方格')
axes[0].axis('off')

axes[1].imshow(b, cmap='gray')
axes[1].set_title('枕型畸變 (Pincushion)')
axes[1].axis('off')

axes[2].imshow(c, cmap='gray')
axes[2].set_title('桶狀畸變 (Barrel)')
axes[2].axis('off')

plt.tight_layout()
plt.show()
