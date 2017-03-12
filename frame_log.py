from tkinter import *

class FrameLog(LabelFrame):

    def __init__(self, fenetre, **kwargs):
        LabelFrame.__init__(self, fenetre, **kwargs)

        #self.columnconfigure(0, weight=1)

        self.scrollBar1 = Scrollbar(self, orient=VERTICAL) 
        self.scrollBar2 = Scrollbar(self, orient=HORIZONTAL) 
        self.text = Text(self, wrap=NONE, width=39, height=5)    
  
## association du déplacement de la glissière des scrollbar avec la position visible dans  
## le widget Text et inversement.               
        self.scrollBar1.config(command = self.text.yview) 
        self.scrollBar2.config(command = self.text.xview) 
        self.text.config(yscrollcommand = self.scrollBar1.set, xscrollcommand = self.scrollBar2.set) 
  
## Placement du widget Text et des Scrollbar associés 
        self.text.grid(column=0, row=0) 
        self.scrollBar1.grid(column=1, row=0, sticky=S+N) 
        self.scrollBar2.grid(column=0, row=1, sticky=W+E) 

    def print(self, message):
        #self.text.insert(END, "\n")
        self.text.insert(END, message)
        self.text.see(END)
        self.text.xview_moveto(0.0)

