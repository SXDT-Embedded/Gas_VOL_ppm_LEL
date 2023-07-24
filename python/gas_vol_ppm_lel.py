import tkinter as tk

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
        entry_lel.insert(tk.END, str(lel))
        entry_vol.delete(0, tk.END)
        entry_vol.insert(tk.END, str(vol))
        entry_ppm.delete(0, tk.END)
        entry_ppm.insert(tk.END, str(ppm))

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

# 创建主窗口
root = tk.Tk()
root.title("燃气爆炸下限计算器")
root.geometry("400x300")

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
