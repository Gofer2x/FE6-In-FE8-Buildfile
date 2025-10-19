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

To insert new Mugs/Class Cards, go into [Graphics/MugsAndCards](Graphics/MugsAndCards).

Drop your mug's png file (Have it named like "Character.png") into the "Png" folder, and run "_BatchPortraitFormatter.cmd". ~~If inserting a card uhh just do that manually I got lazy and am reusing vanilla card data lol~~
 
Afterwards, open "MugsAndCards.csv". This is where you'll set up how your mug/card should be installed.

If you're adding a mug, set the Type field to "Mug". If it's a card, set it to "Card".

The "MouthX", "MouthY", "EyeX", and "EyeY" fields are used for mugs and should be self-explanatory.

The "NoMini" field when set to any non-blank value will not #include minimug data for a mug, instead using 0x0.
 
The "PalSwapOf" field if non-blank will install a mug as a palette swap of another mug. Only new palette data will be #included, and the others (like the graphics and frames data) will be that of the original mug.

The "ReservedID" field forces a mug/card to have a specific ID in the portrait table. This is useful for mugs with hardcoded values (e.g. vendors).

The "CardUseVanillaData" field changes a card to not #include any new data and only set the portrait table entry. Since all the class cards I need for this project are in the vanilla ROM already I implemented this to save a few kilobytes.
 
When done, run "MasterMugAndCardInstallerGenerator.py". Press enter when it finishes. It will have generated all the relevant data imports, definitions, and also put the various LoadMugs into ParseDefinitions in the main Text folder (e.g. [LoadRoy], [LoadSoldier2]...).

To change the paths of the generated definitions/parseDefs, just edit the generator script. The values are near the top.
