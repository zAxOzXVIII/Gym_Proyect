import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from validations.validate import Validaciones
import controller.control_index as control
import datetime
from PIL import Image, ImageTk

class View_User:
    def __init__(self, window):
        self.window = window
        # Validaciones
        self.validate_str = (self.window.register(lambda P, max_length: Validaciones.validate_entry(P, max_length, Validaciones.validar_longitud)), "%P", 45)
        self.validate_int = (self.window.register(lambda P, max_length: Validaciones.validate_entry(P, max_length, Validaciones.validar_numero)), "%P", 11)
        self.validate_float = (self.window.register(Validaciones.validar_numero_flotante), "%P")

    def Main_Users(self):
        self.window.geometry("640x480")

        self.navbar = tk.Frame(self.window, bg="blue", height=40)
        self.navbar.pack(fill="x")

        self.button_Person = tk.Button(self.navbar, text="Persona", bg="blue", fg="white", command=lambda:Validaciones.back_window(self.Main_User, self.window))
        self.button_Person.pack(side="left", padx=10, pady=5)

        self.button_Measures = tk.Button(self.navbar, text="Carga de Ejercicios", bg="blue", fg="white", command=lambda:Validaciones.back_window(self.Main_Exercise_Kit, self.window))
        self.button_Measures.pack(side="left", padx=10, pady=5)

        self.button_Diet = tk.Button(self.navbar, text="Dieta", bg="blue", fg="white", command=lambda:Validaciones.back_window(self.Main_Diet, self.window))
        self.button_Diet.pack(side="left", padx=10, pady=5)

        self.button_Training_Plan = tk.Button(self.navbar, text="Plan de Entreno", bg="blue", fg="white", command=lambda:Validaciones.back_window(self.Main_Routine_Plan, self.window))
        self.button_Training_Plan.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        # Asignando contenido al Frame
        self.Main_User_Content(self.contenido)
    
    # Funcion donde irá el contenido del Frame
    def Main_User_Content(self, tkFrame):
        self.background_image = Image.open("docs/images/logo_gym.png")
        self.background_image = self.background_image.resize((638, 440), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        tk.Label(tkFrame, bg="white", image=self.background_photo, background="#000000").place(x=0, y=0)

# Apartado de User
    # Main_User -> ventana principal de opciones de control de usuario
    def Main_User(self):
        # instancia de controladores
        self.control_User = control.UsuarioC()

        # Asignando widgets a la ventana
        self.navbar = tk.Frame(self.window, bg="blue", height=40)
        self.navbar.pack(fill="x")

        self.button_id = tk.Button(self.navbar, text="Buscar ID", bg="blue", fg="white", command=self.Form_Search_User)
        self.button_id.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Users, self.window))
        self.button_Back.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        self.treeview = ttk.Treeview(self.contenido, columns=("Col1", "Col2", "Col3", "Col4", "Col5"), show="headings")
        self.treeview.heading("Col1", text="ID")
        self.treeview.heading("Col2", text="NUMERO")
        self.treeview.heading("Col3", text="DIRECCION")
        self.treeview.heading("Col4", text="NOMBRE")
        self.treeview.heading("Col5", text="STATUS")
        self.treeview.pack(fill="both", expand=True)

        # fill table
        for row in self.control_User.get_all_users_Controller():
            self.treeview.insert("", "end", values=row)
        
        # Actualizar y ajustar la geometría automáticamente
        self.window.update_idletasks()
        self.window.geometry("")

# Formulario para buscar registro por id
    def Form_Search_User(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        label_user_id = tk.Label(self.top_level, text="Ingrese el ID")
        label_user_id.grid(row=0, column=0, padx=25, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_User.get_all_users_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=0, column=1, padx=25, pady=5)

        button_add = tk.Button(self.top_level, text="Buscar", command=self.Query_Search_User)
        button_add.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    def Query_Search_User(self):
        data_user_level = self.control_User.get_one_users_Controller(self.entry_user_id.get().split()[0])[0]
        messagebox.showinfo("Sesion de usuario", f"=======================================\nnumero de usuario:{data_user_level[1]}\ndireccion:{data_user_level[2]}\nnombre:{data_user_level[3]}\nstatus:{data_user_level[4]}")

# Plan de entreno apartado---
    # Main de Main_Exercise_Kit
    def Main_Exercise_Kit(self):
        # instancia de controladores
        self.control_Exercise_Kit = control.Set_EjerciciosC()
        self.control_Routine_Plan = control.RutinaC()
        self.control_User = control.UsuarioC()

        # Asignando widgets a la ventana
        self.navbar = tk.Frame(self.window, bg="blue", height=40)
        self.navbar.pack(fill="x")

        self.button_id = tk.Button(self.navbar, text="Buscar ID", bg="blue", fg="white", command=self.Form_Search_Exercise_Kit)
        self.button_id.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Users, self.window))
        self.button_Back.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        self.treeview = ttk.Treeview(self.contenido, columns=("Col1", "Col2", "Col3", "Col4", "Col5"), show="headings")
        self.treeview.heading("Col1", text="ID")
        self.treeview.heading("Col2", text="RUTINA")
        self.treeview.heading("Col3", text="COMIENZO DE EJERCICIOS")
        self.treeview.heading("Col4", text="PLAN DE RUTINA")
        self.treeview.heading("Col5", text="USUARIO")
        self.treeview.pack(fill="both", expand=True)

        # fill table
        for row in self.control_Exercise_Kit.get_all_exercise_kits_Controller():
            self.treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[5]))
        
        # Actualizar y ajustar la geometría automáticamente
        self.window.update_idletasks()
        self.window.geometry("")

