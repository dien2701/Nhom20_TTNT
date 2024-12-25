import tkinter as tk
from tkinter import messagebox
import itertools

def calculate_path_cost(path, costs):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += costs[path[i]][path[i + 1]]
    total_cost += costs[path[-1]][path[0]]  # Quay lại thành phố đầu tiên
    return total_cost

def bfs_tsp(costs):
    num_cities = len(costs)
    min_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(range(num_cities)):
        current_cost = calculate_path_cost(perm, costs)
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = perm

    return min_cost, best_path

def solve_tsp():
    try:
        num_cities = int(entry_num_cities.get())
        if num_cities <= 0:
            raise ValueError("Số lượng thành phố phải lớn hơn 0.")
        
        costs = []
        for i in range(num_cities):
            row = []
            for j in range(num_cities):
                cost_entry = entry_costs[i][j].get()
                if not cost_entry.isdigit():
                    raise ValueError("Chi phí phải là số nguyên dương.")
                row.append(int(cost_entry))
            costs.append(row)

        min_cost, best_path = bfs_tsp(costs)

        # Thêm thành phố ban đầu vào lộ trình
        full_path = best_path + (best_path[0],)
        result_text = f"Tổng chi phí tối thiểu là: {min_cost}\nLộ trình tối ưu là: {' -> '.join(f'Thành phố {i}' for i in full_path)}"
        messagebox.showinfo("Kết quả", result_text)

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def create_cost_entries():
    try:
        num_cities = int(entry_num_cities.get())
        if num_cities <= 0:
            raise ValueError("Số lượng thành phố phải lớn hơn 0.")
        
        for widget in frame_costs.winfo_children():
            widget.destroy()

        global entry_costs
        entry_costs = []
        for i in range(num_cities):
            row_entries = []
            for j in range(num_cities):
                entry = tk.Entry(frame_costs, width=10, font=('Arial', 13))
                entry.grid(row=i, column=j, padx=4, pady=4)  
                row_entries.append(entry)
            entry_costs.append(row_entries)

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Tạo giao diện chính
root = tk.Tk()
root.title("Bài toán người du lịch")
root.geometry("800x500")

# Căn giữa cửa sổ
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (800 // 2)
y = (screen_height // 2) - (500 // 2)
root.geometry(f"800x500+{x}+{y}")

# Nhập số lượng thành phố
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nhập số lượng thành phố:").grid(row=0, column=0)
entry_num_cities = tk.Entry(frame_input, width=10, font=('Arial', 14))  # Tăng kích thước ô nhập
entry_num_cities.grid(row=0, column=1)

tk.Button(frame_input, text="Tạo bảng chi phí", command=create_cost_entries).grid(row=0, column=2)

# Nhập chi phí
frame_costs = tk.Frame(root)
frame_costs.pack(pady=10)

# Nút giải bài toán
tk.Button(root, text="Bài toán người du lịch", command=solve_tsp).pack(pady=10)

root.mainloop()