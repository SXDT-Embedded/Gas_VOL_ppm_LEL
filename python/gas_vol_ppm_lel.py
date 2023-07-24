import tkinter as tk
from tkinter import messagebox
# 计算LEL、VOL%和ppm

"""
//                 爆炸浓度 (V%)
// 物质名称	分子式	下限 LEL	上限 UEL
// 甲烷	    CH4	    5	        15
// 乙烷	    C2H6	3	        15.5
// 丙烷	    C3H8	2.1	        9.5

// 甲烷的爆炸下限为 5.0VOL%，即 100% LEL=5.0VOL%
// 那么 10% LEL = 5.0VOL% * 10% = 0.5 VOL%
// 10000 ppm = 1 Vol%
"""

# 计算
def calculate():
    gas_type = variable.get()
    try:
        if gas_type == "甲烷":
            if entry_lel.get():
                lel = float(entry_lel.get())
                vol = lel * 0.05
                ppm = vol * 10000
            elif entry_vol.get():
                vol = float(entry_vol.get())
                lel = vol / 0.05
                ppm = vol * 10000
            elif entry_ppm.get():
                ppm = float(entry_ppm.get())
                vol = ppm / 10000
                lel = vol / 0.05
            else:
                lel, vol, ppm = 0, 0, 0

        elif gas_type == "乙烷":
            if entry_lel.get():
                lel = float(entry_lel.get())
                vol = lel * 0.03
                ppm = vol * 10000
            elif entry_vol.get():
                vol = float(entry_vol.get())
                lel = vol / 0.03
                ppm = vol * 10000
            elif entry_ppm.get():
                ppm = float(entry_ppm.get())
                vol = ppm / 10000
                lel = vol / 0.03
            else:
                lel, vol, ppm = 0, 0, 0

        elif gas_type == "丙烷":
            if entry_lel.get():
                lel = float(entry_lel.get())
                vol = lel * 0.021
                ppm = vol * 10000
            elif entry_vol.get():
                vol = float(entry_vol.get())
                lel = vol / 0.021
                ppm = vol * 10000
            elif entry_ppm.get():
                ppm = float(entry_ppm.get())
                vol = ppm / 10000
                lel = vol / 0.021
            else:
                lel, vol, ppm = 0, 0, 0
                
        else:
            lel, vol, ppm = 0, 0, 0

        entry_lel.delete(0, tk.END)
        entry_lel.insert(tk.END, str(round(lel, 4)))
        entry_vol.delete(0, tk.END)
        entry_vol.insert(tk.END, str(round(vol, 4)))
        entry_ppm.delete(0, tk.END)
        entry_ppm.insert(tk.END, str(round(ppm, 4)))

    except ValueError:
        entry_lel.delete(0, tk.END)
        entry_vol.delete(0, tk.END)
        entry_ppm.delete(0, tk.END)
        entry_lel.insert(tk.END, "Error")
        entry_vol.insert(tk.END, "Error")
        entry_ppm.insert(tk.END, "Error")


# 清除所有输入和结果
def clear():
    entry_lel.delete(0, tk.END)
    entry_vol.delete(0, tk.END)
    entry_ppm.delete(0, tk.END)

# 显示帮助信息
def show_help():
    help_text = """
燃气爆炸下限计算器

计算三种气体（甲烷、乙烷、丙烷）的爆炸下限（LEL）、体积百分比（VOL%）和百万分之一体积（ppm）之间的转换关系。

爆炸浓度 (V%)
物质名称    分子式   下限 LEL   上限 UEL
甲烷        CH4         5          15
乙烷        C2H6        3          15.5
丙烷       C3H8        2.1        9.5

例如，甲烷的爆炸下限为 5.0VOL%，即 100% LEL=5.0VOL%
那么 10% LEL = 5.0VOL% * 10% = 0.5 VOL%
10000 ppm = 1 Vol%

计算公式：
甲烷：LEL = VOL% * 0.05，VOL% = LEL / 0.05，ppm = VOL% * 10000
乙烷：LEL = VOL% * 0.03，VOL% = LEL / 0.03，ppm = VOL% * 10000
丙烷：LEL = VOL% * 0.021，VOL% = LEL / 0.021，ppm = VOL% * 10000

使用方法：
1. 选择气体类型。
2. 输入已知值（LEL、VOL%或ppm）。
3. 点击“计算”按钮，即可自动计算其他两个值。
4. 若要清除所有输入和结果，点击“清除”按钮。
5. 若要调整页面大小，请点击菜单栏中的“设置”。

注意事项：
- 请在输入框中只输入数字。
- 计算结果保留小数点后四位。

有任何问题，请点击菜单栏中的“帮助”查看帮助信息。
"""
    messagebox.showinfo("帮助", help_text)
    
