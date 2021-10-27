import os
from pathlib import Path
import shutil

#Fetches list of all filepaths containing "solved"
pathlist = Path().glob('**/solved')
#Removes student solution files
for path in pathlist:
    if (str(path)[16:19]).lower() == 'stu':
        print(path)
        shutil.rmtree(path)

#Removes class time trackers and lesson plants
pathlist = Path().glob('*/*')
for path in pathlist:
    if str(path)[2:] == 'TimeTracker.xlsx':
        print(path)
        os.remove(path)
    if str(path)[2:] == 'LessonPlan.md':
        print(path)
        os.remove(path)
