#include "C_Code.h" // headers 

void UnitExpGainToC() {
    gEventSlots[0xC] = PidStatsGetExpGain(gEventSlots[0x1]);
}