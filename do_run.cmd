@echo off

SET ROOT=%~dp0

SET PIPELINE=emovoice
SET CONFIG=model.pipeline-config

echo model:type=%1 >> %CONFIG%
echo model:chain=%2 > %CONFIG%

%ROOT%bin\xmlpipe.exe -log ssi.log -config %CONFIG% %PIPELINE%

DEL %CONFIG%
pause