"""
# 设置页面
def settings():
    def apply_settings():
        try:
            new_width = int(width_entry.get())
            new_height = int(height_entry.get())
            if 100 <= new_width <= 800 and 100 <= new_height <= 600:
                root.geometry(f"{new_width}x{new_height}")
                current_width_label.config(text=f"当前宽度：{new_width}")
                current_height_label.config(text=f"当前高度：{new_height}")
                max_width_label.config(text=f"最大宽度：{new_width}")
                max_height_label.config(text=f"最大高度：{new_height}")
                settings_window.destroy()
            else:
                messagebox.showerror("错误", "请输入在范围内的宽度和高度（宽度：100-800，高度：100-600）！")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的宽度和高度！")

    settings_window = tk.Toplevel(root)
    settings_window.title("页面设置")
    settings_window.geometry("400x200")

    current_width_label = tk.Label(settings_window, text=f"当前宽度：{root.winfo_width()}")
    current_width_label.pack()

    current_height_label = tk.Label(settings_window, text=f"当前高度：{root.winfo_height()}")
    current_height_label.pack()

    max_width_label = tk.Label(settings_window, text=f"最大宽度：{root.winfo_screenwidth()}")
    max_width_label.pack()

    max_height_label = tk.Label(settings_window, text=f"最大高度：{root.winfo_screenheight()}")
    max_height_label.pack()

    width_label = tk.Label(settings_window, text="宽度：")
    width_label.pack()
    width_entry = tk.Entry(settings_window)
    width_entry.pack()

    height_label = tk.Label(settings_window, text="高度：")
    height_label.pack()
    height_entry = tk.Entry(settings_window)
    height_entry.pack()

    apply_button = tk.Button(settings_window, text="应用", command=apply_settings)
    apply_button.pack()
"""

# 创建主窗口
root = tk.Tk()
root.title("燃气爆炸下限计算器")
root.geometry("400x300")

# 创建菜单栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 创建“帮助”菜单
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="帮助", command=show_help)

"""
# 创建“设置”菜单
settings_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="设置", menu=settings_menu)
settings_menu.add_command(label="调整页面大小", command=settings)
"""

# 气体类型下拉菜单
label_gas_type = tk.Label(root, text="气体类型：")
label_gas_type.pack()
gas_types = ["甲烷", "乙烷", "丙烷"]
variable = tk.StringVar(root)
variable.set(gas_types[0])
gas_type_menu = tk.OptionMenu(root, variable, *gas_types)
gas_type_menu.pack()

# 输入LEL
label_lel = tk.Label(root, text="LEL (Lower Explosive Limit):")
label_lel.pack()
entry_lel = tk.Entry(root)
entry_lel.pack()

# 输入VOL%
label_vol = tk.Label(root, text="VOL% (Volume Percentage):")
label_vol.pack()
entry_vol = tk.Entry(root)
entry_vol.pack()

# 输入ppm
label_ppm = tk.Label(root, text="ppm (Parts Per Million):")
label_ppm.pack()
entry_ppm = tk.Entry(root)
entry_ppm.pack()

# 计算和清除按钮
button_frame = tk.Frame(root)
button_frame.pack()

calculate_button = tk.Button(button_frame, text="计算", command=calculate)
calculate_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="清除", command=clear)
clear_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
