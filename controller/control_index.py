import tkinter as tk
from tkinter import messagebox
import model.model_index as model

class UsuarioC(model.Usuario):
    def create_user_Controller(self, number, address, name, status):
        # Validaciones
        if number == "":
            messagebox.showwarning("Advertencia Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.create_user(number, address, name, status)
    
    def get_all_users_Controller(self):
        return self.get_all_users()
    
    def get_one_users_Controller(self, id):
        # Validaciones
        if id == "":
            messagebox.showwarning("Advertencia Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_users(id)
    
    def update_user_Controller(self, id, number, address, name, status):
        # Validaciones
        if number == "":
            messagebox.showwarning("Advertencia Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_user(id, number, address, name, status)
    
    def delete_user_Controller(self, id):
        # Validaciones
        if id == "":
            messagebox.showwarning("Advertencia Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_user(id)
    
    def get_one_user_pdf_Controller(self, id):
        # Validaciones
        if id == "":
            messagebox.showwarning("Advertencia Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_user_pdf(id)

class DietaC(model.Dieta):
    def get_all_diets_Controller(self):
        return self.get_all_diets()
    
    def get_one_diets_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Dieta", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_diets(id)
    
    def insert_diet_Controller(self, description, status, user_id):
        if description == "":
            messagebox.showwarning("Advertencia Dieta", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.insert_diet(description, status, user_id)
    
    def update_diet_Controller(self, id, description, status, user_id):
        if description == "":
            messagebox.showwarning("Advertencia Dieta", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_diet(id, description, status, user_id)
    
    def delete_diet_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Dieta", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_diet(id)

class PagoC(model.Pago):
    def get_all_payments_with_usernames_Controller(self):
        return self.get_all_payments_with_usernames()
    
    def get_one_payments_with_usernames_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Pago", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_payments_with_usernames(id)
    
    def insert_payment_Controller(self, amount, payment_credit, user_id):
        if amount == "":
            messagebox.showwarning("Advertencia Pago", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.insert_payment(amount, payment_credit, user_id)
    
    def update_payment_Controller(self, id, amount, payment_credit, user_id):
        if id == "":
            messagebox.showwarning("Advertencia Pago", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_payment(id, amount, payment_credit, user_id)
    
    def delete_payment_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Pago", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_payment(id)

class RolC(model.Rol):
    def get_all_roles_Controller(self):
        return self.get_all_roles()
    
    def get_one_roles_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Rol", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_roles(id)
    
    def insert_role_Controller(self, name):
        if name == "":
            messagebox.showwarning("Advertencia Rol", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.insert_role(name)
    
    def update_role_Controller(self, id, name):
        if id == "":
            messagebox.showwarning("Advertencia Rol", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_role(id, name)
    
    def delete_role_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Rol", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_role(id)

class Usuario_LoginC(model.Usuario_Login):
    def login_user_acces_Controller(self, user, password):
        value = self.login_user_acces(user, password)

        if value==[]: 
            messagebox.showwarning("Login del sistema", "Usuario o contraseña incorrecta")
            return
        elif value != []:
            return value[0]

    def get_all_user_access_Controller(self):
        return self.get_all_user_access()
    
    def get_one_user_access_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Acceso de Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_user_access(id)
    
    def insert_user_access_Controller(self, user_name, password, user_id, rol_id):
        if user_name == "":
            messagebox.showwarning("Advertencia Acceso de Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.insert_user_access(user_name, password, user_id, rol_id)
    
    def update_user_access_Controller(self, id, user_name, password, user_id, rol_id):
        if user_name == "":
            messagebox.showwarning("Advertencia Acceso de Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_user_access(id, user_name, password, user_id, rol_id)
    
    def delete_user_access_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Acceso de Usuario", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_user_access(id)

class RutinaC(model.Rutina):
    def get_all_routine_plans_Controller(self):
        return self.get_all_routine_plans()
    
    def get_one_routine_plans_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Rutina", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_routine_plans(id)
    
    def insert_routine_plan_Controller(self, name, days_plan):
        if name == "":
            messagebox.showwarning("Advertencia Rutina", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.insert_routine_plan(name, days_plan)
    
    def update_routine_plan_Controller(self, id, name, days_plan):
        if id == "":
            messagebox.showwarning("Advertencia Rutina", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_routine_plan(id, name, days_plan)
    
    def delete_routine_plan_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Rutina", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_routine_plan(id)

class Set_EjerciciosC(model.Set_Ejercicio):
    def get_all_exercise_kits_Controller(self):
        return self.get_all_exercise_kits()
    
    def get_one_exercise_kits_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Set de Ejercicios", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.get_one_exercise_kits(id)
    
    def insert_exercise_kit_Controller(self, routine, exercise_start, routine_plan_id, user_id):
        if routine == "":
            messagebox.showwarning("Advertencia Set de Ejercicios", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.insert_exercise_kit(routine, exercise_start, routine_plan_id, user_id)
    
    def update_exercise_kit_Controller(self, id, routine, exercise_start, routine_plan_id, user_id):
        if routine == "":
            messagebox.showwarning("Advertencia Set de Ejercicios", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.update_exercise_kit(id, routine, exercise_start, routine_plan_id, user_id)
    
    def delete_exercise_kit_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Set de Ejercicios", "Debe pasar total de valores correctamente.")
            return
        else:
            return self.delete_exercise_kit(id)

class MedidasC(model.Medidas):
    def get_all_emeasures_Controller(self):
        return self.get_all_emeasures()
    
    def get_one_emeasures_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Medidas", "Debe pasar total de valores correctamente.")
            return
        else: return self.get_one_emeasures(id)
    
    def insert_measures_Controller(self, measure_date, weight, waist, abdomen, hip, right_bicep, left_bicep, right_leg, left_leg, user_id):
        if measure_date == "":
            messagebox.showwarning("Advertencia Medidas", "Debe pasar total de valores correctamente.")
            return
        else: return self.insert_measures(measure_date, weight, waist, abdomen, hip, right_bicep, left_bicep, right_leg, left_leg, user_id)
    
    def update_measures_Controller(self, id, measure_date, weight, waist, abdomen, hip, right_bicep, left_bicep, right_leg, left_leg, user_id):
        if measure_date == "" or id == "":
            messagebox.showwarning("Advertencia Medidas", "Debe pasar total de valores correctamente.")
            return
        else: return self.update_measures(id, measure_date, weight, waist, abdomen, hip, right_bicep, left_bicep, right_leg, left_leg, user_id)
    
    def delete_measures_Controller(self, id):
        if id == "":
            messagebox.showwarning("Advertencia Medidas", "Debe pasar total de valores correctamente.")
            return
        else: return self.delete_measures(id)





































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# By zAxOz