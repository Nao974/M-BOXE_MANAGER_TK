from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

from frame_config import *
from frame_position import *
from frame_speed import *
from frame_log import *
from frame_advanced import *
from frame_data import *
from mboxe import *

from pickle import *

from lang_EN import *
from lang_FR import *

class Interface():

    def __init__(self, version, lang):
        self.version = version
        self.mboxeSelected = -1 
        self.mboxeGet = Mboxe(self.mboxeSelected)
        self.frame_set=0
        self.lang= lang
        self.bye='N'
        
        self.windows = Tk()
        #self.windows.geometry("300x400+200+100")
        self.windows.title("Mboxe Manager v%s" % self.version)
        #self.windows.iconbitmap(...)
        self.windows.resizable(0, 0)

        self.add_frames()

        self.toolbar = Menu(self.windows)
        self.add_toolbar_filemenu()
        self.add_toolbar_mboxemenu()
        self.add_toolbar_helpmenu()       
        self.add_toolbar_langmenu()       
        self.windows.config(menu=self.toolbar)

        self.log_print("M-Boxe Manager v%s" % self.version)
        self.log_print("\nNao-Tumu Reunion Island")
        self.log_print("\n----------------------------")
        self.log_print("\nMboxe %s v%s" % (self.lang['library'], self.mboxeGet.return_vlib()) )

        self.i2c_test()
        
    def add_toolbar_filemenu(self):
        menu_file = Menu(self.toolbar, tearoff=0)
        menu_file.add_command(label=self.lang['New'], command= lambda: self.select_mboxe(0))
        menu_file.add_command(label=self.lang['Open'], command= self.load)
        menu_file.add_command(label=self.lang['Save'], command= self.save)
        menu_file.add_separator()
        menu_file.add_command(label=self.lang['Exit'], command= self.quit)
        self.toolbar.add_cascade(label=self.lang['File'], menu= menu_file)

    def add_toolbar_mboxemenu(self):
        self.menu_mboxe = Menu(self.toolbar, tearoff=0)
        self.menu_mboxe.add_command(label=self.lang['To Scan'], command= self.scan_mboxe)
        self.menu_mboxe.add_separator()         
        self.toolbar.add_cascade(label=self.lang['Mboxe'], menu= self.menu_mboxe) 

    def add_toolbar_langmenu(self):
        menu_lang = Menu(self.toolbar, tearoff=0)
        menu_lang.add_command(label=self.lang['English'], command=self.select_EN)
        menu_lang.add_command(label=self.lang['French'], command=self.select_FR)
        self.toolbar.add_cascade(label=self.lang['Language'], menu= menu_lang)
       
    def add_toolbar_helpmenu(self):
        menu_help = Menu(self.toolbar, tearoff=0)
        menu_help.add_command(label=self.lang['About'], command= self.show_about)
        self.toolbar.add_cascade(label=self.lang['Help'], menu= menu_help)

    def add_frames(self):
        if self.frame_set == 0:
            self.mainframe= FrameConfig(self, text=self.lang['Main Config'])
            self.mainframe.grid(column=0, row=0, pady=2, padx=5, sticky=NSEW) 
            self.advancedframe= FrameAdvanced(self, text=self.lang['Advanced'])
            self.advancedframe.grid(column=1, row=0, pady=2, padx=5, sticky=NSEW) 
            self.positionframe= FramePosition(self, text=self.lang['Position'])            
            self.positionframe.grid(column=0, row=1, pady=2, padx=5, sticky=NSEW) 
            self.speedframe= FrameSpeed(self, text=self.lang['Speed'])
            self.speedframe.grid(column=1, row=1, pady=2, padx=5, sticky=NSEW) 
            self.dataframe= FrameData(self, text=self.lang['Data'])
            self.dataframe.grid(column=0, row=2, pady=2, padx=5, sticky=NSEW) 
            self.logframe= FrameLog(self.windows, text=self.lang['Log'])
            self.logframe.grid(column=1, row=2, pady=2, padx=5, sticky=NSEW) 
            self.frame_set=1
       
    def log_print(self, message):
        self.logframe.print(message)
        
    def i2c_test(self):
        (version, bus)= self.mboxeGet.i2c_test()
        self.log_print("\nI2C %s v%s" % (self.lang['library'],version) )
        self.log_print("\n%s: " % self.lang['Search the I2C Bus'])        
        if bus != -1:
            self.log_print("%s %d" % (self.lang['find at bus'], bus))
        else:
            self.log_print(" %s" % self.lang['ERROR'])
            self.menu_mboxe.delete(0,128)
            self.menu_mboxe.add_command(label="NO I2C BUS")

    def scan_mboxe(self):
        self.menu_mboxe.delete(2,128)
        self.mboxe={1:0x00}
        adresse = 3
        self.log_print("\n%s" % self.lang["Launch search Mboxe"])
        while adresse <120:
            i2c = Ah_I2C( adresse )
            try:
                state= i2c.readU8_Test(0x2F)	
            except:
                pass
            else:
                self.log_print("\n   %s: %d" % (self.lang['Find Mboxe'], adresse))
                self.menu_mboxe.add_command(label="Mboxe %d" % adresse, command= lambda x=adresse: self.select_mboxe(x))
            adresse+=1
        self.log_print("\n%s" % self.lang['Close search Mboxe'])


    def select_mboxe(self, id):
        self.mboxeSelected=id
        if id==0:
            self.log_print("\n%s" % self.lang['Selection defaults'])
            self.mboxeGet = Mboxe(id)
        else:
            self.mboxeGet.get(id)
            self.log_print("\nMboxe %d: %s" % (self.mboxeSelected, self.lang['taken from the memory']))
        self.mainframe.update(self.mboxeGet)
        self.positionframe.update(self.mboxeGet)
        self.advancedframe.update(self.mboxeGet)
        self.dataframe.update(self.mboxeGet)

    def realtime_go(self):
        if self.mboxeSelected < 3:
            self.log_print("\n%s" % self.lang['Not selected Mboxe'])
            self.dataframe.realtime.set(0)
            self.dataframe.realtime_changed()
        else:
            if self.dataframe.realtime.get() == 1:
                self.mboxeGet.get_realtime()
                state= "0x%02X-%s" % (self.mboxeGet.return_state(), self.mboxeGet.state_list[self.mboxeGet.return_state()])
                self.mainframe.state.set(state)
                self.positionframe.update(self.mboxeGet)
                self.dataframe.update(self.mboxeGet)
            
                delay= self.dataframe.delayRtvalueScale.get()
                self.windows.after(delay, self.realtime_go)

    def save(self):
        dico= self.mboxeGet.saveDico()
        filename= "Mboxe%d_%s_%s" %(self.mboxeGet.id, self.mboxeGet.skeletonPosition, self.mboxeGet.infoConfig)
        for c in r'[]/\;,><&*:%=+@!#^()|?¨':
            filename= filename.replace(c,'-')
        filepath= asksaveasfilename(title="Saving in", initialfile= filename, filetypes=[('Mboxe files','.mboxe'),('All files','.*')])
        try:
            with open(filepath, 'wb') as file:
                my_pickler= Pickler(file)
                my_pickler.dump(dico)
            self.log_print("\n%: %s" % (self.lang['Saved at'], filepath))
        except:
            self.log_print("\n%s" % self.lang['Saving Canceled'])
            

    def load(self):
        filepath= askopenfilename(title="Select the file to open", filetypes=[('Mboxe files','.mboxe'),('All files','.*')])
        try:
            with open(filepath, 'rb') as file:
                my_unpickler= Unpickler(file)
                dico= my_unpickler.load()
            self.mboxeGet.loadDico(dico)
            self.log_print("\n%s: %s" % (self.lang['Loading file'], filepath))
        except:
            self.log_print("\n%s" % self.lang['Loading Canceled'])
        self.mainframe.update(self.mboxeGet)
        self.positionframe.update(self.mboxeGet)
        self.advancedframe.update(self.mboxeGet)
        self.dataframe.update(self.mboxeGet)

    def quit(self):
        if askyesno('Quit', '%s' % self.lang['Are you sure you want to quit ?']):
            self.bye='Q'
            self.windows.destroy()
            
    def select_EN(self):
        self.lang= lang_EN
        self.bye='EN'
        self.windows.destroy()
        
    def select_FR(self):
        self.lang= lang_FR
        self.bye='FR'
        self.windows.destroy()

    def show_about(self):
        showinfo(self.lang['About'], '%s %s' % (self.lang['About Text'], self.version) )

    def get_lang(self):
        return self.lang

    def get_bye(self):
        return self.bye
