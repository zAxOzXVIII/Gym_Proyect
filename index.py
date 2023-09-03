import tkinter as tk
from view.view_index import Vista

if __name__ == '__main__':
    window = tk.Tk()
    app = Vista(window)
    window.mainloop()
