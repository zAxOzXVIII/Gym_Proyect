import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from validations.validate import Validaciones
from model.pdf_script import PDFGenerator, PDFGenerator_Pay
import controller.control_index as control
import datetime
from PIL import Image, ImageTk

class View_Trainer:
    def __init__(self, window):
        self.window = window
        # Validaciones
        self.validate_str = (self.window.register(lambda P, max_length: Validaciones.validate_entry(P, max_length, Validaciones.validar_longitud)), "%P", 45)
        self.validate_int = (self.window.register(lambda P, max_length: Validaciones.validate_entry(P, max_length, Validaciones.validar_numero)), "%P", 11)
        self.validate_float = (self.window.register(Validaciones.validar_numero_flotante), "%P")

    def Main_Trainer(self):
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

        self.button_Pay = tk.Button(self.navbar, text="Pago", bg="blue", fg="white", command=lambda:Validaciones.back_window(self.Main_Pay, self.window))
        self.button_Pay.pack(side="left", padx=10, pady=5)

        self.button_Pay = tk.Button(self.navbar, text="PDF User", bg="blue", fg="white", command=self.Main_PDF_Generator)
        self.button_Pay.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        # Asignando contenido al Frame
        self.Main_Trainer_Content(self.contenido)
    
    # Funcion donde irá el contenido del Frame
    def Main_Trainer_Content(self, tkFrame):
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

        self.button_update = tk.Button(self.navbar, text="Actualizar", bg="blue", fg="white", command=self.Form_Update_User)
        self.button_update.pack(side="left", padx=10, pady=5)

        self.button_create = tk.Button(self.navbar, text="Agregar", bg="blue", fg="white", command=self.Form_Add_User)
        self.button_create.pack(side="left", padx=10, pady=5)

        self.button_delete = tk.Button(self.navbar, text="Eliminar", bg="blue", fg="white", command=self.Form_Delete_User)
        self.button_delete.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Trainer, self.window))
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

# Formulario para agregar Usuarios
    def Form_Add_User(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title
        self.top_level.grab_set()

        self.label_number = tk.Label(self.top_level, text="Número de telefono:")
        self.label_number.grid(row=1, column=0, padx=10, pady=5)
        self.entry_number = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_int)
        self.entry_number.grid(row=1, column=1, padx=10, pady=5)

        self.label_address = tk.Label(self.top_level, text="Dirección:")
        self.label_address.grid(row=2, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_str)
        self.entry_address.grid(row=2, column=1, padx=10, pady=5)

        self.label_name = tk.Label(self.top_level, text="Nombre:")
        self.label_name.grid(row=3, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_str)
        self.entry_name.grid(row=3, column=1, padx=10, pady=5)

        self.label_status = tk.Label(self.top_level, text="Estado:")
        self.label_status.grid(row=4, column=0, padx=10, pady=5)
        self.entry_status = ttk.Combobox(self.top_level, values=("inactivo", "activo"), state="readonly")
        self.entry_status.grid(row=4, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Add_User)
        button_add.grid(row=5, columnspan=2, padx=10, pady=10)

    def Query_Add_User(self):
        if self.entry_number.get() == "" and self.entry_address.get() == "" and self.entry_name.get() == "" and self.entry_status.get() == "":
            messagebox.showwarning("Advertencia de Sesion de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_User.create_user_Controller(self.entry_number.get(), self.entry_address.get(), self.entry_name.get(), self.entry_status.get()) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha insertado exitosamente al usuario")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_User.get_all_users_Controller():
                    self.treeview.insert("", "end", values=row)
            else:
                messagebox.showwarning("Advertencia del sistema", "Error al insertar el usuario")

