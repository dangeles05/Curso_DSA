import tkinter as tk
from tkinter import messagebox, simpledialog
from StackHanoi import Stack

class InterfazHanoi:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanoi")  # Configura el título de la ventana principal
        
        # Variables del juego
        self.stacks = []  # Lista de las pilas (izquierda, medio, derecha)
        self.num_disks = 0  # Número de discos (se define al iniciar el juego)
        self.num_user_moves = 0  # Contador de movimientos realizados por el usuario
        self.num_optimal_moves = 0  # Número óptimo de movimientos para resolver el juego
        self.selected_from = None  # Pila seleccionada como origen para mover un disco

        # Configuración inicial del juego (pantalla inicial)
        self.setup_game()
    
    def setup_game(self):
        """Muestra la pantalla inicial para configurar el número de discos."""
        self.start_frame = tk.Frame(self.root)  # Crea un marco para la configuración inicial
        self.start_frame.pack(pady=20)  # Añade espacio vertical

        # Etiqueta para pedir el número de discos
        tk.Label(self.start_frame, text="Selecciona el número de discos (3-8):").pack()

        # Entrada para ingresar el número de discos
        self.disk_input = tk.Entry(self.start_frame)
        self.disk_input.pack()

        # Botón para iniciar el juego
        tk.Button(self.start_frame, text="Iniciar Juego", command=self.start_game).pack(pady=10)
    
    def start_game(self):
        """Inicia el juego después de ingresar el número de discos."""
        try:
            self.num_disks = int(self.disk_input.get())  # Convierte la entrada en un número entero
            if self.num_disks < 3 or self.num_disks > 8:  # Valida que el número de discos sea entre 3 y 8
                raise ValueError  # Lanza un error si el número no es válido
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número entre 3 y 8.")  # Muestra un mensaje de error
            return

        # Configuración inicial de las variables del juego
        self.num_user_moves = 0
        self.num_optimal_moves = 2 ** self.num_disks - 1  # Fórmula para los movimientos mínimos

        # Elimina la pantalla inicial
        self.start_frame.destroy()

        # Crea las pilas y agrega los discos
        self.create_stacks()

        # Configura la interfaz gráfica principal
        self.setup_gui()
    
    def create_stacks(self):
        """Crea las pilas y añade los discos a la pila izquierda."""
        self.stacks = [
            Stack("Left"),   # Pila izquierda
            Stack("Middle"),  # Pila central
            Stack("Right")   # Pila derecha
        ]

        # Añade los discos a la pila izquierda en orden descendente
        for disk in range(self.num_disks, 0, -1):
            self.stacks[0].push(disk)
    
    def setup_gui(self):
        """Configura la interfaz gráfica principal del juego."""
        self.main_frame = tk.Frame(self.root)  # Crea el marco principal
        self.main_frame.pack()

        # Canvas para visualizar las pilas
        self.canvas = tk.Canvas(self.main_frame, width=600, height=400, bg="white")
        self.canvas.pack()

        # Frame para los botones de interacción
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=10)

        # Botones de interacción (seleccionar origen, destino, reiniciar juego)
        tk.Button(self.buttons_frame, text="Seleccionar Origen", command=self.select_from).pack(side="left", padx=10)
        tk.Button(self.buttons_frame, text="Seleccionar Destino", command=self.select_to).pack(side="left", padx=10)
        tk.Button(self.buttons_frame, text="Reiniciar Juego", command=self.reset_game).pack(side="left", padx=10)

        # Etiqueta para mostrar los movimientos realizados
        self.info_label = tk.Label(self.main_frame, text=f"Movimientos: 0 | Mínimos: {self.num_optimal_moves}")
        self.info_label.pack(pady=10)

        # Dibuja las pilas y los discos
        self.draw_stacks()
    
    def draw_stacks(self):
        """Dibuja las pilas y los discos en el canvas."""
        self.canvas.delete("all")  # Limpia el canvas
        positions = [100, 300, 500]  # Posiciones x de las pilas

        # Colores para los discos (en función de su tamaño)
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

        for i, stack in enumerate(self.stacks):
            # Dibujar la base de la pila
            self.canvas.create_rectangle(positions[i] - 50, 350, positions[i] + 50, 360, fill="black")
            self.canvas.create_line(positions[i], 100, positions[i], 350, fill="black", width=3)

            # Obtener discos de la pila actual
            disks = []
            pointer = stack.top_item  # Apunta al disco superior
            while pointer:
                disks.append(pointer.get_value())  # Añade el valor del disco
                pointer = pointer.get_next_node()

            # Dibujar los discos en orden inverso
            for j, disk in enumerate(reversed(disks)):
                width = disk * 20  # Calcula el ancho del disco según su tamaño
                color = colors[(disk - 1) % len(colors)]  # Asigna un color
                self.canvas.create_rectangle(
                    positions[i] - width // 2,
                    340 - j * 20,
                    positions[i] + width // 2,
                    360 - j * 20,
                    fill=color,
                    outline="black"
                )
    
    def select_from(self):
        """Permite seleccionar la pila de origen."""
        self.selected_from = self.get_stack_choice("Selecciona la pila de origen:")
        if self.selected_from is not None:
            messagebox.showinfo("Origen Seleccionado", f"Pila seleccionada: {self.selected_from.get_name()}")
    
    def select_to(self):
        """Permite seleccionar la pila de destino y realiza el movimiento."""
        if not self.selected_from:
            messagebox.showerror("Error", "Primero selecciona una pila de origen.")  # Error si no se ha seleccionado origen
            return

        selected_to = self.get_stack_choice("Selecciona la pila de destino:")
        if selected_to is not None:
            if self.validate_move(self.selected_from, selected_to):  # Valida el movimiento
                disk = self.selected_from.pop()  # Remueve el disco de origen
                selected_to.push(disk)  # Añade el disco a destino
                self.num_user_moves += 1  # Incrementa el contador de movimientos
                self.info_label.config(
                    text=f"Movimientos: {self.num_user_moves} | Mínimos: {self.num_optimal_moves}"
                )
                self.draw_stacks()  # Redibuja las pilas

                # Verifica si el juego se completó
                if self.stacks[2].get_size() == self.num_disks:
                    messagebox.showinfo(
                        "Juego Completado",
                        f"¡Completaste el juego en {self.num_user_moves} movimientos!"
                    )
                    self.reset_game()  # Reinicia el juego
            else:
                messagebox.showerror("Error", "Movimiento no válido. Inténtalo de nuevo.")
    
    def validate_move(self, from_stack, to_stack):
        """Valida si un movimiento es válido."""
        if from_stack.is_empty():  # No se puede mover desde una pila vacía
            return False
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():  # Movimiento válido si la pila destino está vacía o el disco es más pequeño
            return True
        return False
    
    def get_stack_choice(self, message):
        """Muestra un diálogo para seleccionar una pila (L, M, R)."""
        choice = simpledialog.askstring("Seleccionar Pila", message)  # Diálogo para pedir entrada
        if choice is None:  # Si el usuario cancela
            return None

        choice = choice.upper()
        if choice == "L":  # Pila izquierda
            return self.stacks[0]
        elif choice == "M":  # Pila central
            return self.stacks[1]
        elif choice == "R":  # Pila derecha
            return self.stacks[2]
        else:
            messagebox.showerror("Error", "Entrada no válida. Usa L, M o R.")  # Error si la entrada es inválida
            return None

    def reset_game(self):
        """Reinicia el juego eliminando el marco principal y mostrando la configuración inicial."""
        self.main_frame.destroy()  # Elimina el marco principal
        self.setup_game()  # Vuelve a mostrar la pantalla inicial

# Inicialización de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazHanoi(root)
    root.mainloop()