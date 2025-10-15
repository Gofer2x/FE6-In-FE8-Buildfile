set soundPrioFixEAPath=Tools\SoundScripts\SoundPriorityFixEA.event
set targetROMPath=FE6InFE8_Music.gba
cd %~dp0EventAssembler
ColorzCore A FE8 -output:%~dp0%targetROMPath% -input:%~dp0%soundPrioFixEAPath% --build-times
cd %~dp0