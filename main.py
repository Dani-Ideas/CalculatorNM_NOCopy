from Controller.ControllerPrincipal import ControllerPrincipal
from Model.ModelPrincipal import ModelPrincipal
from View.ViewPrincipal import ViewPrincipal
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    model_principal = ModelPrincipal()
    view_principal = ViewPrincipal(root)
    controller_principal = ControllerPrincipal(model_principal, view_principal)
    root.mainloop()
    