import cv2
import numpy as np

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

# 3. 轉換為二值化影像，閾值設定為 0.3 (255 * 0.3 = 76)
_, binary_frame = cv2.threshold(gray_frame, 76, 255, cv2.THRESH_BINARY)

# 4. 轉換為負片影像 (255 減去像素值)
negative_frame = 255 - frame

# 5. 彩色影像調亮
bright_frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=50)  # alpha: 對比度, beta: 亮度

# 6. 灰階影像調暗
dark_gray_frame = cv2.convertScaleAbs(gray_frame, alpha=0.8, beta=-50)

# 顯示所有結果
cv2.imshow("Original Image", frame)
cv2.imshow("Grayscale Image", gray_frame)
cv2.imshow("Binary Image", binary_frame)
cv2.imshow("Negative Image", negative_frame)
cv2.imshow("Brightened Color Image", bright_frame)
cv2.imshow("Darkened Grayscale Image", dark_gray_frame)

# 按任意鍵結束
cv2.waitKey(0)

# 釋放攝影機與關閉視窗
camera.release()
cv2.destroyAllWindows()
