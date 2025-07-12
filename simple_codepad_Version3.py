import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)
    root.title("GRAPHENE - New File")

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)
            root.title(f"GRAPHENE - {filepath}")
        except Exception as e:
            messagebox.showerror("Open File", f"Cannot open file: {e}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text.get(1.0, tk.END))
            root.title(f"GRAPHENE - {filepath}")
        except Exception as e:
            messagebox.showerror("Save File", f"Cannot save file: {e}")

root = tk.Tk()
root.title("GRAPHENE")
root.geometry("700x500")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

text = tk.Text(root, font=("Consolas", 12), undo=True)
text.pack(fill=tk.BOTH, expand=1)

root.mainloop()