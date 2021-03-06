from Tkinter import *

root = Tk()
Label(root, text = "Northwest Latitude / Longitude").grid(row = 0, sticky = W)
Label(root, text = "Southwest Latitude / Longitude").grid(row = 1, sticky = W)
Label(root, text = "Northeast Latitude / Longitude").grid(row = 2, sticky = W)
Label(root, text = "Southeast Latitude / Longitude").grid(row = 3, sticky = W)
Label(root, text = "How many random GPS Coordinates would you like?").grid(row = 4, sticky = W)

NWLA = Entry(root)
NWLO = Entry(root)
SWLA = Entry(root)
SWLO = Entry(root)
NELA = Entry(root)
NELO = Entry(root)
SELA = Entry(root)
SELO = Entry(root)
random = Entry(root)


NWLA.grid(row = 0, column = 1)
NWLO.grid(row = 0, column = 2)
SWLA.grid(row = 1, column = 1)
SWLO.grid(row = 1, column = 2)
NELA.grid(row = 2, column = 1)
NELO.grid(row = 2, column = 2)
SELA.grid(row = 3, column = 1)
SELO.grid(row = 3, column = 2)
random.grid(row = 4, column = 1)

def getInput():
    with open("examples.txt", 'a') as outfile:
        outfile.write(NWLA.get())
        outfile.write('\n')
        outfile.write(NWLO.get())
        outfile.write('\n')
        outfile.write(SWLA.get())
        outfile.write('\n')
        outfile.write(SWLO.get())
        outfile.write('\n')
        outfile.write(NELA.get())
        outfile.write('\n')
        outfile.write(NELO.get())
        outfile.write('\n')
        outfile.write(SELA.get())
        outfile.write('\n')
        outfile.write(SELO.get())
        outfile.write('\n')
        outfile.write(random.get())
        outfile.write('\n')
        root.destroy()

Button(root, text = "submit", command = getInput).grid(row = 5, sticky = W)
mainloop()
