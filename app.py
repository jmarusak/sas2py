import tkinter as tk
from tkinter import ttk

from sas2py.sas import get_sas_code

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("sas2py")
        self.root.state('normal')  # 'normal' window size

        # Create a menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Add File menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add Command menu
        self.command_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Command", menu=self.command_menu)

        # Add submenus
        self.command_menu.add_command(label="Explain", command=None)
        self.command_menu.add_command(label="Generate", command=None)

        # Create main window frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Add input text widget on top of notebooks
        self.input_text = tk.Text(self.main_frame, height=5)
        self.input_text.pack(fill=tk.X)

        # Create left notebook
        self.left_notebook = ttk.Notebook(self.main_frame)
        self.left_notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.left_tab_file = ttk.Frame(self.left_notebook)
        self.left_notebook.add(self.left_tab_file, text=f"SAS")
        self.left_tab_explain = ttk.Frame(self.left_notebook)
        self.left_notebook.add(self.left_tab_explain, text=f"Explain")

        self.left_text_file = tk.Text(self.left_tab_file, height=15)
        self.left_text_file.pack(fill=tk.BOTH, expand=True)
        self.left_text_file.insert(tk.END, get_sas_code())   # sample sas file
        self.left_text_explain = tk.Text(self.left_tab_explain, height=15)
        self.left_text_explain.pack(fill=tk.BOTH, expand=True)

        # Create right notebook
        self.right_notebook = ttk.Notebook(self.main_frame)
        self.right_notebook.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.right_tab_file = ttk.Frame(self.right_notebook)
        self.right_notebook.add(self.right_tab_file, text=f"Python")
        self.right_text_file = tk.Text(self.right_tab_file, height=15)
        self.right_text_file.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
