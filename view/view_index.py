import tkinter as tk
from tkinter import messagebox, PhotoImage
import controller.control_index as control
from view.view_Admin import View_Admin
from view.view_Trainer import View_Trainer
from view.view_User import View_User
from validations.validate import Validaciones
from PIL import Image, ImageTk



# Clase config de Wwindow
class Vista:
    def __init__(self, window):
        self.window = window
        # asignacion de configuracion de la ventana
        self.window.title("Gym")
        self.window.wm_minsize(100, 100)
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap("docs/images/logo_gym.ico")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        # Toma de atributos de clases
        self.Login = Login(self.window)

        # Redireccionando hacia Login
        self.LoginI()
    
    def LoginI(self):
        self.Login.Login_Main()

# Clase Login
class Login:
    def __init__(self, window):
        self.window = window
        # Atributo Usuario_Login
        self.Usuario_Login = control.Usuario_LoginC()
        self.Admin = View_Admin(self.window)
        self.Trainer = View_Trainer(self.window)
        self.User = View_User(self.window)
        # Validaciones
        self.validate_str = (self.window.register(lambda P, max_length: Validaciones.validate_entry(P, max_length, Validaciones.validar_longitud)), "%P", 45)
        self.validate_int = (self.window.register(lambda P, max_length: Validaciones.validate_entry(P, max_length, Validaciones.validar_numero)), "%P", 16)
        self.validate_float = (self.window.register(Validaciones.validar_numero_flotante), "%P")

    def Login_Main(self):
        # Cargar la imagen como fondo (en formato GIF o PNG)
        self.background_image = Image.open("docs/images/logo_gym.png")
        self.background_image = self.background_image.resize((64, 64), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        login_frame = tk.Frame(self.window, background="white")
        login_frame.grid(row=0, column=0, sticky="nsew")

        login_frame_logo = tk.Frame(self.window, background="white")
        login_frame_logo.grid(row=0, column=1, sticky="nsew")

        background_label = tk.Label(login_frame_logo, image=self.background_photo)
        background_label.grid(row=0, column=1)

        tk.Label(login_frame, text="Inicio de Sesión", font=("Helvetica", 16, "bold"), background="white").grid(row=0, columnspan=2, pady=10)

        tk.Label(login_frame, text="Usuario:", background="white").grid(row=1, column=0, sticky="e", pady=(2, 7))
        username_entry = tk.Entry(login_frame, validate="key", validatecommand=self.validate_str, background="white")
        username_entry.grid(row=1, column=1, padx=10, pady=(2, 7))

        tk.Label(login_frame, text="Contraseña:", background="white").grid(row=2, column=0, sticky="e", pady=(2, 7))
        password_entry = tk.Entry(login_frame, show="•", validate="key", validatecommand=self.validate_str, background="white")
        password_entry.grid(row=2, column=1, padx=10, pady=(2, 7))

        login_button = tk.Button(login_frame, text="Iniciar Sesión", command= lambda : self.Login_Action(username_entry, password_entry), background="white")
        login_button.grid(row=3, columnspan=2, pady=20)

    def Login_Action(self, username, password):
        # Validaremos que si este lleno el formulario
        if username.get() == "": return messagebox.showwarning("Advertencia del Login", "Debe llenar el apartado Login")
        elif password.get() == "": return messagebox.showwarning("Advertencia del Login", "Debe llenar el apartado Password")

        # Validaremos si existe ese usuario
        user = self.Usuario_Login.login_user_acces_Controller(username.get(), password.get())
        if user != None:
            # Limpiamos ventana
            Validaciones.clean_window(self.window)
            match user[5]:
                case "Admin" : self.Admin.Main_Admin()
                case "entrenador" : self.Trainer.Main_Trainer()
                case "usuario" : self.User.Main_Users()


