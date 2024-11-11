class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind_buttons()

    def bind_buttons(self):
        # Vincular todos los botones con el método on_button_click
        for button in self.view.button_frame.winfo_children():
            button.bind("<Button-1>", self.on_button_click)

    def on_button_click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            expression = self.view.get_expression()

            try:
                x1_value = float(self.view.get_x1_value())
            except ValueError:
                self.view.set_expression("Error: Invalid x1")
                return
            try:
                x2_value = float(self.view.get_x2_value())
            except ValueError:
                self.view.set_expression("Error: Invalid x2")
                return

            result1 = self.model.evaluate_expression(expression, x1_value)
            result2 = self.model.evaluate_expression(expression, x2_value)
            criterio ="-"if (float(result1)*float(result2))<=0 else "+"
            print(f"function input: {expression}, value to reslult 1:{x1_value}, value to reslult 2:{x2_value} ,result 1: {result1}, result 2: {result2} el signo es {criterio}")
            self.view.set_expression(result1)
        elif text == "AC":
            self.view.clear()
        else:
            current_text = self.view.get_expression()
            self.view.set_expression(current_text + text)
