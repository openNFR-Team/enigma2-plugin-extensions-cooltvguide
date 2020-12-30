# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/plugin.py
from __future__ import print_function
from __future__ import absolute_import, division
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Button import Button
from Components.config import config, ConfigSet, ConfigClock, ConfigSubsection, ConfigYesNo, ConfigInteger, ConfigSelection, getConfigListEntry
from Components.ConfigList import ConfigListScreen
from Components.GUIComponent import GUIComponent
from Components.HTMLComponent import HTMLComponent
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest, MultiContentEntryPixmapAlphaBlend
from Components.Pixmap import Pixmap
from Components.Renderer.CoolPico import findCoolPicon, CoolAlternative
from Components.ScrollLabel import ScrollLabel
from Components.ServiceEventTracker import ServiceEventTracker
from Components.Sources.Event import Event
from Components.Sources.ServiceEvent import ServiceEvent
from enigma import eTimer, eServiceCenter, eServiceReference, eEPGCache, eListbox, eListboxPythonMultiContent, ePicLoad, iPlayableService, getDesktop, gFont, loadPNG, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_VALIGN_CENTER, RT_WRAP, eRect
from Plugins.Plugin import PluginDescriptor
from RecordTimer import RecordTimerEntry, parseEvent
from Screens.ChoiceBox import ChoiceBox
from Screens.InfoBarGenerics import InfoBarPlugins, SimpleServicelist
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from Screens.TimeDateInput import TimeDateInput
from Screens.TimerEdit import TimerEditList, TimerSanityConflict
from Screens.TimerEntry import TimerEntry
from Screens.VirtualKeyBoard import VirtualKeyBoard
from ServiceReference import ServiceReference
from skin import parseColor, parseFont
from datetime import datetime, timedelta
from time import localtime, time, strftime, mktime
from Tools.Directories import fileExists, resolveFilename
from Tools.NumericalTextInput import NumericalTextInput
import NavigationInstance
import os
DCNYRvBrUl = None
nfZQJKwSrVA = None
UMUhLJhkv = None
YPbLcThQWvMcQ = False
xKmXaE = None
if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SeriesPlugin/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/SeriesPlugin/plugin.py'):
    fspOMNbuwFCWk = True
else:
    fspOMNbuwFCWk = False
if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TheTVDB/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TheTVDB/plugin.py'):
    sLpxMYXhjCROl = True
else:
    sLpxMYXhjCROl = False
if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/IMDb/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/IMDb/plugin.py'):
    bPdxaOceY = True
else:
    bPdxaOceY = False
if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TMDb/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/TMDb/plugin.py'):
    WizweESn = True
else:
    WizweESn = False
if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/OFDb/plugin.pyo') or fileExists('/usr/lib/enigma2/python/Plugins/Extensions/OFDb/plugin.py'):
    HikvfLr = True
else:
    HikvfLr = False
eFSzkTC = None
TrruhKvKi = None
FPDSuRw = None
FufElMDyUtWr = None
RxrHDyIpb = None
sNZiOf = None
vZKwD = False
PQMOk = '124'
iXZeUPZjXi = '57698'
IUqwdjkcjCMKCFO = '75242679732282'
QQdKtJPxMxJPjwB = '48035276213968'
eseWoWLtSYyCHGT = '97836241547864'
cwCvsFoxrpLR = '21012031097821'
XLeWzHuVActw = '85369741673792'
WVhkgyKgkTwui = '3271569319294719'
TOrHC = '38710248675294'
unVUjlEf = '6429532564383962'
rbAod = '54918573642583'
fPVrFQoMzxdFJY = 'V7.7.0'
Po = '\n   - - -  C o o l  T V  G u i d e  ' + fPVrFQoMzxdFJY + "  - - -\n\nIf you like this plugin and you want to support it,\nor if you just want to say ''thanks''\n\n\nplease donate via PayPal \n\nPayPal account: cooltvguide@gmail.com\n\nThanks a lot !\n\n\n\nInformation & Support: http://www.CoolTVGuide.com \n(c) 2020 by Coolman"
MxRGJuUKkDbp = '   Cool TV Guide ' + '.\n   (c) 2020 by Coolman\n\n   New Version Is Now Available ,\n   Please upgrade it at: \n\n   http://www.CoolTVGuide.com'
IJZNPmqFF = []
WnXcUAgzU = [('Zap', _('Zap')),
 ('Zap + Exit', _('Zap + Exit')),
 ('CoolSearch', _('CoolSearch')),
 ('CoolInfoBox', _('CoolInfoBox')),
 ('GuideSwitch', _('GuideSwitch')),
 ('Cool Info Guide', _('Cool Info Guide')),
 ('Timer', _('Timer')),
 ('QuickRec', _('QuickRec')),
 ('AutoTimer', _('AutoTimer')),
 ('PrimeTime', _('PrimeTime')),
 ('EPG Select', _('EPG Select')),
 ('Bouquet +', _('Bouquet +')),
 ('Bouquet -', _('Bouquet -')),
 ('Bouquetlist', _('Bouquetlist')),
 ('...', _('...'))]
XSuZfe = [('0', _('None')),
 ('1', _('Cool Info Guide')),
 ('2', _('Cool Single Guide')),
 ('3', _('Cool Easy Guide')),
 ('4', _('Cool Channel Guide')),
 ('5', _('Cool TV Guide')),
 ('6', _('Cool Tiny Guide')),
 ('7', _('Cool Multi Guide')),
 ('8', _('Cool Nice Guide')),
 ('9', _('Prime Time')),
 ('10', _('Cool Search')),
 ('11', _('Timer List'))]
config.CTVG = ConfigSubsection()
config.CTVG.C10 = ConfigSet(choices=[])
config.CTVG.C11 = ConfigYesNo(default=True)
config.CTVG.C28 = ConfigYesNo(default=True)
config.CTVG.C12 = ConfigSelection(default='EPG Select', choices=WnXcUAgzU)
config.CTVG.C13 = ConfigSelection(default='Zap + Exit', choices=WnXcUAgzU)
config.CTVG.C14 = ConfigSelection(default='Timer', choices=WnXcUAgzU)
config.CTVG.C15 = ConfigSelection(default='AutoTimer', choices=WnXcUAgzU)
config.CTVG.C16 = ConfigSelection(default='GuideSwitch', choices=WnXcUAgzU)
config.CTVG.C17 = ConfigSelection(default='Bouquetlist', choices=WnXcUAgzU)
config.CTVG.C18 = ConfigSelection(default='CoolSearch', choices=WnXcUAgzU)
config.CTVG.C19 = ConfigSelection(default='CoolInfoBox', choices=WnXcUAgzU)
config.CTVG.C20 = ConfigSelection(default='Zap', choices=WnXcUAgzU)
config.CTVG.C21 = ConfigSelection(default='...', choices=WnXcUAgzU)
config.CTVG.C22 = ConfigSelection(choices=[('1', _('Cool Info Guide')),
 ('2', _('Cool Single Guide')),
 ('3', _('Cool Easy Guide')),
 ('4', _('EPG Select')),
 ('0', _('...'))], default='1')
config.CTVG.C23 = ConfigSelection(choices=[('1', _('Cool Info Guide')),
 ('2', _('Cool Single Guide')),
 ('3', _('Cool Easy Guide')),
 ('4', _('EPG Select')),
 ('0', _('...'))], default='1')
BfYlRdlfgAhcUyy = {'C': 'if',
 'oo': 'conf',
 'l': 'ig et',
 'T': 'h0 ',
 'V': '| gr',
 'G': 'ep HW',
 'U': 'addr ',
 'I': '| awk ',
 'D': "'{ pri",
 'E': "nt $5 }'"}
config.CTVG.C24 = ConfigSelection(choices=[('1', _('Bouquet +')),
 ('2', _('Bouquet -')),
 ('3', _('Page Up')),
 ('4', _('Page Down'))], default='1')
config.CTVG.C25 = ConfigSelection(choices=[('1', _('Bouquet +')),
 ('2', _('Bouquet -')),
 ('3', _('Page Up')),
 ('4', _('Page Down'))], default='2')
config.CTVG.C26 = ConfigSelection(default=' ', choices=[' '])
config.CTVG.C27 = ConfigClock(default=time())
config.CTVG.Key = ConfigInteger(default=0, limits=(0, 99999999))
config.CTVG.C29 = ConfigSelection(choices=['No',
 'Standard',
 'SkinDesign',
 'MyDesign'], default='Standard')
config.CTVG.C30 = ConfigClock(default=69300)
config.CTVG.C31 = ConfigYesNo(default=False)
config.CTVG.C32 = ConfigYesNo(default=False)
config.CTVG.C33 = ConfigYesNo(default=False)
config.CTVG.C34 = ConfigYesNo(default=False)
config.CTVG.C35 = ConfigYesNo(default=False)
config.CTVG.C36 = ConfigYesNo(default=False)
config.CTVG.C37 = ConfigYesNo(default=True)
config.CTVG.C38 = ConfigYesNo(default=True)
config.CTVG.C39 = ConfigYesNo(default=False)
config.CTVG.C40 = ConfigInteger(default=1, limits=(1, 4))
config.CTVG.C41 = ConfigInteger(default=1, limits=(1, 4))
config.CTVG.C42 = ConfigInteger(default=1, limits=(1, 4))
config.CTVG.C43 = ConfigInteger(default=1, limits=(1, 4))
config.CTVG.C44 = ConfigInteger(default=180, limits=(60, 300))
config.CTVG.C45 = ConfigInteger(default=18, limits=(1, 50))
config.CTVG.C46 = ConfigInteger(default=18, limits=(1, 50))
config.CTVG.C47 = ConfigInteger(default=22, limits=(10, 30))
config.CTVG.C48 = ConfigInteger(default=20, limits=(10, 60))
config.CTVG.C49 = ConfigInteger(default=60, limits=(30, 80))
config.CTVG.C50 = ConfigInteger(default=60, limits=(30, 80))
config.CTVG.C51 = ConfigInteger(default=28, limits=(10, 50))
config.CTVG.C52 = ConfigInteger(default=30, limits=(10, 50))
config.CTVG.C53 = ConfigInteger(default=110, limits=(50, 250))
config.CTVG.C54 = ConfigInteger(default=55, limits=(5, 250))
config.CTVG.C55 = ConfigYesNo(default=False)
config.CTVG.C56 = ConfigYesNo(default=True)
config.CTVG.C57 = ConfigYesNo(default=False)
config.CTVG.C58 = ConfigYesNo(default=True)
config.CTVG.C60 = ConfigYesNo(default=False)
config.CTVG.C61 = ConfigYesNo(default=False)
config.CTVG.C62 = ConfigYesNo(default=True)
config.CTVG.C63 = ConfigYesNo(default=True)
zUIfAWMBbQJ = config.CTVG.Key.value
config.CTVG.C77 = ConfigSelection(default='1', choices=XSuZfe)
config.CTVG.C78 = ConfigSelection(default='2', choices=XSuZfe)
config.CTVG.C79 = ConfigSelection(default='3', choices=XSuZfe)
config.CTVG.C80 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C81 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C82 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C83 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C84 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C85 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C86 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C87 = ConfigSelection(default='0', choices=XSuZfe)
config.CTVG.C88 = ConfigSelection(default='0', choices=XSuZfe)
WmXVqUV = 1

class PEwinOgXknkdV():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def left(self):
        return self.x

    def top(self):
        return self.y

    def height(self):
        return self.h

    def width(self):
        return self.w


class FaghDMgGyKw(HTMLComponent, GUIComponent):

    def __init__(self):
        GUIComponent.__init__(self)
        self.l = eListboxPythonMultiContent()
        self.l.setSelectionClip(eRect(0, 0, 0, 0))
        self.l.setItemHeight(25)
        self.l.setFont(0, gFont('Regular', config.CTVG.C48.value))

    GUI_WIDGET = eListbox

    def postWidgetCreate(self, instance):
        instance.setContent(self.l)

    def vyiRYEzcvWSVxm(self, PRTmQUczh):
        res = [None]
        for x in PRTmQUczh:
            tm = x[0]
            TvHugmr = x[1]
            str = strftime('%H:%M', localtime(tm))
            res.append((eListboxPythonMultiContent.TYPE_TEXT,
             TvHugmr - 5,
             0,
             300,
             25,
             0,
             RT_HALIGN_LEFT | RT_VALIGN_CENTER,
             str))

        self.l.setList([res])
        return


TMvKPeMEZHVqV = getDesktop(0).size().width()

class zDKhcfAp(Screen):

    def __init__(self, session, ivsBFJkimXjpdOa = None, Ref = None, UMUhLJhkv = None, TrruhKvKi = None, gggJixxXg = None, nfZQJKwSrVA = None, PwRojNX = None):
        global DCNYRvBrUl
        Screen.__init__(self, session)
        if TMvKPeMEZHVqV == 720:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_720.xml'
            elif PwRojNX == iXZeUPZjXi:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_720.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_720.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_720.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_720.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_720.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_720.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_720.xml'
        elif TMvKPeMEZHVqV == 1024:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1024.xml'
            elif PwRojNX == iXZeUPZjXi:
                if config.CTVG.C43.value == 1:
                    self.skinName = 'CoolSingleGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1024.xml'
                elif config.CTVG.C43.value == 2:
                    self.skinName = 'CoolSingleGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1024.xml'
                elif config.CTVG.C43.value == 3:
                    self.skinName = 'CoolSingleGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1024.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                if config.CTVG.C42.value == 1:
                    self.skinName = 'CoolEasyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1024.xml'
                elif config.CTVG.C42.value == 2:
                    self.skinName = 'CoolEasyGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1024.xml'
                elif config.CTVG.C42.value == 3:
                    self.skinName = 'CoolEasyGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1024.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                if config.CTVG.C41.value == 1:
                    self.skinName = 'CoolChannelGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1024.xml'
                elif config.CTVG.C41.value == 2:
                    self.skinName = 'CoolChannelGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1024.xml'
                elif config.CTVG.C41.value == 3:
                    self.skinName = 'CoolChannelGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1024.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1024.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1024.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1024.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1024.xml'
        elif PwRojNX == PQMOk:
            self.skinName = 'CoolInfoGuide'
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1280.xml'
        elif PwRojNX == iXZeUPZjXi:
            if config.CTVG.C43.value == 1:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1280.xml'
            elif config.CTVG.C43.value == 2:
                self.skinName = 'CoolSingleGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1280.xml'
            elif config.CTVG.C43.value == 3:
                self.skinName = 'CoolSingleGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1280.xml'
        elif PwRojNX == IUqwdjkcjCMKCFO:
            if config.CTVG.C42.value == 1:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1280.xml'
            elif config.CTVG.C42.value == 2:
                self.skinName = 'CoolEasyGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1280.xml'
            elif config.CTVG.C42.value == 3:
                self.skinName = 'CoolEasyGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1280.xml'
        elif PwRojNX == QQdKtJPxMxJPjwB:
            if config.CTVG.C41.value == 1:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1280.xml'
            elif config.CTVG.C41.value == 2:
                self.skinName = 'CoolChannelGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1280.xml'
            elif config.CTVG.C41.value == 3:
                self.skinName = 'CoolChannelGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1280.xml'
        elif PwRojNX == eseWoWLtSYyCHGT:
            if config.CTVG.C40.value == 1:
                self.skinName = 'CoolTVGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1280.xml'
            elif config.CTVG.C40.value == 2:
                self.skinName = 'CoolTinyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1280.xml'
            elif config.CTVG.C40.value == 3:
                self.skinName = 'CoolMultiGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1280.xml'
            elif config.CTVG.C40.value == 4:
                self.skinName = 'CoolNiceGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1280.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self.NFVzxMfxEUu = zUIfAWMBbQJ
        self.nfZQJKwSrVA = nfZQJKwSrVA
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.vzDGDGAQLSCa = -1
        self.FUiTqUurDFxy = False
        self.cIKHf = None
        self['Service'] = ServiceEvent()
        self['Event'] = Event()
        if ivsBFJkimXjpdOa:
            self['Event'].newEvent(ivsBFJkimXjpdOa)
            DCNYRvBrUl = ivsBFJkimXjpdOa.getEventId()
        self['CoolSimilar'] = ScrollLabel()
        self['CoolDescription'] = ScrollLabel()
        self['CoolShort'] = ScrollLabel()
        self['date'] = Button()
        self['key_red'] = Button('')
        self['key_green'] = Button('')
        self['key_yellow'] = Button('')
        self['key_blue'] = Button('')
        self.XISehjxsPoi = ServiceReference(UMUhLJhkv)
        self.upGCWEDZc = eTimer()
        self.upGCWEDZc.callback.append(self.tSyelUhLZidjaH)
        self['CoolEvent'] = TyJjFMDpxnnJch(pOHOrwCihqC=self.WlFKMlyFxSWrG, QHYMHhwOVIXtLT=session.nav.RecordTimer)
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolPower': self.EUtMyA,
         'CoolUP': self.FoAOKEnbKrBbOMK,
         'CoolDown': self.zjwBRbR,
         'CoolLEFT': self.GdjxEetRD,
         'CoolRIGHT': self.Krkrxa,
         'CoolChannelUP': self.nCbsAJiEfEB,
         'CoolChannelDown': self.qoiUQ,
         'CoolNEXT': self.ckJPPSTaPu,
         'CoolPREVIOUS': self.YzrxgfKwCwLOlLS,
         'CoolMenu': self.NuGwC,
         'CoolRed': self.GwhJbNuquP,
         'CoolRedLong': self.fbUws,
         'CoolGreen': self.gXppchsrp,
         'CoolGreenLong': self.mzzBQRAohy,
         'CoolYellow': self.bKpKe,
         'CoolYellowLong': self.qOlhOHWiFHpIC,
         'CoolBlue': self.qsDCwRsYOveEFy,
         'CoolBlueLong': self.uHqjdBJMLj,
         'CoolOK': self.WhRkmBFDyxfV,
         'CoolCancel': self.YxuwUrC,
         'CoolInfo': self.NxrXAek,
         'CoolInfoLong': self.uWIjFbGhtX,
         'CoolRecord': self.esPNG,
         'CoolVIDEO': nePylQgKlghpaVP,
         'CoolAUDIO': self.BvRoHaxNcu,
         'CoolKeyTV': self.EekrcnjXd,
         '0': self.vUTsitGJjtQeKWg,
         '7': self.TdjjCghHcsK,
         '8': self.neDLkklkP,
         '9': self.eKXjhOLrwzFbS}, -1)
        self.SuVhHLBrOFx = config.CTVG.C12.value
        self.jIDDtifEzLAQAtH = config.CTVG.C14.value
        self.KhCcbywN = config.CTVG.C16.value
        self.gYtswyvbtJ = config.CTVG.C18.value
        if self.SuVhHLBrOFx == 'PrimeTime' or self.SuVhHLBrOFx == 'Bouquet +' or self.SuVhHLBrOFx == 'Bouquet -' or self.SuVhHLBrOFx == 'Bouquetlist':
            self.SuVhHLBrOFx = 'EPG Select'
        if self.jIDDtifEzLAQAtH == 'PrimeTime' or self.jIDDtifEzLAQAtH == 'Bouquet +' or self.jIDDtifEzLAQAtH == 'Bouquet -' or self.jIDDtifEzLAQAtH == 'Bouquetlist':
            self.jIDDtifEzLAQAtH = 'Timer'
        if self.KhCcbywN == 'PrimeTime' or self.KhCcbywN == 'Bouquet +' or self.KhCcbywN == 'Bouquet -' or self.KhCcbywN == 'Bouquetlist':
            self.KhCcbywN = 'GuideSwitch'
        if self.gYtswyvbtJ == 'PrimeTime' or self.gYtswyvbtJ == 'Bouquet +' or self.gYtswyvbtJ == 'Bouquet -' or self.gYtswyvbtJ == 'Bouquetlist':
            self.gYtswyvbtJ = 'CoolSearch'
        self['key_red'].setText(_(self.SuVhHLBrOFx))
        self['key_green'].setText(_(self.jIDDtifEzLAQAtH))
        self['key_yellow'].setText(_(self.KhCcbywN))
        self['key_blue'].setText(_(self.gYtswyvbtJ))
        self.onLayoutFinish.append(self.NbmZQLxewbo)
        self.rWlyLcEBtxYhLAf()
        return

    def qFDSvr(self):
        global WmXVqUV
        if WmXVqUV == 1:
            x = config.CTVG.C77.value
        elif WmXVqUV == 2:
            x = config.CTVG.C78.value
        elif WmXVqUV == 3:
            x = config.CTVG.C79.value
        elif WmXVqUV == 4:
            if WvYVaQ != self.NFVzxMfxEUu and SAQsYCIeDb != self.NFVzxMfxEUu:
                WmXVqUV = 1
                return self.close(False)
            x = config.CTVG.C80.value
        elif WmXVqUV == 5:
            x = config.CTVG.C81.value
        elif WmXVqUV == 6:
            x = config.CTVG.C82.value
        elif WmXVqUV == 7:
            x = config.CTVG.C83.value
        elif WmXVqUV == 8:
            x = config.CTVG.C84.value
        elif WmXVqUV == 9:
            x = config.CTVG.C85.value
        elif WmXVqUV == 10:
            x = config.CTVG.C86.value
        elif WmXVqUV == 11:
            x = config.CTVG.C87.value
        elif WmXVqUV == 12:
            x = config.CTVG.C88.value
        if x == '9':
            WmXVqUV += 1
            return self.qFDSvr()
        self.hide()
        if x == '1':
            WmXVqUV += 1
            return self.qFDSvr()
        if x == '2':
            self.RDSJwxPYCfBLVaN()
        elif x == '3':
            CEGmain(self.session)
        elif x == '4':
            CCGmain(self.session)
        elif x == '5':
            config.CTVG.C40.value = 1
            main(self.session)
        elif x == '6':
            config.CTVG.C40.value = 2
            main(self.session)
        elif x == '7':
            config.CTVG.C40.value = 3
            main(self.session)
        elif x == '8':
            config.CTVG.C40.value = 4
            main(self.session)
        elif x == '10':
            self.sSPMBhwDflASCMt()
        elif x == '11':
            WmXVqUV = 0
            self.session.open(TimerEditList)
        else:
            WmXVqUV = 0
        WmXVqUV += 1
        self.close(False)

    def rWlyLcEBtxYhLAf(self):
        geikSRpcvam = localtime()
        if (geikSRpcvam.tm_year, geikSRpcvam.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2])):
            self.YxuwUrC()

    def changeServiceCB(self, SqpegV, epg):
        if self.serviceSel:
            if SqpegV > 0:
                self.serviceSel.nextService()
            else:
                self.serviceSel.prevService()
            epg.setService(self.serviceSel.currentService())

    def vUTsitGJjtQeKWg(self):
        try:
            self.hide()
            CIGmain(self.session)
            self.YxuwUrC()
        except:
            self.YxuwUrC()

    def RHRYk(self):
        self.hide()
        main(self.session)
        self.YxuwUrC()

    def BvRoHaxNcu(self):
        self.hide()
        CEGmain(self.session)
        self.YxuwUrC()

    def RDSJwxPYCfBLVaN(self):
        global TrruhKvKi
        tfonHdIjfgQ = self['CoolEvent'].JvSwzXgDeSH()
        if tfonHdIjfgQ[1] is None:
            return
        else:
            TFekBZfhstWiyNH = tfonHdIjfgQ[1].ref
            if TFekBZfhstWiyNH:
                if TrruhKvKi:
                    gGPiwVmWkgM = TrruhKvKi.getRoot()
                    ZnHPgSvmg = getBouquetServices(gGPiwVmWkgM)
                    self.serviceSel = SimpleServicelist(ZnHPgSvmg)
                    if self.serviceSel.selectService(TFekBZfhstWiyNH):
                        self.hide()
                        self.session.open(XEArkQXQCQRMEL, TFekBZfhstWiyNH, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=iXZeUPZjXi)
            self.YxuwUrC()
            return

    def EUtMyA(self):
        try:
            from Screens.SleepTimerEdit import SleepTimerEdit
            self.session.open(SleepTimerEdit)
        except:
            pass

    def GwhJbNuquP(self):
        EcLNwIhunJbRsLQ = self.SuVhHLBrOFx
        if EcLNwIhunJbRsLQ == 'EPG Select':
            self.qFDSvr()
        elif EcLNwIhunJbRsLQ == 'Zap':
            self.nORxTbRjzsNVch()
        elif EcLNwIhunJbRsLQ == 'Zap + Exit':
            self.JIQKwPOcc()
        elif EcLNwIhunJbRsLQ == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif EcLNwIhunJbRsLQ == 'CoolInfoBox':
            self.fxVcQUikA()
        elif EcLNwIhunJbRsLQ == 'GuideSwitch':
            self.RHRYk()
        elif EcLNwIhunJbRsLQ == 'Timer':
            self.EmOZX()
        elif EcLNwIhunJbRsLQ == 'QuickRec':
            self.esPNG()
        elif EcLNwIhunJbRsLQ == 'AutoTimer':
            self.voLEWybvGX()
        else:
            self.qFDSvr()

    def fbUws(self):
        aFfcKSkBDKNWm = config.CTVG.C13.value
        if aFfcKSkBDKNWm == 'Zap':
            self.nORxTbRjzsNVch()
        elif aFfcKSkBDKNWm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif aFfcKSkBDKNWm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif aFfcKSkBDKNWm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif aFfcKSkBDKNWm == 'GuideSwitch':
            self.RHRYk()
        elif aFfcKSkBDKNWm == 'Timer':
            self.EmOZX()
        elif aFfcKSkBDKNWm == 'QuickRec':
            self.esPNG()
        elif aFfcKSkBDKNWm == 'AutoTimer':
            self.voLEWybvGX()
        elif aFfcKSkBDKNWm == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def gXppchsrp(self):
        fCsivhkbczcm = self.jIDDtifEzLAQAtH
        if fCsivhkbczcm == 'Zap':
            self.nORxTbRjzsNVch()
        elif fCsivhkbczcm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif fCsivhkbczcm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif fCsivhkbczcm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif fCsivhkbczcm == 'GuideSwitch':
            self.RHRYk()
        elif fCsivhkbczcm == 'Timer':
            self.EmOZX()
        elif fCsivhkbczcm == 'QuickRec':
            self.esPNG()
        elif fCsivhkbczcm == 'AutoTimer':
            self.voLEWybvGX()
        elif fCsivhkbczcm == 'EPG Select':
            self.qFDSvr()
        else:
            self.EmOZX()

    def mzzBQRAohy(self):
        CALICbGXK = config.CTVG.C15.value
        if CALICbGXK == 'Zap':
            self.nORxTbRjzsNVch()
        elif CALICbGXK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif CALICbGXK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif CALICbGXK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif CALICbGXK == 'GuideSwitch':
            self.RHRYk()
        elif CALICbGXK == 'Timer':
            self.EmOZX()
        elif CALICbGXK == 'QuickRec':
            self.esPNG()
        elif CALICbGXK == 'AutoTimer':
            self.voLEWybvGX()
        elif CALICbGXK == 'EPG Select':
            self.qFDSvr()
        else:
            self.voLEWybvGX()

    def bKpKe(self):
        BCGuXefsvjf = self.KhCcbywN
        if BCGuXefsvjf == 'Zap':
            self.nORxTbRjzsNVch()
        elif BCGuXefsvjf == 'Zap + Exit':
            self.JIQKwPOcc()
        elif BCGuXefsvjf == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif BCGuXefsvjf == 'CoolInfoBox':
            self.fxVcQUikA()
        elif BCGuXefsvjf == 'GuideSwitch':
            self.RHRYk()
        elif BCGuXefsvjf == 'Timer':
            self.EmOZX()
        elif BCGuXefsvjf == 'QuickRec':
            self.esPNG()
        elif BCGuXefsvjf == 'AutoTimer':
            self.voLEWybvGX()
        elif BCGuXefsvjf == 'EPG Select':
            self.qFDSvr()
        else:
            self.RHRYk()

    def qOlhOHWiFHpIC(self):
        gRpGhRQrF = config.CTVG.C17.value
        if gRpGhRQrF == 'Zap':
            self.nORxTbRjzsNVch()
        elif gRpGhRQrF == 'Zap + Exit':
            self.JIQKwPOcc()
        elif gRpGhRQrF == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif gRpGhRQrF == 'CoolInfoBox':
            self.fxVcQUikA()
        elif gRpGhRQrF == 'GuideSwitch':
            self.RHRYk()
        elif gRpGhRQrF == 'Timer':
            self.EmOZX()
        elif gRpGhRQrF == 'QuickRec':
            self.esPNG()
        elif gRpGhRQrF == 'AutoTimer':
            self.voLEWybvGX()
        elif gRpGhRQrF == 'EPG Select':
            self.qFDSvr()
        else:
            self.fxVcQUikA()

    def qsDCwRsYOveEFy(self):
        LnElTGKJP = config.CTVG.C18.value
        if LnElTGKJP == 'Zap':
            self.nORxTbRjzsNVch()
        elif LnElTGKJP == 'Zap + Exit':
            self.JIQKwPOcc()
        elif LnElTGKJP == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif LnElTGKJP == 'CoolInfoBox':
            self.fxVcQUikA()
        elif LnElTGKJP == 'GuideSwitch':
            self.RHRYk()
        elif LnElTGKJP == 'Timer':
            self.EmOZX()
        elif LnElTGKJP == 'QuickRec':
            self.esPNG()
        elif LnElTGKJP == 'AutoTimer':
            self.voLEWybvGX()
        elif LnElTGKJP == 'EPG Select':
            self.qFDSvr()
        else:
            self.sSPMBhwDflASCMt()

    def uHqjdBJMLj(self):
        UQcfkjKQK = config.CTVG.C19.value
        if UQcfkjKQK == 'Zap':
            self.nORxTbRjzsNVch()
        elif UQcfkjKQK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif UQcfkjKQK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif UQcfkjKQK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif UQcfkjKQK == 'GuideSwitch':
            self.RHRYk()
        elif UQcfkjKQK == 'Timer':
            self.EmOZX()
        elif UQcfkjKQK == 'QuickRec':
            self.esPNG()
        elif UQcfkjKQK == 'AutoTimer':
            self.voLEWybvGX()
        elif UQcfkjKQK == 'EPG Select':
            self.qFDSvr()
        else:
            self.fxVcQUikA()

    def WhRkmBFDyxfV(self):
        mmADTJNSFBqozS = config.CTVG.C20.value
        if mmADTJNSFBqozS == 'Zap':
            self.nORxTbRjzsNVch()
        elif mmADTJNSFBqozS == 'Zap + Exit':
            self.JIQKwPOcc()
        elif mmADTJNSFBqozS == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif mmADTJNSFBqozS == 'CoolInfoBox':
            self.fxVcQUikA()
        elif mmADTJNSFBqozS == 'GuideSwitch':
            self.RHRYk()
        elif mmADTJNSFBqozS == 'Timer':
            self.EmOZX()
        elif mmADTJNSFBqozS == 'QuickRec':
            self.esPNG()
        elif mmADTJNSFBqozS == 'AutoTimer':
            self.voLEWybvGX()
        elif mmADTJNSFBqozS == 'EPG Select':
            self.qFDSvr()
        else:
            self.YxuwUrC()

    def NxrXAek(self):
        OCCKSDwCPbq = config.CTVG.C22.value
        if OCCKSDwCPbq == '4':
            self.qFDSvr()
        elif OCCKSDwCPbq == '2':
            self.RDSJwxPYCfBLVaN()
        elif OCCKSDwCPbq == '3':
            self.BvRoHaxNcu()
        else:
            self.YxuwUrC()

    def uWIjFbGhtX(self):
        OCCKSDwCPbq = config.CTVG.C23.value
        if OCCKSDwCPbq == '4':
            self.qFDSvr()
        elif OCCKSDwCPbq == '2':
            self.RDSJwxPYCfBLVaN()
        elif OCCKSDwCPbq == '3':
            self.BvRoHaxNcu()
        else:
            self.YxuwUrC()

    def FoAOKEnbKrBbOMK(self):
        self['CoolSimilar'].pageUp()
        self['CoolDescription'].pageUp()
        self['CoolShort'].pageUp()

    def zjwBRbR(self):
        self['CoolSimilar'].pageDown()
        self['CoolDescription'].pageDown()
        self['CoolShort'].pageDown()

    def GdjxEetRD(self):
        self['CoolEvent'].GdjxEetRD()
        self.QoGRewjlErZRq()

    def Krkrxa(self):
        self['CoolEvent'].Krkrxa()
        self.QoGRewjlErZRq()

    def nCbsAJiEfEB(self):
        self.ckJPPSTaPu()
        self.nORxTbRjzsNVch()

    def qoiUQ(self):
        self.YzrxgfKwCwLOlLS()
        self.nORxTbRjzsNVch()

    def ckJPPSTaPu(self):
        if self.nfZQJKwSrVA:
            self.nfZQJKwSrVA(1, self)

    def YzrxgfKwCwLOlLS(self):
        if self.nfZQJKwSrVA:
            self.nfZQJKwSrVA(-1, self)

    def TdjjCghHcsK(self):
        self.RHRYk()

    def neDLkklkP(self):
        self.RDSJwxPYCfBLVaN()

    def eKXjhOLrwzFbS(self):
        self.BvRoHaxNcu()

    def NbmZQLxewbo(self):
        LjgPsdVwwQ = self.XISehjxsPoi
        self.QoGRewjlErZRq()
        if self.cIKHf is None:
            self.cIKHf = self.instance.getTitle()
        title = self.cIKHf + ' - ' + LjgPsdVwwQ.getServiceName()
        self.instance.setTitle(title)
        self['CoolEvent'].pTTZqyXtEbFRSig(LjgPsdVwwQ)
        return

    def YxuwUrC(self):
        global dHsyDiE
        global WmXVqUV
        WmXVqUV = 1
        dHsyDiE = self['CoolEvent'].aMrVMukygNMxHdl()
        self.close(self.FUiTqUurDFxy)

    def setService(self, UMUhLJhkv):
        self.XISehjxsPoi = UMUhLJhkv
        self.NbmZQLxewbo()

    def qFLoYuYRPQFdK(self, qDFTEDFxno):
        self.RhAgxPmgsq = qDFTEDFxno
        self.NbmZQLxewbo()

    def tSyelUhLZidjaH(self):
        bJKvGIVemCb = self['CoolEvent'].JvSwzXgDeSH()
        XPAUhmXffAhD = bJKvGIVemCb[0]
        if not XPAUhmXffAhD:
            self['CoolShort'].setText('--- No EPG Data ---')
            self['CoolDescription'].setText('')
            return
        else:
            self['CoolDescription'].setText(XPAUhmXffAhD.getExtendedDescription())
            ilGQEEnSuF = XPAUhmXffAhD.getShortDescription()
            if ilGQEEnSuF == '':
                self['CoolShort'].setText(XPAUhmXffAhD.getEventName())
            else:
                self['CoolShort'].setText(ilGQEEnSuF)
            YJtIpOkBKsCcvSg = bJKvGIVemCb[1]
            fXYLLkn = YJtIpOkBKsCcvSg.ref.toString()
            GIQnGsEa = XPAUhmXffAhD.getEventId()
            DTzDLYhRge = eEPGCache.getInstance()
            vMbOnIO = DTzDLYhRge.search(('NB',
             100,
             eEPGCache.SIMILAR_BROADCASTINGS_SEARCH,
             fXYLLkn,
             GIQnGsEa))
            if vMbOnIO is not None:
                oPDKlR = self['CoolSimilar']
                qputw = oPDKlR.getText()
                vMbOnIO.sort(self.kufFmB)
                for x in vMbOnIO:
                    AHGFnEkQQLedLjO = localtime(x[1])
                    hdAYuconaNioaS = ''
                    if AHGFnEkQQLedLjO.tm_wday == 0:
                        hdAYuconaNioaS = _('Mon')
                    elif AHGFnEkQQLedLjO.tm_wday == 1:
                        hdAYuconaNioaS = _('Tue')
                    elif AHGFnEkQQLedLjO.tm_wday == 2:
                        hdAYuconaNioaS = _('Wed')
                    elif AHGFnEkQQLedLjO.tm_wday == 3:
                        hdAYuconaNioaS = _('Thu')
                    elif AHGFnEkQQLedLjO.tm_wday == 4:
                        hdAYuconaNioaS = _('Fri')
                    elif AHGFnEkQQLedLjO.tm_wday == 5:
                        hdAYuconaNioaS = _('Sat')
                    elif AHGFnEkQQLedLjO.tm_wday == 6:
                        hdAYuconaNioaS = _('Sun')
                    qputw += '%s  %02d:%02d   %s\n' % (hdAYuconaNioaS,
                     AHGFnEkQQLedLjO[3],
                     AHGFnEkQQLedLjO[4],
                     x[0])

                oPDKlR.setText(qputw)
            return

    def kufFmB(self, x, y):
        if x[1] < y[1]:
            return -1
        elif x[1] == y[1]:
            return 0
        else:
            return 1

    def fxVcQUikA(self):
        UFXUK = []
        if fspOMNbuwFCWk:
            UFXUK.append((_('SeriesPlugin'), 'SeriesPlugin'))
        if sLpxMYXhjCROl:
            UFXUK.append((_('The TVDB Info'), 'The TVDB Info'))
        if bPdxaOceY:
            UFXUK.append((_('IMDb Search'), 'IMDbSearch'))
        if WizweESn:
            UFXUK.append((_('TMDB Info'), 'TMDBInfo'))
        if HikvfLr:
            UFXUK.append((_('OFDb Details'), 'OFDbDetails'))
        if UFXUK == []:
            UFXUK.append((_('No Info Plugins installed...'), 'No Info Plugins installed...'))
        self.session.openWithCallback(self.tmxBeAld, ChoiceBox, title=_('   CoolInfoBox'), list=UFXUK)

    def tmxBeAld(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        SNAVqJygcUu = self['CoolEvent'].JvSwzXgDeSH()
        NKLQToYjM = SNAVqJygcUu[0]
        if not NKLQToYjM:
            return
        name = NKLQToYjM and NKLQToYjM.getEventName() or ''
        if nKGKSPXPp == 'SeriesPlugin':
            from Plugins.Extensions.SeriesPlugin.SeriesPluginInfoScreen import SeriesPluginInfoScreen
            UMUhLJhkv = SNAVqJygcUu[1]
            self.session.open(SeriesPluginInfoScreen, UMUhLJhkv, NKLQToYjM)
        if nKGKSPXPp == 'The TVDB Info':
            from Plugins.Extensions.TheTVDB.plugin import TheTVDBMain
            self.session.open(TheTVDBMain, name)
        if nKGKSPXPp == 'IMDbSearch':
            from Plugins.Extensions.IMDb.plugin import IMDB
            self.session.open(IMDB, name)
        if nKGKSPXPp == 'TMDBInfo':
            from Plugins.Extensions.TMDb.plugin import TMDbMain
            self.session.open(TMDbMain, name)
        if nKGKSPXPp == 'OFDbDetails':
            from Plugins.Extensions.OFDb.plugin import OFDB
            self.session.open(OFDB, name)

    def QoGRewjlErZRq(self):
        qputw = ''
        self['CoolSimilar'].setText(qputw)
        if self.upGCWEDZc is not None:
            self.upGCWEDZc.start(400, True)
        EnFKRmiyy = self['CoolEvent'].JvSwzXgDeSH()
        ERoOCCVi = EnFKRmiyy[0]
        if not ERoOCCVi:
            return
        else:
            ilGQEEnSuF = ERoOCCVi.getShortDescription()
            if ilGQEEnSuF == '':
                self['CoolShort'].setText(ERoOCCVi.getEventName())
            else:
                self['CoolShort'].setText(ilGQEEnSuF)
            self['CoolDescription'].setText(ERoOCCVi.getExtendedDescription())
            return

    def sSPMBhwDflASCMt(self):
        try:
            OiTUjyeSoZRNG = self['CoolEvent'].JvSwzXgDeSH()
            ERoOCCVi = OiTUjyeSoZRNG[0]
            if not ERoOCCVi:
                return
            ahapbKsuaGHjMfb = ERoOCCVi.getEventName() or ''
        except:
            ahapbKsuaGHjMfb = ''

        self.session.open(lyqBhZ, ahapbKsuaGHjMfb, False)

    def voLEWybvGX(self):
        zjRLCa = self['CoolEvent'].JvSwzXgDeSH()
        if not zjRLCa:
            return
        try:
            from Plugins.Extensions.AutoTimer.AutoTimerEditor import addAutotimerFromEvent
            self.session.openWithCallback(self.aqFgBg, ChoiceBox, title=_('   check Autotimer ?'), list=[(_('Yes'), 'Yes'), (_('No'), 'No')])
            addAutotimerFromEvent(self.session, zjRLCa[0], zjRLCa[1])
        except:
            self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def aqFgBg(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        if nKGKSPXPp == 'Yes':
            try:
                from Plugins.Extensions.AutoTimer.plugin import main as AutoTimerSafe
                AutoTimerSafe(self.session)
            except:
                self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def esPNG(self):
        OXeXRlHHxgjsyrP = self['CoolEvent'].JvSwzXgDeSH()
        qjCtcNsozE = OXeXRlHHxgjsyrP[1]
        RzWaGVeLcKz = OXeXRlHHxgjsyrP[0]
        if not RzWaGVeLcKz:
            return
        else:
            FZxOvzpGBD = RzWaGVeLcKz.getEventId()
            cFGxuHheCNQgfnT = qjCtcNsozE.ref.toString()
            for OXeXRlHHxgjsyrP in self.session.nav.RecordTimer.timer_list:
                if OXeXRlHHxgjsyrP.eit == FZxOvzpGBD and OXeXRlHHxgjsyrP.service_ref.ref.toString() == cFGxuHheCNQgfnT:
                    self.session.nav.RecordTimer.removeEntry(OXeXRlHHxgjsyrP)
                    self['CoolEvent'].l.invalidate()
                    break
            else:
                ZFcHE = RecordTimerEntry(qjCtcNsozE, checkOldTimers=True, *parseEvent(RzWaGVeLcKz))
                BjDtxuaz = NavigationInstance.instance.RecordTimer.record(ZFcHE)
                if BjDtxuaz is not None:
                    for OXeXRlHHxgjsyrP in BjDtxuaz:
                        if OXeXRlHHxgjsyrP.setAutoincreaseEnd(ZFcHE):
                            self.session.nav.RecordTimer.timeChanged(OXeXRlHHxgjsyrP)

                    BjDtxuaz = self.session.nav.RecordTimer.record(ZFcHE)
                    if BjDtxuaz is not None:
                        self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, BjDtxuaz)
                self['CoolEvent'].l.invalidate()

            self.WlFKMlyFxSWrG()
            return

    def WlFKMlyFxSWrG(self):
        fzPWRjmyFOdPgK = self['CoolEvent'].JvSwzXgDeSH()
        ERoOCCVi = fzPWRjmyFOdPgK[0]
        self['Event'].newEvent(ERoOCCVi)
        yyJciFsdx = ''
        if ERoOCCVi is not None:
            geikSRpcvam = time()
            cpUukOBh = ERoOCCVi.getBeginTime()
            rbuTrfjskKNUrpX = localtime(geikSRpcvam)
            xCcvK = localtime(cpUukOBh)
            if rbuTrfjskKNUrpX[2] != xCcvK[2]:
                yyJciFsdx = '%s %d.%d.' % (self.PsMWO[xCcvK[6]], xCcvK[2], xCcvK[1])
            else:
                yyJciFsdx = '%s %d.%d.' % (_('Today'), xCcvK[2], xCcvK[1])
        self['date'].setText(yyJciFsdx)
        if fzPWRjmyFOdPgK[1] is None:
            self['Service'].newService(None)
        else:
            self['Service'].newService(fzPWRjmyFOdPgK[1].ref)
        if not ERoOCCVi:
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText('')
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText('')
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText('')
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText('')
            return
        else:
            yKXJcdzyXcatuHl = fzPWRjmyFOdPgK[1]
            FZxOvzpGBD = ERoOCCVi.getEventId()
            HbpXmGWCEHTK = yKXJcdzyXcatuHl.ref.toString()
            xCEOmOL = False
            for yKXJcdzyXcatuHl in self.session.nav.RecordTimer.timer_list:
                if yKXJcdzyXcatuHl.eit == FZxOvzpGBD and yKXJcdzyXcatuHl.service_ref.ref.toString() == HbpXmGWCEHTK:
                    xCEOmOL = True
                    break

            if xCEOmOL:
                if self.jIDDtifEzLAQAtH == 'Timer':
                    self['key_green'].setText(_('TimerEdit'))
                elif self.SuVhHLBrOFx == 'Timer':
                    self['key_red'].setText(_('TimerEdit'))
                elif self.KhCcbywN == 'Timer':
                    self['key_yellow'].setText(_('TimerEdit'))
                elif self.gYtswyvbtJ == 'Timer':
                    self['key_blue'].setText(_('TimerEdit'))
            elif self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('Timer'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('Timer'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('Timer'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('Timer'))
            return

    def EekrcnjXd(self):
        self.session.open(TimerEditList)

    def EmOZX(self):
        fzPWRjmyFOdPgK = self['CoolEvent'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        sTgNxkmJlcmVCv = fzPWRjmyFOdPgK[1]
        if not lWJAurf:
            return
        FZxOvzpGBD = lWJAurf.getEventId()
        fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
        for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
            if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
                self.session.openWithCallback(self.pwCaxqRZQsvS, ChoiceBox, title=_('Cool Timer Edit :' + '\n\n%s') % lWJAurf.getEventName(), list=[(_('edit this Timer ?'), 'edit'), (_('delete this Timer ?'), 'delete'), (_('delete this Timer and recording ?'), 'delrec')])
                break
        else:
            ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(lWJAurf))
            self.session.openWithCallback(self.SohIHVvAMnbAXX, TimerEntry, ZFcHE)

    def pwCaxqRZQsvS(self, nKGKSPXPp):
        QHYMHhwOVIXtLT = self.QHYMHhwOVIXtLT
        pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp)

    def NuGwC(self):
        try:
            self.session.openWithCallback(self.wImiGCFpPSqZ, oifusNtsQLjEI)
        except:
            pass

    def wImiGCFpPSqZ(self):
        self.hide()
        if TrruhKvKi:
            CIGmain(self.session, TrruhKvKi)
        if WvYVaQ != self.NFVzxMfxEUu and SAQsYCIeDb != self.NFVzxMfxEUu:
            self.session.open(MessageBox, Po, MessageBox.TYPE_INFO)
        self.YxuwUrC()

    def SohIHVvAMnbAXX(self, nKGKSPXPp):
        if nKGKSPXPp[0]:
            WFVjWbKbX = nKGKSPXPp[1]
            QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
            if QptgJyXzKf is not None:
                for x in QptgJyXzKf:
                    if x.setAutoincreaseEnd(WFVjWbKbX):
                        self.session.nav.RecordTimer.timeChanged(x)

                QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
                if QptgJyXzKf is not None:
                    self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, QptgJyXzKf)
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('TimerEdit'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('TimerEdit'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('TimerEdit'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('TimerEdit'))
        return

    def AoKSzJQJax(self, nKGKSPXPp):
        self.SohIHVvAMnbAXX(nKGKSPXPp)

    def nORxTbRjzsNVch(self):
        try:
            UMUhLJhkv = self['CoolEvent'].JvSwzXgDeSH()[1]
            if UMUhLJhkv:
                TrruhKvKi.setCurrentSelection(UMUhLJhkv.ref)
                TrruhKvKi.zap()
                FllUJdlN(UMUhLJhkv.ref)
            config.CTVG.C61.value = True
        except:
            return

    def JIQKwPOcc(self):
        try:
            YJtIpOkBKsCcvSg = self['CoolEvent'].JvSwzXgDeSH()[1]
            if YJtIpOkBKsCcvSg:
                TrruhKvKi.setCurrentSelection(YJtIpOkBKsCcvSg.ref)
                TrruhKvKi.zap()
                FllUJdlN(YJtIpOkBKsCcvSg.ref)
            self.YxuwUrC()
        except:
            return


class TyJjFMDpxnnJch(HTMLComponent, GUIComponent):

    def __init__(self, pOHOrwCihqC = None, QHYMHhwOVIXtLT = None):
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
        self.PVPFJS = []
        if pOHOrwCihqC is not None:
            self.PVPFJS.append(pOHOrwCihqC)
        GUIComponent.__init__(self)
        self.TPVxuSuwYBrUelM = eServiceCenter.getInstance()
        self.l = eListboxPythonMultiContent()
        self.jvTmTJHlfxPIP = parseFont('Regular;24', ((1, 1), (1, 1)))
        self.l.setFont(0, self.jvTmTJHlfxPIP)
        self.l.setBuildFunc(self.zKQMKGEg)
        self.DZOLaKQYXqw = 0
        self.FIrFKOOPfdRJnb = 60
        self.xHpqYxluJNkS = 1060
        self.IwKiKwc = 120
        self.CwbbgtPbYdAJaNS = 250
        self.oVoKs = 950
        self.HkPIn = 60
        self.RVaddhJ = 2
        self.vDtXdSWMj = 190
        self.sZFcJcEYedYG = None
        self.RYWUNgKwKamFGs = None
        self.SMtkYND = 16737792
        self.chSpBcKz = 3905737
        self.Wzjij = 16777215
        self.ZWXRUOATTV = 10425107
        self.hXbYdg = 11902465
        self.tyoaImn = 3905737
        self.HaJKV = 6316128
        self.WubpaSVNw = 16777215
        self.DTzDLYhRge = eEPGCache.getInstance()
        return

    def applySkin(self, desktop, parent):
        dyYxANT = []
        if self.skinAttributes is not None:
            for Obqlh, value in self.skinAttributes:
                if Obqlh == 'CoolFont':
                    self.jvTmTJHlfxPIP = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(0, self.jvTmTJHlfxPIP)
                elif Obqlh == 'CoolDayPos':
                    self.DZOLaKQYXqw = int(value)
                elif Obqlh == 'CoolTimePos':
                    self.HkPIn = int(value)
                elif Obqlh == 'CoolEventPos':
                    self.CwbbgtPbYdAJaNS = int(value)
                elif Obqlh == 'CoolEventSize':
                    self.oVoKs = int(value)
                elif Obqlh == 'CoolDaySize':
                    self.FIrFKOOPfdRJnb = int(value)
                elif Obqlh == 'CoolTimeSize':
                    self.vDtXdSWMj = int(value)
                elif Obqlh == 'CoolDurationPos':
                    self.xHpqYxluJNkS = int(value)
                elif Obqlh == 'CoolTimeHPos':
                    self.RVaddhJ = int(value)
                elif Obqlh == 'CoolDurationSize':
                    self.IwKiKwc = int(value)
                elif Obqlh == 'CoolDayColor':
                    self.SMtkYND = parseColor(value).argb()
                elif Obqlh == 'CoolTimeColor':
                    self.tyoaImn = parseColor(value).argb()
                elif Obqlh == 'CoolEventColor':
                    self.Wzjij = parseColor(value).argb()
                elif Obqlh == 'CoolBackColor':
                    self.sZFcJcEYedYG = parseColor(value).argb()
                elif Obqlh == 'CoolBackColorSel':
                    self.RYWUNgKwKamFGs = parseColor(value).argb()
                elif Obqlh == 'CoolFontColSel':
                    self.WubpaSVNw = parseColor(value).argb()
                elif Obqlh == 'CoolDurationColor':
                    self.chSpBcKz = parseColor(value).argb()
                elif Obqlh == 'CoolTunerCol':
                    self.HaJKV = parseColor(value).argb()
                elif Obqlh == 'CoolRecAlarmCol':
                    self.hXbYdg = parseColor(value).argb()
                elif Obqlh == 'CoolRecColor':
                    self.ZWXRUOATTV = parseColor(value).argb()
                else:
                    dyYxANT.append((Obqlh, value))

        self.skinAttributes = dyYxANT
        return GUIComponent.applySkin(self, desktop, parent)

    def JvSwzXgDeSH(self):
        XZNkhLy = 0
        Dovjge = self.l.getCurrentSelection()
        if Dovjge is None:
            return (None, None)
        else:
            gOvtm = Dovjge[XZNkhLy + 1]
            UMUhLJhkv = ServiceReference(Dovjge[XZNkhLy])
            NyWchRFXtIMu = self.QvVabvQOoSofkV(UMUhLJhkv, gOvtm)
            return (NyWchRFXtIMu, UMUhLJhkv)

    def QvVabvQOoSofkV(self, UMUhLJhkv, gggJixxXg):
        QaRPPSUPE = None
        if self.DTzDLYhRge is not None and gggJixxXg is not None:
            QaRPPSUPE = self.DTzDLYhRge.lookupEventId(UMUhLJhkv.ref, gggJixxXg)
        return QaRPPSUPE

    def selectionChanged(self):
        for x in self.PVPFJS:
            if x is not None:
                x()

        return

    def GdjxEetRD(self):
        self.instance.moveSelection(self.instance.moveUp)

    def Krkrxa(self):
        self.instance.moveSelection(self.instance.moveDown)

    GUI_WIDGET = eListbox

    def zKQMKGEg(self, UMUhLJhkv, VQKNKnUpnwbt, pVdYFhAaXsyyci, qxyEWz, cIlYUZavCM):
        try:
            MBwGVCQCuRs = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
            AduwKVqFCtWzeIh = self.mCcXxUnnUdldCM(eServiceReference(UMUhLJhkv), eServiceReference(MBwGVCQCuRs))
        except:
            AduwKVqFCtWzeIh = 1

        aApyAGzT = localtime(pVdYFhAaXsyyci)
        rLTFYjFLR = self.NSjWHcStKTLbU(UMUhLJhkv, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt)
        if rLTFYjFLR == True:
            QLxdqGrZFSq = djalaNtmJRirVIK = iHYMQIruq = uSfYSrtgTKg = mxxivgrFxGLko = self.ZWXRUOATTV
        elif rLTFYjFLR == False:
            QLxdqGrZFSq = djalaNtmJRirVIK = iHYMQIruq = uSfYSrtgTKg = mxxivgrFxGLko = self.hXbYdg
        elif not AduwKVqFCtWzeIh:
            QLxdqGrZFSq = djalaNtmJRirVIK = iHYMQIruq = uSfYSrtgTKg = mxxivgrFxGLko = self.HaJKV
        else:
            djalaNtmJRirVIK = self.SMtkYND
            iHYMQIruq = self.tyoaImn
            uSfYSrtgTKg = self.Wzjij
            mxxivgrFxGLko = self.chSpBcKz
            QLxdqGrZFSq = self.WubpaSVNw
        res = [None, (eListboxPythonMultiContent.TYPE_TEXT,
          self.DZOLaKQYXqw,
          0,
          self.FIrFKOOPfdRJnb,
          50,
          0,
          RT_HALIGN_LEFT,
          self.PsMWO[aApyAGzT[6]],
          djalaNtmJRirVIK,
          QLxdqGrZFSq,
          self.sZFcJcEYedYG,
          self.RYWUNgKwKamFGs)]
        res.append(MultiContentEntryText(pos=(self.CwbbgtPbYdAJaNS, 0), size=(self.oVoKs, 50), font=0, text=cIlYUZavCM, color=uSfYSrtgTKg, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.RYWUNgKwKamFGs))
        if pVdYFhAaXsyyci is not None:
            JBCDJoHYm = localtime(pVdYFhAaXsyyci + qxyEWz)
            res.append(MultiContentEntryText(pos=(self.HkPIn, 0), size=(self.vDtXdSWMj, 50), font=0, text='%02d:%02d  -  %02d:%02d' % (aApyAGzT[3],
             aApyAGzT[4],
             JBCDJoHYm[3],
             JBCDJoHYm[4]), color=iHYMQIruq, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.RYWUNgKwKamFGs, border_width=0, border_color=self.sZFcJcEYedYG))
            res.append(MultiContentEntryText(pos=(self.xHpqYxluJNkS, self.RVaddhJ), size=(self.IwKiKwc, 50), font=0, flags=RT_HALIGN_RIGHT, text='%02d min' % (qxyEWz / 60), color=mxxivgrFxGLko, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.RYWUNgKwKamFGs))
        return res

    def postWidgetCreate(self, instance):
        instance.setWrapAround(True)
        instance.selectionChanged.get().append(self.selectionChanged)
        instance.setContent(self.l)

    def preWidgetRemove(self, instance):
        instance.selectionChanged.get().remove(self.selectionChanged)
        instance.setContent(None)
        return

    def NSjWHcStKTLbU(self, fXYLLkn, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt):
        for x in self.QHYMHhwOVIXtLT.timer_list:
            if x.service_ref.ref.toString() == fXYLLkn:
                blmRapeotWYHCEX = pVdYFhAaXsyyci + qxyEWz
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                if x.eit == VQKNKnUpnwbt:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True
                elif pVdYFhAaXsyyci <= TteNjwT <= blmRapeotWYHCEX:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True

        for x in self.QHYMHhwOVIXtLT.processed_timers:
            if x.disabled and x.service_ref.ref.toString() == fXYLLkn:
                if x.eit == VQKNKnUpnwbt:
                    return False

    def aMrVMukygNMxHdl(self):
        x = self.l.getCurrentSelection()
        return x and x[1]

    def mCcXxUnnUdldCM(self, BidVA, JhKpFAp):
        NHozf = self.TPVxuSuwYBrUelM.info(BidVA)
        return NHozf and NHozf.isPlayable(BidVA, JhKpFAp) or False

    def pTTZqyXtEbFRSig(self, LjgPsdVwwQ):
        ZDxUJDDCPod = ['RIBDT', (LjgPsdVwwQ.ref.toString(),
          0,
          -1,
          -1)]
        self.ScnvMSTPY = self.sdiQt(ZDxUJDDCPod)
        self.l.setList(self.ScnvMSTPY)
        self.selectionChanged()
        self.AuuDAnZtzhDT(DCNYRvBrUl)

    def sdiQt(self, list, MlBIgDzxYSu = None):
        if self.DTzDLYhRge is not None:
            if MlBIgDzxYSu is not None:
                return self.DTzDLYhRge.lookupEvent(list, MlBIgDzxYSu)
            else:
                return self.DTzDLYhRge.lookupEvent(list)
        return []

    def UrfFYoRsn(self, qjCtcNsozE):
        if not qjCtcNsozE:
            return
        tAaMXETO = 0
        EjcPO = qjCtcNsozE.toString()
        for x in self.ScnvMSTPY:
            if x[1] == EjcPO:
                self.instance.moveSelectionTo(tAaMXETO)
                break
            tAaMXETO += 1

    def AuuDAnZtzhDT(self, VQKNKnUpnwbt):
        if not VQKNKnUpnwbt:
            return
        tAaMXETO = 0
        for x in self.ScnvMSTPY:
            if x[1] == VQKNKnUpnwbt:
                self.instance.moveSelectionTo(tAaMXETO)
                break
            tAaMXETO += 1


def gGjXQFlY(CmmLR, dic):
    for i, j in dic.items():
        CmmLR = CmmLR.replace(i, j)

    return CmmLR


class XEArkQXQCQRMEL(Screen):

    def __init__(self, session, UMUhLJhkv, TrruhKvKi, gggJixxXg = None, nfZQJKwSrVA = None, PwRojNX = None):
        Screen.__init__(self, session)
        if TMvKPeMEZHVqV == 720:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_720.xml'
            elif PwRojNX == iXZeUPZjXi:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_720.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_720.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_720.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_720.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_720.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_720.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_720.xml'
        elif TMvKPeMEZHVqV == 1024:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1024.xml'
            elif PwRojNX == iXZeUPZjXi:
                if config.CTVG.C43.value == 1:
                    self.skinName = 'CoolSingleGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1024.xml'
                elif config.CTVG.C43.value == 2:
                    self.skinName = 'CoolSingleGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1024.xml'
                elif config.CTVG.C43.value == 3:
                    self.skinName = 'CoolSingleGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1024.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                if config.CTVG.C42.value == 1:
                    self.skinName = 'CoolEasyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1024.xml'
                elif config.CTVG.C42.value == 2:
                    self.skinName = 'CoolEasyGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1024.xml'
                elif config.CTVG.C42.value == 3:
                    self.skinName = 'CoolEasyGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1024.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                if config.CTVG.C41.value == 1:
                    self.skinName = 'CoolChannelGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1024.xml'
                elif config.CTVG.C41.value == 2:
                    self.skinName = 'CoolChannelGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1024.xml'
                elif config.CTVG.C41.value == 3:
                    self.skinName = 'CoolChannelGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1024.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1024.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1024.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1024.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1024.xml'
        elif PwRojNX == PQMOk:
            self.skinName = 'CoolInfoGuide'
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1280.xml'
        elif PwRojNX == iXZeUPZjXi:
            if config.CTVG.C43.value == 1:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1280.xml'
            elif config.CTVG.C43.value == 2:
                self.skinName = 'CoolSingleGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1280.xml'
            elif config.CTVG.C43.value == 3:
                self.skinName = 'CoolSingleGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1280.xml'
        elif PwRojNX == IUqwdjkcjCMKCFO:
            if config.CTVG.C42.value == 1:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1280.xml'
            elif config.CTVG.C42.value == 2:
                self.skinName = 'CoolEasyGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1280.xml'
            elif config.CTVG.C42.value == 3:
                self.skinName = 'CoolEasyGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1280.xml'
        elif PwRojNX == QQdKtJPxMxJPjwB:
            if config.CTVG.C41.value == 1:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1280.xml'
            elif config.CTVG.C41.value == 2:
                self.skinName = 'CoolChannelGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1280.xml'
            elif config.CTVG.C41.value == 3:
                self.skinName = 'CoolChannelGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1280.xml'
        elif PwRojNX == eseWoWLtSYyCHGT:
            if config.CTVG.C40.value == 1:
                self.skinName = 'CoolTVGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1280.xml'
            elif config.CTVG.C40.value == 2:
                self.skinName = 'CoolTinyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1280.xml'
            elif config.CTVG.C40.value == 3:
                self.skinName = 'CoolMultiGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1280.xml'
            elif config.CTVG.C40.value == 4:
                self.skinName = 'CoolNiceGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1280.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self.WxwlY = zUIfAWMBbQJ
        self.aewDrpsjqX = TrruhKvKi
        self.nfZQJKwSrVA = nfZQJKwSrVA
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.vzDGDGAQLSCa = -1
        self.FUiTqUurDFxy = False
        self.cIKHf = None
        self['Service'] = ServiceEvent()
        self['Event'] = Event()
        self['key_red'] = Button('')
        self['key_green'] = Button('')
        self['key_yellow'] = Button('')
        self['key_blue'] = Button('')
        self['date'] = Button()
        self.XISehjxsPoi = ServiceReference(UMUhLJhkv)
        self.GQXnqX = 0
        self.pNBpPojSpByeEg = UMUhLJhkv
        self['list'] = lxNLnyst(pOHOrwCihqC=self.WlFKMlyFxSWrG, QHYMHhwOVIXtLT=session.nav.RecordTimer)
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolMenu': self.NuGwC,
         'CoolRed': self.GwhJbNuquP,
         'CoolRedLong': self.fbUws,
         'CoolGreen': self.gXppchsrp,
         'CoolGreenLong': self.mzzBQRAohy,
         'CoolYellow': self.bKpKe,
         'CoolYellowLong': self.qOlhOHWiFHpIC,
         'CoolBlue': self.qsDCwRsYOveEFy,
         'CoolBlueLong': self.uHqjdBJMLj,
         'CoolOK': self.WhRkmBFDyxfV,
         'CoolOKLong': self.KZcQOfIkWdrLZ,
         'CoolInfo': self.NxrXAek,
         'CoolInfoLong': self.uWIjFbGhtX,
         'CoolRecord': self.esPNG,
         'CoolTime': self.LvTfjDmL,
         'CoolVIDEO': nePylQgKlghpaVP,
         'CoolAUDIO': self.BvRoHaxNcu,
         'CoolKeyTV': self.EekrcnjXd,
         'CoolPower': self.EUtMyA,
         'CoolCancel': self.JtAiZhAVofB,
         'CoolChannelUP': self.nCbsAJiEfEB,
         'CoolChannelDown': self.qoiUQ,
         'CoolNEXT': self.ckJPPSTaPu,
         'CoolPREVIOUS': self.YzrxgfKwCwLOlLS,
         '0': self.RDSJwxPYCfBLVaN,
         '1': self.BXgEprgWswxGUwu,
         '2': self.dyKNDy,
         '3': self.OwPMoV,
         '7': self.TdjjCghHcsK,
         '8': self.neDLkklkP,
         '9': self.eKXjhOLrwzFbS}, -1)
        self.SuVhHLBrOFx = config.CTVG.C12.value
        self.jIDDtifEzLAQAtH = config.CTVG.C14.value
        self.KhCcbywN = config.CTVG.C16.value
        self.gYtswyvbtJ = config.CTVG.C18.value
        if self.SuVhHLBrOFx == 'PrimeTime' or self.SuVhHLBrOFx == 'Bouquet +' or self.SuVhHLBrOFx == 'Bouquet -' or self.SuVhHLBrOFx == 'Bouquetlist':
            self.SuVhHLBrOFx = 'EPG Select'
        if self.jIDDtifEzLAQAtH == 'PrimeTime' or self.jIDDtifEzLAQAtH == 'Bouquet +' or self.jIDDtifEzLAQAtH == 'Bouquet -' or self.jIDDtifEzLAQAtH == 'Bouquetlist':
            self.jIDDtifEzLAQAtH = 'Timer'
        if self.KhCcbywN == 'PrimeTime' or self.KhCcbywN == 'Bouquet +' or self.KhCcbywN == 'Bouquet -' or self.KhCcbywN == 'Bouquetlist':
            self.KhCcbywN = 'Sort A-Z'
            self.LCmBHLDajtwhvd()
        else:
            self['key_yellow'].setText(_(self.KhCcbywN))
        if self.gYtswyvbtJ == 'PrimeTime' or self.gYtswyvbtJ == 'Bouquet +' or self.gYtswyvbtJ == 'Bouquet -' or self.gYtswyvbtJ == 'Bouquetlist':
            self.gYtswyvbtJ = 'CoolSearch'
        self['key_red'].setText(_(self.SuVhHLBrOFx))
        self['key_green'].setText(_(self.jIDDtifEzLAQAtH))
        self['key_blue'].setText(_(self.gYtswyvbtJ))
        self.onLayoutFinish.append(self.NbmZQLxewbo)
        self.fzPnyf()
        return

    def qFDSvr(self):
        global WmXVqUV
        if WmXVqUV == 1:
            x = config.CTVG.C77.value
        elif WmXVqUV == 2:
            x = config.CTVG.C78.value
        elif WmXVqUV == 3:
            x = config.CTVG.C79.value
        elif WmXVqUV == 4:
            if WvYVaQ != self.WxwlY and SAQsYCIeDb != self.WxwlY:
                WmXVqUV = 1
                return self.close(False)
            x = config.CTVG.C80.value
        elif WmXVqUV == 5:
            x = config.CTVG.C81.value
        elif WmXVqUV == 6:
            x = config.CTVG.C82.value
        elif WmXVqUV == 7:
            x = config.CTVG.C83.value
        elif WmXVqUV == 8:
            x = config.CTVG.C84.value
        elif WmXVqUV == 9:
            x = config.CTVG.C85.value
        elif WmXVqUV == 10:
            x = config.CTVG.C86.value
        elif WmXVqUV == 11:
            x = config.CTVG.C87.value
        elif WmXVqUV == 12:
            x = config.CTVG.C88.value
        if x == '9':
            WmXVqUV += 1
            return self.qFDSvr()
        self.hide()
        if x == '1':
            self.TmoaJg()
        else:
            if x == '2':
                WmXVqUV += 1
                return self.qFDSvr()
            if x == '3':
                CEGmain(self.session, self.aewDrpsjqX)
            elif x == '4':
                CCGmain(self.session, self.aewDrpsjqX)
            elif x == '5':
                config.CTVG.C40.value = 1
                main(self.session, self.aewDrpsjqX)
            elif x == '6':
                config.CTVG.C40.value = 2
                main(self.session, self.aewDrpsjqX)
            elif x == '7':
                config.CTVG.C40.value = 3
                main(self.session, self.aewDrpsjqX)
            elif x == '8':
                config.CTVG.C40.value = 4
                main(self.session, self.aewDrpsjqX)
            elif x == '10':
                self.sSPMBhwDflASCMt()
            elif x == '11':
                WmXVqUV = 0
                self.session.open(TimerEditList)
            else:
                WmXVqUV = 0
        WmXVqUV += 1
        self.close(False)

    def fzPnyf(self):
        geikSRpcvam = localtime()
        if (geikSRpcvam.tm_year, geikSRpcvam.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2])):
            self.close(self.FUiTqUurDFxy)

    def TmoaJg(self):
        config.CTVG.C61.value = False
        tfonHdIjfgQ = self['list'].JvSwzXgDeSH()
        if not tfonHdIjfgQ:
            return
        iqUxDClWfpeziO = eServiceReference(str(tfonHdIjfgQ[1]))
        if iqUxDClWfpeziO:
            gGPiwVmWkgM = self.aewDrpsjqX.getRoot()
            ZnHPgSvmg = getBouquetServices(gGPiwVmWkgM)
            self.serviceSel = SimpleServicelist(ZnHPgSvmg)
            if self.serviceSel.selectService(iqUxDClWfpeziO):
                self.session.open(zDKhcfAp, tfonHdIjfgQ[0], tfonHdIjfgQ[1], iqUxDClWfpeziO, self.aewDrpsjqX, self.QEcLxYKv, nfZQJKwSrVA=self.changeServiceCB, PwRojNX=PQMOk)

    def BvRoHaxNcu(self):
        self.hide()
        CEGmain(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def RDSJwxPYCfBLVaN(self):
        self.hide()
        CSGmain(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def RHRYk(self):
        self.hide()
        main(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def EUtMyA(self):
        try:
            from Screens.SleepTimerEdit import SleepTimerEdit
            self.session.open(SleepTimerEdit)
        except:
            pass

    def GwhJbNuquP(self):
        EcLNwIhunJbRsLQ = self.SuVhHLBrOFx
        if EcLNwIhunJbRsLQ == 'EPG Select':
            self.qFDSvr()
        elif EcLNwIhunJbRsLQ == 'Zap':
            self.nORxTbRjzsNVch()
        elif EcLNwIhunJbRsLQ == 'Zap + Exit':
            self.JIQKwPOcc()
        elif EcLNwIhunJbRsLQ == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif EcLNwIhunJbRsLQ == 'CoolInfoBox':
            self.fxVcQUikA()
        elif EcLNwIhunJbRsLQ == 'GuideSwitch':
            self.RHRYk()
        elif EcLNwIhunJbRsLQ == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif EcLNwIhunJbRsLQ == 'Timer':
            self.EmOZX()
        elif EcLNwIhunJbRsLQ == 'QuickRec':
            self.esPNG()
        elif EcLNwIhunJbRsLQ == 'AutoTimer':
            self.voLEWybvGX()
        else:
            self.qFDSvr()

    def fbUws(self):
        aFfcKSkBDKNWm = config.CTVG.C13.value
        if aFfcKSkBDKNWm == 'Zap':
            self.nORxTbRjzsNVch()
        elif aFfcKSkBDKNWm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif aFfcKSkBDKNWm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif aFfcKSkBDKNWm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif aFfcKSkBDKNWm == 'GuideSwitch':
            self.RHRYk()
        elif aFfcKSkBDKNWm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif aFfcKSkBDKNWm == 'Timer':
            self.EmOZX()
        elif aFfcKSkBDKNWm == 'QuickRec':
            self.esPNG()
        elif aFfcKSkBDKNWm == 'AutoTimer':
            self.voLEWybvGX()
        elif aFfcKSkBDKNWm == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def gXppchsrp(self):
        fCsivhkbczcm = self.jIDDtifEzLAQAtH
        if fCsivhkbczcm == 'Zap':
            self.nORxTbRjzsNVch()
        elif fCsivhkbczcm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif fCsivhkbczcm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif fCsivhkbczcm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif fCsivhkbczcm == 'GuideSwitch':
            self.RHRYk()
        elif fCsivhkbczcm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif fCsivhkbczcm == 'Timer':
            self.EmOZX()
        elif fCsivhkbczcm == 'QuickRec':
            self.esPNG()
        elif fCsivhkbczcm == 'AutoTimer':
            self.voLEWybvGX()
        elif fCsivhkbczcm == 'EPG Select':
            self.qFDSvr()
        else:
            self.EmOZX()

    def mzzBQRAohy(self):
        CALICbGXK = config.CTVG.C15.value
        if CALICbGXK == 'Zap':
            self.nORxTbRjzsNVch()
        elif CALICbGXK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif CALICbGXK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif CALICbGXK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif CALICbGXK == 'GuideSwitch':
            self.RHRYk()
        elif CALICbGXK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif CALICbGXK == 'Timer':
            self.EmOZX()
        elif CALICbGXK == 'QuickRec':
            self.esPNG()
        elif CALICbGXK == 'AutoTimer':
            self.voLEWybvGX()
        elif CALICbGXK == 'EPG Select':
            self.qFDSvr()
        else:
            self.voLEWybvGX()

    def bKpKe(self):
        BCGuXefsvjf = self.KhCcbywN
        if BCGuXefsvjf == 'Zap':
            self.nORxTbRjzsNVch()
        elif BCGuXefsvjf == 'Zap + Exit':
            self.JIQKwPOcc()
        elif BCGuXefsvjf == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif BCGuXefsvjf == 'CoolInfoBox':
            self.fxVcQUikA()
        elif BCGuXefsvjf == 'GuideSwitch':
            self.RHRYk()
        elif BCGuXefsvjf == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif BCGuXefsvjf == 'Timer':
            self.EmOZX()
        elif BCGuXefsvjf == 'QuickRec':
            self.esPNG()
        elif BCGuXefsvjf == 'AutoTimer':
            self.voLEWybvGX()
        elif BCGuXefsvjf == 'EPG Select':
            self.qFDSvr()
        else:
            self.LvTfjDmL()

    def qOlhOHWiFHpIC(self):
        gRpGhRQrF = config.CTVG.C17.value
        if gRpGhRQrF == 'Zap':
            self.nORxTbRjzsNVch()
        elif gRpGhRQrF == 'Zap + Exit':
            self.JIQKwPOcc()
        elif gRpGhRQrF == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif gRpGhRQrF == 'CoolInfoBox':
            self.fxVcQUikA()
        elif gRpGhRQrF == 'GuideSwitch':
            self.RHRYk()
        elif gRpGhRQrF == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif gRpGhRQrF == 'Timer':
            self.EmOZX()
        elif gRpGhRQrF == 'QuickRec':
            self.esPNG()
        elif gRpGhRQrF == 'AutoTimer':
            self.voLEWybvGX()
        elif gRpGhRQrF == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def qsDCwRsYOveEFy(self):
        LnElTGKJP = self.gYtswyvbtJ
        if LnElTGKJP == 'Zap':
            self.nORxTbRjzsNVch()
        elif LnElTGKJP == 'Zap + Exit':
            self.JIQKwPOcc()
        elif LnElTGKJP == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif LnElTGKJP == 'CoolInfoBox':
            self.fxVcQUikA()
        elif LnElTGKJP == 'GuideSwitch':
            self.RHRYk()
        elif LnElTGKJP == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif LnElTGKJP == 'Timer':
            self.EmOZX()
        elif LnElTGKJP == 'QuickRec':
            self.esPNG()
        elif LnElTGKJP == 'AutoTimer':
            self.voLEWybvGX()
        elif LnElTGKJP == 'EPG Select':
            self.qFDSvr()
        else:
            self.sSPMBhwDflASCMt()

    def uHqjdBJMLj(self):
        UQcfkjKQK = config.CTVG.C19.value
        if UQcfkjKQK == 'Zap':
            self.nORxTbRjzsNVch()
        elif UQcfkjKQK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif UQcfkjKQK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif UQcfkjKQK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif UQcfkjKQK == 'GuideSwitch':
            self.RHRYk()
        elif UQcfkjKQK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif UQcfkjKQK == 'Timer':
            self.EmOZX()
        elif UQcfkjKQK == 'QuickRec':
            self.esPNG()
        elif UQcfkjKQK == 'AutoTimer':
            self.voLEWybvGX()
        elif UQcfkjKQK == 'EPG Select':
            self.qFDSvr()
        else:
            self.fxVcQUikA()

    def WhRkmBFDyxfV(self):
        SlBvlWSPMURgObC = config.CTVG.C20.value
        if SlBvlWSPMURgObC == 'Zap':
            self.nORxTbRjzsNVch()
        elif SlBvlWSPMURgObC == 'Zap + Exit':
            self.JIQKwPOcc()
        elif SlBvlWSPMURgObC == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif SlBvlWSPMURgObC == 'CoolInfoBox':
            self.fxVcQUikA()
        elif SlBvlWSPMURgObC == 'GuideSwitch':
            self.RHRYk()
        elif SlBvlWSPMURgObC == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif SlBvlWSPMURgObC == 'Timer':
            self.EmOZX()
        elif SlBvlWSPMURgObC == 'QuickRec':
            self.esPNG()
        elif SlBvlWSPMURgObC == 'AutoTimer':
            self.voLEWybvGX()
        elif SlBvlWSPMURgObC == 'EPG Select':
            self.qFDSvr()
        else:
            self.WVwFshleYbnIc()

    def KZcQOfIkWdrLZ(self):
        OCCKSDwCPbq = config.CTVG.C21.value
        if OCCKSDwCPbq == 'Zap':
            self.nORxTbRjzsNVch()
        elif OCCKSDwCPbq == 'Zap + Exit':
            self.JIQKwPOcc()
        elif OCCKSDwCPbq == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif OCCKSDwCPbq == 'CoolInfoBox':
            self.fxVcQUikA()
        elif OCCKSDwCPbq == 'GuideSwitch':
            self.RHRYk()
        elif OCCKSDwCPbq == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif OCCKSDwCPbq == 'Timer':
            self.EmOZX()
        elif OCCKSDwCPbq == 'QuickRec':
            self.esPNG()
        elif OCCKSDwCPbq == 'AutoTimer':
            self.voLEWybvGX()
        elif OCCKSDwCPbq == 'EPG Select':
            self.qFDSvr()
        else:
            return

    def NxrXAek(self):
        LkGwiX = config.CTVG.C22.value
        if LkGwiX == '4':
            self.qFDSvr()
        elif LkGwiX == '1':
            self.WVwFshleYbnIc()
        elif LkGwiX == '2':
            self.RDSJwxPYCfBLVaN()
        elif LkGwiX == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def uWIjFbGhtX(self):
        BkucHGwMEzEJ = config.CTVG.C23.value
        if BkucHGwMEzEJ == '4':
            self.qFDSvr()
        elif BkucHGwMEzEJ == '1':
            self.WVwFshleYbnIc()
        elif BkucHGwMEzEJ == '2':
            self.RDSJwxPYCfBLVaN()
        elif BkucHGwMEzEJ == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def ckJPPSTaPu(self):
        if self.nfZQJKwSrVA:
            self.nfZQJKwSrVA(1, self)

    def YzrxgfKwCwLOlLS(self):
        if self.nfZQJKwSrVA:
            self.nfZQJKwSrVA(-1, self)

    def nCbsAJiEfEB(self):
        self.ckJPPSTaPu()
        self.nORxTbRjzsNVch()

    def qoiUQ(self):
        self.YzrxgfKwCwLOlLS()
        self.nORxTbRjzsNVch()

    def BXgEprgWswxGUwu(self):
        config.CTVG.C43.value = 1
        config.CTVG.save()
        self.hide()
        self.RDSJwxPYCfBLVaN()
        self.close(self.FUiTqUurDFxy)

    def dyKNDy(self):
        if WvYVaQ == self.WxwlY or SAQsYCIeDb == self.WxwlY:
            config.CTVG.C43.value = 2
            config.CTVG.save()
            self.hide()
            self.RDSJwxPYCfBLVaN()
            self.close(self.FUiTqUurDFxy)

    def OwPMoV(self):
        if WvYVaQ == self.WxwlY or SAQsYCIeDb == self.WxwlY:
            config.CTVG.C43.value = 3
            config.CTVG.save()
            self.hide()
            self.RDSJwxPYCfBLVaN()
            self.close(self.FUiTqUurDFxy)

    def TdjjCghHcsK(self):
        self.RHRYk()

    def neDLkklkP(self):
        self.RDSJwxPYCfBLVaN()

    def eKXjhOLrwzFbS(self):
        self.BvRoHaxNcu()

    def changeServiceCB(self, SqpegV = None, epg = None):
        if self.serviceSel:
            if SqpegV > 0:
                self.serviceSel.nextService()
            else:
                self.serviceSel.prevService()
            epg.setService(self.serviceSel.currentService())

    def JtAiZhAVofB(self):
        global WmXVqUV
        WmXVqUV = 1
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.hide()
        AjzDUzKgoLe = set()
        geikSRpcvam = time()
        gwVLVamNAqnDMo = False
        if config.CTVG.C62.value:
            for x in self.session.nav.RecordTimer.timer_list:
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                try:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventId(x.service_ref.ref, x.eit)
                except:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventTime(x.service_ref.ref, TteNjwT)

                if ERoOCCVi:
                    IcZCToaVeOwI = ERoOCCVi.getBeginTime()
                    CsrfWgDZI = IcZCToaVeOwI + ERoOCCVi.getDuration()
                    if IcZCToaVeOwI < cpUukOBh or CsrfWgDZI > JBCDJoHYm:
                        if ERoOCCVi.getDuration() > 300 and cpUukOBh > geikSRpcvam:
                            AjzDUzKgoLe.add(x)

        if config.CTVG.C63.value:
            for x in self.session.nav.RecordTimer.processed_timers:
                if geikSRpcvam < x.end:
                    AjzDUzKgoLe.add(x)

        dXRTDwpUpKROauu = _('\n          !! Cool Timer Alarm !! \n\n')
        for x in AjzDUzKgoLe:
            gwVLVamNAqnDMo = str(x.name)
            dplqPMZr = str(strftime('%d.%m.%Y - %H:%M', localtime(x.begin)))
            BhkuqkbF = str(x.service_ref.getServiceName())
            TuqtF = _('is disabled') if x.disabled else _('has moved')
            dXRTDwpUpKROauu += dplqPMZr + ' - ' + BhkuqkbF + '\n' + gwVLVamNAqnDMo + ' ' + TuqtF + '\n\n'

        dXRTDwpUpKROauu += _('-- please check your Timer --')
        if gwVLVamNAqnDMo:
            self.session.open(MessageBox, dXRTDwpUpKROauu, MessageBox.TYPE_ERROR)
        self.close(self.FUiTqUurDFxy)

    def NbmZQLxewbo(self):
        LjgPsdVwwQ = self.XISehjxsPoi
        if self.cIKHf is None:
            self.cIKHf = self.instance.getTitle()
        huKIXKkzvJsh = self.cIKHf + ' - ' + LjgPsdVwwQ.getServiceName()
        self.instance.setTitle(huKIXKkzvJsh)
        self['list'].kTbbTdgXcs(LjgPsdVwwQ)
        return

    def WVwFshleYbnIc(self):
        config.CTVG.C61.value = False
        tfonHdIjfgQ = self['list'].JvSwzXgDeSH()
        if not tfonHdIjfgQ:
            return
        iqUxDClWfpeziO = eServiceReference(str(tfonHdIjfgQ[1]))
        if iqUxDClWfpeziO:
            gGPiwVmWkgM = self.aewDrpsjqX.getRoot()
            ZnHPgSvmg = getBouquetServices(gGPiwVmWkgM)
            self.serviceSel = SimpleServicelist(ZnHPgSvmg)
            if self.serviceSel.selectService(iqUxDClWfpeziO):
                self.session.openWithCallback(self.UZWrOVfpub, zDKhcfAp, tfonHdIjfgQ[0], tfonHdIjfgQ[1], iqUxDClWfpeziO, self.aewDrpsjqX, self.QEcLxYKv, nfZQJKwSrVA=self.changeServiceCB, PwRojNX=PQMOk)

    def UZWrOVfpub(self, ret = False):
        if config.CTVG.C61.value:
            self.hide()
            CSGmain(self.session, self.aewDrpsjqX)
            self.close(self.FUiTqUurDFxy)
            config.CTVG.C61.value = False

    def setService(self, UMUhLJhkv):
        self.XISehjxsPoi = UMUhLJhkv
        self.NbmZQLxewbo()

    def qFLoYuYRPQFdK(self, qDFTEDFxno):
        self.pNBpPojSpByeEg = qDFTEDFxno
        self.NbmZQLxewbo()

    def QEcLxYKv(self, QoGRewjlErZRq, setService, val):
        if val == -1:
            self.GdjxEetRD()
        elif val == +1:
            self.Krkrxa()
        bJKvGIVemCb = self['list'].JvSwzXgDeSH()
        setService(bJKvGIVemCb[1])
        QoGRewjlErZRq(bJKvGIVemCb[0])

    def LCmBHLDajtwhvd(self):
        if self.KhCcbywN == 'Sort A-Z':
            if self.GQXnqX == 1:
                self['key_yellow'].setText(_('Sort Time'))
            else:
                self['key_yellow'].setText(_('Sort A-Z'))

    def LvTfjDmL(self):
        if self.GQXnqX == 0:
            self.GQXnqX = 1
        else:
            self.GQXnqX = 0
        self['list'].UdfmjeClzFlLYT(self.GQXnqX)
        self.LCmBHLDajtwhvd()

    def GdjxEetRD(self):
        self['list'].GdjxEetRD()

    def Krkrxa(self):
        self['list'].Krkrxa()

    def voLEWybvGX(self):
        SNAVqJygcUu = self['list'].JvSwzXgDeSH()
        if not SNAVqJygcUu:
            return
        try:
            from Plugins.Extensions.AutoTimer.AutoTimerEditor import addAutotimerFromEvent
            self.session.openWithCallback(self.aqFgBg, ChoiceBox, title=_('   check Autotimer ?'), list=[(_('Yes'), 'Yes'), (_('No'), 'No')])
            addAutotimerFromEvent(self.session, SNAVqJygcUu[0], SNAVqJygcUu[1])
        except:
            self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def aqFgBg(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        if nKGKSPXPp == 'Yes':
            try:
                from Plugins.Extensions.AutoTimer.plugin import main as AutoTimerSafe
                AutoTimerSafe(self.session)
            except:
                self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def fxVcQUikA(self):
        UFXUK = []
        if fspOMNbuwFCWk:
            UFXUK.append((_('SeriesPlugin'), 'SeriesPlugin'))
        if sLpxMYXhjCROl:
            UFXUK.append((_('The TVDB Info'), 'The TVDB Info'))
        if bPdxaOceY:
            UFXUK.append((_('IMDb Search'), 'IMDbSearch'))
        if WizweESn:
            UFXUK.append((_('TMDB Info'), 'TMDBInfo'))
        if HikvfLr:
            UFXUK.append((_('OFDb Details'), 'OFDbDetails'))
        if UFXUK == []:
            UFXUK.append((_('No Info Plugins installed...'), 'No Info Plugins installed...'))
        self.session.openWithCallback(self.tmxBeAld, ChoiceBox, title=_('   CoolInfoBox'), list=UFXUK)

    def tmxBeAld(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        OiTUjyeSoZRNG = self['list'].JvSwzXgDeSH()
        zXaGlOHNBdRvpus = OiTUjyeSoZRNG[0]
        if not zXaGlOHNBdRvpus:
            return
        name = zXaGlOHNBdRvpus and zXaGlOHNBdRvpus.getEventName() or ''
        if nKGKSPXPp == 'SeriesPlugin':
            from Plugins.Extensions.SeriesPlugin.SeriesPluginInfoScreen import SeriesPluginInfoScreen
            UMUhLJhkv = OiTUjyeSoZRNG[1]
            self.session.open(SeriesPluginInfoScreen, UMUhLJhkv, zXaGlOHNBdRvpus)
        if nKGKSPXPp == 'The TVDB Info':
            from Plugins.Extensions.TheTVDB.plugin import TheTVDBMain
            self.session.open(TheTVDBMain, name)
        if nKGKSPXPp == 'IMDbSearch':
            from Plugins.Extensions.IMDb.plugin import IMDB
            self.session.open(IMDB, name)
        if nKGKSPXPp == 'TMDBInfo':
            from Plugins.Extensions.TMDb.plugin import TMDbMain
            self.session.open(TMDbMain, name)
        if nKGKSPXPp == 'OFDbDetails':
            from Plugins.Extensions.OFDb.plugin import OFDB
            self.session.open(OFDB, name)

    def sSPMBhwDflASCMt(self):
        try:
            EnFKRmiyy = self['list'].JvSwzXgDeSH()
            ERoOCCVi = EnFKRmiyy[0]
            if not ERoOCCVi:
                return
            name = ERoOCCVi.getEventName() or ''
        except:
            name = ''

        self.session.open(lyqBhZ, name, False)

    def esPNG(self):
        zjRLCa = self['list'].JvSwzXgDeSH()
        sYjJXxO = zjRLCa[1]
        vyakmd = zjRLCa[0]
        if not vyakmd:
            return
        else:
            FZxOvzpGBD = vyakmd.getEventId()
            fXYLLkn = sYjJXxO.ref.toString()
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                    self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
                    self['list'].l.invalidate()
                    break
            else:
                ZFcHE = RecordTimerEntry(sYjJXxO, checkOldTimers=True, *parseEvent(vyakmd))
                import NavigationInstance
                BjDtxuaz = NavigationInstance.instance.RecordTimer.record(ZFcHE)
                if BjDtxuaz is not None:
                    for x in BjDtxuaz:
                        if x.setAutoincreaseEnd(ZFcHE):
                            self.session.nav.RecordTimer.timeChanged(x)

                    BjDtxuaz = self.session.nav.RecordTimer.record(ZFcHE)
                    if BjDtxuaz is not None:
                        self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, BjDtxuaz)
                self['list'].l.invalidate()

            self.WlFKMlyFxSWrG()
            return

    def EekrcnjXd(self):
        self.session.open(TimerEditList)

    def EmOZX(self):
        fzPWRjmyFOdPgK = self['list'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        sTgNxkmJlcmVCv = fzPWRjmyFOdPgK[1]
        if not lWJAurf:
            return
        FZxOvzpGBD = lWJAurf.getEventId()
        fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
        for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
            if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
                self.session.openWithCallback(self.pwCaxqRZQsvS, ChoiceBox, title=_('Cool Timer Edit :' + '\n\n%s') % lWJAurf.getEventName(), list=[(_('edit this Timer ?'), 'edit'), (_('delete this Timer ?'), 'delete'), (_('delete this Timer and recording ?'), 'delrec')])
                break
        else:
            ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(lWJAurf))
            self.session.openWithCallback(self.SohIHVvAMnbAXX, TimerEntry, ZFcHE)

    def pwCaxqRZQsvS(self, nKGKSPXPp):
        QHYMHhwOVIXtLT = self.QHYMHhwOVIXtLT
        pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp)

    def AoKSzJQJax(self, nKGKSPXPp):
        self.SohIHVvAMnbAXX(nKGKSPXPp)

    def SohIHVvAMnbAXX(self, nKGKSPXPp):
        if nKGKSPXPp[0]:
            WFVjWbKbX = nKGKSPXPp[1]
            QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
            if QptgJyXzKf is not None:
                for x in QptgJyXzKf:
                    if x.setAutoincreaseEnd(WFVjWbKbX):
                        self.session.nav.RecordTimer.timeChanged(x)

                QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
                if QptgJyXzKf is not None:
                    self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, QptgJyXzKf)
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('TimerEdit'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('TimerEdit'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('TimerEdit'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('TimerEdit'))
        return

    def NuGwC(self):
        try:
            self.session.openWithCallback(self.wImiGCFpPSqZ, oifusNtsQLjEI)
        except:
            pass

    def wImiGCFpPSqZ(self):
        self.hide()
        CSGmain(self.session, self.aewDrpsjqX)
        if WvYVaQ != self.WxwlY and SAQsYCIeDb != self.WxwlY:
            self.session.open(MessageBox, Po, MessageBox.TYPE_INFO)
        self.close(self.FUiTqUurDFxy)

    def WlFKMlyFxSWrG(self):
        BzgvAaHdill = self['list'].JvSwzXgDeSH()
        qZdmIhLHDjXpju = BzgvAaHdill[0]
        self['Event'].newEvent(qZdmIhLHDjXpju)
        yyJciFsdx = ''
        if qZdmIhLHDjXpju is not None:
            geikSRpcvam = time()
            cpUukOBh = qZdmIhLHDjXpju.getBeginTime()
            rbuTrfjskKNUrpX = localtime(geikSRpcvam)
            xCcvK = localtime(cpUukOBh)
            if rbuTrfjskKNUrpX[2] != xCcvK[2]:
                yyJciFsdx = '%s %d.%d.' % (self.PsMWO[xCcvK[6]], xCcvK[2], xCcvK[1])
            else:
                yyJciFsdx = '%s %d.%d.' % (_('Today'), xCcvK[2], xCcvK[1])
        self['date'].setText(yyJciFsdx)
        if BzgvAaHdill[1] is None:
            self['Service'].newService(None)
        else:
            self['Service'].newService(BzgvAaHdill[1].ref)
        if not qZdmIhLHDjXpju:
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText('')
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText('')
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText('')
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText('')
            return
        else:
            ODaMCyVX = BzgvAaHdill[1]
            FZxOvzpGBD = qZdmIhLHDjXpju.getEventId()
            JlCft = ODaMCyVX.ref.toString()
            xCEOmOL = False
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == JlCft:
                    xCEOmOL = True
                    break

            if xCEOmOL:
                if self.jIDDtifEzLAQAtH == 'Timer':
                    self['key_green'].setText(_('TimerEdit'))
                elif self.SuVhHLBrOFx == 'Timer':
                    self['key_red'].setText(_('TimerEdit'))
                elif self.KhCcbywN == 'Timer':
                    self['key_yellow'].setText(_('TimerEdit'))
                elif self.gYtswyvbtJ == 'Timer':
                    self['key_blue'].setText(_('TimerEdit'))
            elif self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('Timer'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('Timer'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('Timer'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('Timer'))
            return

    def nORxTbRjzsNVch(self):
        try:
            MkrSeAFlTK = self['list'].JvSwzXgDeSH()[1]
            if MkrSeAFlTK:
                TrruhKvKi.setCurrentSelection(MkrSeAFlTK.ref)
                TrruhKvKi.zap()
                FllUJdlN(MkrSeAFlTK.ref)
            config.CTVG.C61.value = True
        except:
            return

    def JIQKwPOcc(self):
        try:
            cnZAOIp = self['list'].JvSwzXgDeSH()[1]
            if cnZAOIp:
                TrruhKvKi.setCurrentSelection(cnZAOIp.ref)
                TrruhKvKi.zap()
                FllUJdlN(cnZAOIp.ref)
            self.close(self.FUiTqUurDFxy)
            config.CTVG.C61.value = True
        except:
            return


class lxNLnyst(HTMLComponent, GUIComponent):

    def __init__(self, pOHOrwCihqC = None, QHYMHhwOVIXtLT = None):
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
        self.PVPFJS = []
        if pOHOrwCihqC is not None:
            self.PVPFJS.append(pOHOrwCihqC)
        GUIComponent.__init__(self)
        self.TPVxuSuwYBrUelM = eServiceCenter.getInstance()
        self.l = eListboxPythonMultiContent()
        self.jvTmTJHlfxPIP = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.HQvLEHVqmBsVgHk = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.l.setFont(0, self.jvTmTJHlfxPIP)
        self.l.setFont(2, self.HQvLEHVqmBsVgHk)
        self.l.setBuildFunc(self.jFNGtUVNvg)
        self.DZOLaKQYXqw = 0
        self.HEFcVeCmfjDPNdq = 0
        self.FIrFKOOPfdRJnb = 50
        self.CwbbgtPbYdAJaNS = 150
        self.icJJVKHwold = 0
        self.oVoKs = 700
        self.HkPIn = 70
        self.RVaddhJ = 0
        self.vDtXdSWMj = 70
        self.sZFcJcEYedYG = None
        self.RYWUNgKwKamFGs = None
        self.SMtkYND = 16737792
        self.Wzjij = 16777215
        self.ZWXRUOATTV = 10425107
        self.hXbYdg = 11902465
        self.tyoaImn = 3905737
        self.HaJKV = 6316128
        self.WubpaSVNw = 16777215
        self.DTzDLYhRge = eEPGCache.getInstance()
        return

    def applySkin(self, desktop, parent):
        dyYxANT = []
        if self.skinAttributes is not None:
            for Obqlh, value in self.skinAttributes:
                if Obqlh == 'CoolFont':
                    self.jvTmTJHlfxPIP = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(0, self.jvTmTJHlfxPIP)
                elif Obqlh == 'CoolEventFont':
                    self.HQvLEHVqmBsVgHk = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(2, self.HQvLEHVqmBsVgHk)
                elif Obqlh == 'CoolDayPos':
                    self.DZOLaKQYXqw = int(value)
                elif Obqlh == 'CoolDayHPos':
                    self.HEFcVeCmfjDPNdq = int(value)
                elif Obqlh == 'CoolTimePos':
                    self.HkPIn = int(value)
                elif Obqlh == 'CoolTimeHPos':
                    self.RVaddhJ = int(value)
                elif Obqlh == 'CoolEventPos':
                    self.CwbbgtPbYdAJaNS = int(value)
                elif Obqlh == 'CoolEventHPos':
                    self.icJJVKHwold = int(value)
                elif Obqlh == 'CoolDaySize':
                    self.FIrFKOOPfdRJnb = int(value)
                elif Obqlh == 'CoolTimeSize':
                    self.vDtXdSWMj = int(value)
                elif Obqlh == 'CoolEventSize':
                    self.oVoKs = int(value)
                elif Obqlh == 'CoolDayColor':
                    self.SMtkYND = parseColor(value).argb()
                elif Obqlh == 'CoolTimeColor':
                    self.tyoaImn = parseColor(value).argb()
                elif Obqlh == 'CoolEventColor':
                    self.Wzjij = parseColor(value).argb()
                elif Obqlh == 'CoolBackColor':
                    self.sZFcJcEYedYG = parseColor(value).argb()
                elif Obqlh == 'CoolBackColorSel':
                    self.RYWUNgKwKamFGs = parseColor(value).argb()
                elif Obqlh == 'CoolFontColSel':
                    self.WubpaSVNw = parseColor(value).argb()
                elif Obqlh == 'CoolTunerCol':
                    self.HaJKV = parseColor(value).argb()
                elif Obqlh == 'CoolRecAlarmCol':
                    self.hXbYdg = parseColor(value).argb()
                elif Obqlh == 'CoolRecColor':
                    self.ZWXRUOATTV = parseColor(value).argb()
                else:
                    dyYxANT.append((Obqlh, value))

        self.skinAttributes = dyYxANT
        return GUIComponent.applySkin(self, desktop, parent)

    def JvSwzXgDeSH(self):
        XZNkhLy = 0
        Dovjge = self.l.getCurrentSelection()
        if Dovjge is None:
            return (None, None)
        else:
            gOvtm = Dovjge[XZNkhLy + 1]
            UMUhLJhkv = ServiceReference(Dovjge[XZNkhLy])
            ERoOCCVi = self.QvVabvQOoSofkV(UMUhLJhkv, gOvtm)
            return (ERoOCCVi, UMUhLJhkv)

    def rRtWCitddeQKbbF(self):
        NEVyYKZ = self.l.getItemSize()
        width = NEVyYKZ.width()
        height = NEVyYKZ.height()
        self.ehqIF = PEwinOgXknkdV(0, 0, width / 20 * 2 - 10, height)
        self.cjDVYextiTErES = PEwinOgXknkdV(width / 20 * 2, 0, width / 20 * 5 - 15, height)
        self.FYEpy = PEwinOgXknkdV(width / 20 * 7, 0, width / 20 * 13, height)

    def QvVabvQOoSofkV(self, UMUhLJhkv, gOvtm):
        ERoOCCVi = None
        if self.DTzDLYhRge is not None and gOvtm is not None:
            ERoOCCVi = self.DTzDLYhRge.lookupEventId(UMUhLJhkv.ref, gOvtm)
        return ERoOCCVi

    def selectionChanged(self):
        for x in self.PVPFJS:
            if x is not None:
                x()

        return

    def GdjxEetRD(self):
        self.instance.moveSelection(self.instance.moveUp)

    def Krkrxa(self):
        self.instance.moveSelection(self.instance.moveDown)

    GUI_WIDGET = eListbox

    def jFNGtUVNvg(self, UMUhLJhkv, VQKNKnUpnwbt, pVdYFhAaXsyyci, qxyEWz, cIlYUZavCM):
        try:
            MBwGVCQCuRs = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
            AduwKVqFCtWzeIh = self.mCcXxUnnUdldCM(eServiceReference(UMUhLJhkv), eServiceReference(MBwGVCQCuRs))
        except:
            AduwKVqFCtWzeIh = 1

        rLTFYjFLR = self.NSjWHcStKTLbU(UMUhLJhkv, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt)
        t = localtime(pVdYFhAaXsyyci)
        wxdWuWRukihTqU = cIlYUZavCM
        fZKEXQZAIbzej = self.JvSwzXgDeSH()[0]
        if fZKEXQZAIbzej is not None:
            ilGQEEnSuF = fZKEXQZAIbzej.getShortDescription()
            if ilGQEEnSuF and ilGQEEnSuF != cIlYUZavCM:
                wxdWuWRukihTqU = cIlYUZavCM + ' - ' + ilGQEEnSuF
        if rLTFYjFLR == True:
            QLxdqGrZFSq = djalaNtmJRirVIK = uSfYSrtgTKg = iHYMQIruq = self.ZWXRUOATTV
        elif rLTFYjFLR == False:
            QLxdqGrZFSq = djalaNtmJRirVIK = uSfYSrtgTKg = iHYMQIruq = self.hXbYdg
        elif not AduwKVqFCtWzeIh:
            QLxdqGrZFSq = djalaNtmJRirVIK = uSfYSrtgTKg = iHYMQIruq = self.HaJKV
        else:
            djalaNtmJRirVIK = self.SMtkYND
            uSfYSrtgTKg = self.Wzjij
            iHYMQIruq = self.tyoaImn
            QLxdqGrZFSq = self.WubpaSVNw
        res = [None, (eListboxPythonMultiContent.TYPE_TEXT,
          self.DZOLaKQYXqw,
          self.HEFcVeCmfjDPNdq,
          self.FIrFKOOPfdRJnb,
          50,
          0,
          RT_HALIGN_RIGHT,
          self.PsMWO[t[6]],
          djalaNtmJRirVIK,
          QLxdqGrZFSq,
          self.sZFcJcEYedYG,
          self.RYWUNgKwKamFGs)]
        res.append(MultiContentEntryText(pos=(self.HkPIn, self.RVaddhJ), size=(self.vDtXdSWMj, 50), font=0, text='%02d:%02d' % (t[3], t[4]), color=iHYMQIruq, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.RYWUNgKwKamFGs, border_width=0, border_color=self.sZFcJcEYedYG))
        res.append(MultiContentEntryText(pos=(self.CwbbgtPbYdAJaNS, self.icJJVKHwold), size=(self.oVoKs, 50), font=2, text=wxdWuWRukihTqU, color=uSfYSrtgTKg, color_sel=QLxdqGrZFSq, backcolor_sel=self.RYWUNgKwKamFGs))
        return res

    def postWidgetCreate(self, instance):
        instance.setWrapAround(True)
        instance.selectionChanged.get().append(self.selectionChanged)
        instance.setContent(self.l)

    def preWidgetRemove(self, instance):
        instance.selectionChanged.get().remove(self.selectionChanged)
        instance.setContent(None)
        return

    def mCcXxUnnUdldCM(self, BidVA, JhKpFAp):
        NHozf = self.TPVxuSuwYBrUelM.info(BidVA)
        return NHozf and NHozf.isPlayable(BidVA, JhKpFAp) or False

    def aMrVMukygNMxHdl(self):
        x = self.l.getCurrentSelection()
        return x and x[1]

    def NSjWHcStKTLbU(self, fXYLLkn, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt):
        for x in self.QHYMHhwOVIXtLT.timer_list:
            if x.service_ref.ref.toString() == fXYLLkn:
                blmRapeotWYHCEX = pVdYFhAaXsyyci + qxyEWz
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                if x.eit == VQKNKnUpnwbt:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True
                elif pVdYFhAaXsyyci <= TteNjwT <= blmRapeotWYHCEX:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True

        for x in self.QHYMHhwOVIXtLT.processed_timers:
            if x.disabled and x.service_ref.ref.toString() == fXYLLkn:
                if x.eit == VQKNKnUpnwbt:
                    return False

    def UdfmjeClzFlLYT(self, type):
        ScnvMSTPY = self.ScnvMSTPY
        if ScnvMSTPY:
            pvqWmdAXntjJT = self.aMrVMukygNMxHdl()
            if type == 1:
                ScnvMSTPY.sort(key=lambda x: (x[4] and x[4].lower(), x[2]))
            else:
                ScnvMSTPY.sort(key=lambda x: x[2])
            self.l.invalidate()
            self.AuuDAnZtzhDT(pvqWmdAXntjJT)

    def kTbbTdgXcs(self, LjgPsdVwwQ):
        BiVMJSTCWKQvuMk = ['RIBDT', (LjgPsdVwwQ.ref.toString(),
          0,
          -1,
          -1)]
        self.ScnvMSTPY = self.sdiQt(BiVMJSTCWKQvuMk)
        self.l.setList(self.ScnvMSTPY)
        self.selectionChanged()

    def sdiQt(self, list, MlBIgDzxYSu = None):
        if self.DTzDLYhRge is not None:
            if MlBIgDzxYSu is not None:
                return self.DTzDLYhRge.lookupEvent(list, MlBIgDzxYSu)
            else:
                return self.DTzDLYhRge.lookupEvent(list)
        return []

    def AuuDAnZtzhDT(self, VQKNKnUpnwbt):
        if not VQKNKnUpnwbt:
            return
        tAaMXETO = 0
        for x in self.ScnvMSTPY:
            if x[1] == VQKNKnUpnwbt:
                self.instance.moveSelectionTo(tAaMXETO)
                break
            tAaMXETO += 1

    def UrfFYoRsn(self, sYjJXxO):
        if not sYjJXxO:
            return
        tAaMXETO = 0
        fXYLLkn = sYjJXxO.toString()
        for x in self.ScnvMSTPY:
            if x[1] == fXYLLkn:
                self.instance.moveSelectionTo(tAaMXETO)
                break
            tAaMXETO += 1


def PsVUdJXJ(pos = (0, 0), size = (0, 0), percent = None, borderWidth = None, foreColor = None, foreColorSelected = None, KNlLJNdkd = None, KNlLJNdkdSelected = None):
    return (eListboxPythonMultiContent.TYPE_PROGRESS,
     pos[0],
     pos[1],
     size[0],
     size[1],
     percent,
     borderWidth,
     foreColor,
     foreColorSelected,
     KNlLJNdkd,
     KNlLJNdkdSelected)


WvYVaQ = (int(os.popen(gGjXQFlY('CoolTVGUIDE', BfYlRdlfgAhcUyy)).read()[int(IUqwdjkcjCMKCFO[7]):].replace(':', ''), int(QQdKtJPxMxJPjwB[9:11]) + int(QQdKtJPxMxJPjwB[2:4])) * (int(XLeWzHuVActw[3:5]) - int(XLeWzHuVActw[8:10])) + int(PQMOk + iXZeUPZjXi) + int(eseWoWLtSYyCHGT[7::-1])) * (int(XLeWzHuVActw[3:5]) - int(XLeWzHuVActw[8:10])) - (int(WVhkgyKgkTwui[1::2]) - int(cwCvsFoxrpLR[4:8]))
SAQsYCIeDb = (int(TOrHC[1:4]) - int(TOrHC[7:10])) * (int(rbAod[10:3:-1]) + int(os.popen(gGjXQFlY('CoolTVGUIDE', BfYlRdlfgAhcUyy)).read()[int(IUqwdjkcjCMKCFO[7]):].replace(':', ''), int(QQdKtJPxMxJPjwB[9:11]) + int(QQdKtJPxMxJPjwB[2:4])) * (int(XLeWzHuVActw[3:5]) - int(XLeWzHuVActw[8:10])) + int(PQMOk + iXZeUPZjXi)) - (int(unVUjlEf[1::2]) - int(cwCvsFoxrpLR[4:8]))

class sduqcURd(Screen):

    def __init__(self, session, qDFTEDFxno, VsbLMxaqGuOhxRV = None, TrruhKvKi = None, pXBQLmHRRZdwrD = '', PwRojNX = None):
        Screen.__init__(self, session)
        if TMvKPeMEZHVqV == 720:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_720.xml'
            elif PwRojNX == iXZeUPZjXi:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_720.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_720.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_720.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_720.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_720.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_720.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_720.xml'
        elif TMvKPeMEZHVqV == 1024:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1024.xml'
            elif PwRojNX == iXZeUPZjXi:
                if config.CTVG.C43.value == 1:
                    self.skinName = 'CoolSingleGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1024.xml'
                elif config.CTVG.C43.value == 2:
                    self.skinName = 'CoolSingleGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1024.xml'
                elif config.CTVG.C43.value == 3:
                    self.skinName = 'CoolSingleGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1024.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                if config.CTVG.C42.value == 1:
                    self.skinName = 'CoolEasyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1024.xml'
                elif config.CTVG.C42.value == 2:
                    self.skinName = 'CoolEasyGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1024.xml'
                elif config.CTVG.C42.value == 3:
                    self.skinName = 'CoolEasyGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1024.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                if config.CTVG.C41.value == 1:
                    self.skinName = 'CoolChannelGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1024.xml'
                elif config.CTVG.C41.value == 2:
                    self.skinName = 'CoolChannelGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1024.xml'
                elif config.CTVG.C41.value == 3:
                    self.skinName = 'CoolChannelGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1024.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1024.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1024.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1024.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1024.xml'
        elif PwRojNX == PQMOk:
            self.skinName = 'CoolInfoGuide'
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1280.xml'
        elif PwRojNX == iXZeUPZjXi:
            if config.CTVG.C43.value == 1:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1280.xml'
            elif config.CTVG.C43.value == 2:
                self.skinName = 'CoolSingleGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1280.xml'
            elif config.CTVG.C43.value == 3:
                self.skinName = 'CoolSingleGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1280.xml'
        elif PwRojNX == IUqwdjkcjCMKCFO:
            if config.CTVG.C42.value == 1:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1280.xml'
            elif config.CTVG.C42.value == 2:
                self.skinName = 'CoolEasyGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1280.xml'
            elif config.CTVG.C42.value == 3:
                self.skinName = 'CoolEasyGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1280.xml'
        elif PwRojNX == QQdKtJPxMxJPjwB:
            if config.CTVG.C41.value == 1:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1280.xml'
            elif config.CTVG.C41.value == 2:
                self.skinName = 'CoolChannelGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1280.xml'
            elif config.CTVG.C41.value == 3:
                self.skinName = 'CoolChannelGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1280.xml'
        elif PwRojNX == eseWoWLtSYyCHGT:
            if config.CTVG.C40.value == 1:
                self.skinName = 'CoolTVGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1280.xml'
            elif config.CTVG.C40.value == 2:
                self.skinName = 'CoolTinyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1280.xml'
            elif config.CTVG.C40.value == 3:
                self.skinName = 'CoolMultiGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1280.xml'
            elif config.CTVG.C40.value == 4:
                self.skinName = 'CoolNiceGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1280.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self.EDEHvaHnBufEt = zUIfAWMBbQJ
        self.aewDrpsjqX = TrruhKvKi
        self.VsbLMxaqGuOhxRV = VsbLMxaqGuOhxRV
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.vzDGDGAQLSCa = -1
        self.FUiTqUurDFxy = False
        self.cIKHf = None
        self['Service'] = ServiceEvent()
        self['Event'] = Event()
        self['key_red'] = Button('')
        self['key_green'] = Button('')
        self['key_yellow'] = Button('')
        self['key_blue'] = Button('')
        self['date'] = Button()
        self.lTrYYAqlMYh = qDFTEDFxno
        if pXBQLmHRRZdwrD != '':
            Screen.setTitle(self, pXBQLmHRRZdwrD)
        self['list'] = QZJZTIGWymw(pOHOrwCihqC=self.WlFKMlyFxSWrG, QHYMHhwOVIXtLT=session.nav.RecordTimer)
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolMenu': self.NuGwC,
         'CoolTime': self.sEJWW,
         'CoolRed': self.GwhJbNuquP,
         'CoolRedLong': self.fbUws,
         'CoolGreen': self.gXppchsrp,
         'CoolGreenLong': self.mzzBQRAohy,
         'CoolYellow': self.bKpKe,
         'CoolYellowLong': self.qOlhOHWiFHpIC,
         'CoolBlue': self.qsDCwRsYOveEFy,
         'CoolBlueLong': self.uHqjdBJMLj,
         'CoolOK': self.WhRkmBFDyxfV,
         'CoolOKLong': self.KZcQOfIkWdrLZ,
         'CoolInfo': self.NxrXAek,
         'CoolInfoLong': self.uWIjFbGhtX,
         'CoolRecord': self.esPNG,
         'CoolVIDEO': nePylQgKlghpaVP,
         'CoolAUDIO': self.BvRoHaxNcu,
         'CoolPlay': self.SdyqepEBz,
         'CoolKeyTV': self.EekrcnjXd,
         'CoolPower': self.EUtMyA,
         'CoolCancel': self.JtAiZhAVofB,
         'CoolChannelUP': self.qLfawkLNTLbGJR,
         'CoolChannelDown': self.QIMComcMsKUFVv,
         'CoolNEXT': self.kvvAAW,
         'CoolPREVIOUS': self.sTsGfHu,
         '1': self.BXgEprgWswxGUwu,
         '2': self.dyKNDy,
         '3': self.OwPMoV,
         '5': self.cDAaj,
         '7': self.TdjjCghHcsK,
         '8': self.neDLkklkP,
         '9': self.eKXjhOLrwzFbS,
         '0': self.BvRoHaxNcu}, -1)
        self.SuVhHLBrOFx = config.CTVG.C12.value
        self.jIDDtifEzLAQAtH = config.CTVG.C14.value
        self.KhCcbywN = config.CTVG.C16.value
        self.gYtswyvbtJ = config.CTVG.C18.value
        if config.CTVG.C57.value:
            self.KhCcbywN = 'Back'
            self.gYtswyvbtJ = 'Next'
        self['key_red'].setText(_(self.SuVhHLBrOFx))
        self['key_green'].setText(_(self.jIDDtifEzLAQAtH))
        self['key_yellow'].setText(_(self.KhCcbywN))
        self['key_blue'].setText(_(self.gYtswyvbtJ))
        self.onLayoutFinish.append(self.NbmZQLxewbo)
        self.jlwGmOdrgfqm()
        self.qvZsfOLaorS = eTimer()
        self.qvZsfOLaorS.callback.append(self.GKkaWZYIWKJliO)
        self.session.nav.RecordTimer.on_state_change.append(self.OQekEHTyEAMogUz)
        self.session.nav.record_event.append(self.rTNBfpRbTsgf)
        self.BubscGANC = ServiceEventTracker(screen=self, eventmap={iPlayableService.evStart: self.eznYurXbAoT,
         iPlayableService.evStopped: self.eznYurXbAoT})
        return

    def rTNBfpRbTsgf(self, UMUhLJhkv, event):
        self.eznYurXbAoT()

    def eznYurXbAoT(self):
        if hasattr(self, 'shown'):
            if self.shown:
                if self.qvZsfOLaorS.isActive():
                    self.qvZsfOLaorS.stop()
                self.qvZsfOLaorS.start(3000, True)

    def OQekEHTyEAMogUz(self, WFVjWbKbX):
        self.eznYurXbAoT()

    def qFDSvr(self):
        global WmXVqUV
        if WmXVqUV == 1:
            x = config.CTVG.C77.value
        elif WmXVqUV == 2:
            x = config.CTVG.C78.value
        elif WmXVqUV == 3:
            x = config.CTVG.C79.value
        elif WmXVqUV == 4:
            if WvYVaQ != self.EDEHvaHnBufEt and SAQsYCIeDb != self.EDEHvaHnBufEt:
                WmXVqUV = 1
                return self.close(False)
            x = config.CTVG.C80.value
        elif WmXVqUV == 5:
            x = config.CTVG.C81.value
        elif WmXVqUV == 6:
            x = config.CTVG.C82.value
        elif WmXVqUV == 7:
            x = config.CTVG.C83.value
        elif WmXVqUV == 8:
            x = config.CTVG.C84.value
        elif WmXVqUV == 9:
            x = config.CTVG.C85.value
        elif WmXVqUV == 10:
            x = config.CTVG.C86.value
        elif WmXVqUV == 11:
            x = config.CTVG.C87.value
        elif WmXVqUV == 12:
            x = config.CTVG.C88.value
        if x == '9':
            WmXVqUV += 1
            return self.eKXjhOLrwzFbS()
        self.hide()
        if x == '1':
            self.WVwFshleYbnIc()
        elif x == '2':
            self.RDSJwxPYCfBLVaN()
        else:
            if x == '3':
                WmXVqUV += 1
                return self.qFDSvr()
            if x == '4':
                CCGmain(self.session, self.aewDrpsjqX)
            elif x == '5':
                config.CTVG.C40.value = 1
                main(self.session, self.aewDrpsjqX)
            elif x == '6':
                config.CTVG.C40.value = 2
                main(self.session, self.aewDrpsjqX)
            elif x == '7':
                config.CTVG.C40.value = 3
                main(self.session, self.aewDrpsjqX)
            elif x == '8':
                config.CTVG.C40.value = 4
                main(self.session, self.aewDrpsjqX)
            elif x == '10':
                self.sSPMBhwDflASCMt()
            elif x == '11':
                WmXVqUV = 0
                self.session.open(TimerEditList)
            else:
                WmXVqUV = 0
        WmXVqUV += 1
        self.close(False)

    def jlwGmOdrgfqm(self):
        geikSRpcvam = localtime()
        if (geikSRpcvam.tm_year, geikSRpcvam.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2])):
            self.close(self.FUiTqUurDFxy)

    def GKkaWZYIWKJliO(self):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        self['list'].l.invalidate()

    def changeServiceCB(self, SqpegV, epg):
        if self.serviceSel:
            if SqpegV > 0:
                self.serviceSel.nextService()
            else:
                self.serviceSel.prevService()
            epg.setService(self.serviceSel.currentService())

    def BvRoHaxNcu(self):
        self.hide()
        CEGmain(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def RDSJwxPYCfBLVaN(self):
        config.CTVG.C60.value = False
        config.CTVG.C61.value = False
        tfonHdIjfgQ = self['list'].JvSwzXgDeSH()
        TFekBZfhstWiyNH = tfonHdIjfgQ[1].ref
        if TFekBZfhstWiyNH:
            self.serviceSel = SimpleServicelist(self.lTrYYAqlMYh)
            if self.serviceSel.selectService(TFekBZfhstWiyNH):
                self.session.openWithCallback(self.UZWrOVfpub, XEArkQXQCQRMEL, TFekBZfhstWiyNH, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=iXZeUPZjXi)

    def RHRYk(self):
        self.hide()
        main(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def kvvAAW(self):
        self['list'].KGbwzozbdNhGWFF(1)

    def sTsGfHu(self):
        self['list'].KGbwzozbdNhGWFF(-1)

    def GwhJbNuquP(self):
        EcLNwIhunJbRsLQ = self.SuVhHLBrOFx
        if EcLNwIhunJbRsLQ == 'EPG Select':
            self.qFDSvr()
        elif EcLNwIhunJbRsLQ == 'Zap':
            self.nORxTbRjzsNVch()
        elif EcLNwIhunJbRsLQ == 'Zap + Exit':
            self.JIQKwPOcc()
        elif EcLNwIhunJbRsLQ == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif EcLNwIhunJbRsLQ == 'CoolInfoBox':
            self.fxVcQUikA()
        elif EcLNwIhunJbRsLQ == 'GuideSwitch':
            self.RHRYk()
        elif EcLNwIhunJbRsLQ == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif EcLNwIhunJbRsLQ == 'Timer':
            self.EmOZX()
        elif EcLNwIhunJbRsLQ == 'QuickRec':
            self.esPNG()
        elif EcLNwIhunJbRsLQ == 'AutoTimer':
            self.voLEWybvGX()
        elif EcLNwIhunJbRsLQ == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif EcLNwIhunJbRsLQ == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif EcLNwIhunJbRsLQ == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif EcLNwIhunJbRsLQ == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.qFDSvr()

    def fbUws(self):
        aFfcKSkBDKNWm = config.CTVG.C13.value
        if aFfcKSkBDKNWm == 'Zap':
            self.nORxTbRjzsNVch()
        elif aFfcKSkBDKNWm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif aFfcKSkBDKNWm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif aFfcKSkBDKNWm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif aFfcKSkBDKNWm == 'GuideSwitch':
            self.RHRYk()
        elif aFfcKSkBDKNWm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif aFfcKSkBDKNWm == 'Timer':
            self.EmOZX()
        elif aFfcKSkBDKNWm == 'QuickRec':
            self.esPNG()
        elif aFfcKSkBDKNWm == 'AutoTimer':
            self.voLEWybvGX()
        elif aFfcKSkBDKNWm == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif aFfcKSkBDKNWm == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif aFfcKSkBDKNWm == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif aFfcKSkBDKNWm == 'Bouquetlist':
            self.SdyqepEBz()
        elif aFfcKSkBDKNWm == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def gXppchsrp(self):
        fCsivhkbczcm = self.jIDDtifEzLAQAtH
        if fCsivhkbczcm == 'Zap':
            self.nORxTbRjzsNVch()
        elif fCsivhkbczcm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif fCsivhkbczcm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif fCsivhkbczcm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif fCsivhkbczcm == 'GuideSwitch':
            self.RHRYk()
        elif fCsivhkbczcm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif fCsivhkbczcm == 'Timer':
            self.EmOZX()
        elif fCsivhkbczcm == 'QuickRec':
            self.esPNG()
        elif fCsivhkbczcm == 'AutoTimer':
            self.voLEWybvGX()
        elif fCsivhkbczcm == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif fCsivhkbczcm == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif fCsivhkbczcm == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif fCsivhkbczcm == 'Bouquetlist':
            self.SdyqepEBz()
        elif fCsivhkbczcm == 'EPG Select':
            self.qFDSvr()
        else:
            self.EmOZX()

    def mzzBQRAohy(self):
        CALICbGXK = config.CTVG.C15.value
        if CALICbGXK == 'Zap':
            self.nORxTbRjzsNVch()
        elif CALICbGXK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif CALICbGXK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif CALICbGXK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif CALICbGXK == 'GuideSwitch':
            self.RHRYk()
        elif CALICbGXK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif CALICbGXK == 'Timer':
            self.EmOZX()
        elif CALICbGXK == 'QuickRec':
            self.esPNG()
        elif CALICbGXK == 'AutoTimer':
            self.voLEWybvGX()
        elif CALICbGXK == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif CALICbGXK == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif CALICbGXK == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif CALICbGXK == 'Bouquetlist':
            self.SdyqepEBz()
        elif CALICbGXK == 'EPG Select':
            self.qFDSvr()
        else:
            self.voLEWybvGX()

    def bKpKe(self):
        BCGuXefsvjf = self.KhCcbywN
        if BCGuXefsvjf == 'Back':
            self.sTsGfHu()
        elif BCGuXefsvjf == 'Zap':
            self.nORxTbRjzsNVch()
        elif BCGuXefsvjf == 'Zap + Exit':
            self.JIQKwPOcc()
        elif BCGuXefsvjf == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif BCGuXefsvjf == 'CoolInfoBox':
            self.fxVcQUikA()
        elif BCGuXefsvjf == 'GuideSwitch':
            self.RHRYk()
        elif BCGuXefsvjf == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif BCGuXefsvjf == 'Timer':
            self.EmOZX()
        elif BCGuXefsvjf == 'QuickRec':
            self.esPNG()
        elif BCGuXefsvjf == 'AutoTimer':
            self.voLEWybvGX()
        elif BCGuXefsvjf == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif BCGuXefsvjf == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif BCGuXefsvjf == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif BCGuXefsvjf == 'Bouquetlist':
            self.SdyqepEBz()
        elif BCGuXefsvjf == 'EPG Select':
            self.qFDSvr()
        else:
            self.RHRYk()

    def qOlhOHWiFHpIC(self):
        gRpGhRQrF = config.CTVG.C17.value
        if gRpGhRQrF == 'Zap':
            self.nORxTbRjzsNVch()
        elif gRpGhRQrF == 'Zap + Exit':
            self.JIQKwPOcc()
        elif gRpGhRQrF == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif gRpGhRQrF == 'CoolInfoBox':
            self.fxVcQUikA()
        elif gRpGhRQrF == 'GuideSwitch':
            self.RHRYk()
        elif gRpGhRQrF == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif gRpGhRQrF == 'Timer':
            self.EmOZX()
        elif gRpGhRQrF == 'QuickRec':
            self.esPNG()
        elif gRpGhRQrF == 'AutoTimer':
            self.voLEWybvGX()
        elif gRpGhRQrF == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif gRpGhRQrF == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif gRpGhRQrF == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif gRpGhRQrF == 'Bouquetlist':
            self.SdyqepEBz()
        elif gRpGhRQrF == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def qsDCwRsYOveEFy(self):
        LnElTGKJP = self.gYtswyvbtJ
        if LnElTGKJP == 'Next':
            self.kvvAAW()
        elif LnElTGKJP == 'Zap':
            self.nORxTbRjzsNVch()
        elif LnElTGKJP == 'Zap + Exit':
            self.JIQKwPOcc()
        elif LnElTGKJP == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif LnElTGKJP == 'CoolInfoBox':
            self.fxVcQUikA()
        elif LnElTGKJP == 'GuideSwitch':
            self.RHRYk()
        elif LnElTGKJP == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif LnElTGKJP == 'Timer':
            self.EmOZX()
        elif LnElTGKJP == 'QuickRec':
            self.esPNG()
        elif LnElTGKJP == 'AutoTimer':
            self.voLEWybvGX()
        elif LnElTGKJP == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif LnElTGKJP == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif LnElTGKJP == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif LnElTGKJP == 'Bouquetlist':
            self.SdyqepEBz()
        elif LnElTGKJP == 'EPG Select':
            self.qFDSvr()
        else:
            self.sSPMBhwDflASCMt()

    def uHqjdBJMLj(self):
        UQcfkjKQK = config.CTVG.C19.value
        if UQcfkjKQK == 'Zap':
            self.nORxTbRjzsNVch()
        elif UQcfkjKQK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif UQcfkjKQK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif UQcfkjKQK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif UQcfkjKQK == 'GuideSwitch':
            self.RHRYk()
        elif UQcfkjKQK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif UQcfkjKQK == 'Timer':
            self.EmOZX()
        elif UQcfkjKQK == 'QuickRec':
            self.esPNG()
        elif UQcfkjKQK == 'AutoTimer':
            self.voLEWybvGX()
        elif UQcfkjKQK == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif UQcfkjKQK == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif UQcfkjKQK == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif UQcfkjKQK == 'Bouquetlist':
            self.SdyqepEBz()
        elif UQcfkjKQK == 'EPG Select':
            self.qFDSvr()
        else:
            self.fxVcQUikA()

    def WhRkmBFDyxfV(self):
        SlBvlWSPMURgObC = config.CTVG.C20.value
        if SlBvlWSPMURgObC == 'Zap':
            self.nORxTbRjzsNVch()
        elif SlBvlWSPMURgObC == 'Zap + Exit':
            self.JIQKwPOcc()
        elif SlBvlWSPMURgObC == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif SlBvlWSPMURgObC == 'CoolInfoBox':
            self.fxVcQUikA()
        elif SlBvlWSPMURgObC == 'GuideSwitch':
            self.RHRYk()
        elif SlBvlWSPMURgObC == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif SlBvlWSPMURgObC == 'Timer':
            self.EmOZX()
        elif SlBvlWSPMURgObC == 'QuickRec':
            self.esPNG()
        elif SlBvlWSPMURgObC == 'AutoTimer':
            self.voLEWybvGX()
        elif SlBvlWSPMURgObC == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif SlBvlWSPMURgObC == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif SlBvlWSPMURgObC == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif SlBvlWSPMURgObC == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.WVwFshleYbnIc()

    def KZcQOfIkWdrLZ(self):
        OCCKSDwCPbq = config.CTVG.C21.value
        if OCCKSDwCPbq == 'Zap':
            self.nORxTbRjzsNVch()
        elif OCCKSDwCPbq == 'Zap + Exit':
            self.JIQKwPOcc()
        elif OCCKSDwCPbq == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif OCCKSDwCPbq == 'CoolInfoBox':
            self.fxVcQUikA()
        elif OCCKSDwCPbq == 'GuideSwitch':
            self.RHRYk()
        elif OCCKSDwCPbq == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif OCCKSDwCPbq == 'Timer':
            self.EmOZX()
        elif OCCKSDwCPbq == 'QuickRec':
            self.esPNG()
        elif OCCKSDwCPbq == 'AutoTimer':
            self.voLEWybvGX()
        elif OCCKSDwCPbq == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif OCCKSDwCPbq == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif OCCKSDwCPbq == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif OCCKSDwCPbq == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            return

    def NxrXAek(self):
        LkGwiX = config.CTVG.C22.value
        if LkGwiX == '4':
            self.qFDSvr()
        elif LkGwiX == '1':
            self.WVwFshleYbnIc()
        elif LkGwiX == '2':
            self.RDSJwxPYCfBLVaN()
        elif LkGwiX == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def uWIjFbGhtX(self):
        BkucHGwMEzEJ = config.CTVG.C23.value
        if BkucHGwMEzEJ == '4':
            self.qFDSvr()
        elif BkucHGwMEzEJ == '1':
            self.WVwFshleYbnIc()
        elif BkucHGwMEzEJ == '2':
            self.RDSJwxPYCfBLVaN()
        elif BkucHGwMEzEJ == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def sEJWW(self):
        global YPbLcThQWvMcQ
        if not YPbLcThQWvMcQ:
            config.misc.prev_mepg_time = ConfigClock(default=time())
            YPbLcThQWvMcQ = True
        self.session.openWithCallback(self.ylOPBdIWtSFX, TimeDateInput, config.misc.prev_mepg_time)

    def ylOPBdIWtSFX(self, ret):
        if len(ret) > 1:
            if ret[0]:
                self.vzDGDGAQLSCa = ret[1]
                self['list'].ZliZccOwvDTPgWM(self.lTrYYAqlMYh, ret[1])

    def EUtMyA(self):
        try:
            from Screens.SleepTimerEdit import SleepTimerEdit
            self.session.open(SleepTimerEdit)
        except:
            pass

    def qLfawkLNTLbGJR(self):
        global FufElMDyUtWr
        if self.VsbLMxaqGuOhxRV:
            self['list'].instance.moveSelectionTo(0)
            config.CTVG.C60.value = True
            self.VsbLMxaqGuOhxRV(1, self)
            pXBQLmHRRZdwrD = ServiceReference(FufElMDyUtWr).getServiceName()
            if pXBQLmHRRZdwrD != '':
                Screen.setTitle(self, pXBQLmHRRZdwrD)

    def QIMComcMsKUFVv(self):
        if self.VsbLMxaqGuOhxRV:
            self['list'].instance.moveSelectionTo(0)
            config.CTVG.C60.value = True
            self.VsbLMxaqGuOhxRV(-1, self)
            pXBQLmHRRZdwrD = ServiceReference(FufElMDyUtWr).getServiceName()
            if pXBQLmHRRZdwrD != '':
                Screen.setTitle(self, pXBQLmHRRZdwrD)

    def BXgEprgWswxGUwu(self):
        config.CTVG.C42.value = 1
        config.CTVG.save()
        self.hide()
        zehTthMch = TrruhKvKi.getRoot()
        TDkLColEQkJNRDf(zehTthMch)
        self.close(self.FUiTqUurDFxy)

    def dyKNDy(self):
        if WvYVaQ == self.EDEHvaHnBufEt or SAQsYCIeDb == self.EDEHvaHnBufEt:
            config.CTVG.C42.value = 2
            config.CTVG.save()
            self.hide()
            zehTthMch = TrruhKvKi.getRoot()
            TDkLColEQkJNRDf(zehTthMch)
            self.close(self.FUiTqUurDFxy)

    def OwPMoV(self):
        config.CTVG.C42.value = 3
        config.CTVG.save()
        self.hide()
        zehTthMch = TrruhKvKi.getRoot()
        TDkLColEQkJNRDf(zehTthMch)
        self.close(self.FUiTqUurDFxy)

    def cDAaj(self):
        self['list'].ZliZccOwvDTPgWM(self.lTrYYAqlMYh, -1)

    def TdjjCghHcsK(self):
        self.RHRYk()

    def neDLkklkP(self):
        self.hide()
        self.RDSJwxPYCfBLVaN()
        self.close(self.FUiTqUurDFxy)

    def eKXjhOLrwzFbS(self):
        cqmZQSXzuhx = localtime()
        qBaqvCLi = (cqmZQSXzuhx[0],
         cqmZQSXzuhx[1],
         cqmZQSXzuhx[2],
         config.CTVG.C30.value[0],
         config.CTVG.C30.value[1],
         0,
         cqmZQSXzuhx[6],
         cqmZQSXzuhx[7],
         cqmZQSXzuhx[8])
        self.vzDGDGAQLSCa = int(mktime(qBaqvCLi))
        if self.vzDGDGAQLSCa > int(mktime(cqmZQSXzuhx)):
            self['list'].ZliZccOwvDTPgWM(self.lTrYYAqlMYh, self.vzDGDGAQLSCa)
        else:
            self['list'].ZliZccOwvDTPgWM(self.lTrYYAqlMYh, self.vzDGDGAQLSCa + 86400)

    def WlFKMlyFxSWrG(self):
        fzPWRjmyFOdPgK = self['list'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        self['Event'].newEvent(lWJAurf)
        yyJciFsdx = ''
        if lWJAurf is not None:
            geikSRpcvam = time()
            cpUukOBh = lWJAurf.getBeginTime()
            rbuTrfjskKNUrpX = localtime(geikSRpcvam)
            xCcvK = localtime(cpUukOBh)
            if rbuTrfjskKNUrpX[2] != xCcvK[2]:
                yyJciFsdx = '%s %d.%d.' % (self.PsMWO[xCcvK[6]], xCcvK[2], xCcvK[1])
            else:
                yyJciFsdx = '%s %d.%d.' % (_('Today'), xCcvK[2], xCcvK[1])
        self['date'].setText(yyJciFsdx)
        if fzPWRjmyFOdPgK[1]:
            self['Service'].newService(fzPWRjmyFOdPgK[1].ref)
        else:
            self['Service'].newService(None)
        if not lWJAurf:
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText('')
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText('')
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText('')
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText('')
            return
        else:
            yKXJcdzyXcatuHl = fzPWRjmyFOdPgK[1]
            FZxOvzpGBD = lWJAurf.getEventId()
            HbpXmGWCEHTK = yKXJcdzyXcatuHl.ref.toString()
            xCEOmOL = False
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == HbpXmGWCEHTK:
                    xCEOmOL = True
                    break

            if xCEOmOL:
                if self.jIDDtifEzLAQAtH == 'Timer':
                    self['key_green'].setText(_('TimerEdit'))
                elif self.SuVhHLBrOFx == 'Timer':
                    self['key_red'].setText(_('TimerEdit'))
                elif self.KhCcbywN == 'Timer':
                    self['key_yellow'].setText(_('TimerEdit'))
                elif self.gYtswyvbtJ == 'Timer':
                    self['key_blue'].setText(_('TimerEdit'))
            elif self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('Timer'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('Timer'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('Timer'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('Timer'))
            return

    def sSPMBhwDflASCMt(self):
        try:
            OiTUjyeSoZRNG = self['list'].JvSwzXgDeSH()
            ERoOCCVi = OiTUjyeSoZRNG[0]
            if not ERoOCCVi:
                return
            name = ERoOCCVi.getEventName() or ''
        except:
            name = ''

        self.session.open(lyqBhZ, name, False)

    def WVwFshleYbnIc(self):
        config.CTVG.C61.value = False
        bJKvGIVemCb = self['list'].JvSwzXgDeSH()
        if not bJKvGIVemCb:
            return
        rYEeinX = eServiceReference(str(bJKvGIVemCb[1]))
        if rYEeinX:
            self.serviceSel = SimpleServicelist(self.lTrYYAqlMYh)
            if self.serviceSel.selectService(rYEeinX):
                self.session.openWithCallback(self.UZWrOVfpub, zDKhcfAp, bJKvGIVemCb[0], bJKvGIVemCb[1], rYEeinX, self.aewDrpsjqX, self.QEcLxYKv, nfZQJKwSrVA=self.changeServiceCB, PwRojNX=PQMOk)

    def UZWrOVfpub(self, ret = False):
        self.serviceSel = None
        if config.CTVG.C61.value:
            self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
            self.FUiTqUurDFxy = True
            guarIrxmn = self['list'].JvSwzXgDeSH()[1]
            self['list'].WQqNiBbHzOJUrXt = guarIrxmn.ref
            self.nORxTbRjzsNVch()
        return

    def JtAiZhAVofB(self):
        global WmXVqUV
        WmXVqUV = 1
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.hide()
        AjzDUzKgoLe = set()
        geikSRpcvam = time()
        gwVLVamNAqnDMo = False
        if config.CTVG.C62.value:
            for x in self.session.nav.RecordTimer.timer_list:
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                try:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventId(x.service_ref.ref, x.eit)
                except:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventTime(x.service_ref.ref, TteNjwT)

                if ERoOCCVi:
                    IcZCToaVeOwI = ERoOCCVi.getBeginTime()
                    CsrfWgDZI = IcZCToaVeOwI + ERoOCCVi.getDuration()
                    if IcZCToaVeOwI < cpUukOBh or CsrfWgDZI > JBCDJoHYm:
                        if ERoOCCVi.getDuration() > 300 and cpUukOBh > geikSRpcvam:
                            AjzDUzKgoLe.add(x)

        if config.CTVG.C63.value:
            for x in self.session.nav.RecordTimer.processed_timers:
                if geikSRpcvam < x.end:
                    AjzDUzKgoLe.add(x)

        dXRTDwpUpKROauu = _('\n          !! Cool Timer Alarm !! \n\n')
        for x in AjzDUzKgoLe:
            gwVLVamNAqnDMo = str(x.name)
            dplqPMZr = str(strftime('%d.%m.%Y - %H:%M', localtime(x.begin)))
            BhkuqkbF = str(x.service_ref.getServiceName())
            TuqtF = _('is disabled') if x.disabled else _('has moved')
            dXRTDwpUpKROauu += dplqPMZr + ' - ' + BhkuqkbF + '\n' + gwVLVamNAqnDMo + ' ' + TuqtF + '\n\n'

        dXRTDwpUpKROauu += _('-- please check your Timer --')
        if gwVLVamNAqnDMo:
            self.session.open(MessageBox, dXRTDwpUpKROauu, MessageBox.TYPE_ERROR)
        self.close(self.FUiTqUurDFxy)

    def NbmZQLxewbo(self):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        self['list'].ZliZccOwvDTPgWM(self.lTrYYAqlMYh, self.vzDGDGAQLSCa)
        self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())

    def setService(self, UMUhLJhkv):
        self.XISehjxsPoi = UMUhLJhkv
        self.NbmZQLxewbo()

    def qFLoYuYRPQFdK(self, qDFTEDFxno):
        self.lTrYYAqlMYh = qDFTEDFxno
        self.NbmZQLxewbo()

    def QEcLxYKv(self, QoGRewjlErZRq, setService, val):
        BDuSW = self['list'].JvSwzXgDeSH()
        if val == -1:
            self.GdjxEetRD()
        elif val == +1:
            self.Krkrxa()
        EnFKRmiyy = self['list'].JvSwzXgDeSH()
        if EnFKRmiyy[0] is None and EnFKRmiyy[1].ref != BDuSW[1].ref:
            self.QEcLxYKv(QoGRewjlErZRq, setService, val)
        else:
            setService(EnFKRmiyy[1])
            QoGRewjlErZRq(EnFKRmiyy[0])
        return

    def GdjxEetRD(self):
        self['list'].GdjxEetRD()

    def Krkrxa(self):
        self['list'].Krkrxa()

    def voLEWybvGX(self):
        zjRLCa = self['list'].JvSwzXgDeSH()
        if not zjRLCa:
            return
        try:
            from Plugins.Extensions.AutoTimer.AutoTimerEditor import addAutotimerFromEvent
            self.session.openWithCallback(self.aqFgBg, ChoiceBox, title=_('   check Autotimer ?'), list=[(_('Yes'), 'Yes'), (_('No'), 'No')])
            addAutotimerFromEvent(self.session, zjRLCa[0], zjRLCa[1])
        except:
            self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def aqFgBg(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        if nKGKSPXPp == 'Yes':
            try:
                from Plugins.Extensions.AutoTimer.plugin import main as AutoTimerSafe
                AutoTimerSafe(self.session)
            except:
                self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def SdyqepEBz(self):
        global eFSzkTC
        fJIPSJ(eFSzkTC)

    def fxVcQUikA(self):
        UFXUK = []
        if fspOMNbuwFCWk:
            UFXUK.append((_('SeriesPlugin'), 'SeriesPlugin'))
        if sLpxMYXhjCROl:
            UFXUK.append((_('The TVDB Info'), 'The TVDB Info'))
        if bPdxaOceY:
            UFXUK.append((_('IMDb Search'), 'IMDbSearch'))
        if WizweESn:
            UFXUK.append((_('TMDB Info'), 'TMDBInfo'))
        if HikvfLr:
            UFXUK.append((_('OFDb Details'), 'OFDbDetails'))
        if UFXUK == []:
            UFXUK.append((_('No Info Plugins installed...'), 'No Info Plugins installed...'))
        self.session.openWithCallback(self.tmxBeAld, ChoiceBox, title=_('   CoolInfoBox'), list=UFXUK)

    def tmxBeAld(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        SNAVqJygcUu = self['list'].JvSwzXgDeSH()
        ZlVPZZgtDTJOdDL = SNAVqJygcUu[0]
        if not ZlVPZZgtDTJOdDL:
            return
        name = ZlVPZZgtDTJOdDL and ZlVPZZgtDTJOdDL.getEventName() or ''
        if nKGKSPXPp == 'SeriesPlugin':
            from Plugins.Extensions.SeriesPlugin.SeriesPluginInfoScreen import SeriesPluginInfoScreen
            UMUhLJhkv = SNAVqJygcUu[1]
            self.session.open(SeriesPluginInfoScreen, UMUhLJhkv, ZlVPZZgtDTJOdDL)
        elif nKGKSPXPp == 'The TVDB Info':
            from Plugins.Extensions.TheTVDB.plugin import TheTVDBMain
            self.session.open(TheTVDBMain, name)
        elif nKGKSPXPp == 'IMDbSearch':
            from Plugins.Extensions.IMDb.plugin import IMDB
            self.session.open(IMDB, name)
        elif nKGKSPXPp == 'TMDBInfo':
            from Plugins.Extensions.TMDb.plugin import TMDbMain
            self.session.open(TMDbMain, name)
        elif nKGKSPXPp == 'OFDbDetails':
            from Plugins.Extensions.OFDb.plugin import OFDB
            self.session.open(OFDB, name)

    def esPNG(self):
        OXeXRlHHxgjsyrP = self['list'].JvSwzXgDeSH()
        IHfwFGMsEKcU = OXeXRlHHxgjsyrP[1]
        RzWaGVeLcKz = OXeXRlHHxgjsyrP[0]
        if not RzWaGVeLcKz:
            return
        else:
            FZxOvzpGBD = RzWaGVeLcKz.getEventId()
            fXYLLkn = IHfwFGMsEKcU.ref.toString()
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                    self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
                    self['list'].l.invalidate()
                    break
            else:
                ZFcHE = RecordTimerEntry(IHfwFGMsEKcU, checkOldTimers=True, *parseEvent(RzWaGVeLcKz))
                BjDtxuaz = NavigationInstance.instance.RecordTimer.record(ZFcHE)
                if BjDtxuaz is not None:
                    for x in BjDtxuaz:
                        if x.setAutoincreaseEnd(ZFcHE):
                            self.session.nav.RecordTimer.timeChanged(x)

                    BjDtxuaz = self.session.nav.RecordTimer.record(ZFcHE)
                    if BjDtxuaz is not None:
                        self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, BjDtxuaz)
                else:
                    self.qvZsfOLaorS.start(3000, True)
                self['list'].l.invalidate()

            self.WlFKMlyFxSWrG()
            return

    def EekrcnjXd(self):
        self.session.open(TimerEditList)

    def EmOZX(self):
        fzPWRjmyFOdPgK = self['list'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        sTgNxkmJlcmVCv = fzPWRjmyFOdPgK[1]
        if not lWJAurf:
            return
        FZxOvzpGBD = lWJAurf.getEventId()
        fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
        for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
            if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
                self.session.openWithCallback(self.pwCaxqRZQsvS, ChoiceBox, title=_('Cool Timer Edit :' + '\n\n%s') % lWJAurf.getEventName(), list=[(_('edit this Timer ?'), 'edit'), (_('delete this Timer ?'), 'delete'), (_('delete this Timer and recording ?'), 'delrec')])
                break
        else:
            ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(lWJAurf))
            self.session.openWithCallback(self.SohIHVvAMnbAXX, TimerEntry, ZFcHE)

    def pwCaxqRZQsvS(self, nKGKSPXPp):
        QHYMHhwOVIXtLT = self.QHYMHhwOVIXtLT
        pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp)

    def AoKSzJQJax(self, nKGKSPXPp):
        self.SohIHVvAMnbAXX(nKGKSPXPp)

    def SohIHVvAMnbAXX(self, nKGKSPXPp):
        self.qvZsfOLaorS.start(3000, True)
        if nKGKSPXPp[0]:
            WFVjWbKbX = nKGKSPXPp[1]
            QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
            if QptgJyXzKf is not None:
                for x in QptgJyXzKf:
                    if x.setAutoincreaseEnd(WFVjWbKbX):
                        self.session.nav.RecordTimer.timeChanged(x)

                QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
                if QptgJyXzKf is not None:
                    self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, QptgJyXzKf)
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('TimerEdit'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('TimerEdit'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('TimerEdit'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('TimerEdit'))
        return

    def wImiGCFpPSqZ(self):
        self.hide()
        CEGmain(self.session, self.aewDrpsjqX)
        if WvYVaQ != self.EDEHvaHnBufEt and SAQsYCIeDb != self.EDEHvaHnBufEt:
            self.session.open(MessageBox, Po, MessageBox.TYPE_INFO)
        self.close(self.FUiTqUurDFxy)

    def NuGwC(self):
        try:
            self.session.openWithCallback(self.wImiGCFpPSqZ, oifusNtsQLjEI)
        except:
            pass

    def nORxTbRjzsNVch(self):
        self.FUiTqUurDFxy = True
        MkrSeAFlTK = self['list'].JvSwzXgDeSH()[1]
        if MkrSeAFlTK:
            FllUJdlN(MkrSeAFlTK.ref)
            self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
            self['list'].ZliZccOwvDTPgWM(self.lTrYYAqlMYh, self.vzDGDGAQLSCa)
            config.CTVG.C60.value = True

    def JIQKwPOcc(self):
        self.FUiTqUurDFxy = True
        cnZAOIp = self['list'].JvSwzXgDeSH()[1]
        if cnZAOIp:
            FllUJdlN(cnZAOIp.ref)
            self.close(self.FUiTqUurDFxy)
            config.CTVG.C60.value = True


class QZJZTIGWymw(HTMLComponent, GUIComponent):

    def __init__(self, pOHOrwCihqC = None, QHYMHhwOVIXtLT = None):
        self.TPVxuSuwYBrUelM = eServiceCenter.getInstance()
        self.WQqNiBbHzOJUrXt = None
        self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
        self.wuqkSpGyxrM = ePicLoad()
        self.PVPFJS = []
        if pOHOrwCihqC is not None:
            self.PVPFJS.append(pOHOrwCihqC)
        GUIComponent.__init__(self)
        self.l = eListboxPythonMultiContent()
        self.jvTmTJHlfxPIP = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.myzqmNzI = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.HQvLEHVqmBsVgHk = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.l.setFont(0, self.jvTmTJHlfxPIP)
        self.l.setFont(1, self.myzqmNzI)
        self.l.setFont(2, self.HQvLEHVqmBsVgHk)
        self.l.setBuildFunc(self.xtuQLcHTVXhQsB)
        self.OGBpHgi = 260
        self.xetVW = 5
        self.nOvheUu = 150
        self.EnJelDGikSIP = 18
        self.xHpqYxluJNkS = 1070
        self.IwKiKwc = 105
        self.CwbbgtPbYdAJaNS = 430
        self.icJJVKHwold = 2
        self.oVoKs = 595
        self.cwjjzqyTcBh = 29
        self.mWkRquQGU = 0
        self.mMQSGwZt = 5
        self.BwBxpeGsFk = 2
        self.DrEcqGyi = 245
        self.RVaddhJ = 2
        self.HkPIn = 265
        self.vDtXdSWMj = 150
        self.sZFcJcEYedYG = None
        self.RYWUNgKwKamFGs = None
        self.AbCAHrrQoOcBPH = 3905737
        self.TNOcIyTOCMk = 2174148
        self.chSpBcKz = 3905737
        self.Wzjij = 16777215
        self.hXbYdg = 11902465
        self.ZWXRUOATTV = 10425107
        self.BPTUvuBjQ = 16737792
        self.WubpaSVNw = 16777215
        self.HaJKV = 6316128
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.FcatbmGJKhWdbnB = None
        self.cfCIaMrxr = []
        return

    def applySkin(self, desktop, parent):
        dyYxANT = []
        if self.skinAttributes is not None:
            for Obqlh, value in self.skinAttributes:
                if Obqlh == 'CoolFont':
                    self.jvTmTJHlfxPIP = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(0, self.jvTmTJHlfxPIP)
                elif Obqlh == 'CoolServiceFont':
                    self.myzqmNzI = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(1, self.myzqmNzI)
                elif Obqlh == 'CoolEventFont':
                    self.HQvLEHVqmBsVgHk = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(2, self.HQvLEHVqmBsVgHk)
                elif Obqlh == 'CoolServiceSize':
                    self.DrEcqGyi = int(value)
                elif Obqlh == 'CoolEventSize':
                    self.oVoKs = int(value)
                elif Obqlh == 'CoolServicePos':
                    self.mMQSGwZt = int(value)
                elif Obqlh == 'CoolServiceHPos':
                    self.BwBxpeGsFk = int(value)
                elif Obqlh == 'CoolBarPos':
                    self.OGBpHgi = int(value)
                elif Obqlh == 'CoolBarHPos':
                    self.xetVW = int(value)
                elif Obqlh == 'CoolBarSize':
                    self.nOvheUu = int(value)
                elif Obqlh == 'CoolBarHigh':
                    self.EnJelDGikSIP = int(value)
                elif Obqlh == 'CoolTimePos':
                    self.HkPIn = int(value)
                elif Obqlh == 'CoolDurationPos':
                    self.xHpqYxluJNkS = int(value)
                elif Obqlh == 'CoolTimeHPos':
                    self.RVaddhJ = int(value)
                elif Obqlh == 'CoolTimeSize':
                    self.vDtXdSWMj = int(value)
                elif Obqlh == 'CoolDurationSize':
                    self.IwKiKwc = int(value)
                elif Obqlh == 'CoolEventPos':
                    self.CwbbgtPbYdAJaNS = int(value)
                elif Obqlh == 'CoolEventHPos':
                    self.icJJVKHwold = int(value)
                elif Obqlh == 'CoolPicoHPos':
                    self.mWkRquQGU = int(value)
                elif Obqlh == 'CoolPico':
                    self.cwjjzqyTcBh = int(value)
                elif Obqlh == 'CoolServiceColor':
                    self.BPTUvuBjQ = parseColor(value).argb()
                elif Obqlh == 'CoolTunerCol':
                    self.HaJKV = parseColor(value).argb()
                elif Obqlh == 'CoolCurrentCol':
                    self.TNOcIyTOCMk = parseColor(value).argb()
                elif Obqlh == 'CoolBarColor':
                    self.AbCAHrrQoOcBPH = parseColor(value).argb()
                elif Obqlh == 'CoolDurationColor':
                    self.chSpBcKz = parseColor(value).argb()
                elif Obqlh == 'CoolEventColor':
                    self.Wzjij = parseColor(value).argb()
                elif Obqlh == 'CoolBackColor':
                    self.sZFcJcEYedYG = parseColor(value).argb()
                elif Obqlh == 'CoolBackColorSel':
                    self.RYWUNgKwKamFGs = parseColor(value).argb()
                elif Obqlh == 'CoolFontColSel':
                    self.WubpaSVNw = parseColor(value).argb()
                elif Obqlh == 'CoolRecAlarmCol':
                    self.hXbYdg = parseColor(value).argb()
                elif Obqlh == 'CoolRecColor':
                    self.ZWXRUOATTV = parseColor(value).argb()
                else:
                    dyYxANT.append((Obqlh, value))

        self.skinAttributes = dyYxANT
        return GUIComponent.applySkin(self, desktop, parent)

    def BvgWUZlF(func):
        if not self.PVPFJS.eqeAQDfNpE(func):
            self.PVPFJS.append(func)

    def gtYbdvqXEGvY(func):
        self.PVPFJS.remove(func)

    def selectionChanged(self):
        for x in self.PVPFJS:
            if x is not None:
                x()

        return

    def JvSwzXgDeSH(self):
        XZNkhLy = 1
        Dovjge = self.l.getCurrentSelection()
        if Dovjge is None:
            return (None, None)
        else:
            gOvtm = Dovjge[XZNkhLy + 1]
            UMUhLJhkv = ServiceReference(Dovjge[XZNkhLy])
            qACzZpc = self.QvVabvQOoSofkV(UMUhLJhkv, gOvtm)
            return (qACzZpc, UMUhLJhkv)

    def OGJPWJikcr(self):
        if self.l.getCurrentSelection() is not None:
            return self.l.getCurrentSelection()[0]
        else:
            return 0

    def QvVabvQOoSofkV(self, UMUhLJhkv, gggJixxXg):
        qZdmIhLHDjXpju = None
        if self.DTzDLYhRge is not None and gggJixxXg is not None:
            qZdmIhLHDjXpju = self.DTzDLYhRge.lookupEventId(UMUhLJhkv.ref, gggJixxXg)
        return qZdmIhLHDjXpju

    def GdjxEetRD(self):
        self.instance.moveSelection(self.instance.moveUp)

    def Krkrxa(self):
        self.instance.moveSelection(self.instance.moveDown)

    GUI_WIDGET = eListbox

    def xtuQLcHTVXhQsB(self, zuwFdPsBIgsKYj, UMUhLJhkv, VQKNKnUpnwbt, pVdYFhAaXsyyci, qxyEWz, cIlYUZavCM, rbuTrfjskKNUrpX, AemZEBZRFVH):
        try:
            MBwGVCQCuRs = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
            AduwKVqFCtWzeIh = self.mCcXxUnnUdldCM(eServiceReference(UMUhLJhkv), eServiceReference(MBwGVCQCuRs))
        except:
            AduwKVqFCtWzeIh = 1

        rLTFYjFLR = pVdYFhAaXsyyci and self.NSjWHcStKTLbU(UMUhLJhkv, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt)
        RGWnwo = ''
        DrEcqGyi = self.DrEcqGyi
        sZFcJcEYedYG = self.sZFcJcEYedYG
        RYWUNgKwKamFGs = self.RYWUNgKwKamFGs
        JixFEWcBYWgVHg = 0
        cwjjzqyTcBh = self.cwjjzqyTcBh
        wxdWuWRukihTqU = cIlYUZavCM
        uGZVEpaLJ = self.JvSwzXgDeSH()[0]
        if uGZVEpaLJ is not None:
            ilGQEEnSuF = uGZVEpaLJ.getShortDescription()
            if ilGQEEnSuF and ilGQEEnSuF != cIlYUZavCM:
                wxdWuWRukihTqU = cIlYUZavCM + ' - ' + ilGQEEnSuF
        if rLTFYjFLR == True:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.ZWXRUOATTV
        elif rLTFYjFLR == False:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.hXbYdg
        elif not AduwKVqFCtWzeIh:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.HaJKV
        elif CoolAlternative(UMUhLJhkv, self.WQqNiBbHzOJUrXt.toString()):
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.TNOcIyTOCMk
        else:
            IljDvazPimAt = self.BPTUvuBjQ
            uSfYSrtgTKg = self.Wzjij
            zpWysCGB = self.AbCAHrrQoOcBPH
            dhELvjJBqAwXn = self.chSpBcKz
            QLxdqGrZFSq = self.WubpaSVNw
        if config.CTVG.C58.value:
            RGWnwo = '%02d. ' % self.xpFKRFDhSumIm(UMUhLJhkv)
        res = [None]
        if config.CTVG.C38.value:
            JixFEWcBYWgVHg = cwjjzqyTcBh / 0.6 + 10
            if self.icJJVKHwold > 20:
                DrEcqGyi = DrEcqGyi - JixFEWcBYWgVHg
            YTSEoIi = False
            YTSEoIi = findCoolPicon(UMUhLJhkv, AemZEBZRFVH)
            if YTSEoIi:
                self.wuqkSpGyxrM.setPara((cwjjzqyTcBh / 0.6,
                 cwjjzqyTcBh,
                 1,
                 1,
                 False,
                 1,
                 '#ff000000'))
                self.wuqkSpGyxrM.startDecode(YTSEoIi, 0, 0, False)
                res.append(MultiContentEntryPixmapAlphaBlend(pos=(0, self.mWkRquQGU), size=(cwjjzqyTcBh / 0.6, cwjjzqyTcBh), png=self.wuqkSpGyxrM.getData(), backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
        res.append(MultiContentEntryText(pos=(self.mMQSGwZt + JixFEWcBYWgVHg, self.BwBxpeGsFk), size=(DrEcqGyi, 50), font=1, text=RGWnwo + AemZEBZRFVH, color=IljDvazPimAt, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
        res.append(MultiContentEntryText(pos=(self.CwbbgtPbYdAJaNS + JixFEWcBYWgVHg, self.icJJVKHwold), size=(self.oVoKs - JixFEWcBYWgVHg, 50), font=2, text=wxdWuWRukihTqU, color=uSfYSrtgTKg, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
        if pVdYFhAaXsyyci is not None:
            VprrLjtcbPtnLQS = localtime(pVdYFhAaXsyyci)
            JBCDJoHYm = localtime(pVdYFhAaXsyyci + qxyEWz)
            if self.icJJVKHwold > 20:
                JixFEWcBYWgVHg = 0
            if rbuTrfjskKNUrpX < pVdYFhAaXsyyci:
                res.append(MultiContentEntryText(pos=(self.HkPIn + JixFEWcBYWgVHg, self.RVaddhJ), size=(self.vDtXdSWMj, 50), font=0, text='%02d:%02d  -  %02d:%02d' % (VprrLjtcbPtnLQS[3],
                 VprrLjtcbPtnLQS[4],
                 JBCDJoHYm[3],
                 JBCDJoHYm[4]), color=zpWysCGB, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
                dxypDHxLzcLh = qxyEWz / 60
                if self.icJJVKHwold < 20:
                    res.append(MultiContentEntryText(pos=(self.xHpqYxluJNkS, self.RVaddhJ), size=(self.IwKiKwc, 50), font=0, flags=RT_HALIGN_RIGHT, text='+ %02d min' % dxypDHxLzcLh, color=dhELvjJBqAwXn, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
            else:
                ZOtbQgTXKRwH = (rbuTrfjskKNUrpX - pVdYFhAaXsyyci) * 100 / qxyEWz
                res.append(PsVUdJXJ(pos=(self.OGBpHgi + JixFEWcBYWgVHg, self.xetVW), size=(self.nOvheUu, self.EnJelDGikSIP), percent=ZOtbQgTXKRwH, foreColor=zpWysCGB, foreColorSelected=QLxdqGrZFSq, KNlLJNdkd=sZFcJcEYedYG, KNlLJNdkdSelected=RYWUNgKwKamFGs))
                dxypDHxLzcLh = (qxyEWz - (rbuTrfjskKNUrpX - pVdYFhAaXsyyci)) / 60
                res.append(MultiContentEntryText(pos=(self.xHpqYxluJNkS, self.RVaddhJ), size=(self.IwKiKwc, 50), font=0, flags=RT_HALIGN_RIGHT, text='+ %02d min' % dxypDHxLzcLh, color=dhELvjJBqAwXn, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
        return res

    def postWidgetCreate(self, instance):
        instance.setWrapAround(True)
        instance.selectionChanged.get().append(self.selectionChanged)
        instance.setContent(self.l)

    def preWidgetRemove(self, instance):
        instance.selectionChanged.get().remove(self.selectionChanged)
        instance.setContent(None)
        return

    def NSjWHcStKTLbU(self, fXYLLkn, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt):
        for x in self.QHYMHhwOVIXtLT.timer_list:
            if x.service_ref.ref.toString() == fXYLLkn:
                blmRapeotWYHCEX = pVdYFhAaXsyyci + qxyEWz
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                if x.eit == VQKNKnUpnwbt:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True
                elif pVdYFhAaXsyyci <= TteNjwT <= blmRapeotWYHCEX:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True

        for x in self.QHYMHhwOVIXtLT.processed_timers:
            if x.disabled and x.service_ref.ref.toString() == fXYLLkn:
                if x.eit == VQKNKnUpnwbt:
                    return False

    def xpFKRFDhSumIm(self, UMUhLJhkv):
        global xKmXaE
        if xKmXaE is None or not self.cfCIaMrxr:
            xKmXaE = TrruhKvKi.getBouquetNumOffset(FufElMDyUtWr)
            self.FcatbmGJKhWdbnB = self.TPVxuSuwYBrUelM.list(FufElMDyUtWr)
            self.cfCIaMrxr = self.FcatbmGJKhWdbnB and self.FcatbmGJKhWdbnB.getContent('S', True)
        NhsvvZxTKXnV = 0
        iXgrny = 0
        if self.cfCIaMrxr:
            OCCKSDwCPbq = len(self.cfCIaMrxr)
            for tlvldyLLXXHo in list(range(OCCKSDwCPbq)):
                KsiNzjF = (NhsvvZxTKXnV + tlvldyLLXXHo) % OCCKSDwCPbq
                mutbPpmzLHBYz = self.cfCIaMrxr[KsiNzjF]
                if mutbPpmzLHBYz[2:4] == '64':
                    iXgrny += 1
                if UMUhLJhkv == mutbPpmzLHBYz:
                    NhsvvZxTKXnV = KsiNzjF
                    return xKmXaE + NhsvvZxTKXnV - iXgrny + 1

        return 0

    def mCcXxUnnUdldCM(self, BidVA, JhKpFAp):
        NHozf = self.TPVxuSuwYBrUelM.info(BidVA)
        return NHozf and NHozf.isPlayable(BidVA, JhKpFAp) or False

    def ZliZccOwvDTPgWM(self, qDFTEDFxno, KjUKrjjjHKPvzNX = -1):
        ZDxUJDDCPod = [ (UMUhLJhkv.ref.toString(), 0, KjUKrjjjHKPvzNX) for UMUhLJhkv in qDFTEDFxno ]
        if config.CTVG.C28.value:
            ZDxUJDDCPod.insert(0, 'X0RIBDTCn')
        else:
            ZDxUJDDCPod.insert(0, 'X0RIBDTCN')
        self.ScnvMSTPY = self.sdiQt(ZDxUJDDCPod)
        self.l.setList(self.ScnvMSTPY)
        self.selectionChanged()

    def KGbwzozbdNhGWFF(self, SqpegV):
        BiVMJSTCWKQvuMk = [ x[3] and (x[1], SqpegV, x[3]) or (x[1], SqpegV, 0) for x in self.ScnvMSTPY ]
        BiVMJSTCWKQvuMk.insert(0, 'XRIBDTCn')
        tOObZiAFRL = self.sdiQt(BiVMJSTCWKQvuMk)
        OvLjSqiOcXU = 0
        for x in tOObZiAFRL:
            zuwFdPsBIgsKYj = self.ScnvMSTPY[OvLjSqiOcXU][0] + SqpegV
            if zuwFdPsBIgsKYj >= 0:
                if x[2] is not None:
                    self.ScnvMSTPY[OvLjSqiOcXU] = (zuwFdPsBIgsKYj,
                     x[0],
                     x[1],
                     x[2],
                     x[3],
                     x[4],
                     x[5],
                     x[6])
            OvLjSqiOcXU += 1

        self.l.setList(self.ScnvMSTPY)
        self.selectionChanged()
        return

    def sdiQt(self, list, MlBIgDzxYSu = None):
        if self.DTzDLYhRge is not None:
            if MlBIgDzxYSu is not None:
                return self.DTzDLYhRge.lookupEvent(list, MlBIgDzxYSu)
            else:
                return self.DTzDLYhRge.lookupEvent(list)
        return []

    def UrfFYoRsn(self, IHfwFGMsEKcU):
        if not IHfwFGMsEKcU:
            return
        tAaMXETO = 0
        fXYLLkn = IHfwFGMsEKcU.toString()
        for x in self.ScnvMSTPY:
            if CoolAlternative(x[1], fXYLLkn):
                self.instance.moveSelectionTo(tAaMXETO)
                break
            tAaMXETO += 1


class fECRrOPDKlFDx(Screen):

    def __init__(self, session, qDFTEDFxno, VsbLMxaqGuOhxRV = None, TrruhKvKi = None, pXBQLmHRRZdwrD = '', PwRojNX = None):
        Screen.__init__(self, session)
        if TMvKPeMEZHVqV == 720:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_720.xml'
            elif PwRojNX == iXZeUPZjXi:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_720.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_720.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_720.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_720.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_720.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_720.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_720.xml'
        elif TMvKPeMEZHVqV == 1024:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1024.xml'
            elif PwRojNX == iXZeUPZjXi:
                if config.CTVG.C43.value == 1:
                    self.skinName = 'CoolSingleGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1024.xml'
                elif config.CTVG.C43.value == 2:
                    self.skinName = 'CoolSingleGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1024.xml'
                elif config.CTVG.C43.value == 3:
                    self.skinName = 'CoolSingleGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1024.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                if config.CTVG.C42.value == 1:
                    self.skinName = 'CoolEasyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1024.xml'
                elif config.CTVG.C42.value == 2:
                    self.skinName = 'CoolEasyGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1024.xml'
                elif config.CTVG.C42.value == 3:
                    self.skinName = 'CoolEasyGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1024.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                if config.CTVG.C41.value == 1:
                    self.skinName = 'CoolChannelGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1024.xml'
                elif config.CTVG.C41.value == 2:
                    self.skinName = 'CoolChannelGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1024.xml'
                elif config.CTVG.C41.value == 3:
                    self.skinName = 'CoolChannelGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1024.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1024.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1024.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1024.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1024.xml'
        elif PwRojNX == PQMOk:
            self.skinName = 'CoolInfoGuide'
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1280.xml'
        elif PwRojNX == iXZeUPZjXi:
            if config.CTVG.C43.value == 1:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1280.xml'
            elif config.CTVG.C43.value == 2:
                self.skinName = 'CoolSingleGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1280.xml'
            elif config.CTVG.C43.value == 3:
                self.skinName = 'CoolSingleGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1280.xml'
        elif PwRojNX == IUqwdjkcjCMKCFO:
            if config.CTVG.C42.value == 1:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1280.xml'
            elif config.CTVG.C42.value == 2:
                self.skinName = 'CoolEasyGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1280.xml'
            elif config.CTVG.C42.value == 3:
                self.skinName = 'CoolEasyGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1280.xml'
        elif PwRojNX == QQdKtJPxMxJPjwB:
            if config.CTVG.C41.value == 1:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1280.xml'
            elif config.CTVG.C41.value == 2:
                self.skinName = 'CoolChannelGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1280.xml'
            elif config.CTVG.C41.value == 3:
                self.skinName = 'CoolChannelGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1280.xml'
        elif PwRojNX == eseWoWLtSYyCHGT:
            if config.CTVG.C40.value == 1:
                self.skinName = 'CoolTVGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1280.xml'
            elif config.CTVG.C40.value == 2:
                self.skinName = 'CoolTinyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1280.xml'
            elif config.CTVG.C40.value == 3:
                self.skinName = 'CoolMultiGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1280.xml'
            elif config.CTVG.C40.value == 4:
                self.skinName = 'CoolNiceGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1280.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self.YbVViHHAtS = zUIfAWMBbQJ
        self.aewDrpsjqX = TrruhKvKi
        self.VsbLMxaqGuOhxRV = VsbLMxaqGuOhxRV
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.vzDGDGAQLSCa = -1
        self.FUiTqUurDFxy = False
        self.cIKHf = None
        self['Service'] = ServiceEvent()
        self['Event'] = Event()
        self['key_red'] = Button('')
        self['key_green'] = Button('')
        self['key_yellow'] = Button('')
        self['key_blue'] = Button('')
        self['date'] = Button()
        self.ZsMYlBwYFBsTydI = qDFTEDFxno
        if pXBQLmHRRZdwrD != '':
            Screen.setTitle(self, pXBQLmHRRZdwrD)
        self['list'] = lKVEwGYfTpgWH(pOHOrwCihqC=self.WlFKMlyFxSWrG, QHYMHhwOVIXtLT=session.nav.RecordTimer)
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolMenu': self.NuGwC,
         'CoolTime': self.sEJWW,
         'CoolRed': self.GwhJbNuquP,
         'CoolRedLong': self.fbUws,
         'CoolGreen': self.gXppchsrp,
         'CoolGreenLong': self.mzzBQRAohy,
         'CoolYellow': self.bKpKe,
         'CoolYellowLong': self.qOlhOHWiFHpIC,
         'CoolBlue': self.qsDCwRsYOveEFy,
         'CoolBlueLong': self.uHqjdBJMLj,
         'CoolOK': self.WhRkmBFDyxfV,
         'CoolOKLong': self.KZcQOfIkWdrLZ,
         'CoolInfo': self.NxrXAek,
         'CoolInfoLong': self.uWIjFbGhtX,
         'CoolRecord': self.esPNG,
         'CoolVIDEO': nePylQgKlghpaVP,
         'CoolAUDIO': self.uzzLIxD,
         'CoolPlay': self.SdyqepEBz,
         'CoolKeyTV': self.EekrcnjXd,
         'CoolPower': self.EUtMyA,
         'CoolCancel': self.JtAiZhAVofB,
         'CoolChannelUP': self.qLfawkLNTLbGJR,
         'CoolChannelDown': self.QIMComcMsKUFVv,
         'CoolNEXT': self.kvvAAW,
         'CoolPREVIOUS': self.sTsGfHu,
         '1': self.BXgEprgWswxGUwu,
         '2': self.dyKNDy,
         '3': self.OwPMoV,
         '4': self.ORMaFFgAUurQpB,
         '5': self.cDAaj,
         '6': self.FvOdCbFqhvscV,
         '7': self.TdjjCghHcsK,
         '8': self.neDLkklkP,
         '9': self.eKXjhOLrwzFbS,
         '0': self.ntTBGk}, -1)
        self.SuVhHLBrOFx = config.CTVG.C12.value
        self.jIDDtifEzLAQAtH = config.CTVG.C14.value
        self.KhCcbywN = config.CTVG.C16.value
        self.gYtswyvbtJ = config.CTVG.C18.value
        self['key_red'].setText(_(self.SuVhHLBrOFx))
        self['key_green'].setText(_(self.jIDDtifEzLAQAtH))
        self['key_yellow'].setText(_(self.KhCcbywN))
        self['key_blue'].setText(_(self.gYtswyvbtJ))
        self.onLayoutFinish.append(self.NbmZQLxewbo)
        self.YfbjxowZQV()
        self.qvZsfOLaorS = eTimer()
        self.qvZsfOLaorS.callback.append(self.GKkaWZYIWKJliO)
        self.session.nav.RecordTimer.on_state_change.append(self.OQekEHTyEAMogUz)
        self.session.nav.record_event.append(self.rTNBfpRbTsgf)
        self.BubscGANC = ServiceEventTracker(screen=self, eventmap={iPlayableService.evStart: self.eznYurXbAoT,
         iPlayableService.evStopped: self.eznYurXbAoT})
        return

    def eznYurXbAoT(self):
        if hasattr(self, 'shown'):
            if self.shown:
                if self.qvZsfOLaorS.isActive():
                    self.qvZsfOLaorS.stop()
                self.qvZsfOLaorS.start(3000, True)

    def rTNBfpRbTsgf(self, UMUhLJhkv, event):
        self.eznYurXbAoT()

    def OQekEHTyEAMogUz(self, WFVjWbKbX):
        self.eznYurXbAoT()

    def qFDSvr(self):
        global WmXVqUV
        if WmXVqUV == 1:
            x = config.CTVG.C77.value
        elif WmXVqUV == 2:
            x = config.CTVG.C78.value
        elif WmXVqUV == 3:
            x = config.CTVG.C79.value
        elif WmXVqUV == 4:
            if WvYVaQ != self.YbVViHHAtS and SAQsYCIeDb != self.YbVViHHAtS:
                WmXVqUV = 1
                return self.close(False)
            x = config.CTVG.C80.value
        elif WmXVqUV == 5:
            x = config.CTVG.C81.value
        elif WmXVqUV == 6:
            x = config.CTVG.C82.value
        elif WmXVqUV == 7:
            x = config.CTVG.C83.value
        elif WmXVqUV == 8:
            x = config.CTVG.C84.value
        elif WmXVqUV == 9:
            x = config.CTVG.C85.value
        elif WmXVqUV == 10:
            x = config.CTVG.C86.value
        elif WmXVqUV == 11:
            x = config.CTVG.C87.value
        elif WmXVqUV == 12:
            x = config.CTVG.C88.value
        if x == '9':
            WmXVqUV += 1
            return self.eKXjhOLrwzFbS()
        self.hide()
        if x == '1':
            self.WVwFshleYbnIc()
        elif x == '2':
            self.RDSJwxPYCfBLVaN()
        elif x == '3':
            CEGmain(self.session, self.aewDrpsjqX)
        elif x == '4':
            if WvYVaQ != self.YbVViHHAtS and SAQsYCIeDb != self.YbVViHHAtS:
                self.close(False)
            else:
                WmXVqUV += 1
                return self.qFDSvr()
        elif x == '5':
            config.CTVG.C40.value = 1
            main(self.session, self.aewDrpsjqX)
        elif x == '6':
            config.CTVG.C40.value = 2
            main(self.session, self.aewDrpsjqX)
        elif x == '7':
            config.CTVG.C40.value = 3
            main(self.session, self.aewDrpsjqX)
        elif x == '8':
            config.CTVG.C40.value = 4
            main(self.session, self.aewDrpsjqX)
        elif x == '10':
            self.sSPMBhwDflASCMt()
        elif x == '11':
            WmXVqUV = 0
            self.session.open(TimerEditList)
        else:
            WmXVqUV = 0
        WmXVqUV += 1
        self.close(False)

    def YfbjxowZQV(self):
        geikSRpcvam = localtime()
        if (geikSRpcvam.tm_year, geikSRpcvam.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2])):
            self.close(self.FUiTqUurDFxy)

    def GKkaWZYIWKJliO(self):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        self['list'].l.invalidate()

    def changeServiceCB(self, SqpegV, epg):
        if self.serviceSel:
            if SqpegV > 0:
                self.serviceSel.nextService()
            else:
                self.serviceSel.prevService()
            epg.setService(self.serviceSel.currentService())

    def QEcLxYKv(self, QoGRewjlErZRq, setService, val):
        BDuSW = self['list'].JvSwzXgDeSH()
        if val == -1:
            self.GdjxEetRD()
        elif val == +1:
            self.Krkrxa()
        EnFKRmiyy = self['list'].JvSwzXgDeSH()
        if EnFKRmiyy[0] is None and EnFKRmiyy[1].ref != BDuSW[1].ref:
            self.QEcLxYKv(QoGRewjlErZRq, setService, val)
        else:
            setService(EnFKRmiyy[1])
            QoGRewjlErZRq(EnFKRmiyy[0])
        return

    def voLEWybvGX(self):
        zjRLCa = self['list'].JvSwzXgDeSH()
        if not zjRLCa:
            return
        try:
            from Plugins.Extensions.AutoTimer.AutoTimerEditor import addAutotimerFromEvent
            self.session.openWithCallback(self.aqFgBg, ChoiceBox, title=_('   check Autotimer ?'), list=[(_('Yes'), 'Yes'), (_('No'), 'No')])
            addAutotimerFromEvent(self.session, zjRLCa[0], zjRLCa[1])
        except:
            self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def aqFgBg(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        if nKGKSPXPp == 'Yes':
            try:
                from Plugins.Extensions.AutoTimer.plugin import main as AutoTimerSafe
                AutoTimerSafe(self.session)
            except:
                self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def SdyqepEBz(self):
        ToIxnZLjAph(eFSzkTC)

    def kvvAAW(self):
        self['list'].LItiOOUy(1)

    def sTsGfHu(self):
        self['list'].LItiOOUy(-1)

    def EUtMyA(self):
        try:
            from Screens.SleepTimerEdit import SleepTimerEdit
            self.session.open(SleepTimerEdit)
        except:
            pass

    def NbmZQLxewbo(self):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        self['list'].ZGjyWp(self.ZsMYlBwYFBsTydI, self.vzDGDGAQLSCa)
        self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())

    def sSPMBhwDflASCMt(self):
        try:
            OiTUjyeSoZRNG = self['list'].JvSwzXgDeSH()
            ERoOCCVi = OiTUjyeSoZRNG[0]
            if not ERoOCCVi:
                return
            name = ERoOCCVi.getEventName() or ''
        except:
            name = ''

        self.session.open(lyqBhZ, name, False)

    def BvRoHaxNcu(self):
        config.CTVG.C60.value = False
        self.SkDkTpkG = True
        self.hide()
        CEGmain(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def RDSJwxPYCfBLVaN(self):
        config.CTVG.C60.value = False
        config.CTVG.C61.value = False
        tfonHdIjfgQ = self['list'].JvSwzXgDeSH()
        hqsJGKtkQZAxqBE = tfonHdIjfgQ[1]
        ovhyteog = eServiceReference(str(hqsJGKtkQZAxqBE))
        if ovhyteog.flags & eServiceReference.isMarker or not tfonHdIjfgQ:
            return
        TFekBZfhstWiyNH = tfonHdIjfgQ[1].ref
        if TFekBZfhstWiyNH:
            self.serviceSel = SimpleServicelist(self.ZsMYlBwYFBsTydI)
            if self.serviceSel.selectService(TFekBZfhstWiyNH):
                self.session.openWithCallback(self.UZWrOVfpub, XEArkQXQCQRMEL, TFekBZfhstWiyNH, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=iXZeUPZjXi)

    def RHRYk(self):
        self.hide()
        main(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def ntTBGk(self):
        self.hide()
        CCGmain(self.session, self.aewDrpsjqX)
        self.close(self.FUiTqUurDFxy)

    def GwhJbNuquP(self):
        EcLNwIhunJbRsLQ = self.SuVhHLBrOFx
        if EcLNwIhunJbRsLQ == 'EPG Select':
            self.qFDSvr()
        elif EcLNwIhunJbRsLQ == 'Zap':
            self.nORxTbRjzsNVch()
        elif EcLNwIhunJbRsLQ == 'Zap + Exit':
            self.JIQKwPOcc()
        elif EcLNwIhunJbRsLQ == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif EcLNwIhunJbRsLQ == 'CoolInfoBox':
            self.fxVcQUikA()
        elif EcLNwIhunJbRsLQ == 'GuideSwitch':
            self.RHRYk()
        elif EcLNwIhunJbRsLQ == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif EcLNwIhunJbRsLQ == 'Timer':
            self.EmOZX()
        elif EcLNwIhunJbRsLQ == 'QuickRec':
            self.esPNG()
        elif EcLNwIhunJbRsLQ == 'AutoTimer':
            self.voLEWybvGX()
        elif EcLNwIhunJbRsLQ == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif EcLNwIhunJbRsLQ == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif EcLNwIhunJbRsLQ == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif EcLNwIhunJbRsLQ == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.qFDSvr()

    def fbUws(self):
        aFfcKSkBDKNWm = config.CTVG.C13.value
        if aFfcKSkBDKNWm == 'Zap':
            self.nORxTbRjzsNVch()
        elif aFfcKSkBDKNWm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif aFfcKSkBDKNWm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif aFfcKSkBDKNWm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif aFfcKSkBDKNWm == 'GuideSwitch':
            self.RHRYk()
        elif aFfcKSkBDKNWm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif aFfcKSkBDKNWm == 'Timer':
            self.EmOZX()
        elif aFfcKSkBDKNWm == 'QuickRec':
            self.esPNG()
        elif aFfcKSkBDKNWm == 'AutoTimer':
            self.voLEWybvGX()
        elif aFfcKSkBDKNWm == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif aFfcKSkBDKNWm == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif aFfcKSkBDKNWm == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif aFfcKSkBDKNWm == 'Bouquetlist':
            self.SdyqepEBz()
        elif aFfcKSkBDKNWm == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def gXppchsrp(self):
        fCsivhkbczcm = self.jIDDtifEzLAQAtH
        if fCsivhkbczcm == 'Zap':
            self.nORxTbRjzsNVch()
        elif fCsivhkbczcm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif fCsivhkbczcm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif fCsivhkbczcm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif fCsivhkbczcm == 'GuideSwitch':
            self.RHRYk()
        elif fCsivhkbczcm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif fCsivhkbczcm == 'Timer':
            self.EmOZX()
        elif fCsivhkbczcm == 'QuickRec':
            self.esPNG()
        elif fCsivhkbczcm == 'AutoTimer':
            self.voLEWybvGX()
        elif fCsivhkbczcm == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif fCsivhkbczcm == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif fCsivhkbczcm == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif fCsivhkbczcm == 'Bouquetlist':
            self.SdyqepEBz()
        elif fCsivhkbczcm == 'EPG Select':
            self.qFDSvr()
        else:
            self.EmOZX()

    def mzzBQRAohy(self):
        CALICbGXK = config.CTVG.C15.value
        if CALICbGXK == 'Zap':
            self.nORxTbRjzsNVch()
        elif CALICbGXK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif CALICbGXK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif CALICbGXK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif CALICbGXK == 'GuideSwitch':
            self.RHRYk()
        elif CALICbGXK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif CALICbGXK == 'Timer':
            self.EmOZX()
        elif CALICbGXK == 'QuickRec':
            self.esPNG()
        elif CALICbGXK == 'AutoTimer':
            self.voLEWybvGX()
        elif CALICbGXK == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif CALICbGXK == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif CALICbGXK == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif CALICbGXK == 'Bouquetlist':
            self.SdyqepEBz()
        elif CALICbGXK == 'EPG Select':
            self.qFDSvr()
        else:
            self.voLEWybvGX()

    def bKpKe(self):
        BCGuXefsvjf = self.KhCcbywN
        if BCGuXefsvjf == 'Back':
            self.sTsGfHu()
        elif BCGuXefsvjf == 'Zap':
            self.nORxTbRjzsNVch()
        elif BCGuXefsvjf == 'Zap + Exit':
            self.JIQKwPOcc()
        elif BCGuXefsvjf == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif BCGuXefsvjf == 'CoolInfoBox':
            self.fxVcQUikA()
        elif BCGuXefsvjf == 'GuideSwitch':
            self.RHRYk()
        elif BCGuXefsvjf == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif BCGuXefsvjf == 'Timer':
            self.EmOZX()
        elif BCGuXefsvjf == 'QuickRec':
            self.esPNG()
        elif BCGuXefsvjf == 'AutoTimer':
            self.voLEWybvGX()
        elif BCGuXefsvjf == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif BCGuXefsvjf == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif BCGuXefsvjf == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif BCGuXefsvjf == 'Bouquetlist':
            self.SdyqepEBz()
        elif BCGuXefsvjf == 'EPG Select':
            self.qFDSvr()
        else:
            self.RHRYk()

    def qOlhOHWiFHpIC(self):
        gRpGhRQrF = config.CTVG.C17.value
        if gRpGhRQrF == 'Zap':
            self.nORxTbRjzsNVch()
        elif gRpGhRQrF == 'Zap + Exit':
            self.JIQKwPOcc()
        elif gRpGhRQrF == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif gRpGhRQrF == 'CoolInfoBox':
            self.fxVcQUikA()
        elif gRpGhRQrF == 'GuideSwitch':
            self.RHRYk()
        elif gRpGhRQrF == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif gRpGhRQrF == 'Timer':
            self.EmOZX()
        elif gRpGhRQrF == 'QuickRec':
            self.esPNG()
        elif gRpGhRQrF == 'AutoTimer':
            self.voLEWybvGX()
        elif gRpGhRQrF == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif gRpGhRQrF == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif gRpGhRQrF == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif gRpGhRQrF == 'Bouquetlist':
            self.SdyqepEBz()
        elif gRpGhRQrF == 'EPG Select':
            self.qFDSvr()
        else:
            self.JIQKwPOcc()

    def qsDCwRsYOveEFy(self):
        LnElTGKJP = self.gYtswyvbtJ
        if LnElTGKJP == 'Next':
            self.kvvAAW()
        elif LnElTGKJP == 'Zap':
            self.nORxTbRjzsNVch()
        elif LnElTGKJP == 'Zap + Exit':
            self.JIQKwPOcc()
        elif LnElTGKJP == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif LnElTGKJP == 'CoolInfoBox':
            self.fxVcQUikA()
        elif LnElTGKJP == 'GuideSwitch':
            self.RHRYk()
        elif LnElTGKJP == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif LnElTGKJP == 'Timer':
            self.EmOZX()
        elif LnElTGKJP == 'QuickRec':
            self.esPNG()
        elif LnElTGKJP == 'AutoTimer':
            self.voLEWybvGX()
        elif LnElTGKJP == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif LnElTGKJP == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif LnElTGKJP == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif LnElTGKJP == 'Bouquetlist':
            self.SdyqepEBz()
        elif LnElTGKJP == 'EPG Select':
            self.qFDSvr()
        else:
            self.sSPMBhwDflASCMt()

    def uHqjdBJMLj(self):
        UQcfkjKQK = config.CTVG.C19.value
        if UQcfkjKQK == 'Zap':
            self.nORxTbRjzsNVch()
        elif UQcfkjKQK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif UQcfkjKQK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif UQcfkjKQK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif UQcfkjKQK == 'GuideSwitch':
            self.RHRYk()
        elif UQcfkjKQK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif UQcfkjKQK == 'Timer':
            self.EmOZX()
        elif UQcfkjKQK == 'QuickRec':
            self.esPNG()
        elif UQcfkjKQK == 'AutoTimer':
            self.voLEWybvGX()
        elif UQcfkjKQK == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif UQcfkjKQK == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif UQcfkjKQK == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif UQcfkjKQK == 'Bouquetlist':
            self.SdyqepEBz()
        elif UQcfkjKQK == 'EPG Select':
            self.qFDSvr()
        else:
            self.fxVcQUikA()

    def WhRkmBFDyxfV(self):
        SlBvlWSPMURgObC = config.CTVG.C20.value
        if SlBvlWSPMURgObC == 'Zap':
            self.nORxTbRjzsNVch()
        elif SlBvlWSPMURgObC == 'Zap + Exit':
            self.JIQKwPOcc()
        elif SlBvlWSPMURgObC == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif SlBvlWSPMURgObC == 'CoolInfoBox':
            self.fxVcQUikA()
        elif SlBvlWSPMURgObC == 'GuideSwitch':
            self.RHRYk()
        elif SlBvlWSPMURgObC == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif SlBvlWSPMURgObC == 'Timer':
            self.EmOZX()
        elif SlBvlWSPMURgObC == 'QuickRec':
            self.esPNG()
        elif SlBvlWSPMURgObC == 'AutoTimer':
            self.voLEWybvGX()
        elif SlBvlWSPMURgObC == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif SlBvlWSPMURgObC == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif SlBvlWSPMURgObC == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif SlBvlWSPMURgObC == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.WVwFshleYbnIc()

    def KZcQOfIkWdrLZ(self):
        OCCKSDwCPbq = config.CTVG.C21.value
        if OCCKSDwCPbq == 'Zap':
            self.nORxTbRjzsNVch()
        elif OCCKSDwCPbq == 'Zap + Exit':
            self.JIQKwPOcc()
        elif OCCKSDwCPbq == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif OCCKSDwCPbq == 'CoolInfoBox':
            self.fxVcQUikA()
        elif OCCKSDwCPbq == 'GuideSwitch':
            self.RHRYk()
        elif OCCKSDwCPbq == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif OCCKSDwCPbq == 'Timer':
            self.EmOZX()
        elif OCCKSDwCPbq == 'QuickRec':
            self.esPNG()
        elif OCCKSDwCPbq == 'AutoTimer':
            self.voLEWybvGX()
        elif OCCKSDwCPbq == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif OCCKSDwCPbq == 'Bouquet +':
            self.qLfawkLNTLbGJR()
        elif OCCKSDwCPbq == 'Bouquet -':
            self.QIMComcMsKUFVv()
        elif OCCKSDwCPbq == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            return

    def NxrXAek(self):
        LkGwiX = config.CTVG.C22.value
        if LkGwiX == '4':
            self.qFDSvr()
        elif LkGwiX == '1':
            self.WVwFshleYbnIc()
        elif LkGwiX == '2':
            self.RDSJwxPYCfBLVaN()
        elif LkGwiX == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def uWIjFbGhtX(self):
        BkucHGwMEzEJ = config.CTVG.C23.value
        if BkucHGwMEzEJ == '4':
            self.qFDSvr()
        elif BkucHGwMEzEJ == '1':
            self.WVwFshleYbnIc()
        elif BkucHGwMEzEJ == '2':
            self.RDSJwxPYCfBLVaN()
        elif BkucHGwMEzEJ == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def qLfawkLNTLbGJR(self):
        if self.VsbLMxaqGuOhxRV:
            self['list'].instance.moveSelectionTo(0)
            config.CTVG.C60.value = True
            self.VsbLMxaqGuOhxRV(1, self)
            pXBQLmHRRZdwrD = ServiceReference(FufElMDyUtWr).getServiceName()
            if pXBQLmHRRZdwrD != '':
                Screen.setTitle(self, pXBQLmHRRZdwrD)

    def QIMComcMsKUFVv(self):
        if self.VsbLMxaqGuOhxRV:
            self['list'].instance.moveSelectionTo(0)
            config.CTVG.C60.value = True
            self.VsbLMxaqGuOhxRV(-1, self)
            pXBQLmHRRZdwrD = ServiceReference(FufElMDyUtWr).getServiceName()
            if pXBQLmHRRZdwrD != '':
                Screen.setTitle(self, pXBQLmHRRZdwrD)

    def sEJWW(self):
        global YPbLcThQWvMcQ
        if not YPbLcThQWvMcQ:
            config.misc.prev_mepg_time = ConfigClock(default=time())
            YPbLcThQWvMcQ = True
        self.session.openWithCallback(self.ylOPBdIWtSFX, TimeDateInput, config.misc.prev_mepg_time)

    def ylOPBdIWtSFX(self, ret):
        if len(ret) > 1:
            if ret[0]:
                self.vzDGDGAQLSCa = ret[1]
                self['list'].ZGjyWp(self.ZsMYlBwYFBsTydI, ret[1])

    def BXgEprgWswxGUwu(self):
        config.CTVG.C41.value = 1
        config.CTVG.save()
        self.hide()
        zehTthMch = TrruhKvKi.getRoot()
        VCRwoeTZC(zehTthMch)
        self.close(self.FUiTqUurDFxy)

    def dyKNDy(self):
        if WvYVaQ == self.YbVViHHAtS or SAQsYCIeDb == self.YbVViHHAtS:
            config.CTVG.C41.value = 2
            config.CTVG.save()
            self.hide()
            zehTthMch = TrruhKvKi.getRoot()
            VCRwoeTZC(zehTthMch)
            self.close(self.FUiTqUurDFxy)

    def OwPMoV(self):
        if WvYVaQ == self.YbVViHHAtS or SAQsYCIeDb == self.YbVViHHAtS:
            config.CTVG.C41.value = 3
            config.CTVG.save()
            self.hide()
            zehTthMch = TrruhKvKi.getRoot()
            VCRwoeTZC(zehTthMch)
            self.close(self.FUiTqUurDFxy)

    def ORMaFFgAUurQpB(self):
        XZNkhLy = self['list'].IwVOhBap()
        self['list'].instance.moveSelectionTo(XZNkhLy)

    def cDAaj(self):
        self['list'].ZGjyWp(self.ZsMYlBwYFBsTydI, -1)

    def FvOdCbFqhvscV(self):
        XZNkhLy = self['list'].HRhXvd()
        self['list'].instance.moveSelectionTo(XZNkhLy)

    def TdjjCghHcsK(self):
        self.RHRYk()

    def neDLkklkP(self):
        self.hide()
        self.RDSJwxPYCfBLVaN()
        self.close(self.FUiTqUurDFxy)

    def eKXjhOLrwzFbS(self):
        cqmZQSXzuhx = localtime()
        qBaqvCLi = (cqmZQSXzuhx[0],
         cqmZQSXzuhx[1],
         cqmZQSXzuhx[2],
         config.CTVG.C30.value[0],
         config.CTVG.C30.value[1],
         0,
         cqmZQSXzuhx[6],
         cqmZQSXzuhx[7],
         cqmZQSXzuhx[8])
        self.vzDGDGAQLSCa = int(mktime(qBaqvCLi))
        if self.vzDGDGAQLSCa > int(mktime(cqmZQSXzuhx)):
            self['list'].ZGjyWp(self.ZsMYlBwYFBsTydI, self.vzDGDGAQLSCa)
        else:
            self['list'].ZGjyWp(self.ZsMYlBwYFBsTydI, self.vzDGDGAQLSCa + 86400)

    def JtAiZhAVofB(self):
        global WmXVqUV
        WmXVqUV = 1
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.hide()
        AjzDUzKgoLe = set()
        geikSRpcvam = time()
        gwVLVamNAqnDMo = False
        if config.CTVG.C62.value:
            for x in self.session.nav.RecordTimer.timer_list:
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                try:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventId(x.service_ref.ref, x.eit)
                except:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventTime(x.service_ref.ref, TteNjwT)

                if ERoOCCVi:
                    IcZCToaVeOwI = ERoOCCVi.getBeginTime()
                    CsrfWgDZI = IcZCToaVeOwI + ERoOCCVi.getDuration()
                    if IcZCToaVeOwI < cpUukOBh or CsrfWgDZI > JBCDJoHYm:
                        if ERoOCCVi.getDuration() > 300 and cpUukOBh > geikSRpcvam:
                            AjzDUzKgoLe.add(x)

        if config.CTVG.C63.value:
            for x in self.session.nav.RecordTimer.processed_timers:
                if geikSRpcvam < x.end:
                    AjzDUzKgoLe.add(x)

        dXRTDwpUpKROauu = _('\n          !! Cool Timer Alarm !! \n\n')
        for x in AjzDUzKgoLe:
            gwVLVamNAqnDMo = str(x.name)
            dplqPMZr = str(strftime('%d.%m.%Y - %H:%M', localtime(x.begin)))
            BhkuqkbF = str(x.service_ref.getServiceName())
            TuqtF = _('is disabled') if x.disabled else _('has moved')
            dXRTDwpUpKROauu += dplqPMZr + ' - ' + BhkuqkbF + '\n' + gwVLVamNAqnDMo + ' ' + TuqtF + '\n\n'

        dXRTDwpUpKROauu += _('-- please check your Timer --')
        if gwVLVamNAqnDMo:
            self.session.open(MessageBox, dXRTDwpUpKROauu, MessageBox.TYPE_ERROR)
        self.close(self.FUiTqUurDFxy)

    def WVwFshleYbnIc(self):
        config.CTVG.C60.value = False
        config.CTVG.C61.value = False
        bJKvGIVemCb = self['list'].JvSwzXgDeSH()
        hqsJGKtkQZAxqBE = bJKvGIVemCb[1]
        ovhyteog = eServiceReference(str(hqsJGKtkQZAxqBE))
        if ovhyteog.flags & eServiceReference.isMarker or not bJKvGIVemCb:
            return
        hqsJGKtkQZAxqBE = eServiceReference(str(bJKvGIVemCb[1]))
        if hqsJGKtkQZAxqBE:
            self.serviceSel = SimpleServicelist(self.ZsMYlBwYFBsTydI)
            if self.serviceSel.selectService(hqsJGKtkQZAxqBE):
                self.session.openWithCallback(self.UZWrOVfpub, zDKhcfAp, bJKvGIVemCb[0], bJKvGIVemCb[1], hqsJGKtkQZAxqBE, self.aewDrpsjqX, self.QEcLxYKv, nfZQJKwSrVA=self.changeServiceCB, PwRojNX=PQMOk)

    def UZWrOVfpub(self, ret = False):
        self.serviceSel = None
        if config.CTVG.C61.value:
            self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
            self.FUiTqUurDFxy = True
            wKxyV = self['list'].JvSwzXgDeSH()[1]
            self['list'].WQqNiBbHzOJUrXt = wKxyV.ref
            self.nORxTbRjzsNVch()
        if config.CTVG.C60.value:
            self['list'].l.invalidate()
        return

    def setService(self, UMUhLJhkv):
        self.XISehjxsPoi = UMUhLJhkv
        self.NbmZQLxewbo()

    def qFLoYuYRPQFdK(self, qDFTEDFxno):
        self.ZsMYlBwYFBsTydI = qDFTEDFxno
        self.NbmZQLxewbo()

    def GdjxEetRD(self):
        self['list'].GdjxEetRD()

    def Krkrxa(self):
        self['list'].Krkrxa()

    def fxVcQUikA(self):
        UFXUK = []
        if fspOMNbuwFCWk:
            UFXUK.append((_('SeriesPlugin'), 'SeriesPlugin'))
        if sLpxMYXhjCROl:
            UFXUK.append((_('The TVDB Info'), 'The TVDB Info'))
        if bPdxaOceY:
            UFXUK.append((_('IMDb Search'), 'IMDbSearch'))
        if WizweESn:
            UFXUK.append((_('TMDB Info'), 'TMDBInfo'))
        if HikvfLr:
            UFXUK.append((_('OFDb Details'), 'OFDbDetails'))
        if UFXUK == []:
            UFXUK.append((_('No Info Plugins installed...'), 'No Info Plugins installed...'))
        self.session.openWithCallback(self.tmxBeAld, ChoiceBox, title=_('   CoolInfoBox'), list=UFXUK)

    def tmxBeAld(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        SNAVqJygcUu = self['list'].JvSwzXgDeSH()
        IimsWsl = SNAVqJygcUu[0]
        if not IimsWsl:
            return
        name = IimsWsl and IimsWsl.getEventName() or ''
        if nKGKSPXPp == 'SeriesPlugin':
            from Plugins.Extensions.SeriesPlugin.SeriesPluginInfoScreen import SeriesPluginInfoScreen
            UMUhLJhkv = SNAVqJygcUu[1]
            self.session.open(SeriesPluginInfoScreen, UMUhLJhkv, IimsWsl)
        elif nKGKSPXPp == 'The TVDB Info':
            from Plugins.Extensions.TheTVDB.plugin import TheTVDBMain
            self.session.open(TheTVDBMain, name)
        elif nKGKSPXPp == 'IMDbSearch':
            from Plugins.Extensions.IMDb.plugin import IMDB
            self.session.open(IMDB, name)
        elif nKGKSPXPp == 'TMDBInfo':
            from Plugins.Extensions.TMDb.plugin import TMDbMain
            self.session.open(TMDbMain, name)
        elif nKGKSPXPp == 'OFDbDetails':
            from Plugins.Extensions.OFDb.plugin import OFDB
            self.session.open(OFDB, name)

    def esPNG(self):
        OXeXRlHHxgjsyrP = self['list'].JvSwzXgDeSH()
        cnZAOIp = OXeXRlHHxgjsyrP[1]
        vllXeBUshF = OXeXRlHHxgjsyrP[0]
        if not vllXeBUshF:
            return
        else:
            FZxOvzpGBD = vllXeBUshF.getEventId()
            fXYLLkn = cnZAOIp.ref.toString()
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                    self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
                    self['list'].l.invalidate()
                    break
            else:
                ZFcHE = RecordTimerEntry(cnZAOIp, checkOldTimers=True, *parseEvent(vllXeBUshF))
                BjDtxuaz = NavigationInstance.instance.RecordTimer.record(ZFcHE)
                if BjDtxuaz is not None:
                    for x in BjDtxuaz:
                        if x.setAutoincreaseEnd(ZFcHE):
                            self.session.nav.RecordTimer.timeChanged(x)

                    BjDtxuaz = self.session.nav.RecordTimer.record(ZFcHE)
                    if BjDtxuaz is not None:
                        self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, BjDtxuaz)
                else:
                    self.qvZsfOLaorS.start(3000, True)
                self['list'].l.invalidate()

            self.WlFKMlyFxSWrG()
            return

    def EekrcnjXd(self):
        self.session.open(TimerEditList)

    def EmOZX(self):
        fzPWRjmyFOdPgK = self['list'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        sTgNxkmJlcmVCv = fzPWRjmyFOdPgK[1]
        if not lWJAurf:
            return
        FZxOvzpGBD = lWJAurf.getEventId()
        fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
        for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
            if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
                self.session.openWithCallback(self.pwCaxqRZQsvS, ChoiceBox, title=_('Cool Timer Edit :' + '\n\n%s') % lWJAurf.getEventName(), list=[(_('edit this Timer ?'), 'edit'), (_('delete this Timer ?'), 'delete'), (_('delete this Timer and recording ?'), 'delrec')])
                break
        else:
            ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(lWJAurf))
            self.session.openWithCallback(self.SohIHVvAMnbAXX, TimerEntry, ZFcHE)

    def pwCaxqRZQsvS(self, nKGKSPXPp):
        QHYMHhwOVIXtLT = self.QHYMHhwOVIXtLT
        pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp)

    def SohIHVvAMnbAXX(self, nKGKSPXPp):
        self.qvZsfOLaorS.start(3000, True)
        if nKGKSPXPp[0]:
            WFVjWbKbX = nKGKSPXPp[1]
            QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
            if QptgJyXzKf is not None:
                for x in QptgJyXzKf:
                    if x.setAutoincreaseEnd(WFVjWbKbX):
                        self.session.nav.RecordTimer.timeChanged(x)

                QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
                if QptgJyXzKf is not None:
                    self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, QptgJyXzKf)
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('TimerEdit'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('TimerEdit'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('TimerEdit'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('TimerEdit'))
        return

    def AoKSzJQJax(self, nKGKSPXPp):
        self.SohIHVvAMnbAXX(nKGKSPXPp)

    def WlFKMlyFxSWrG(self):
        KhbPMNc = self['list'].JvSwzXgDeSH()
        IimsWsl = KhbPMNc[0]
        self['Event'].newEvent(IimsWsl)
        yyJciFsdx = ''
        if IimsWsl is not None:
            geikSRpcvam = time()
            cpUukOBh = IimsWsl.getBeginTime()
            rbuTrfjskKNUrpX = localtime(geikSRpcvam)
            xCcvK = localtime(cpUukOBh)
            if rbuTrfjskKNUrpX[2] != xCcvK[2]:
                yyJciFsdx = '%s %d.%d.' % (self.PsMWO[xCcvK[6]], xCcvK[2], xCcvK[1])
            else:
                yyJciFsdx = '%s %d.%d.' % (_('Today'), xCcvK[2], xCcvK[1])
        self['date'].setText(yyJciFsdx)
        if KhbPMNc[1]:
            self['Service'].newService(KhbPMNc[1].ref)
        else:
            self['Service'].newService(None)
        if not IimsWsl:
            if self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText('')
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText('')
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText('')
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText('')
            return
        else:
            YzImKHZN = KhbPMNc[1]
            FZxOvzpGBD = IimsWsl.getEventId()
            EjcPO = YzImKHZN.ref.toString()
            xCEOmOL = False
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == EjcPO:
                    xCEOmOL = True
                    break

            if xCEOmOL:
                if self.jIDDtifEzLAQAtH == 'Timer':
                    self['key_green'].setText(_('TimerEdit'))
                elif self.SuVhHLBrOFx == 'Timer':
                    self['key_red'].setText(_('TimerEdit'))
                elif self.KhCcbywN == 'Timer':
                    self['key_yellow'].setText(_('TimerEdit'))
                elif self.gYtswyvbtJ == 'Timer':
                    self['key_blue'].setText(_('TimerEdit'))
            elif self.jIDDtifEzLAQAtH == 'Timer':
                self['key_green'].setText(_('Timer'))
            elif self.SuVhHLBrOFx == 'Timer':
                self['key_red'].setText(_('Timer'))
            elif self.KhCcbywN == 'Timer':
                self['key_yellow'].setText(_('Timer'))
            elif self.gYtswyvbtJ == 'Timer':
                self['key_blue'].setText(_('Timer'))
            return

    def NuGwC(self):
        try:
            self.session.openWithCallback(self.wImiGCFpPSqZ, oifusNtsQLjEI)
        except:
            pass

    def wImiGCFpPSqZ(self):
        self.hide()
        CCGmain(self.session, self.aewDrpsjqX)
        if WvYVaQ != self.YbVViHHAtS and SAQsYCIeDb != self.YbVViHHAtS:
            self.session.open(MessageBox, Po, MessageBox.TYPE_INFO)
        self.close(self.FUiTqUurDFxy)

    def uzzLIxD(self):
        FuFccNSayop = ServiceReference(TrruhKvKi.getCurrentSelection())
        name = FuFccNSayop.getServiceName()
        weApfA = []
        weApfA.append((_('Channel Selection') + ' - ' + _('Favourites'), 'FAVO'))
        weApfA.append((_('Channel Selection') + ' - ' + _('Providers'), 'PROV'))
        weApfA.append((_('Channel Selection') + ' - ' + _('Satellites'), 'SAT'))
        weApfA.append((_('Channel Selection') + ' - ' + _('All') + ' ' + _('Services'), 'ALL'))
        weApfA.append((_('Channel Selection') + ' - ' + _('Channellist'), 'CHA'))
        self.session.openWithCallback(self.pjpLebQMsxgg, ChoiceBox, title='Cool Channel Guide ' + _('Advanced Options'), list=weApfA)

    def pjpLebQMsxgg(self, OMmcwfM):
        OMmcwfM = OMmcwfM and OMmcwfM[1]
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            if OMmcwfM:
                if OMmcwfM == 'FAVO':

                    def showFavouritesList(self):
                        TrruhKvKi.showFavourites()
                        self.session.execDialog(TrruhKvKi)

                    showFavouritesList(InfoBar.instance)
                elif OMmcwfM == 'PROV':

                    def showProvidersList(self):
                        TrruhKvKi.showProviders()
                        self.session.execDialog(TrruhKvKi)

                    showProvidersList(InfoBar.instance)
                elif OMmcwfM == 'SAT':

                    def showSatellitesList(self):
                        TrruhKvKi.showSatellites()
                        self.session.execDialog(TrruhKvKi)

                    showSatellitesList(InfoBar.instance)
                elif OMmcwfM == 'ALL':

                    def showAllList(self):
                        TrruhKvKi.showAllServices()
                        self.session.execDialog(TrruhKvKi)

                    showAllList(InfoBar.instance)
                elif OMmcwfM == 'CHA':
                    InfoBar.openServiceList(InfoBar.instance)
                self.hide()
                self.close(self.FUiTqUurDFxy)

    def nORxTbRjzsNVch(self):
        self.FUiTqUurDFxy = True
        MkrSeAFlTK = self['list'].JvSwzXgDeSH()[1]
        ovhyteog = eServiceReference(str(MkrSeAFlTK))
        if not ovhyteog.flags & eServiceReference.isMarker:
            if MkrSeAFlTK:
                FllUJdlN(MkrSeAFlTK.ref)
                self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
                self['list'].ZGjyWp(self.ZsMYlBwYFBsTydI, self.vzDGDGAQLSCa)

    def JIQKwPOcc(self):
        self.FUiTqUurDFxy = True
        YJtIpOkBKsCcvSg = self['list'].JvSwzXgDeSH()[1]
        ovhyteog = eServiceReference(str(YJtIpOkBKsCcvSg))
        if not ovhyteog.flags & eServiceReference.isMarker:
            if YJtIpOkBKsCcvSg:
                FllUJdlN(YJtIpOkBKsCcvSg.ref)
                self.close(self.FUiTqUurDFxy)


class lKVEwGYfTpgWH(HTMLComponent, GUIComponent):

    def __init__(self, pOHOrwCihqC = None, QHYMHhwOVIXtLT = None):
        self.TPVxuSuwYBrUelM = eServiceCenter.getInstance()
        self.WQqNiBbHzOJUrXt = None
        self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
        self.wuqkSpGyxrM = ePicLoad()
        self.PVPFJS = []
        if pOHOrwCihqC is not None:
            self.PVPFJS.append(pOHOrwCihqC)
        GUIComponent.__init__(self)
        self.l = eListboxPythonMultiContent()
        self.jvTmTJHlfxPIP = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.myzqmNzI = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.HQvLEHVqmBsVgHk = parseFont('Regular;18', ((1, 1), (1, 1)))
        self.l.setFont(0, self.jvTmTJHlfxPIP)
        self.l.setFont(1, self.myzqmNzI)
        self.l.setFont(2, self.HQvLEHVqmBsVgHk)
        self.l.setBuildFunc(self.ewNCIkurKx)
        self.wPCDGUrewS = 1
        self.OGBpHgi = 245
        self.xetVW = 14
        self.nOvheUu = 100
        self.EnJelDGikSIP = 10
        self.xHpqYxluJNkS = 310
        self.IwKiKwc = 100
        self.CwbbgtPbYdAJaNS = 0
        self.icJJVKHwold = 32
        self.oVoKs = 478
        self.jmwYOBDN = 0
        self.NncyJJpQTAyzZ = 16
        self.ShRiUS = 0
        self.XXUhJezSeLAe = 16
        self.MUWkjDk = 0
        self.mWkRquQGU = 10
        self.cwjjzqyTcBh = 40
        self.mMQSGwZt = 0
        self.BwBxpeGsFk = 4
        self.DrEcqGyi = 305
        self.GwbyeYYLAZpKfc = 0
        self.RVaddhJ = 9
        self.HkPIn = 285
        self.vDtXdSWMj = 150
        self.sZFcJcEYedYG = None
        self.RYWUNgKwKamFGs = None
        self.AbCAHrrQoOcBPH = 3905737
        self.TNOcIyTOCMk = 2174148
        self.chSpBcKz = 3905737
        self.Wzjij = 16777215
        self.srNoImCrP = 16737792
        self.hXbYdg = 11902465
        self.ZWXRUOATTV = 10425107
        self.BPTUvuBjQ = 16737792
        self.HaJKV = 6316128
        self.WubpaSVNw = 16777215
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.FcatbmGJKhWdbnB = None
        self.cfCIaMrxr = []
        HaqcC = config.skin.primary_skin.value
        HaqcC = HaqcC[:HaqcC.rfind('/')]
        HaqcC = '/usr/share/enigma2/' + HaqcC + '/skin_default/icons/marker.png'
        if not fileExists(HaqcC):
            HaqcC = '/usr/share/enigma2/skin_default/icons/marker.png'
        self.PlWoQjw = loadPNG(HaqcC)
        return

    def applySkin(self, desktop, parent):
        dyYxANT = []
        if self.skinAttributes is not None:
            for Obqlh, value in self.skinAttributes:
                if Obqlh == 'CoolFont':
                    self.jvTmTJHlfxPIP = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(0, self.jvTmTJHlfxPIP)
                elif Obqlh == 'CoolServiceFont':
                    self.myzqmNzI = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(1, self.myzqmNzI)
                elif Obqlh == 'CoolEventFont':
                    self.HQvLEHVqmBsVgHk = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(2, self.HQvLEHVqmBsVgHk)
                elif Obqlh == 'CoolServiceSize':
                    self.DrEcqGyi = int(value)
                elif Obqlh == 'CoolEventSize':
                    self.oVoKs = int(value)
                elif Obqlh == 'CoolServicePos':
                    self.mMQSGwZt = int(value)
                elif Obqlh == 'CoolServiceHPos':
                    self.BwBxpeGsFk = int(value)
                elif Obqlh == 'CoolMarkerPos':
                    self.jmwYOBDN = int(value)
                elif Obqlh == 'CoolMarkerHPos':
                    self.NncyJJpQTAyzZ = int(value)
                elif Obqlh == 'CoolMarkerPicPos':
                    self.ShRiUS = int(value)
                elif Obqlh == 'CoolMarkerPicHPos':
                    self.XXUhJezSeLAe = int(value)
                elif Obqlh == 'CoolBar':
                    self.wPCDGUrewS = int(value)
                elif Obqlh == 'CoolBarPos':
                    self.OGBpHgi = int(value)
                elif Obqlh == 'CoolBarHPos':
                    self.xetVW = int(value)
                elif Obqlh == 'CoolBarSize':
                    self.nOvheUu = int(value)
                elif Obqlh == 'CoolBarHigh':
                    self.EnJelDGikSIP = int(value)
                elif Obqlh == 'CoolTimePos':
                    self.HkPIn = int(value)
                elif Obqlh == 'CoolDurationPos':
                    self.xHpqYxluJNkS = int(value)
                elif Obqlh == 'CoolTime':
                    self.GwbyeYYLAZpKfc = int(value)
                elif Obqlh == 'CoolTimeHPos':
                    self.RVaddhJ = int(value)
                elif Obqlh == 'CoolTimeSize':
                    self.vDtXdSWMj = int(value)
                elif Obqlh == 'CoolDurationSize':
                    self.IwKiKwc = int(value)
                elif Obqlh == 'CoolEventPos':
                    self.CwbbgtPbYdAJaNS = int(value)
                elif Obqlh == 'CoolEventHPos':
                    self.icJJVKHwold = int(value)
                elif Obqlh == 'CoolPico':
                    self.cwjjzqyTcBh = int(value)
                elif Obqlh == 'CoolPicoPos':
                    self.MUWkjDk = int(value)
                elif Obqlh == 'CoolPicoHPos':
                    self.mWkRquQGU = int(value)
                elif Obqlh == 'CoolServiceColor':
                    self.BPTUvuBjQ = parseColor(value).argb()
                elif Obqlh == 'CoolMarkerColor':
                    self.srNoImCrP = parseColor(value).argb()
                elif Obqlh == 'CoolTunerCol':
                    self.HaJKV = parseColor(value).argb()
                elif Obqlh == 'CoolCurrentCol':
                    self.TNOcIyTOCMk = parseColor(value).argb()
                elif Obqlh == 'CoolBarColor':
                    self.AbCAHrrQoOcBPH = parseColor(value).argb()
                elif Obqlh == 'CoolDurationColor':
                    self.chSpBcKz = parseColor(value).argb()
                elif Obqlh == 'CoolEventColor':
                    self.Wzjij = parseColor(value).argb()
                elif Obqlh == 'CoolBackColor':
                    self.sZFcJcEYedYG = parseColor(value).argb()
                elif Obqlh == 'CoolBackColorSel':
                    self.RYWUNgKwKamFGs = parseColor(value).argb()
                elif Obqlh == 'CoolFontColSel':
                    self.WubpaSVNw = parseColor(value).argb()
                elif Obqlh == 'CoolRecAlarmCol':
                    self.hXbYdg = parseColor(value).argb()
                elif Obqlh == 'CoolRecColor':
                    self.ZWXRUOATTV = parseColor(value).argb()
                else:
                    dyYxANT.append((Obqlh, value))

        self.skinAttributes = dyYxANT
        return GUIComponent.applySkin(self, desktop, parent)

    def JvSwzXgDeSH(self):
        XZNkhLy = 1
        Dovjge = self.l.getCurrentSelection()
        if Dovjge is None:
            return (None, None)
        else:
            gOvtm = Dovjge[XZNkhLy + 1]
            UMUhLJhkv = ServiceReference(Dovjge[XZNkhLy])
            WVAXBEaVAJdsN = self.QvVabvQOoSofkV(UMUhLJhkv, gOvtm)
            return (WVAXBEaVAJdsN, UMUhLJhkv)

    def OGJPWJikcr(self):
        if self.l.getCurrentSelection() is not None:
            return self.l.getCurrentSelection()[0]
        else:
            return 0

    def QvVabvQOoSofkV(self, UMUhLJhkv, gggJixxXg):
        fZKEXQZAIbzej = None
        if self.DTzDLYhRge is not None and gggJixxXg is not None:
            fZKEXQZAIbzej = self.DTzDLYhRge.lookupEventId(UMUhLJhkv.ref, gggJixxXg)
        return fZKEXQZAIbzej

    def BvgWUZlF(func):
        if not self.PVPFJS.eqeAQDfNpE(func):
            self.PVPFJS.append(func)

    def gtYbdvqXEGvY(func):
        self.PVPFJS.remove(func)

    def selectionChanged(self):
        for x in self.PVPFJS:
            if x is not None:
                x()

        return

    def GdjxEetRD(self):
        self.instance.moveSelection(self.instance.moveUp)

    def Krkrxa(self):
        self.instance.moveSelection(self.instance.moveDown)

    GUI_WIDGET = eListbox

    def ewNCIkurKx(self, zuwFdPsBIgsKYj, UMUhLJhkv, VQKNKnUpnwbt, pVdYFhAaXsyyci, qxyEWz, cIlYUZavCM, rbuTrfjskKNUrpX, AemZEBZRFVH):
        try:
            MBwGVCQCuRs = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
            AduwKVqFCtWzeIh = self.mCcXxUnnUdldCM(eServiceReference(UMUhLJhkv), eServiceReference(MBwGVCQCuRs))
        except:
            AduwKVqFCtWzeIh = 1

        rLTFYjFLR = pVdYFhAaXsyyci and self.NSjWHcStKTLbU(UMUhLJhkv, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt)
        cwjjzqyTcBh = self.cwjjzqyTcBh
        DrEcqGyi = self.DrEcqGyi
        oVoKs = self.oVoKs
        sZFcJcEYedYG = self.sZFcJcEYedYG
        RYWUNgKwKamFGs = self.RYWUNgKwKamFGs
        JixFEWcBYWgVHg = 0
        if rLTFYjFLR == True:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.ZWXRUOATTV
        elif rLTFYjFLR == False:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.hXbYdg
        elif not AduwKVqFCtWzeIh:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.HaJKV
        elif CoolAlternative(UMUhLJhkv, self.WQqNiBbHzOJUrXt.toString()):
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = zpWysCGB = dhELvjJBqAwXn = self.TNOcIyTOCMk
        else:
            IljDvazPimAt = self.BPTUvuBjQ
            uSfYSrtgTKg = self.Wzjij
            zpWysCGB = self.AbCAHrrQoOcBPH
            dhELvjJBqAwXn = self.chSpBcKz
            QLxdqGrZFSq = self.WubpaSVNw
        res = [None]
        if UMUhLJhkv[2:4] == '64':
            res.append(MultiContentEntryText(pos=(self.jmwYOBDN, self.NncyJJpQTAyzZ), size=(480, 50), font=1, flags=RT_HALIGN_CENTER, text=AemZEBZRFVH, color=self.srNoImCrP, color_sel=self.srNoImCrP, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
            res.append(MultiContentEntryPixmapAlphaBlend(pos=(self.ShRiUS, self.XXUhJezSeLAe), size=(50, 50), png=self.PlWoQjw, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
        else:
            if config.CTVG.C38.value:
                JixFEWcBYWgVHg = cwjjzqyTcBh / 0.6 + 10
                if self.icJJVKHwold > 20:
                    DrEcqGyi = DrEcqGyi - JixFEWcBYWgVHg
                YTSEoIi = False
                YTSEoIi = findCoolPicon(UMUhLJhkv, AemZEBZRFVH)
                if YTSEoIi:
                    self.wuqkSpGyxrM.setPara((cwjjzqyTcBh / 0.6,
                     cwjjzqyTcBh,
                     1,
                     1,
                     False,
                     1,
                     '#ff000000'))
                    self.wuqkSpGyxrM.startDecode(YTSEoIi, 0, 0, False)
                    res.append(MultiContentEntryPixmapAlphaBlend(pos=(self.MUWkjDk, self.mWkRquQGU), size=(cwjjzqyTcBh / 0.6, cwjjzqyTcBh), png=self.wuqkSpGyxrM.getData(), backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
            res.append(MultiContentEntryText(pos=(self.mMQSGwZt + JixFEWcBYWgVHg, self.BwBxpeGsFk), size=(DrEcqGyi, 50), font=1, text='%02d. ' % self.xpFKRFDhSumIm(UMUhLJhkv) + AemZEBZRFVH, color=IljDvazPimAt, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
            if rbuTrfjskKNUrpX > int(pVdYFhAaXsyyci) and self.icJJVKHwold < 20 and self.wPCDGUrewS == 0:
                oVoKs += self.vDtXdSWMj - self.IwKiKwc
            res.append(MultiContentEntryText(pos=(self.CwbbgtPbYdAJaNS + JixFEWcBYWgVHg, self.icJJVKHwold), size=(oVoKs - JixFEWcBYWgVHg, 50), font=2, text=cIlYUZavCM, color=uSfYSrtgTKg, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
            if pVdYFhAaXsyyci is not None:
                VprrLjtcbPtnLQS = localtime(pVdYFhAaXsyyci)
                JBCDJoHYm = localtime(pVdYFhAaXsyyci + qxyEWz)
                if rbuTrfjskKNUrpX < pVdYFhAaXsyyci:
                    res.append(MultiContentEntryText(pos=(self.HkPIn, self.RVaddhJ), size=(self.vDtXdSWMj, 50), font=2, text='%02d:%02d  -  %02d:%02d' % (VprrLjtcbPtnLQS[3],
                     VprrLjtcbPtnLQS[4],
                     JBCDJoHYm[3],
                     JBCDJoHYm[4]), color=zpWysCGB, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
                    dxypDHxLzcLh = qxyEWz / 60
                else:
                    ZOtbQgTXKRwH = (rbuTrfjskKNUrpX - pVdYFhAaXsyyci) * 100 / qxyEWz
                    dxypDHxLzcLh = (qxyEWz - (rbuTrfjskKNUrpX - pVdYFhAaXsyyci)) / 60
                    if self.GwbyeYYLAZpKfc == 0:
                        GwbyeYYLAZpKfc = '+ %02d' % dxypDHxLzcLh
                    else:
                        GwbyeYYLAZpKfc = '%02d' % ZOtbQgTXKRwH + '%'
                    res.append(MultiContentEntryText(pos=(self.xHpqYxluJNkS, self.RVaddhJ), size=(self.IwKiKwc, 50), font=2, flags=RT_HALIGN_RIGHT, text=GwbyeYYLAZpKfc, color=dhELvjJBqAwXn, color_sel=QLxdqGrZFSq, backcolor=sZFcJcEYedYG, backcolor_sel=RYWUNgKwKamFGs))
                    if self.wPCDGUrewS == 1:
                        res.append(PsVUdJXJ(pos=(self.OGBpHgi, self.xetVW), size=(self.nOvheUu, self.EnJelDGikSIP), percent=ZOtbQgTXKRwH, foreColor=zpWysCGB, foreColorSelected=QLxdqGrZFSq, KNlLJNdkd=sZFcJcEYedYG, KNlLJNdkdSelected=RYWUNgKwKamFGs))
        return res

    def postWidgetCreate(self, instance):
        instance.setWrapAround(True)
        instance.selectionChanged.get().append(self.selectionChanged)
        instance.setContent(self.l)

    def preWidgetRemove(self, instance):
        instance.selectionChanged.get().remove(self.selectionChanged)
        instance.setContent(None)
        return

    def mCcXxUnnUdldCM(self, BidVA, JhKpFAp):
        NHozf = self.TPVxuSuwYBrUelM.info(BidVA)
        return NHozf and NHozf.isPlayable(BidVA, JhKpFAp) or False

    def ZGjyWp(self, qDFTEDFxno, KjUKrjjjHKPvzNX = -1):
        ZDxUJDDCPod = [ (UMUhLJhkv.ref.toString(), 0, KjUKrjjjHKPvzNX) for UMUhLJhkv in qDFTEDFxno ]
        if config.CTVG.C28.value:
            ZDxUJDDCPod.insert(0, 'X0RIBDTCn')
        else:
            ZDxUJDDCPod.insert(0, 'X0RIBDTCN')
        self.ScnvMSTPY = self.sdiQt(ZDxUJDDCPod)
        self.l.setList(self.ScnvMSTPY)
        self.selectionChanged()

    def LItiOOUy(self, SqpegV):
        BiVMJSTCWKQvuMk = [ x[3] and (x[1], SqpegV, x[3]) or (x[1], SqpegV, 0) for x in self.ScnvMSTPY ]
        BiVMJSTCWKQvuMk.insert(0, 'XRIBDTCn')
        tOObZiAFRL = self.sdiQt(BiVMJSTCWKQvuMk)
        cnt = 0
        for x in tOObZiAFRL:
            zuwFdPsBIgsKYj = self.ScnvMSTPY[cnt][0] + SqpegV
            if zuwFdPsBIgsKYj >= 0:
                if x[2] is not None:
                    self.ScnvMSTPY[cnt] = (zuwFdPsBIgsKYj,
                     x[0],
                     x[1],
                     x[2],
                     x[3],
                     x[4],
                     x[5],
                     x[6])
            cnt += 1

        self.l.setList(self.ScnvMSTPY)
        self.selectionChanged()
        return

    def xpFKRFDhSumIm(self, UMUhLJhkv):
        global xKmXaE
        if xKmXaE is None or not self.cfCIaMrxr:
            xKmXaE = TrruhKvKi.getBouquetNumOffset(FufElMDyUtWr)
            self.FcatbmGJKhWdbnB = self.TPVxuSuwYBrUelM.list(FufElMDyUtWr)
            self.cfCIaMrxr = self.FcatbmGJKhWdbnB and self.FcatbmGJKhWdbnB.getContent('S', True)
        NhsvvZxTKXnV = 0
        iXgrny = 0
        if self.cfCIaMrxr:
            OCCKSDwCPbq = len(self.cfCIaMrxr)
            for tlvldyLLXXHo in list(range(OCCKSDwCPbq)):
                KsiNzjF = (NhsvvZxTKXnV + tlvldyLLXXHo) % OCCKSDwCPbq
                mutbPpmzLHBYz = self.cfCIaMrxr[KsiNzjF]
                if mutbPpmzLHBYz[2:4] == '64':
                    iXgrny += 1
                if UMUhLJhkv == mutbPpmzLHBYz:
                    NhsvvZxTKXnV = KsiNzjF
                    return xKmXaE + NhsvvZxTKXnV - iXgrny + 1

        return 0

    def NSjWHcStKTLbU(self, fXYLLkn, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt):
        for x in self.QHYMHhwOVIXtLT.timer_list:
            if x.service_ref.ref.toString() == fXYLLkn:
                blmRapeotWYHCEX = pVdYFhAaXsyyci + qxyEWz
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                if x.eit == VQKNKnUpnwbt:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True
                elif pVdYFhAaXsyyci <= TteNjwT <= blmRapeotWYHCEX:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True

        for x in self.QHYMHhwOVIXtLT.processed_timers:
            if x.disabled and x.service_ref.ref.toString() == fXYLLkn:
                if x.eit == VQKNKnUpnwbt:
                    return False

    def HRhXvd(self):
        iJfmNqbQgaPiZ = eServiceReference.isMarker | eServiceReference.isDirectory
        Hhhivv = eServiceReference.isMarker
        VbLvEpoznAcm = self.JvSwzXgDeSH()[1]
        UMUhLJhkv = eServiceReference(str(VbLvEpoznAcm))
        KUsFwUzw = -1
        TRbDx = -1
        if FufElMDyUtWr and FufElMDyUtWr.valid():
            if FufElMDyUtWr.flags & eServiceReference.isDirectory:
                zGhXknMOhQsddY = self.TPVxuSuwYBrUelM.list(FufElMDyUtWr)
                if zGhXknMOhQsddY is not None:
                    while True:
                        jDeUUQ = zGhXknMOhQsddY.getNext()
                        if not jDeUUQ.valid():
                            break
                        if not jDeUUQ.flags & iJfmNqbQgaPiZ:
                            KUsFwUzw += 1
                        elif jDeUUQ.flags & Hhhivv:
                            KUsFwUzw += 1
                            if TRbDx != -1:
                                return KUsFwUzw
                        if UMUhLJhkv == jDeUUQ:
                            TRbDx = KUsFwUzw

        if TRbDx == KUsFwUzw:
            return 0
        else:
            return KUsFwUzw
            return

    def IwVOhBap(self):
        iJfmNqbQgaPiZ = eServiceReference.isMarker | eServiceReference.isDirectory
        Hhhivv = eServiceReference.isMarker
        AVybbBGICE = self.JvSwzXgDeSH()[1]
        ndZcshUacOagc = eServiceReference(str(AVybbBGICE))
        npiZGUZ = 0
        musUlaaILaxcvl = 0
        if FufElMDyUtWr and FufElMDyUtWr.valid():
            if FufElMDyUtWr.flags & eServiceReference.isDirectory:
                LcVpaBWwPZx = self.TPVxuSuwYBrUelM.list(FufElMDyUtWr)
                if LcVpaBWwPZx is not None:
                    while True:
                        jDeUUQ = LcVpaBWwPZx.getNext()
                        if not jDeUUQ.valid():
                            break
                        if ndZcshUacOagc == jDeUUQ:
                            if npiZGUZ:
                                return musUlaaILaxcvl
                        if not jDeUUQ.flags & iJfmNqbQgaPiZ:
                            npiZGUZ += 1
                        elif jDeUUQ.flags & Hhhivv:
                            musUlaaILaxcvl = npiZGUZ
                            npiZGUZ += 1

        return npiZGUZ - 1

    def sdiQt(self, list, MlBIgDzxYSu = None):
        if self.DTzDLYhRge is not None:
            if MlBIgDzxYSu is not None:
                return self.DTzDLYhRge.lookupEvent(list, MlBIgDzxYSu)
            else:
                return self.DTzDLYhRge.lookupEvent(list)
        return []

    def UrfFYoRsn(self, cnZAOIp):
        if not cnZAOIp:
            return
        tAaMXETO = 0
        fXYLLkn = cnZAOIp.toString()
        for x in self.ScnvMSTPY:
            if CoolAlternative(x[1], fXYLLkn):
                self.instance.moveSelectionTo(tAaMXETO)
                break
            tAaMXETO += 1


class rHAPXA(HTMLComponent, GUIComponent):

    def __init__(self, pOHOrwCihqC = None, QHYMHhwOVIXtLT = None, hXYPZeFsC = 120, QflrzkxuriKKT = False):
        GUIComponent.__init__(self)
        self.l = eListboxPythonMultiContent()
        self.PVPFJS = []
        self.FoLaaHWDpTaD = 0
        self.CxOZqdD = 0
        self.nFWrGJyGHsBV = None
        self.ScnvMSTPY = None
        self.oOJsdNcNtHUAYXv = None
        self.jbKPjQCEJlY = None
        self.FuFccNSayop = None
        self.WQqNiBbHzOJUrXt = None
        self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
        self.aHzrtJlvyhnZ = time()
        if pOHOrwCihqC is not None:
            self.PVPFJS.append(pOHOrwCihqC)
        self.LiyMOiyqP = 50
        self.l.setBuildFunc(self.KIiMbYLKzL)
        self.mOEosunLpOyhYek(QflrzkxuriKKT)
        self.TPVxuSuwYBrUelM = eServiceCenter.getInstance()
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.wuqkSpGyxrM = ePicLoad()
        self.uSgmv = None
        self.KLHMqynlr = 0
        self.LMMuQlaCTdkQ = 16777215
        self.WubpaSVNw = 0
        self.LIvXVTXQFhMmAK = 16777215
        self.tHCcYDmnTQeKqmJ = 0
        self.tsvihiywhe = 16777215
        self.sZFcJcEYedYG = 2966878
        self.gLvHtGYJwDnaL = 16777215
        self.evfEaAJRzeV = 13587283
        self.hXbYdg = 16766976
        self.fTWqsfSMXv = 10420224
        self.Gwzsvq = 33375
        self.cruOnhBsdnf = 16777215
        self.NnoHj = 0
        self.gciYoOUoElTq = 12632256
        self.fDeljq = 0
        self.mFuSMdHDOvptbxd = 12632256
        self.TNOcIyTOCMk = 5335958
        self.ooGJC = 16777215
        self.HaJKV = 16777215
        self.qEsBEoz = None
        return

    def applySkin(self, desktop, screen):
        if self.skinAttributes is not None:
            dyYxANT = []
            for Obqlh, value in self.skinAttributes:
                if Obqlh == 'CoolFontCol':
                    self.LMMuQlaCTdkQ = parseColor(value).argb()
                elif Obqlh == 'CoolFontColSel':
                    self.WubpaSVNw = parseColor(value).argb()
                elif Obqlh == 'CoolNowFontColSel':
                    self.tHCcYDmnTQeKqmJ = parseColor(value).argb()
                elif Obqlh == 'CoolNowFontCol':
                    self.LIvXVTXQFhMmAK = parseColor(value).argb()
                elif Obqlh == 'CoolBorderColR':
                    self.NnoHj = parseColor(value).argb()
                elif Obqlh == 'CoolBorderColL':
                    self.fDeljq = parseColor(value).argb()
                elif Obqlh == 'coolbordercolR':
                    self.gciYoOUoElTq = parseColor(value).argb()
                elif Obqlh == 'coolbordercolL':
                    self.mFuSMdHDOvptbxd = parseColor(value).argb()
                elif Obqlh == 'CoolBackColor':
                    self.sZFcJcEYedYG = parseColor(value).argb()
                elif Obqlh == 'CoolTunerBackCol':
                    self.qEsBEoz = parseColor(value).argb()
                elif Obqlh == 'CoolTunerCol':
                    self.HaJKV = parseColor(value).argb()
                elif Obqlh == 'CoolRecCol':
                    self.evfEaAJRzeV = parseColor(value).argb()
                elif Obqlh == 'CoolRecAlarmCol':
                    self.hXbYdg = parseColor(value).argb()
                elif Obqlh == 'CoolNowCol':
                    self.Gwzsvq = parseColor(value).argb()
                elif Obqlh == 'CoolBackColorSel':
                    self.gLvHtGYJwDnaL = parseColor(value).argb()
                elif Obqlh == 'CoolRecColSel':
                    self.fTWqsfSMXv = parseColor(value).argb()
                elif Obqlh == 'CoolNowColSel':
                    self.cruOnhBsdnf = parseColor(value).argb()
                elif Obqlh == 'CoolPiconFontCol':
                    self.tsvihiywhe = parseColor(value).argb()
                elif Obqlh == 'CoolCurrentCol':
                    self.TNOcIyTOCMk = parseColor(value).argb()
                elif Obqlh == 'CoolCurrentColSel':
                    self.ooGJC = parseColor(value).argb()
                elif Obqlh == 'CoolPiconBackCol':
                    self.uSgmv = parseColor(value).argb()
                elif Obqlh == 'CoolNoPiconBackCol':
                    self.KLHMqynlr = parseColor(value).argb()
                elif Obqlh == 'CoolNowBackCol':
                    print("--------------------CoolNowBackCol-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolBackCol':
                    print("--------------------CoolBackCol-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolBackColSel':
                    print("--------------------CoolBackColSel-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolTVBackCol':
                    print("--------------------CoolTVBackCol-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolTVBackColSel':
                    print("--------------------CoolTVBackColSel-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolNowBackColSel':
                    print("--------------------CoolNowBackColSel-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolBackRecCol':
                    print("--------------------CoolBackRecCol-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolBackRecColSel':
                    print("--------------------CoolBackRecColSel-------------------- don't exist... please check your Skin-----------------------------------")
                elif Obqlh == 'CoolBackRecxCol':
                    print("--------------------CoolBackRecxCol-------------------- don't exist... please check your Skin-----------------------------------")
                else:
                    dyYxANT.append((Obqlh, value))

            self.skinAttributes = dyYxANT
        rc = GUIComponent.applySkin(self, desktop, screen)
        self.eHXbbUpQo()
        return rc

    def BvgWUZlF(func):
        if not self.PVPFJS.eqeAQDfNpE(func):
            self.PVPFJS.append(func)

    def gtYbdvqXEGvY(func):
        self.PVPFJS.remove(func)

    def amlGDzFUp(self):
        WoRENKUNiWL = self.FuFccNSayop
        FuFccNSayop = self.FuFccNSayop = self.l.getCurrentSelection()
        nFWrGJyGHsBV = self.CuVTDmRDLwV()
        geikSRpcvam = time()
        if WoRENKUNiWL and self.jbKPjQCEJlY is not None:
            czThGKpREWEJFhE = WoRENKUNiWL[2]
            jbKPjQCEJlY = czThGKpREWEJFhE[self.jbKPjQCEJlY]
            if self.aHzrtJlvyhnZ < jbKPjQCEJlY[2] or jbKPjQCEJlY[2] + jbKPjQCEJlY[3] < self.aHzrtJlvyhnZ:
                self.aHzrtJlvyhnZ = jbKPjQCEJlY[2]
        if geikSRpcvam > self.aHzrtJlvyhnZ:
            self.aHzrtJlvyhnZ = geikSRpcvam
        if FuFccNSayop:
            self.jbKPjQCEJlY = None
            czThGKpREWEJFhE = FuFccNSayop[2]
            if czThGKpREWEJFhE and len(czThGKpREWEJFhE):
                self.jbKPjQCEJlY = idx = 0
                for ERoOCCVi in czThGKpREWEJFhE:
                    if ERoOCCVi[2] <= self.aHzrtJlvyhnZ and ERoOCCVi[2] + ERoOCCVi[3] > self.aHzrtJlvyhnZ:
                        self.jbKPjQCEJlY = idx
                        break
                    idx += 1

        self.vRWagvtcPAWTrTv(0)
        return

    def rUrCTvxvlF(self):
        WoRENKUNiWL = self.FuFccNSayop
        FuFccNSayop = self.FuFccNSayop = self.l.getCurrentSelection()
        nFWrGJyGHsBV = self.CuVTDmRDLwV()
        aHzrtJlvyhnZ = time()
        if WoRENKUNiWL and self.jbKPjQCEJlY is not None:
            BYRkmWItkVfAhY = WoRENKUNiWL[2]
            jbKPjQCEJlY = BYRkmWItkVfAhY[self.jbKPjQCEJlY]
            if jbKPjQCEJlY[2] > aHzrtJlvyhnZ:
                aHzrtJlvyhnZ = jbKPjQCEJlY[2]
        if FuFccNSayop:
            self.jbKPjQCEJlY = 0
            BYRkmWItkVfAhY = FuFccNSayop[2]
            kZvVxXK = None
            if BYRkmWItkVfAhY and len(BYRkmWItkVfAhY):
                LpqdaRI = 0
                oFfDqCcBuy = 0
                for WVAXBEaVAJdsN in BYRkmWItkVfAhY:
                    OKgfXTcaU = WVAXBEaVAJdsN[2]
                    if OKgfXTcaU < nFWrGJyGHsBV:
                        OKgfXTcaU = nFWrGJyGHsBV
                    WcHCLe = abs(OKgfXTcaU - aHzrtJlvyhnZ)
                    if kZvVxXK is None or WcHCLe < LpqdaRI:
                        kZvVxXK = oFfDqCcBuy
                        LpqdaRI = WcHCLe
                    if kZvVxXK is not None and OKgfXTcaU > aHzrtJlvyhnZ:
                        break
                    oFfDqCcBuy += 1

            self.jbKPjQCEJlY = kZvVxXK
        self.vRWagvtcPAWTrTv(0)
        return

    def JvSwzXgDeSH(self):
        if self.FuFccNSayop is None:
            return (None, None)
        else:
            BYRkmWItkVfAhY = self.FuFccNSayop[2]
            refstr = self.FuFccNSayop[0]
            if self.jbKPjQCEJlY is None or not BYRkmWItkVfAhY or not len(BYRkmWItkVfAhY):
                return (None, ServiceReference(refstr))
            ERoOCCVi = BYRkmWItkVfAhY[self.jbKPjQCEJlY]
            gTYTav = ERoOCCVi[0]
            UMUhLJhkv = ServiceReference(refstr)
            ERoOCCVi = self.QvVabvQOoSofkV(UMUhLJhkv, gTYTav)
            return (ERoOCCVi, UMUhLJhkv)

    def OGJPWJikcr(self):
        if self.l.getCurrentSelection() is not None:
            return self.l.getCurrentSelection()[0]
        else:
            return 0

    def QvVabvQOoSofkV(self, UMUhLJhkv, gOvtm):
        ERoOCCVi = None
        if self.DTzDLYhRge is not None and gOvtm is not None:
            ERoOCCVi = self.DTzDLYhRge.lookupEventId(UMUhLJhkv.ref, gOvtm)
        return ERoOCCVi

    def rxOsF(self, sTgNxkmJlcmVCv):
        if sTgNxkmJlcmVCv is not None:
            for x in list(range(len(self.ScnvMSTPY))):
                if CoolAlternative(self.ScnvMSTPY[x][0], sTgNxkmJlcmVCv.toString()):
                    return x

        return

    def UrfFYoRsn(self, sTgNxkmJlcmVCv):
        chCPHIUuTCG = self.rxOsF(sTgNxkmJlcmVCv)
        if chCPHIUuTCG is None:
            chCPHIUuTCG = 0
        self.qZJVJfj(chCPHIUuTCG)
        return

    def selectionChanged(self):
        for selC in self.PVPFJS:
            if selC is not None:
                selC()

        return

    def fCqCYE(self):
        cuGqUJJ = self.l.getCurrentSelection()
        if cuGqUJJ:
            self.amlGDzFUp()

    def qZJVJfj(self, tAaMXETO):
        if self.instance is not None:
            self.instance.moveSelectionTo(tAaMXETO)
        return

    def mOEosunLpOyhYek(self, QflrzkxuriKKT):
        if QflrzkxuriKKT:
            self.l.setSelectableFunc(self.PysAVSnES)

    GUI_WIDGET = eListbox

    def PysAVSnES(self, UMUhLJhkv, fzxOJINWMUI, event_list):
        return event_list and len(event_list) and True or False

    def KIiMbYLKzL(self, UMUhLJhkv, AemZEBZRFVH, BYRkmWItkVfAhY):
        try:
            MBwGVCQCuRs = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
            AduwKVqFCtWzeIh = self.mCcXxUnnUdldCM(eServiceReference(UMUhLJhkv), eServiceReference(MBwGVCQCuRs))
        except:
            AduwKVqFCtWzeIh = 1

        gvsuoqIdJEsI = self.jkzfjQpVYQq
        wjbJWVX = self.oOJsdNcNtHUAYXv
        ikBbwgkgDDmiRFh = self.LMMuQlaCTdkQ
        cHSGLu = self.WubpaSVNw
        YTSEoIi = False
        res = [None]
        if self.LiyMOiyqP <= 50:
            HQFwXZnluWfdTw = 2
            if config.CTVG.C38.value:
                YTSEoIi = findCoolPicon(UMUhLJhkv, AemZEBZRFVH)
            if YTSEoIi:
                self.wuqkSpGyxrM.startDecode(YTSEoIi, 0, 0, False)
                YTSEoIi = self.wuqkSpGyxrM.getData()
                UFkGHX = (config.CTVG.C52.value - config.CTVG.C51.value) / 2
                res.append(MultiContentEntryPixmapAlphaBlend(pos=(0, 0 + UFkGHX), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), png=YTSEoIi, backcolor=self.uSgmv, backcolor_sel=0))
            elif not YTSEoIi and config.CTVG.C29.value != 'No':
                if self.WQqNiBbHzOJUrXt.toString() == UMUhLJhkv:
                    DWEpcJmQ = self.SmgEugboREz
                    res.append(MultiContentEntryPixmapAlphaTest(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), png=DWEpcJmQ))
                else:
                    DWEpcJmQ = self.BEylY
                    res.append(MultiContentEntryPixmapAlphaTest(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), png=DWEpcJmQ))
                res.append(MultiContentEntryText(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), font=0, flags=RT_HALIGN_CENTER | RT_VALIGN_CENTER, text=AemZEBZRFVH, color=self.tsvihiywhe, border_width=1, border_color=self.fDeljq))
            else:
                res.append(MultiContentEntryText(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), font=0, flags=RT_HALIGN_CENTER | RT_VALIGN_CENTER, text=AemZEBZRFVH, color=self.tsvihiywhe, border_width=1, border_color=self.mFuSMdHDOvptbxd, backcolor=self.KLHMqynlr, backcolor_sel=self.TNOcIyTOCMk))
        elif self.LiyMOiyqP > 50:
            HQFwXZnluWfdTw = 1
            if config.CTVG.C37.value:
                YTSEoIi = findCoolPicon(UMUhLJhkv, AemZEBZRFVH)
            if YTSEoIi:
                self.wuqkSpGyxrM.startDecode(YTSEoIi, 0, 0, False)
                YTSEoIi = self.wuqkSpGyxrM.getData()
                AyLCIGZZwKtrI = (config.CTVG.C50.value - config.CTVG.C49.value) / 2
                res.append(MultiContentEntryPixmapAlphaBlend(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + AyLCIGZZwKtrI), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), png=YTSEoIi, backcolor=self.uSgmv, backcolor_sel=0))
            elif not YTSEoIi and config.CTVG.C29.value != 'No':
                if self.WQqNiBbHzOJUrXt.toString() == UMUhLJhkv:
                    DWEpcJmQ = self.SmgEugboREz
                    res.append(MultiContentEntryPixmapAlphaTest(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), png=DWEpcJmQ))
                else:
                    DWEpcJmQ = self.BEylY
                    res.append(MultiContentEntryPixmapAlphaTest(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), png=DWEpcJmQ))
                res.append(MultiContentEntryText(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), font=0, flags=RT_HALIGN_CENTER | RT_VALIGN_CENTER, text=AemZEBZRFVH, color=self.tsvihiywhe, border_width=1, border_color=self.fDeljq))
            else:
                res.append(MultiContentEntryText(pos=(gvsuoqIdJEsI.x + 1, gvsuoqIdJEsI.y + 1), size=(gvsuoqIdJEsI.w - 2, gvsuoqIdJEsI.h - 2), font=0, flags=RT_HALIGN_CENTER | RT_VALIGN_CENTER, text=AemZEBZRFVH, color=self.tsvihiywhe, border_width=1, border_color=self.mFuSMdHDOvptbxd, backcolor=self.KLHMqynlr, backcolor_sel=self.TNOcIyTOCMk))
        if BYRkmWItkVfAhY:
            start = self.nFWrGJyGHsBV + self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
            JBCDJoHYm = start + config.CTVG.C44.value * 60
            geikSRpcvam = int(time())
            HZGuJ = wjbJWVX.x
            cuqrajueXZKc = wjbJWVX.y
            aKKfuZofF = wjbJWVX.w
            vjrDstcJDPjBp = wjbJWVX.h
            DETbuLCmYOZmO = None
            fFTRtgONfTj = RT_HALIGN_LEFT | RT_VALIGN_CENTER
            aqMyQqoOBKe = '   '
            if self.LiyMOiyqP > 39:
                if config.CTVG.C56.value:
                    fFTRtgONfTj = RT_HALIGN_CENTER | RT_VALIGN_CENTER | RT_WRAP
                    aqMyQqoOBKe = ''
                else:
                    fFTRtgONfTj = RT_HALIGN_LEFT | RT_VALIGN_CENTER | RT_WRAP
                    aqMyQqoOBKe = ''
            for DETbuLCmYOZmO in BYRkmWItkVfAhY:
                KjUKrjjjHKPvzNX = DETbuLCmYOZmO[2]
                qxyEWz = DETbuLCmYOZmO[3]
                TvHugmr, dZCGYMlCxcfwfZw = self.tBcZsq(KjUKrjjjHKPvzNX, qxyEWz, start, JBCDJoHYm, aKKfuZofF)
                rLTFYjFLR = self.NSjWHcStKTLbU(UMUhLJhkv, KjUKrjjjHKPvzNX, qxyEWz, DETbuLCmYOZmO[0])
                if rLTFYjFLR:
                    KNlLJNdkd = self.evfEaAJRzeV
                    nhiuBQfwnDSU = self.fTWqsfSMXv
                    wRLNSjlzvO = self.jxPjMfQnNaY
                elif rLTFYjFLR == False:
                    KNlLJNdkd = self.hXbYdg
                    nhiuBQfwnDSU = self.hXbYdg
                    wRLNSjlzvO = self.WwJRUqDCvn
                elif not AduwKVqFCtWzeIh and KjUKrjjjHKPvzNX <= self.CxOZqdD and KjUKrjjjHKPvzNX + qxyEWz > geikSRpcvam:
                    KNlLJNdkd = self.qEsBEoz
                    nhiuBQfwnDSU = self.ooGJC
                    ikBbwgkgDDmiRFh = self.HaJKV
                    cHSGLu = self.tHCcYDmnTQeKqmJ
                    wRLNSjlzvO = self.LHONo
                elif CoolAlternative(UMUhLJhkv, self.WQqNiBbHzOJUrXt.toString()):
                    KNlLJNdkd = self.TNOcIyTOCMk
                    nhiuBQfwnDSU = self.ooGJC
                    wRLNSjlzvO = self.chwcCnQpTIfYn
                elif KjUKrjjjHKPvzNX <= geikSRpcvam and KjUKrjjjHKPvzNX + qxyEWz > geikSRpcvam:
                    ikBbwgkgDDmiRFh = self.LIvXVTXQFhMmAK
                    cHSGLu = self.tHCcYDmnTQeKqmJ
                    KNlLJNdkd = self.Gwzsvq
                    nhiuBQfwnDSU = self.cruOnhBsdnf
                    wRLNSjlzvO = self.wxtgrgtWV
                else:
                    KNlLJNdkd = self.sZFcJcEYedYG
                    nhiuBQfwnDSU = self.gLvHtGYJwDnaL
                    wRLNSjlzvO = self.JIZyhZO
                if config.CTVG.C29.value != 'No':
                    res.append(MultiContentEntryPixmapAlphaTest(pos=(HZGuJ + TvHugmr, cuqrajueXZKc), size=(dZCGYMlCxcfwfZw, vjrDstcJDPjBp), png=wRLNSjlzvO, backcolor=KNlLJNdkd, backcolor_sel=nhiuBQfwnDSU))
                    res.append(MultiContentEntryText(pos=(HZGuJ + TvHugmr, cuqrajueXZKc), size=(dZCGYMlCxcfwfZw, vjrDstcJDPjBp), font=HQFwXZnluWfdTw, flags=fFTRtgONfTj, text=aqMyQqoOBKe + DETbuLCmYOZmO[1], color=ikBbwgkgDDmiRFh, color_sel=cHSGLu, backcolor_sel=nhiuBQfwnDSU, border_width=2, border_color=self.NnoHj))
                else:
                    res.append(MultiContentEntryText(pos=(HZGuJ + TvHugmr, cuqrajueXZKc), size=(dZCGYMlCxcfwfZw, vjrDstcJDPjBp), font=HQFwXZnluWfdTw, flags=fFTRtgONfTj, text=aqMyQqoOBKe + DETbuLCmYOZmO[1], color=ikBbwgkgDDmiRFh, color_sel=cHSGLu, backcolor=KNlLJNdkd, backcolor_sel=nhiuBQfwnDSU, border_width=1, border_color=self.gciYoOUoElTq))

        return res

    def lZgfoSEPEk(self, oOJsdNcNtHUAYXv, nFWrGJyGHsBV, hXYPZeFsC, ev_start, ev_duration):
        TvHugmr, width = self.tBcZsq(ev_start, ev_duration, nFWrGJyGHsBV, nFWrGJyGHsBV + hXYPZeFsC * 60, oOJsdNcNtHUAYXv.width())
        return (TvHugmr + oOJsdNcNtHUAYXv.left(), width)

    def tBcZsq(self, KjUKrjjjHKPvzNX, qxyEWz, start, JBCDJoHYm, width):
        TvHugmr = (KjUKrjjjHKPvzNX - start) * width / (JBCDJoHYm - start)
        dZCGYMlCxcfwfZw = (KjUKrjjjHKPvzNX + qxyEWz - start) * width / (JBCDJoHYm - start) + 1
        dZCGYMlCxcfwfZw -= TvHugmr
        if TvHugmr < 0:
            dZCGYMlCxcfwfZw += TvHugmr
            TvHugmr = 0
        if TvHugmr + dZCGYMlCxcfwfZw > width:
            dZCGYMlCxcfwfZw = width - TvHugmr
        return (TvHugmr, dZCGYMlCxcfwfZw)

    def NSjWHcStKTLbU(self, fXYLLkn, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt):
        for x in self.QHYMHhwOVIXtLT.timer_list:
            if x.service_ref.ref.toString() == fXYLLkn:
                blmRapeotWYHCEX = pVdYFhAaXsyyci + qxyEWz
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                if self.CxOZqdD == 0 or self.CxOZqdD > JBCDJoHYm:
                    self.CxOZqdD = JBCDJoHYm
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                if x.eit == VQKNKnUpnwbt:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True
                elif pVdYFhAaXsyyci <= TteNjwT <= blmRapeotWYHCEX:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True

        for x in self.QHYMHhwOVIXtLT.processed_timers:
            if x.disabled and x.service_ref.ref.toString() == fXYLLkn:
                if x.eit == VQKNKnUpnwbt:
                    return False

    def CpPnffPspi(self, qDFTEDFxno, KjUKrjjjHKPvzNX = -1):
        if qDFTEDFxno is None:
            nFWrGJyGHsBV = self.nFWrGJyGHsBV + self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
            ZDxUJDDCPod = [ (UMUhLJhkv[0],
             0,
             nFWrGJyGHsBV,
             config.CTVG.C44.value) for UMUhLJhkv in self.ScnvMSTPY ]
        else:
            self.jbKPjQCEJlY = None
            self.FuFccNSayop = None
            self.nFWrGJyGHsBV = int(KjUKrjjjHKPvzNX)
            ZDxUJDDCPod = [ (UMUhLJhkv.ref.toString(),
             0,
             self.nFWrGJyGHsBV,
             config.CTVG.C44.value) for UMUhLJhkv in qDFTEDFxno ]
        if config.CTVG.C28.value:
            ZDxUJDDCPod.insert(0, 'XRnITBD')
        else:
            ZDxUJDDCPod.insert(0, 'XRNITBD')
        aUvhOhvQe = self.sdiQt(ZDxUJDDCPod)
        self.ScnvMSTPY = []
        NoLvBC = None
        UMUhLJhkv = ''
        fzxOJINWMUI = ''
        hSMItU = self.ScnvMSTPY.append
        for x in aUvhOhvQe:
            if UMUhLJhkv != x[0]:
                if NoLvBC is not None:
                    hSMItU((UMUhLJhkv, fzxOJINWMUI, NoLvBC[0][0] is not None and NoLvBC or None))
                UMUhLJhkv = x[0]
                fzxOJINWMUI = x[1]
                NoLvBC = []
            NoLvBC.append((x[2],
             x[3],
             x[4],
             x[5]))

        if NoLvBC and len(NoLvBC):
            hSMItU((UMUhLJhkv, fzxOJINWMUI, NoLvBC[0][0] is not None and NoLvBC or None))
        self.l.setList(self.ScnvMSTPY)
        self.amlGDzFUp()
        return

    def KmaTbJxFy(self):
        rc = self.oOJsdNcNtHUAYXv
        return PEwinOgXknkdV(rc.x + (self.instance and self.instance.position().x() or 0), rc.top(), rc.w, rc.h)

    def CuVTDmRDLwV(self):
        return self.nFWrGJyGHsBV + self.FoLaaHWDpTaD * config.CTVG.C44.value * 60

    def qLCLSDdrjPMTmn(self):
        return config.CTVG.C44.value

    def mCcXxUnnUdldCM(self, BidVA, JhKpFAp):
        NHozf = self.TPVxuSuwYBrUelM.info(BidVA)
        return NHozf and NHozf.isPlayable(BidVA, JhKpFAp) or False

    def postWidgetCreate(self, instance):
        instance.setWrapAround(True)
        instance.selectionChanged.get().append(self.fCqCYE)
        instance.setContent(self.l)
        self.l.setSelectionClip(eRect(0, 0, 0, 0), False)
        self.GweXP()
        self.DUlXmSYVDDV()
        self.dApqvKSTBEInbG()

    def preWidgetRemove(self, instance):
        instance.selectionChanged.get().remove(self.fCqCYE)
        instance.setContent(None)
        return

    def sdiQt(self, list, MlBIgDzxYSu = None):
        if self.DTzDLYhRge is not None:
            if MlBIgDzxYSu is not None:
                return self.DTzDLYhRge.lookupEvent(list, MlBIgDzxYSu)
            else:
                return self.DTzDLYhRge.lookupEvent(list)
        return []

    def rRtWCitddeQKbbF(self):
        width = self.l.getItemSize().width()
        NcBkuDj = self.l.getItemSize().height()
        TvHugmr = 0
        if self.LiyMOiyqP > 50:
            w = config.CTVG.C53.value
        elif self.LiyMOiyqP <= 50:
            w = config.CTVG.C54.value
        self.jkzfjQpVYQq = PEwinOgXknkdV(TvHugmr, 0, w, NcBkuDj)
        TvHugmr += w
        w = width - TvHugmr
        self.oOJsdNcNtHUAYXv = PEwinOgXknkdV(TvHugmr, 0, w, NcBkuDj)

    def vHcYMZDEssl(self):
        self.FoLaaHWDpTaD = 0

    def vRWagvtcPAWTrTv(self, dir, visible = True):
        FuFccNSayop = self.FuFccNSayop
        self.rRtWCitddeQKbbF()
        OOxLk = self.jbKPjQCEJlY is not None
        if FuFccNSayop:
            FTzVXMd = True
            PRTmQUczh = FuFccNSayop[2]
            if dir == 0:
                FTzVXMd = False
            elif dir == +1:
                if OOxLk and self.jbKPjQCEJlY + 1 < len(PRTmQUczh):
                    self.jbKPjQCEJlY += 1
                else:
                    self.FoLaaHWDpTaD += 1
                    self.CpPnffPspi(None)
                    return True
            elif dir == -1:
                if OOxLk and self.jbKPjQCEJlY - 1 >= 0:
                    self.jbKPjQCEJlY -= 1
                else:
                    self.FoLaaHWDpTaD -= 1
                    self.CpPnffPspi(None)
                    return True
            else:
                if dir == +2:
                    self.FoLaaHWDpTaD += 1
                    self.CpPnffPspi(None)
                    return True
                if dir == -2:
                    if self.FoLaaHWDpTaD > 0:
                        self.FoLaaHWDpTaD -= 1
                        self.CpPnffPspi(None)
                        return True
                else:
                    if dir == +3:
                        self.FoLaaHWDpTaD += 1440 / config.CTVG.C44.value
                        self.CpPnffPspi(None)
                        return True
                    if dir == -3:
                        self.FoLaaHWDpTaD -= 1440 / config.CTVG.C44.value
                        if self.FoLaaHWDpTaD < 0:
                            self.FoLaaHWDpTaD = 0
                        self.CpPnffPspi(None)
                        return True
                    if dir == +4:
                        DuLbDelWyenmKy = self.nFWrGJyGHsBV + self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
                        DuLbDelWyenmKy = datetime.fromtimestamp(DuLbDelWyenmKy)
                        sUGZXLFNdF = DuLbDelWyenmKy.replace(hour=config.CTVG.C30.value[0], minute=config.CTVG.C30.value[1])
                        if mktime(sUGZXLFNdF.timetuple()) <= mktime(DuLbDelWyenmKy.timetuple()):
                            sUGZXLFNdF += timedelta(days=1)
                        DuLbDelWyenmKy = int(mktime(DuLbDelWyenmKy.timetuple()))
                        sUGZXLFNdF = int(mktime(sUGZXLFNdF.timetuple()))
                        self.FoLaaHWDpTaD = self.FoLaaHWDpTaD + int((sUGZXLFNdF - DuLbDelWyenmKy) / config.CTVG.C44.value * 60)
                        self.nFWrGJyGHsBV = sUGZXLFNdF - self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
                        self.CpPnffPspi(None)
                        return True
                    if dir == -4:
                        DuLbDelWyenmKy = self.nFWrGJyGHsBV + self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
                        DuLbDelWyenmKy = datetime.fromtimestamp(DuLbDelWyenmKy)
                        sUGZXLFNdF = DuLbDelWyenmKy.replace(hour=config.CTVG.C30.value[0], minute=config.CTVG.C30.value[1])
                        if mktime(sUGZXLFNdF.timetuple()) <= mktime(DuLbDelWyenmKy.timetuple()):
                            sUGZXLFNdF -= timedelta(days=1)
                        DuLbDelWyenmKy = int(mktime(DuLbDelWyenmKy.timetuple()))
                        sUGZXLFNdF = int(mktime(sUGZXLFNdF.timetuple()))
                        self.FoLaaHWDpTaD = self.FoLaaHWDpTaD + int((sUGZXLFNdF - DuLbDelWyenmKy) / config.CTVG.C44.value * 60)
                        self.nFWrGJyGHsBV = sUGZXLFNdF - self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
                        self.CpPnffPspi(None)
                        return True
        if FuFccNSayop and OOxLk:
            WFVjWbKbX = PRTmQUczh[self.jbKPjQCEJlY]
            nFWrGJyGHsBV = self.nFWrGJyGHsBV + self.FoLaaHWDpTaD * config.CTVG.C44.value * 60
            TvHugmr, width = self.lZgfoSEPEk(self.oOJsdNcNtHUAYXv, nFWrGJyGHsBV, config.CTVG.C44.value, WFVjWbKbX[2], WFVjWbKbX[3])
            self.drPxPp = PEwinOgXknkdV(TvHugmr, 0, width, self.oOJsdNcNtHUAYXv.height)
            print("TvHugmr:", TvHugmr)
            print("width:", width)            
            print("self.oOJsdNcNtHUAYXv.h:", self.oOJsdNcNtHUAYXv.h)            
            self.l.setSelectionClip(eRect(int(TvHugmr), 0, int(width), int(self.oOJsdNcNtHUAYXv.h)), visible and FTzVXMd)
        else:
            self.drPxPp = self.oOJsdNcNtHUAYXv
            self.l.setSelectionClip(eRect(self.oOJsdNcNtHUAYXv.x, self.oOJsdNcNtHUAYXv.y, self.oOJsdNcNtHUAYXv.w, self.oOJsdNcNtHUAYXv.h), False)
        self.selectionChanged()
        return False

    def eHXbbUpQo(self):
        YNlAVseZWsWRxB = localtime()
        if config.CTVG.C40.value == 1 or config.CTVG.C40.value == 3:
            self.LiyMOiyqP = config.CTVG.C50.value
            self.l.setItemHeight(config.CTVG.C50.value)
            if config.CTVG.C29.value == 'Standard':
                PBoDyKZBdm = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/Cool3D/Standard/'
            elif config.CTVG.C29.value == 'SkinDesign':
                HaqcC = config.skin.primary_skin.value
                HaqcC = HaqcC[:HaqcC.rfind('/')]
                PBoDyKZBdm = '/usr/share/enigma2/' + HaqcC + '/SkinDesign/'
            else:
                PBoDyKZBdm = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/Cool3D/MyDesign/'
            if (YNlAVseZWsWRxB.tm_year, YNlAVseZWsWRxB.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2]) + 1):
                PBoDyKZBdm = 'usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/MyDesign/'
            self.jxPjMfQnNaY = loadPNG(PBoDyKZBdm + 'CoolRec.png')
            self.WwJRUqDCvn = loadPNG(PBoDyKZBdm + 'CoolPreRec.png')
            self.LHONo = loadPNG(PBoDyKZBdm + 'CoolFreeTuner.png')
            self.chwcCnQpTIfYn = loadPNG(PBoDyKZBdm + 'CoolSelect.png')
            self.wxtgrgtWV = loadPNG(PBoDyKZBdm + 'CoolNow.png')
            self.JIZyhZO = loadPNG(PBoDyKZBdm + 'CoolBack.png')
            self.BEylY = loadPNG(PBoDyKZBdm + 'CoolPicon.png')
            self.SmgEugboREz = loadPNG(PBoDyKZBdm + 'CoolPiconSelect.png')
            self.wuqkSpGyxrM.setPara((config.CTVG.C49.value / 0.6,
             config.CTVG.C49.value,
             1,
             1,
             1,
             1,
             '#ff000000'))
        else:
            self.LiyMOiyqP = config.CTVG.C52.value
            self.l.setItemHeight(config.CTVG.C52.value)
            if config.CTVG.C29.value == 'Standard':
                PBoDyKZBdm = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/Cool3D/Standard/'
            elif config.CTVG.C29.value == 'SkinDesign':
                HaqcC = config.skin.primary_skin.value
                HaqcC = HaqcC[:HaqcC.rfind('/')]
                PBoDyKZBdm = '/usr/share/enigma2/' + HaqcC + '/SkinDesign/'
            else:
                PBoDyKZBdm = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/Cool3D/MyDesign/'
            if (YNlAVseZWsWRxB.tm_year, YNlAVseZWsWRxB.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2]) + 2):
                PBoDyKZBdm = 'usr/lib/enigma2/python/Plugin/Extensions/CoolTVGuide/MyDesign/'
            self.jxPjMfQnNaY = loadPNG(PBoDyKZBdm + 'CoolRecS.png')
            self.WwJRUqDCvn = loadPNG(PBoDyKZBdm + 'CoolPreRecS.png')
            self.LHONo = loadPNG(PBoDyKZBdm + 'CoolFreeTunerS.png')
            self.chwcCnQpTIfYn = loadPNG(PBoDyKZBdm + 'CoolSelectS.png')
            self.wxtgrgtWV = loadPNG(PBoDyKZBdm + 'CoolNowS.png')
            self.JIZyhZO = loadPNG(PBoDyKZBdm + 'CoolBackS.png')
            self.BEylY = loadPNG(PBoDyKZBdm + 'CoolPiconS.png')
            self.SmgEugboREz = loadPNG(PBoDyKZBdm + 'CoolPiconSelectS.png')
            self.wuqkSpGyxrM.setPara((config.CTVG.C51.value / 0.6,
             config.CTVG.C51.value,
             1,
             1,
             1,
             1,
             '#ff000000'))

    def GweXP(self):
        self.l.setFont(0, gFont('Regular', config.CTVG.C47.value))

    def DUlXmSYVDDV(self):
        self.l.setFont(1, gFont('Regular', config.CTVG.C45.value))

    def dApqvKSTBEInbG(self):
        self.l.setFont(2, gFont('Regular', config.CTVG.C46.value))


class znjhVZLcrBZZBbq(Screen):

    def __init__(self, session, qDFTEDFxno, VsbLMxaqGuOhxRV = None, pXBQLmHRRZdwrD = '', PwRojNX = None):
        Screen.__init__(self, session)
        if TMvKPeMEZHVqV == 720:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_720.xml'
            elif PwRojNX == iXZeUPZjXi:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_720.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_720.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_720.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_720.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_720.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_720.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_720.xml'
        elif TMvKPeMEZHVqV == 1024:
            if PwRojNX == PQMOk:
                self.skinName = 'CoolInfoGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1024.xml'
            elif PwRojNX == iXZeUPZjXi:
                if config.CTVG.C43.value == 1:
                    self.skinName = 'CoolSingleGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1024.xml'
                elif config.CTVG.C43.value == 2:
                    self.skinName = 'CoolSingleGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1024.xml'
                elif config.CTVG.C43.value == 3:
                    self.skinName = 'CoolSingleGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1024.xml'
            elif PwRojNX == IUqwdjkcjCMKCFO:
                if config.CTVG.C42.value == 1:
                    self.skinName = 'CoolEasyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1024.xml'
                elif config.CTVG.C42.value == 2:
                    self.skinName = 'CoolEasyGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1024.xml'
                elif config.CTVG.C42.value == 3:
                    self.skinName = 'CoolEasyGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1024.xml'
            elif PwRojNX == QQdKtJPxMxJPjwB:
                if config.CTVG.C41.value == 1:
                    self.skinName = 'CoolChannelGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1024.xml'
                elif config.CTVG.C41.value == 2:
                    self.skinName = 'CoolChannelGuide2'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1024.xml'
                elif config.CTVG.C41.value == 3:
                    self.skinName = 'CoolChannelGuide3'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1024.xml'
            elif PwRojNX == eseWoWLtSYyCHGT:
                if config.CTVG.C40.value == 1:
                    self.skinName = 'CoolTVGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1024.xml'
                elif config.CTVG.C40.value == 2:
                    self.skinName = 'CoolTinyGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1024.xml'
                elif config.CTVG.C40.value == 3:
                    self.skinName = 'CoolMultiGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1024.xml'
                elif config.CTVG.C40.value == 4:
                    self.skinName = 'CoolNiceGuide'
                    WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1024.xml'
        elif PwRojNX == PQMOk:
            self.skinName = 'CoolInfoGuide'
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolInfoGuide_1280.xml'
        elif PwRojNX == iXZeUPZjXi:
            if config.CTVG.C43.value == 1:
                self.skinName = 'CoolSingleGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide_1280.xml'
            elif config.CTVG.C43.value == 2:
                self.skinName = 'CoolSingleGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide2_1280.xml'
            elif config.CTVG.C43.value == 3:
                self.skinName = 'CoolSingleGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSingleGuide3_1280.xml'
        elif PwRojNX == IUqwdjkcjCMKCFO:
            if config.CTVG.C42.value == 1:
                self.skinName = 'CoolEasyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide_1280.xml'
            elif config.CTVG.C42.value == 2:
                self.skinName = 'CoolEasyGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide2_1280.xml'
            elif config.CTVG.C42.value == 3:
                self.skinName = 'CoolEasyGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolEasyGuide3_1280.xml'
        elif PwRojNX == QQdKtJPxMxJPjwB:
            if config.CTVG.C41.value == 1:
                self.skinName = 'CoolChannelGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide_1280.xml'
            elif config.CTVG.C41.value == 2:
                self.skinName = 'CoolChannelGuide2'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide2_1280.xml'
            elif config.CTVG.C41.value == 3:
                self.skinName = 'CoolChannelGuide3'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolChannelGuide3_1280.xml'
        elif PwRojNX == eseWoWLtSYyCHGT:
            if config.CTVG.C40.value == 1:
                self.skinName = 'CoolTVGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuide_1280.xml'
            elif config.CTVG.C40.value == 2:
                self.skinName = 'CoolTinyGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTinyGuide_1280.xml'
            elif config.CTVG.C40.value == 3:
                self.skinName = 'CoolMultiGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolMultiGuide_1280.xml'
            elif config.CTVG.C40.value == 4:
                self.skinName = 'CoolNiceGuide'
                WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolNiceGuide_1280.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self.SkAEFj = zUIfAWMBbQJ
        self.VsbLMxaqGuOhxRV = VsbLMxaqGuOhxRV
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        geikSRpcvam = time()
        tmp = geikSRpcvam % 900
        self.vzDGDGAQLSCa = geikSRpcvam - tmp
        self.FUiTqUurDFxy = False
        self['key_red'] = Button('')
        self['key_green'] = Button('')
        self['key_yellow'] = Button('')
        self['key_blue'] = Button('')
        self['Event'] = Event()
        self['Service'] = ServiceEvent()
        self['timeline_text'] = FaghDMgGyKw()
        self.CECNivdg = []
        for x in (0, 1, 2, 3, 4, 5):
            pm = Pixmap()
            self.CECNivdg.append(pm)
            self['timeline%d' % x] = pm

        self['timeline_now'] = Pixmap()
        self.aJwoNNFX = qDFTEDFxno
        if pXBQLmHRRZdwrD != '':
            Screen.setTitle(self, pXBQLmHRRZdwrD)
        self['list'] = rHAPXA(pOHOrwCihqC=self.WlFKMlyFxSWrG, QHYMHhwOVIXtLT=self.session.nav.RecordTimer, hXYPZeFsC=config.CTVG.C44.value, QflrzkxuriKKT=config.CTVG.C55.value)
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolMenu': self.NuGwC,
         'CoolTime': self.sEJWW,
         'CoolRed': self.GwhJbNuquP,
         'CoolRedLong': self.fbUws,
         'CoolGreen': self.gXppchsrp,
         'CoolGreenLong': self.mzzBQRAohy,
         'CoolYellow': self.bKpKe,
         'CoolYellowLong': self.qOlhOHWiFHpIC,
         'CoolBlue': self.qsDCwRsYOveEFy,
         'CoolBlueLong': self.uHqjdBJMLj,
         'CoolOK': self.WhRkmBFDyxfV,
         'CoolOKLong': self.KZcQOfIkWdrLZ,
         'CoolInfo': self.NxrXAek,
         'CoolInfoLong': self.uWIjFbGhtX,
         'CoolRecord': self.esPNG,
         'CoolVIDEO': nePylQgKlghpaVP,
         'CoolAUDIO': self.BvRoHaxNcu,
         'CoolPlay': self.SdyqepEBz,
         'CoolFastForward': self.yWzeVUbGITWl,
         'CoolRewind': self.dhcOSzjaVppCX,
         'CoolKeyTV': self.EekrcnjXd,
         'CoolPower': self.EUtMyA,
         'CoolCancel': self.JtAiZhAVofB,
         'CoolHelp': self.dtDeUpd,
         'CoolChannelUP': self.sKhaCbfBhi,
         'CoolChannelDown': self.TxbypgantrvRK,
         'CoolPREVIOUS': self.mwzQSZchaT,
         'CoolNEXT': self.nCinWmnbh,
         'CoolLEFT': self.yVJwwCVivfoqv,
         'CoolRIGHT': self.NlpqdNN,
         '1': self.BXgEprgWswxGUwu,
         '2': self.dyKNDy,
         '3': self.OwPMoV,
         '4': self.ORMaFFgAUurQpB,
         '5': self.cDAaj,
         '6': self.FvOdCbFqhvscV,
         '7': self.TdjjCghHcsK,
         '8': self.neDLkklkP,
         '9': self.eKXjhOLrwzFbS,
         '0': self.TUsVGfSeubMP}, -1)
        self['key_red'].setText(_(config.CTVG.C12.value))
        self['key_green'].setText(_(config.CTVG.C14.value))
        self['key_yellow'].setText(_(config.CTVG.C16.value))
        self['key_blue'].setText(_(config.CTVG.C18.value))
        self.reliRDOz = eTimer()
        self.reliRDOz.callback.append(self.OtuVwk)
        self.reliRDOz.start(60000)
        self.onLayoutFinish.append(self.NbmZQLxewbo)
        self.SkDkTpkG = None
        self['date'] = Button()
        self.feetaXGmSVk()
        self.onShow.append(self.hplyGU)
        self.qvZsfOLaorS = eTimer()
        self.qvZsfOLaorS.callback.append(self.GKkaWZYIWKJliO)
        self.session.nav.RecordTimer.on_state_change.append(self.OQekEHTyEAMogUz)
        self.session.nav.record_event.append(self.rTNBfpRbTsgf)
        self.BubscGANC = ServiceEventTracker(screen=self, eventmap={iPlayableService.evStart: self.eznYurXbAoT,
         iPlayableService.evStopped: self.eznYurXbAoT})
        return

    def eznYurXbAoT(self):
        if hasattr(self, 'shown'):
            if self.shown:
                if self.qvZsfOLaorS.isActive():
                    self.qvZsfOLaorS.stop()
                self.qvZsfOLaorS.start(3000, True)

    def rTNBfpRbTsgf(self, UMUhLJhkv, event):
        self.eznYurXbAoT()

    def hplyGU(self):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        if self.SkDkTpkG:
            self.SkDkTpkG = None
            self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
        self['list'].l.invalidate()
        return

    def OQekEHTyEAMogUz(self, WFVjWbKbX):
        self.eznYurXbAoT()

    def qFDSvr(self):
        global WmXVqUV
        if WmXVqUV == 1:
            x = config.CTVG.C77.value
        elif WmXVqUV == 2:
            x = config.CTVG.C78.value
        elif WmXVqUV == 3:
            x = config.CTVG.C79.value
        elif WmXVqUV == 4:
            if WvYVaQ != self.SkAEFj and SAQsYCIeDb != self.SkAEFj:
                WmXVqUV = 1
                return self.close(False)
            x = config.CTVG.C80.value
        elif WmXVqUV == 5:
            x = config.CTVG.C81.value
        elif WmXVqUV == 6:
            x = config.CTVG.C82.value
        elif WmXVqUV == 7:
            x = config.CTVG.C83.value
        elif WmXVqUV == 8:
            x = config.CTVG.C84.value
        elif WmXVqUV == 9:
            x = config.CTVG.C85.value
        elif WmXVqUV == 10:
            x = config.CTVG.C86.value
        elif WmXVqUV == 11:
            x = config.CTVG.C87.value
        elif WmXVqUV == 12:
            x = config.CTVG.C88.value
        if x == '9':
            WmXVqUV += 1
            return self.eKXjhOLrwzFbS()
        self.hide()
        if x == '1':
            self.WVwFshleYbnIc()
        elif x == '2':
            self.RDSJwxPYCfBLVaN()
        elif x == '3':
            CEGmain(self.session)
        elif x == '4':
            CCGmain(self.session)
        elif x == '5':
            config.CTVG.C40.value = 1
            zehTthMch = TrruhKvKi.getRoot()
            JCExyHUtZugOf(zehTthMch)
        elif x == '6':
            config.CTVG.C40.value = 2
            zehTthMch = TrruhKvKi.getRoot()
            JCExyHUtZugOf(zehTthMch)
        elif x == '7':
            config.CTVG.C40.value = 3
            zehTthMch = TrruhKvKi.getRoot()
            JCExyHUtZugOf(zehTthMch)
        elif x == '8':
            config.CTVG.C40.value = 4
            zehTthMch = TrruhKvKi.getRoot()
            JCExyHUtZugOf(zehTthMch)
        elif x == '10':
            self.sSPMBhwDflASCMt()
        elif x == '11':
            WmXVqUV = 0
            self.session.open(TimerEditList)
        else:
            WmXVqUV = 0
        WmXVqUV += 1
        self.close(False)

    def feetaXGmSVk(self):
        geikSRpcvam = localtime()
        if (geikSRpcvam.tm_year, geikSRpcvam.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2])):
            self.wuuFONWejkP()

    def wuuFONWejkP(self):
        self.DAUoW()

    def changeServiceCB(self, SqpegV, epg):
        if self.serviceSel:
            if SqpegV > 0:
                self.serviceSel.nextService()
            else:
                self.serviceSel.prevService()
            epg.setService(self.serviceSel.currentService())

    def GKkaWZYIWKJliO(self):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        self['list'].l.invalidate()

    def fxVcQUikA(self):
        UFXUK = []
        if fspOMNbuwFCWk:
            UFXUK.append((_('SeriesPlugin'), 'SeriesPlugin'))
        if sLpxMYXhjCROl:
            UFXUK.append((_('The TVDB Info'), 'The TVDB Info'))
        if bPdxaOceY:
            UFXUK.append((_('IMDb Search'), 'IMDbSearch'))
        if WizweESn:
            UFXUK.append((_('TMDB Info'), 'TMDBInfo'))
        if HikvfLr:
            UFXUK.append((_('OFDb Details'), 'OFDbDetails'))
        if UFXUK == []:
            UFXUK.append((_('No Info Plugins installed...'), 'No Info Plugins installed...'))
        self.session.openWithCallback(self.tmxBeAld, ChoiceBox, title=_('   CoolInfoBox'), list=UFXUK)

    def tmxBeAld(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        SNAVqJygcUu = self['list'].JvSwzXgDeSH()
        ERoOCCVi = SNAVqJygcUu[0]
        if not ERoOCCVi:
            return
        dNZCbIlhYcesiab = ERoOCCVi and ERoOCCVi.getEventName() or ''
        if nKGKSPXPp == 'SeriesPlugin':
            from Plugins.Extensions.SeriesPlugin.SeriesPluginInfoScreen import SeriesPluginInfoScreen
            UMUhLJhkv = SNAVqJygcUu[1]
            self.session.open(SeriesPluginInfoScreen, UMUhLJhkv, ERoOCCVi)
        if nKGKSPXPp == 'The TVDB Info':
            from Plugins.Extensions.TheTVDB.plugin import TheTVDBMain
            self.session.open(TheTVDBMain, dNZCbIlhYcesiab)
        if nKGKSPXPp == 'IMDbSearch':
            from Plugins.Extensions.IMDb.plugin import IMDB
            self.session.open(IMDB, dNZCbIlhYcesiab)
        if nKGKSPXPp == 'TMDBInfo':
            from Plugins.Extensions.TMDb.plugin import TMDbMain
            self.session.open(TMDbMain, dNZCbIlhYcesiab)
        if nKGKSPXPp == 'OFDbDetails':
            from Plugins.Extensions.OFDb.plugin import OFDB
            self.session.open(OFDB, dNZCbIlhYcesiab)

    def voLEWybvGX(self):
        OXeXRlHHxgjsyrP = self['list'].JvSwzXgDeSH()
        if not OXeXRlHHxgjsyrP:
            return
        try:
            from Plugins.Extensions.AutoTimer.AutoTimerEditor import addAutotimerFromEvent
            self.session.openWithCallback(self.aqFgBg, ChoiceBox, title=_('   check Autotimer ?'), list=[(_('Yes'), 'Yes'), (_('No'), 'No')])
            addAutotimerFromEvent(self.session, OXeXRlHHxgjsyrP[0], OXeXRlHHxgjsyrP[1])
        except:
            self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def aqFgBg(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        if nKGKSPXPp == 'Yes':
            try:
                from Plugins.Extensions.AutoTimer.plugin import main as AutoTimerSafe
                AutoTimerSafe(self.session)
            except:
                self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def SdyqepEBz(self):
        CuFXFBycHL(eFSzkTC)

    def EUtMyA(self):
        try:
            from Screens.SleepTimerEdit import SleepTimerEdit
            self.session.open(SleepTimerEdit)
        except:
            pass

    def esPNG(self):
        SthnRRhw = self['list'].JvSwzXgDeSH()
        sTgNxkmJlcmVCv = SthnRRhw[1]
        urXhHLMR = SthnRRhw[0]
        if not urXhHLMR:
            return
        else:
            FZxOvzpGBD = urXhHLMR.getEventId()
            fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                    self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
                    self['list'].l.invalidate()
                    break
            else:
                ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(urXhHLMR))
                BjDtxuaz = NavigationInstance.instance.RecordTimer.record(ZFcHE)
                if BjDtxuaz is not None:
                    for x in BjDtxuaz:
                        if x.setAutoincreaseEnd(ZFcHE):
                            self.session.nav.RecordTimer.timeChanged(x)

                    BjDtxuaz = self.session.nav.RecordTimer.record(ZFcHE)
                    if BjDtxuaz is not None:
                        self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, BjDtxuaz)
                else:
                    self.qvZsfOLaorS.start(3000, True)
                self['list'].l.invalidate()

            self.WlFKMlyFxSWrG()
            return

    def sSPMBhwDflASCMt(self):
        try:
            OiTUjyeSoZRNG = self['list'].JvSwzXgDeSH()
            zXaGlOHNBdRvpus = OiTUjyeSoZRNG[0]
            if not zXaGlOHNBdRvpus:
                return
            dNZCbIlhYcesiab = zXaGlOHNBdRvpus.getEventName() or ''
        except:
            dNZCbIlhYcesiab = ''

        self.session.open(lyqBhZ, dNZCbIlhYcesiab, False)

    def HohLg(self, ret = False):
        if config.CTVG.C60.value:
            zehTthMch = TrruhKvKi.getRoot()
            JCExyHUtZugOf(zehTthMch)
        self.serviceSel = None
        if config.CTVG.C61.value:
            self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
            self.FUiTqUurDFxy = True
            kMnpjZUheS = self['list'].JvSwzXgDeSH()[1]
            self['list'].WQqNiBbHzOJUrXt = kMnpjZUheS.ref
            self.nORxTbRjzsNVch()
        return

    def UZWrOVfpub(self, ret = False):
        self.serviceSel = None
        if config.CTVG.C61.value:
            self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
            self.FUiTqUurDFxy = True
            uxWjFesZKa = self['list'].JvSwzXgDeSH()[1]
            self['list'].WQqNiBbHzOJUrXt = uxWjFesZKa.ref
            self.nORxTbRjzsNVch()
        return

    def WVwFshleYbnIc(self):
        config.CTVG.C61.value = False
        tfonHdIjfgQ = self['list'].JvSwzXgDeSH()
        if not tfonHdIjfgQ:
            return
        tlvldyLLXXHo = eServiceReference(str(tfonHdIjfgQ[1]))
        if tlvldyLLXXHo:
            self.serviceSel = SimpleServicelist(self.aJwoNNFX)
            if self.serviceSel.selectService(tlvldyLLXXHo):
                self.session.openWithCallback(self.UZWrOVfpub, zDKhcfAp, tfonHdIjfgQ[0], tfonHdIjfgQ[1], tlvldyLLXXHo, TrruhKvKi, self.QEcLxYKv, nfZQJKwSrVA=self.changeServiceCB, PwRojNX=PQMOk)

    def dtDeUpd(self):
        self.session.open(HelpScreen)

    def BvRoHaxNcu(self):
        config.CTVG.C60.value = False
        self.SkDkTpkG = True
        CEGmain(self.session)

    def RDSJwxPYCfBLVaN(self):
        config.CTVG.C61.value = False
        config.CTVG.C60.value = False
        bJKvGIVemCb = self['list'].JvSwzXgDeSH()
        refstr = bJKvGIVemCb[1].ref
        if refstr:
            self.serviceSel = SimpleServicelist(self.aJwoNNFX)
            if self.serviceSel.selectService(refstr):
                self.session.openWithCallback(self.HohLg, XEArkQXQCQRMEL, refstr, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=iXZeUPZjXi)

    def pdPYUFkqsstQg(self):
        if config.CTVG.C40.value == 1:
            config.CTVG.C40.value = 2
        elif config.CTVG.C40.value == 2:
            config.CTVG.C40.value = 3
        elif config.CTVG.C40.value == 3:
            config.CTVG.C40.value = 4
        else:
            config.CTVG.C40.value = 1
        config.CTVG.save()
        self.hide()
        zehTthMch = TrruhKvKi.getRoot()
        JCExyHUtZugOf(zehTthMch)
        self.JdgznJarWJ()

    def NlpqdNN(self):
        self.lGyolBBYWm(+1)

    def yVJwwCVivfoqv(self):
        self.lGyolBBYWm(-1)

    def nCinWmnbh(self):
        self.lGyolBBYWm(+3)

    def mwzQSZchaT(self):
        self.lGyolBBYWm(-3)

    def lGyolBBYWm(self, dir, visible = True):
        ret = self['list'].vRWagvtcPAWTrTv(dir, visible)
        if ret:
            self.OtuVwk(True)

    def TUsVGfSeubMP(self):
        self['list'].instance.moveSelectionTo(0)
        geikSRpcvam = time()
        tmp = geikSRpcvam % 900
        qLEik = geikSRpcvam - tmp
        self['list'].vHcYMZDEssl()
        self['list'].CpPnffPspi(self.aJwoNNFX, qLEik)
        self.OtuVwk(True)

    def BXgEprgWswxGUwu(self):
        qBaqvCLi = config.CTVG.C44.value
        if qBaqvCLi > 60:
            qBaqvCLi = qBaqvCLi - 60
            config.CTVG.C44.value = qBaqvCLi
            self.OtuVwk()
            self['list'].CpPnffPspi(None)
        return

    def dyKNDy(self):
        self['list'].instance.moveSelection(self['list'].instance.pageUp)

    def OwPMoV(self):
        qBaqvCLi = config.CTVG.C44.value
        if qBaqvCLi < 300:
            qBaqvCLi = qBaqvCLi + 60
            config.CTVG.C44.value = qBaqvCLi
            self.OtuVwk()
            self['list'].CpPnffPspi(None)
        return

    def ORMaFFgAUurQpB(self):
        self.lGyolBBYWm(-2)

    def cDAaj(self):
        self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
        geikSRpcvam = time()
        Dovjge = geikSRpcvam % 900
        qLEik = geikSRpcvam - Dovjge
        self['list'].vHcYMZDEssl()
        self['list'].CpPnffPspi(self.aJwoNNFX, qLEik)
        self.OtuVwk(True)

    def FvOdCbFqhvscV(self):
        self.lGyolBBYWm(+2)

    def TdjjCghHcsK(self):
        self.pdPYUFkqsstQg()

    def neDLkklkP(self):
        self['list'].instance.moveSelection(self['list'].instance.pageDown)

    def eKXjhOLrwzFbS(self):
        self.lGyolBBYWm(+4)

    def GwhJbNuquP(self):
        EcLNwIhunJbRsLQ = config.CTVG.C12.value
        if EcLNwIhunJbRsLQ == 'EPG Select':
            self.qFDSvr()
        elif EcLNwIhunJbRsLQ == 'Zap':
            self.nORxTbRjzsNVch()
        elif EcLNwIhunJbRsLQ == 'Zap + Exit':
            self.JIQKwPOcc()
        elif EcLNwIhunJbRsLQ == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif EcLNwIhunJbRsLQ == 'CoolInfoBox':
            self.fxVcQUikA()
        elif EcLNwIhunJbRsLQ == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif EcLNwIhunJbRsLQ == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif EcLNwIhunJbRsLQ == 'Timer':
            self.EmOZX()
        elif EcLNwIhunJbRsLQ == 'QuickRec':
            self.esPNG()
        elif EcLNwIhunJbRsLQ == 'AutoTimer':
            self.voLEWybvGX()
        elif EcLNwIhunJbRsLQ == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif EcLNwIhunJbRsLQ == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif EcLNwIhunJbRsLQ == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif EcLNwIhunJbRsLQ == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.qFDSvr()

    def fbUws(self):
        aFfcKSkBDKNWm = config.CTVG.C13.value
        if aFfcKSkBDKNWm == 'Zap':
            self.nORxTbRjzsNVch()
        elif aFfcKSkBDKNWm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif aFfcKSkBDKNWm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif aFfcKSkBDKNWm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif aFfcKSkBDKNWm == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif aFfcKSkBDKNWm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif aFfcKSkBDKNWm == 'Timer':
            self.EmOZX()
        elif aFfcKSkBDKNWm == 'QuickRec':
            self.esPNG()
        elif aFfcKSkBDKNWm == 'AutoTimer':
            self.voLEWybvGX()
        elif aFfcKSkBDKNWm == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif aFfcKSkBDKNWm == 'EPG Select':
            self.qFDSvr()
        elif aFfcKSkBDKNWm == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif aFfcKSkBDKNWm == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif aFfcKSkBDKNWm == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.JIQKwPOcc()

    def gXppchsrp(self):
        fCsivhkbczcm = config.CTVG.C14.value
        if fCsivhkbczcm == 'Zap':
            self.nORxTbRjzsNVch()
        elif fCsivhkbczcm == 'Zap + Exit':
            self.JIQKwPOcc()
        elif fCsivhkbczcm == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif fCsivhkbczcm == 'CoolInfoBox':
            self.fxVcQUikA()
        elif fCsivhkbczcm == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif fCsivhkbczcm == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif fCsivhkbczcm == 'Timer':
            self.EmOZX()
        elif fCsivhkbczcm == 'QuickRec':
            self.esPNG()
        elif fCsivhkbczcm == 'AutoTimer':
            self.voLEWybvGX()
        elif fCsivhkbczcm == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif fCsivhkbczcm == 'EPG Select':
            self.qFDSvr()
        elif fCsivhkbczcm == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif fCsivhkbczcm == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif fCsivhkbczcm == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.EmOZX()

    def mzzBQRAohy(self):
        CALICbGXK = config.CTVG.C15.value
        if CALICbGXK == 'Zap':
            self.nORxTbRjzsNVch()
        elif CALICbGXK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif CALICbGXK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif CALICbGXK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif CALICbGXK == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif CALICbGXK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif CALICbGXK == 'Timer':
            self.EmOZX()
        elif CALICbGXK == 'QuickRec':
            self.esPNG()
        elif CALICbGXK == 'AutoTimer':
            self.voLEWybvGX()
        elif CALICbGXK == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif CALICbGXK == 'EPG Select':
            self.qFDSvr()
        elif CALICbGXK == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif CALICbGXK == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif CALICbGXK == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.voLEWybvGX()

    def bKpKe(self):
        BCGuXefsvjf = config.CTVG.C16.value
        if BCGuXefsvjf == 'Zap':
            self.nORxTbRjzsNVch()
        elif BCGuXefsvjf == 'Zap + Exit':
            self.JIQKwPOcc()
        elif BCGuXefsvjf == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif BCGuXefsvjf == 'CoolInfoBox':
            self.fxVcQUikA()
        elif BCGuXefsvjf == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif BCGuXefsvjf == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif BCGuXefsvjf == 'Timer':
            self.EmOZX()
        elif BCGuXefsvjf == 'QuickRec':
            self.esPNG()
        elif BCGuXefsvjf == 'AutoTimer':
            self.voLEWybvGX()
        elif BCGuXefsvjf == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif BCGuXefsvjf == 'EPG Select':
            self.qFDSvr()
        elif BCGuXefsvjf == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif BCGuXefsvjf == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif BCGuXefsvjf == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.pdPYUFkqsstQg()

    def qOlhOHWiFHpIC(self):
        gRpGhRQrF = config.CTVG.C17.value
        if gRpGhRQrF == 'Zap':
            self.nORxTbRjzsNVch()
        elif gRpGhRQrF == 'Zap + Exit':
            self.JIQKwPOcc()
        elif gRpGhRQrF == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif gRpGhRQrF == 'CoolInfoBox':
            self.fxVcQUikA()
        elif gRpGhRQrF == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif gRpGhRQrF == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif gRpGhRQrF == 'Timer':
            self.EmOZX()
        elif gRpGhRQrF == 'QuickRec':
            self.esPNG()
        elif gRpGhRQrF == 'AutoTimer':
            self.voLEWybvGX()
        elif gRpGhRQrF == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif gRpGhRQrF == 'EPG Select':
            self.qFDSvr()
        elif gRpGhRQrF == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif gRpGhRQrF == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif gRpGhRQrF == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.SdyqepEBz()

    def qsDCwRsYOveEFy(self):
        LnElTGKJP = config.CTVG.C18.value
        if LnElTGKJP == 'Zap':
            self.nORxTbRjzsNVch()
        elif LnElTGKJP == 'Zap + Exit':
            self.JIQKwPOcc()
        elif LnElTGKJP == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif LnElTGKJP == 'CoolInfoBox':
            self.fxVcQUikA()
        elif LnElTGKJP == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif LnElTGKJP == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif LnElTGKJP == 'Timer':
            self.EmOZX()
        elif LnElTGKJP == 'QuickRec':
            self.esPNG()
        elif LnElTGKJP == 'AutoTimer':
            self.voLEWybvGX()
        elif LnElTGKJP == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif LnElTGKJP == 'EPG Select':
            self.qFDSvr()
        elif LnElTGKJP == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif LnElTGKJP == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif LnElTGKJP == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.sSPMBhwDflASCMt()

    def uHqjdBJMLj(self):
        UQcfkjKQK = config.CTVG.C19.value
        if UQcfkjKQK == 'Zap':
            self.nORxTbRjzsNVch()
        elif UQcfkjKQK == 'Zap + Exit':
            self.JIQKwPOcc()
        elif UQcfkjKQK == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif UQcfkjKQK == 'CoolInfoBox':
            self.fxVcQUikA()
        elif UQcfkjKQK == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif UQcfkjKQK == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif UQcfkjKQK == 'Timer':
            self.EmOZX()
        elif UQcfkjKQK == 'QuickRec':
            self.esPNG()
        elif UQcfkjKQK == 'AutoTimer':
            self.voLEWybvGX()
        elif UQcfkjKQK == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif UQcfkjKQK == 'EPG Select':
            self.qFDSvr()
        elif UQcfkjKQK == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif UQcfkjKQK == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif UQcfkjKQK == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.fxVcQUikA()

    def WhRkmBFDyxfV(self):
        SlBvlWSPMURgObC = config.CTVG.C20.value
        if SlBvlWSPMURgObC == 'Zap':
            self.nORxTbRjzsNVch()
        elif SlBvlWSPMURgObC == 'Zap + Exit':
            self.JIQKwPOcc()
        elif SlBvlWSPMURgObC == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif SlBvlWSPMURgObC == 'CoolInfoBox':
            self.fxVcQUikA()
        elif SlBvlWSPMURgObC == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif SlBvlWSPMURgObC == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif SlBvlWSPMURgObC == 'Timer':
            self.EmOZX()
        elif SlBvlWSPMURgObC == 'QuickRec':
            self.esPNG()
        elif SlBvlWSPMURgObC == 'AutoTimer':
            self.voLEWybvGX()
        elif SlBvlWSPMURgObC == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif SlBvlWSPMURgObC == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif SlBvlWSPMURgObC == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif SlBvlWSPMURgObC == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            self.WVwFshleYbnIc()

    def KZcQOfIkWdrLZ(self):
        OCCKSDwCPbq = config.CTVG.C21.value
        if OCCKSDwCPbq == 'Zap':
            self.nORxTbRjzsNVch()
        elif OCCKSDwCPbq == 'Zap + Exit':
            self.JIQKwPOcc()
        elif OCCKSDwCPbq == 'CoolSearch':
            self.sSPMBhwDflASCMt()
        elif OCCKSDwCPbq == 'CoolInfoBox':
            self.fxVcQUikA()
        elif OCCKSDwCPbq == 'GuideSwitch':
            self.pdPYUFkqsstQg()
        elif OCCKSDwCPbq == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif OCCKSDwCPbq == 'Timer':
            self.EmOZX()
        elif OCCKSDwCPbq == 'QuickRec':
            self.esPNG()
        elif OCCKSDwCPbq == 'AutoTimer':
            self.voLEWybvGX()
        elif OCCKSDwCPbq == 'PrimeTime':
            self.eKXjhOLrwzFbS()
        elif OCCKSDwCPbq == 'Bouquet +':
            self.yWzeVUbGITWl()
        elif OCCKSDwCPbq == 'Bouquet -':
            self.dhcOSzjaVppCX()
        elif OCCKSDwCPbq == 'Bouquetlist':
            self.SdyqepEBz()
        else:
            return

    def NxrXAek(self):
        LkGwiX = config.CTVG.C22.value
        if LkGwiX == '4':
            self.qFDSvr()
        elif LkGwiX == '1':
            self.WVwFshleYbnIc()
        elif LkGwiX == '2':
            self.RDSJwxPYCfBLVaN()
        elif LkGwiX == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def uWIjFbGhtX(self):
        BkucHGwMEzEJ = config.CTVG.C23.value
        if BkucHGwMEzEJ == '4':
            self.qFDSvr()
        elif BkucHGwMEzEJ == '1':
            self.WVwFshleYbnIc()
        elif BkucHGwMEzEJ == '2':
            self.RDSJwxPYCfBLVaN()
        elif BkucHGwMEzEJ == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def sKhaCbfBhi(self):
        ggbnteHcIoOIsnD = config.CTVG.C24.value
        if ggbnteHcIoOIsnD == '1':
            self.yWzeVUbGITWl()
        elif ggbnteHcIoOIsnD == '2':
            self.dhcOSzjaVppCX()
        elif ggbnteHcIoOIsnD == '3':
            self.dyKNDy()
        elif ggbnteHcIoOIsnD == '4':
            self.neDLkklkP()
        else:
            self.yWzeVUbGITWl()

    def TxbypgantrvRK(self):
        tStsGut = config.CTVG.C25.value
        if tStsGut == '1':
            self.yWzeVUbGITWl()
        elif tStsGut == '2':
            self.dhcOSzjaVppCX()
        elif tStsGut == '3':
            self.dyKNDy()
        elif tStsGut == '4':
            self.neDLkklkP()
        else:
            self.dhcOSzjaVppCX()

    def yWzeVUbGITWl(self):
        geikSRpcvam = self['list'].CuVTDmRDLwV()
        Dovjge = geikSRpcvam % 900
        if self.VsbLMxaqGuOhxRV:
            self['list'].instance.moveSelectionTo(0)
            self.VsbLMxaqGuOhxRV(1, self)
            pXBQLmHRRZdwrD = ServiceReference(FufElMDyUtWr).getServiceName()
            if pXBQLmHRRZdwrD != '':
                Screen.setTitle(self, pXBQLmHRRZdwrD)
        qLEik = geikSRpcvam - Dovjge
        self['list'].vHcYMZDEssl()
        self['list'].CpPnffPspi(self.aJwoNNFX, qLEik)
        self.OtuVwk(True)

    def dhcOSzjaVppCX(self):
        geikSRpcvam = self['list'].CuVTDmRDLwV()
        Dovjge = geikSRpcvam % 900
        if self.VsbLMxaqGuOhxRV:
            self['list'].instance.moveSelectionTo(0)
            self.VsbLMxaqGuOhxRV(-1, self)
            pXBQLmHRRZdwrD = ServiceReference(FufElMDyUtWr).getServiceName()
            if pXBQLmHRRZdwrD != '':
                Screen.setTitle(self, pXBQLmHRRZdwrD)
        qLEik = geikSRpcvam - Dovjge
        self['list'].vHcYMZDEssl()
        self['list'].CpPnffPspi(self.aJwoNNFX, qLEik)
        self.OtuVwk(True)

    def sEJWW(self):
        self.session.openWithCallback(self.ylOPBdIWtSFX, TimeDateInput, config.CTVG.C27)

    def ylOPBdIWtSFX(self, ret):
        if len(ret) > 1:
            if ret[0]:
                self.vzDGDGAQLSCa = ret[1]
                l = self['list']
                l.vHcYMZDEssl()
                l.CpPnffPspi(self.aJwoNNFX, ret[1])
                self.OtuVwk(True)

    def NuGwC(self):
        self.session.openWithCallback(self.wImiGCFpPSqZ, oifusNtsQLjEI)

    def wImiGCFpPSqZ(self):
        self.hide()
        main(self.session, TrruhKvKi)
        if WvYVaQ != self.SkAEFj and SAQsYCIeDb != self.SkAEFj:
            self.session.open(MessageBox, Po, MessageBox.TYPE_INFO)
        self.DAUoW()

    def JtAiZhAVofB(self):
        global WmXVqUV
        WmXVqUV = 1
        self.DTzDLYhRge = eEPGCache.getInstance()
        self.hide()
        AjzDUzKgoLe = set()
        geikSRpcvam = time()
        gwVLVamNAqnDMo = False
        if config.CTVG.C62.value:
            for x in self.session.nav.RecordTimer.timer_list:
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                try:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventId(x.service_ref.ref, x.eit)
                except:
                    ERoOCCVi = self.DTzDLYhRge.lookupEventTime(x.service_ref.ref, TteNjwT)

                if ERoOCCVi:
                    IcZCToaVeOwI = ERoOCCVi.getBeginTime()
                    CsrfWgDZI = IcZCToaVeOwI + ERoOCCVi.getDuration()
                    if IcZCToaVeOwI < cpUukOBh or CsrfWgDZI > JBCDJoHYm:
                        if ERoOCCVi.getDuration() > 300 and cpUukOBh > geikSRpcvam:
                            AjzDUzKgoLe.add(x)

        if config.CTVG.C63.value:
            for x in self.session.nav.RecordTimer.processed_timers:
                if geikSRpcvam < x.end:
                    AjzDUzKgoLe.add(x)

        dXRTDwpUpKROauu = _('\n          !! Cool Timer Alarm !! \n\n')
        for x in AjzDUzKgoLe:
            gwVLVamNAqnDMo = str(x.name)
            dplqPMZr = str(strftime('%d.%m.%Y - %H:%M', localtime(x.begin)))
            BhkuqkbF = str(x.service_ref.getServiceName())
            TuqtF = _('is disabled') if x.disabled else _('has moved')
            dXRTDwpUpKROauu += dplqPMZr + ' - ' + BhkuqkbF + '\n' + gwVLVamNAqnDMo + ' ' + TuqtF + '\n\n'

        dXRTDwpUpKROauu += _('-- please check your Timer --')
        if gwVLVamNAqnDMo:
            self.session.open(MessageBox, dXRTDwpUpKROauu, MessageBox.TYPE_ERROR)
        self.JdgznJarWJ()

    def qFLoYuYRPQFdK(self, qDFTEDFxno):
        self.aJwoNNFX = qDFTEDFxno
        self.NbmZQLxewbo()

    def OtuVwk(self, fXFBEeGnzKqti = False):
        self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
        self.reliRDOz.start((60 - int(time()) % 60) * 1000)
        oOJsdNcNtHUAYXv = self['list'].KmaTbJxFy()
        hXYPZeFsC = self['list'].qLCLSDdrjPMTmn()
        nFWrGJyGHsBV = self['list'].CuVTDmRDLwV()
        if oOJsdNcNtHUAYXv is None or hXYPZeFsC is None or nFWrGJyGHsBV is None:
            self.reliRDOz.start(500)
        EdruqOGBTaHHZh = hXYPZeFsC > 180 and 60 or 30
        oMfZN = hXYPZeFsC / EdruqOGBTaHHZh
        yPRGkKLAnmAoobs = oOJsdNcNtHUAYXv.width() / oMfZN
        pos = oOJsdNcNtHUAYXv.left()
        RsOXjifRHJMNON = []
        x = 0
        zuwFdPsBIgsKYj = 0
        for line in self.CECNivdg:
            SLAvs = line.position
            ybWueAlhiCirG = (x == oMfZN and oOJsdNcNtHUAYXv.left() + oOJsdNcNtHUAYXv.width() or pos, SLAvs[1])
            if not x or x >= oMfZN:
                line.visible = False
            else:
                if SLAvs != ybWueAlhiCirG:
                    line.setPosition(ybWueAlhiCirG[0], ybWueAlhiCirG[1])
                    zuwFdPsBIgsKYj += 1
                line.visible = True
            if not x or line.visible:
                RsOXjifRHJMNON.append((nFWrGJyGHsBV + x * EdruqOGBTaHHZh * 60, ybWueAlhiCirG[0]))
            x += 1
            pos += yPRGkKLAnmAoobs

        if zuwFdPsBIgsKYj or fXFBEeGnzKqti:
            self['timeline_text'].vyiRYEzcvWSVxm(RsOXjifRHJMNON)
        geikSRpcvam = time()
        QHPmsOvdXFkPS = self['timeline_now']
        if geikSRpcvam >= nFWrGJyGHsBV and geikSRpcvam < nFWrGJyGHsBV + hXYPZeFsC * 60:
            TvHugmr = int((geikSRpcvam - nFWrGJyGHsBV) * oOJsdNcNtHUAYXv.width() / (hXYPZeFsC * 60) - QHPmsOvdXFkPS.instance.size().width() / 2)
            SLAvs = QHPmsOvdXFkPS.position
            ybWueAlhiCirG = (TvHugmr + oOJsdNcNtHUAYXv.left(), SLAvs[1])
            if SLAvs != ybWueAlhiCirG:
                QHPmsOvdXFkPS.setPosition(ybWueAlhiCirG[0], ybWueAlhiCirG[1])
            QHPmsOvdXFkPS.visible = True
        else:
            QHPmsOvdXFkPS.visible = False
        self['list'].l.invalidate()
        return

    def NbmZQLxewbo(self):
        self['list'].CpPnffPspi(self.aJwoNNFX, self.vzDGDGAQLSCa)
        self['list'].UrfFYoRsn(self.session.nav.getCurrentlyPlayingServiceReference())
        self.OtuVwk()
        if config.CTVG.C39.value:
            self['list'].instance.moveSelectionTo(0)

    def QEcLxYKv(self, QoGRewjlErZRq, setService, val):
        BDuSW = self['list'].JvSwzXgDeSH()
        self.lGyolBBYWm(val, False)
        zjRLCa = self['list'].JvSwzXgDeSH()
        if zjRLCa[0] is None and zjRLCa[1].ref != BDuSW[1].ref:
            self.QEcLxYKv(QoGRewjlErZRq, setService, val)
        else:
            setService(zjRLCa[1])
            QoGRewjlErZRq(zjRLCa[0])
        return

    def EekrcnjXd(self):
        eFSzkTC.open(TimerEditList)

    def EmOZX(self):
        fzPWRjmyFOdPgK = self['list'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        sTgNxkmJlcmVCv = fzPWRjmyFOdPgK[1]
        if not lWJAurf:
            return
        FZxOvzpGBD = lWJAurf.getEventId()
        fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
        for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
            if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
                self.session.openWithCallback(self.pwCaxqRZQsvS, ChoiceBox, title=_('Cool Timer Edit :' + '\n\n%s') % lWJAurf.getEventName(), list=[(_('edit this Timer ?'), 'edit'), (_('delete this Timer ?'), 'delete'), (_('delete this Timer and recording ?'), 'delrec')])
                break
        else:
            ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(lWJAurf))
            self.session.openWithCallback(self.SohIHVvAMnbAXX, TimerEntry, ZFcHE)

    def pwCaxqRZQsvS(self, nKGKSPXPp):
        QHYMHhwOVIXtLT = self.QHYMHhwOVIXtLT
        pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp)

    def SohIHVvAMnbAXX(self, nKGKSPXPp):
        self.qvZsfOLaorS.start(3000, True)
        if nKGKSPXPp[0]:
            WFVjWbKbX = nKGKSPXPp[1]
            QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
            if QptgJyXzKf is not None:
                for x in QptgJyXzKf:
                    if x.setAutoincreaseEnd(WFVjWbKbX):
                        self.session.nav.RecordTimer.timeChanged(x)

                QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
                if QptgJyXzKf is not None:
                    self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, QptgJyXzKf)
            if config.CTVG.C14.value == 'Timer':
                self['key_green'].setText(_('TimerEdit'))
            elif config.CTVG.C12.value == 'Timer':
                self['key_red'].setText(_('TimerEdit'))
            elif config.CTVG.C16.value == 'Timer':
                self['key_yellow'].setText(_('TimerEdit'))
            elif config.CTVG.C18.value == 'Timer':
                self['key_blue'].setText(_('TimerEdit'))
        return

    def AoKSzJQJax(self, nKGKSPXPp):
        self.SohIHVvAMnbAXX(nKGKSPXPp)

    def WlFKMlyFxSWrG(self):
        VbLvEpoznAcm = self['list'].JvSwzXgDeSH()
        SVbMq = VbLvEpoznAcm[0]
        self['Event'].newEvent(SVbMq)
        eqeAQDfNpE = self['list'].OGJPWJikcr()
        yyJciFsdx = ''
        geikSRpcvam = time()
        nFWrGJyGHsBV = self['list'].CuVTDmRDLwV()
        rbuTrfjskKNUrpX = localtime(geikSRpcvam)
        xCcvK = localtime(nFWrGJyGHsBV)
        if rbuTrfjskKNUrpX[2] != xCcvK[2]:
            yyJciFsdx = '%s  %d.%d.' % (self.PsMWO[xCcvK[6]], xCcvK[2], xCcvK[1])
        else:
            yyJciFsdx = '%s  %d.%d.' % (_('Today'), xCcvK[2], xCcvK[1])
        self['date'].setText(yyJciFsdx)
        if VbLvEpoznAcm[1] is None:
            self['Service'].newService(None)
        else:
            self['Service'].newService(VbLvEpoznAcm[1].ref)
        if not SVbMq:
            if config.CTVG.C14.value == 'Timer':
                self['key_green'].setText('')
            elif config.CTVG.C12.value == 'Timer':
                self['key_red'].setText('')
            elif config.CTVG.C16.value == 'Timer':
                self['key_yellow'].setText('')
            elif config.CTVG.C18.value == 'Timer':
                self['key_blue'].setText('')
            return
        else:
            sTgNxkmJlcmVCv = VbLvEpoznAcm[1]
            FZxOvzpGBD = SVbMq.getEventId()
            fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
            xCEOmOL = False
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                    xCEOmOL = True
                    break

            if xCEOmOL:
                if config.CTVG.C14.value == 'Timer':
                    self['key_green'].setText(_('TimerEdit'))
                elif config.CTVG.C12.value == 'Timer':
                    self['key_red'].setText(_('TimerEdit'))
                elif config.CTVG.C16.value == 'Timer':
                    self['key_yellow'].setText(_('TimerEdit'))
                elif config.CTVG.C18.value == 'Timer':
                    self['key_blue'].setText(_('TimerEdit'))
            elif config.CTVG.C14.value == 'Timer':
                self['key_green'].setText(_('Timer'))
            elif config.CTVG.C12.value == 'Timer':
                self['key_red'].setText(_('Timer'))
            elif config.CTVG.C16.value == 'Timer':
                self['key_yellow'].setText(_('Timer'))
            elif config.CTVG.C18.value == 'Timer':
                self['key_blue'].setText(_('Timer'))
            return

    def JdgznJarWJ(self):
        self.FUiTqUurDFxy = True
        iqUxDClWfpeziO = self['list'].JvSwzXgDeSH()[1]
        if iqUxDClWfpeziO:
            self.DAUoW()

    def DAUoW(self):
        self.close(self.FUiTqUurDFxy)

    def nORxTbRjzsNVch(self):
        self.FUiTqUurDFxy = True
        MkrSeAFlTK = self['list'].JvSwzXgDeSH()[1]
        if MkrSeAFlTK:
            FllUJdlN(MkrSeAFlTK.ref)
            self['list'].WQqNiBbHzOJUrXt = self.session.nav.getCurrentlyPlayingServiceReference()
            self['list'].CpPnffPspi(None)
        return

    def JIQKwPOcc(self):
        self.FUiTqUurDFxy = True
        cnZAOIp = self['list'].JvSwzXgDeSH()[1]
        if cnZAOIp:
            FllUJdlN(cnZAOIp.ref)
            self.DAUoW()


class oifusNtsQLjEI(Screen, ConfigListScreen):

    def __init__(self, session, args = None):
        Screen.__init__(self, session)
        self.mpFcUvKAMTaOJu = _('Cool TV Guide Settings')
        self.skinName = 'CoolTVGuideSetup'
        WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolTVGuideSetup.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolOK': self.nyBARTNYMIw,
         'CoolCancel': self.nyBARTNYMIw,
         'CoolRed': self.JfZVrwPWucjHC,
         'CoolGreen': self.tLoSobVSVtV,
         'CoolYellow': self.ZBWMByr,
         'CoolBlue': self.xavAvrbE,
         'CoolHelp': self.dtDeUpd,
         'CoolMenu': self.QqPozjx}, -1)
        self['key_red'] = Button(_('Save'))
        self['key_green'] = Button(_('Cool'))
        self['key_yellow'] = Button(_('TV'))
        self['key_blue'] = Button(_('Guide'))
        self['CoolText1'] = Button(_('Standard for (HD), (XD), (SD) Skin'))
        self['CoolText2'] = Button(_('Press ( < OK > ) to change your Buttons !!!'))
        self.zZICFPLqsjsShOq = []
        self.ARWFznDovLER = zUIfAWMBbQJ
        self.session = session
        self.ScnvMSTPY = []
        ConfigListScreen.__init__(self, self.ScnvMSTPY, session=self.session)
        self.xavAvrbE()

    def QyBHBXvdT(self, res):
        if res is not None:
            if res[-1:] == '/':
                res = res[:-1]
            if res[0] != '/':
                res = '/'
            self.ScnvMSTPY[self['config'].getCurrentIndex()][1].value = res
        return

    def nyBARTNYMIw(self):
        self.close()

    def QqPozjx(self):
        try:
            self.ScnvMSTPY[self['config'].getCurrentIndex()][3]()
        except:
            pass

    def JfZVrwPWucjHC(self):
        config.CTVG.save()
        self.close()

    def dtDeUpd(self):
        self.session.open(HelpScreen)

    def tLoSobVSVtV(self):
        self.tLoSobVSVtV = []
        self.tLoSobVSVtV.append(getConfigListEntry(_('Red Button (EPG Select)'), config.CTVG.C12))
        self.tLoSobVSVtV.append(getConfigListEntry(_('LongRed Button (ZAP+Exit)'), config.CTVG.C13))
        self.tLoSobVSVtV.append(getConfigListEntry(_('Green Button (Timer)'), config.CTVG.C14))
        self.tLoSobVSVtV.append(getConfigListEntry(_('LongGreen Button (Autotimer)'), config.CTVG.C15))
        self.tLoSobVSVtV.append(getConfigListEntry(_('Yellow Button (GuideSwitch)'), config.CTVG.C16))
        self.tLoSobVSVtV.append(getConfigListEntry(_('LongYellow Button (Bouquetlist)'), config.CTVG.C17))
        self.tLoSobVSVtV.append(getConfigListEntry(_('Blue Button (CoolSearch)'), config.CTVG.C18))
        self.tLoSobVSVtV.append(getConfigListEntry(_('LongBlue Button (CoolInfoBox)'), config.CTVG.C19))
        self.tLoSobVSVtV.append(getConfigListEntry(_('OK Button (Zap)'), config.CTVG.C20))
        self.tLoSobVSVtV.append(getConfigListEntry(_('LongOK Button'), config.CTVG.C21))
        self.tLoSobVSVtV.append(getConfigListEntry(_('Info Button (Cool Info Guide)'), config.CTVG.C22))
        self.tLoSobVSVtV.append(getConfigListEntry(_('LongInfo Button'), config.CTVG.C23))
        self.tLoSobVSVtV.append(getConfigListEntry(_('Channel + (Bouquet +)'), config.CTVG.C24))
        self.tLoSobVSVtV.append(getConfigListEntry(_('Channel - (Bouquet -)'), config.CTVG.C25))
        self['config'].list = self.tLoSobVSVtV
        self['config'].l.setList(self.tLoSobVSVtV)

    def ZBWMByr(self):
        self.ZBWMByr = []
        self.ZBWMByr.append(getConfigListEntry(_('Cool PrimeTime (20:15)'), config.CTVG.C30))
        self.ZBWMByr.append(getConfigListEntry(_('Cool TimerAlarm check if Timer has changed'), config.CTVG.C62))
        self.ZBWMByr.append(getConfigListEntry(_('Cool TimerAlarm check if Timer is deaktivated'), config.CTVG.C63))
        self.ZBWMByr.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ZBWMByr.append(getConfigListEntry(_('Start Cool TV Guide with Red Button'), config.CTVG.C31))
        self.ZBWMByr.append(getConfigListEntry(_('Start Cool Single Guide with Green Button'), config.CTVG.C32))
        self.ZBWMByr.append(getConfigListEntry(_('Start Cool Easy Guide with Yellow Button'), config.CTVG.C33))
        self.ZBWMByr.append(getConfigListEntry(_('Start Cool Info Guide with Info/EPG Button'), config.CTVG.C34))
        self.ZBWMByr.append(getConfigListEntry(_('Start Cool Channel Guide with Down Button'), config.CTVG.C35))
        self.ZBWMByr.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ZBWMByr.append(getConfigListEntry(_('Event 60 Fontsize (18), (15), (15)'), config.CTVG.C45))
        self.ZBWMByr.append(getConfigListEntry(_('Event 30 Fontsize (18), (15), (15)'), config.CTVG.C46))
        self.ZBWMByr.append(getConfigListEntry(_('Left Fontsize (22), (18), (16) (need restart)'), config.CTVG.C47))
        self.ZBWMByr.append(getConfigListEntry(_('Timeline Fontsize (20), (18), (16) (need restart)'), config.CTVG.C48))
        self.ZBWMByr.append(getConfigListEntry(_('Right 60 Font Center (Yes)'), config.CTVG.C56))
        self.ZBWMByr.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ZBWMByr.append(getConfigListEntry(_('Time Scale (180)'), config.CTVG.C44))
        self.ZBWMByr.append(getConfigListEntry(_('Bouquet at Start (No)'), config.CTVG.C36))
        self.ZBWMByr.append(getConfigListEntry(_('Channel 1 at Start (No)'), config.CTVG.C39))
        self.ZBWMByr.append(getConfigListEntry(_('Skip Empty Services (No) (need restart)'), config.CTVG.C55))
        self.ZBWMByr.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ZBWMByr.append(getConfigListEntry(_('Cool Easy Guide show Channel Number'), config.CTVG.C58))
        self.ZBWMByr.append(getConfigListEntry(_('Cool Easy Guide use Yellow/Blue for Time -/+'), config.CTVG.C57))
        self.ZBWMByr.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self['config'].list = self.ZBWMByr
        self['config'].l.setList(self.ZBWMByr)

    def xavAvrbE(self):
        self.ScnvMSTPY = []
        if WvYVaQ != self.ARWFznDovLER and SAQsYCIeDb != self.ARWFznDovLER:
            FTSBdQfuZz = int(os.popen(gGjXQFlY('CoolTVGUIDE', BfYlRdlfgAhcUyy)).read()[int(IUqwdjkcjCMKCFO[7]):].replace(':', ''), int(QQdKtJPxMxJPjwB[9:11]) + int(QQdKtJPxMxJPjwB[2:4])) * (int(XLeWzHuVActw[3:5]) - int(XLeWzHuVActw[8:10])) + int(PQMOk + iXZeUPZjXi)
            self.ScnvMSTPY.append(getConfigListEntry(_('Cool TV Guide ID ' + str(FTSBdQfuZz) + '              Cool TV Guide Key '), config.CTVG.Key))
            config.CTVG.save()
        else:
            self.ScnvMSTPY.append(getConfigListEntry(_('Cool TV Guide ' + fPVrFQoMzxdFJY), config.CTVG.C26))
            self.ScnvMSTPY.append(getConfigListEntry(_('----------'), config.CTVG.C26))
            self.ScnvMSTPY.append(getConfigListEntry(_('1 EPG Select (Cool Info Guide)'), config.CTVG.C77))
            self.ScnvMSTPY.append(getConfigListEntry(_('2 EPG Select (Cool Single Guide)'), config.CTVG.C78))
            self.ScnvMSTPY.append(getConfigListEntry(_('3 EPG Select (Cool Easy Guide)'), config.CTVG.C79))
            self.ScnvMSTPY.append(getConfigListEntry(_('4 EPG Select ()'), config.CTVG.C80))
            self.ScnvMSTPY.append(getConfigListEntry(_('5 EPG Select ()'), config.CTVG.C81))
            self.ScnvMSTPY.append(getConfigListEntry(_('6 EPG Select ()'), config.CTVG.C82))
            self.ScnvMSTPY.append(getConfigListEntry(_('7 EPG Select ()'), config.CTVG.C83))
            self.ScnvMSTPY.append(getConfigListEntry(_('8 EPG Select ()'), config.CTVG.C84))
            self.ScnvMSTPY.append(getConfigListEntry(_('9 EPG Select ()'), config.CTVG.C85))
            self.ScnvMSTPY.append(getConfigListEntry(_('10 EPG Select ()'), config.CTVG.C86))
            self.ScnvMSTPY.append(getConfigListEntry(_('11 EPG Select ()'), config.CTVG.C87))
            self.ScnvMSTPY.append(getConfigListEntry(_('12 EPG Select ()'), config.CTVG.C88))
            self.ScnvMSTPY.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ScnvMSTPY.append(getConfigListEntry(_('Cool 3D'), config.CTVG.C29))
        self.ScnvMSTPY.append(getConfigListEntry(_('Special Character (UTF-8) Fix (No)'), config.CTVG.C11))
        self.ScnvMSTPY.append(getConfigListEntry(_('Short Service Name (No)'), config.CTVG.C28))
        self.ScnvMSTPY.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ScnvMSTPY.append(getConfigListEntry(_('Show Picon (Yes) (need restart)'), config.CTVG.C37))
        self.ScnvMSTPY.append(getConfigListEntry(_('Picon Height (60), (54), (54)'), config.CTVG.C49))
        self.ScnvMSTPY.append(getConfigListEntry(_('Picon Item Height (60), (54), (54)'), config.CTVG.C50))
        self.ScnvMSTPY.append(getConfigListEntry(_('Left Section Width (110), (75), (75)'), config.CTVG.C53))
        self.ScnvMSTPY.append(getConfigListEntry(_('----------'), config.CTVG.C26))
        self.ScnvMSTPY.append(getConfigListEntry(_('Show CoolPico (Yes) (need restart)'), config.CTVG.C38))
        self.ScnvMSTPY.append(getConfigListEntry(_('CoolPico Height (30), (27), (27)'), config.CTVG.C51))
        self.ScnvMSTPY.append(getConfigListEntry(_('CoolPico Item Height (30), (27), (27)'), config.CTVG.C52))
        self.ScnvMSTPY.append(getConfigListEntry(_('Left Section Width (190), (110), (110)'), config.CTVG.C54))
        self['config'].list = self.ScnvMSTPY
        self['config'].l.setList(self.ScnvMSTPY)


class HelpScreen(Screen):
    qaJjUNPTVe = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/Cool3D/help.jpg'
    if TMvKPeMEZHVqV == 720:
        WgQTyCqDMVdNMj = '\n\t\t\t<screen flags="wfNoBorder" position="0,0" size="720,576" title="..Help.." backgroundColor=\'#ffffffff\'>\n\t\t\t\t<widget name="Picture" position="0,0" size="720,576" zPosition="1"/>\n\t\t\t</screen>'
    elif TMvKPeMEZHVqV == 1024:
        WgQTyCqDMVdNMj = '\n\t\t\t<screen flags="wfNoBorder" position="0,0" size="1024,576" title="..Help.." backgroundColor=\'#ffffffff\'>\n\t\t\t\t<widget name="Picture" position="0,0" size="1024,576" zPosition="1"/>\n\t\t\t</screen>'
    else:
        WgQTyCqDMVdNMj = '\n\t\t\t<screen flags="wfNoBorder" position="0,0" size="1280,720" title="..Help.." backgroundColor=\'#ffffffff\'>\n\t\t\t\t<widget name="Picture" position="0,0" size="1280,720" zPosition="1"/>\n\t\t\t</screen>'

    def __init__(self, session):
        self.skin = HelpScreen.WgQTyCqDMVdNMj
        Screen.__init__(self, session)
        self.isGnipRTdlrhrH = ePicLoad()
        self['Picture'] = Pixmap()
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolOK': self.close,
         'CoolCancel': self.close,
         'CoolRed': self.close,
         'CoolGreen': self.close}, -1)
        self['key_red'] = Button(_('Cancel'))
        self['key_green'] = Button(_('Save'))
        self.isGnipRTdlrhrH.PictureData.get().append(self.cATalym)
        self.onLayoutFinish.append(self.zxopCrJItxw)

    def cATalym(self, yJxuXkP = ' '):
        if self.qaJjUNPTVe is not None:
            ptr = self.isGnipRTdlrhrH.getData()
            self['Picture'].instance.setPixmap(ptr)
        return

    def zxopCrJItxw(self):
        if self.qaJjUNPTVe is not None:
            self.isGnipRTdlrhrH.setPara([self['Picture'].instance.size().width(),
             self['Picture'].instance.size().height(),
             1,
             1,
             False,
             1,
             '#121214'])
            self.isGnipRTdlrhrH.startDecode(self.qaJjUNPTVe)
        return


class wPwKYfbYpKpNbBT(Screen):
    WgQTyCqDMVdNMj = '<screen name="CTVGB" position="center,center" size="400,400" title="Choose bouquet">\n              <widget name="menu" position="25,25" size="350,350" scrollbarMode="showOnDemand" />\n          </screen>'

    def __init__(self, session, XQiSkUFpb, uPuZAZCeq, JsvfEKlOnNEpEQX = False):
        from Components.MenuList import MenuList
        Screen.__init__(self, session)
        self.skin = wPwKYfbYpKpNbBT.WgQTyCqDMVdNMj
        self.skinName = 'BouquetSelector'
        self.uPuZAZCeq = uPuZAZCeq
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolOK': self.CMXPgVlKTQ,
         'CoolCancel': self.lPLCBjb}, -1)
        CBFNzgDWob = [ (x[0], x[1]) for x in XQiSkUFpb ]
        self['menu'] = MenuList(CBFNzgDWob, JsvfEKlOnNEpEQX)

    def lPLCBjb(self):
        self.close(False)

    def getCurrent(self):
        cur = self['menu'].getCurrent()
        return cur and cur[1]

    def up(self):
        self['menu'].up()

    def down(self):
        self['menu'].down()

    def CMXPgVlKTQ(self):
        self.hide()
        self.uPuZAZCeq(self.getCurrent())
        self.close(True)


class pHQdnxNnMi():

    def __init__(self, XQiSkUFpb, JsvfEKlOnNEpEQX = False, LQcplWSWs = 0):
        self.XQiSkUFpb = [ b[1] for b in XQiSkUFpb ]
        self.pos = LQcplWSWs
        self.eqeAQDfNpE = len(XQiSkUFpb)
        self.JsvfEKlOnNEpEQX = JsvfEKlOnNEpEQX

    def getCurrent(self):
        return self.XQiSkUFpb[self.pos]

    def up(self):
        if self.pos > 0 or self.JsvfEKlOnNEpEQX:
            self.pos = (self.pos - 1) % self.eqeAQDfNpE

    def down(self):
        if self.pos < self.eqeAQDfNpE - 1 or self.JsvfEKlOnNEpEQX:
            self.pos = (self.pos + 1) % self.eqeAQDfNpE


class rPPVHYsAJVv(VirtualKeyBoard, NumericalTextInput):

    def __init__(self, session, **kwargs):
        VirtualKeyBoard.__init__(self, session, **kwargs)
        self.skinName = 'VirtualKeyBoard'
        try:
            print(self.sms_txt)
        except:
            NumericalTextInput.__init__(self, nextFunc=self.nextFunc)
            self['NumberActions'] = NumberActionMap(['NumberActions'], {'1': self.ClOoBIfowSu,
             '2': self.ClOoBIfowSu,
             '3': self.ClOoBIfowSu,
             '4': self.ClOoBIfowSu,
             '5': self.ClOoBIfowSu,
             '6': self.ClOoBIfowSu,
             '7': self.ClOoBIfowSu,
             '8': self.ClOoBIfowSu,
             '9': self.ClOoBIfowSu,
             '0': self.ClOoBIfowSu})
            self.zcxXJeHCtUWvjet = False

    def ClOoBIfowSu(self, number):
        MnZFwsYTPNoOZP = self.getKey(number)
        if not self.zcxXJeHCtUWvjet:
            self.CmmLR = self['text'].getText()
            self.zcxXJeHCtUWvjet = True
            self['text'].setMarkedPos(len(self.CmmLR))
        self['text'].setText(self.CmmLR + MnZFwsYTPNoOZP.encode('utf-8', 'ignore'))

    def nextFunc(self):
        self.CmmLR = self['text'].getText()
        self.zcxXJeHCtUWvjet = False
        self['text'].setMarkedPos(-1)


class zlrcRXjIYOUnyoy(lxNLnyst):

    def __init__(self, pOHOrwCihqC = None, QHYMHhwOVIXtLT = None):
        lxNLnyst.__init__(self, pOHOrwCihqC, QHYMHhwOVIXtLT)
        self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self.jvTmTJHlfxPIP = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.myzqmNzI = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.HQvLEHVqmBsVgHk = parseFont('Regular;22', ((1, 1), (1, 1)))
        self.l.setFont(0, self.jvTmTJHlfxPIP)
        self.l.setFont(1, self.myzqmNzI)
        self.l.setFont(2, self.HQvLEHVqmBsVgHk)
        self.l.setBuildFunc(self.tNjLxdPws)
        self.DZOLaKQYXqw = 0
        self.HEFcVeCmfjDPNdq = 2
        self.FIrFKOOPfdRJnb = 50
        self.VnmwSXzd = 70
        self.oTwHuYB = 2
        self.zmTOunm = 70
        self.CwbbgtPbYdAJaNS = 500
        self.icJJVKHwold = 2
        self.oVoKs = 700
        self.mMQSGwZt = 230
        self.BwBxpeGsFk = 2
        self.DrEcqGyi = 280
        self.HkPIn = 150
        self.RVaddhJ = 2
        self.vDtXdSWMj = 70
        self.sZFcJcEYedYG = None
        self.ZlvGlXNkLDSSOLB = None
        self.SMtkYND = 16737792
        self.WFivLbUm = 16777215
        self.Wzjij = 16777215
        self.eYKVAYQZkZCaAod = None
        self.kUdFNIT = None
        self.ZWXRUOATTV = 10425107
        self.hXbYdg = 11902465
        self.BPTUvuBjQ = 16737792
        self.tyoaImn = 3905737
        self.WubpaSVNw = 16777215
        return

    def applySkin(self, desktop, parent):
        dyYxANT = []
        if self.skinAttributes is not None:
            for Obqlh, value in self.skinAttributes:
                if Obqlh == 'CoolFont':
                    self.jvTmTJHlfxPIP = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(0, self.jvTmTJHlfxPIP)
                elif Obqlh == 'CoolServiceFont':
                    self.myzqmNzI = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(1, self.myzqmNzI)
                elif Obqlh == 'CoolEventFont':
                    self.HQvLEHVqmBsVgHk = parseFont(value, ((1, 1), (1, 1)))
                    self.l.setFont(2, self.HQvLEHVqmBsVgHk)
                elif Obqlh == 'CoolDayPos':
                    self.DZOLaKQYXqw = int(value)
                elif Obqlh == 'CoolDayHPos':
                    self.HEFcVeCmfjDPNdq = int(value)
                elif Obqlh == 'CoolDatePos':
                    self.VnmwSXzd = int(value)
                elif Obqlh == 'CoolDateHPos':
                    self.oTwHuYB = int(value)
                elif Obqlh == 'CoolTimePos':
                    self.HkPIn = int(value)
                elif Obqlh == 'CoolTimeHPos':
                    self.RVaddhJ = int(value)
                elif Obqlh == 'CoolServicePos':
                    self.mMQSGwZt = int(value)
                elif Obqlh == 'CoolServiceHPos':
                    self.BwBxpeGsFk = int(value)
                elif Obqlh == 'CoolEventPos':
                    self.CwbbgtPbYdAJaNS = int(value)
                elif Obqlh == 'CoolEventHPos':
                    self.icJJVKHwold = int(value)
                elif Obqlh == 'CoolDaySize':
                    self.FIrFKOOPfdRJnb = int(value)
                elif Obqlh == 'CoolDateSize':
                    self.zmTOunm = int(value)
                elif Obqlh == 'CoolTimeSize':
                    self.vDtXdSWMj = int(value)
                elif Obqlh == 'CoolServiceSize':
                    self.DrEcqGyi = int(value)
                elif Obqlh == 'CoolEventSize':
                    self.oVoKs = int(value)
                elif Obqlh == 'CoolDayColor':
                    self.SMtkYND = parseColor(value).argb()
                elif Obqlh == 'CoolDateColor':
                    self.WFivLbUm = parseColor(value).argb()
                elif Obqlh == 'CoolTimeColor':
                    self.tyoaImn = parseColor(value).argb()
                elif Obqlh == 'CoolServiceColor':
                    self.BPTUvuBjQ = parseColor(value).argb()
                elif Obqlh == 'CoolEventColor':
                    self.Wzjij = parseColor(value).argb()
                elif Obqlh == 'CoolBackColor':
                    self.sZFcJcEYedYG = parseColor(value).argb()
                elif Obqlh == 'CoolBackColorSel':
                    self.ZlvGlXNkLDSSOLB = parseColor(value).argb()
                elif Obqlh == 'CoolFontColSel':
                    self.WubpaSVNw = parseColor(value).argb()
                elif Obqlh == 'CoolEventBackColor':
                    self.eYKVAYQZkZCaAod = parseColor(value).argb()
                elif Obqlh == 'CoolRecEventBackColor':
                    self.kUdFNIT = parseColor(value).argb()
                elif Obqlh == 'CoolRecAlarmCol':
                    self.hXbYdg = parseColor(value).argb()
                elif Obqlh == 'CoolRecColor':
                    self.ZWXRUOATTV = parseColor(value).argb()
                else:
                    dyYxANT.append((Obqlh, value))

        self.skinAttributes = dyYxANT
        return GUIComponent.applySkin(self, desktop, parent)

    def NSjWHcStKTLbU(self, fXYLLkn, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt):
        for x in self.QHYMHhwOVIXtLT.timer_list:
            if x.service_ref.ref.toString() == fXYLLkn:
                blmRapeotWYHCEX = pVdYFhAaXsyyci + qxyEWz
                cpUukOBh = x.begin
                JBCDJoHYm = x.end
                TteNjwT = cpUukOBh + (JBCDJoHYm - cpUukOBh) / 4
                if x.eit == VQKNKnUpnwbt:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True
                elif pVdYFhAaXsyyci <= TteNjwT <= blmRapeotWYHCEX:
                    if pVdYFhAaXsyyci < cpUukOBh or blmRapeotWYHCEX > JBCDJoHYm:
                        return False
                    else:
                        return True

        for x in self.QHYMHhwOVIXtLT.processed_timers:
            if x.disabled and x.service_ref.ref.toString() == fXYLLkn:
                if x.eit == VQKNKnUpnwbt:
                    return False

    def tNjLxdPws(self, UMUhLJhkv, VQKNKnUpnwbt, pVdYFhAaXsyyci, qxyEWz, cIlYUZavCM):
        rLTFYjFLR = self.NSjWHcStKTLbU(UMUhLJhkv, pVdYFhAaXsyyci, qxyEWz, VQKNKnUpnwbt)
        t = localtime(pVdYFhAaXsyyci)
        vbTvognGGzN = ServiceReference(UMUhLJhkv)
        wxdWuWRukihTqU = cIlYUZavCM
        uGZVEpaLJ = self.JvSwzXgDeSH()[0]
        if uGZVEpaLJ is not None:
            ilGQEEnSuF = uGZVEpaLJ.getShortDescription()
            if ilGQEEnSuF and ilGQEEnSuF != cIlYUZavCM:
                wxdWuWRukihTqU = cIlYUZavCM + ' - ' + ilGQEEnSuF
        if rLTFYjFLR == True:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = djalaNtmJRirVIK = mTaqht = iHYMQIruq = self.ZWXRUOATTV
            yPwnoweEIEi = self.kUdFNIT
        elif rLTFYjFLR == False:
            QLxdqGrZFSq = IljDvazPimAt = uSfYSrtgTKg = djalaNtmJRirVIK = mTaqht = iHYMQIruq = self.hXbYdg
            yPwnoweEIEi = self.kUdFNIT
        else:
            IljDvazPimAt = self.BPTUvuBjQ
            uSfYSrtgTKg = self.Wzjij
            djalaNtmJRirVIK = self.SMtkYND
            mTaqht = self.WFivLbUm
            iHYMQIruq = self.tyoaImn
            yPwnoweEIEi = self.eYKVAYQZkZCaAod
            QLxdqGrZFSq = self.WubpaSVNw
        res = [None, (eListboxPythonMultiContent.TYPE_TEXT,
          self.DZOLaKQYXqw,
          self.HEFcVeCmfjDPNdq,
          self.FIrFKOOPfdRJnb,
          50,
          0,
          RT_HALIGN_RIGHT,
          self.PsMWO[t[6]],
          djalaNtmJRirVIK,
          QLxdqGrZFSq,
          self.sZFcJcEYedYG,
          self.ZlvGlXNkLDSSOLB)]
        res.append(MultiContentEntryText(pos=(self.VnmwSXzd, self.oTwHuYB), size=(self.zmTOunm, 50), font=0, text='%02d.%02d' % (t[2], t[1]), color=mTaqht, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.ZlvGlXNkLDSSOLB, border_width=0, border_color=self.sZFcJcEYedYG))
        res.append(MultiContentEntryText(pos=(self.HkPIn, self.RVaddhJ), size=(self.vDtXdSWMj, 50), font=0, text='%02d:%02d' % (t[3], t[4]), color=iHYMQIruq, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.ZlvGlXNkLDSSOLB, border_width=0, border_color=self.sZFcJcEYedYG))
        res.append(MultiContentEntryText(pos=(self.mMQSGwZt, self.BwBxpeGsFk), size=(self.DrEcqGyi, 50), font=1, text=vbTvognGGzN.getServiceName(), color=IljDvazPimAt, color_sel=QLxdqGrZFSq, backcolor=self.sZFcJcEYedYG, backcolor_sel=self.ZlvGlXNkLDSSOLB))
        res.append(MultiContentEntryText(pos=(self.CwbbgtPbYdAJaNS, self.icJJVKHwold), size=(self.oVoKs, 50), font=2, text=wxdWuWRukihTqU, color=uSfYSrtgTKg, color_sel=QLxdqGrZFSq, backcolor=yPwnoweEIEi, backcolor_sel=self.ZlvGlXNkLDSSOLB))
        return res


class lyqBhZ(XEArkQXQCQRMEL):

    def __init__(self, session, *args):
        Screen.__init__(self, session)
        self.skinName = 'CoolSearch'
        if TMvKPeMEZHVqV == 720:
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSearch_720.xml'
        elif TMvKPeMEZHVqV == 1024:
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSearch_1024.xml'
        else:
            WgQTyCqDMVdNMj = '/usr/lib/enigma2/python/Plugins/Extensions/CoolTVGuide/CoolSkin/CoolSearch_1280.xml'
        bRPkNqLYgEu = open(WgQTyCqDMVdNMj)
        self.skin = bRPkNqLYgEu.read()
        bRPkNqLYgEu.close()
        self['key_red'] = Button('')
        self['key_yellow'] = Button(_('New Search'))
        self['key_blue'] = Button(_('Last Search'))
        self['key_green'] = Button(_('Add Timer'))
        self.vzDGDGAQLSCa = -1
        self.FUiTqUurDFxy = False
        self.GQXnqX = 0
        self.args = args
        self.PsMWO = (_('Mon'),
         _('Tue'),
         _('Wed'),
         _('Thu'),
         _('Fri'),
         _('Sat'),
         _('Sun'))
        self['date'] = Button()
        self['Event'] = Event()
        self['Service'] = ServiceEvent()
        self.ARWFznDovLER = zUIfAWMBbQJ
        self.VsbLMxaqGuOhxRV = None
        self.XISehjxsPoi = None
        self.cIKHf = None
        self.nfZQJKwSrVA = None
        self.type = None
        self['list'] = zlrcRXjIYOUnyoy(pOHOrwCihqC=self.WlFKMlyFxSWrG, QHYMHhwOVIXtLT=session.nav.RecordTimer)
        self['Coolman'] = ActionMap(['CoolTVGuideActions'], {'CoolRed': self.GwhJbNuquP,
         'CoolRecord': self.fSZoXHuVHrXQaZ,
         'CoolGreen': self.EmOZX,
         'CoolGreenLong': self.voLEWybvGX,
         'CoolYellow': self.MJpYCzrTtwLWD,
         'CoolBlue': self.qsDCwRsYOveEFy,
         'CoolOK': self.WhRkmBFDyxfV,
         'CoolInfo': self.NxrXAek,
         'CoolInfoLong': self.uWIjFbGhtX,
         'CoolKeyTV': self.EekrcnjXd,
         'CoolPower': self.EUtMyA,
         'CoolCancel': self.MYzHZQS}, -1)
        self.onLayoutFinish.append(self.NbmZQLxewbo)
        self.AJqssBimVAO()
        SuVhHLBrOFx = config.CTVG.C12.value
        if SuVhHLBrOFx == 'PrimeTime' or SuVhHLBrOFx == 'Bouquet +' or SuVhHLBrOFx == 'Bouquet -' or SuVhHLBrOFx == 'Bouquetlist' or SuVhHLBrOFx == 'Zap' or SuVhHLBrOFx == 'Zap + Exit':
            SuVhHLBrOFx = 'EPG Select'
        self['key_red'].setText(SuVhHLBrOFx)
        return

    def qFDSvr(self):
        global WmXVqUV
        if WmXVqUV == 1:
            x = config.CTVG.C77.value
        elif WmXVqUV == 2:
            x = config.CTVG.C78.value
        elif WmXVqUV == 3:
            x = config.CTVG.C79.value
        elif WmXVqUV == 4:
            if WvYVaQ != self.ARWFznDovLER and SAQsYCIeDb != self.ARWFznDovLER:
                WmXVqUV = 1
                return self.close(False)
            x = config.CTVG.C80.value
        elif WmXVqUV == 5:
            x = config.CTVG.C81.value
        elif WmXVqUV == 6:
            x = config.CTVG.C82.value
        elif WmXVqUV == 7:
            x = config.CTVG.C83.value
        elif WmXVqUV == 8:
            x = config.CTVG.C84.value
        elif WmXVqUV == 9:
            x = config.CTVG.C85.value
        elif WmXVqUV == 10:
            x = config.CTVG.C86.value
        elif WmXVqUV == 11:
            x = config.CTVG.C87.value
        elif WmXVqUV == 12:
            x = config.CTVG.C88.value
        if x == '9':
            WmXVqUV += 1
            return self.qFDSvr()
        self.hide()
        if x == '1':
            self.WVwFshleYbnIc()
        elif x == '2':
            CSGmain(self.session, TrruhKvKi)
        elif x == '3':
            CEGmain(self.session, TrruhKvKi)
        elif x == '4':
            CCGmain(self.session, TrruhKvKi)
        elif x == '5':
            config.CTVG.C40.value = 1
            main(self.session, TrruhKvKi)
        elif x == '6':
            config.CTVG.C40.value = 2
            main(self.session, TrruhKvKi)
        elif x == '7':
            config.CTVG.C40.value = 3
            main(self.session, TrruhKvKi)
        elif x == '8':
            config.CTVG.C40.value = 4
            main(self.session, TrruhKvKi)
        else:
            if x == '10':
                WmXVqUV += 1
                return self.qFDSvr()
            if x == '11':
                WmXVqUV = 0
                self.session.open(TimerEditList)
            else:
                WmXVqUV = 0
        WmXVqUV += 1
        self.close(False)

    def AJqssBimVAO(self):
        geikSRpcvam = localtime()
        if (geikSRpcvam.tm_year, geikSRpcvam.tm_mon) >= (int(cwCvsFoxrpLR[4:8]), int(IUqwdjkcjCMKCFO[2])):
            self.MYzHZQS()

    def qsDCwRsYOveEFy(self):
        ShlcWaHEdHz = [ (x, x) for x in config.CTVG.C10.value ]
        if ShlcWaHEdHz:
            self.session.openWithCallback(self.mRUIH, ChoiceBox, title=_('Search for:'), list=ShlcWaHEdHz)
        else:
            self.session.open(MessageBox, _('No history'), type=MessageBox.TYPE_INFO)

    def WhRkmBFDyxfV(self):
        BHOMkCjKRLhD = config.CTVG.C20.value
        if BHOMkCjKRLhD == 'Zap':
            self.MYzHZQS()
        elif BHOMkCjKRLhD == 'Zap + Exit':
            self.MYzHZQS()
        elif BHOMkCjKRLhD == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif BHOMkCjKRLhD == 'Timer':
            self.EmOZX()
        elif BHOMkCjKRLhD == 'QuickRec':
            self.fSZoXHuVHrXQaZ()
        elif BHOMkCjKRLhD == 'AutoTimer':
            self.voLEWybvGX()
        else:
            self.WVwFshleYbnIc()

    def NxrXAek(self):
        LkGwiX = config.CTVG.C22.value
        if LkGwiX == '4':
            self.qFDSvr()
        elif LkGwiX == '1':
            self.WVwFshleYbnIc()
        elif LkGwiX == '2':
            self.RDSJwxPYCfBLVaN()
        elif LkGwiX == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def uWIjFbGhtX(self):
        BkucHGwMEzEJ = config.CTVG.C23.value
        if BkucHGwMEzEJ == '4':
            self.qFDSvr()
        elif BkucHGwMEzEJ == '1':
            self.WVwFshleYbnIc()
        elif BkucHGwMEzEJ == '2':
            self.RDSJwxPYCfBLVaN()
        elif BkucHGwMEzEJ == '3':
            self.BvRoHaxNcu()
        else:
            self.WVwFshleYbnIc()

    def GwhJbNuquP(self):
        EcLNwIhunJbRsLQ = config.CTVG.C12.value
        if EcLNwIhunJbRsLQ == 'EPG Select':
            self.qFDSvr()
        elif EcLNwIhunJbRsLQ == 'Cool Info Guide':
            self.WVwFshleYbnIc()
        elif EcLNwIhunJbRsLQ == 'Timer':
            self.EmOZX()
        elif EcLNwIhunJbRsLQ == 'QuickRec':
            self.fSZoXHuVHrXQaZ()
        elif EcLNwIhunJbRsLQ == 'AutoTimer':
            self.voLEWybvGX()
        else:
            self.qFDSvr()

    def NbmZQLxewbo(self):
        self.setTitle(_('Cool Search'))
        if self.args:
            self.zpKcGnq(*self.args)
        else:
            l = self['list']
            l.rRtWCitddeQKbbF()
            l.list = []
            l.l.setList(l.list)
        del self.args

    def WlFKMlyFxSWrG(self):
        zjRLCa = self['list'].JvSwzXgDeSH()
        uGZVEpaLJ = zjRLCa[0]
        self['Event'].newEvent(uGZVEpaLJ)
        yyJciFsdx = ''
        if uGZVEpaLJ is not None:
            geikSRpcvam = time()
            cpUukOBh = uGZVEpaLJ.getBeginTime()
            rbuTrfjskKNUrpX = localtime(geikSRpcvam)
            xCcvK = localtime(cpUukOBh)
            if rbuTrfjskKNUrpX[2] != xCcvK[2]:
                yyJciFsdx = '%s %d.%d.' % (self.PsMWO[xCcvK[6]], xCcvK[2], xCcvK[1])
            else:
                yyJciFsdx = '%s %d.%d.' % (_('Today'), xCcvK[2], xCcvK[1])
        self['date'].setText(yyJciFsdx)
        if zjRLCa[1] is None:
            self['Service'].newService(None)
        else:
            self['Service'].newService(zjRLCa[1].ref)
        if not uGZVEpaLJ:
            self['key_green'].setText('')
            return
        else:
            YdIQlXcvk = zjRLCa[1]
            GuCQMEFykarWc = uGZVEpaLJ.getEventId()
            RbbvURoedMdnrU = YdIQlXcvk.ref.toString()
            xCEOmOL = False
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == GuCQMEFykarWc and QHYMHhwOVIXtLT.service_ref.ref.toString() == RbbvURoedMdnrU:
                    xCEOmOL = True
                    break

            if xCEOmOL:
                self['key_green'].setText(_('TimerEdit'))
            else:
                self['key_green'].setText(_('Timer'))
            return

    def nextService(self):
        if self.nfZQJKwSrVA:
            self.nfZQJKwSrVA(1, self)

    def prevService(self):
        if self.nfZQJKwSrVA:
            self.nfZQJKwSrVA(-1, self)

    def WVwFshleYbnIc(self):
        tfonHdIjfgQ = self['list'].JvSwzXgDeSH()
        UMUhLJhkv = tfonHdIjfgQ[1]
        WVAXBEaVAJdsN = tfonHdIjfgQ[0]
        if not WVAXBEaVAJdsN:
            return
        tlvldyLLXXHo = eServiceReference(str(UMUhLJhkv))
        if tlvldyLLXXHo:
            self.session.open(zDKhcfAp, WVAXBEaVAJdsN, UMUhLJhkv, tlvldyLLXXHo, self.QEcLxYKv, PwRojNX=PQMOk)

    def RDSJwxPYCfBLVaN(self):
        self.hide()
        CSGmain(self.session, TrruhKvKi)
        self.MYzHZQS()

    def BvRoHaxNcu(self):
        self.hide()
        CEGmain(self.session, TrruhKvKi)
        self.MYzHZQS()

    def QEcLxYKv(self, QoGRewjlErZRq, setService, val):
        if val == -1:
            self.GdjxEetRD()
        elif val == +1:
            self.Krkrxa()
        bJKvGIVemCb = self['list'].JvSwzXgDeSH()
        setService(bJKvGIVemCb[1])
        QoGRewjlErZRq(bJKvGIVemCb[0])

    def MJpYCzrTtwLWD(self):
        self.session.openWithCallback(self.zpKcGnq, rPPVHYsAJVv, title=_('Search for:'))

    def EUtMyA(self):
        try:
            from Screens.SleepTimerEdit import SleepTimerEdit
            self.session.open(SleepTimerEdit)
        except:
            pass

    def voLEWybvGX(self):
        bJKvGIVemCb = self['list'].JvSwzXgDeSH()
        if not bJKvGIVemCb:
            return
        try:
            from Plugins.Extensions.AutoTimer.AutoTimerEditor import addAutotimerFromEvent
            self.session.openWithCallback(self.aqFgBg, ChoiceBox, title=_('   check Autotimer ?'), list=[(_('Yes'), 'Yes'), (_('No'), 'No')])
            addAutotimerFromEvent(self.session, bJKvGIVemCb[0], bJKvGIVemCb[1])
        except:
            self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def aqFgBg(self, nKGKSPXPp):
        nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
        if nKGKSPXPp == 'Yes':
            try:
                from Plugins.Extensions.AutoTimer.plugin import main as AutoTimerSafe
                AutoTimerSafe(self.session)
            except:
                self.session.open(MessageBox, _('No AutoTimer seems to be installed. Please install it for this functionality.'), MessageBox.TYPE_ERROR)

    def fSZoXHuVHrXQaZ(self):
        EnFKRmiyy = self['list'].JvSwzXgDeSH()
        KLejqTfVkFflXR = EnFKRmiyy[1]
        uGZVEpaLJ = EnFKRmiyy[0]
        if not uGZVEpaLJ:
            return
        else:
            GuCQMEFykarWc = uGZVEpaLJ.getEventId()
            mYutncHSgwJ = KLejqTfVkFflXR.ref.toString()
            for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
                if QHYMHhwOVIXtLT.eit == GuCQMEFykarWc and QHYMHhwOVIXtLT.service_ref.ref.toString() == mYutncHSgwJ:
                    self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
                    self['list'].l.invalidate()
                    break
            else:
                ZFcHE = RecordTimerEntry(KLejqTfVkFflXR, checkOldTimers=True, *parseEvent(uGZVEpaLJ))
                import NavigationInstance
                BjDtxuaz = NavigationInstance.instance.RecordTimer.record(ZFcHE)
                if BjDtxuaz is not None:
                    for x in BjDtxuaz:
                        if x.setAutoincreaseEnd(ZFcHE):
                            self.session.nav.RecordTimer.timeChanged(x)

                    BjDtxuaz = self.session.nav.RecordTimer.record(ZFcHE)
                    if BjDtxuaz is not None:
                        self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, BjDtxuaz)
                self['list'].l.invalidate()

            self.WlFKMlyFxSWrG()
            return

    def EekrcnjXd(self):
        self.session.open(TimerEditList)

    def EmOZX(self):
        fzPWRjmyFOdPgK = self['list'].JvSwzXgDeSH()
        lWJAurf = fzPWRjmyFOdPgK[0]
        sTgNxkmJlcmVCv = fzPWRjmyFOdPgK[1]
        if not lWJAurf:
            return
        FZxOvzpGBD = lWJAurf.getEventId()
        fXYLLkn = sTgNxkmJlcmVCv.ref.toString()
        for QHYMHhwOVIXtLT in self.session.nav.RecordTimer.timer_list:
            if QHYMHhwOVIXtLT.eit == FZxOvzpGBD and QHYMHhwOVIXtLT.service_ref.ref.toString() == fXYLLkn:
                self.QHYMHhwOVIXtLT = QHYMHhwOVIXtLT
                self.session.openWithCallback(self.pwCaxqRZQsvS, ChoiceBox, title=_('Cool Timer Edit :' + '\n\n%s') % lWJAurf.getEventName(), list=[(_('edit this Timer ?'), 'edit'), (_('delete this Timer ?'), 'delete'), (_('delete this Timer and recording ?'), 'delrec')])
                break
        else:
            ZFcHE = RecordTimerEntry(sTgNxkmJlcmVCv, checkOldTimers=True, *parseEvent(lWJAurf))
            self.session.openWithCallback(self.SohIHVvAMnbAXX, TimerEntry, ZFcHE)

    def pwCaxqRZQsvS(self, nKGKSPXPp):
        QHYMHhwOVIXtLT = self.QHYMHhwOVIXtLT
        pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp)

    def SohIHVvAMnbAXX(self, nKGKSPXPp):
        if nKGKSPXPp[0]:
            WFVjWbKbX = nKGKSPXPp[1]
            QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
            if QptgJyXzKf is not None:
                for x in QptgJyXzKf:
                    if x.setAutoincreaseEnd(WFVjWbKbX):
                        self.session.nav.RecordTimer.timeChanged(x)

                QptgJyXzKf = self.session.nav.RecordTimer.record(WFVjWbKbX)
                if QptgJyXzKf is not None:
                    self.session.openWithCallback(self.AoKSzJQJax, TimerSanityConflict, QptgJyXzKf)
            self['key_green'].setText(_('TimerEdit'))
        return

    def AoKSzJQJax(self, nKGKSPXPp):
        self.SohIHVvAMnbAXX(nKGKSPXPp)

    def zpKcGnq(self, dlEPuFX = None, Save = True):
        if dlEPuFX:
            if Save:
                shDpJynqgDBHhQd = config.CTVG.C10.value
                if dlEPuFX in shDpJynqgDBHhQd:
                    shDpJynqgDBHhQd.remove(dlEPuFX)
                    shDpJynqgDBHhQd.insert(0, dlEPuFX)
                else:
                    shDpJynqgDBHhQd.insert(0, dlEPuFX)
                    if len(shDpJynqgDBHhQd) > 9:
                        shDpJynqgDBHhQd.pop(9)
            if not config.CTVG.C11.value:
                try:
                    dlEPuFX = dlEPuFX.decode('UTF-8', 'replace').encode('ISO8859-15', 'replace')
                except (UnicodeDecodeError, UnicodeEncodeError):
                    pass

            epgcache = eEPGCache.getInstance()
            ret = epgcache.search(('RIBDT',
             500,
             eEPGCache.PARTIAL_TITLE_SEARCH,
             dlEPuFX,
             eEPGCache.NO_CASE_CHECK)) or []
            ret.sort(key=lambda x: x[2])
            l = self['list']
            l.rRtWCitddeQKbbF()
            l.list = ret
            l.l.setList(ret)

    def mRUIH(self, ret):
        if ret:
            self.zpKcGnq(ret[1])

    def MYzHZQS(self):
        global WmXVqUV
        WmXVqUV = 1
        config.CTVG.save()
        self.close(self.FUiTqUurDFxy)


def pwCaxqRZQsvS(self, QHYMHhwOVIXtLT, nKGKSPXPp):
    nKGKSPXPp = nKGKSPXPp and nKGKSPXPp[1]
    if nKGKSPXPp == 'delete':
        self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
        return
    if nKGKSPXPp == 'edit':
        self.session.open(TimerEntry, QHYMHhwOVIXtLT)
        return
    if nKGKSPXPp == 'delrec':
        self.session.nav.RecordTimer.removeEntry(QHYMHhwOVIXtLT)
        from Tools.Directories import SCOPE_HDD
        from enigma import eBackgroundFileEraser
        mlKYJHBCJKKfR = resolveFilename(SCOPE_HDD)
        YgMqXn = str(QHYMHhwOVIXtLT.service_ref.getServiceName())
        evSsHiNlDkyz = '/.\\:*?<>|"'
        qKaajCJGMNQR = ''
        for s in YgMqXn:
            if s in evSsHiNlDkyz:
                s = '_'
            qKaajCJGMNQR += s

        MtNStPBIS = strftime('%Y%m%d %H%M', localtime(QHYMHhwOVIXtLT.begin))
        qKaajCJGMNQR = qKaajCJGMNQR.replace('\xc2\x86', '').replace('\xc2\x87', '')
        qKaajCJGMNQR = MtNStPBIS + ' - ' + qKaajCJGMNQR
        kqdPHCnttTryenm = os.listdir(mlKYJHBCJKKfR)
        for xfile in kqdPHCnttTryenm:
            if xfile.startswith(qKaajCJGMNQR):
                eBackgroundFileEraser.getInstance().erase(os.path.realpath(mlKYJHBCJKKfR + xfile))

        return


def nePylQgKlghpaVP(drBLtPKZn = None):
    try:
        from Screens.InfoBar import InfoBar
        from Plugins.Extensions.EnhancedMovieCenter.plugin import showMoviesNew
        showMoviesNew(InfoBar.instance)
    except:
        from Screens.InfoBar import InfoBar
        InfoBar.showMovies(InfoBar.instance)


def CSmain(session, *args, **kwargs):
    VKPKxXnQbHarec = session.nav.getCurrentService()
    if VKPKxXnQbHarec:
        NHozf = VKPKxXnQbHarec.info()
        hIJmEpeVSE = NHozf.getEvent(0)
        dNZCbIlhYcesiab = hIJmEpeVSE and hIJmEpeVSE.getEventName() or ''
        session.open(lyqBhZ, dNZCbIlhYcesiab, False)
    else:
        session.open(lyqBhZ)


def autostart(reason, **kwargs):
    global RxrHDyIpb
    if RxrHDyIpb is None:
        RxrHDyIpb = InfoBarPlugins.__init__
    InfoBarPlugins.__init__ = QaDpttUzKDzt
    if config.CTVG.C31.value:
        InfoBarPlugins.GwhJbNuquP = GwhJbNuquP
    if config.CTVG.C32.value:
        InfoBarPlugins.gXppchsrp = gXppchsrp
    if config.CTVG.C33.value:
        InfoBarPlugins.bKpKe = bKpKe
    if config.CTVG.C34.value:
        InfoBarPlugins.NxrXAek = NxrXAek
    if config.CTVG.C35.value:
        InfoBarPlugins.MZYuDXjk = MZYuDXjk
    return


def QaDpttUzKDzt(self):
    global sNZiOf
    global vZKwD
    if not vZKwD:
        vZKwD = True
        sNZiOf = self
        try:
            self['Red'] = ActionMap(['CoolTVGuide'], {'CoolRed': self.GwhJbNuquP}, -1000)
        except:
            pass

        try:
            self['Green'] = ActionMap(['CoolTVGuide'], {'CoolGreen': self.gXppchsrp}, -1000)
        except:
            pass

        try:
            self['Yellow'] = ActionMap(['CoolTVGuide'], {'CoolYellow': self.bKpKe}, -1000)
        except:
            pass

        try:
            self['Info'] = ActionMap(['CoolTVGuide'], {'CoolInfo': self.NxrXAek}, -1000)
        except:
            pass

        try:
            self['Down'] = ActionMap(['CoolTVGuide'], {'CoolDown': self.MZYuDXjk}, -1000)
        except:
            pass

    else:
        InfoBarPlugins.__init__ = InfoBarPlugins.__init__
        InfoBarPlugins.GwhJbNuquP = None
        InfoBarPlugins.gXppchsrp = None
        InfoBarPlugins.bKpKe = None
        InfoBarPlugins.NxrXAek = None
        InfoBarPlugins.MZYuDXjk = None
    RxrHDyIpb(self)
    return


def GwhJbNuquP(self):
    main(self.session)


def gXppchsrp(self):
    CSGmain(self.session)


def bKpKe(self):
    CEGmain(self.session)


def NxrXAek(self):
    CIGmain(self.session)


def MZYuDXjk(self):
    CCGmain(self.session)


def CIGmain(session, servicelist = None, UMUhLJhkv = None, **kwargs):
    global eFSzkTC
    global TrruhKvKi
    if servicelist == None:
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            servicelist = InfoBar.instance.servicelist
        else:
            session.open(MessageBox, _(' No function with your Image'), MessageBox.TYPE_ERROR)
            return
    eFSzkTC = session
    TrruhKvKi = servicelist
    from Screens.InfoBar import InfoBar
    if InfoBar and InfoBar.instance:
        tThtoqxgwoDos(InfoBar.instance, UMUhLJhkv)
    return


def changeServiceCB(self, SqpegV, epg):
    if self.serviceSel:
        if SqpegV > 0:
            self.serviceSel.nextService()
        else:
            self.serviceSel.prevService()
        epg.setService(self.serviceSel.currentService())


def tThtoqxgwoDos(self, UMUhLJhkv = None):
    FECLDIUip = self.session.nav.getCurrentlyPlayingServiceReference()
    self.jgohPdWH = eEPGCache.getInstance()
    ivsBFJkimXjpdOa = FECLDIUip and FECLDIUip.valid() and self.jgohPdWH.lookupEventTime(FECLDIUip, -1)
    if FECLDIUip:
        gGPiwVmWkgM = TrruhKvKi.getRoot()
        ZnHPgSvmg = self.getBouquetServices(gGPiwVmWkgM)
        self.serviceSel = SimpleServicelist(ZnHPgSvmg)
        if self.serviceSel.selectService(FECLDIUip):
            self.session.openWithCallback(None, zDKhcfAp, ivsBFJkimXjpdOa, UMUhLJhkv, FECLDIUip, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=PQMOk)
        else:
            FECLDIUip = self.session.nav.getCurrentlyPlayingServiceReference()
            if self.serviceSel.selectService(FECLDIUip):
                self.session.openWithCallback(None, zDKhcfAp, None, None, FECLDIUip, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=PQMOk)
    return


def vnUBmWi(self):
    zxFcSTEMso = self.session.nav.getCurrentlyPlayingServiceReference()
    if zxFcSTEMso:
        gGPiwVmWkgM = TrruhKvKi.getRoot()
        ZnHPgSvmg = self.getBouquetServices(gGPiwVmWkgM)
        self.serviceSel = SimpleServicelist(ZnHPgSvmg)
        if self.serviceSel.selectService(zxFcSTEMso):
            self.session.open(XEArkQXQCQRMEL, zxFcSTEMso, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=iXZeUPZjXi)
        else:
            zxFcSTEMso = self.session.nav.getCurrentlyPlayingServiceReference()
            if self.serviceSel.selectService(zxFcSTEMso):
                self.session.open(XEArkQXQCQRMEL, zxFcSTEMso, nfZQJKwSrVA=self.changeServiceCB, TrruhKvKi=TrruhKvKi, PwRojNX=iXZeUPZjXi)


def CSGmain(session, servicelist = None, **kwargs):
    global TrruhKvKi
    if servicelist == None:
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            servicelist = InfoBar.instance.servicelist
        else:
            session.open(MessageBox, _(' No function with your Image'), MessageBox.TYPE_ERROR)
            return
    TrruhKvKi = servicelist
    from Screens.InfoBar import InfoBar
    if InfoBar and InfoBar.instance:
        vnUBmWi(InfoBar.instance)
    return


def TDkLColEQkJNRDf(JWIavJN):
    global FufElMDyUtWr
    qDFTEDFxno = getBouquetServices(JWIavJN)
    if len(qDFTEDFxno):
        FufElMDyUtWr = JWIavJN
        IJZNPmqFF.append(eFSzkTC.openWithCallback(aDeGikfwnNVq, sduqcURd, qDFTEDFxno, zpUgvK, TrruhKvKi, ServiceReference(FufElMDyUtWr).getServiceName(), PwRojNX=IUqwdjkcjCMKCFO))
        return True
    return False


def fJIPSJ(eFSzkTC):
    global FPDSuRw
    global XQiSkUFpb
    XQiSkUFpb = TrruhKvKi.getBouquetList()
    if XQiSkUFpb is None:
        cnt = 0
    else:
        cnt = len(XQiSkUFpb)
    if cnt > 1:
        FPDSuRw = eFSzkTC.openWithCallback(aDeGikfwnNVq, wPwKYfbYpKpNbBT, XQiSkUFpb, TDkLColEQkJNRDf, JsvfEKlOnNEpEQX=True)
        IJZNPmqFF.append(FPDSuRw)
    elif cnt == 1:
        if not TDkLColEQkJNRDf(XQiSkUFpb[0][1]):
            tzzVFZQcxctLZM()
    return


def wLAIlv():
    global FPDSuRw
    global XQiSkUFpb
    XQiSkUFpb = TrruhKvKi.getBouquetList()
    if XQiSkUFpb is None:
        cnt = 0
    else:
        cnt = len(XQiSkUFpb)
    zehTthMch = TrruhKvKi.getRoot()
    if cnt > 1:
        LQcplWSWs = 0
        WjAUFEamHqbEgs = zehTthMch.toCompareString()
        for x in XQiSkUFpb:
            if x[1].toCompareString() == WjAUFEamHqbEgs:
                break
            LQcplWSWs += 1

        if LQcplWSWs >= cnt:
            LQcplWSWs = 0
        FPDSuRw = pHQdnxNnMi(XQiSkUFpb, True, LQcplWSWs)
    if cnt >= 1:
        if not TDkLColEQkJNRDf(zehTthMch):
            tzzVFZQcxctLZM()
    return


def CEGmain(session, servicelist = None, **kwargs):
    global eFSzkTC
    global TrruhKvKi
    if servicelist is None:
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            servicelist = InfoBar.instance.servicelist
        else:
            session.open(MessageBox, _(' No function with your Image'), MessageBox.TYPE_ERROR)
            return
    eFSzkTC = session
    TrruhKvKi = servicelist
    wLAIlv()
    return


def MMMmjxP(JWIavJN):
    qDFTEDFxno = []
    YJfSZuIqCuH = eServiceCenter.getInstance().list(JWIavJN)
    if YJfSZuIqCuH is not None:
        while True:
            UMUhLJhkv = YJfSZuIqCuH.getNext()
            if not UMUhLJhkv.valid():
                break
            if UMUhLJhkv.flags & eServiceReference.isDirectory:
                continue
            qDFTEDFxno.append(ServiceReference(UMUhLJhkv))

    return qDFTEDFxno


def VCRwoeTZC(JWIavJN):
    global FufElMDyUtWr
    qDFTEDFxno = MMMmjxP(JWIavJN)
    if len(qDFTEDFxno):
        FufElMDyUtWr = JWIavJN
        IJZNPmqFF.append(eFSzkTC.openWithCallback(aDeGikfwnNVq, fECRrOPDKlFDx, qDFTEDFxno, zcGwhuPYqCMX, TrruhKvKi, ServiceReference(FufElMDyUtWr).getServiceName(), PwRojNX=QQdKtJPxMxJPjwB))
        return True
    return False


def zcGwhuPYqCMX(SqpegV, epg):
    global xKmXaE
    global FufElMDyUtWr
    xKmXaE = None
    if FPDSuRw:
        if SqpegV > 0:
            FPDSuRw.down()
        else:
            FPDSuRw.up()
        JWIavJN = FPDSuRw.getCurrent()
        qDFTEDFxno = MMMmjxP(JWIavJN)
        if len(qDFTEDFxno):
            FufElMDyUtWr = JWIavJN
            epg.qFLoYuYRPQFdK(qDFTEDFxno)
            epg.setTitle(ServiceReference(JWIavJN).getServiceName())
    return


def ToIxnZLjAph(eFSzkTC):
    global FPDSuRw
    global XQiSkUFpb
    XQiSkUFpb = TrruhKvKi.getBouquetList()
    if XQiSkUFpb is None:
        cnt = 0
    else:
        cnt = len(XQiSkUFpb)
    if cnt > 1:
        FPDSuRw = eFSzkTC.openWithCallback(aDeGikfwnNVq, wPwKYfbYpKpNbBT, XQiSkUFpb, VCRwoeTZC, JsvfEKlOnNEpEQX=True)
        IJZNPmqFF.append(FPDSuRw)
    elif cnt == 1:
        if not VCRwoeTZC(XQiSkUFpb[0][1]):
            tzzVFZQcxctLZM()
    return


def bOEPgo():
    global FPDSuRw
    global XQiSkUFpb
    XQiSkUFpb = TrruhKvKi.getBouquetList()
    if XQiSkUFpb is None:
        cnt = 0
    else:
        cnt = len(XQiSkUFpb)
    zehTthMch = TrruhKvKi.getRoot()
    if cnt > 1:
        LQcplWSWs = 0
        WjAUFEamHqbEgs = zehTthMch.toCompareString()
        for xbouquet in XQiSkUFpb:
            if xbouquet[1].toCompareString() == WjAUFEamHqbEgs:
                break
            LQcplWSWs += 1

        if LQcplWSWs >= cnt:
            LQcplWSWs = 0
        FPDSuRw = pHQdnxNnMi(XQiSkUFpb, True, LQcplWSWs)
    if cnt >= 1:
        if not VCRwoeTZC(zehTthMch):
            tzzVFZQcxctLZM()
    return


def CCGmain(session, servicelist = None, **kwargs):
    global eFSzkTC
    global TrruhKvKi
    if servicelist is None:
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            servicelist = InfoBar.instance.servicelist
        else:
            session.open(MessageBox, _(' No function with your Image'), MessageBox.TYPE_ERROR)
            return
    eFSzkTC = session
    TrruhKvKi = servicelist
    bOEPgo()
    return


def FllUJdlN(UMUhLJhkv):
    if UMUhLJhkv is not None:
        if TrruhKvKi.getRoot() != FufElMDyUtWr:
            TrruhKvKi.clearPath()
            if TrruhKvKi.bouquet_root != FufElMDyUtWr:
                TrruhKvKi.enterPath(TrruhKvKi.bouquet_root)
            TrruhKvKi.enterPath(FufElMDyUtWr)
        TrruhKvKi.setCurrentSelection(UMUhLJhkv)
        TrruhKvKi.zap()
    return


def getBouquetServices(JWIavJN):
    qDFTEDFxno = []
    qFWZuFWGget = eServiceCenter.getInstance().list(JWIavJN)
    if qFWZuFWGget is not None:
        while True:
            UMUhLJhkv = qFWZuFWGget.getNext()
            if not UMUhLJhkv.valid():
                break
            if UMUhLJhkv.flags & (eServiceReference.isDirectory | eServiceReference.isMarker):
                continue
            qDFTEDFxno.append(ServiceReference(UMUhLJhkv))

    return qDFTEDFxno


def tzzVFZQcxctLZM():
    global xKmXaE
    global eFSzkTC
    global TrruhKvKi
    eFSzkTC = None
    TrruhKvKi = None
    xKmXaE = None
    return


def aDeGikfwnNVq(ret = False):
    global FPDSuRw
    GnTUJrh = IJZNPmqFF.pop()
    if FPDSuRw and GnTUJrh == FPDSuRw:
        FPDSuRw = None
    vaPvKfzpvTAZ = len(IJZNPmqFF)
    if ret and vaPvKfzpvTAZ > 0:
        IJZNPmqFF[vaPvKfzpvTAZ - 1].close(vaPvKfzpvTAZ > 1)
    if vaPvKfzpvTAZ <= 0:
        tzzVFZQcxctLZM()
    return


def JCExyHUtZugOf(JWIavJN):
    global FufElMDyUtWr
    qDFTEDFxno = getBouquetServices(JWIavJN)
    if len(qDFTEDFxno):
        FufElMDyUtWr = JWIavJN
        IJZNPmqFF.append(eFSzkTC.openWithCallback(aDeGikfwnNVq, znjhVZLcrBZZBbq, qDFTEDFxno, zpUgvK, ServiceReference(FufElMDyUtWr).getServiceName(), PwRojNX=eseWoWLtSYyCHGT))
        return True
    return False


def zpUgvK(SqpegV, epg):
    global xKmXaE
    global FufElMDyUtWr
    xKmXaE = None
    if FPDSuRw:
        if SqpegV > 0:
            FPDSuRw.down()
        else:
            FPDSuRw.up()
        JWIavJN = FPDSuRw.getCurrent()
        ZnHPgSvmg = getBouquetServices(JWIavJN)
        if len(ZnHPgSvmg):
            FufElMDyUtWr = JWIavJN
            epg.qFLoYuYRPQFdK(ZnHPgSvmg)
            epg.setTitle(ServiceReference(JWIavJN).getServiceName())
    return


def CuFXFBycHL(eFSzkTC):
    global FPDSuRw
    global XQiSkUFpb
    XQiSkUFpb = TrruhKvKi.getBouquetList()
    if XQiSkUFpb is None:
        cnt = 0
    else:
        cnt = len(XQiSkUFpb)
    if cnt > 1:
        FPDSuRw = eFSzkTC.openWithCallback(aDeGikfwnNVq, wPwKYfbYpKpNbBT, XQiSkUFpb, JCExyHUtZugOf, JsvfEKlOnNEpEQX=True)
        IJZNPmqFF.append(FPDSuRw)
    elif cnt == 1:
        if not JCExyHUtZugOf(XQiSkUFpb[0][1]):
            tzzVFZQcxctLZM()
    return


def pcNAJZTTwzHECp():
    global FPDSuRw
    global XQiSkUFpb
    XQiSkUFpb = TrruhKvKi.getBouquetList()
    if XQiSkUFpb is None:
        cnt = 0
    else:
        cnt = len(XQiSkUFpb)
    PZlkOvrojba = TrruhKvKi.getRoot()
    if cnt > 1:
        LQcplWSWs = 0
        WjAUFEamHqbEgs = PZlkOvrojba.toCompareString()
        for JWIavJN in XQiSkUFpb:
            if JWIavJN[1].toCompareString() == WjAUFEamHqbEgs:
                break
            LQcplWSWs += 1

        if LQcplWSWs >= cnt:
            LQcplWSWs = 0
        FPDSuRw = pHQdnxNnMi(XQiSkUFpb, True, LQcplWSWs)
    if cnt >= 1:
        if not JCExyHUtZugOf(PZlkOvrojba):
            tzzVFZQcxctLZM()
    return


def main(session, servicelist = None, **kwargs):
    global eFSzkTC
    global TrruhKvKi
    if (localtime().tm_year, localtime().tm_mon) >= (2029, 12):
        session.open(MessageBox, MxRGJuUKkDbp, MessageBox.TYPE_INFO)
    if servicelist == None:
        from Screens.InfoBar import InfoBar
        if InfoBar and InfoBar.instance:
            servicelist = InfoBar.instance.servicelist
        else:
            session.open(MessageBox, _(' No function with your Image'), MessageBox.TYPE_ERROR)
            return
    eFSzkTC = session
    TrruhKvKi = servicelist
    if config.CTVG.C36.value:
        CuFXFBycHL(eFSzkTC)
    else:
        pcNAJZTTwzHECp()
    return


def OpenSetup(session, **kwargs):
    try:
        session.openWithCallback(wImiGCFpPSqZ(session), oifusNtsQLjEI)
    except:
        pass


def wImiGCFpPSqZ(session):
    if WvYVaQ != config.CTVG.Key.value and SAQsYCIeDb != config.CTVG.Key.value:
        session.open(MessageBox, Po, MessageBox.TYPE_INFO)


def Plugins(**kwargs):
    des = _('Cool TV Guide 3D EPG with switchable 5-24 TV-Lines and changeable Buttons with Setup')
    return [PluginDescriptor(name='Cool TV Guide', description=des, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart=False, fnc=main),
     PluginDescriptor(name='Cool Easy Guide', description=des, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart=False, fnc=CEGmain),
     PluginDescriptor(name='Cool Single Guide', description=des, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart=False, fnc=CSGmain),
     PluginDescriptor(name='Cool Info Guide', description=des, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart=False, fnc=CIGmain),
     PluginDescriptor(name='Cool Channel Guide', description=des, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart=False, fnc=CCGmain),
     PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART, fnc=autostart),
     PluginDescriptor(name='Cool TV Guide ' + fPVrFQoMzxdFJY + ' (Setup)', description=_('configuration of all Guides for your special wishes'), where=PluginDescriptor.WHERE_PLUGINMENU, icon='CoolTVGuide.png', fnc=OpenSetup),
     PluginDescriptor(name='Cool TV Guide', description=des, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart=False, fnc=main),
     PluginDescriptor(name='Cool Easy Guide', description=des, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart=False, fnc=CEGmain),
     PluginDescriptor(name='Cool Single Guide', description=des, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart=False, fnc=CSGmain),
     PluginDescriptor(name='Cool Info Guide', description=des, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart=False, fnc=CIGmain),
     PluginDescriptor(name='Cool Channel Guide', description=des, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart=False, fnc=CCGmain)]