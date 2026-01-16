An attempt at a recreation of FE6 in FE8's engine.

Requires "FE8_clean.gba" (sha1: c25b145e37456171ada4b0d440bf88a19f4d509f) and "FE6.gba" (either original or translated will work) in the root directory.

Requires Python 3 and a copy of FEBuilder in Tools/FEBuilderGBA (or change the febPath variable in "_FullSoundInsertion.bat" to wherever your FEBuilder is).

To build, run "MAKE HACK_full.cmd", which will build "FE6InFE8.gba". Afterwards run "_FullSoundInsertion.bat" to build "FE6InFE8_Music.gba" (using FEBuilder's Sound Import function), which will be the proper finished ROM. It will take a few minutes though.

For information about how to insert new data, various helper scripts used etc. please read [GUIDE.md](GUIDE.md).

<details>

<summary>Differences compared to base FE6:</summary>

*  There is a world map! No shops on it though (yet). World map cutscenes are also not implemented as of now (god they are a pain).

-  You generally will have a World Map segment before each chapter, the exceptions being:
  
    -  All gaidens, Ch8, Ch20B, Ch24.

- At the start of the game you can enable Casual and/or Fixed Growths modes.

-  The Trial Maps are implemented via a temple on Valor (the Dread Isle). It's unlocked after beating Ch21.
  
-  The Torch staff has its FE7/FE8 behavior.
  
-  All enemies with unique AI have more standard AI.
    -  The Ch2 gate enemies have attack-in-range AI.
    -  The Ch23 gate enemies have stationary AI.
    -  Galle and his squad have standard aggressive AI.
  
- There also might be some more minute differences in Target AI.

- The different promotion bonuses for Brigand and Pirate promoting into Berserker have been merged.
    -  FE6 Brigand -> Berserker: +4 HP, +2 STR, +5 SKL, +2 SPD, +3 DEF, +1 CON, +1 MOV, +50 Axe
    -  FE6 Pirate -> Berserker: +5 HP, +3 STR, +4 SKL, +1 SPD, +3 DEF, +3 CON, +1 MOV, +50 Axe
    -  Merged Brigand/Pirate -> Berserker: +4 HP, +3 STR, +5 SKL, +1 SPD, +3 DEF, Variable CON

- The traps in Ch21x are not implemented.
- Ch16x does not have the fancy parallax background.

</details>

Credits in [CREDITS.md](CREDITS.md).

Built off [SkillSystem_FE8](https://github.com/FireEmblemUniverse/SkillSystem_FE8/).
