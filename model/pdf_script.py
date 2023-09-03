from fpdf import FPDF

class PDFGenerator:
    def __init__(self, user_data, directory):
        self.pdf = FPDF()
        self.pdf.add_page()
        
        # Establecer fuentes y tamaños
        self.pdf.set_font("Arial", size=22)  # Encabezado
        self.pdf.cell(200, 20, "Gym Agua Limpia", ln=True, align="C")
        
        self.pdf.set_font("Arial", size=18)  # Contenido
        
        # Mostrar información del usuario

        self.pdf.ln(50)

        self.pdf.cell(200, 10, f"ID : {user_data['id']}", ln=True)
        self.pdf.cell(200, 10, f"Numero de telefono : {user_data['number']}", ln=True)
        self.pdf.cell(200, 10, f"Direccion : {user_data['address']}", ln=True)
        self.pdf.cell(200, 10, f"Nombre : {user_data['name']}", ln=True)
        self.pdf.cell(200, 10, f"Estatus : {user_data['status']}", ln=True)
        self.add_text(f"Rutina : {user_data['routine']}", max_width=150)
        self.pdf.cell(200, 10, f"Fecha de inicio : {user_data['exercise_start']}", ln=True)
        self.pdf.cell(200, 10, f"Plan de rutina : {user_data['routine_plan']}", ln=True)
        
        self.pdf.ln(50)

        # Pie de página
        self.pdf.set_font("Arial", size=22)  # Pie de página
        self.pdf.cell(200, 10, "Derechos reservados GYM", ln=True, align="C")

        # Guardar el PDF
        self.save_output_pdf(directory)
    
    def add_text(self, text, max_width):
        # Divide el texto en líneas más cortas que se ajusten dentro del ancho máximo
        lines = []
        line = ""
        words = text.split()
        for word in words:
            if self.pdf.get_string_width(line + word) <= max_width:
                line += word + " "
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)
        
        # Agrega las líneas de texto al PDF
        for line in lines:
            self.pdf.cell(0, 10, line, ln=True)
    
    def save_output_pdf(self, directory):
        self.pdf.output(directory)

class PDFGenerator_Pay:
    def __init__(self, user_pay : list, directory : str):
        self.pdf = FPDF()
        self.pdf.add_page()
        
        # Establecer fuentes y tamaños
        self.pdf.set_font("Arial", size=22)  # Encabezado
        self.pdf.cell(200, 20, "Gym Jerusalen", ln=True, align="C")
        
        self.pdf.set_font("Arial", size=18)  # Contenido
        
        # Mostrar información del usuario

        self.pdf.ln(50)

        self.pdf.set_font("Arial", "", 16)
        for row in user_pay:
            data = f"ID : {row[0]}, Monto : {row[1]}, Monto Abonado : {row[2]}, Usuario : {row[3]}"
            self.pdf.multi_cell(0, 10, data)
        self.pdf.ln()
        
        self.pdf.ln(100)

        # Pie de página
        self.pdf.set_font("Arial", size=22)  # Pie de página
        self.pdf.cell(200, 10, "Derechos reservados GYM", ln=True, align="C")

        # Guardar el PDF
        self.save_output_pdf(directory)
    
    def save_output_pdf(self, directory):
        self.pdf.output(directory)

# Datos de ejemplo (reemplaza con tus datos reales)
# user_data = {
#     "id": 1,
#     "number": "12345",
#     "address": "123 Main St",
#     "name": "John Doe",
#     "status": "Active",
#     "routine" : "Esta rutina es un texto vacio como prueba para la obtencion de un mejor pdf.",
#     "exercise_start" : "2022-05-22",
#     "routine_plan" : "medio"
# }

# Generar el PDF con los datos proporcionados
# pdf_generator = PDFGenerator(user_data)
