import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json, os

FILENAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f: return json.load(f)
    return []

def save_inventory(data):
    with open(FILENAME, "w") as f: json.dump(data, f, indent=2)

class InventoryApp:
    def __init__(self, root):
        self.root, self.inventory = root, load_inventory()
        self.root.title("FreshMart Inventory")
        self.build_ui()
        self.refresh_table()
        self.low_stock_alert()

    def build_ui(self):
        f = ttk.LabelFrame(self.root, text="Add Item")
        f.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.entries = {}
        for i, (label, w) in enumerate([("Name", 20), ("Category", 15), ("Quantity", 10), ("Price/unit", 10)]):
            ttk.Label(f, text=f"{label}:").grid(row=i//2, column=(i%2)*2)
            e = ttk.Entry(f, width=w); e.grid(row=i//2, column=(i%2)*2+1)
            self.entries[label.lower()] = e
        ttk.Label(f, text="Expiry:").grid(row=2, column=0)
        self.expiry = DateEntry(f, width=12, date_pattern='yyyy-mm-dd')
        self.expiry.grid(row=2, column=1)
        ttk.Button(f, text="Add", command=self.add_item).grid(row=2, column=3)

        self.table = ttk.Treeview(self.root, columns=("Name", "Category", "Quantity", "Price", "Expiry"), show="headings", height=12)
        self.table.grid(row=1, column=0, padx=10)
        for col in self.table["columns"]: self.table.heading(col, text=col)

        btns = ttk.Frame(self.root); btns.grid(row=2, column=0, pady=10)
        for txt, cmd in [("Update Stock", self.update_stock), ("Delete", self.delete_item), ("Refresh", self.refresh_table)]:
            ttk.Button(btns, text=txt, command=cmd).pack(side="left", padx=5)

    def refresh_table(self):
        self.table.delete(*self.table.get_children())
        for i, item in enumerate(self.inventory):
            self.table.insert("", "end", iid=i, values=(
                item["name"], item["category"], item["quantity"], f"{item['price']:.2f}", item["expiry"]
            ))

    def add_item(self):
        name, cat = self.entries["name"].get(), self.entries["category"].get()
        qty, price = self.entries["quantity"].get(), self.entries["price/unit"].get()
        if not name or not qty or not price:
            messagebox.showerror("Error", "Name, Quantity, and Price required."); return
        try: qty, price = int(qty), float(price)
        except: messagebox.showerror("Error", "Invalid Quantity/Price."); return
        self.inventory.append({"name": name, "category": cat, "quantity": qty, "price": price, "expiry": self.expiry.get_date().strftime("%Y-%m-%d")})
        save_inventory(self.inventory); self.refresh_table()
        for e in self.entries.values(): e.delete(0, tk.END)

    def selected_index(self):
        sel = self.table.selection()
        return int(sel[0]) if sel else None

    def update_stock(self):
        idx = self.selected_index()
        if idx is None: return messagebox.showwarning("Select", "Select an item.")
        w = tk.Toplevel(self.root); w.title("Update Stock")
        ttk.Label(w, text="New Qty:").grid(row=0, column=0)
        e = ttk.Entry(w, width=10); e.insert(0, str(self.inventory[idx]["quantity"])); e.grid(row=0, column=1)
        def save_qty():
            try: self.inventory[idx]["quantity"] = int(e.get())
            except: messagebox.showerror("Error", "Invalid Qty."); return
            save_inventory(self.inventory); self.refresh_table(); w.destroy()
        ttk.Button(w, text="Save", command=save_qty).grid(row=1, columnspan=2)

    def delete_item(self):
        idx = self.selected_index()
        if idx is None: return messagebox.showwarning("Select", "Select an item.")
        if messagebox.askyesno("Delete", "Delete this item?"):
            del self.inventory[idx]; save_inventory(self.inventory); self.refresh_table()

    def low_stock_alert(self):
        low = [f"{i['name']} (Qty: {i['quantity']})" for i in self.inventory if i["quantity"] < 10]
        if low: messagebox.showwarning("Low Stock", "\n".join(low))

if __name__ == "__main__":
    root = tk.Tk()
    InventoryApp(root)
    root.mainloop()
