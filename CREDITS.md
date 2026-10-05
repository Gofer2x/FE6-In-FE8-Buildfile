Unless stated otherwise, all assets were taken from the repository.

# Battle Animations
<details>
  <summary>Inside here (long):</summary>

- "King" aka "Zephiel Dark Aura and Critical BGM Kill Fixed" made by [shadowofchaos](https://forums.serenesforest.net/topic/19553-king-zephiel-in-fe7-animation-screwup-and-fix/)

- "RogueF" aka "[Rogue-Reskin] [F] Ponytail by Temp" made by {Temp, Black Mage, Wan}

- The following are various Vanilla FE6 animations. I have only kept the ones I intend to use (e.g. no Bard weapon animations).

- "Bard" aka "[Bard-Base] [M] Elffin +Weapons"

- - "Refresh (FE6)(Bird Sfx)" by Orihara_Saki.
- - "Refresh (FE7-8)" by Eldritch Abomination.

- "Dancer" aka "[Dancer-Base] [F] Vanilla FE6 Larum +FE7-8, Staff"
- - "Refresh (Fixed SFX)" by Eldritch Abomination.
- - "Refresh (Heart FE8 Compatible)" by SHYUTERz.

- "DemonDragon" aka "[Boss-Base] [U] Vanilla FE6 Idunn +FE7-8"

- - Dragonstone (FEx, Claw Attack + Transform) by {SHYUTERz}

- "FireManakete" aka "[Manakete-Base] [F] Vanilla FE6 Fire Dragon +FE7"

- - "8. Dragonstone (FE8)" {Eldritch Abomination}
	
- "NomadTrooperF" aka "[Nomad Trooper Base] [F] Vanilla FE6 +Fix]"

- - I assume Bow fix by {ltranc, Valak}

- "MageF" aka "[Mage-Base] [F] Vanilla FE6 Lilina +Staff"

- - "Magic" by Shin19 and SHYUTERz.
	
- "Sage" aka "[Sage-Base] [M] Vanilla FE6 +Fixes"

- - "Fixed magic" by Shin19.

- "SageF" aka "[Sage-Base] [F] Vanilla FE6 Lilina +Fixes"

- - "FE8 Fixes" by SHYUTERz.

All others are by IS.
</details>


# Map sprites:

- "RogueF_SMS" AKA "Rogue (F) {Unknown}-stand" by Unknown



# Mugs/Portraits:

- All blinking mugs by {Lenh, Obsidian Daddy}
    Thea mug along with some missing/misaligned villager mugs fixed by me.

# Spell Animations:

- [Fire] Forblaze - FE8  FE6 Version {SHYUTERz}

- [Light] Aureola {SHYUTERz}

- [Dark] Apocalypse - FE8 {SHYUTERz}  1

# Scripts/Engine Hacks/Patches
<details>
  <summary>Inside here (very long, probably too long and could be better sorted)</summary>

- Death Dance (aka refresh unit when they are dropped by a rescuing ally on player phase) - Author: snow.chr https://feuniverse.us/t/snows-code-repo/29119
- 16 Tracks/12 Sounds Fix - Author: Agro/Brendor https://feuniverse.us/t/fe7-fe8-16-tracks-12-sounds-patch/895
- Allow 254 generic minimugs - Authors: Gryz, 7743 https://feuniverse.us/t/allowing-for-more-than-0x06-generic-minimugs/1085/9
- Battle Transformations - Authors: Tequila, UNKNOWN, Aera, circleseverywhere, Ported by 7743 https://feuniverse.us/t/teqs-minor-assembly-shenanigans/1655/77
- Convert Chapter Titles to Text v2.1 - Author: circleseverywhere, 7743, gamma https://feuniverse.us/t/hypergammaspaces-assorted-asm/4085/24
- Remove Enemy Control Glitch - Author: Brendor, Compatability/Ported by 7743
- Remove Pierce Glitch - Author: Brendor https://feuniverse.us/t/pierce-fix/699
- Fix CAM1/CAMERA2 going out of bounds - Author: Stan
- Fix proc names not being clearedAuthor: Stan
- Fix Weak Promoted Enemies - Author: Gryz https://feuniverse.us/t/fe7-fe8-difficulty-stat-changes/1295/3
- Enable Faster Movement By Holding A - Author: Gryz https://feuniverse.us/t/unit-movement-speed/920
- 01command_hack, 48command_hack, and Anti-Huffman - Author: Hextator, Compatability/Ported by 7743
- FillAIDangerMap Efficiency Fix 20220712 - Author: Hextator, Updated by 7743 https://feuniverse.us/t/hypergammaspaces-assorted-asm/4085/8
- Add Event: AutoLvlUnit - Author: Vesly https://feuniverse.us/t/veslys-asm/12011/14 https://github.com/Veslyquix/ASM/blob/main/AutoLevelUnits/
- AddEvent: Get the number of Count number of units in a specific range - - Author: 7743, add state suusuke
- Add Event Condition: Item Check(All units and transporters) - Author: Kaito, Compatability/Ported? by 7743
- Magic Sword Rework - Author: Sme https://feuniverse.us/t/smes-asm-and-miscellany/4445
- MultiTransformManims - Author: Eebit https://feuniverse.us/t/is-there-a-way-to-have-multiple-classes-that-transform-with-battle-anims-off/23526/2
- NarrowFont - Author: Scraiza https://feuniverse.us/t/scraizas-crazy-asm/5624/2, MintX
- Adjust Mode Coefficient Experience Gain - Author: Vennobennu, Ported by 7743 https://feuniverse.us/t/exp-formula-mode-coefficient-fix/27/2
- Autocursor Fix - Author: Vennos https://feuniverse.us/t/vennos-small-asm-hacks-and-notes/269/66
- Weapon Exp Required for (Rank) - Author: Blademaster https://feuniverse.us/t/fe8-change-required-wexp-for-next-level/7895
- Class ID of an enemy unit born from an egg - Author: Huichelaar
- Class ID that determines that the AI can use Rogue lockpick skill - Author: Kirito
- Devil Axs: The value to use when lowering the probability of self-destruction - Author: beikehanmu https://feuniverse.us/t/fe-builder-gba/2845/1738
- Don't draw portrait on item select menu if unit is generic - Author: hypergammaspaces
- Skip:Game Opening Demo - Author: Fati
- Item ID which changes to money when stolen patches - Author: v
- Extended Moving Map Animation List - Authors: Icecube https://feuniverse.us/t/max-number-of-standing-map-sprites/773/10 , Snakey1 https://feuniverse.us/t/max-number-of-standing-map-sprites/773/29
- Units after this Unit ID will Class Grow - Source: fe8 decomp project. https://feuniverse.us/t/autolevel-function/12463/2
- Summon Skill: Edit Summoned Class - Source: FE8 Summoneditor by Nintenlord, ZaneAvernathy

Following patches by Aera:
- Additional AI: Talk AI
- Remove Creature Campaign
- Hide Record (Lagdou/Valni)
- Fixed sound of Aircalibur
- Fixed sound of the Sword of the seal
- Fixed sound of Ekkesachs SongID:0x10C
- Fixed sound of Ekkesachs SongID:0x11E https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81
- Silencer-Immune Class https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81

Following patches by Tequila:
- Add Event: Set Unit State Conditions (UNCM) https://feuniverse.us/t/teqs-minor-assembly-shenanigans/1655/80
- fix_lz77decompress
- Modify S-Rank Limits
- Unlock various restrictions of chapter 5x https://feuniverse.us/t/fe-builder-gba/2845/1547

Following patches by circleseverywhere:
- CSA (Custom Spell Anims) ver2
- Toggle Health & Safety Warning https://feuniverse.us/t/fe7-8-skip-the-intro-cutscene/1225/17
- Toggle New Game Intro Cutscene https://feuniverse.us/t/fe7-8-skip-the-intro-cutscene/1225/13
- Toggle New Game Text https://feuniverse.us/t/fe7-8-skip-the-intro-cutscene/1225/13
- Eclipse Damage (1) https://feuniverse.us/t/fe6-eclipse-effect-in-fe8-answered/3602/2
- Saving in the Tower and Ruins https://feuniverse.us/t/fe8-saving-in-the-tower-of-valni-and-lagdou-ruins/1266
- Toggle New Game Music On/Of

Following patches by/from Chap@FE8_GIRLS:
- Great Shield First Class and Last Class https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81
- Slayer Skill First Class and Last Class https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81
- Sure Strike Skill First Class and Last Class
- Disabled Status Screen On Map 2 https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81
- Skill Pick https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81
- Skill Pierce from this class and to this class https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81
- Toggle World Map Monster Skirmishes https://dw.ngmansion.xyz/doku.php?id=data:%E3%83%91%E3%83%83%E3%83%81

Following patches by 7743:
- Unique Battle Music Per Unit
- AddEvent: Get Unit Status
- Add Event: Change Edition
- Add Event: Change AI of unit or class at onc
- Add Event: Change unit / class affiliation at once
- Define Multiple dancers(Battle animation effect)
- Define multiple classes that can discover desert treasures
- Simple setting of Sacred Weapons 2
- Change Effectiveness damage coefficient of the weapon
- These class force the staff to hit 0% and deactivate it
- These unit force the staff to hit 0% and deactivate 1 and 2
- Always Ranged Animate: Rune Sword, Hand Axe, Hatchet, Tomahawk
- Armor Triangle Attack Class Patches
- Change Battle BGM if Specified Item Weapon1 and 2
- Worldmap fleet icon
- Fix Glitch that self-destructs whenever an underflow bug occurs
- Item ID for which you can get money by drop patches
- Prevent Freeze For Camera Event 0x26
- Prevent Freeze For Get Unit State Event 0x33
- Fix_GenerateBestMovementScript Move Glitch
- Item ID of Lunar Brace, Solar Brace
- Item Nightmare
- Main Character - Eirika's Tale and Ephraim's Tale
- Item ID that reduces damage to 0
- Prohibits the Crit by Item _ Stone
- Special class 1 and 2 to reduce number of possessed items to zero when loading
- Special class 1 and 2 to that BadStatus A when load
- Special class 1 and 2 to that fixes HP to 5 when load
- Summoned Creature Weapon 1-4
- Eirika Campaign Supply
- Ephraim Campaign Supply
- Triangle Attack Class Promoted
- Triangle Attack Class UnPromoted
- Change Effectiveness damage coefficient of the weapon
- Sound Room 100% Unlocked

Uncredited
- allow Wyvern Knights to triangle attack
- Fix Stone's map animation crashing no$ due to a bad decompression
- Class Crit% Bonus
- Fixes the world map chapter ID being loaded instead of the actual chapter ID
- Mini Mug Portrait of carriage wagon at sale on world map
- Mini Mug Portrait of Supply carriage wagon
- fix prep screen in ch5x
- Show gold in ch5x
- Supply Unlock Prologue and Chapter 1
- Ewan Base Class For Weapon Rank Removal
- Fix CG Fade Glitch, ported by 7743
- Class that weakens the staff's hit rate without using the base value
- Forcibly defeats 0 defeat EXP.Class 1
- Forcibly defeats 0 defeat EXP.Class 2
- Set Class that prohibits additional effects such as poisons from bad status
- Demon King Multi-Summon Class
- Forcibly overwrites defeat EXP. Class1
- Class that disappears when the chapter is cleared
- Prohibits the use of Arena by Class
- All Sound Hardcoding patches
- Skip World Map Fix (Disable Skirmishes & World Map)
- Portrait Upshift Edit(or?) <- got this one from Github search but couldn't find a proper source?
</details>

* * * * *

Various scripts and macros/definitions taken from other projects. I've kept credits in ones that had them, but most of them I found from github searches and they appeared in multiple repos, so not sure how to credit them. But thank you.

Thanks to the Fire Emblem Wiki (https://fireemblemwiki.org/) for various information about specific chapters and mechanics. Ch14x's bridges, Ch16x's arrow trap timings, Ch21's reinforcement zones and more.

Also thanks to Vesly for their great .bat files for processing data, and the various people on the FEU discord for helping out when I ran into problems.
