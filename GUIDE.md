EA Configs
===============
The file [FE6InFE8Config.event](FE6InFE8Config.event) contains a few definitions that you can uncomment/comment out to enable and disable various behaviors (not like most of them do anything at the moment though...).

Table Readers
===============
There is a Python script ("IDsFromTables.py" in Tools/IDsFromTables) that can take the names out of the leftmost column of a Nightmare table and using Enumerate (another script) autogenerate EA definitions. It's ran on various tables through "_UpdateIDsFromTables.cmd" in the root folder, with its outputs being in Definitions/Generated.

Supports
===============
Due to engine limitations, Roy and Lilina cannot have all of their supports (they originally have 11 in FE6, but the FE8 engine has a limit of 7). There is a script to let you choose which of their supports are cut in [Tables/ExternalTables/Supports](Tables/ExternalTables/Supports).

It also supports adding new supports if you add them in the support data dict in the script itself. Just follow the naming convention of the already present vanilla supports' text data.

Mugs
===============

To insert new Mugs/Portraits, go into [Graphics/Mugs](Graphics/Mugs).

Drop your mug's png file (Have it named like "Character.png") into the "Png" folder, and run "_BatchPortraitFormatter.cmd". 
 
Afterwards, open "Mugs.csv". This is where you'll set up how your mug should be installed.
 
Add your mug's entry to the csv (the Name and Eye/Mouth X/Y fields should be obvious), but only put it after the "SecretShop" entry. Otherwise it will mess up vendor menus.
     
If your mug doesn't have a mini version, set the "NoMini" field to any non-blank value. Preferably stick to the "TRUE".
 
If it's a palette swap, set the "PalSwapOf" value to what this mug is a palette swap of.
 
When done, run "MasterMugInstallerGenerator.py". Press enter when it finishes. It will have generated all the relevant data imports, definitions, and also put the various LoadMugs into ParseDefinitions in the main Text folder (e.g. [LoadRoy], [LoadSoldier2]...).