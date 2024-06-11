@echo off

echo [i] Compling source code

pyinstaller --onefile --noconsole --noconfirm -i "Assets/Game Icon.ico" "Blocker 2.py"

echo [i] Cloneing requried folders/files

robocopy Assets dist/Assets /E
echo [i] Cloned Assets Folder into dist

robocopy Fonts dist/Fonts /E
echo [i] Cloned Fonts Folder into Dist

robocopy Sounds dist/Sounds /E
echo [i] Cloned Sonuds Folder into Dist

copy Data.json dist/Data.json /y
echo [i] Cloned Data File into Dist

ren dist Blocker2
echo [i] Renamed dist to Blocker2

echo [i] Fully complied source code
pause