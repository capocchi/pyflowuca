# -*- coding: utf-8 -*-
'''
Created on 27/05/2010

@author: Federico Cáceres <fede.caceres@gmail.com>
'''

import wx
from ui.aerowizard import AeroWizard, AeroPage
from ui.wizardpages import *

app = wx.PySimpleApp(redirect = False)

wizard = AeroWizard(u"PyFlow")
p1 = PaginaInicio(wizard, None)
p2 = PaginaCrearRed(wizard, None)
p3 = PaginaIndicarFuenteYDestino(wizard, None)
p4 = PaginaSolucion(wizard, None)
p4.is_end = True

wizard.SetStartPage(p1)
p1.Chain({"nuevo":p2})
p2.Chain({"nuevo":p3})
p3.Chain({"nuevo":p4})

ib = wx.IconBundle()
ib.AddIconFromFile("ui/img/pyflow.ico", wx.BITMAP_TYPE_ANY)
wizard.SetIcons(ib)
wizard.RunWizzard()
try:
    wizard.Destroy()
except:
    pass