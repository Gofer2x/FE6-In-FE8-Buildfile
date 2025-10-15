An attempt at a recreation of FE6 in FE8's engine.

Requires "FE8_clean.gba" (sha1: c25b145e37456171ada4b0d440bf88a19f4d509f) and "FE6.gba" (either original or translated will work) in the root directory.

Requires Python 3 and a copy of FEBuilder in Tools/FEBuilderGBA (or change the febPath variable in "_FullSoundInsertion.bat" to wherever your FEBuilder is).

To build, run "MAKE HACK_full.cmd", which will build "FE6InFE8.gba". Afterwards run "_FullSoundInsertion.bat" to build "FE6InFE8_Music.gba" (using FEBuilder's Sound Import function), which will be the proper finished ROM. It will take a few minutes though.

For information about how to insert new data, various helper scripts used etc. please read [GUIDE.md](GUIDE.md).

Credits in [CREDITS.md](CREDITS.md).

Built off [SkillSystem_FE8](https://github.com/FireEmblemUniverse/SkillSystem_FE8/).