# Formulario para actualizar Usuarios
    def Form_Update_User(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return

        # ID de usuario
        self.user_id = data_treeview[0]

        self.top_level = tk.Toplevel(self.window)
        self.top_level.title
        self.top_level.grab_set()

        self.label_number = tk.Label(self.top_level, text="Número de telefono:")
        self.label_number.grid(row=1, column=0, padx=10, pady=5)
        self.entry_number = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_int)
        self.entry_number.insert(0, data_treeview[1])
        self.entry_number.grid(row=1, column=1, padx=10, pady=5)

        self.label_address = tk.Label(self.top_level, text="Dirección:")
        self.label_address.grid(row=2, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_str)
        self.entry_address.insert(0, data_treeview[2])
        self.entry_address.grid(row=2, column=1, padx=10, pady=5)

        self.label_name = tk.Label(self.top_level, text="Nombre:")
        self.label_name.grid(row=3, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_str)
        self.entry_name.insert(0, data_treeview[3])
        self.entry_name.grid(row=3, column=1, padx=10, pady=5)

        self.label_status = tk.Label(self.top_level, text="Estado:")
        self.label_status.grid(row=4, column=0, padx=10, pady=5)
        self.entry_status = ttk.Combobox(self.top_level, values=("inactivo", "activo"), state="readonly")
        self.entry_status.set(data_treeview[4])
        self.entry_status.grid(row=4, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Update_User)
        button_add.grid(row=5, columnspan=2, padx=10, pady=10)

    def Query_Update_User(self):
        if self.entry_number.get() == "" and self.entry_address.get() == "" and self.entry_name.get() == "" and self.entry_status.get() == "":
            messagebox.showwarning("Advertencia de Sesion de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_User.update_user_Controller(self.user_id, self.entry_number.get(), self.entry_address.get(), self.entry_name.get(), self.entry_status.get()) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha actualizado exitosamente al usuario")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_User.get_all_users_Controller():
                    self.treeview.insert("", "end", values=row)
            else:
                messagebox.showwarning("Advertencia del sistema", "Error al actualizar el usuario")

# Formulario para borrar un usuario
    def Form_Delete_User(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return
        else: 
            if messagebox.askyesno("Pregunta del sistema", f"Esta seguro de eliminar el registro\n{data_treeview[0]} - {data_treeview[3]}"):
                self.Query_Delete_User(data_treeview[0])
            else: messagebox.showinfo("Mensaje del sistema", "Se ha revertido con exito")

    def Query_Delete_User(self, id_user_access):
        if self.control_User.delete_user_Controller(id_user_access) != None:
            messagebox.showinfo("Mensaje del sistema", "Se ha eliminado el usuario nuevo con exito.")
            # actualizar tabla
            self.treeview.delete(*self.treeview.get_children())
            for row in self.control_User.get_all_users_Controller():
                self.treeview.insert("", "end", values=row)
        else: messagebox.showwarning("Advertencia del sistema", "Error al eliminar el usuario.")

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

        self.button_update = tk.Button(self.navbar, text="Actualizar", bg="blue", fg="white", command=self.Form_Update_Exercise_Kit)
        self.button_update.pack(side="left", padx=10, pady=5)

        self.button_create = tk.Button(self.navbar, text="Agregar", bg="blue", fg="white", command=self.Form_Add_Exercise_Kit)
        self.button_create.pack(side="left", padx=10, pady=5)

        self.button_delete = tk.Button(self.navbar, text="Eliminar", bg="blue", fg="white", command=self.Form_Delete_Exercise_Kit)
        self.button_delete.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Trainer, self.window))
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

