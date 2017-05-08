__author__ = 'Pasquadibiceglie-Zaza'

from distutils.core import setup
import py2exe
import os
import matplotlib

_appName = "FISDeT"
_appVersion = '1.0.0'
_appDescription = "Fuzzy inference system development tool"
_authorName = 'Vincenzo Pasquadibisceglie - Gianluca Zaza'
_authorEmail = 'infofisdet@gmail.com'
_authorURL = 'http://www.fisdet.altervista.org'

data_files=[('img',['img\Red.png']),('img',['img\Green.png']),('img',['img\Splash.png']),('img',['img\Trash.png']),('img',['img\Apply.png']),('img',['img\LogoInt.png']),('img',['img\Mod.png']),('img',['img\TastoPiu.png'])]
data_files.extend(matplotlib.get_py2exe_datafiles())

setup(
    windows=[{'script':'FISDeT.py', 'icon_resources':[(1,'img\LogoInt.ico')]}],
    name=_appName,
    version=_appVersion,
    description=_appDescription,
    author=_authorName,
    author_email=_authorEmail,
    url=_authorURL,
    options={
        'py2exe': {
            'packages' : ['matplotlib','pytz',r'scipy.sparse.csgraph._validation',r'scipy.special._ufuncs_cxx',
                          'fuzzy.defuzzify.COG','fuzzy.set.Function','fuzzy.set.Triangle','fuzzy.set.SFunction',
                          'fuzzy.set.ZFunction','fuzzy.norm.Min','fuzzy.operator.Compound','fuzzy.operator.Input',
                          'fuzzy.AdjectiveProxy','fuzzy.Rule','fuzzy.defuzzify.Dict','fuzzy.Adjective',
                          'fuzzy.InputVariable','fuzzy.OutputVariable','fuzzy.fuzzify.Plain','fuzzy.System',
                          'fuzzy.set.PiFunction','fuzzy.set.Polygon','fuzzy.set.Triangle','fuzzy.set.Trapez',
                            'FileDialog','fuzzy.defuzzify.COGS','fuzzy.defuzzify.LM','fuzzy.defuzzify.RM',
                          'fuzzy.defuzzify.MaxRight','fuzzy.defuzzify.MaxLeft'
                          ],
            'dll_excludes': ['libgdk-win32-2.0-0.dll',
                             'libgobject-2.0-0.dll',
                             'libgdk_pixbuf-2.0-0.dll',
                             'libgtk-win32-2.0-0.dll',
                             'libglib-2.0-0.dll',
                             'libcairo-2.dll',
                             'libpango-1.0-0.dll',
                             'libpangowin32-1.0-0.dll',
                             'libpangocairo-1.0-0.dll',
                             'libglade-2.0-0.dll',
                             'libgmodule-2.0-0.dll',
                             'libgthread-2.0-0.dll'],
        }
    },
    data_files=data_files
)
