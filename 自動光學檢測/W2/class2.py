import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# 全域變數：用來儲存滑鼠點擊資訊
# 格式: [(x1, y1, 'gray'/'mosaic'), (x2, y2, 'gray'/'mosaic')]
clicked_points = []

# Matplotlib 子圖(軸)物件，稍後在 main() 裡面指定
ax_gray = None
ax_mosaic = None

# 逐區塊馬賽克處理函式
def mosaic_average(gray_img, block_size):
    h, w = gray_img.shape
    for j in range(0, h, block_size):
        for i in range(0, w, block_size):
            # 取出區塊
            block = gray_img[j:j+block_size, i:i+block_size]
            # 計算該區塊的平均灰階值 (用 float32 避免整數截斷)
            avg_val = np.mean(block, dtype=np.float32)
            # 將此區塊填上平均值
            gray_img[j:j+block_size, i:i+block_size] = avg_val
    return gray_img

def on_click(event):
    global clicked_points, ax_gray, ax_mosaic

    if event.inaxes is None:
        return  # 點在圖框外，不處理

    xdata = event.xdata
    ydata = event.ydata
    if xdata is None or ydata is None:
        return  # 點在坐標軸邊緣，無法取得有效座標

    # 判斷點擊到哪個子圖
    if event.inaxes == ax_gray:
        clicked_points.append((xdata, ydata, 'gray'))
    elif event.inaxes == ax_mosaic:
        clicked_points.append((xdata, ydata, 'mosaic'))
    else:
        return

    # 當收集到兩個點，計算歐幾里得距離
    if len(clicked_points) == 2:
        (x1, y1, which1), (x2, y2, which2) = clicked_points
        if which1 == which2:
            dx = x1 - x2
            dy = y1 - y2
            dist = math.sqrt(dx**2 + dy**2)
            print(f"兩點距離（{which1}）: {dist:.2f} pixels")
        else:
            print("兩點分別在不同影像上，無法計算距離。")
        # 清空 clicked_points，方便下次量測
        clicked_points.clear()

def main():
    global ax_gray, ax_mosaic

    # 從檔案讀取圖片
    cap = cv2.imread('W2\P2.png')
    if cap is None:
        print("無法讀取圖片，請檢查檔案路徑。")
        return

    # 將影像轉為灰階
    gray_img = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    
    # 設定馬賽克區塊大小 (學號後兩碼/2)
    block_size = 49

    # 產生馬賽克影像
    mosaic_img = gray_img.copy()
    mosaic_img = mosaic_average(mosaic_img, block_size)

    # 使用 Matplotlib 顯示兩張影像，建立 1x2 的子圖
    fig, (ax_gray, ax_mosaic) = plt.subplots(1, 2, figsize=(12, 6))

    # 左側顯示原始灰階影像
    ax_gray.imshow(gray_img, cmap='gray')
    ax_gray.set_title("gray")
    ax_gray.set_xlabel("X")
    ax_gray.set_ylabel("Y")

    # 右側顯示馬賽克影像
    ax_mosaic.imshow(mosaic_img, cmap='gray')
    ax_mosaic.set_title(f"mosaic (block_size={block_size})")
    ax_mosaic.set_xlabel("X")
    ax_mosaic.set_ylabel("Y")

    # 綁定滑鼠事件，用於量測兩點之間的距離
    fig.canvas.mpl_connect('button_press_event', on_click)

    # 顯示 Matplotlib 視窗
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
