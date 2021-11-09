from tkinter import *

class Elevator_label(Label):

    def __init__(self, sim_window:Simulator_Window = none):
        super(Elevator_label, self).__init__(window=sim_window)



class Simulator_Window(Tk):

    def __init__(self, num_of_elev:int = 1):
        super(Simulator_Window, self).__init__()
        self.geometry("1000x700")
        self.resizable(FALSE, FALSE)
        self.title("Elevator simulator")
        self.configure(bg='black')
        close_image = PhotoImage("../../images/closeDoors.png")
        self.elev = Label(self, image=close_image).pack

    def show(self):
        self.mainloop()



if __name__ == '__main__':
    window = Simulator_Window()
    window.show()




