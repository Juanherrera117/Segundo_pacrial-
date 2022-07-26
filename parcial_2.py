import tkinter as tk
from tkinter import messagebox, Canvas, Frame,Label,BOTH, Entry, Button


# ----------------------------------
# VARIABLES GLOBALES
# ----------------------------------
BASE = 460
ALTURA = 380

#-----------------------
# VENTANA PRINCIPAL
#-----------------------
ventana_principal = tk.Tk()
ventana_principal.title("Plano")
ventana_principal.geometry("500x730")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="dark red")


# ----------------------------------
# FRAME DE GRAFICACIÓN
# ----------------------------------
frame_graficaion = Frame(ventana_principal)
frame_graficaion.config(bg = "white", width = 480, height = 400)
frame_graficaion.pack(fill = BOTH, padx = 10, pady = 10)

# Creacion del canva
c = Canvas(frame_graficaion, width = BASE, height = ALTURA)
c.place(x = 10,y = 10)

#------------------------
# FRAME OPERACIONES
#------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white", width = 480, height = 400)
frame_operaciones.pack(fill = BOTH, padx = 10, pady = 10)

graficar= tk.Button(frame_operaciones, text = "Graficar")
graficar.config(width = 15,height = 4)
graficar.place(x = 50,y = 160)

pendiente = tk.Button(frame_operaciones, text = "Pendiente")
pendiente.config(width = 15,height = 4)
pendiente.place(x = 250,y = 160)

# Líneas rectas
linea3 = c.create_line(BASE/2, 0, BASE/2, ALTURA/2, fill = "black")
linea4 = c.create_line(BASE, ALTURA/2, BASE/2, ALTURA/2, fill = "black")
linea5 = c.create_line(BASE/2, ALTURA, BASE/2, ALTURA/2, fill = "black")
linea6 = c.create_line(0,ALTURA/2, BASE/2, ALTURA/2, fill = "black")



ventana_principal.mainloop()