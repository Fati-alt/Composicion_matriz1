import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from logica import composicion
from logica import potencia


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Composición Matricial")
        self.geometry("800x650")
        self.resizable(False, False)

        self.bg = "#4b4b87"
        self.fg = "white"
        self.box = "#50527B"

        self.configure(bg=self.bg)

        self.modo = tk.IntVar(value=1)

        self.n = 2
        self.grado = 2

        self.entradas_a = []
        self.entradas_b = []

        self.mostrar_inicio()

#Para limpiar ventana

    def limpiar(self):

        for widget in self.winfo_children():
            widget.destroy()

#Pantalla 1

    def mostrar_inicio(self):

        self.limpiar()

        titulo = tk.Label(
            self,
            text="Composición Matricial",
            font=("Arial", 20, "bold"),
            bg=self.bg,
            fg=self.fg
        )

        titulo.pack(pady=30)

        tk.Radiobutton(
            self,
            text="Potencia de una matriz",
            variable=self.modo,
            value=1,
            bg=self.bg,
            fg=self.fg,
            selectcolor=self.box
        ).pack(pady=10)

        tk.Radiobutton(
            self,
            text="Composición de dos matrices",
            variable=self.modo,
            value=2,
            bg=self.bg,
            fg=self.fg,
            selectcolor=self.box
        ).pack(pady=10)

        tk.Button(
            self,
            text="Continuar",
            command=self.mostrar_configuracion
        ).pack(pady=20)

#Pantalla 2
    def mostrar_configuracion(self):

        self.limpiar()

        tk.Label(
            self,
            text="Tamaño de matriz",
            bg=self.bg,
            fg=self.fg
        ).pack(pady=10)

        self.combo_n = ttk.Combobox(
            self,
            values=[2, 3, 4, 5],
            state="readonly"
        )

        self.combo_n.current(0)

        self.combo_n.pack()

        if self.modo.get() == 1:

            tk.Label(
                self,
                text="Grado",
                bg=self.bg,
                fg=self.fg
            ).pack(pady=10)

            self.entry_grado = tk.Entry(self)

            self.entry_grado.insert(0, "2")

            self.entry_grado.pack()

        tk.Button(
            self,
            text="Generar Matrices",
            command=self.mostrar_matrices
        ).pack(pady=20)

#Pantalla 3
    def mostrar_matrices(self):

        self.n = int(self.combo_n.get())
        if self.modo.get() == 1:
            self.grado = int(self.entry_grado.get())

        self.limpiar()

        self.entradas_a = []

        tk.Label(
            self,
            text="Matriz A",
            bg=self.bg,
            fg=self.fg
        ).pack()

        frame_a = tk.Frame(
            self,
            bg=self.bg
        )

        frame_a.pack(pady=10)

        for i in range(self.n):

            fila = []

            for j in range(self.n):

                e = tk.Entry(
                    frame_a,
                    width=3,
                    justify="center"
                )

                e.grid(
                    row=i,
                    column=j,
                    padx=2,
                    pady=2
                )

                fila.append(e)

            self.entradas_a.append(fila)

        if self.modo.get() == 2:

            self.entradas_b = []

            tk.Label(
                self,
                text="Matriz B",
                bg=self.bg,
                fg=self.fg
            ).pack()

            frame_b = tk.Frame(
                self,
                bg=self.bg
            )

            frame_b.pack(pady=10)

            for i in range(self.n):

                fila = []

                for j in range(self.n):

                    e = tk.Entry(
                        frame_b,
                        width=3,
                        justify="center"
                    )

                    e.grid(
                        row=i,
                        column=j,
                        padx=2,
                        pady=2
                    )

                    fila.append(e)

                self.entradas_b.append(fila)

        tk.Button(
            self,
            text="Calcular",
            command=self.calcular
        ).pack(pady=20)

#Leer matriz
    def leer_matriz(self, entradas):

        matriz = []

        try:

            for fila in entradas:

                nueva = []

                for e in fila:

                    valor = int(
                        e.get()
                    )

                    if valor not in (0, 1):

                        raise ValueError

                    nueva.append(valor)

                matriz.append(nueva)

            return matriz

        except:

            messagebox.showerror(
                "Error",
                "Solo se permiten 0 y 1"
            )

            return None
#Calcular
    def calcular(self):

        A = self.leer_matriz(
            self.entradas_a
        )

        if A is None:
            return

        if self.modo.get() == 1:

            try:

                grado = self.grado

            except:

                messagebox.showerror(
                    "Error",
                    "Grado inválido"
                )

                return

            resultado = potencia(
                A,
                grado
            )

        else:

            B = self.leer_matriz(
                self.entradas_b
            )

            if B is None:
                return

            resultado = composicion(
                A,
                B
            )

        self.mostrar_resultado(
            resultado
        )

   #Resultado
    def mostrar_resultado(
        self,
        matriz
    ):

        self.limpiar()

        tk.Label(
            self,
            text="Resultado",
            font=("Arial", 18, "bold"),
            bg=self.bg,
            fg=self.fg
        ).pack(pady=20)

        texto = ""

        for fila in matriz:

            texto += (
                " ".join(
                    map(str, fila)
                ) + "\n"
            )

        tk.Label(
            self,
            text=texto,
            font=("Consolas", 16),
            bg=self.bg,
            fg=self.fg
        ).pack()

        tk.Button(
            self,
            text="Nuevo cálculo",
            command=self.mostrar_inicio
        ).pack(pady=20)