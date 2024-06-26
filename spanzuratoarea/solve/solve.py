from z3 import *

flag = [BitVec('flag[%d]' % i, 8) for i in range(51)]

s = Solver()

s.add((flag[2] ^ 27) ^ flag[3] == 29 )
s.add((flag[3] ^ 91) ^ flag[27] == 118 )
s.add(((flag[13] >> 3) * (flag[16] << 2)) == 2736 )
s.add(((flag[10] >> 1) * (flag[15] << 2)) == 21996 )
s.add((flag[45] * flag[13]) == 5200 )
s.add(((flag[38] >> 3) * (flag[39] << 3)) == 5472 )
s.add((flag[18] & flag[50]) == 93 )
s.add((flag[46] + flag[6]) == 165 )
s.add(((flag[31] >> 7) & 29) == 0 )
s.add((flag[20] * flag[6]) == 5814 )
s.add((flag[14] & 125) == 116 )
s.add((flag[23] + flag[38]) == 104 )
s.add((flag[49] & flag[0]) == 0 )
s.add(((flag[17] >> 4) & 249) == 1 )
s.add((flag[17] * flag[7]) == 2548 )
s.add((flag[15] ^ 78) ^ flag[28] == 15 )
s.add(((flag[35] >> 3) * (flag[27] << 2)) == 4840 )
s.add(((flag[30] >> 1) * (flag[15] << 3)) == 50544 )
s.add((flag[3] * flag[39]) == 7638 )
s.add(((flag[28] >> 1) * (flag[21] << 3)) == 19760 )
s.add((flag[19] + flag[48]) == 151 )
s.add(((flag[28] >> 2) * (flag[0] << 2)) == 3796 )
s.add((flag[24] - flag[37]) == 40 )
s.add((flag[48] ^ 194) ^ flag[13] == 197 )
s.add(((flag[23] >> 2) & 127) == 13 )
s.add((flag[41] + flag[45]) == 197 )
s.add((flag[11] - flag[48]) == 1 )
s.add((flag[36] - flag[31]) == -65 )
s.add((flag[42] * flag[9]) == 5995 )
s.add((flag[17] - flag[31]) == -68 )
s.add(((flag[22] >> 3) * (flag[17] << 2)) == 1176 )
s.add((flag[30] ^ 133) ^ flag[39] == 154 )
s.add((flag[43] - flag[47]) == -46 )
s.add((flag[20] * flag[44]) == 4845 )
s.add((flag[28] + flag[18]) == 147 )
s.add((flag[36] * flag[7]) == 2704 )
s.add((flag[16] * flag[8]) == 5586 )
s.add(((flag[46] >> 2) * (flag[40] << 3)) == 10560 )
s.add((flag[15] & flag[35]) == 85 )
s.add((flag[42] & flag[45]) == 36 )
s.add(((flag[27] >> 4) & 25) == 0 )
s.add((flag[48] + flag[40]) == 161 )
s.add((flag[2] ^ 77) ^ flag[20] == 59 )
s.add(((flag[22] >> 1) & 117) == 17 )
s.add((flag[42] * flag[13]) == 2860 )
s.add((flag[27] & 165) == 36 )
s.add(((flag[43] >> 2) * (flag[17] << 3)) == 4704 )
s.add((flag[23] + flag[49]) == 104 )
s.add((flag[1] ^ 86) ^ flag[50] == 127 )
s.add((flag[32] + flag[31]) == 231 )
s.add((flag[48] * flag[15]) == 5967 )
s.add(((flag[41] >> 1) * (flag[44] << 3)) == 36480 )
s.add(((flag[29] >> 1) & 11) == 11 )
s.add((flag[33] ^ 13) ^ flag[34] == 81 )
s.add((flag[41] ^ 115) ^ flag[38] == 38 )
s.add((flag[6] - flag[44]) == 19 )
s.add((flag[4] ^ 149) ^ flag[18] == 177 )
s.add((flag[8] + flag[47]) == 144 )
s.add((flag[18] & 241) == 81 )
s.add((flag[7] & 32) == 32 )
s.add(((flag[18] >> 2) & 10) == 2 )
s.add(((flag[22] >> 5) & 91) == 1 )
s.add((flag[1] & 18) == 16 )
s.add((flag[27] - flag[48]) == 59 )
s.add((flag[37] - flag[18]) == -40 )
s.add((flag[13] & 21) == 20 )
s.add((flag[36] & flag[18]) == 20 )
s.add((flag[41] - flag[5]) == -19 )
s.add((flag[8] + flag[15]) == 166 )
s.add((flag[48] & flag[25]) == 48 )
s.add((flag[40] & 138) == 10 )
s.add((flag[27] - flag[3]) == 43 )
s.add((flag[29] & 189) == 29 )
s.add((flag[29] & flag[43]) == 17 )
s.add((flag[6] & flag[39]) == 114 )
s.add((flag[5] & flag[14]) == 116 )
s.add((flag[31] & 205) == 69 )
s.add((flag[27] & 68) == 68 )
s.add(((flag[44] >> 6) & 18) == 0 )
s.add(((flag[29] >> 3) * (flag[4] << 3)) == 10824 )
s.add((flag[50] & flag[20]) == 49 )
s.add(((flag[29] >> 3) & 183) == 3 )
s.add(((flag[24] >> 1) & 206) == 14 )
s.add(((flag[15] >> 1) * (flag[50] << 2)) == 29000 )
s.add(((flag[47] >> 2) * (flag[42] << 2)) == 5060 )
s.add(((flag[13] >> 1) * (flag[24] << 1)) == 4940 )
s.add(((flag[39] >> 7) & 192) == 0 )
s.add(((flag[23] >> 2) * (flag[40] << 3)) == 11440 )
s.add(((flag[13] >> 1) * (flag[47] << 1)) == 4940 )
s.add(((flag[38] >> 1) * (flag[44] << 2)) == 9880 )
s.add(((flag[29] >> 1) & 103) == 39 )
s.add(((flag[15] >> 5) & 66) == 2 )
s.add(((flag[1] >> 6) & 107) == 1 )
s.add(((flag[27] >> 2) * (flag[28] << 1)) == 2808 )
s.add(((flag[19] >> 4) & 228) == 4 )
s.add(((flag[37] >> 6) & 29) == 0 )
s.add(((flag[3] >> 3) * (flag[40] << 1)) == 1760 )
s.add(((flag[47] >> 7) & 123) == 0 )
s.add(((flag[21] >> 1) * (flag[19] << 3)) == 37600 )
s.add(((flag[35] >> 1) * (flag[17] << 3)) == 18424 )
s.add(((flag[0] >> 1) * (flag[26] << 3)) == 14976 )
s.add(((flag[5] >> 7) & 82) == 0 )
s.add(((flag[34] >> 1) & 163) == 34 )
s.add(((flag[21] >> 1) * (flag[16] << 2)) == 21432 )
s.add(((flag[38] >> 1) & 153) == 24 )
s.add(((flag[41] >> 7) & 222) == 0 )
s.add(((flag[35] >> 4) & 117) == 5 )
s.add(((flag[2] >> 1) * (flag[44] << 1)) == 6460 )
s.add(((flag[8] >> 5) & 123) == 1 )
s.add(((flag[29] >> 4) & 108) == 4 )
s.add(((flag[27] >> 5) & 88) == 0 )
s.add(((flag[10] >> 4) & 112) == 0 )
s.add(((flag[6] >> 3) & 127) == 14 )
s.add(((flag[14] >> 4) & 140) == 4 )
s.add(((flag[34] >> 2) * (flag[44] << 3)) == 20520 )
s.add(((flag[29] >> 2) & 40) == 0 )
s.add(((flag[17] >> 2) & 93) == 12 )
s.add(((flag[1] >> 4) & 128) == 0 )
s.add(((flag[41] >> 3) & 196) == 4 )
s.add(((flag[13] >> 2) & 158) == 12 )
s.add(((flag[9] >> 3) & 197) == 5 )
s.add(((flag[22] >> 1) * (flag[23] << 1)) == 2600 )
s.add(((flag[28] >> 3) * (flag[17] << 3)) == 2352 )
s.add(((flag[25] >> 3) * (flag[32] << 1)) == 3192 )
s.add(((flag[40] >> 2) & 222) == 26 )
s.add(((flag[19] >> 1) * (flag[48] << 2)) == 10200 )
s.add(((flag[5] >> 2) & 155) == 25 )
s.add(((flag[36] >> 1) * (flag[22] << 1)) == 2652 )
s.add(((flag[31] >> 3) * (flag[15] << 2)) == 6552 )
s.add(((flag[30] >> 7) & 178) == 0 )
s.add(((flag[0] >> 7) & 50) == 0 )
s.add(((flag[6] >> 7) & 175) == 0 )
s.add(((flag[31] >> 5) & 109) == 1 )
s.add(((flag[0] >> 2) * (flag[46] << 3)) == 7344 )
s.add(((flag[46] >> 4) & 17) == 1 )
s.add(((flag[38] >> 7) & 179) == 0 )
s.add(((flag[24] >> 2) * (flag[11] << 2)) == 4784 )
s.add(((flag[8] >> 3) * (flag[41] << 1)) == 1164 )
s.add(((flag[47] >> 6) & 227) == 1 )
s.add(((flag[7] >> 2) * (flag[26] << 3)) == 5408 )
s.add(((flag[35] >> 3) * (flag[43] << 1)) == 1078 )
s.add(((flag[19] >> 2) & 135) == 1 )
s.add(((flag[21] >> 6) & 55) == 1 )
s.add(((flag[27] >> 1) & 57) == 49 )
s.add(((flag[50] >> 2) & 120) == 24 )
s.add(((flag[43] >> 3) * (flag[48] << 3)) == 2448 )
s.add(((flag[6] >> 4) & 89) == 1 )
s.add(((flag[29] >> 2) * (flag[19] << 2)) == 9200 )
s.add(((flag[36] >> 7) & 238) == 0 )
s.add(((flag[16] >> 1) & 70) == 0 )
s.add(((flag[3] >> 6) & 134) == 0 )
s.add(((flag[19] >> 3) & 82) == 0 )
s.add(((flag[28] >> 2) * (flag[8] << 2)) == 2548 )
s.add(((flag[48] >> 7) & 120) == 0 )
s.add(((flag[22] >> 2) & 169) == 8 )
s.add(((flag[48] >> 2) * (flag[1] << 2)) == 4032 )
s.add(((flag[34] >> 1) & 182) == 54 )
s.add(((flag[15] >> 3) * (flag[8] << 3)) == 5488 )
s.add(((flag[38] >> 4) & 20) == 0 )
s.add(((flag[30] >> 1) * (flag[42] << 3)) == 23760 )
s.add(((flag[6] >> 6) & 80) == 0 )
s.add(((flag[43] >> 6) & 139) == 0 )
s.add(((flag[28] >> 5) & 1) == 1 )
s.add(((flag[6] >> 3) * (flag[14] << 3)) == 12992 )
s.add(((flag[22] >> 2) * (flag[48] << 3)) == 4896 )
s.add(((flag[26] >> 2) & 237) == 13 )
s.add(((flag[33] >> 3) * (flag[5] << 1)) == 1392 )
s.add(((flag[15] >> 7) & 37) == 0 )
s.add(((flag[14] >> 2) & 95) == 29 )
s.add(((flag[28] >> 3) * (flag[30] << 2)) == 2616 )
s.add(((flag[12] >> 6) & 179) == 1 )
s.add(((flag[32] >> 3) & 141) == 12 )
s.add(((flag[28] >> 3) & 200) == 0 )
s.add(((flag[3] >> 3) * (flag[34] << 3)) == 6976 )
s.add(((flag[9] >> 7) & 142) == 0 )
s.add(((flag[40] >> 2) * (flag[44] << 1)) == 5130 )
s.add(((flag[18] >> 1) * (flag[30] << 1)) == 10246 )
s.add(((flag[2] >> 2) * (flag[47] << 3)) == 12920 )
s.add(((flag[18] >> 1) & 185) == 41 )
s.add(((flag[27] >> 2) * (flag[37] << 2)) == 5940 )
s.add(((flag[46] >> 7) & 146) == 0 )
s.add(((flag[30] >> 2) & 67) == 3 )
s.add(((flag[24] >> 5) & 52) == 0 )
s.add(((flag[26] >> 3) * (flag[16] << 2)) == 2736 )
s.add(((flag[11] >> 3) * (flag[49] << 2)) == 1248 )
s.add(((flag[5] >> 3) & 65) == 0 )
s.add(((flag[15] >> 2) & 46) == 12 )
s.add(((flag[6] >> 3) * (flag[9] << 3)) == 12208 )
s.add(((flag[17] >> 6) & 105) == 0 )
s.add(((flag[20] >> 3) * (flag[25] << 2)) == 2688 )
s.add(((flag[48] >> 3) & 15) == 6 )
s.add(((flag[2] >> 6) & 102) == 0 )
s.add(((flag[48] >> 1) & 200) == 8 )
s.add(((flag[36] >> 2) * (flag[0] << 3)) == 7592 )
s.add(((flag[5] >> 6) & 245) == 1 )
s.add(((flag[34] >> 6) & 127) == 1 )
s.add(((flag[11] >> 3) * (flag[22] << 2)) == 1224 )
s.add(((flag[21] >> 1) & 61) == 45 )
s.add(((flag[46] >> 2) * (flag[9] << 1)) == 2616 )
s.add(((flag[21] >> 1) * (flag[7] << 3)) == 19552 )
s.add(((flag[37] >> 7) & 71) == 0 )
s.add(((flag[38] >> 3) & 149) == 4 )
s.add(((flag[50] >> 2) * (flag[30] << 3)) == 27032 )
s.add(((flag[23] >> 6) & 132) == 0 )
s.add(((flag[30] >> 4) & 162) == 2 )
s.add(((flag[28] >> 7) & 217) == 0 )
s.add(((flag[24] >> 3) * (flag[3] << 3)) == 5896 )
s.add(((flag[3] >> 1) * (flag[1] << 3)) == 22176 )
s.add(((flag[27] >> 3) * (flag[17] << 3)) == 5096 )
s.add(((flag[3] >> 3) & 199) == 0 )
s.add(((flag[15] >> 3) * (flag[28] << 2)) == 2912 )
s.add(((flag[11] >> 3) & 140) == 4 )
s.add(((flag[33] >> 1) * (flag[40] << 3)) == 21120 )
s.add(((flag[24] >> 1) * (flag[12] << 1)) == 10152 )
s.add(((flag[32] >> 2) * (flag[33] << 1)) == 2744 )
s.add(((flag[15] >> 7) & 127) == 0 )
s.add(((flag[46] >> 2) * (flag[17] << 1)) == 1176 )
s.add(((flag[32] >> 1) * (flag[3] << 3)) == 30552 )
s.add(((flag[7] >> 2) & 227) == 1 )
s.add(((flag[1] >> 6) & 244) == 0 )
s.add(((flag[42] >> 3) * (flag[0] << 2)) == 1752 )
s.add(((flag[12] >> 1) * (flag[45] << 2)) == 21600 )
s.add(((flag[16] >> 2) * (flag[43] << 3)) == 10976 )
s.add(((flag[17] >> 2) * (flag[38] << 2)) == 2496 )
s.add(((flag[11] >> 4) & 171) == 3 )
s.add(((flag[2] >> 2) & 43) == 1 )
s.add(((flag[39] >> 3) * (flag[46] << 2)) == 2856 )
s.add(((flag[33] >> 1) * (flag[0] << 2)) == 7008 )
s.add(((flag[32] >> 2) & 72) == 8 )
s.add(((flag[33] >> 2) & 30) == 12 )
s.add(((flag[18] >> 5) & 206) == 2 )
s.add(((flag[1] >> 3) * (flag[44] << 3)) == 7600 )
s.add(((flag[6] >> 4) & 56) == 0 )
s.add(((flag[39] >> 1) & 197) == 1 )
s.add(((flag[15] >> 5) & 56) == 0 )
s.add(((flag[14] >> 2) * (flag[17] << 1)) == 2842 )
s.add(((flag[3] >> 2) * (flag[25] << 3)) == 14336 )
s.add(((flag[48] >> 1) * (flag[0] << 2)) == 7300 )
s.add(((flag[19] >> 2) & 237) == 9 )
s.add(((flag[12] >> 6) & 36) == 0 )
s.add(((flag[12] >> 7) & 156) == 0 )
s.add(((flag[38] >> 1) * (flag[25] << 3)) == 23296 )
s.add(((flag[41] >> 3) & 162) == 0 )
s.add(((flag[20] >> 5) & 19) == 1 )
s.add(((flag[36] >> 3) * (flag[22] << 3)) == 2448 )
s.add(((flag[10] >> 7) & 31) == 0 )
s.add(((flag[3] >> 5) & 86) == 2 )
s.add(((flag[29] >> 1) * (flag[8] << 1)) == 4606 )
s.add(((flag[47] >> 2) * (flag[6] << 3)) == 20976 )
s.add(((flag[10] >> 2) * (flag[23] << 3)) == 9568 )
s.add(((flag[17] >> 3) & 154) == 2 )
s.add(((flag[4] >> 3) * (flag[37] << 2)) == 3300 )
s.add(((flag[44] >> 2) * (flag[3] << 3)) == 12328 )
s.add(((flag[10] >> 3) & 239) == 11 )
s.add(((flag[15] >> 2) & 16) == 16 )
s.add(((flag[0] >> 3) & 219) == 9 )
s.add(((flag[10] >> 2) * (flag[46] << 1)) == 2346 )
s.add(((flag[39] >> 2) * (flag[35] << 1)) == 5320 )
s.add(((flag[21] >> 6) & 115) == 1 )
s.add(((flag[24] >> 4) & 16) == 0 )
s.add(((flag[41] >> 3) & 239) == 12 )
s.add(((flag[8] >> 6) & 56) == 0 )
s.add(((flag[30] >> 4) & 47) == 6 )
s.add(((flag[20] >> 4) & 107) == 3 )
s.add(((flag[27] >> 1) * (flag[28] << 1)) == 5720 )
s.add(((flag[43] >> 4) & 182) == 2 )
s.add(((flag[40] >> 5) & 173) == 1 )
s.add(((flag[7] >> 3) * (flag[14] << 1)) == 1392 )
s.add(((flag[6] >> 4) & 110) == 6 )
s.add(((flag[3] >> 3) * (flag[1] << 2)) == 2688 )
s.add(((flag[18] >> 7) & 34) == 0 )
s.add(((flag[46] >> 2) * (flag[34] << 3)) == 10464 )
s.add(((flag[41] >> 3) * (flag[36] << 1)) == 1248 )
s.add(((flag[39] >> 4) & 16) == 0 )
s.add(((flag[11] >> 3) & 135) == 6 )
s.add(((flag[32] >> 3) * (flag[33] << 3)) == 5488 )
s.add(((flag[2] >> 4) & 76) == 4 )
s.add(((flag[7] >> 5) & 245) == 1 )
s.add(((flag[42] >> 7) & 57) == 0 )
s.add(((flag[40] >> 4) & 160) == 0 )
s.add(((flag[9] >> 5) & 87) == 3 )
s.add(((flag[8] >> 5) & 31) == 1 )
s.add(((flag[42] >> 6) & 80) == 0 )
s.add(((flag[34] >> 2) * (flag[18] << 3)) == 20520 )
s.add(((flag[32] >> 5) & 104) == 0 )
s.add(((flag[26] >> 5) & 161) == 1 )
s.add(((flag[50] >> 6) & 17) == 1 )
s.add(((flag[8] >> 4) & 98) == 2 )
s.add(((flag[26] >> 7) & 83) == 0 )
s.add(((flag[12] >> 7) & 208) == 0 )
s.add(((flag[45] >> 5) & 83) == 3 )
s.add(((flag[1] >> 2) * (flag[15] << 2)) == 9828 )
s.add(((flag[21] >> 3) & 63) == 11 )
s.add(((flag[2] >> 1) * (flag[21] << 2)) == 12920 )
s.add(((flag[44] >> 4) & 101) == 5 )
s.add(((flag[25] >> 2) * (flag[31] << 2)) == 13104 )
s.add(((flag[34] >> 1) * (flag[33] << 1)) == 5292 )
s.add(((flag[49] >> 2) & 71) == 5 )
s.add(((flag[29] >> 1) * (flag[50] << 2)) == 23500 )
s.add(((flag[48] >> 3) * (flag[35] << 2)) == 2280 )
s.add(((flag[6] >> 1) * (flag[27] << 1)) == 12540 )
s.add(((flag[0] >> 3) * (flag[7] << 3)) == 3744 )
s.add(((flag[12] >> 3) * (flag[32] << 2)) == 5928 )
s.add(((flag[6] >> 3) * (flag[19] << 1)) == 2800 )
s.add(((flag[7] >> 5) & 223) == 1 )
s.add(((flag[37] >> 4) & 149) == 1 )
s.add(((flag[43] >> 2) * (flag[40] << 3)) == 10560 )
s.add(((flag[33] >> 2) & 37) == 4 )
s.add(((flag[50] >> 7) & 166) == 0 )
s.add(((flag[24] >> 2) & 89) == 17 )
s.add(((flag[8] >> 1) * (flag[48] << 3)) == 9792 )
s.add(((flag[44] >> 2) & 26) == 18 )
s.add(((flag[27] >> 2) & 213) == 17 )
s.add(((flag[5] >> 2) * (flag[31] << 1)) == 6786 )
s.add(((flag[25] >> 3) * (flag[1] << 1)) == 2352 )
s.add(((flag[27] >> 2) * (flag[30] << 3)) == 23544 )
s.add(((flag[3] >> 4) & 205) == 4 )
s.add(((flag[12] >> 1) & 141) == 4 )
s.add(((flag[31] >> 3) & 255) == 14 )
s.add(((flag[39] >> 3) * (flag[3] << 2)) == 3752 )
s.add(((flag[19] >> 3) * (flag[23] << 1)) == 1248 )
s.add(((flag[1] >> 2) * (flag[47] << 2)) == 7980 )
s.add(((flag[34] >> 2) * (flag[38] << 2)) == 5616 )
s.add(((flag[23] >> 1) & 199) == 2 )
s.add(((flag[17] >> 3) & 86) == 6 )
s.add(((flag[28] >> 6) & 135) == 0 )
s.add(((flag[5] >> 1) * (flag[22] << 2)) == 11832 )
s.add(((flag[6] >> 6) & 186) == 0 )
s.add(((flag[28] >> 6) & 90) == 0 )
s.add(((flag[15] >> 7) & 23) == 0 )
s.add(((flag[31] >> 5) & 234) == 2 )
s.add(((flag[27] >> 3) & 16) == 0 )
s.add(((flag[11] >> 3) * (flag[38] << 3)) == 2496 )
s.add(((flag[20] >> 7) & 44) == 0 )
s.add(((flag[25] >> 2) & 180) == 20 )
s.add(((flag[26] >> 3) * (flag[5] << 1)) == 1392 )
s.add(((flag[22] >> 3) * (flag[39] << 3)) == 5472 )
s.add(((flag[37] >> 5) & 71) == 1 )
s.add(((flag[23] >> 3) & 75) == 2 )
s.add(((flag[13] >> 1) * (flag[22] << 3)) == 10608 )
s.add(((flag[34] >> 2) * (flag[10] << 1)) == 5130 )
s.add(((flag[17] >> 1) & 163) == 0 )
s.add(((flag[5] >> 2) & 158) == 28 )
s.add(((flag[2] >> 6) & 163) == 1 )
s.add(((flag[9] >> 2) * (flag[29] << 3)) == 20520 )
s.add(((flag[21] >> 2) * (flag[23] << 3)) == 9568 )
s.add(((flag[41] >> 3) & 158) == 12 )
s.add(((flag[43] >> 2) & 161) == 0 )
s.add(((flag[22] >> 5) & 80) == 0 )
s.add(((flag[48] >> 6) & 109) == 0 )
s.add(((flag[48] >> 2) * (flag[32] << 1)) == 2736 )
s.add(((flag[33] >> 3) & 217) == 0 )
s.add(((flag[49] >> 1) * (flag[7] << 3)) == 10816 )
s.add(((flag[37] >> 2) & 172) == 12 )
s.add(((flag[11] >> 3) & 173) == 4 )
s.add(((flag[33] >> 3) * (flag[46] << 2)) == 1224 )
s.add(((flag[42] >> 3) * (flag[29] << 2)) == 2280 )
s.add(((flag[45] >> 4) & 178) == 2 )
s.add(((flag[23] >> 7) & 212) == 0 )
s.add(((flag[2] >> 3) * (flag[42] << 1)) == 880 )
s.add(((flag[13] >> 3) * (flag[31] << 1)) == 1404 )
s.add(((flag[6] >> 2) & 213) == 20 )
s.add(((flag[21] >> 3) * (flag[1] << 2)) == 3696 )
s.add(((flag[12] >> 2) * (flag[39] << 1)) == 6156 )
s.add(((flag[2] >> 3) * (flag[48] << 3)) == 3264 )
s.add(((flag[20] >> 1) * (flag[6] << 1)) == 5700 )
s.add(((flag[47] >> 1) * (flag[9] << 1)) == 10246 )
s.add(((flag[24] >> 4) & 229) == 5 )
s.add(((flag[12] >> 1) * (flag[37] << 1)) == 5940 )
s.add(((flag[33] >> 3) * (flag[30] << 1)) == 1308 )
s.add(((flag[2] >> 6) & 4) == 0 )
s.add(((flag[20] >> 3) & 17) == 0 )
s.add(((flag[16] >> 1) * (flag[21] << 3)) == 43320 )
s.add(((flag[5] >> 1) * (flag[8] << 3)) == 22736 )
s.add(((flag[15] >> 2) * (flag[12] << 3)) == 25056 )
s.add(((flag[23] >> 1) * (flag[32] << 1)) == 5928 )
s.add(((flag[32] >> 5) & 224) == 0 )
s.add(((flag[25] >> 7) & 18) == 0 )
s.add(((flag[20] >> 5) & 37) == 1 )
s.add(((flag[40] >> 4) & 203) == 2 )
s.add(((flag[14] >> 1) * (flag[35] << 1)) == 11020 )
s.add(((flag[13] >> 1) * (flag[8] << 3)) == 10192 )
s.add(((flag[37] >> 1) & 86) == 18 )
s.add(((flag[3] >> 4) & 210) == 0 )
s.add(((flag[32] >> 2) & 188) == 28 )
s.add(((flag[7] >> 1) & 177) == 16 )
s.add(((flag[0] >> 2) * (flag[46] << 1)) == 1836 )
s.add(((flag[43] >> 3) * (flag[15] << 2)) == 2808 )
s.add(((flag[34] >> 4) & 10) == 2 )
s.add(((flag[33] >> 6) & 21) == 0 )
s.add(((flag[31] >> 5) & 195) == 3 )
s.add(((flag[39] >> 1) * (flag[42] << 1)) == 6270 )
s.add(((flag[45] >> 4) & 22) == 6 )
s.add(((flag[50] >> 3) & 40) == 8 )
s.add(((flag[26] >> 7) & 247) == 0 )
s.add(((flag[32] >> 3) & 98) == 2 )
s.add(((flag[49] >> 1) * (flag[33] << 3)) == 10192 )
s.add(((flag[25] >> 2) & 52) == 20 )
s.add(((flag[2] >> 5) & 222) == 2 )
s.add(((flag[36] >> 2) & 36) == 4 )
s.add(((flag[41] >> 7) & 139) == 0 )
s.add(((flag[0] >> 2) * (flag[35] << 3)) == 13680 )
s.add(((flag[31] >> 6) & 35) == 1 )
s.add(((flag[44] >> 5) & 42) == 2 )
s.add(((flag[26] >> 1) & 149) == 16 )
s.add(((flag[28] >> 5) & 143) == 1 )
s.add(((flag[47] >> 4) & 111) == 5 )
s.add(((flag[35] >> 1) & 56) == 40 )
s.add(((flag[41] >> 1) * (flag[50] << 1)) == 12000 )
s.add(((flag[31] >> 3) * (flag[6] << 3)) == 12768 )
s.add(((flag[50] >> 1) * (flag[31] << 2)) == 29016 )
s.add(((flag[40] >> 3) & 99) == 1 )
s.add(((flag[11] >> 1) * (flag[40] << 2)) == 11440 )
s.add(((flag[30] >> 7) & 117) == 0 )
s.add(((flag[48] >> 2) & 26) == 8 )
s.add(((flag[35] >> 3) * (flag[47] << 1)) == 2090 )
s.add(((flag[34] >> 2) & 72) == 8 )
s.add(((flag[22] >> 6) & 35) == 0 )
s.add(((flag[27] >> 3) * (flag[0] << 2)) == 3796 )
s.add(((flag[2] >> 2) * (flag[49] << 3)) == 7072 )
s.add(((flag[13] >> 2) & 172) == 12 )
s.add(((flag[13] >> 1) & 142) == 10 )
s.add(((flag[9] >> 3) & 106) == 8 )
s.add(((flag[11] >> 2) * (flag[23] << 2)) == 2704 )
s.add(((flag[31] >> 5) & 136) == 0 )
s.add(((flag[48] >> 3) * (flag[22] << 1)) == 612 )
s.add(((flag[19] >> 5) & 198) == 2 )
s.add(((flag[32] >> 2) & 155) == 24 )
s.add(((flag[1] >> 3) * (flag[34] << 3)) == 8720 )
s.add(((flag[45] >> 1) * (flag[2] << 2)) == 13800 )
s.add(((flag[34] >> 7) & 135) == 0 )
s.add(((flag[41] >> 3) & 129) == 0 )
s.add(((flag[9] >> 3) * (flag[23] << 3)) == 5408 )
s.add(((flag[19] >> 4) & 163) == 2 )
s.add(((flag[19] >> 2) & 31) == 25 )
s.add(((flag[23] >> 2) & 4) == 4 )
s.add(((flag[12] >> 1) & 195) == 2 )
s.add(((flag[46] >> 1) & 240) == 16 )
s.add(((flag[29] >> 2) * (flag[13] << 2)) == 4784 )
s.add(((flag[11] >> 3) & 247) == 6 )
s.add(((flag[25] >> 2) * (flag[12] << 2)) == 12096 )
s.add(((flag[3] >> 2) * (flag[46] << 1)) == 1632 )
s.add(((flag[25] >> 2) * (flag[45] << 2)) == 11200 )
s.add(((flag[9] >> 3) * (flag[23] << 2)) == 2704 )
s.add(((flag[46] >> 2) * (flag[4] << 1)) == 2952 )
s.add(((flag[21] >> 3) * (flag[15] << 1)) == 2574 )
s.add(((flag[12] >> 1) * (flag[42] << 2)) == 11880 )
s.add(((flag[10] >> 6) & 206) == 0 )
s.add(((flag[26] >> 2) * (flag[1] << 2)) == 4368 )
s.add(((flag[27] >> 2) & 240) == 16 )
s.add(((flag[44] >> 3) * (flag[24] << 2)) == 4180 )
s.add(((flag[10] >> 7) & 97) == 0 )
s.add(((flag[21] >> 2) * (flag[8] << 3)) == 9016 )
s.add(((flag[11] >> 5) & 72) == 0 )
s.add(((flag[13] >> 1) * (flag[47] << 1)) == 4940 )
s.add(((flag[12] >> 1) * (flag[4] << 3)) == 53136 )
s.add(((flag[32] >> 6) & 75) == 1 )
s.add(((flag[1] >> 1) * (flag[16] << 1)) == 9576 )
s.add(((flag[23] >> 2) & 81) == 1 )
s.add(((flag[29] >> 3) & 25) == 9 )
s.add(((flag[45] >> 2) * (flag[2] << 1)) == 3450 )
s.add(((flag[47] >> 4) & 246) == 4 )
s.add(((flag[46] >> 2) & 100) == 4 )
s.add(((flag[3] >> 1) & 103) == 33 )
s.add(((flag[34] >> 3) & 34) == 0 )
s.add(((flag[28] >> 2) * (flag[0] << 2)) == 3796 )
s.add(((flag[41] >> 1) & 158) == 16 )
s.add(((flag[10] >> 3) * (flag[7] << 2)) == 2288 )
s.add(((flag[42] >> 5) & 22) == 0 )
s.add(((flag[12] >> 3) & 188) == 12 )
s.add(((flag[12] >> 7) & 230) == 0 )
s.add(((flag[11] >> 7) & 172) == 0 )
s.add(((flag[31] >> 7) & 47) == 0 )
s.add(((flag[48] >> 7) & 85) == 0 )
s.add(((flag[20] >> 1) * (flag[21] << 3)) == 19000 )
s.add(((flag[24] >> 2) & 60) == 20 )
s.add(((flag[10] >> 5) & 77) == 0 )
s.add(((flag[32] >> 3) * (flag[17] << 3)) == 5488 )
s.add(((flag[47] >> 5) & 241) == 0 )
s.add(((flag[19] >> 4) & 209) == 0 )
s.add(((flag[11] >> 3) * (flag[47] << 1)) == 1140 )
s.add(((flag[9] >> 1) * (flag[10] << 3)) == 41040 )
s.add(((flag[9] >> 1) * (flag[13] << 1)) == 5616 )
s.add(((flag[49] >> 1) * (flag[40] << 2)) == 11440 )
s.add(((flag[3] >> 1) & 159) == 1 )
s.add(((flag[13] >> 2) * (flag[34] << 2)) == 5668 )
s.add(((flag[37] >> 2) & 241) == 1 )
s.add(((flag[42] >> 1) & 79) == 11 )
s.add(((flag[24] >> 1) * (flag[42] << 1)) == 5170 )
s.add(((flag[46] >> 2) * (flag[14] << 1)) == 2784 )
s.add(((flag[39] >> 6) & 105) == 1 )
s.add(((flag[7] >> 1) & 235) == 10 )
s.add(((flag[38] >> 3) * (flag[44] << 3)) == 4560 )
s.add(((flag[8] >> 2) & 104) == 8 )
s.add(((flag[12] >> 5) & 124) == 0 )
s.add(((flag[22] >> 1) & 158) == 24 )
s.add(((flag[34] >> 3) * (flag[3] << 2)) == 3484 )
s.add(((flag[1] >> 4) & 27) == 1 )
s.add(((flag[11] >> 3) & 136) == 0 )
s.add(((flag[13] >> 2) * (flag[11] << 1)) == 1352 )
s.add(((flag[49] >> 1) * (flag[31] << 1)) == 6084 )
s.add(((flag[28] >> 2) * (flag[46] << 3)) == 5304 )
s.add(((flag[15] >> 3) & 180) == 4 )
s.add(((flag[41] >> 5) & 242) == 2 )
s.add(((flag[50] >> 5) & 52) == 0 )
s.add(((flag[37] >> 3) * (flag[46] << 3)) == 2448 )
s.add(((flag[19] >> 4) & 44) == 4 )
s.add(((flag[38] >> 1) * (flag[6] << 3)) == 23712 )
s.add(((flag[44] >> 1) * (flag[18] << 2)) == 17860 )
s.add(((flag[7] >> 4) & 97) == 1 )
s.add(((flag[26] >> 7) & 70) == 0 )
s.add(((flag[49] >> 3) * (flag[20] << 3)) == 2448 )


for i in range(51):
    s.add(flag[i] >= 32)
    s.add(flag[i] <= 126)

print(s.check())
model = s.model()
flag = ''.join([chr(int(str(model[flag[i]]))) for i in range(len(model))])
print(flag)

