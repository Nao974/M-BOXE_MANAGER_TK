from tkinter import *

class FramePosition(LabelFrame):
    
    def __init__(self, interface, **kwargs):
        LabelFrame.__init__(self, interface.windows, **kwargs)

        self.interface= interface
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        
        self.limitBW= IntVar()
        self.limitBWEntry= Entry(self, textvariable= self.limitBW, width=4)
        self.limitBWEntry.bind("<FocusOut>", self.limitBW_changed)
        self.limitBW.set(350)
        Label(self, text=self.interface.lang["LimitBW"]).grid(column=0, row=0, pady=2, padx=5, sticky=W)        
        self.limitBWEntry.grid(column=1, row=0, padx=5, pady=5)

        self.limitFW= IntVar()        
        self.limitFWEntry= Entry(self, textvariable= self.limitFW, width=4)
        Label(self, text=self.interface.lang["LimitFW"]).grid(column=4, row=0, pady=2, padx=5, sticky=W)        
        self.limitFWEntry.bind("<FocusOut>", self.limitFW_changed)
        self.limitFW.set(1150)
        self.limitFWEntry.grid(column=3, row=0, padx=5, pady=5)

        self.positionvalueScale = IntVar()
        self.positionScale= Scale(self, from_=self.limitBW.get(), to=self.limitFW.get(), orient=HORIZONTAL, variable=self.positionvalueScale, showvalue=0, command=self.positionScale_changed)
        self.positionScale.grid(column=2, row=0, sticky=E)

        self.contactBW= StringVar()
        self.contactBW.set("%s: ?" % self.interface.lang["Contact BW"])
        Label(self, textvariable=self.contactBW).grid(column=0, row=1, pady=2, columnspan=2, padx=5, sticky=W)        

        self.positionvalueEntry= IntVar()
        self.positionEntry= Entry(self, textvariable= self.positionvalueEntry, width=4)
        self.positionEntry.bind("<FocusOut>", self.positionEntry_changed)
        self.positionEntry.grid(column=2, row=1)
        self.positionvalueEntry.set(750)

        self.contactFW= StringVar()
        self.contactFW.set("%s: ?" % self.interface.lang['Contact FW'])
        Label(self, textvariable=self.contactFW).grid(column=3, row=1, pady=2, columnspan=2, padx=5, sticky=E)        

        self.getButton= Button(self, text="   %s   " % self.interface.lang['Get'], command=self.getPressed)
        self.getButton.grid(column=0, columnspan=2, row=2, pady=5, sticky=E)
        self.setButton= Button(self, text="   %s   " % self.interface.lang['Set'], command=self.setPressed)
        self.setButton.grid(column=3, columnspan=2,  row=2, pady=5, sticky=W)        
                

    def positionScale_changed(self, event):
        value= self.positionvalueScale.get()
        self.positionvalueEntry.set(value)
        self.interface.mboxeGet.positionCurrent= value



    def positionEntry_changed(self, event):
        try:
            value= self.positionvalueEntry.get()
        except:
            value=0
        lastValue= self.interface.mboxeGet.positionCurrent
        minRef= self.interface.mboxeGet.positionCurrent_ref["min"]
        maxRef= self.interface.mboxeGet.positionCurrent_ref["max"]
        if value>=minRef and value<=maxRef:
            self.positionvalueScale.set(value)
            self.interface.mboxeGet.positionCurrent= value
        else:
            self.positionvalueEntry.set(lastValue)
            self.interface.log_print("\n%s: %s %d<>%d" % (self.interface.lang['Position'], self.interface.lang['Invalid value'], minRef, maxRef))
            
    def limitBW_changed(self, event):
        try:
            value= self.limitBW.get()
        except:
            value=0
        lastValue= self.interface.mboxeGet.limitBW
        minRef= self.interface.mboxeGet.limitBW_ref["min"]
        maxRef= self.interface.mboxeGet.limitBW_ref["max"]
        if value>=minRef and value<=maxRef:
            self.positionScale.config(from_= value)
            self.interface.mboxeGet.limitBW= value
        else:
            self.limitBW.set(lastValue)
            self.interface.log_print("\n%s: %s %d<>%d" % (self.interface.lang['LimitBW'], self.interface.lang['Invalid value'], minRef, maxRef))
            
    def limitFW_changed(self, event):
        try:
            value= self.limitFW.get()
        except:
            value=0
        lastValue= self.interface.mboxeGet.limitFW
        minRef= self.interface.mboxeGet.limitFW_ref["min"]
        maxRef= self.interface.mboxeGet.limitFW_ref["max"]
        if value>=minRef and value<=maxRef:
            self.positionScale.config(to = value)
            self.interface.mboxeGet.limitFW= value
        else:
            self.limitFW.set(lastValue)
            self.interface.log_print("\n%s: %s %d<>%d" % (self.interface.lang['LimitFW'], self.interface.lang['Invalid value'], minRef, maxRef))
       
    def setPressed(self):
        if self.interface.mboxeSelected > 2:
            value= self.positionvalueScale.get()
            self.interface.mboxeGet.set_positionCurrent(value)
            self.interface.log_print("\n%s= %d" % (self.interface.lang['Set Position'], self.positionvalueEntry.get()) )
        else:
            self.interface.log_print("\n%s" % self.interface.lang['Not selected Mboxe'])
            
    def getPressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.mboxeGet.get_positionCurrent()
            self.positionvalueEntry.set(self.interface.mboxeGet.positionCurrent)
            self.positionvalueScale.set(self.interface.mboxeGet.positionCurrent)
            self.positionScale.update()
            self.interface.log_print("\n%s= %d" % (self.interface.lang['Get Position'], self.interface.mboxeGet.positionCurrent) )
        else:
            self.interface.log_print("\n%s" % self.interface.lang['Not selected Mboxe'])
            

    def update(self, mboxeGet):
        self.limitBW.set(mboxeGet.return_limitBW())
        self.limitFW.set(mboxeGet.return_limitFW())        
        self.positionvalueEntry.set(mboxeGet.return_positionCurrent())
        self.positionvalueScale.set(mboxeGet.return_positionCurrent())
        self.positionScale.update()
        contactBWFW= mboxeGet.return_contactBWFW()
        self.contactBW.set("%s: %s" % (self.interface.lang['Contact BW'], (1 & (contactBWFW) >> 5) ) )
        self.contactFW.set("%s: %s" % (self.interface.lang['Contact FW'], (1 & (contactBWFW) >> 4) ) )
