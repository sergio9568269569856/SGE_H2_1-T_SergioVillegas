import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Conexión a la base de datos
def conectar_bd():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="campusfp",
        database="ENCUESTAS"
    )
    return conn

# Función para generar gráficos de barras y circular
# Función para generar gráfico circular
def mostrar_grafico_circular():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT Sexo, COUNT(*) FROM ENCUESTA GROUP BY Sexo")
    registros = cursor.fetchall()
    conn.close()

    sexos = [registro[0] for registro in registros]
    conteos = [registro[1] for registro in registros]

    # Crear una nueva ventana para el gráfico circular
    ventana_circular = tk.Toplevel(ventana)
    ventana_circular.title("Gráfico Circular")
    ventana_circular.geometry("800x600")

    # Gráfico circular (pie chart) con nuevos colores
    fig, ax = plt.subplots()
    ax.pie(conteos, labels=sexos, autopct='%1.1f%%', colors=['#ff6347', '#32cd32', '#1e90ff'])
    ax.set_title('Distribución por Sexo')

    # Mostrar el gráfico en la nueva ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_circular)
    canvas.draw()
    canvas.get_tk_widget().pack()



def mostrar_grafico_barras():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT edad, BebidasSemana FROM ENCUESTA")
    registros = cursor.fetchall()
    conn.close()

    edades = [registro[0] for registro in registros]
    bebidas = [registro[1] for registro in registros]

    # Crear una nueva ventana para el gráfico
    ventana_barras = tk.Toplevel(ventana)
    ventana_barras.title("Gráfico de Barras")
    ventana_barras.geometry("800x600")

    # Crear el gráfico (barras o líneas)
    fig, ax = plt.subplots()

    # Si quieres un gráfico de barras, usa este código
    ax.bar(edades, bebidas, color='orange')  # Cambié el color a naranja

    # Configuración de etiquetas y título
    ax.set_xlabel('Edad')
    ax.set_ylabel('Bebidas por Semana')
    ax.set_title('Consumo de Alcohol por Edad')

    # Mostrar el gráfico en la nueva ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_barras)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Función para crear registros
