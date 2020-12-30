from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext

def localeInit():
    lang = language.getLanguage()[:2]
    os_environ['LANGUAGE'] = lang
    gettext.bindtextdomain('CoolTVGuide', resolveFilename(SCOPE_PLUGINS, 'Extensions/CoolTVGuide/locale'))


_ = lambda txt: gettext.dgettext('CoolTVGuide', txt)
localeInit()
language.addCallback(localeInit)