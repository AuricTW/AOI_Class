import tkinter as tk
from tkinter import ttk

class SliderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HW7")
        self.root.geometry("300x350")  # 增加視窗高度
        
        # 置中
        frame_width = 250
        frame_height = 300
        self.main_frame = tk.Frame(self.root, width=frame_width, height=frame_height)
        self.main_frame.pack(expand=True)
        
        # 滑動條1
        self.slider1_label = tk.Label(self.main_frame, text="滑動條1")
        self.slider1_label.place(relx=0.5, rely=0.12, anchor="center")
        
        self.slider1_value = tk.IntVar(value=0)
        self.slider1_value_label = tk.Label(self.main_frame, text="0")
        self.slider1_value_label.place(relx=0.5, rely=0.17, anchor="center")
        
        self.slider1 = tk.Scale(self.main_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                            length=150, showvalue=0, variable=self.slider1_value,
                            command=self.update_values)
        self.slider1.place(relx=0.5, rely=0.23, anchor="center")
        
        # 滑動條2
        self.slider2_label = tk.Label(self.main_frame, text="滑動條2")
        self.slider2_label.place(relx=0.5, rely=0.33, anchor="center")
        
        self.slider2_value = tk.IntVar(value=0)
        self.slider2_value_label = tk.Label(self.main_frame, text="0")
        self.slider2_value_label.place(relx=0.5, rely=0.38, anchor="center")
        
        self.slider2 = tk.Scale(self.main_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                            length=150, showvalue=0, variable=self.slider2_value,
                            command=self.update_values)
        self.slider2.place(relx=0.5, rely=0.44, anchor="center")
        
        # 數值總和顯示
        self.sum_label = tk.Label(self.main_frame, text="數值總和: 0", font=("Arial", 10))
        self.sum_label.place(relx=0.5, rely=0.55, anchor="center")
        
        # 輸入框1
        self.entry1 = tk.Entry(self.main_frame, width=10)
        self.entry1.place(relx=0.25, rely=0.65, anchor="center")
        self.entry1.bind('<KeyRelease>', self.calculate_sum)
        
        # 加號
        plus_label = tk.Label(self.main_frame, text="+")
        plus_label.place(relx=0.5, rely=0.65, anchor="center")
        
        # 輸入框2
        self.entry2 = tk.Entry(self.main_frame, width=10)
        self.entry2.place(relx=0.75, rely=0.65, anchor="center")
        self.entry2.bind('<KeyRelease>', self.calculate_sum)
        
        # 輸入框總和
        self.entry_sum_label = tk.Label(self.main_frame, text="總和: 0")
        self.entry_sum_label.place(relx=0.5, rely=0.75, anchor="center")

    def update_values(self, event=None):
        # 更新滑動條值顯示
        val1 = int(self.slider1_value.get())
        val2 = int(self.slider2_value.get())
        
        self.slider1_value_label.config(text=str(val1))
        self.slider2_value_label.config(text=str(val2))
        
        # 計算總和
        total = val1 + val2
        self.sum_label.config(text=f"數值總和: {total}")

    def calculate_sum(self, event=None):
        try:
            # 獲取輸入框的值
            value1 = int(self.entry1.get()) if self.entry1.get() else 0
            value2 = int(self.entry2.get()) if self.entry2.get() else 0
            
         
            total = value1 + value2
            self.entry_sum_label.config(text=f"總和: {total}")
        except ValueError:
            
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SliderApp(root)
    root.mainloop() 