def crear_encuesta():
    # Obtenemos los datos de los campos de entrada
    id_encuesta = id_entry.get()
    edad = edad_entry.get()
    sexo = sexo_entry.get()
    bebidas_semana = bebidas_semana_entry.get()
    cervezas_semana = cervezas_semana_entry.get()
    bebidas_fin_semana = bebidas_fin_semana_entry.get()
    bebidas_destiladas_semana = bebidas_destiladas_semana_entry.get()
    vinos_semana = vinos_semana_entry.get()
    perdidas_control = perdidas_control_entry.get()
    diversion = diversion_entry.get()
    problemas_digestivos = problemas_digestivos_entry.get()
    tension_alta = tension_alta_entry.get()
    dolor_cabeza = dolor_cabeza_entry.get()

    # Validación de campos obligatorios
    if not id_encuesta or not edad or not sexo:
        messagebox.showerror("Error", "Los campos ID, Edad y Sexo son obligatorios.")
        return

    # Conexión a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()

    # Insertamos los valores en la tabla ENCUESTA
    query = """
        INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion, problemas_digestivos, tension_alta, dolor_cabeza))
    conn.commit()
    conn.close()

    # Mostramos un mensaje de éxito
    messagebox.showinfo("Éxito", "Encuesta creada correctamente.")

    # Limpiar los campos de entrada después de insertar los datos
    limpiar_campos()

# Función para limpiar los campos de entrada
def limpiar_campos():
    id_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    sexo_entry.delete(0, tk.END)
    bebidas_semana_entry.delete(0, tk.END)
    cervezas_semana_entry.delete(0, tk.END)
    bebidas_fin_semana_entry.delete(0, tk.END)
    bebidas_destiladas_semana_entry.delete(0, tk.END)
    vinos_semana_entry.delete(0, tk.END)
    perdidas_control_entry.delete(0, tk.END)
    diversion_entry.delete(0, tk.END)
    problemas_digestivos_entry.delete(0, tk.END)
    tension_alta_entry.delete(0, tk.END)
    dolor_cabeza_entry.delete(0, tk.END)

# Función para mostrar encuestas con filtros
def mostrar_encuestas():
    # Obtener los filtros seleccionados
    id_filtro = id_entry.get()
    edad_filtro = edad_entry.get()
    sexo_filtro = sexo_entry.get()
    bebidas_semana_filtro = bebidas_semana_entry.get()
    cervezas_semana_filtro = cervezas_semana_entry.get()
    bebidas_fin_semana_filtro = bebidas_fin_semana_entry.get()
    bebidas_destiladas_semana_filtro = bebidas_destiladas_semana_entry.get()
    vinos_semana_filtro = vinos_semana_entry.get()
    perdidas_control_filtro = perdidas_control_entry.get()
    diversion_filtro = diversion_entry.get()
    problemas_digestivos_filtro = problemas_digestivos_entry.get()
    tension_alta_filtro = tension_alta_entry.get()
    dolor_cabeza_filtro = dolor_cabeza_entry.get()

    conn = conectar_bd()
    cursor = conn.cursor()

    # Crear la consulta base
    query = "SELECT * FROM ENCUESTA WHERE 1=1"
    params = []

    # Agregar filtros a la consulta según los valores de los Entry
    if id_filtro:
        query += " AND idEncuesta = %s"
        params.append(id_filtro)
    if edad_filtro:
        query += " AND edad = %s"
        params.append(edad_filtro)
    if sexo_filtro:
        query += " AND Sexo = %s"
        params.append(sexo_filtro)
    if bebidas_semana_filtro:
        query += " AND BebidasSemana = %s"
        params.append(bebidas_semana_filtro)
    if cervezas_semana_filtro:
        query += " AND CervezasSemana = %s"
        params.append(cervezas_semana_filtro)
    if bebidas_fin_semana_filtro:
        query += " AND BebidasFinSemana = %s"
        params.append(bebidas_fin_semana_filtro)
    if bebidas_destiladas_semana_filtro:
        query += " AND BebidasDestiladasSemana = %s"
        params.append(bebidas_destiladas_semana_filtro)
    if vinos_semana_filtro:
        query += " AND VinosSemana = %s"
        params.append(vinos_semana_filtro)
    if perdidas_control_filtro:
        query += " AND PerdidasControl = %s"
        params.append(perdidas_control_filtro)
    if diversion_filtro:
        query += " AND DiversionDependenciaAlcohol = %s"
        params.append(diversion_filtro)
    if problemas_digestivos_filtro:
        query += " AND ProblemasDigestivos = %s"
        params.append(problemas_digestivos_filtro)
    if tension_alta_filtro:
        query += " AND TensionAlta = %s"
        params.append(tension_alta_filtro)
    if dolor_cabeza_filtro:
        query += " AND DolorCabeza = %s"
        params.append(dolor_cabeza_filtro)

    cursor.execute(query, tuple(params))
    registros = cursor.fetchall()
    conn.close()

    # Limpiar la vista anterior
    for item in treeview.get_children():
        treeview.delete(item)

    # Mostrar los registros filtrados
    for row in registros:
        treeview.insert("", "end", values=row)

# Función para generar gráficos
def generar_grafico():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT edad, BebidasSemana FROM ENCUESTA")
    registros = cursor.fetchall()
    conn.close()

    edades = [registro[0] for registro in registros]
    bebidas = [registro[1] for registro in registros]

    # Limitar los registros para no hacer el gráfico demasiado grande
    registros = registros[:10]  # Mostrar solo los primeros 10 registros

    # Gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(edades, bebidas)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Bebidas por Semana')
    ax.set_title('Consumo de Alcohol por Edad')

    # Mostrar en la interfaz
    canvas = FigureCanvasTkAgg(fig, master=ventana)  # ventana es la ventana Tkinter
    canvas.draw()
    canvas.get_tk_widget().pack()

# Función para eliminar una encuesta por ID
def eliminar_encuesta():
    # Crear una nueva ventana para ingresar el ID
    eliminar_ventana = tk.Toplevel(ventana)
    eliminar_ventana.title("Eliminar Encuesta")
    eliminar_ventana.geometry("300x150")

    id_label = tk.Label(eliminar_ventana, text="Ingrese el ID de la Encuesta a eliminar:")
    id_label.pack(pady=10)

    id_entry_eliminar = tk.Entry(eliminar_ventana)
    id_entry_eliminar.pack(pady=5)

    def eliminar():
        id_encuesta = id_entry_eliminar.get()

        if not id_encuesta:
            messagebox.showerror("Error", "Debe ingresar un ID válido.")
            return

        # Conexión a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Ejecutar la consulta para eliminar el registro con el ID dado
        query = "DELETE FROM ENCUESTA WHERE idEncuesta = %s"
        cursor.execute(query, (id_encuesta,))
        conn.commit()

        # Verificamos si se eliminó alguna fila
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
        else:
            messagebox.showerror("Error", "No se encontró ninguna encuesta con ese ID.")

        conn.close()
        eliminar_ventana.destroy()

    # Botón para eliminar la encuesta
    eliminar_button = tk.Button(eliminar_ventana, text="Eliminar", command=eliminar)
    eliminar_button.pack(pady=10)

# Función para actualizar una encuesta
def actualizar_encuesta():
    # Crear una nueva ventana para ingresar el ID
    actualizar_ventana = tk.Toplevel(ventana)
    actualizar_ventana.title("Actualizar Encuesta")
    actualizar_ventana.geometry("300x400")

    id_label = tk.Label(actualizar_ventana, text="Ingrese el ID de la Encuesta a actualizar:")
    id_label.pack(pady=10)

    id_entry_actualizar = tk.Entry(actualizar_ventana)
    id_entry_actualizar.pack(pady=5)

    # Función para actualizar una encuesta
def actualizar_encuesta():
    # Crear una nueva ventana para ingresar el ID
    actualizar_ventana = tk.Toplevel(ventana)
    actualizar_ventana.title("Actualizar Encuesta")
    actualizar_ventana.geometry("400x900")

    id_label = tk.Label(actualizar_ventana, text="Ingrese el ID de la Encuesta a actualizar:")
    id_label.pack(pady=10)

    id_entry_actualizar = tk.Entry(actualizar_ventana)
    id_entry_actualizar.pack(pady=5)

    def actualizar():
        id_encuesta = id_entry_actualizar.get()

        if not id_encuesta:
            messagebox.showerror("Error", "Debe ingresar un ID válido.")
            return

        # Conexión a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Verificamos si el ID existe
        query = "SELECT * FROM ENCUESTA WHERE idEncuesta = %s"
        cursor.execute(query, (id_encuesta,))
        encuesta = cursor.fetchone()

        if not encuesta:
            messagebox.showerror("Error", "No se encontró ninguna encuesta con ese ID.")
            conn.close()
            return

        # Si el ID existe, mostramos los datos en los campos correspondientes
        edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion, problemas_digestivos, tension_alta, dolor_cabeza = encuesta[1:]

        # Crear campos para modificar los datos
        edad_label = tk.Label(actualizar_ventana, text="Edad")
        edad_label.pack()
        edad_entry = tk.Entry(actualizar_ventana)
        edad_entry.insert(0, edad)
        edad_entry.pack(pady=5)

        sexo_label = tk.Label(actualizar_ventana, text="Sexo")
        sexo_label.pack()
        sexo_entry = tk.Entry(actualizar_ventana)
        sexo_entry.insert(0, sexo)
        sexo_entry.pack(pady=5)

        bebidas_semana_label = tk.Label(actualizar_ventana, text="Bebidas por Semana")
        bebidas_semana_label.pack()
        bebidas_semana_entry = tk.Entry(actualizar_ventana)
        bebidas_semana_entry.insert(0, bebidas_semana)
        bebidas_semana_entry.pack(pady=5)

        cervezas_semana_label = tk.Label(actualizar_ventana, text="Cervezas por Semana")
        cervezas_semana_label.pack()
        cervezas_semana_entry = tk.Entry(actualizar_ventana)
        cervezas_semana_entry.insert(0, cervezas_semana)
        cervezas_semana_entry.pack(pady=5)

        bebidas_fin_semana_label = tk.Label(actualizar_ventana, text="Bebidas en Fin de Semana")
        bebidas_fin_semana_label.pack()
        bebidas_fin_semana_entry = tk.Entry(actualizar_ventana)
        bebidas_fin_semana_entry.insert(0, bebidas_fin_semana)
        bebidas_fin_semana_entry.pack(pady=5)

        bebidas_destiladas_semana_label = tk.Label(actualizar_ventana, text="Bebidas Destiladas por Semana")
        bebidas_destiladas_semana_label.pack()
        bebidas_destiladas_semana_entry = tk.Entry(actualizar_ventana)
        bebidas_destiladas_semana_entry.insert(0, bebidas_destiladas_semana)
        bebidas_destiladas_semana_entry.pack(pady=5)

        vinos_semana_label = tk.Label(actualizar_ventana, text="Vinos por Semana")
        vinos_semana_label.pack()
        vinos_semana_entry = tk.Entry(actualizar_ventana)
        vinos_semana_entry.insert(0, vinos_semana)
        vinos_semana_entry.pack(pady=5)

        perdidas_control_label = tk.Label(actualizar_ventana, text="Pérdidas de Control")
        perdidas_control_label.pack()
        perdidas_control_entry = tk.Entry(actualizar_ventana)
        perdidas_control_entry.insert(0, perdidas_control)
        perdidas_control_entry.pack(pady=5)

        diversion_label = tk.Label(actualizar_ventana, text="Diversión y Dependencia")
        diversion_label.pack()
        diversion_entry = tk.Entry(actualizar_ventana)
        diversion_entry.insert(0, diversion)
        diversion_entry.pack(pady=5)

        problemas_digestivos_label = tk.Label(actualizar_ventana, text="Problemas Digestivos")
        problemas_digestivos_label.pack()
        problemas_digestivos_entry = tk.Entry(actualizar_ventana)
        problemas_digestivos_entry.insert(0, problemas_digestivos)
        problemas_digestivos_entry.pack(pady=5)

        tension_alta_label = tk.Label(actualizar_ventana, text="Tensión Alta")
        tension_alta_label.pack()
        tension_alta_entry = tk.Entry(actualizar_ventana)
        tension_alta_entry.insert(0, tension_alta)
        tension_alta_entry.pack(pady=5)

        dolor_cabeza_label = tk.Label(actualizar_ventana, text="Dolor de Cabeza")
        dolor_cabeza_label.pack()
        dolor_cabeza_entry = tk.Entry(actualizar_ventana)
        dolor_cabeza_entry.insert(0, dolor_cabeza)
        dolor_cabeza_entry.pack(pady=5)

        def guardar():
            # Recoger los nuevos valores
            edad_nueva = edad_entry.get()
            sexo_nuevo = sexo_entry.get()
            bebidas_semana_nuevo = bebidas_semana_entry.get()
            cervezas_semana_nuevo = cervezas_semana_entry.get()
            bebidas_fin_semana_nuevo = bebidas_fin_semana_entry.get()
            bebidas_destiladas_semana_nuevo = bebidas_destiladas_semana_entry.get()
            vinos_semana_nuevo = vinos_semana_entry.get()
            perdidas_control_nuevo = perdidas_control_entry.get()
            diversion_nuevo = diversion_entry.get()
            problemas_digestivos_nuevo = problemas_digestivos_entry.get()
            tension_alta_nuevo = tension_alta_entry.get()
            dolor_cabeza_nuevo = dolor_cabeza_entry.get()

            # Actualizar en la base de datos
            query = """UPDATE ENCUESTA SET 
                edad = %s, 
                Sexo = %s, 
                BebidasSemana = %s, 
                CervezasSemana = %s, 
                BebidasFinSemana = %s, 
                BebidasDestiladasSemana = %s, 
                VinosSemana = %s, 
                PerdidasControl = %s, 
                DiversionDependenciaAlcohol = %s, 
                ProblemasDigestivos = %s, 
                TensionAlta = %s, 
                DolorCabeza = %s 
                WHERE idEncuesta = %s
            """
            cursor.execute(query, (
                edad_nueva, sexo_nuevo, bebidas_semana_nuevo, cervezas_semana_nuevo,
                bebidas_fin_semana_nuevo, bebidas_destiladas_semana_nuevo, vinos_semana_nuevo,
                perdidas_control_nuevo, diversion_nuevo, problemas_digestivos_nuevo,
                tension_alta_nuevo, dolor_cabeza_nuevo, id_encuesta
            ))
            conn.commit()

            messagebox.showinfo("Éxito", "Encuesta actualizada correctamente.")
            conn.close()
            actualizar_ventana.destroy()

        # Botón para guardar los cambios
        guardar_button = tk.Button(actualizar_ventana, text="Guardar", command=guardar)
        guardar_button.pack(pady=20)

    # Botón para buscar y actualizar la encuesta
    actualizar_button = tk.Button(actualizar_ventana, text="Buscar Encuesta", command=actualizar)
    actualizar_button.pack(pady=10)

# Función para exportar a Excel
# Función para exportar a Excel
def exportar_a_excel(filtro):
    conn = conectar_bd()
    cursor = conn.cursor()

    # Crear la consulta SQL según el filtro
    query = "SELECT * FROM ENCUESTA WHERE 1=1"
    params = []

    # Filtros según el criterio
    if filtro.get("id"):
        query += " AND idEncuesta = %s"
        params.append(filtro["id"])
    if filtro.get("edad"):
        query += " AND edad = %s"
        params.append(filtro["edad"])
    if filtro.get("sexo"):
        query += " AND Sexo = %s"
        params.append(filtro["sexo"])

    cursor.execute(query, tuple(params))
    registros = cursor.fetchall()
    conn.close()

    # Crear un DataFrame de pandas para exportar
    columnas = ["idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana",
                "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana",
                "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos",
                "TensionAlta", "DolorCabeza"]
    df = pd.DataFrame(registros, columns=columnas)

    # Guardar el archivo Excel
    df.to_excel("encuestas_exportadas.xlsx", index=False)

    messagebox.showinfo("Éxito", "Los datos fueron exportados a Excel correctamente.")

# Función para exportar los datos a PDF
def exportar_a_pdf(filtro):
    conn = conectar_bd()
    cursor = conn.cursor()

    # Crear la consulta SQL según el filtro
    query = "SELECT * FROM ENCUESTA WHERE 1=1"
    params = []

    if filtro.get("id"):
        query += " AND idEncuesta = %s"
        params.append(filtro["id"])
    if filtro.get("edad"):
        query += " AND edad = %s"
        params.append(filtro["edad"])
    if filtro.get("sexo"):
        query += " AND Sexo = %s"
        params.append(filtro["sexo"])

    cursor.execute(query, tuple(params))
    registros = cursor.fetchall()
    conn.close()

    # Crear un PDF
    c = canvas.Canvas("encuestas_exportadas.pdf", pagesize=letter)
    width, height = letter

    # Escribir en el PDF
    c.drawString(30, height - 30, "Encuestas Exportadas:")
    y_position = height - 50

    # Encabezado de la tabla
    columnas = ["idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana",
                "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana",
                "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos",
                "TensionAlta", "DolorCabeza"]

    x_offsets = [30, 80, 130, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630]

    for i, col in enumerate(columnas):
        c.drawString(x_offsets[i], y_position, col)
    y_position -= 20

    # Datos
    for row in registros:
        for i, dato in enumerate(row):
            c.drawString(x_offsets[i], y_position, str(dato))
        y_position -= 20

        if y_position < 40:  # Si llega al final de la página, crear nueva página
            c.showPage()
            y_position = height - 50
            for i, col in enumerate(columnas):
                c.drawString(x_offsets[i], y_position, col)
            y_position -= 20

    c.save()

    messagebox.showinfo("Éxito", "Los datos fueron exportados a PDF correctamente.")

# Crear la ventana de exportación
def ventana_exportar(filtro):
    exportar_ventana = tk.Toplevel(ventana)
    exportar_ventana.title("Exportar Encuestas")
    exportar_ventana.geometry("300x150")

    # Botón para exportar a Excel
    excel_button = tk.Button(exportar_ventana, text="Exportar a Excel", command=lambda: exportar_a_excel(filtro))
    excel_button.pack(pady=10)

    # Botón para exportar a PDF
    pdf_button = tk.Button(exportar_ventana, text="Exportar a PDF", command=lambda: exportar_a_pdf(filtro))
    pdf_button.pack(pady=10)

# Función para mostrar la ventana de exportación
def mostrar_exportar():
    filtro = {
        "id": id_entry.get(),
        "edad": edad_entry.get(),
        "sexo": sexo_entry.get(),
    }
    ventana_exportar(filtro)

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Encuestas")
ventana.geometry("1220x600")

# Entradas y etiquetas para los datos
id_label = tk.Label(ventana, text="ID Encuesta")
id_label.grid(row=0, column=0, padx=10, pady=5)
id_entry = tk.Entry(ventana)
id_entry.grid(row=0, column=1, padx=10, pady=5)

edad_label = tk.Label(ventana, text="Edad")
edad_label.grid(row=1, column=0, padx=10, pady=5)
edad_entry = tk.Entry(ventana)
edad_entry.grid(row=1, column=1, padx=10, pady=5)

sexo_label = tk.Label(ventana, text="Sexo")
sexo_label.grid(row=1, column=2, padx=10, pady=5)
sexo_entry = tk.Entry(ventana)
sexo_entry.grid(row=1, column=3, padx=10, pady=5)


bebidas_semana_label = tk.Label(ventana, text="Bebidas por Semana")
bebidas_semana_label.grid(row=2, column=0, padx=10, pady=5)
bebidas_semana_entry = tk.Entry(ventana)
bebidas_semana_entry.grid(row=2, column=1, padx=10, pady=5)

cervezas_semana_label = tk.Label(ventana, text="Cervezas por Semana")
cervezas_semana_label.grid(row=2, column=2, padx=10, pady=5)
cervezas_semana_entry = tk.Entry(ventana)
cervezas_semana_entry.grid(row=2, column=3, padx=10, pady=5)

bebidas_fin_semana_label = tk.Label(ventana, text="Bebidas Fin de Semana")
bebidas_fin_semana_label.grid(row=3, column=0, padx=10, pady=5)
bebidas_fin_semana_entry = tk.Entry(ventana)
bebidas_fin_semana_entry.grid(row=3, column=1, padx=10, pady=5)

bebidas_destiladas_semana_label = tk.Label(ventana, text="Bebidas Destiladas por Semana")
bebidas_destiladas_semana_label.grid(row=3, column=2, padx=10, pady=5)
bebidas_destiladas_semana_entry = tk.Entry(ventana)
bebidas_destiladas_semana_entry.grid(row=3, column=3, padx=10, pady=5)

vinos_semana_label = tk.Label(ventana, text="Vinos por Semana")
vinos_semana_label.grid(row=4, column=0, padx=10, pady=5)
vinos_semana_entry = tk.Entry(ventana)
vinos_semana_entry.grid(row=4, column=1, padx=10, pady=5)

perdidas_control_label = tk.Label(ventana, text="Pérdidas de Control")
perdidas_control_label.grid(row=4, column=2, padx=10, pady=5)
perdidas_control_entry = tk.Entry(ventana)
perdidas_control_entry.grid(row=4, column=3, padx=10, pady=5)

diversion_label = tk.Label(ventana, text="Diversión / Dependencia")
diversion_label.grid(row=5, column=0, padx=10, pady=5)
diversion_entry = tk.Entry(ventana)
diversion_entry.grid(row=5, column=1, padx=10, pady=5)

problemas_digestivos_label = tk.Label(ventana, text="Problemas Digestivos")
problemas_digestivos_label.grid(row=5, column=2, padx=10, pady=5)
problemas_digestivos_entry = tk.Entry(ventana)
problemas_digestivos_entry.grid(row=5, column=3, padx=10, pady=5)

tension_alta_label = tk.Label(ventana, text="Tensión Alta")
tension_alta_label.grid(row=6, column=0, padx=10, pady=5)
tension_alta_entry = tk.Entry(ventana)
tension_alta_entry.grid(row=6, column=1, padx=10, pady=5)

dolor_cabeza_label = tk.Label(ventana, text="Dolor de Cabeza")
dolor_cabeza_label.grid(row=6, column=2, padx=10, pady=5)
dolor_cabeza_entry = tk.Entry(ventana)
dolor_cabeza_entry.grid(row=6, column=3, padx=10, pady=5)

# Botones para insertar, mostrar y eliminar encuestas
insertar_button = tk.Button(ventana, text="Insertar Encuesta", command=crear_encuesta)
insertar_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

mostrar_button = tk.Button(ventana, text="Mostrar Encuestas", command=mostrar_encuestas)
mostrar_button.grid(row=7, column=1, columnspan=2, padx=10, pady=5)

eliminar_button = tk.Button(ventana, text="Eliminar Encuesta", command=eliminar_encuesta)
eliminar_button.grid(row=7, column=2, columnspan=2, padx=10, pady=5)

actualizar_button = tk.Button(ventana, text="Actualizar Encuesta", command=actualizar_encuesta)
actualizar_button.grid(row=7, column=3, columnspan=2, padx=10, pady=5)

boton_grafico_barras = tk.Button(ventana, text="Mostrar Gráfico de Barras", command=mostrar_grafico_barras)
boton_grafico_barras.grid(row=10, column=0, columnspan=2, pady=20)

boton_grafico_circular = tk.Button(ventana, text="Mostrar Gráfico Circular", command=mostrar_grafico_circular)
boton_grafico_circular.grid(row=10, column=2, columnspan=2, pady=20)

exportar_button = tk.Button(ventana, text="Exportar Encuestas", command=mostrar_exportar)
exportar_button.grid(row=10, column=1, columnspan=2, pady=20)


# Treeview para mostrar registros
columns = ("idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza")
treeview = ttk.Treeview(ventana, columns=columns, show="headings")
treeview.grid(row=9, column=0, columnspan=4, padx=10, pady=5)

treeview.heading("idEncuesta", text="ID")
treeview.heading("edad", text="Edad")
treeview.heading("Sexo", text="Sexo")
treeview.heading("BebidasSemana", text="Bebidas /S")
treeview.heading("CervezasSemana", text="Cervezas /S")
treeview.heading("BebidasFinSemana", text="Bebidas /FS")
treeview.heading("BebidasDestiladasSemana", text="Bebidas Destiladas")
treeview.heading("VinosSemana", text="Vinos /S")
treeview.heading("PerdidasControl", text="Pérdidas de Control")
treeview.heading("DiversionDependenciaAlcohol", text="Diversión/Dependencia")
treeview.heading("ProblemasDigestivos", text="Problemas Digestivos")
treeview.heading("TensionAlta", text="Tensión Alta")
treeview.heading("DolorCabeza", text="Dolor de Cabeza")

# Ajuste del ancho de las columnas
column_widths = {
    "idEncuesta": 80, "edad": 50, "Sexo": 60, "BebidasSemana": 90, "CervezasSemana": 90,
    "BebidasFinSemana": 120, "BebidasDestiladasSemana": 120, "VinosSemana": 90, "PerdidasControl": 100,
    "DiversionDependenciaAlcohol": 100, "ProblemasDigestivos": 120, "TensionAlta": 80, "DolorCabeza": 100
}

for col, width in column_widths.items():
    treeview.column(col, width=width)

# Ejecutar la ventana
ventana.mainloop()