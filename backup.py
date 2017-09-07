import os.path
import shutil
from datetime import *
import tarfile

#step 0
if not (os.path.exists('backup')):
	os.mkdir('backup')

#step 1
today = datetime.today()
week = today.strftime("%U")
os.mkdir('./backup/W' + week)
#step 2
listadir = os.listdir('./')
for linea in listadir:
	linea.strip()
	if not (linea == 'backup' or linea == 'backup.py'):
		if week in linea:
			shutil.move('./' + linea, './backup/W' + week)
#step 3
with tarfile.open('./backup/W' + week + '.tgz', 'w:gz') as tar:
	tar.add('./backup/W' + week, arcname=os.path.basename('./backup/W' + week))
#step 4
if not(os.path.exists('trash')):
	os.mkdir('trash')
#step 5
tutteDirectory = os.listdir('./')
for linea in tutteDirectory:
	if not (linea == "backup" or linea == "backup.py"):
		shutil.move('./' + linea, './trash')