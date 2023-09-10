import mariadb as mdb

class Conexion:
    def get_query(self, query : str, params = ()):
        try:
            conn = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="gymdb"
            )
            # Generando cursor
            cursor = conn.cursor()
            # Asignando query
            if params == ():
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            # obteniendo la data
            data = cursor.fetchall()

            return data
        except mdb.Error as e:
            return e
        finally:
            cursor.close()
            conn.close()
    
    def set_query(self, query : str, params = ()):
        try:
            conn = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="gymdb"
            )
            # Generando cursor
            cursor = conn.cursor()
            # Asignando query
            if params == ():
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            # obteniendo la data
            data = cursor.rowcount
            if data > 0:
                conn.commit()

            return data
        except mdb.Error as e:
            return e
        finally:
            cursor.close()
            conn.close()

class Usuario(Conexion):
    # Crear un usuario
    def create_user(self, number, address, name, status):
        insert_query = "INSERT INTO user (number, address, name, status) VALUES (%s, %s, %s, %s)"
        user_data = (number, address, name, status)

        row = self.set_query(insert_query, user_data)

        return row
    
    # Tomar data de todos los usuarios
    def get_all_users(self):
        select_query = "SELECT * FROM user"

        users = self.get_query(select_query)

        return users
    
    # Tomar data de 1 de los usuarios
    def get_one_users(self, id):
        select_query = "SELECT * FROM user WHERE id=%s"
        user_id = (id, )

        users = self.get_query(select_query, user_id)

        return users
    
    # Función para actualizar un usuario
    def update_user(self, id, number, address, name, status):
        update_query = "UPDATE user SET number=%s, address=%s, name=%s, status=%s WHERE id=%s"
        user_data = (number, address, name, status, id)

        row = self.set_query(update_query, user_data)

        return row

    # Función para eliminar un usuario
    def delete_user(self, id):
        delete_query = "DELETE FROM user WHERE id=%s"
        user_id = (id,)

        row = self.set_query(delete_query, user_id)

        return row
    
    # Funcion para retornar data del usuario y su set de ejercicios
    def get_one_user_pdf(self, id):
        query = """
            SELECT u.id, u.number, u.address, u.name, u.status, ek.routine, ek.exercise_start, ek.routine_plan_id
            FROM user u
            INNER JOIN exercise_kit ek ON u.id = ek.user_id
            WHERE
            u.id = %s
        """
        diet_id = (id, )

        fetch = self.get_query(query, diet_id)

        return fetch

class Dieta(Conexion):
    # Tomar valores de la tabla dieta
    def get_all_diets(self):
        query = """
            SELECT diet.id, diet.description, diet.status, user.name
            FROM diet
            INNER JOIN user ON diet.user_id = user.id
        """

        fetch = self.get_query(query)

        return fetch
    
    # Tomar valores de una fila de la tabla dieta
    def get_one_diets(self, id):
        query = """
            SELECT diet.id, diet.description, diet.status, user.name
            FROM diet
            INNER JOIN user ON diet.user_id = user.id
            WHERE
            diet.id = %s
        """
        diet_id = (id, )

        fetch = self.get_query(query, diet_id)

        return fetch

    # Función para insertar una nueva dieta
    def insert_diet(self, description, status, user_id):
        insert_query = "INSERT INTO diet (description, status, user_id) VALUES (%s, %s, %s)"
        diet_data = (description, status, user_id)

        row = self.set_query(insert_query, diet_data)

        return row

# Función para actualizar una dieta
    def update_diet(self, id, description, status, user_id):
        update_query = "UPDATE diet SET description=%s, status=%s, user_id=%s WHERE id=%s"
        diet_data = (description, status, user_id, id)

        row = self.set_query(update_query, diet_data)

        return row

    # Función para eliminar una dieta
    def delete_diet(self, id):
        delete_query = "DELETE FROM diet WHERE id=%s"
        diet_id = (id,)

        row = self.set_query(delete_query, diet_id)

        return row

class Pago(Conexion):
    # Función para obtener todos los pagos con información de usuario
    def get_all_payments_with_usernames(self):
        query = """
            SELECT tpay.id, tpay.amount, tpay.payment_credit, user.name, tpay.user_id
            FROM tpay
            INNER JOIN user ON tpay.user_id = user.id
        """

        fetch = self.get_query(query)

        return fetch

