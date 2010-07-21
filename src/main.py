import sys

from os import getcwd
from os.path import abspath, join, dirname

from org.graver.app import App

mainPath = abspath(join(getcwd(), __file__))
app = App(dirname(mainPath))
app.initApp(sys.argv)
app.start()