set genSoundScriptPath=Tools\SoundScripts\GenerateSoundBat.py
set generatedSoundExchangeBatPath=Tools\SoundScripts\_GeneratedSoundInsertion.bat
set generatedEAFixBatPath="Tools\SoundScripts\_GeneratedSoundEAFix.bat"
set csvPath=Tools\SoundScripts\FE6toFE8Sounds.csv
set febPath=Tools\FEBuilderGBA\FEBuilderGBA.exe
set fe6Path=FE6.gba
set inputHackWithoutMusicPath=FE6InFE8.gba
set outputHackWithMusicPath=FE6InFE8_Music.gba
set cleanFE8RomPath=FE8_clean.gba

set soundPrioFixEAPath=Tools\SoundScripts\SoundPriorityFixEA.event

cd %~dp0

copy %~dp0%inputHackWithoutMusicPath% %~dp0%outputHackWithMusicPath%

echo Generating sound insertion and EA fix .bats.

call %genSoundScriptPath% %generatedSoundExchangeBatPath% %generatedEAFixBatPath% %csvPath% %febPath% %fe6Path% %outputHackWithMusicPath% %soundPrioFixEAPath%

echo Running sound insertion .bat.

call %generatedSoundExchangeBatPath%

echo Running EA priority fix.

cd %~dp0EventAssembler

ColorzCore A FE8 -output:%~dp0%outputHackWithMusicPath% -input:%~dp0%soundPrioFixEAPath% --build-times

cd %~dp0

echo Running ups.

cd "%~dp0Tools/ups"

ups diff -b %~dp0%cleanFE8RomPath% -m %~dp0%outputHackWithMusicPath% -o %~dp0%outputHackWithMusicPath%.ups

pause