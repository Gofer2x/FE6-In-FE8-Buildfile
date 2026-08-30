An attempt at a recreation of FE6 in FE8's engine.

Requires "FE8_clean.gba" (sha1: c25b145e37456171ada4b0d440bf88a19f4d509f) and "FE6.gba" (either original or translated will work) in the root directory.

Requires Python 3 and a copy of FEBuilderCLI (https://github.com/laqieer/FEBuilderGBA/releases) in Tools/FEBuilderGBA/CLI (or change the febCLIPath variable in "_FullSoundInsertion.bat" to wherever your FEBuilder CLI is).

To build, run "MAKE HACK_full.cmd", which will build "FE6InFE8.gba". Afterwards run "_FullSoundInsertion.bat" to build "FE6InFE8_Music.gba" (using FEBuilder's Sound Import function), which will be the proper finished ROM.

For information about how to insert new data, various helper scripts used etc. please read [GUIDE.md](GUIDE.md).

<details>

<summary>Differences compared to base FE6 (most of them at least):</summary>

*  There is a world map! No shops on it though (yet). World map cutscenes are also not implemented as of now (god they are a pain).

-  You generally will have a World Map segment before each chapter, the exceptions being:
  
    -  All gaidens, Ch8, Ch20B, Ch24.

- At the start of the game you will get several config options.
    - Casual Mode, units will come back after each chapter
    - Fixed Growths Mode, units will level perfectly to their averages
    - If enemies in Ch1-5 will have doubled HM bonuses (unintentional but vanilla FE6 behavior)
    - If most enemy units you recruit get HM bonuses (Rutger, Fir, Sin, Gonzalez, Klein, Thea, Cath, Melady, Ch15!Perceval, Garrett, Zeiss)
    - If enemy units you recruit who normally don't get HM bonuses also get them (Raigh, Ch13!Perceval, Hugh, Douglas)

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
- Some unchanged FE8 menus (map status, preparations, chapter intro...).

</details>

Credits in [CREDITS.md](CREDITS.md).

Built off [SkillSystem_FE8](https://github.com/FireEmblemUniverse/SkillSystem_FE8/).
