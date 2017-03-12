# -*-coding:Utf-8 -*

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from interface import *

from lang_EN import *
from lang_FR import *

version= '1.0-2016'
lang=lang_EN
bye='N'

while bye != 'Q':
    interface= Interface(version, lang)
    interface.windows.mainloop()
    lang= interface.get_lang()
    bye= interface.get_bye()
