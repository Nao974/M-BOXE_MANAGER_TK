from tkinter import *

class FrameAdvanced(LabelFrame):
    
    def __init__(self, interface, **kwargs):
        LabelFrame.__init__(self, interface.windows, **kwargs)

        self.interface= interface

        Label(self, text=self.interface.lang['Position']).grid(column=0, row=0, columnspan=2, pady=2, padx=5)

        self.offset= IntVar()
        self.offsetEntry= Entry(self, textvariable= self.offset, width=4)
        self.offsetEntry.bind("<FocusOut>", self.offset_changed)
        Label(self, text="Offset").grid(column=0, row=1, pady=2, padx=5, sticky=W)        
        self.offsetEntry.grid(column=1, row=1, padx=5, pady=5)

        self.deadBand= IntVar()
        self.deadBandEntry= Entry(self, textvariable= self.deadBand, width=4)
        self.deadBandEntry.bind("<FocusOut>", self.deadBand_changed)
        Label(self, text="Dead-Band").grid(column=0, row=2, pady=2, padx=5, sticky=W)        
        self.deadBandEntry.grid(column=1, row=2, padx=5, pady=5)

        Label(self, text="PID %s" % self.interface.lang['Position']).grid(column=0, row=4, columnspan=2, pady=2, padx=5)

        self.kpPunch= DoubleVar()
        self.kpPunchEntry= Entry(self, textvariable= self.kpPunch, width=4)
        self.kpPunchEntry.bind("<FocusOut>", self.kpPunch_changed)
        Label(self, text="kp-Punch").grid(column=0, row=5, pady=2, padx=5, sticky=W)        
        self.kpPunchEntry.grid(column=1, row=5, padx=5, pady=5)

        self.kdDumping= DoubleVar()
        self.kdDumpingEntry= Entry(self, textvariable= self.kdDumping, width=4)
        self.kdDumpingEntry.bind("<FocusOut>", self.kdDumping_changed)
        Label(self, text="kd-Dumping").grid(column=0, row=6, pady=2, padx=5, sticky=W)        
        self.kdDumpingEntry.grid(column=1, row=6, padx=5, pady=5)

        self.kiStretch= DoubleVar()
        self.kiStretchEntry= Entry(self, textvariable= self.kiStretch, width=4)
        self.kiStretchEntry.bind("<FocusOut>", self.kiStretch_changed)
        Label(self, text="ki-Stretch").grid(column=0, row=7, pady=2, padx=5, sticky=W)        
        self.kiStretchEntry.grid(column=1, row=7, padx=2, pady=5)

        Label(self, text=self.interface.lang['Protection']).grid(column=2, row=0, columnspan=2, pady=2, padx=5)

        self.currentMaxSet= DoubleVar()
        self.currentMaxSetEntry= Entry(self, textvariable= self.currentMaxSet, width=4)
        self.currentMaxSetEntry.bind("<FocusOut>", self.currentMaxSet_changed)
        Label(self, text="%s Max  (A)" % self.interface.lang['Current']).grid(column=2, row=1, pady=2, padx=5, sticky=E)        
        self.currentMaxSetEntry.grid(column=3, row=1, padx=5, pady=5)

        self.protectionGoSet= IntVar()
        self.protectionGoSetEntry= Entry(self, textvariable= self.protectionGoSet, width=4)
        self.protectionGoSetEntry.bind("<FocusOut>", self.protectionGoSet_changed)
        Label(self, text="%s (S)" % self.interface.lang['Protection']).grid(column=2, row=2, pady=2, padx=5, sticky=E)        
        self.protectionGoSetEntry.grid(column=3, row=2, padx=5, pady=5)

        self.temperatureMaxSet= IntVar()
        self.temperatureMaxSetEntry= Entry(self, textvariable= self.temperatureMaxSet, width=4)
        self.temperatureMaxSetEntry.bind("<FocusOut>", self.temperatureMaxSet_changed)
        Label(self, text="Temp. Max (°C)").grid(column=2, row=3, pady=2, padx=5, sticky=E)        
        self.temperatureMaxSetEntry.grid(column=3, row=3, padx=5, pady=5)

        Label(self, text="PID %s" % self.interface.lang['Speed']).grid(column=2, row=4, columnspan=2, pady=2, padx=5)

        self.kp= DoubleVar()
        self.kpEntry= Entry(self, textvariable= self.kp, width=4)
        Label(self, text="kp").grid(column=2, row=5, pady=2, padx=5, sticky=E)
        self.kpEntry.configure(state="disable")
        self.kpEntry.grid(column=3, row=5, padx=5, pady=5)

        self.kd= DoubleVar()
        self.kdEntry= Entry(self, textvariable= self.kd, width=4)
        Label(self, text="kd").grid(column=2, row=6, pady=2, padx=5, sticky=E)        
        self.kdEntry.configure(state="disable")
        self.kdEntry.grid(column=3, row=6, padx=5, pady=5)

        self.ki= DoubleVar()
        self.kiEntry= Entry(self, textvariable= self.ki, width=4)
        Label(self, text="ki").grid(column=2, row=7, pady=2, padx=5, sticky=E)        
        self.kiEntry.configure(state="disable")
        self.kiEntry.grid(column=3, row=7, padx=2, pady=5)
    
    def update(self, mboxeGet):
        self.offset.set(mboxeGet.return_offset())
        self.deadBand.set(mboxeGet.return_deadBand())
        self.kpPunch.set(mboxeGet.return_kpPunch())
        self.kdDumping.set(mboxeGet.return_kdDumping())
        self.kiStretch.set(mboxeGet.return_kiStretch())
        self.currentMaxSet.set(mboxeGet.return_currentMaxSet())
        self.protectionGoSet.set(mboxeGet.return_protectionGoSet())
        self.temperatureMaxSet.set(mboxeGet.return_temperatureMaxSet())
        
    def offset_changed(self, event):
        try:
            value= self.offset.get()
        except:
            value=-200
        lastValue= self.interface.mboxeGet.offset
        minRef= self.interface.mboxeGet.offset_ref["min"]
        maxRef= self.interface.mboxeGet.offset_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.offset= value
        else:
            self.offset.set(lastValue)
            self.interface.log_print("\nOffset: %s %d<>%d" % (self.interface.lang['Invalid value'], minRef, maxRef))
        
    def deadBand_changed(self, event):
        try:
            value= self.deadBand.get()
        except:
            value=-1   
        lastValue= self.interface.mboxeGet.deadBand
        minRef= self.interface.mboxeGet.deadBand_ref["min"]
        maxRef= self.interface.mboxeGet.deadBand_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.deadBand= value
        else:
            self.deadBand.set(lastValue)
            self.interface.log_print("\nDeadBand: %s %d<>%d" % (self.interface.lang['Invalid value'],minRef, maxRef))

    def kpPunch_changed(self, event):
        try:
            value= self.kpPunch.get()
        except:
            value=-1
        lastValue= self.interface.mboxeGet.kpPunch
        minRef= self.interface.mboxeGet.kpPunch_ref["min"]
        maxRef= self.interface.mboxeGet.kpPunch_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.kpPunch= value
        else:
            self.kpPunch.set(lastValue)
            self.interface.log_print("\nkpPunch:%s %d<>%d" % (self.interface.lang['Invalid value'],minRef, maxRef))

    def kdDumping_changed(self, event):
        try:
            value= self.kdDumping.get()
        except:
            value=-1 
        lastValue= self.interface.mboxeGet.kdDumping
        minRef= self.interface.mboxeGet.kdDumping_ref["min"]
        maxRef= self.interface.mboxeGet.kdDumping_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.kdDumping= value
        else:
            self.kdDumping.set(lastValue)
            self.interface.log_print("\nkdDumping: %s %d<>%d" % (self.interface.lang['Invalid value'],minRef, maxRef))

    def kiStretch_changed(self, event):
        try:
            value= self.kiStretch.get()
        except:
            value=-1       
        lastValue= self.interface.mboxeGet.kiStretch
        minRef= self.interface.mboxeGet.kiStretch_ref["min"]
        maxRef= self.interface.mboxeGet.kiStretch_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.kiStretch= value
        else:
            self.kiStretch.set(lastValue)
            self.interface.log_print("\nkiStretch: %s %d<>%d" % (self.interface.lang['Invalid value'],minRef, maxRef))

    def currentMaxSet_changed(self, event):
        try:
            value= self.currentMaxSet.get()
        except:
            value=-1       
        lastValue= self.interface.mboxeGet.currentMaxSet
        minRef= self.interface.mboxeGet.currentMaxSet_ref["min"]
        maxRef= self.interface.mboxeGet.currentMaxSet_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.currentMaxSet= value
        else:
            self.currentMaxSet.set(lastValue)
            self.interface.log_print("\n%sMaxSet: %s %d<>%d" % (self.interface.lang['Current'],self.interface.lang['Invalid value'],minRef, maxRef))

    def protectionGoSet_changed(self, event):
        try:
            value= self.protectionGoSet.get()
        except:
            value=-1       
        lastValue= self.interface.mboxeGet.protectionGoSet
        minRef= self.interface.mboxeGet.protectionGoSet_ref["min"]
        maxRef= self.interface.mboxeGet.protectionGoSet_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.protectionGoSet= value
        else:
            self.protectionGoSet.set(lastValue)
            self.interface.log_print("\n%sGoSet: %s %d<>%d" % (self.interface.lang['Protection'],self.interface.lang['Invalid value'],minRef, maxRef))

    def temperatureMaxSet_changed(self, event):
        try:
            value= self.temperatureMaxSet.get()
        except:
            value=-1
        lastValue= self.interface.mboxeGet.temperatureMaxSet
        minRef= self.interface.mboxeGet.temperatureMaxSet_ref["min"]
        maxRef= self.interface.mboxeGet.temperatureMaxSet_ref["max"]
        if value>=minRef and value<=maxRef:
            self.interface.mboxeGet.temperatureMaxSet= value
        else:
            self.temperatureMaxSet.set(lastValue)
            self.interface.log_print("\n%sMaxSet: %s %d<>%d" % (self.interface.lang['Temperature'],self.interface.lang['Invalid value'],minRef, maxRef))
