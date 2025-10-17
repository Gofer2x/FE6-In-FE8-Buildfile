set csvPath=Tools\SoundScripts\FE6toFE8Sounds.csv
set updateSoundIDsScriptPath=Tools\SoundScripts\UpdateSoundIDs.py
set soundIDsPath=Definitions\Generated\NewFE6SoundIDs.event

cd %~dp0

echo Updating sound IDs.

call %updateSoundIDsScriptPath% %csvPath% %soundIDsPath%
