import tkinter as tk
from tkinter import ttk

class SliderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HW7")
        
        # 創建主框架
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 創建滑動條1
        ttk.Label(self.main_frame, text="滑動條1").grid(row=0, column=0, pady=5)
        self.slider1_value = tk.IntVar(value=0)
        self.slider1_label = ttk.Label(self.main_frame, text="0")
        self.slider1_label.grid(row=1, column=0)
        self.slider1 = ttk.Scale(self.main_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                               variable=self.slider1_value, command=self.update_values)
        self.slider1.grid(row=2, column=0, pady=5)
        
        # 創建滑動條2
        ttk.Label(self.main_frame, text="滑動條2").grid(row=3, column=0, pady=5)
        self.slider2_value = tk.IntVar(value=0)
        self.slider2_label = ttk.Label(self.main_frame, text="0")
        self.slider2_label.grid(row=4, column=0)
        self.slider2 = ttk.Scale(self.main_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                               variable=self.slider2_value, command=self.update_values)
        self.slider2.grid(row=5, column=0, pady=5)
        
        # 創建滑動條總和標籤
        ttk.Label(self.main_frame, text="數值總和:").grid(row=6, column=0, pady=5)
        self.slider_sum = ttk.Label(self.main_frame, text="0")
        self.slider_sum.grid(row=7, column=0)
        
        # 創建輸入框
        self.entry1 = ttk.Entry(self.main_frame)
        self.entry1.grid(row=8, column=0, pady=5)
        self.entry1.bind('<KeyRelease>', self.calculate_sum)
        
        ttk.Label(self.main_frame, text="+").grid(row=9, column=0)
        
        self.entry2 = ttk.Entry(self.main_frame)
        self.entry2.grid(row=10, column=0, pady=5)
        self.entry2.bind('<KeyRelease>', self.calculate_sum)
        
        # 創建輸入框總和標籤
        ttk.Label(self.main_frame, text="總和:").grid(row=11, column=0, pady=5)
        self.entry_sum = ttk.Label(self.main_frame, text="0")
        self.entry_sum.grid(row=12, column=0)

    def update_values(self, event=None):
        # 更新滑動條值的顯示
        self.slider1_label.config(text=str(int(self.slider1_value.get())))
        self.slider2_label.config(text=str(int(self.slider2_value.get())))
        
        # 計算並更新總和
        total = int(self.slider1_value.get()) + int(self.slider2_value.get())
        self.slider_sum.config(text=str(total))

    def calculate_sum(self, event=None):
        try:
            # 獲取輸入框的值
            value1 = int(self.entry1.get()) if self.entry1.get() else 0
            value2 = int(self.entry2.get()) if self.entry2.get() else 0
            
            # 計算並更新總和
            total = value1 + value2
            self.entry_sum.config(text=str(total))
        except ValueError:
            # 如果輸入非數字，保持原值
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SliderApp(root)
    root.mainloop() 