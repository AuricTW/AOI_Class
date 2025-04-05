import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 從網路攝影機擷取影像
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()
ret, frame = camera.read()
if not ret:
    print("Error: Failed to capture image.")
    exit()

# 2. 轉換為灰階影像
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 3. 轉換為二值化影像，閾值設定為 
_, binary_frame = cv2.threshold(gray_frame, 130, 255, cv2.THRESH_BINARY)

# 4. 轉換為負片影像 (255 減去像素值)
negative_frame = 255 - frame

# 5. 彩色影像調亮
bright_frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=50)  # alpha: 對比度, beta: 亮度

# 6. 灰階影像調暗
dark_gray_frame = cv2.convertScaleAbs(gray_frame, alpha=0.8, beta= -90)
# 釋放攝影機
camera.release()


# 使用 plt 顯示各種影像

# Matplotlib 顯示彩色影像時，需要先將 BGR 轉成 RGB
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
negative_frame_rgb = cv2.cvtColor(negative_frame, cv2.COLOR_BGR2RGB)
bright_frame_rgb = cv2.cvtColor(bright_frame, cv2.COLOR_BGR2RGB)

# 建立 2x3 的圖表
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# 第 1 行
axes[0, 0].imshow(frame_rgb)
axes[0, 0].set_title("Original")
axes[0, 0].axis('off')

axes[0, 1].imshow(gray_frame, cmap='gray')
axes[0, 1].set_title("Grayscale")
axes[0, 1].axis('off')

axes[0, 2].imshow(binary_frame, cmap='gray')
axes[0, 2].set_title("Binary")
axes[0, 2].axis('off')

# 第 2 行
axes[1, 0].imshow(negative_frame_rgb)
axes[1, 0].set_title("Negative")
axes[1, 0].axis('off')

axes[1, 1].imshow(dark_gray_frame, cmap='gray')
axes[1, 1].set_title("Darkened Grayscale")
axes[1, 1].axis('off')

axes[1, 2].imshow(bright_frame_rgb)
axes[1, 2].set_title("Brightened Color")
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()

# 關閉所有視窗 (若有使用過 cv2.imshow，需要最後再做關閉)
cv2.destroyAllWindows()
