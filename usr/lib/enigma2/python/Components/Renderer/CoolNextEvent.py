# Embedded file name: /usr/lib/enigma2/python/Components/Renderer/CoolNextEvent.py
from Components.VariableText import VariableText
from enigma import eLabel, eEPGCache, eTimer
from Components.Renderer.Renderer import Renderer
from time import localtime
from Tools.BoundFunction import boundFunction
ytsjwt = None
lskiiq = None

class CoolNextEvent(Renderer, VariableText):

    def __init__(self):
        Renderer.__init__(self)
        VariableText.__init__(self)
        self.trrtmz = eEPGCache.getInstance()

    GUI_WIDGET = eLabel

    def changed(self, ytsjwt):
        self.nkulzj = eTimer()
        self.nkulzj.callback.append(boundFunction(self.zoppwz, ytsjwt))
        self.nkulzj.start(800, True)

    def zoppwz(self, ytsjwt):
        ptmqwi = self.source.event
        if ptmqwi is None:
            self.text = 'No EPG Data'
            return
        else:
            rjyljo = self.source.service
            nozttm = ''
            ivuxvt = None
            if self.trrtmz is not None:
                ivuxvt = self.trrtmz.lookupEvent(['IBDCT', (rjyljo.toString(),
                  0,
                  -1,
                  -1)])
            if ivuxvt:
                ivuxvt
                jjxtlk = 0
                for lskiiq in ivuxvt:
                    if jjxtlk > 0:
                        if lskiiq[4]:
                            lskiiq[4]
                            uuprlo = localtime(lskiiq[1])
                            nozttm = nozttm + '%02d:%02d  %s\n' % (uuprlo[3], uuprlo[4], lskiiq[4])
                        else:
                            lskiiq[4]
                            nozttm = nozttm + 'n/a\n'
                    jjxtlk += 1
                    if jjxtlk > 5:
                        break
                        continue

            else:
                ivuxvt
            self.text = nozttm
            return