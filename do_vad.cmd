@echo off

SET ROOT=%~dp0
SET DATA_CHUNKS=%ROOT%data\chunks\
SET DATA_COMBINED=%ROOT%data\combined\
SET LIST=%DATA_CHUNKS%list.txt
SET RATE=16000
SET CLASSES="anger;boredom;disgust;fear;happiness;neutral;sadness"


echo %RATE%
pause
%ROOT%bin\vadanno.exe -silence 1.0 -nTest 3 %DATA_CHUNKS% %RATE% %DATA_COMBINED% %LIST% %CLASSES%

pause
