import os.path
import shutil
from datetime import *

if not (os.path.exists('backup')):
    os.mkdir('backup')

if not(os.path.exist('trash')):
    os.mkdir('trash')
tutteDirectory = os.listdir('./')
for linea in tutteDirectory():
    if not (linea == "backup" or linea == "backup.py"):
        shutil.move('./' + linea, './trash')
today = datetime.today()
week = today.strftime("%U")
os.mkdir('./backup/W' + week)
