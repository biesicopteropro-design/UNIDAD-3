#GARCIA FLORES JUAN PABLO
#PROG 3 
#PROYECTO FINAL PUNTO DE VENTA DE ROPA
#cbtis89

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os

# =====================================================
#  FUNCIÓN MOSTRAR TICKET
# =====================================================
def mostrar_ticket(producto, precio, cantidad, total):
    ticket = tk.Toplevel()
    ticket.title("Ticket de Venta")
    ticket.geometry("300x350")
    ticket.resizable(False, False)

    fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

    texto = (
        " *** PUNTO DE VENTA ***\n"
        "--------------------------------------\n"
        f"Fecha: {fecha_hora}\n"
        "--------------------------------------\n"
        f"Producto: {producto}\n"
        f"Precio: ${precio}\n"
        f"Cantidad: {cantidad}\n"
        "--------------------------------------\n"
        f"TOTAL: ${total}\n"
        "--------------------------------------\n"
        " ¡GRACIAS POR SU COMPRA!\n"
    )

    lbl_ticket = tk.Label(ticket, text=texto, justify="left", font=("Consolas", 11))
    lbl_ticket.pack(pady=15)

    btn_cerrar = ttk.Button(ticket, text="Cerrar", command=ticket.destroy)
    btn_cerrar.pack(pady=10)

# =====================================================
#  REGISTRO DE PRODUCTOS
# =====================================================
def abrir_registro_productos():    
    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("400x400")
    reg.resizable(False, False)

    # --- Etiquetas y campos ---
    lbl_id = tk.Label(reg, text="ID del Producto:", font=("Arial", 12))
    lbl_id.pack(pady=5)
    txt_id = tk.Entry(reg, font=("Arial", 12))
    txt_id.pack(pady=5)

    lbl_desc = tk.Label(reg, text="Descripción:", font=("Arial", 12))
    lbl_desc.pack(pady=5)
    txt_desc = tk.Entry(reg, font=("Arial", 12))
    txt_desc.pack(pady=5)

    lbl_precio = tk.Label(reg, text="Precio:", font=("Arial", 12))
    lbl_precio.pack(pady=5)
    txt_precio = tk.Entry(reg, font=("Arial", 12))
    txt_precio.pack(pady=5)

    lbl_categoria = tk.Label(reg, text="Categoría:", font=("Arial", 12))
    lbl_categoria.pack(pady=5)
    txt_categoria = tk.Entry(reg, font=("Arial", 12))
    txt_categoria.pack(pady=5)

    # --- Función guardar ---
    def guardar_producto():
        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning("Campos Vacíos", "Complete todos los campos.")
            return

        try:
            float(precio)
        except:
            messagebox.showerror("Error", "El precio debe ser un número.")
            return

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as file:
            file.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")

        messagebox.showinfo("Guardado", "Producto registrado correctamente.")

        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    btn_guardar = tk.Button(reg, text="Guardar Producto", command=guardar_producto)
    btn_guardar.pack(pady=20)

# =====================================================
#  REGISTRO DE VENTAS
# =====================================================
def abrir_registro_ventas():
    vent = tk.Toplevel()
    vent.title("Registro de Ventas")
    vent.geometry("400x350")
    vent.resizable(False, False)

    lbl_prod = tk.Label(vent, text="Producto:", font=("Arial", 12))
    lbl_prod.pack(pady=5)
    txt_prod = tk.Entry(vent, font=("Arial", 12))
    txt_prod.pack(pady=5)

    lbl_precio = tk.Label(vent, text="Precio:", font=("Arial", 12))
    lbl_precio.pack(pady=5)
    txt_precio = tk.Entry(vent, font=("Arial", 12))
    txt_precio.pack(pady=5)

    lbl_cant = tk.Label(vent, text="Cantidad:", font=("Arial", 12))
    lbl_cant.pack(pady=5)
    txt_cant = tk.Entry(vent, font=("Arial", 12))
    txt_cant.pack(pady=5)

    def registrar_venta():
        prod = txt_prod.get().strip()
        precio = txt_precio.get().strip()
        cant = txt_cant.get().strip()

        if prod == "" or precio == "" or cant == "":
            messagebox.showwarning("Campos Vacíos", "Llene todos los campos.")
            return

        try:
            precio = float(precio)
            cant = int(cant)
        except:
            messagebox.showerror("Error", "Precio debe ser número y cantidad entero.")
            return

        total = precio * cant

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "ventas.txt")

        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"{prod}|{precio}|{cant}|{total}\n")

        # 🔹 MENSAJE SOLICITADO
        messagebox.showinfo("Venta Registrada", "La venta se registró correctamente.")

        # 🔹 MOSTRAR TICKET
        mostrar_ticket(prod, precio, cant, total)

        txt_prod.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_cant.delete(0, tk.END)

    btn_guardar = ttk.Button(vent, text="Registrar Venta", command=registrar_venta)
    btn_guardar.pack(pady=20)

# =====================================================
#  CONTENIDO EXTRA
# =====================================================
def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# =====================================================
#  VENTANA PRINCIPAL
# =====================================================
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("500x600")
ventana.resizable(False, False)

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "ventas2025.png"))
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo del sistema)", font=("Arial", 14))
    lbl_sin_logo.pack(pady=40)

estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 12), padding=10)

btn_reg_prod = ttk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(ventana, text="Reportes", command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(ventana, text="Acerca de", command=abrir_acerca_de)
btn_acerca.pack(pady=10)

ventana.mainloop()
