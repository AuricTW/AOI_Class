import numpy as np
import matplotlib.pyplot as plt


size = 180
a = np.zeros((size, size)) 


for i in range(0, size, 10):
    a[:, i] = 1
for j in range(0, size, 10):
    a[j, :] = 1


cx, cy = size // 2, size // 2
longaxis = np.sqrt(cx**2 + cy**2)


b = np.zeros_like(a)
for i in range(size):
    for j in range(size):
        dist = np.sqrt((i - cx)**2 + (j - cy)**2)
        scale = 0.9 * dist / longaxis  # 可調整係數 0.9
        m = int(round(cx + scale * (i - cx)))
        n = int(round(cy + scale * (j - cy)))
        if 0 <= m < size and 0 <= n < size:
            b[m, n] = a[i, j]


c = np.zeros_like(a)
for i in range(size):
    for j in range(size):
        dist = np.sqrt((i - cx)**2 + (j - cy)**2)
      
        scale = 1 + 0.4 * (longaxis - dist) / longaxis
        m = int(round(cx + scale * (i - cx)))
        n = int(round(cy + scale * (j - cy)))
        if 0 <= m < size and 0 <= n < size:
            c[m, n] = a[i, j]


fig, axes = plt.subplots(1, 3, figsize=(12, 4))


tick_values = [25, 50, 75, 100, 125, 150, 175]

# (1) 原始方格
axes[0].imshow(a, cmap='gray')
axes[0].set_title('base')
axes[0].set_xticks(tick_values)
axes[0].set_yticks(tick_values)


# (2) 枕型畸變
axes[1].imshow(b, cmap='gray')
axes[1].set_title('Pincushion')
axes[1].set_xticks(tick_values)
axes[1].set_yticks(tick_values)


# (3) 桶狀畸變
axes[2].imshow(c, cmap='gray')
axes[2].set_title('Barrel')
axes[2].set_xticks(tick_values)
axes[2].set_yticks(tick_values)


plt.tight_layout()
plt.show()