# Formulario para agregar rutinas
    def Form_Add_Exercise_Kit(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_routine = tk.Label(self.top_level, text="Rutina:")
        self.label_routine.grid(row=1, column=0, padx=10, pady=5)
        self.entry_routine = tk.Entry(self.top_level)
        self.entry_routine.grid(row=1, column=1, padx=10, pady=5)

        self.label_date = tk.Label(self.top_level, text="Fecha de comienzo:")
        self.label_date.grid(row=2, column=0, padx=10, pady=5)
        today = datetime.date.today()
        self.entry_date = DateEntry(self.top_level, mindate=today, date_pattern="yyyy-mm-dd")
        self.entry_date.grid(row=2, column=1, padx=10, pady=5)

        self.label_routine_id = tk.Label(self.top_level, text="ID del plan de rutina:")
        self.label_routine_id.grid(row=3, column=0, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_routine = []
        for user in self.control_Routine_Plan.get_all_routine_plans_Controller():
            data = f"{user[0]} - {user[1].split()[0]}"
            data_routine.append(data)

        self.entry_routine_id = ttk.Combobox(self.top_level, values=data_routine, state="readonly")
        self.entry_routine_id.grid(row=3, column=1, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_rol = []
        for rol in self.control_User.get_all_users_Controller():
            data = f"{rol[0]} - {rol[3].split()[0]}"
            data_rol.append(data)

        self.label_user_id = tk.Label(self.top_level, text="ID de Usuario:")
        self.label_user_id.grid(row=4, column=0, padx=10, pady=5)
        self.entry_user_id = ttk.Combobox(self.top_level, values=data_rol, state="readonly")
        self.entry_user_id.grid(row=4, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Add_Exercise_Kit)
        button_add.grid(row=5, columnspan=2, padx=10, pady=10)

    def Query_Add_Exercise_Kit(self):
        if self.entry_routine.get() == "" or self.entry_date.get() == "":
            messagebox.showwarning("Advertencia de Sesion de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Exercise_Kit.insert_exercise_kit_Controller(self.entry_routine.get(), self.entry_date.get(), self.entry_routine_id.get().split()[0], self.entry_user_id.get().split()[0]) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha insertado exitosamente al conjunto de ejercicios")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Exercise_Kit.get_all_exercise_kits_Controller():
                    self.treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[5]))
            else:
                messagebox.showwarning("Advertencia del sistema", "Error al insertar el conjunto de ejercicios")

# Formulario para actualizar rutinas
    def Form_Update_Exercise_Kit(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return

        # ID de usuario
        self.user_id = data_treeview[0]

        self.top_level = tk.Toplevel(self.window)
        self.top_level.title
        self.top_level.grab_set()

        self.label_routine = tk.Label(self.top_level, text="Rutina:")
        self.label_routine.grid(row=1, column=0, padx=10, pady=5)
        self.entry_routine = tk.Entry(self.top_level)
        self.entry_routine.insert(0, data_treeview[1])
        self.entry_routine.grid(row=1, column=1, padx=10, pady=5)

        self.label_date = tk.Label(self.top_level, text="Fecha de comienzo:")
        self.label_date.grid(row=2, column=0, padx=10, pady=5)
        today = datetime.date.today()
        self.entry_date = DateEntry(self.top_level, mindate=today, date_pattern="yyyy-mm-dd")
        self.entry_date.grid(row=2, column=1, padx=10, pady=5)

        self.label_routine_id = tk.Label(self.top_level, text="ID del plan de rutina:")
        self.label_routine_id.grid(row=3, column=0, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_routine = []
        for user in self.control_Routine_Plan.get_all_routine_plans_Controller():
            data = f"{user[0]} - {user[1].split()[0]}"
            data_routine.append(data)

        self.entry_routine_id = ttk.Combobox(self.top_level, values=data_routine, state="readonly")
        self.entry_routine_id.grid(row=3, column=1, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_rol = []
        for rol in self.control_User.get_all_users_Controller():
            data = f"{rol[0]} - {rol[3].split()[0]}"
            data_rol.append(data)

        self.label_user_id = tk.Label(self.top_level, text="ID de Usuario:")
        self.label_user_id.grid(row=4, column=0, padx=10, pady=5)
        self.entry_user_id = ttk.Combobox(self.top_level, values=data_rol, state="readonly")
        self.entry_user_id.grid(row=4, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Update_Exercise_Kit)
        button_add.grid(row=5, columnspan=2, padx=10, pady=10)

    def Query_Update_Exercise_Kit(self):
        if self.entry_routine.get() == "" or self.entry_date.get() == "":
            messagebox.showwarning("Advertencia de Sesion de Ejercicios", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Exercise_Kit.update_exercise_kit_Controller(self.user_id, self.entry_routine.get(), self.entry_date.get(), self.entry_routine_id.get().split()[0], self.entry_user_id.get().split()[0]) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha actualizado exitosamente")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Exercise_Kit.get_all_exercise_kits_Controller():
                    self.treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[5]))
            else:
                messagebox.showwarning("Advertencia del sistema", "Error al actualizar")

# Formulario para borrar un conjunto de ejercicios
    def Form_Delete_Exercise_Kit(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return
        else: 
            if messagebox.askyesno("Pregunta del sistema", f"Esta seguro de eliminar el registro\n{data_treeview[0]} - {data_treeview[1]}"):
                self.Query_Delete_Exercise_Kit(data_treeview[0])
            else: messagebox.showinfo("Mensaje del sistema", "Se ha revertido con exito")

    def Query_Delete_Exercise_Kit(self, id_user_access):
        if self.control_Exercise_Kit.delete_exercise_kit_Controller(id_user_access) != None:
            messagebox.showinfo("Mensaje del sistema", "Se ha eliminado el conjunto de ejercicios nuevo con exito.")
            # actualizar tabla
            self.treeview.delete(*self.treeview.get_children())
            for row in self.control_Exercise_Kit.get_all_exercise_kits_Controller():
                self.treeview.insert("", "end", values=row)
        else: messagebox.showwarning("Advertencia del sistema", "Error al eliminar el conjunto de ejercicios.")

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

        self.button_update = tk.Button(self.navbar, text="Actualizar", bg="blue", fg="white", command=self.Form_Update_Diet)
        self.button_update.pack(side="left", padx=10, pady=5)

        self.button_create = tk.Button(self.navbar, text="Agregar", bg="blue", fg="white", command=self.Form_Add_Diet)
        self.button_create.pack(side="left", padx=10, pady=5)

        self.button_delete = tk.Button(self.navbar, text="Eliminar", bg="blue", fg="white", command=self.Form_Delete_Diet)
        self.button_delete.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Trainer, self.window))
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

# Formulario para agregar sesiones se usuarios
    def Form_Add_Diet(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_description = tk.Label(self.top_level, text="Descripcion:")
        self.label_description.grid(row=0, column=0, padx=10, pady=5)
        self.entry_description = tk.Entry(self.top_level, validate="key")
        self.entry_description.grid(row=0, column=1, padx=10, pady=5)

        self.label_status = tk.Label(self.top_level, text="Status:")
        self.label_status.grid(row=1, column=0, padx=10, pady=5)
        self.entry_status = ttk.Combobox(self.top_level, values=("0 - Sin dieta", "1 - Con dieta"), state="readonly")
        self.entry_status.grid(row=1, column=1, padx=10, pady=5)

        self.label_user_id = tk.Label(self.top_level, text="ID de Usuario:")
        self.label_user_id.grid(row=2, column=0, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_User.get_all_users_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=2, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Add_Diet)
        button_add.grid(row=4, columnspan=2, padx=10, pady=10)

    def Query_Add_Diet(self):
        if self.entry_description.get() == "":
            messagebox.showwarning("Advertencia de Sesion de Dieta", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Diet.insert_diet_Controller(self.entry_description.get(),  self.entry_status.get().split()[0], self.entry_user_id.get().split()[0]) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha insertado la dieta nuevo con exito.")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Diet.get_all_diets_Controller():
                    self.treeview.insert("", "end", values=row)
            else: messagebox.showwarning("Advertencia del sistema", "Error al insertar el usuario.")

# Formulario para actualizar sesiones se usuarios
    def Form_Update_Diet(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return

        # ID de usuario
        self.user_acces_id = data_treeview[0]

        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_description = tk.Label(self.top_level, text="Descripcion:")
        self.label_description.grid(row=0, column=0, padx=10, pady=5)
        self.entry_description = tk.Entry(self.top_level, validate="key")
        self.entry_description.insert(0, data_treeview[1])
        self.entry_description.grid(row=0, column=1, padx=10, pady=5)

        self.label_status = tk.Label(self.top_level, text="Status:")
        self.label_status.grid(row=1, column=0, padx=10, pady=5)
        self.entry_status = ttk.Combobox(self.top_level, values=("0 - Sin dieta", "1 - Con dieta"), state="readonly")
        self.entry_status.set(data_treeview[2])
        self.entry_status.grid(row=1, column=1, padx=10, pady=5)

        self.label_user_id = tk.Label(self.top_level, text="ID de Usuario:")
        self.label_user_id.grid(row=2, column=0, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_User.get_all_users_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=2, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Update_Diet)
        button_add.grid(row=4, columnspan=2, padx=10, pady=10)

    def Query_Update_Diet(self):
        if self.entry_description.get() == "":
            messagebox.showwarning("Advertencia de Dieta de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Diet.update_diet_Controller(self.user_acces_id, self.entry_description.get(), self.entry_status.get().split()[0], self.entry_user_id.get().split()[0]) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha actualizado el usuario nuevo con exito.")
                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Diet.get_all_diets_Controller():
                    self.treeview.insert("", "end", values=row)
            else: messagebox.showwarning("Advertencia del sistema", "Error al actializar el usuario.")

    # Formulario para borrar una sesion de usuario
    def Form_Delete_Diet(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return
        else: 
            if messagebox.askyesno("Pregunta del sistema", f"Esta seguro de eliminar el registro\n{data_treeview[0]} - {data_treeview[1]}"):
                self.Query_Delete_Diet(data_treeview[0])
            else: messagebox.showinfo("Mensaje del sistema", "Se ha revertido con exito")

    def Query_Delete_Diet(self, id_user_access):
        if self.control_Diet.delete_diet_Controller(id_user_access) != None:
            messagebox.showinfo("Mensaje del sistema", "Se ha eliminado el usuario nuevo con exito.")
            # actualizar tabla
            self.treeview.delete(*self.treeview.get_children())
            for row in self.control_Diet.get_all_diets_Controller():
                self.treeview.insert("", "end", values=row)
        else: messagebox.showwarning("Advertencia del sistema", "Error al eliminar el usuario.")

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

        self.button_update = tk.Button(self.navbar, text="Actualizar", bg="blue", fg="white", command=self.Form_Update_Routine_Plan)
        self.button_update.pack(side="left", padx=10, pady=5)

        self.button_create = tk.Button(self.navbar, text="Agregar", bg="blue", fg="white", command=self.Form_Add_Routine_Plan)
        self.button_create.pack(side="left", padx=10, pady=5)

        self.button_delete = tk.Button(self.navbar, text="Eliminar", bg="blue", fg="white", command=self.Form_Delete_Routine_Plan)
        self.button_delete.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Trainer, self.window))
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

# Formulario para agregar sesiones se usuarios
    def Form_Add_Routine_Plan(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_routine = tk.Label(self.top_level, text="Nombre del Plan:")
        self.label_routine.grid(row=0, column=0, padx=10, pady=5)
        self.entry_routine = tk.Entry(self.top_level, validate="key")
        self.entry_routine.grid(row=0, column=1, padx=10, pady=5)

        self.label_days_plan = tk.Label(self.top_level, text="Cantidad de dias:")
        self.label_days_plan.grid(row=1, column=0, padx=10, pady=5)
        self.entry_days_plan = tk.Entry(self.top_level, validate="key")
        self.entry_days_plan.grid(row=1, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Add_Routine_Plan)
        button_add.grid(row=4, columnspan=2, padx=10, pady=10)

    def Query_Add_Routine_Plan(self):
        if self.entry_routine.get() == "":
            messagebox.showwarning("Advertencia de Sesion de Dieta", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Routine_Plan.insert_routine_plan_Controller(self.entry_routine.get(),  self.entry_days_plan.get()) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha insertado la dieta nuevo con exito.")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Routine_Plan.get_all_routine_plans_Controller():
                    self.treeview.insert("", "end", values=row)
            else: messagebox.showwarning("Advertencia del sistema", "Error al insertar el plan.")

# Formulario para actualizar sesiones se usuarios
    def Form_Update_Routine_Plan(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return

        # ID de usuario
        self.user_acces_id = data_treeview[0]

        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_routine = tk.Label(self.top_level, text="Nombre del Plan:")
        self.label_routine.grid(row=0, column=0, padx=10, pady=5)
        self.entry_routine = tk.Entry(self.top_level, validate="key")
        self.entry_routine.insert(0, data_treeview[1])
        self.entry_routine.grid(row=0, column=1, padx=10, pady=5)

        self.label_days_plan = tk.Label(self.top_level, text="Cantidad de dias:")
        self.label_days_plan.grid(row=1, column=0, padx=10, pady=5)
        self.entry_days_plan = tk.Entry(self.top_level, validate="key")
        self.entry_days_plan.insert(0, data_treeview[2])
        self.entry_days_plan.grid(row=1, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Update_Routine_Plan)
        button_add.grid(row=4, columnspan=2, padx=10, pady=10)

    def Query_Update_Routine_Plan(self):
        if self.entry_routine.get() == "":
            messagebox.showwarning("Advertencia de Dieta de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Routine_Plan.update_routine_plan_Controller(self.user_acces_id, self.entry_routine.get(),  self.entry_days_plan.get()) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha actualizado el usuario nuevo con exito.")
                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Routine_Plan.get_all_routine_plans_Controller():
                    self.treeview.insert("", "end", values=row)
            else: messagebox.showwarning("Advertencia del sistema", "Error al actializar el usuario.")

    # Formulario para borrar una sesion de usuario
    def Form_Delete_Routine_Plan(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return
        else: 
            if messagebox.askyesno("Pregunta del sistema", f"Esta seguro de eliminar el registro\n{data_treeview[0]} - {data_treeview[1]}"):
                self.Query_Delete_Routine_Plan(data_treeview[0])
            else: messagebox.showinfo("Mensaje del sistema", "Se ha revertido con exito")

    def Query_Delete_Routine_Plan(self, id_user_access):
        if self.control_Routine_Plan.delete_routine_plan_Controller(id_user_access) != None:
            messagebox.showinfo("Mensaje del sistema", "Se ha eliminado el usuario nuevo con exito.")
            # actualizar tabla
            self.treeview.delete(*self.treeview.get_children())
            for row in self.control_Routine_Plan.get_all_routine_plans_Controller():
                self.treeview.insert("", "end", values=row)
        else: messagebox.showwarning("Advertencia del sistema", "Error al eliminar el usuario.")

# Apartado Pagos
    # Main_Pay -> ventana principal de opciones de control de niveles de usuario
    def Main_Pay(self):
        # instancia de controladores
        self.control_Pay = control.PagoC()
        self.control_User = control.UsuarioC()
        self.control_Rol = control.RolC()

        # Asignando widgets a la ventana
        self.navbar = tk.Frame(self.window, bg="blue", height=40)
        self.navbar.pack(fill="x")

        self.button_id = tk.Button(self.navbar, text="Buscar ID", bg="blue", fg="white", command=self.Form_Search_Pay)
        self.button_id.pack(side="left", padx=10, pady=5)

        self.button_update = tk.Button(self.navbar, text="Actualizar", bg="blue", fg="white", command=self.Form_Update_Pay)
        self.button_update.pack(side="left", padx=10, pady=5)

        self.button_create = tk.Button(self.navbar, text="Agregar", bg="blue", fg="white", command=self.Form_Add_Pay)
        self.button_create.pack(side="left", padx=10, pady=5)

        self.button_delete = tk.Button(self.navbar, text="Eliminar", bg="blue", fg="white", command=self.Form_Delete_Pay)
        self.button_delete.pack(side="left", padx=10, pady=5)

        self.button_delete = tk.Button(self.navbar, text="Exportar PDF", bg="blue", fg="white", command=self.Query_PDF_Pay)
        self.button_delete.pack(side="left", padx=10, pady=5)

        self.button_Back = tk.Button(self.navbar, text="Volver", bg="blue", fg="white", command= lambda : Validaciones.back_window(self.Main_Trainer, self.window))
        self.button_Back.pack(side="left", padx=10, pady=5)

        self.contenido = tk.Frame(self.window, bg="white")
        self.contenido.pack(fill="both", expand=True)

        self.treeview = ttk.Treeview(self.contenido, columns=("Col1", "Col2", "Col3", "Col4", "Col5"), show="headings")
        self.treeview.heading("Col1", text="ID")
        self.treeview.heading("Col2", text="USUARIO")
        self.treeview.heading("Col3", text="CONTRASEÑA")
        self.treeview.heading("Col4", text="NOMBRE")
        self.treeview.heading("Col5", text="ROL")
        self.treeview.pack(fill="both", expand=True)

        # fill table
        for row in self.control_Pay.get_all_payments_with_usernames_Controller():
            self.treeview.insert("", "end", values=row)
        
        # Actualizar y ajustar la geometría automáticamente
        self.window.update_idletasks()
        self.window.geometry("")

# Formulario para buscar registro por id
    def Form_Search_Pay(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        label_user_id = tk.Label(self.top_level, text="Ingrese el ID")
        label_user_id.grid(row=0, column=0, padx=25, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_Pay.get_all_payments_with_usernames_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_pay = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_pay.grid(row=0, column=1, padx=25, pady=5)

        button_add = tk.Button(self.top_level, text="Buscar", command=self.Query_Search_User_Level)
        button_add.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    def Query_Search_User_Level(self):
        data_user_level = self.control_Pay.get_one_payments_with_usernames_Controller(self.entry_pay.get().split()[0])[0]
        messagebox.showinfo("Sesion de usuario", f"=======================================\nmonto total:{data_user_level[1]}\ntotal abonado:{data_user_level[2]}\nusuario:{data_user_level[3]}")

# Formulario para agregar sesiones se usuarios
    def Form_Add_Pay(self):
        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_amount = tk.Label(self.top_level, text="Monto total:")
        self.label_amount.grid(row=0, column=0, padx=10, pady=5)
        self.entry_amount = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_int)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=5)

        self.label_payment_credit = tk.Label(self.top_level, text="Monto abonado:")
        self.label_payment_credit.grid(row=1, column=0, padx=10, pady=5)
        self.entry_payment_credit = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_int)
        self.entry_payment_credit.grid(row=1, column=1, padx=10, pady=5)

        self.label_user_id = tk.Label(self.top_level, text="ID de Usuario:")
        self.label_user_id.grid(row=2, column=0, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_User.get_all_users_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=2, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Add_Pay)
        button_add.grid(row=4, columnspan=2, padx=10, pady=10)

    def Query_Add_Pay(self):
        if self.entry_amount.get() == "" and self.entry_payment_credit == "":
            messagebox.showwarning("Advertencia de Sesion de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Pay.insert_payment_Controller(self.entry_amount.get(),  self.entry_payment_credit.get(), self.entry_user_id.get().split()[0]) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha insertado el usuario nuevo con exito.")

                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Pay.get_all_payments_with_usernames_Controller():
                    self.treeview.insert("", "end", values=row)
            else: messagebox.showwarning("Advertencia del sistema", "Error al insertar el usuario.")

# Formulario para actualizar sesiones se usuarios
    def Form_Update_Pay(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return

        # ID de usuario
        self.user_acces_id = data_treeview[0]

        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        self.label_amount = tk.Label(self.top_level, text="Monto total:")
        self.label_amount.grid(row=0, column=0, padx=10, pady=5)
        self.entry_amount = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_int)
        self.entry_amount.insert(0, data_treeview[1])
        self.entry_amount.grid(row=0, column=1, padx=10, pady=5)

        self.label_payment_credit = tk.Label(self.top_level, text="Monto abonado:")
        self.label_payment_credit.grid(row=1, column=0, padx=10, pady=5)
        self.entry_payment_credit = tk.Entry(self.top_level, validate="key", validatecommand=self.validate_int)
        self.entry_payment_credit.insert(0, data_treeview[2])
        self.entry_payment_credit.grid(row=1, column=1, padx=10, pady=5)

        self.label_user_id = tk.Label(self.top_level, text="ID de Usuario:")
        self.label_user_id.grid(row=2, column=0, padx=10, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_User.get_all_users_Controller():
            data = f"{user[0]} - {user[3].split()[0]}"
            data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.set(data_treeview[3])
        self.entry_user_id.grid(row=2, column=1, padx=10, pady=5)

        button_add = tk.Button(self.top_level, text="Agregar", command=self.Query_Update_Pay)
        button_add.grid(row=4, columnspan=2, padx=10, pady=10)

    def Query_Update_Pay(self):
        if self.entry_amount.get() == "" and self.entry_payment_credit == "":
            messagebox.showwarning("Advertencia de Sesion de Usuario", "Debe llenar todos los formularios")
            return
        else:
            if self.control_Pay.update_payment_Controller(self.user_acces_id, self.entry_amount.get(),  self.entry_payment_credit.get(), self.entry_user_id.get().split()[0]) != None:
                messagebox.showinfo("Mensaje del sistema", "Se ha actualizado el usuario nuevo con exito.")
                # actualizar tabla
                self.treeview.delete(*self.treeview.get_children())
                for row in self.control_Pay.get_all_payments_with_usernames_Controller():
                    self.treeview.insert("", "end", values=row)
            else: messagebox.showwarning("Advertencia del sistema", "Error al actializar el usuario.")

    # Formulario para borrar una sesion de usuario
    def Form_Delete_Pay(self):
        # Verificar que hallá seleccionado una entidad del treeview
        data_treeview = Validaciones.verify_treeview(self.treeview)
        if data_treeview == None:
            messagebox.showwarning("Advertencia del sistema", "Debe seleccionar una fila de la tabla")
            return
        else: 
            if messagebox.askyesno("Pregunta del sistema", f"Esta seguro de eliminar el registro\n{data_treeview[0]} - {data_treeview[3]}"):
                self.Query_Delete_Pay(data_treeview[0])
            else: messagebox.showinfo("Mensaje del sistema", "Se ha revertido con exito")

    def Query_Delete_Pay(self, id_user_access):
        if self.control_Pay.delete_payment_Controller(id_user_access) != None:
            messagebox.showinfo("Mensaje del sistema", "Se ha eliminado el usuario nuevo con exito.")
            # actualizar tabla
            self.treeview.delete(*self.treeview.get_children())
            for row in self.control_Pay.get_all_payments_with_usernames_Controller():
                self.treeview.insert("", "end", values=row)
        else: messagebox.showwarning("Advertencia del sistema", "Error al eliminar el usuario.")

# Apartado para generar PDF
    # Main_PDF_Generator
    def Main_PDF_Generator(self):
        # Asignacion de controladores
        self.control_User = control.UsuarioC()
        self.control_Routine_Plan = control.RutinaC()
        self.control_Exercise_Kit = control.Set_EjerciciosC()

        self.top_level = tk.Toplevel(self.window)
        self.top_level.title("Agregar Acceso")
        self.top_level.grab_set()

        label_user_id = tk.Label(self.top_level, text="Ingrese el ID")
        label_user_id.grid(row=0, column=0, padx=25, pady=5)

        #Asignar usuarios al combobox
        data_user = []
        for user in self.control_User.get_all_users_Controller():
            for ek_user in self.control_Exercise_Kit.get_all_exercise_kits_Controller():
                # Condicion que valida si el usuario existe en set de ejercicios tabla
                if ek_user[6] == user[0]:
                    data = f"{user[0]} - {user[3].split()[0]}"
                    data_user.append(data)

        self.entry_user_id = ttk.Combobox(self.top_level, values=data_user, state="readonly")
        self.entry_user_id.grid(row=0, column=1, padx=25, pady=5)

        button_add = tk.Button(self.top_level, text="Generar", command=self.Query_Search_User_PDF)
        button_add.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

    def Query_Search_User_PDF(self):
        # Leer el valor actual del contador desde el archivo
        try:
            with open("docs/contador.txt", "r") as file:
                contador = int(file.read())
        except FileNotFoundError:
            # Si el archivo no existe, comenzar desde 1
            contador = 1

        data_user = self.control_User.get_one_user_pdf(self.entry_user_id.get().split()[0])[0]
        routine_user = self.control_Routine_Plan.get_one_routine_plans_Controller(data_user[6])[0]
        user_data = {
            "id": data_user[0],
            "number": data_user[1],
            "address": data_user[2],
            "name": data_user[3],
            "status": data_user[4],
            "routine" : data_user[5],
            "exercise_start" : data_user[6],
            "routine_plan" : routine_user[1]
        }

        # Generar el nombre del documento PDF usando el valor del contador
        pdf_filename = f"docs/user_data_{contador}.pdf"

        # Crear el PDF
        pdf_creator = PDFGenerator(user_data, pdf_filename)

        # Incrementar el contador
        contador += 1

        # Guardar el nuevo valor del contador en el archivo
        with open("docs/contador.txt", "w") as file:
            file.write(str(contador))

# Main_PDF_Generator_Pay

    def Query_PDF_Pay(self):
        # Controladores
        self.control_Pay_User = control.PagoC()

        # Leer el valor actual del contador desde el archivo
        try:
            with open("docs/contador_pay.txt", "r") as file:
                contador = int(file.read())
        except FileNotFoundError:
            # Si el archivo no existe, comenzar desde 1
            contador = 1

        data_user = self.control_Pay_User.get_all_payments_with_usernames_Controller()

        # Generar el nombre del documento PDF usando el valor del contador
        pdf_filename = f"docs/user_data_{contador}.pdf"

        # Crear el PDF
        pdf_creator = PDFGenerator_Pay(data_user, pdf_filename)

        # Incrementar el contador
        contador += 1

        # Guardar el nuevo valor del contador en el archivo
        with open("docs/contador_pay.txt", "w") as file:
            file.write(str(contador))
