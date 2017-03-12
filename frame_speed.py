from tkinter import *

class FrameSpeed(LabelFrame):
    
    def __init__(self, interface, **kwargs):
        LabelFrame.__init__(self, interface.windows, **kwargs)

        self.interface= interface
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        
        self.Slow= IntVar()
        self.SlowEntry= Entry(self, textvariable= self.Slow, width=4)
        self.SlowEntry.bind("<Return>", self.SlowChange)
        self.Slow.set(0)
        Label(self, text="Slow").grid(column=0, row=0, pady=2, padx=5, sticky=W)        
        self.SlowEntry.grid(column=1, row=0, padx=5, pady=5)

        self.Fast= IntVar()        
        self.FastEntry= Entry(self, textvariable= self.Fast, width=4)
        self.FastEntry.bind("<Return>", self.FastChange)
        self.Fast.set(255)
        self.FastEntry.grid(column=3, row=0, padx=5, pady=5)
        Label(self, text="Fast").grid(column=4, row=0, pady=2, padx=5, sticky=W)        

        self.SpeedvalueScale = IntVar()
        self.SpeedvalueScale= Scale(self, from_=self.Slow.get(), to=self.Fast.get(), orient=HORIZONTAL, variable=self.SpeedvalueScale, showvalue=0, command=self.SpeedChangeScale)
        self.SpeedvalueScale.grid(column=2, row=0, sticky=E)

        self.realtime = IntVar()
        self.realtimeCB= Checkbutton(self, text="Real Time ?",  variable=self.realtime, command=self.realTimeChange)
        self.realtimeCB.grid(column=0, row=1, columnspan=2, sticky=W)
        self.realtime.set(0)

        self.SpeedvalueEntry= IntVar()
        self.SpeedEntry= Entry(self, textvariable= self.SpeedvalueEntry, width=4)
        self.SpeedEntry.bind("<Return>", self.SpeedChangeEntry)
        self.SpeedEntry.grid(column=2, row=1)
        self.SpeedvalueEntry.set(128)

        # PID Speed is not implemented
        self.getButton= Button(self, text="   Get   ", command=self.getPressed)
        self.getButton.grid(column=0, columnspan=2, row=2, padx=5, pady=5)
        self.setButton= Button(self, text="   Set   ", command=self.setPressed)
        self.setButton.grid(column=3, columnspan=2,  row=2, padx=5, pady=5)

        self.SlowEntry.configure(state="disable")
        self.FastEntry.configure(state="disable")
        self.SpeedvalueScale.configure(state="disable")
        self.realtimeCB.configure(state="disable")
        self.SpeedEntry.configure(state="disable")
        self.getButton.configure(state="disable")
        self.setButton.configure(state="disable")

        
    def realTimeChange(self):
        value= int(self.realtime.get())
        print ("RealTime is ", value)
        if value == 1:
            self.getButton.configure(state="disable")
            self.setButton.configure(state="disable")
        else :
            self.getButton.configure(state="normal")
            self.setButton.configure(state="normal")
                

    def SpeedChangeScale(self, event):
        self.SpeedvalueEntry.set(self.SpeedvalueScale.get())
        realTime= int(self.realtime.get())
        if realTime == 1:
            print ("Speed is ", self.SpeedvalueScale.get())

    def SpeedChangeEntry(self, event):
        self.SpeedvalueScale.set(self.SpeedvalueEntry.get())
        realTime= int(self.realtime.get())
        if realTime == 1:
            print ("Speed is ", self.SpeedvalueEntry.get())
            
    def SlowChange(self, event):
        self.SpeedvalueScale.config(from_=self.Slow.get())

    def FastChange(self, event):
        self.SpeedvalueScale.config(to=self.Fast.get())

    def setPressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.log_print("\nSet Speed= %d" % self.interface.mboxeGet.SpeedCurrent)
        else:
            self.interface.log_print("\nNo Mboxe selected")
            
    def getPressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.mboxeGet.get_SpeedCurrent()
            self.SpeedvalueEntry.set(self.interface.mboxeGet.SpeedCurrent)
            self.interface.log_print("\nGet Speed= %d" % self.interface.mboxeGet.SpeedCurrent)
        else:
            self.interface.log_print("\nNo Mboxe selected")
            

    def update(self, mboxeGet):
        #self.Slow.set(mboxeGet.return_Slow())
        #self.Fast.set(mboxeGet.return_Fast())        
        self.SpeedvalueEntry.set(mboxeGet.return_SpeedCurrent())
        self.SpeedvalueScale.set(mboxeGet.return_SpeedCurrent())
        self.SpeedvalueScale.update()

