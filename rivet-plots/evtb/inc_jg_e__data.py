
from numpy import nan

xpoints  = [0.035, 0.10500000000000001, 0.175, 0.245, 0.315, 0.385, 0.45499999999999996, 0.525, 0.595, 0.665, 0.735, 0.8049999999999999, 0.875, 0.9450000000000001, 1.0150000000000001, 1.085, 1.155, 1.225, 1.295, 1.365, 1.435, 1.505, 1.5750000000000002, 1.645, 1.7149999999999999, 1.7850000000000001, 1.855, 1.9249999999999998, 1.9949999999999999, 2.065, 2.135, 2.205, 2.2750000000000004, 2.3449999999999998, 2.415, 2.4850000000000003, 2.5549999999999997, 2.625, 2.6950000000000003, 2.7649999999999997, 2.835, 2.9050000000000002, 2.9749999999999996, 3.045, 3.115, 3.185, 3.255, 3.325, 3.395, 3.465, 3.535, 3.605, 3.675, 3.745, 3.815, 3.885, 3.955, 4.025, 4.095, 4.165, 4.234999999999999, 4.305, 4.375, 4.445, 4.515000000000001, 4.585, 4.655, 4.725, 4.795, 4.865, 4.9350000000000005, 5.005, 5.075, 5.145, 5.215, 5.285, 5.355, 5.425, 5.495, 5.5649999999999995, 5.635, 5.705, 5.775, 5.845, 5.915, 5.984999999999999, 6.055, 6.125, 6.195, 6.265000000000001, 6.335, 6.405, 6.475, 6.545, 6.615, 6.6850000000000005, 6.755, 6.825, 6.895, 6.965]
xedges   = [0.0, 0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.49, 0.56, 0.63, 0.7, 0.77, 0.84, 0.91, 0.98, 1.05, 1.12, 1.19, 1.26, 1.33, 1.4, 1.47, 1.54, 1.61, 1.68, 1.75, 1.82, 1.89, 1.96, 2.03, 2.1, 2.17, 2.24, 2.31, 2.38, 2.45, 2.52, 2.59, 2.66, 2.73, 2.8, 2.87, 2.94, 3.01, 3.08, 3.15, 3.22, 3.29, 3.36, 3.43, 3.5, 3.57, 3.64, 3.71, 3.78, 3.85, 3.92, 3.99, 4.06, 4.13, 4.2, 4.27, 4.34, 4.41, 4.48, 4.55, 4.62, 4.69, 4.76, 4.83, 4.9, 4.97, 5.04, 5.11, 5.18, 5.25, 5.32, 5.39, 5.46, 5.53, 5.6, 5.67, 5.74, 5.81, 5.88, 5.95, 6.02, 6.09, 6.16, 6.23, 6.3, 6.37, 6.44, 6.51, 6.58, 6.65, 6.72, 6.79, 6.86, 6.93, 7.0]
xmins    = [0.0, 0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.49, 0.56, 0.63, 0.7, 0.77, 0.84, 0.91, 0.98, 1.05, 1.12, 1.19, 1.26, 1.33, 1.4, 1.47, 1.54, 1.61, 1.68, 1.75, 1.82, 1.89, 1.96, 2.03, 2.1, 2.17, 2.24, 2.31, 2.38, 2.45, 2.52, 2.59, 2.66, 2.73, 2.8, 2.87, 2.94, 3.01, 3.08, 3.15, 3.22, 3.29, 3.36, 3.43, 3.5, 3.57, 3.64, 3.71, 3.78, 3.85, 3.92, 3.99, 4.06, 4.13, 4.2, 4.27, 4.34, 4.41, 4.48, 4.55, 4.62, 4.69, 4.76, 4.83, 4.9, 4.97, 5.04, 5.11, 5.18, 5.25, 5.32, 5.39, 5.46, 5.53, 5.6, 5.67, 5.74, 5.81, 5.88, 5.95, 6.02, 6.09, 6.16, 6.23, 6.3, 6.37, 6.44, 6.51, 6.58, 6.65, 6.72, 6.79, 6.86, 6.93]
xmaxs    = [0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.49, 0.56, 0.63, 0.7, 0.77, 0.84, 0.91, 0.98, 1.05, 1.12, 1.19, 1.26, 1.33, 1.4, 1.47, 1.54, 1.61, 1.68, 1.75, 1.82, 1.89, 1.96, 2.03, 2.1, 2.17, 2.24, 2.31, 2.38, 2.45, 2.52, 2.59, 2.66, 2.73, 2.8, 2.87, 2.94, 3.01, 3.08, 3.15, 3.22, 3.29, 3.36, 3.43, 3.5, 3.57, 3.64, 3.71, 3.78, 3.85, 3.92, 3.99, 4.06, 4.13, 4.2, 4.27, 4.34, 4.41, 4.48, 4.55, 4.62, 4.69, 4.76, 4.83, 4.9, 4.97, 5.04, 5.11, 5.18, 5.25, 5.32, 5.39, 5.46, 5.53, 5.6, 5.67, 5.74, 5.81, 5.88, 5.95, 6.02, 6.09, 6.16, 6.23, 6.3, 6.37, 6.44, 6.51, 6.58, 6.65, 6.72, 6.79, 6.86, 6.93, 7.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.0, 1.6844657142857142, 2.024432857142858, 1.4172604285714279, 1.0849732857142864, 0.8833899999999999, 0.7366537142857142, 0.6319457142857138, 0.5507002857142862, 0.48634671428571463, 0.43743099999999957, 0.3944145714285717, 0.3582542857142854, 0.32633157142857167, 0.30145957142857116, 0.28000528571428546, 0.2591460000000006, 0.2421579999999998, 0.2264675714285712, 0.2128570000000005, 0.2003977142857141, 0.1879331428571427, 0.17832257142857127, 0.16907114285714325, 0.16060271428571415, 0.15224357142857128, 0.14385600000000032, 0.1386308857142856, 0.13160625714285745, 0.12593164285714234, 0.11986750000000028, 0.11526318571428525, 0.11095901428571454, 0.1062029428571431, 0.10209774285714243, 0.09828705714285736, 0.09413045714285737, 0.09136525714285677, 0.0882883000000002, 0.08446112857142878, 0.08149881428571396, 0.07848055714285732, 0.07606234285714303, 0.0731148999999997, 0.07106941428571445, 0.06925844285714257, 0.06725278571428586, 0.064422642857143, 0.06313372857142832, 0.06137251428571443, 0.059370171428571566, 0.05836498571428548, 0.055537100000000124, 0.055007700000000125, 0.05276302857142836, 0.05106222857142868, 0.05069555714285694, 0.049059442857143275, 0.047316042857142665, 0.047682571428571234, 0.045371014285714675, 0.04490735714285696, 0.042737971428571254, 0.0419752285714284, 0.042078442857143225, 0.04057905714285698, 0.039789785714285555, 0.039221800000000334, 0.03845548571428556, 0.03773595714285699, 0.036641657142857456, 0.03674205714285699, 0.03533739999999985, 0.03423094285714315, 0.034079899999999864, 0.03346157142857129, 0.033936128571428865, 0.03189691428571415, 0.03101851428571416, 0.031079014285714555, 0.03072018571428559, 0.03050731428571416, 0.029009485714285965, 0.029076785714285593, 0.02894562857142845, 0.02904982857142882, 0.030127071428571305, 0.029590071428571306, 0.027761685714285604, 0.02872058571428596, 0.02837332857142846, 0.016455399999999933, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 1.7069471428571428, 2.0043171428571434, 1.4272935714285708, 1.0841201428571436, 0.8837867142857142, 0.7376699999999999, 0.6205191428571423, 0.5540285714285718, 0.4900857142857147, 0.43719985714285675, 0.39006885714285744, 0.3638825714285711, 0.3235787142857145, 0.2977115714285712, 0.275870714285714, 0.25913571428571486, 0.24366442857142837, 0.21986214285714267, 0.21060114285714332, 0.2006434285714284, 0.18410042857142841, 0.17917428571428556, 0.16749014285714323, 0.15961171428571413, 0.151842857142857, 0.14490428571428604, 0.1373634999999999, 0.13142692857142887, 0.12610819999999948, 0.12200307142857171, 0.11717748571428524, 0.10928821428571454, 0.10659078571428596, 0.10306248571428529, 0.09752070000000022, 0.09440242857142879, 0.09035325714285677, 0.08674534285714305, 0.08501011428571448, 0.08131552857142825, 0.07618064285714303, 0.07821828571428589, 0.07481931428571398, 0.07105190000000015, 0.06878214285714257, 0.06716801428571444, 0.06547637142857159, 0.06135421428571403, 0.06163815714285728, 0.05965162857142871, 0.056837514285714055, 0.05555650000000013, 0.05364938571428583, 0.05598948571428549, 0.05121112857142869, 0.05199484285714265, 0.04885340000000042, 0.04663044285714267, 0.0467204142857141, 0.04569021428571468, 0.04419485714285696, 0.042835971428571255, 0.04296965714285697, 0.04229865714285751, 0.03983091428571413, 0.04010777142857126, 0.037724928571428895, 0.0389770428571427, 0.03653114285714271, 0.03636300000000032, 0.034709814285714145, 0.03624941428571414, 0.03552302857142888, 0.034630614285714144, 0.034045242857142714, 0.03311377142857171, 0.032228628571428435, 0.0326497714285713, 0.03171312857142884, 0.03137439999999987, 0.03141461428571416, 0.030371328571428834, 0.03086268571428559, 0.030825157142857013, 0.03149505714285741, 0.03210418571428558, 0.02978935714285702, 0.033101228571428436, 0.031433857142857416, 0.02924529999999988, 0.026685957142857035, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 1.6844657142857142, 2.024432857142858, 1.4172604285714279, 1.0849732857142864, 0.8833899999999999, 0.7366537142857142, 0.6319457142857138, 0.5507002857142862, 0.48634671428571463, 0.43743099999999957, 0.3944145714285717, 0.3582542857142854, 0.32633157142857167, 0.30145957142857116, 0.28000528571428546, 0.2591460000000006, 0.2421579999999998, 0.2264675714285712, 0.2128570000000005, 0.2003977142857141, 0.1879331428571427, 0.17832257142857127, 0.16907114285714325, 0.16060271428571415, 0.15224357142857128, 0.14385600000000032, 0.1386308857142856, 0.13160625714285745, 0.12593164285714234, 0.11986750000000028, 0.11526318571428525, 0.11095901428571454, 0.1062029428571431, 0.10209774285714243, 0.09828705714285736, 0.09413045714285737, 0.09136525714285677, 0.0882883000000002, 0.08446112857142878, 0.08149881428571396, 0.07848055714285732, 0.07606234285714303, 0.0731148999999997, 0.07106941428571445, 0.06925844285714257, 0.06725278571428586, 0.064422642857143, 0.06313372857142832, 0.06137251428571443, 0.059370171428571566, 0.05836498571428548, 0.055537100000000124, 0.055007700000000125, 0.05276302857142836, 0.05106222857142868, 0.05069555714285694, 0.049059442857143275, 0.047316042857142665, 0.047682571428571234, 0.045371014285714675, 0.04490735714285696, 0.042737971428571254, 0.0419752285714284, 0.042078442857143225, 0.04057905714285698, 0.039789785714285555, 0.039221800000000334, 0.03845548571428556, 0.03773595714285699, 0.036641657142857456, 0.03674205714285699, 0.03533739999999985, 0.03423094285714315, 0.034079899999999864, 0.03346157142857129, 0.033936128571428865, 0.03189691428571415, 0.03101851428571416, 0.031079014285714555, 0.03072018571428559, 0.03050731428571416, 0.029009485714285965, 0.029076785714285593, 0.02894562857142845, 0.02904982857142882, 0.030127071428571305, 0.029590071428571306, 0.027761685714285604, 0.02872058571428596, 0.02837332857142846, 0.016455399999999933, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.0, 1.7069471428571428, 2.0043171428571434, 1.4272935714285708, 1.0841201428571436, 0.8837867142857142, 0.7376699999999999, 0.6205191428571423, 0.5540285714285718, 0.4900857142857147, 0.43719985714285675, 0.39006885714285744, 0.3638825714285711, 0.3235787142857145, 0.2977115714285712, 0.275870714285714, 0.25913571428571486, 0.24366442857142837, 0.21986214285714267, 0.21060114285714332, 0.2006434285714284, 0.18410042857142841, 0.17917428571428556, 0.16749014285714323, 0.15961171428571413, 0.151842857142857, 0.14490428571428604, 0.1373634999999999, 0.13142692857142887, 0.12610819999999948, 0.12200307142857171, 0.11717748571428524, 0.10928821428571454, 0.10659078571428596, 0.10306248571428529, 0.09752070000000022, 0.09440242857142879, 0.09035325714285677, 0.08674534285714305, 0.08501011428571448, 0.08131552857142825, 0.07618064285714303, 0.07821828571428589, 0.07481931428571398, 0.07105190000000015, 0.06878214285714257, 0.06716801428571444, 0.06547637142857159, 0.06135421428571403, 0.06163815714285728, 0.05965162857142871, 0.056837514285714055, 0.05555650000000013, 0.05364938571428583, 0.05598948571428549, 0.05121112857142869, 0.05199484285714265, 0.04885340000000042, 0.04663044285714267, 0.0467204142857141, 0.04569021428571468, 0.04419485714285696, 0.042835971428571255, 0.04296965714285697, 0.04229865714285751, 0.03983091428571413, 0.04010777142857126, 0.037724928571428895, 0.0389770428571427, 0.03653114285714271, 0.03636300000000032, 0.034709814285714145, 0.03624941428571414, 0.03552302857142888, 0.034630614285714144, 0.034045242857142714, 0.03311377142857171, 0.032228628571428435, 0.0326497714285713, 0.03171312857142884, 0.03137439999999987, 0.03141461428571416, 0.030371328571428834, 0.03086268571428559, 0.030825157142857013, 0.03149505714285741, 0.03210418571428558, 0.02978935714285702, 0.033101228571428436, 0.031433857142857416, 0.02924529999999988, 0.026685957142857035, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.0, 0.011479002125442714, 0.010609502863961544, 0.007343632532712278, 0.005636901015737684, 0.004627116173345192, 0.0038286695083385863, 0.003351154537572664, 0.0029133027053605733, 0.0025500348136879266, 0.0023157830253303425, 0.002101475671998133, 0.0019727428331422926, 0.0017606173546196116, 0.0016288734055869925, 0.0015410790018022807, 0.001436434076852421, 0.0013483998074815657, 0.0012765980781206047, 0.001213272518472927, 0.0011577203144674494, 0.0011066610011329439, 0.0010378963221392599, 0.001010587220685206, 0.000958444317737906, 0.0009174435421655237, 0.0008817261595349017, 0.0008723010854478331, 0.0008435224976736756, 0.0008019249799509818, 0.0007616548846198709, 0.0007521123993290399, 0.0007249090020302495, 0.000706449588016134, 0.0006952444879027664, 0.0006712739943646008, 0.0007493512840709476, 0.0006560363354795101, 0.0006486277508584376, 0.0006227843994218762, 0.0006053388324242988, 0.0006055304640207168, 0.0005827823831606876, 0.0005597831212685323, 0.000575444459987768, 0.0005569397065524162, 0.0005546909417110829, 0.0005349148320536847, 0.0005374611518946425, 0.0005356664740569198, 0.0005341520077159124, 0.000570754960109672, 0.0005510396481901755, 0.0005834489292656437, 0.0005324306987576782, 0.0005028045832921504, 0.0005197038010408663, 0.0004966387016735649, 0.0004957597755990686, 0.0005205965965375959, 0.0004999220347377487, 0.0005810648212812487, 0.0004931264274700614, 0.0004980996539911672, 0.0005124506944923763, 0.0005126258929496703, 0.0005352256819438344, 0.0005318383596698637, 0.0006495990914339654, 0.0005362924499158387, 0.0005364834478303346, 0.0005611420570259039, 0.0005522253680725421, 0.0005716083645722701, 0.0006041837131069245, 0.0006062017916873019, 0.0006565298382948302, 0.0006597450033063923, 0.0006407763148824107, 0.0006608694026409048, 0.0007012484493780346, 0.000739221874400259, 0.000709698268740364, 0.0007699398333238584, 0.0008474483910600091, 0.0009028111425894606, 0.0009817455300200138, 0.0010604724592061243, 0.0011523648267269962, 0.0014503799642908623, 0.0019126309478979767, 0.002217279542914815, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.02168788808980529, 0.021010021904038164, 0.014768423291963569, 0.010842391294340562, 0.010901077460320992, 0.008409898201233, 0.0059439902765872025, 0.006522892184374938, 0.00666456514496097, 0.0060703612507235225, 0.0039005543823661705, 0.007534783287107425, 0.003504374816874313, 0.003064219446502896, 0.003535174273336057, 0.003182217491508925, 0.003517319538326573, 0.0019783579049302462, 0.002732085993806025, 0.0030624240098860436, 0.0018645084705451696, 0.0020679265964156602, 0.0023472280655779405, 0.0024171192163653073, 0.0018501097595680568, 0.002168553077279782, 0.0018202735833844708, 0.0019209818917864491, 0.001565523971749532, 0.0020542012698717906, 0.0019428366595558811, 0.0015490635749328316, 0.0021401611612022094, 0.0040556767974919, 0.0014189336323666565, 0.0036764248938336904, 0.001334067510454012, 0.0012708283494939664, 0.0012477377896965138, 0.0013834466718589248, 0.0008642558436396653, 0.0013081334263845173, 0.0037108195365246404, 0.0011714476479282975, 0.0011567539028837224, 0.0014503884068111734, 0.0010871810580861082, 0.0007529928042586473, 0.0011221316267511169, 0.0013693815824551445, 0.0008805615091681927, 0.0008728974739337968, 0.000815642478700826, 0.0034170980646849123, 0.0009890933799625386, 0.0015014306103017221, 0.0008283773171640135, 0.0009983844092189243, 0.0012177374469876116, 0.0012982352228612425, 0.0008151732005768897, 0.0008274787129637582, 0.0012764820917710643, 0.0009132394683381936, 0.0006997880145487764, 0.0015077222989039547, 0.000733904292264387, 0.0008191990862160049, 0.0008276528159037845, 0.0009378061676931328, 0.0008376654877621193, 0.001182204702741307, 0.001039478872575403, 0.0013621001941030238, 0.0010474510363111867, 0.001208633905848819, 0.0013054459711812879, 0.0012018264162073763, 0.0008648082245828467, 0.0008860767691438029, 0.0010905316059947369, 0.00102917075793068, 0.0013197911863284243, 0.0014017718379658903, 0.001425785497792119, 0.001309186458711461, 0.0011142847985344177, 0.0020825911058788473, 0.0014410512036109636, 0.0014393053880257598, 0.00174916656538746, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.011479002125442714, 0.010609502863961544, 0.007343632532712278, 0.005636901015737684, 0.004627116173345192, 0.0038286695083385863, 0.003351154537572664, 0.0029133027053605733, 0.0025500348136879266, 0.0023157830253303425, 0.002101475671998133, 0.0019727428331422926, 0.0017606173546196116, 0.0016288734055869925, 0.0015410790018022807, 0.001436434076852421, 0.0013483998074815657, 0.0012765980781206047, 0.001213272518472927, 0.0011577203144674494, 0.0011066610011329439, 0.0010378963221392599, 0.001010587220685206, 0.000958444317737906, 0.0009174435421655237, 0.0008817261595349017, 0.0008723010854478331, 0.0008435224976736756, 0.0008019249799509818, 0.0007616548846198709, 0.0007521123993290399, 0.0007249090020302495, 0.000706449588016134, 0.0006952444879027664, 0.0006712739943646008, 0.0007493512840709476, 0.0006560363354795101, 0.0006486277508584376, 0.0006227843994218762, 0.0006053388324242988, 0.0006055304640207168, 0.0005827823831606876, 0.0005597831212685323, 0.000575444459987768, 0.0005569397065524162, 0.0005546909417110829, 0.0005349148320536847, 0.0005374611518946425, 0.0005356664740569198, 0.0005341520077159124, 0.000570754960109672, 0.0005510396481901755, 0.0005834489292656437, 0.0005324306987576782, 0.0005028045832921504, 0.0005197038010408663, 0.0004966387016735649, 0.0004957597755990686, 0.0005205965965375959, 0.0004999220347377487, 0.0005810648212812487, 0.0004931264274700614, 0.0004980996539911672, 0.0005124506944923763, 0.0005126258929496703, 0.0005352256819438344, 0.0005318383596698637, 0.0006495990914339654, 0.0005362924499158387, 0.0005364834478303346, 0.0005611420570259039, 0.0005522253680725421, 0.0005716083645722701, 0.0006041837131069245, 0.0006062017916873019, 0.0006565298382948302, 0.0006597450033063923, 0.0006407763148824107, 0.0006608694026409048, 0.0007012484493780346, 0.000739221874400259, 0.000709698268740364, 0.0007699398333238584, 0.0008474483910600091, 0.0009028111425894606, 0.0009817455300200138, 0.0010604724592061243, 0.0011523648267269962, 0.0014503799642908623, 0.0019126309478979767, 0.002217279542914815, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.02168788808980529, 0.021010021904038164, 0.014768423291963569, 0.010842391294340562, 0.010901077460320992, 0.008409898201233, 0.0059439902765872025, 0.006522892184374938, 0.00666456514496097, 0.0060703612507235225, 0.0039005543823661705, 0.007534783287107425, 0.003504374816874313, 0.003064219446502896, 0.003535174273336057, 0.003182217491508925, 0.003517319538326573, 0.0019783579049302462, 0.002732085993806025, 0.0030624240098860436, 0.0018645084705451696, 0.0020679265964156602, 0.0023472280655779405, 0.0024171192163653073, 0.0018501097595680568, 0.002168553077279782, 0.0018202735833844708, 0.0019209818917864491, 0.001565523971749532, 0.0020542012698717906, 0.0019428366595558811, 0.0015490635749328316, 0.0021401611612022094, 0.0040556767974919, 0.0014189336323666565, 0.0036764248938336904, 0.001334067510454012, 0.0012708283494939664, 0.0012477377896965138, 0.0013834466718589248, 0.0008642558436396653, 0.0013081334263845173, 0.0037108195365246404, 0.0011714476479282975, 0.0011567539028837224, 0.0014503884068111734, 0.0010871810580861082, 0.0007529928042586473, 0.0011221316267511169, 0.0013693815824551445, 0.0008805615091681927, 0.0008728974739337968, 0.000815642478700826, 0.0034170980646849123, 0.0009890933799625386, 0.0015014306103017221, 0.0008283773171640135, 0.0009983844092189243, 0.0012177374469876116, 0.0012982352228612425, 0.0008151732005768897, 0.0008274787129637582, 0.0012764820917710643, 0.0009132394683381936, 0.0006997880145487764, 0.0015077222989039547, 0.000733904292264387, 0.0008191990862160049, 0.0008276528159037845, 0.0009378061676931328, 0.0008376654877621193, 0.001182204702741307, 0.001039478872575403, 0.0013621001941030238, 0.0010474510363111867, 0.001208633905848819, 0.0013054459711812879, 0.0012018264162073763, 0.0008648082245828467, 0.0008860767691438029, 0.0010905316059947369, 0.00102917075793068, 0.0013197911863284243, 0.0014017718379658903, 0.001425785497792119, 0.001309186458711461, 0.0011142847985344177, 0.0020825911058788473, 0.0014410512036109636, 0.0014393053880257598, 0.00174916656538746, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0133463260075684, 0.9900635310206808, 1.0070792513887206, 0.9992136738587244, 1.0004490817031144, 1.0013795976244702, 0.9819184287981335, 1.0060437334074896, 1.007687931038028, 0.9994715901316029, 0.9889818617249001, 1.0157103095167836, 0.9915642328727003, 0.9875671554157701, 0.9852339522162081, 0.9999603091913989, 1.0062208499055516, 0.970832784006288, 0.9894020063100712, 1.0012261331751717, 0.9796059692960719, 1.0047762561906273, 0.9906489068845067, 0.9938294940754425, 0.9973679395329852, 1.0072870489537156, 0.9908578401720828, 0.9986373856735861, 1.0014020077785963, 1.017816100515748, 1.016608078183308, 0.9849421877910904, 1.0036519031084152, 1.0094492084755757, 0.9922028681584875, 1.0028893031737716, 0.9889235795788583, 0.9825236510063379, 1.0064998624050048, 0.9977510628112557, 0.9706944704593804, 1.0283444182253505, 1.0233114493176394, 0.9997535608546894, 0.9931228601113304, 0.9987395105247898, 1.0163564940011112, 0.9718135721431219, 1.00432836849255, 1.0047407163578055, 0.9738289762281642, 1.0003493160427894, 0.9753068336666633, 1.0611499610658113, 1.0029160497723228, 1.0256291830588704, 0.9958001386656014, 0.985510199953323, 0.9798216179616392, 1.0070353287230898, 0.9841340028598559, 1.0022930428544974, 1.023690843511105, 1.0052334228826365, 0.981563325769028, 1.0079916417889012, 0.961835728381374, 1.0135626200831833, 0.9680725128780167, 0.9923950725871726, 0.9446889201320091, 1.0258087546258154, 1.0377461327804502, 1.0161595041568279, 1.0174430370019338, 0.9757675027330753, 1.0103995729098738, 1.0525897896924232, 1.020403294643928, 1.0212959092044178, 1.0297404088574544, 1.046944743197299, 1.0614201314254132, 1.0649330715617555, 1.0841735972870261, 1.0656258372275529, 1.0067348845293185, 1.1923349652501545, 1.0944713125130259, 1.0307320808828007, 1.621714278769106, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0068146249746082, 1.0052407284472429, 1.0051815688808263, 1.0051954283943745, 1.0052379087077568, 1.0051973803078573, 1.0053029152058741, 1.0052901783073926, 1.0052432446622634, 1.0052940532914456, 1.0053280883218554, 1.005506543569211, 1.0053951793475338, 1.0054032897276008, 1.00550374968055, 1.0055429529178626, 1.005568264552406, 1.0056370016690148, 1.005699941831713, 1.0057771133697506, 1.0058885888050846, 1.0058203306167275, 1.0059772898178083, 1.005967796509546, 1.0060261562019122, 1.0061292275576612, 1.0062922564546375, 1.0064094406754387, 1.0063679386828988, 1.0063541400681575, 1.006525174492343, 1.0065331240250894, 1.006651883356626, 1.0068095970434485, 1.0068297293039197, 1.0079607738750667, 1.0071803698254111, 1.0073467011014874, 1.0073736215695388, 1.00742757839767, 1.0077156748889853, 1.0076619041863495, 1.0076562112684082, 1.0080969354506617, 1.0080414702320293, 1.0082478507889265, 1.0083032115469068, 1.0085130589315119, 1.0087281168172966, 1.0089969760043316, 1.0097790645045934, 1.009922009759065, 1.0106066774154463, 1.0100909806198273, 1.0098468985267417, 1.0102514664071327, 1.010123203052259, 1.0104776254661845, 1.0109179639633623, 1.0110185333655888, 1.0129391898844726, 1.0115383676619802, 1.0118665143929726, 1.0121784614566693, 1.0126327699321596, 1.0134513336107682, 1.013559764204342, 1.0168922347323948, 1.0142117092163743, 1.0146413533028462, 1.01527247249233, 1.0156272212464001, 1.0166985866254918, 1.0177284473577366, 1.0181163575351304, 1.0193460440519302, 1.0206836622940005, 1.0206578661047452, 1.021264168694844, 1.0228269599637199, 1.0242309718737326, 1.0244643519616368, 1.0264795373494664, 1.0292772495497473, 1.031078019629947, 1.032586822530947, 1.0358387934874047, 1.0415091806234955, 1.0504996652477538, 1.0674094667138903, 1.134744797629643, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0262215587332173, 1.0004417571149213, 1.0174996533093823, 1.0092069072747918, 1.012789132485126, 1.0127959497559291, 0.9913242846212175, 1.0178884561243382, 1.0213912520417465, 1.0133488902102976, 0.9988713401187596, 1.0367422513177997, 1.0023029266544063, 0.9977317669820309, 0.9978593362846478, 1.01223994110356, 1.0207457449671502, 0.9795685067080004, 1.00223731825098, 1.0165078644104883, 0.9895270957253919, 1.0163728060824844, 1.0045319860777504, 1.0088797952307842, 1.0095202408893422, 1.022361519794555, 1.003988201231277, 1.013233818498974, 1.0138335455258285, 1.0349533668295678, 1.0334637346317754, 0.9989028703449572, 1.0238035213557646, 1.049172680160613, 1.006639495661784, 1.0419460017750983, 1.0035250544958292, 0.9969177253003719, 1.0212727858882766, 1.0147261155648934, 0.9817068265779344, 1.0455425924761936, 1.0740647094127043, 1.0162367084886186, 1.0098248513078365, 1.0203057310375423, 1.0332322539803616, 0.9837405218306685, 1.022612312694789, 1.0278058608488003, 0.9889161299110043, 1.016066691885853, 0.990134621025539, 1.1259130756406122, 1.022286402528841, 1.0552457943542308, 1.012685314462974, 1.006610536095829, 1.0053600360985846, 1.0356490867203405, 1.00228633362347, 1.021654717854602, 1.054101210177695, 1.0269366848459807, 0.998808379346424, 1.0458838362764589, 0.9805473706890799, 1.0348651487341656, 0.9900052496778423, 1.0179890615281433, 0.9674874663458258, 1.059263527833276, 1.068112777278485, 1.0561273501335775, 1.0487461405799332, 1.011382464036186, 1.0513266030134085, 1.091335243621559, 1.0482294096111702, 1.0501393796633793, 1.0654869710025663, 1.0824217857090819, 1.10680998982644, 1.1133608275701206, 1.1332542827129777, 1.1090813208385446, 1.0443922724550028, 1.2673517033298305, 1.1446461668125385, 1.0814594879405373, 1.72801169878852, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 0.9931853750253917, 0.9947592715527571, 0.9948184311191737, 0.9948045716056255, 0.9947620912922432, 0.9948026196921426, 0.994697084794126, 0.9947098216926075, 0.9947567553377366, 0.9947059467085544, 0.9946719116781447, 0.9944934564307889, 0.9946048206524664, 0.994596710272399, 0.9944962503194501, 0.9944570470821374, 0.9944317354475939, 0.9943629983309851, 0.994300058168287, 0.9942228866302494, 0.9941114111949154, 0.9941796693832726, 0.9940227101821918, 0.9940322034904541, 0.993973843798088, 0.9938707724423388, 0.9937077435453624, 0.9935905593245614, 0.9936320613171012, 0.9936458599318425, 0.9934748255076571, 0.9934668759749106, 0.993348116643374, 0.9931904029565514, 0.9931702706960803, 0.9920392261249333, 0.9928196301745889, 0.9926532988985127, 0.9926263784304613, 0.99257242160233, 0.9922843251110147, 0.9923380958136506, 0.9923437887315919, 0.9919030645493383, 0.9919585297679706, 0.9917521492110735, 0.9916967884530932, 0.9914869410684882, 0.9912718831827033, 0.9910030239956683, 0.9902209354954066, 0.9900779902409349, 0.9893933225845537, 0.9899090193801727, 0.9901531014732582, 0.9897485335928674, 0.9898767969477408, 0.9895223745338156, 0.9890820360366376, 0.9889814666344113, 0.9870608101155275, 0.9884616323380198, 0.9881334856070274, 0.9878215385433308, 0.9873672300678404, 0.9865486663892318, 0.9864402357956581, 0.9831077652676052, 0.9857882907836258, 0.9853586466971538, 0.9847275275076699, 0.9843727787535997, 0.983301413374508, 0.9822715526422635, 0.9818836424648697, 0.9806539559480697, 0.9793163377059995, 0.9793421338952547, 0.9787358313051558, 0.9771730400362802, 0.9757690281262674, 0.9755356480383632, 0.9735204626505335, 0.9707227504502527, 0.968921980370053, 0.9674131774690531, 0.9641612065125952, 0.9584908193765045, 0.9495003347522463, 0.9325905332861097, 0.8652552023703572, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0004710932819192, 0.9796853049264401, 0.9966588494680588, 0.989220440442657, 0.9881090309211031, 0.9899632454930111, 0.9725125729750496, 0.9941990106906412, 0.9939846100343094, 0.9855942900529081, 0.9790923833310406, 0.9946783677157677, 0.9808255390909945, 0.9774025438495093, 0.9726085681477684, 0.9876806772792377, 0.9916959548439531, 0.9620970613045755, 0.9765666943691624, 0.9859444019398551, 0.9696848428667519, 0.9931797062987703, 0.976765827691263, 0.9787791929201007, 0.9852156381766282, 0.9922125781128763, 0.9777274791128886, 0.9840409528481981, 0.9889704700313642, 1.0006788342019282, 0.9997524217348406, 0.9709815052372237, 0.983500284861066, 0.9697257367905386, 0.9777662406551909, 0.9638326045724448, 0.9743221046618875, 0.9681295767123039, 0.9917269389217328, 0.9807760100576179, 0.9596821143408265, 1.0111462439745074, 0.9725581892225748, 0.9832704132207604, 0.9764208689148242, 0.9771732900120373, 0.9994807340218609, 0.9598866224555753, 0.9860444242903109, 0.9816755718668105, 0.958741822545324, 0.984631940199726, 0.9604790463077876, 0.9963868464910103, 0.9835456970158045, 0.9960125717635101, 0.9789149628682289, 0.9644098638108171, 0.954283199824694, 0.978421570725839, 0.9659816720962418, 0.9829313678543927, 0.9932804768445148, 0.9835301609192921, 0.9643182721916321, 0.9700994473013435, 0.943124086073668, 0.9922600914322012, 0.9461397760781909, 0.9668010836462021, 0.9218903739181925, 0.992353981418355, 1.0073794882824156, 0.9761916581800784, 0.9861399334239346, 0.940152541429965, 0.9694725428063392, 1.0138443357632876, 0.9925771796766862, 0.9924524387454565, 0.9939938467123427, 1.0114677006855162, 1.0160302730243862, 1.0165053155533907, 1.0350929118610745, 1.022170353616561, 0.9690774966036342, 1.1173182271704785, 1.0442964582135132, 0.9800046738250642, 1.5154168587496917, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.006814624974608274, 0.005240728447242882, 0.005181568880826326, 0.0051954283943744795, 0.005237908707756755, 0.005197380307857435, 0.005302915205874004, 0.005290178307392535, 0.0052432446622634465, 0.005294053291445611, 0.005328088321855273, 0.0055065435692110976, 0.005395179347533641, 0.005403289727600957, 0.0055037496805498964, 0.005542952917862554, 0.00556826455240611, 0.005637001669014929, 0.005699941831712962, 0.005777113369750619, 0.0058885888050845825, 0.005820330616727376, 0.005977289817808207, 0.005967796509545931, 0.006026156201912047, 0.00612922755766121, 0.006292256454637601, 0.006409440675438582, 0.006367938682898755, 0.006354140068157488, 0.006525174492342911, 0.006533124025089432, 0.006651883356626032, 0.006809597043448634, 0.006829729303919674, 0.007960773875066662, 0.007180369825411148, 0.007346701101487274, 0.007373621569538691, 0.007427578397670054, 0.00771567488898528, 0.0076619041863493775, 0.007656211268408097, 0.008096935450661702, 0.00804147023202939, 0.008247850788926536, 0.00830321154690683, 0.008513058931511774, 0.008728116817296683, 0.008996976004331692, 0.009779064504593427, 0.009922009759065098, 0.010606677415446297, 0.010090980619827272, 0.00984689852674181, 0.010251466407132592, 0.010123203052259222, 0.01047762546618436, 0.01091796396336242, 0.011018533365588667, 0.012939189884472513, 0.011538367661980242, 0.011866514392972594, 0.012178461456669232, 0.01263276993215956, 0.013451333610768224, 0.013559764204341906, 0.016892234732394762, 0.014211709216374158, 0.014641353302846216, 0.015272472492330103, 0.015627221246400258, 0.01669858662549195, 0.017728447357736488, 0.0181163575351303, 0.0193460440519303, 0.020683662294000538, 0.020657866104745293, 0.021264168694844154, 0.02282695996371975, 0.024230971873732576, 0.024464351961636766, 0.02647953734946651, 0.02927724954974731, 0.03107801962994705, 0.03258682253094691, 0.03583879348740482, 0.04150918062349551, 0.05049966524775373, 0.06740946671389025, 0.13474479762964275, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.006814624974608163, 0.005240728447242882, 0.005181568880826326, 0.0051954283943744795, 0.005237908707756755, 0.005197380307857324, 0.005302915205874115, 0.005290178307392646, 0.0052432446622634465, 0.005294053291445611, 0.005328088321855384, 0.0055065435692109865, 0.005395179347533752, 0.005403289727600846, 0.0055037496805498964, 0.005542952917862554, 0.005568264552405999, 0.005637001669014818, 0.005699941831712962, 0.005777113369750619, 0.0058885888050845825, 0.005820330616727487, 0.005977289817808318, 0.005967796509545931, 0.006026156201912158, 0.00612922755766121, 0.00629225645463749, 0.0064094406754386934, 0.006367938682898755, 0.006354140068157488, 0.006525174492342911, 0.006533124025089432, 0.006651883356626032, 0.006809597043448523, 0.006829729303919674, 0.007960773875066662, 0.007180369825411148, 0.007346701101487385, 0.007373621569538802, 0.007427578397670054, 0.00771567488898528, 0.0076619041863494886, 0.007656211268408208, 0.008096935450661702, 0.00804147023202928, 0.008247850788926536, 0.00830321154690683, 0.008513058931511885, 0.008728116817296572, 0.00899697600433158, 0.009779064504593427, 0.009922009759065098, 0.010606677415446297, 0.010090980619827272, 0.009846898526741699, 0.010251466407132703, 0.010123203052259111, 0.01047762546618447, 0.01091796396336231, 0.011018533365588778, 0.012939189884472624, 0.011538367661980242, 0.011866514392972594, 0.012178461456669343, 0.01263276993215956, 0.013451333610768224, 0.013559764204341906, 0.016892234732394762, 0.014211709216374269, 0.014641353302846216, 0.015272472492330103, 0.015627221246400147, 0.01669858662549184, 0.0177284473577366, 0.018116357535130412, 0.01934604405193019, 0.020683662294000538, 0.02065786610474518, 0.021264168694844043, 0.02282695996371986, 0.024230971873732576, 0.024464351961636766, 0.026479537349466398, 0.02927724954974731, 0.03107801962994694, 0.03258682253094691, 0.03583879348740471, 0.04150918062349551, 0.050499665247753844, 0.06740946671389025, 0.13474479762964298, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [0.0, 0.012875232725649166, 0.010378226094240661, 0.010420401920661737, 0.009993233416067393, 0.01234005078201128, 0.011416352131459084, 0.009405855823083953, 0.011844722716848444, 0.013703321003718627, 0.01387730007869481, 0.009889478393859452, 0.021031941801015974, 0.010738693781705888, 0.010164611566260806, 0.012625384068439716, 0.012279631912161193, 0.014524895061598486, 0.008735722701712523, 0.012835311940908811, 0.01528173123531662, 0.00992112642931997, 0.011596549891856989, 0.01388307919324372, 0.015050301155341783, 0.012152301356357031, 0.015074470840839238, 0.013130361059194184, 0.014596432825387917, 0.012431537747232158, 0.017137266313819843, 0.016855656448467427, 0.013960682553866732, 0.020151618247349234, 0.03972347168503709, 0.01443662750329655, 0.03905669860132677, 0.014601474916970836, 0.014394074294033943, 0.014772923483271971, 0.016975052753637754, 0.01101235611855389, 0.017198174250843135, 0.050753260095064645, 0.016483147633928996, 0.016701991196506283, 0.021566220512752476, 0.016875759979250282, 0.011926949687546595, 0.018283944202239, 0.02306514449099495, 0.015087153682840193, 0.01571737584306343, 0.014827787358875688, 0.064763114574801, 0.019370352756518328, 0.029616611295360307, 0.016885175797372476, 0.02110033614250595, 0.02553841813694524, 0.028613757997250744, 0.01815233076361411, 0.01936167500010466, 0.03041036666659014, 0.021703261963344378, 0.01724505357739592, 0.03789219448755776, 0.018711642307705945, 0.021302528650982144, 0.02193273679982577, 0.025593988940970536, 0.022798546213816606, 0.033454773207460486, 0.030366644498034612, 0.039967845976749516, 0.03130310357799926, 0.03561496130311037, 0.0409270301035346, 0.03874545392913564, 0.027826114967241855, 0.028843470458961296, 0.03574656214511174, 0.03547704251178274, 0.04538985840102705, 0.0484277560083648, 0.049080685425951565, 0.04345548361099194, 0.037657387925684294, 0.07501673807967602, 0.05017485429951263, 0.050727407057736484, 0.10629742001941422, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.012875232725648944, 0.01037822609424055, 0.010420401920661737, 0.009993233416067393, 0.012340050782011502, 0.011416352131458973, 0.009405855823083953, 0.011844722716848555, 0.013703321003718516, 0.013877300078694699, 0.009889478393859452, 0.021031941801016085, 0.010738693781705999, 0.010164611566260806, 0.012625384068439716, 0.012279631912161193, 0.014524895061598597, 0.008735722701712412, 0.012835311940908811, 0.01528173123531662, 0.00992112642931997, 0.0115965498918571, 0.01388307919324372, 0.015050301155341672, 0.012152301356357031, 0.01507447084083946, 0.013130361059194295, 0.014596432825387917, 0.012431537747232158, 0.017137266313819843, 0.016855656448467427, 0.013960682553866732, 0.020151618247349345, 0.039723471685037204, 0.01443662750329644, 0.03905669860132677, 0.014601474916970836, 0.014394074294034054, 0.01477292348327186, 0.016975052753637754, 0.011012356118554001, 0.017198174250843135, 0.05075326009506487, 0.016483147633929218, 0.01670199119650606, 0.021566220512752476, 0.016875759979250393, 0.011926949687546595, 0.01828394420223911, 0.023065144490994838, 0.015087153682840082, 0.01571737584306354, 0.014827787358875688, 0.06476311457480088, 0.019370352756518106, 0.029616611295360418, 0.016885175797372587, 0.02110033614250606, 0.02553841813694535, 0.028613757997250744, 0.01815233076361411, 0.01936167500010466, 0.030410366666590027, 0.021703261963344156, 0.01724505357739592, 0.03789219448755765, 0.018711642307705945, 0.021302528650982255, 0.02193273679982566, 0.025593988940970647, 0.022798546213816717, 0.0334547732074606, 0.030366644498034834, 0.03996784597674963, 0.03130310357799937, 0.03561496130311059, 0.04092703010353471, 0.038745453929135865, 0.027826114967242077, 0.028843470458961518, 0.03574656214511185, 0.035477042511782964, 0.04538985840102683, 0.04842775600836502, 0.049080685425951565, 0.04345548361099172, 0.037657387925684294, 0.07501673807967602, 0.05017485429951263, 0.050727407057736595, 0.106297420019414, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}