# Formulario para buscar registro por id
    def Form_Search_Exercise_Kit(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        label_user_id = tk.Label(self.top_level, text="Ingrese el ID")
        label_user_id.grid(row=0, column=0, padx=25, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_Exercise_Kit.get_all_exercise_kits_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=0, column=1, padx=25, pady=5)

        button_add = tk.Button(self.top_level, text="Buscar", command=self.Query_Search_Exercise_Kit)
        button_add.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    def Query_Search_Exercise_Kit(self):
        data_user_level = self.control_Exercise_Kit.get_one_exercise_kits_Controller(self.entry_user_id.get().split()[0])[0]
        messagebox.showinfo("Sesion de usuario", f"=======================================\nrutina:{data_user_level[1]}\nfecha de inicio:{data_user_level[2]}\nnombre de rutina:{data_user_level[3]}\nusuario:{data_user_level[4]}")

# Apartado Dieta
    # Main_Diet -> ventana principal de opciones de control de niveles de usuario
    def Main_Diet(self):
        # instancia de controladores
        self.control_Diet = control.DietaC()
        self.control_User = control.UsuarioC()
        self.control_Rol = control.RolC()

        # Asignando widgets a la ventana
        self.navbar = tk.Frame(self.window, bg="blue", height=40)
        self.navbar.pack(fill="x")

        self.button_id = tk.Button(self.navbar, text="Buscar ID", bg="blue", fg="white", command=self.Form_Search_Diet)
        self.button_id.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Users, self.window))
        self.button_Back.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        self.treeview = ttk.Treeview(self.contenido, columns=("Col1", "Col2", "Col3", "Col4"), show="headings")
        self.treeview.heading("Col1", text="ID")
        self.treeview.heading("Col2", text="DESCRIPCION")
        self.treeview.heading("Col3", text="STATUS")
        self.treeview.heading("Col4", text="USUARIO")
        self.treeview.pack(fill="both", expand=True)

        # fill table
        for row in self.control_Diet.get_all_diets_Controller():
            self.treeview.insert("", "end", values=row)
        
        # Actualizar y ajustar la geometría automáticamente
        self.window.update_idletasks()
        self.window.geometry("")

# Formulario para buscar registro por id
    def Form_Search_Diet(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        label_user_id = tk.Label(self.top_level, text="Ingrese el ID")
        label_user_id.grid(row=0, column=0, padx=25, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_Diet.get_all_diets_Controller():
            data = f"{user[0]} - {user[1].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=0, column=1, padx=25, pady=5)

        button_add = tk.Button(self.top_level, text="Buscar", command=self.Query_Search_Diet)
        button_add.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    def Query_Search_Diet(self):
        data_user_level = self.control_Diet.get_one_diets_Controller(self.entry_user_id.get().split()[0])[0]
        messagebox.showinfo("Sesion de usuario", f"=======================================\nDescripcion de la dieta:{data_user_level[1]}\nEstatus:{'activo' if data_user_level[2]== 1 else 'inactivo'}\nUsuario:{data_user_level[3]}")

# Apartado plan de rutina
    # Main_Routine_Plan -> ventana principal de opciones de control de niveles de usuario
    def Main_Routine_Plan(self):
        # instancia de controladores
        self.control_Routine_Plan = control.RutinaC()
        self.control_User = control.UsuarioC()
        self.control_Rol = control.RolC()

        # Asignando widgets a la ventana
        self.navbar = tk.Frame(self.window, bg="blue", height=40)
        self.navbar.pack(fill="x")

        self.button_id = tk.Button(self.navbar, text="Buscar ID", bg="blue", fg="white", command=self.Form_Search_Routine_Plan)
        self.button_id.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Users, self.window))
        self.button_Back.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        self.treeview = ttk.Treeview(self.contenido, columns=("Col1", "Col2", "Col3"), show="headings")
        self.treeview.heading("Col1", text="ID")
        self.treeview.heading("Col2", text="NOMBRE")
        self.treeview.heading("Col3", text="DIAS DEL PLAN")
        self.treeview.pack(fill="both", expand=True)

        # fill table
        for row in self.control_Routine_Plan.get_all_routine_plans_Controller():
            self.treeview.insert("", "end", values=row)
        
        # Actualizar y ajustar la geometría automáticamente
        self.window.update_idletasks()
        self.window.geometry("")

# Formulario para buscar registro por id
    def Form_Search_Routine_Plan(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        label_user_id = tk.Label(self.top_level, text="Ingrese el ID")
        label_user_id.grid(row=0, column=0, padx=25, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_Routine_Plan.get_all_routine_plans_Controller():
            data = f"{user[0]} - {user[1].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=0, column=1, padx=25, pady=5)

        button_add = tk.Button(self.top_level, text="Buscar", command=self.Query_Search_Routine_Plan)
        button_add.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    def Query_Search_Routine_Plan(self):
        data_user_level = self.control_Routine_Plan.get_one_routine_plans_Controller(self.entry_user_id.get().split()[0])[0]
        messagebox.showinfo("Sesion de usuario", f"=======================================\nplan:{data_user_level[1]}\ndias del plan:{data_user_level[2]}")