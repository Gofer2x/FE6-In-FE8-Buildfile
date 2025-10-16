#include "C_Code.h" // headers 

//Most of this code proudly stolen from LeadershipFunctions.c of the Leadership Stars hack by Zeta/Gilgamesh

#define MAX_RED_UNITS 50

extern struct Unit gUnitArrayRed[];

void ApplyBonusLevelsToEnemyArmy()
{
	u8 levelAmount = gEventSlots[0x1];
	struct Unit* unitArray = gUnitArrayRed;

	// go through the unit array for the appropriate faction
	for (int x = 0; x < MAX_RED_UNITS; x++)
	{
		// make sure the unit is alive
		if (unitArray[x].pCharacterData != NULL && !(unitArray[x].state & US_UNAVAILABLE))
		{
			UnitApplyBonusLevels(unitArray+x, levelAmount);
		}
	}
}