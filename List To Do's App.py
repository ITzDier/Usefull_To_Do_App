import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.config(bg='#120FC4')

        # Configuración de la interfaz
        self.frame = tk.Frame(root, padx=10, pady=10, bg="#120FC4")
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.task_entry = tk.Entry(self.frame, width=50, font=('Helvetica', 12), fg='black', bg='cyan')
        self.task_entry.pack(pady=10)

        # Botones de acción
        self.add_button = tk.Button(self.frame, text="Agregar Tarea", command=self.add_task, font=('Helvetica', 10, 'bold'), bg="#8B0018", fg='yellow', relief=tk.FLAT)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.frame, width=70, height=15, selectmode=tk.SINGLE, font=('Helvetica', 12), fg='black', bg='cyan')
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(self.frame, text="Marcar como Completa", command=self.complete_task, font=('Helvetica', 10, 'bold'), bg='#8B0018', fg='yellow', relief=tk.FLAT)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task, font=('Helvetica', 10, 'bold'), bg='#8B0018', fg='yellow', relief=tk.FLAT)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)
            
            # Formato para indicar que la tarea está completa
            completed_task = "✓ " + selected_task.replace("✓ ", "")
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)
            self.task_listbox.itemconfig(selected_task_index, fg='gray')

        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    app = tk.Tk()
    root = TodoApp(app)
    app.geometry("800x600")
    app.mainloop()