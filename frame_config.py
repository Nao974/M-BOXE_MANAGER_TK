from tkinter import *

class FrameConfig(LabelFrame):

    def __init__(self, interface, **kwargs):
        LabelFrame.__init__(self, interface.windows, **kwargs)

        self.interface= interface
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.versionCode= DoubleVar()
        Label(self, text="%s : " % self.interface.lang['Firmware-Version']).grid(column=0, row=0, pady=2, padx=5, sticky=W)
        Label(self, textvariable= self.versionCode).grid(column=1, row=0, pady=2, padx=5, sticky=W)
        self.versionCode.set('')
        
        self.state= StringVar()
        Label(self, text="%s : " % self.interface.lang['State']).grid(column=0, row=1, pady=2, padx=5, sticky=W)
        Label(self, textvariable= self.state).grid(column=1, row=1, pady=2, padx=5, sticky=W)
        
        self.id= IntVar()
        id_ref= self.interface.mboxeGet.id_ref
        Label(self, text="%s : " % self.interface.lang['Ident Number']).grid(column=0, row=2, pady=2, padx=5, sticky=W)
        self.idSpin= Spinbox(self,values= [x for x in range(id_ref["min"], id_ref["max"])], textvariable= self.id, command=self.id_changed, state="readonly")
        self.idSpin.grid(column=1, row=2, pady=2, padx=5, sticky=W)
        self.id.set('')

        self.mode= IntVar()
        self.modeText= StringVar()
        mode_ref= self.interface.mboxeGet.mode_ref
        Label(self, text="%s : " % self.interface.lang['Mode']).grid(column=0, row=3, pady=2, padx=5, sticky=W)
        self.modeSpin= Spinbox(self,values= [x for x in range(mode_ref["min"], mode_ref["max"])], textvariable= self.mode, width=2, command=self.mode_changed, state="readonly")
        self.modeSpin.grid(column=1, row=3, pady=2, padx=5, sticky=W)
        self.modeLabel=Label(self, textvariable=self.modeText)
        self.modeLabel.grid(column=1, row=3, pady=2, padx=5)
        self.mode.set('')
        self.modeText.set('')
        
        self.infoConfig= StringVar()
        Label(self, text="%s : " % self.interface.lang['Info-Config']).grid(column=0, row=4, pady=2, padx=5, sticky=W)
        self.infoConfigEntry= Entry(self, textvariable= self.infoConfig, width=16, validate='focusout', vcmd=self.infoConfig_changed)
        self.infoConfigEntry.grid(column=1, row=4, pady=2, padx=5, sticky=W)

        self.skeletonPosition= StringVar()
        Label(self, text="%s : " % self.interface.lang['Skeleton-Position']).grid(column=0, row=5, pady=2, padx=5, sticky=W)
        self.skeletonPositionEntry= Entry(self, textvariable= self.skeletonPosition, width= 4, validate='focusout', vcmd=self.skeletonPosition_changed)
        self.skeletonPositionEntry.grid(column=1, row=5, pady=2, padx=5, sticky=W)

        Button(self, text="  %s  " % self.interface.lang['Get from Memory'], command=self.get_pressed).grid(column=0, row=6, padx=2, pady=5)
        Button(self, text="  %s  " % self.interface.lang['Set in Memory'], command=self.set_pressed).grid(column=1, row=6, padx=2, pady=5)

        Button(self, text="%s" % self.interface.lang['Reload from EEPROM'], command=self.reload_pressed).grid(column=0, row=7, padx=2, pady=5)
        Button(self, text="Write in EEPROM", command=self.write_pressed).grid(column=1, row=7, padx=2, pady=5)

        self.pack()

    def id_changed(self):
        value=self.id.get()
        mboxe= self.interface.mboxeGet
        if value <= mboxe.id_ref["max"] and value >= mboxe.id_ref["min"]:
            mboxe.id= value
        else:
            self.interface.log_print("\n%s: %s: %d" % (self.interface.lang['Ident Number'], self.interface.lang['Invalid value'], value))
        
    def mode_changed(self):
        value= self.mode.get()
        mboxe= self.interface.mboxeGet
        if value <= mboxe.mode_ref["max"] & value >= mboxe.mode_ref["min"]:
            mboxe.mode= value
            self.modeText.set(self.interface.mboxeGet.mode_list[value])
        else:
            self.interface.log_print("\n%s: %s" % (self.interface.lang['Mode'], self.interface.lang['Invalid value']) )
            
    def infoConfig_changed(self):
        value= self.infoConfig.get()
        size = self.interface.mboxeGet.infoConfig_ref["size"]
        if len(value) <= size:
            self.interface.mboxeGet.infoConfig= value
        else:
            self.interface.log_print("\n%s %s Max= %d char." % (self.interface.lang['Info-Config'], self.interface.lang['Size'], size) )
            self.infoConfig.set(value[:size])
            self.interface.mboxeGet.infoConfig= value[:size]
            self.infoConfigEntry.config(validate="focusout")
        return(True)

    def skeletonPosition_changed(self):
        value= self.skeletonPosition.get()
        size= self.interface.mboxeGet.skeletonPosition_ref["size"]
        if len(value) <= size:
            self.interface.mboxeGet.skeletonPosition= value
        else:
            self.interface.log_print("\n%s %s Max= %d char." % (self.interface.lang['Skeleton-Position'], self.interface.lang['Size'],size) )
            self.skeletonPosition.set(value[:size])
            self.interface.mboxeGet.skeletonPosition= value[:size]
            self.skeletonPositionEntry.config(validate="focusout")
        return(True)
        
    def update(self, mboxeGet):
        self.id.set(mboxeGet.return_id())
        self.versionCode.set(mboxeGet.return_versionCode())
        self.infoConfig.set(mboxeGet.return_infoConfig())
        self.skeletonPosition.set(mboxeGet.return_skeletonPosition())
        
        state= "0x%02X-%s" % (mboxeGet.return_state(), mboxeGet.state_list[mboxeGet.return_state()])
        self.state.set(state)
        
        self.mode.set(mboxeGet.return_mode())
        self.modeText.set(mboxeGet.mode_list[mboxeGet.return_mode()])

    def get_pressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.select_mboxe(self.interface.mboxeSelected)
        else:
            self.interface.log_print("\n%s" % self.interface.lang['Not selected Mboxe'])

    def set_pressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.mboxeGet.set()
            self.interface.log_print("\nMboxe %d: Upload config in Memory" % self.interface.mboxeSelected)
        else:
            self.interface.log_print("\n%s" % self.interface.lang['Not selected Mboxe']) 
            
    def reload_pressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.mboxeGet.cmd_eepromLoad()
            self.interface.log_print("\nMboxe %d: %s" % (self.interface.mboxeSelected, self.interface.lang['Configuration reloaded from EEPROM']) )
            self.interface.select_mboxe(self.interface.mboxeSelected)
        else:
            self.interface.log_print("\n%s" % self.interface.lang['Not selected Mboxe'])

    def write_pressed(self):
        if self.interface.mboxeSelected > 2:
            self.interface.mboxeGet.set()
            self.interface.mboxeGet.cmd_eepromSave()
            self.interface.log_print("\nMboxe %d: %s" % (self.interface.mboxeSelected, self.interface.lang['Configuration writed in EEPROM']) )
        else:
            self.interface.log_print("\n%s" % self.interface.lang['Not selected Mboxe'])
