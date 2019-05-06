import tkinter


# search or cleans
def runPhase1():
# if action == 'search':
    import Phase2.py

def runPhase2():
# if action == 'cleans':
    import Phase1.py

# GUI
window = tkinter.Tk()
window.title("Ontology-Based Data Cleaning & Cleansing System(Customized for Olympic Data-Set)")
# frame = tkinter.Frame(window).pack()
btn1 = tkinter.Button(window, text = "phase_1", fg = "Red", command= runPhase1).grid(row = 0, column = 1)
btn2 = tkinter.Button(window, text = "phase_2", fg = "Green", command= runPhase2).grid(row = 1, column = 1)
tkinter.Label(window, text = "If you want to search athletes in their olympic records please"
                             "select phase_1", fg = "Black").grid(row = 0, column = 0)
tkinter.Label(window, text = "If you want to clean the uncleaned pleasedata select phase_2  "
                             "                     ", fg = "Black").grid(row = 1, column = 0)
window.mainloop()
