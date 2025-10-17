#include "C_Code.h" // headers 

void ApplyBonusLevelsToUnit()
{
	UnitApplyBonusLevels(GetUnitStructFromEventParameter(gEventSlots[0x1]), gEventSlots[0x2]);
}