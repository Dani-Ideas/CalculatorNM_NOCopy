from tkinter import Tk
from Controllers.Controller_scienceGraficNM import CalculatorController

if __name__ == "__main__":
    root = Tk()
    app = CalculatorController(root)
    root.mainloop()