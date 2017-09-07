import os.path
import shutil
from datetime import *

if not (os.path.exists('backup')):
    os.mkdir('backup')

today = datetime.today()
week = today.strftime("%U")
os.mkdir('./backup/W' + week)