# Función para obtener uno de los pagos con información de usuario
    def get_one_payments_with_usernames(self, id):
        query = """
            SELECT tpay.id, tpay.amount, tpay.payment_credit, user.name
            FROM tpay
            INNER JOIN user ON tpay.user_id = user.id
            WHERE tpay.id = %s
        """
        payment_id = (id, )

        fetch = self.get_query(query, payment_id)

        return fetch

# Función para insertar un nuevo pago
    def insert_payment(self, amount, payment_credit, user_id):
        insert_query = "INSERT INTO tpay (amount, payment_credit, user_id) VALUES (%s, %s, %s)"
        payment_data = (amount, payment_credit, user_id)

        row = self.set_query(insert_query, payment_data)

        return row

# Función para actualizar un pago
    def update_payment(self, id, amount, payment_credit, user_id):
        update_query = "UPDATE tpay SET amount=%s, payment_credit=%s, user_id=%s WHERE id=%s"
        payment_data = (amount, payment_credit, user_id, id)

        row = self.set_query(update_query, payment_data)

        return row

# Función para eliminar un pago
    def delete_payment(self, id):
        delete_query = "DELETE FROM tpay WHERE id=%s"
        payment_id = (id,)

        row = self.set_query(delete_query, payment_id)

        return row

class Rol(Conexion):
    def get_all_roles(self):
        query = "SELECT * FROM rol"

        fetch = self.get_query(query)

        return fetch
# seleccion por id
    def get_one_roles(self, id):
        query = "SELECT * FROM rol WHERE id=%s"
        rol_id=(id, )

        fetch = self.get_query(query, rol_id)

        return fetch

# Función para insertar un nuevo rol
    def insert_role(self, name):
        insert_query = "INSERT INTO rol (name) VALUES (%s)"
        role_data = (name,)

        row = self.set_query(insert_query, role_data)

        return row

# Función para actualizar un rol
    def update_role(self, id, name):
        update_query = "UPDATE rol SET name=%s WHERE id=%s"
        role_data = (name, id)

        row = self.set_query(update_query, role_data)

        return row

# Función para eliminar un rol
    def delete_role(self, id):
        delete_query = "DELETE FROM rol WHERE id=%s"
        role_id = (id,)

        row = self.set_query(delete_query, role_id)

        return row

class Usuario_Login(Conexion):
    # Funcion para loguearse
    def login_user_acces(self, user, password):
        query = """SELECT ua.id, ua.user_name, ua.password, u.name, u.id, r.name, r.id
                FROM user_acces ua 
                INNER JOIN user u ON ua.user_id = u.id
                INNER JOIN rol r ON ua.rol_id = r.id
                WHERE ua.user_name = %s and ua.password = %s"""

        params = (user, password)
        fetch = self.get_query(query, params)

        return fetch

    # Función para obtener todos los accesos de usuarios con información de usuario y rol
    def get_all_user_access(self):
        query = """
            SELECT ua.id, ua.user_name, ua.password, u.name as user_name, r.name as rol_name, u.id as user_id, r.id as rol_id
            FROM user_acces ua
            INNER JOIN user u ON ua.user_id = u.id
            INNER JOIN rol r ON ua.rol_id = r.id
        """

        fetch = self.get_query(query)

        return fetch
    
    # Función para obtener uno de los accesos de usuarios con información de usuario y rol
    def get_one_user_access(self, id):
        query = """
            SELECT ua.id, ua.user_name, ua.password, u.name as user_name, r.name as rol_name
            FROM user_acces ua
            INNER JOIN user u ON ua.user_id = u.id
            INNER JOIN rol r ON ua.rol_id = r.id
            WHERE ua.id = %s
        """
        user_acces_id = (id, )

        fetch = self.get_query(query, user_acces_id)

        return fetch

# Función para insertar un nuevo acceso de usuario
    def insert_user_access(self, user_name, password, user_id, rol_id):
        insert_query = "INSERT INTO user_acces (user_name, password, user_id, rol_id) VALUES (%s, %s, %s, %s)"
        user_access_data = (user_name, password, user_id, rol_id)

        row = self.set_query(insert_query, user_access_data)

        return row

