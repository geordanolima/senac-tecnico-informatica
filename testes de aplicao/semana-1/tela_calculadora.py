import customtkinter as ctk
from calculadora import calcular

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("350x350")
        self.title("Calculadora")

        self.display_var = ctk.StringVar(value="0")
        self.display = ctk.CTkLabel(self, textvariable=self.display_var, font=("Arial", 24), height=50)
        self.display.pack(pady=10)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10, padx=20)
        # Botões numéricos e operadores
        button_grid = [["7", "8", "9", "C", "*"],
                       ["4", "5", "6", "-", "/"],
                       ["1", "2", "3"],
                       ["0", False, "."]]

        for row, buttons in enumerate(button_grid):
            for col, button_text in enumerate(buttons):
                if button_text:
                    button = ctk.CTkButton(
                        button_frame, text=button_text, command=lambda t=button_text: self.click_button(t), width=50
                    )
                    button.grid(row=row, column=col, padx=5, pady=5)

        soma_button = ctk.CTkButton(button_frame, text="+", command=lambda: self.click_button("+"), width=50, height=70)
        soma_button.grid(row=2, column=3, padx=5, pady=5, rowspan=2)
        igual_button = ctk.CTkButton(button_frame, text="=", command=lambda: self.click_button("="), width=50, height=70)
        igual_button.grid(row=2, column=4, padx=5, pady=5, rowspan=2)

    def click_button(self, text):
        self.click(text=text)
    
    def click(self, text):
        retorno = calcular(text, self.display_var.get())
        if retorno:
            self.display_var.set(retorno)
        else:
            self.display_var.set('0')


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
