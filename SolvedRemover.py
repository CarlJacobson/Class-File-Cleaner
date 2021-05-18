import os
from pathlib import Path
import shutil

pathlist = Path().glob('**/solved')
for path in pathlist:
    #print(path)
    if (str(path)[16:19]).lower() == 'stu':
        print(path)
        shutil.rmtree(path)

pathlist = Path().glob('*/*')
for path in pathlist:
    if str(path)[2:] == 'TimeTracker.xlsx':
        print(path)
        os.remove(path)
    if str(path)[2:] == 'LessonPlan.md':
        print(path)
        os.remove(path)