# Función para actualizar un acceso de usuario
    def update_user_access(self, id, user_name, password, user_id, rol_id):
        update_query = "UPDATE user_acces SET user_name=%s, password=%s, user_id=%s, rol_id=%s WHERE id=%s"
        user_access_data = (user_name, password, user_id, rol_id, id)

        row = self.set_query(update_query, user_access_data)

        return row

# Función para eliminar un acceso de usuario
    def delete_user_access(self, id):
        delete_query = "DELETE FROM user_acces WHERE id=%s"
        user_access_id = (id,)

        row = self.set_query(delete_query, user_access_id)

        return row

class Rutina(Conexion):
    # Función para obtener todos los planes de rutina
    def get_all_routine_plans(self):
        query = "SELECT * FROM routine_plan"

        fetch = self.get_query(query)

        return fetch
    
    # Función para obtener uno de los planes de rutina
    def get_one_routine_plans(self, id):
        query = """SELECT * FROM routine_plan
                WHERE id=%s"""
        routine_id = (id, )

        fetch = self.get_query(query, routine_id)
        
        return fetch

# Función para insertar un nuevo plan de rutina
    def insert_routine_plan(self, name, days_plan):
        insert_query = "INSERT INTO routine_plan (name, days_plan) VALUES (%s, %s)"
        routine_plan_data = (name, days_plan)

        row = self.set_query(insert_query, routine_plan_data)

        return row

# Función para actualizar un plan de rutina
    def update_routine_plan(self, id, name, days_plan):
        update_query = "UPDATE routine_plan SET name=%s, days_plan=%s WHERE id=%s"
        routine_plan_data = (name, days_plan, id)

        row = self.set_query(update_query, routine_plan_data)

        return row

# Función para eliminar un plan de rutina
    def delete_routine_plan(self, id):
        delete_query = "DELETE FROM routine_plan WHERE id=%s"
        routine_plan_id = (id,)

        row = self.set_query(delete_query, routine_plan_id)

        return row

class Set_Ejercicio(Conexion):
    # Función para obtener todos los kits de ejercicios con información de usuario y plan de rutina
    def get_all_exercise_kits(self):
        query = """
            SELECT ek.id, ek.routine, ek.exercise_start,
                    rp.name as routine_plan_name, rp.id as routine_plan_id, u.name as user_name, u.id as user_id, ek.user_id
            FROM exercise_kit ek
            INNER JOIN routine_plan rp ON ek.routine_plan_id = rp.id
            INNER JOIN user u ON ek.user_id = u.id
        """

        fetch = self.get_query(query)

        return fetch
    
    # Función para obtener uno de los kits de ejercicios con información de usuario y plan de rutina
    def get_one_exercise_kits(self, id):
        query = """
            SELECT ek.id, ek.routine, ek.exercise_start,
                    rp.name as routine_plan_name, u.name as user_name
            FROM exercise_kit ek
            INNER JOIN routine_plan rp ON ek.routine_plan_id = rp.id
            INNER JOIN user u ON ek.user_id = u.id
            WHERE ek.id = %s
        """
        exercise_kit_id = (id, )

        fetch = self.get_query(query, exercise_kit_id)

        return fetch

# Función para insertar un nuevo kit de ejercicios
    def insert_exercise_kit(self, routine, exercise_start, routine_plan_id, user_id):
        insert_query = "INSERT INTO exercise_kit (routine, exercise_start, routine_plan_id, user_id) VALUES (%s, %s, %s, %s)"
        exercise_kit_data = (routine, exercise_start, routine_plan_id, user_id)

        row = self.set_query(insert_query, exercise_kit_data)

        return row

# Función para actualizar un kit de ejercicios
    def update_exercise_kit(self, id, routine, exercise_start, routine_plan_id, user_id):
        update_query = "UPDATE exercise_kit SET routine=%s, exercise_start=%s, routine_plan_id=%s, user_id=%s WHERE id=%s"
        exercise_kit_data = (routine, exercise_start, routine_plan_id, user_id, id)

        row = self.set_query(update_query, exercise_kit_data)
        
        return row

# Función para eliminar un kit de ejercicios
    def delete_exercise_kit(self, id):
        delete_query = "DELETE FROM exercise_kit WHERE id=%s"
        exercise_kit_id = (id,)

        row = self.set_query(delete_query, exercise_kit_id)

        return row


# testeo de modelo

# modelo = Set_Ejercicio()
# start = modelo.get_all_exercise_kits()[0][5]
# print(start)
