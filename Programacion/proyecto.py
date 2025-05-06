import tkinter as tk
from tkinter import messagebox

class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        self.jugador_actual = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.crear_interfaz()

    def crear_interfaz(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(
                    self.root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda f=fila, c=col: self.jugar(f, c)
                )
                boton.grid(row=fila, column=col, padx=5, pady=5)
                self.botones[fila][col] = boton

    def jugar(self, fila, col):
        if self.tablero[fila][col] == "":
            self.tablero[fila][col] = self.jugador_actual
            self.botones[fila][col].config(text=self.jugador_actual, state="disabled")
            
            if self.verificar_victoria(self.jugador_actual):
                messagebox.showinfo("Fin del juego", f"Jugador {self.jugador_actual} ha ganado.")
                self.reiniciar_juego()
            elif self.tablero_lleno():
                messagebox.showinfo("Fin del juego", "Empate.")
                self.reiniciar_juego()
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def verificar_victoria(self, jugador):
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)) or \
               all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        if all(self.tablero[i][i] == jugador for i in range(3)) or \
           all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(self.tablero[f][c] != "" for f in range(3) for c in range(3))

    def reiniciar_juego(self):
        self.jugador_actual = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for fila in range(3):
            for col in range(3):
                self.botones[fila][col].config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    juego = TresEnRaya(root)
    root.mainloop()

