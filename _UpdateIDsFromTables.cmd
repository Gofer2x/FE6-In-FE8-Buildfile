set idsFromTables="%~dp0Tools\IDsFromTables\IDsFromTables.py"
set enumerate="%~dp0Tools\Enumerate\Enumerate.py"
%idsFromTables% Tables\NightmareModules\CharactersClasses\CharacterTable.csv Definitions\Generated\CharacterIDs.event %enumerate% Character --oneIndexed
%idsFromTables% Tables\NightmareModules\CharactersClasses\ClassTable.csv Definitions\Generated\ClassIDs.event %enumerate% Class --oneIndexed --ignoreFirstItem
%idsFromTables% Tables\NightmareModules\Items\ItemTable.csv Definitions\Generated\ItemIDs.event %enumerate% Item  --oneIndexed --ignoreFirstItem
%idsFromTables% Tables\NightmareModules\ChapterData\ChapterData.csv Definitions\Generated\ChapterIDs.event %enumerate% Chapter
