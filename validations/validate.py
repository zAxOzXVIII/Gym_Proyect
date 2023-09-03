

# Clase de Validaciones de formularios
class Validaciones:
    @staticmethod
    def validar_longitud(entry_text, max_length):
        if len(entry_text) <= int(max_length):
            return True
        else:
            return False

    @staticmethod
    def validar_numero(entry_text, max_length):
        if Validaciones.validar_longitud(entry_text, max_length) and entry_text.isdigit():
            return True
        else:
            return False

    @staticmethod
    def validar_numero_flotante(entry_text):
        if entry_text == "":
            return True  # Permitir borrar el contenido del Entry
        try:
            float(entry_text)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_entry(entry_text, max_length, validacion_func):
        if validacion_func(entry_text, max_length) or entry_text == "":
            return True
        else:
            return False
    
    @staticmethod
    def clean_window(window):
        # Destruir los widgets del contenido actual
        for widget in window.winfo_children():
            widget.destroy()

    @staticmethod
    def back_window(destination_window_func, window_root):
        # Clean window
        Validaciones.clean_window(window_root)

        # Execute destination function
        destination_window_func()
    
    @staticmethod
    def verify_treeview(treeview):
        seleccion = treeview.selection()
        if seleccion:
            fila_seleccionada = seleccion[0]  # Tomar el primer índice de la selección
            valores_fila = treeview.item(fila_seleccionada, "values")
            return valores_fila
        else:
            return