from tkinter import *
from epidemicback import World

class MyEpidemicModel:
    def __init__(self, master):
            
        self.height = 300
        self.width = 200
        self.people_infected=0

        self.master = master
        master.title("An Epidemic Model")

        self.label = Label(master, text="This is our Epidemic Model")
        self.label.pack()

        self.lbl_population= Label(master, text="population size")
        self.lbl_population.pack()

        self.population=IntVar()

        self.entry_population = Entry(self.master, textvariable=self.population)
        self.entry_population.pack()
    

        self.lbl_people_infected = Label(self.master, text="no. of people infected=" + str(self.people_infected))
        self.lbl_people_infected.pack()

        self.this_world = World(self.height, self.width, self.entry_population.get())

        self.canvas = Canvas(master, width = self.width, height = self.height)
        self.canvas.pack()
        
        
        for person in self.this_world.get_people():
            x, y = person.get_location()
            self.canvas.create_oval(x,y, x+3, y+3, fill="red")
        self.update_epidemic()
        
        
        
        
    def update_epidemic(self):
        
        self.canvas.delete("all")

        self.this_world.update_world()

        self.people_infected=0

        for person in self.this_world.get_people():
            x, y = person.get_location()

            if person.get_infection()==True:
                colour="blue"
                self.people_infected+=1
            elif person.get_doctor()==True:
                colour="yellow"
            else:
                colour="red"
            self.canvas.create_oval(x,y, x+3, y+3, fill=colour)

        
        self.canvas.after(100, self.update_epidemic)
        self.lbl_people_infected.configure(text="no. of people infected=" + str(self.people_infected))




if __name__ == "__main__":
    root = Tk()
    my_gui = MyEpidemicModel(root)
    root.mainloop()
