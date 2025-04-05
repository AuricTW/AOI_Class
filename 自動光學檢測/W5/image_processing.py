import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("影像處理工具 D1155099 李韋宏")
        self.root.geometry("800x800")  # 增加視窗高度
        
        # 初始化變數
        self.original_image = None
        self.processed_image = None
        self.kernel = np.ones((4,4), np.uint8)  # 半徑為4的盤型遮罩
        
        # 創建主框架
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 創建狀態標籤
        self.status_label = tk.Label(self.main_frame, text="原始圖片", font=('Arial', 16))
        self.status_label.pack(side=tk.TOP, pady=10)
        
        # 創建圖片顯示區域
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # 圖片顯示標籤
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(expand=True)
        
        # 創建按鈕框架
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(side=tk.TOP, pady=10)
        
        # 創建按鈕
        self.create_buttons()
        
        # 自動載入預設圖片
        self.load_default_image()

    def create_buttons(self):
        # 設定按鈕樣式
        button_width = 15
        button_height = 2
        
        # 創建按鈕容器框架
        button_container = tk.Frame(self.button_frame)
        button_container.pack(expand=True)
        
        # 各種處理按鈕
        tk.Button(button_container, text="原始圖片", command=self.show_original, 
                 width=button_width, height=button_height).pack(pady=5)
        tk.Button(button_container, text="侵蝕處理", command=self.erosion,
                 width=button_width, height=button_height).pack(pady=5)
        tk.Button(button_container, text="膨脹處理", command=self.dilation,
                 width=button_width, height=button_height).pack(pady=5)
        tk.Button(button_container, text="先侵蝕後膨脹", command=self.erosion_then_dilation,
                 width=button_width, height=button_height).pack(pady=5)

    def load_default_image(self):
        try:
            # 載入彩色圖片
            self.original_image = cv2.imread("image.png")
            if self.original_image is not None:
                # 二值化處理
                _, self.original_image = cv2.threshold(self.original_image, 200, 255, cv2.THRESH_BINARY)
                self.show_original()
            else:
                messagebox.showerror("錯誤", "無法開啟預設圖片 image.png")
        except Exception as e:
            messagebox.showerror("錯誤", f"載入圖片時發生錯誤：{str(e)}")

    def display_image(self, image):
        # 調整圖片大小
        height, width = image.shape[:2]
        max_size = 400
        if height > max_size or width > max_size:
            scale = max_size / max(height, width)
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = cv2.resize(image, (new_width, new_height))
        
        # 轉換顏色空間
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 轉換為 PIL 圖片
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)
        
        # 更新標籤
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def show_original(self):
        if self.original_image is not None:
            self.status_label.config(text="原始圖片")
            self.display_image(self.original_image)
            cv2.imwrite('original.jpg', self.original_image)

    def erosion(self):
        if self.original_image is None:
            messagebox.showerror("錯誤", "請先開啟圖片")
            return
        
        self.status_label.config(text="侵蝕處理結果")
        self.processed_image = cv2.erode(self.original_image, self.kernel, iterations=1)
        self.display_image(self.processed_image)
        cv2.imwrite('erosion.jpg', self.processed_image)

    def dilation(self):
        if self.original_image is None:
            messagebox.showerror("錯誤", "請先開啟圖片")
            return
        
        self.status_label.config(text="膨脹處理結果")
        self.processed_image = cv2.dilate(self.original_image, self.kernel, iterations=1)
        self.display_image(self.processed_image)
        cv2.imwrite('dilation.jpg', self.processed_image)

    def erosion_then_dilation(self):
        if self.original_image is None:
            messagebox.showerror("錯誤", "請先開啟圖片")
            return
        
        self.status_label.config(text="開運算處理結果")
        # 使用形態學開運算
        self.processed_image = cv2.morphologyEx(self.original_image, cv2.MORPH_OPEN, self.kernel)
        self.display_image(self.processed_image)
        cv2.imwrite('opening.jpg', self.processed_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop() 