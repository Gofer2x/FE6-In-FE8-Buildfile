#include "C_Code.h" // headers 

void EVENTGetUnitEquippedWeapon()
{
	u8 unitID = gEventSlots[0x1];
	u8 equippedItem = GetUnitEquippedWeapon(GetUnitStructFromEventParameter(unitID));
	gEventSlots[0xC] = equippedItem;
}