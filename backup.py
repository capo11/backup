import os.path
import shutil
from datetime import *

if not (os.path.exists('backup')):
    os.mkdir('backup')

today = datetime.today()
week = today.strftime("%U")
os.mkdir('./backup/W' + week)
listadir = os.listdir('./')
for linea in listadir:
	linea.strip()
	if not (linea == 'backup' or linea == 'backup.py'):
		if week in linea:
			shutil.move('./' + linea, './backup/W' + week)
