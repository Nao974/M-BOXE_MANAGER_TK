from tkinter import *

class FrameData(LabelFrame):
    
    def __init__(self, interface, **kwargs):
        LabelFrame.__init__(self, interface.windows, **kwargs)

        self.interface= interface

        self.currentCurrent= StringVar()
        self.currentCurrent.set("%s: ? A" % self.interface.lang['Current'])
        Label(self, textvariable=self.currentCurrent).grid(column=0, row=0, pady=2, padx=5, sticky=W)        

        self.temperatureCurrent= StringVar()
        self.temperatureCurrent.set("%s: ?°C" % self.interface.lang['Temperature'])
        Label(self, textvariable=self.temperatureCurrent).grid(column=0, row=1, pady=2, padx=5, sticky=W)        

        self.protectionCurrent= StringVar()
        self.protectionCurrent.set("%s: ?"% self.interface.lang['Protection'])
        Label(self, textvariable=self.protectionCurrent).grid(column=0, row=2, pady=2, padx=5, sticky=W)        

        self.pinA2= StringVar()
        self.pinA2.set("%s A2: ?" % self.interface.lang['Pin'])
        Label(self, textvariable=self.pinA2).grid(column=2, row=0, pady=2, padx=5, sticky=W)        

        self.pinA3= StringVar()
        self.pinA3.set("%s A3: ?" % self.interface.lang['Pin'])
        Label(self, textvariable=self.pinA3).grid(column=2, row=1, pady=2, padx=5, sticky=W)        

        self.portD= StringVar()
        self.portD.set("%s D: 0 0 0 0 0 0 0 0" % self.interface.lang['Port'])
        Label(self, textvariable=self.portD).grid(column=2, row=2, pady=2, padx=5)

        self.realtime= IntVar()
        self.realtimeCB= Checkbutton(self, text="%s" % self.interface.lang['Real Time'], variable= self.realtime, command= self.realtime_changed)
        self.realtimeCB.grid(column=0, row=3, pady=2, padx=5, sticky=W)     
        self.realtime.set(0)

        self.delayRtvalueScale= IntVar()
        self.delayRtScale= Scale(self, showvalue=0,  from_=500, to=5000, resolution=100, orient=HORIZONTAL, length= 130, variable=self.delayRtvalueScale, command=self.delayRtScale_changed)
        self.delayRtScale.grid(column=2, row=3, pady=2, padx=5, sticky=W)     
        self.delayRtvalueScale.set(1000)
        self.delayRtScale.configure(state="disable")

        self.delayRtvalueEntry= IntVar()
        self.delayRtEntry= Entry(self, textvariable= self.delayRtvalueEntry, width=4)
        self.delayRtEntry.bind("<FocusOut>", self.delayRtEntry_changed)
        self.delayRtEntry.grid(column=3, row=3)
        self.delayRtEntry.configure(state="disable")
        Label(self,  text="ms").grid(column=4,row=3)  

    def realtime_changed(self):
            value= self.realtime.get()
            if value == 1:
                self.delayRtScale.configure(state="normal")
                self.delayRtEntry.configure(state="normal")
                self.interface.realtime_go()
            else:
                self.delayRtScale.configure(state="disable")
                self.delayRtEntry.configure(state="disable")
                
                

    def delayRtScale_changed(self, event):
            self.delayRtvalueEntry.set(self.delayRtvalueScale.get())

    def delayRtEntry_changed(self, event):
            self.delayRtvalueScale.set(self.delayRtvalueEntry.get())

    
    def update(self, mboxeGet):
            self.currentCurrent.set("%s: %d A" % (self.interface.lang['Current'], mboxeGet.return_currentCurrent()) )
            self.temperatureCurrent.set("%s: %.1f °C" % (self.interface.lang['Temperature'], mboxeGet.return_temperatureCurrent()) )
            if mboxeGet.return_protectionCurrent() == 0:
                self.protectionCurrent.set("%s: OK" % self.interface.lang['Protection'])
            else:
                self.protectionCurrent.set("%s:  %d" % (self.interface.lang['Fault Protection'], mboxeGet.return_protectionCurrent()) )
            self.pinA2.set("%s A2: %d" % (self.interface.lang['Pin'], mboxeGet.return_pinA2()) )
            self.pinA3.set("%s A3: %d" % (self.interface.lang['Pin'], mboxeGet.return_pinA3()) )

            portDValue = mboxeGet.return_portD()
            portDString=  ' '.join(str(1 & (portDValue) >> i) for i in range(8)[::+1])
            self.portD.set("%s D: %s" % (self.interface.lang['Port'], portDString) )

        
        
