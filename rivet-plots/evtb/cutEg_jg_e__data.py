
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
  'curve0' : [0.0, 1.6844657142857142, 2.024432857142858, 1.4172604285714279, 1.0849732857142864, 0.8833899999999999, 0.7366537142857142, 0.6319457142857138, 0.5507002857142862, 0.48634671428571463, 0.43743099999999957, 0.3944145714285717, 0.3582542857142854, 0.32633157142857167, 0.30145957142857116, 0.28000528571428546, 0.2591460000000006, 0.2421579999999998, 0.2264675714285712, 0.2128570000000005, 0.2003977142857141, 0.1879331428571427, 0.17832257142857127, 0.16907114285714325, 0.16060271428571415, 0.15224357142857128, 0.14385600000000032, 0.1386308857142856, 0.13160625714285745, 0.12593164285714234, 0.11986750000000028, 0.11526318571428525, 0.11095901428571454, 0.1062029428571431, 0.10209774285714243, 0.09828705714285736, 0.09413045714285737, 0.09136525714285677, 0.0882883000000002, 0.08446112857142878, 0.08149881428571396, 0.07848055714285732, 0.06566688571428587, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 1.7069471428571428, 2.0043171428571434, 1.4272935714285708, 1.0841201428571436, 0.8837867142857142, 0.7376699999999999, 0.6205191428571423, 0.5540285714285718, 0.4900857142857147, 0.43719985714285675, 0.39006885714285744, 0.3638825714285711, 0.3235787142857145, 0.2977115714285712, 0.275870714285714, 0.25913571428571486, 0.24366442857142837, 0.21986214285714267, 0.21060114285714332, 0.2006434285714284, 0.18410042857142841, 0.17917428571428556, 0.16749014285714323, 0.15961171428571413, 0.151842857142857, 0.14490428571428604, 0.1373634999999999, 0.13142692857142887, 0.12610819999999948, 0.12200307142857171, 0.11717748571428524, 0.10928821428571454, 0.10659078571428596, 0.10306248571428529, 0.09752070000000022, 0.09440242857142879, 0.09035325714285677, 0.08674534285714305, 0.08501011428571448, 0.08131552857142825, 0.07618064285714303, 0.0674055571428573, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 1.6844657142857142, 2.024432857142858, 1.4172604285714279, 1.0849732857142864, 0.8833899999999999, 0.7366537142857142, 0.6319457142857138, 0.5507002857142862, 0.48634671428571463, 0.43743099999999957, 0.3944145714285717, 0.3582542857142854, 0.32633157142857167, 0.30145957142857116, 0.28000528571428546, 0.2591460000000006, 0.2421579999999998, 0.2264675714285712, 0.2128570000000005, 0.2003977142857141, 0.1879331428571427, 0.17832257142857127, 0.16907114285714325, 0.16060271428571415, 0.15224357142857128, 0.14385600000000032, 0.1386308857142856, 0.13160625714285745, 0.12593164285714234, 0.11986750000000028, 0.11526318571428525, 0.11095901428571454, 0.1062029428571431, 0.10209774285714243, 0.09828705714285736, 0.09413045714285737, 0.09136525714285677, 0.0882883000000002, 0.08446112857142878, 0.08149881428571396, 0.07848055714285732, 0.06566688571428587, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.0, 1.7069471428571428, 2.0043171428571434, 1.4272935714285708, 1.0841201428571436, 0.8837867142857142, 0.7376699999999999, 0.6205191428571423, 0.5540285714285718, 0.4900857142857147, 0.43719985714285675, 0.39006885714285744, 0.3638825714285711, 0.3235787142857145, 0.2977115714285712, 0.275870714285714, 0.25913571428571486, 0.24366442857142837, 0.21986214285714267, 0.21060114285714332, 0.2006434285714284, 0.18410042857142841, 0.17917428571428556, 0.16749014285714323, 0.15961171428571413, 0.151842857142857, 0.14490428571428604, 0.1373634999999999, 0.13142692857142887, 0.12610819999999948, 0.12200307142857171, 0.11717748571428524, 0.10928821428571454, 0.10659078571428596, 0.10306248571428529, 0.09752070000000022, 0.09440242857142879, 0.09035325714285677, 0.08674534285714305, 0.08501011428571448, 0.08131552857142825, 0.07618064285714303, 0.0674055571428573, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.0, 0.011479002125442714, 0.010609502863961544, 0.007343632532712278, 0.005636901015737684, 0.004627116173345192, 0.0038286695083385863, 0.003351154537572664, 0.0029133027053605733, 0.0025500348136879266, 0.0023157830253303425, 0.002101475671998133, 0.0019727428331422926, 0.0017606173546196116, 0.0016288734055869925, 0.0015410790018022807, 0.001436434076852421, 0.0013483998074815657, 0.0012765980781206047, 0.001213272518472927, 0.0011577203144674494, 0.0011066610011329439, 0.0010378963221392599, 0.001010587220685206, 0.000958444317737906, 0.0009174435421655237, 0.0008817261595349017, 0.0008723010854478331, 0.0008435224976736756, 0.0008019249799509818, 0.0007616548846198709, 0.0007521123993290399, 0.0007249090020302495, 0.000706449588016134, 0.0006952444879027664, 0.0006712739943646008, 0.0007493512840709476, 0.0006560363354795101, 0.0006486277508584376, 0.0006227843994218762, 0.0006053388324242988, 0.0006055304640207168, 0.0005421309051948139, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.02168788808980529, 0.021010021904038164, 0.014768423291963569, 0.010842391294340562, 0.010901077460320992, 0.008409898201233, 0.0059439902765872025, 0.006522892184374938, 0.00666456514496097, 0.0060703612507235225, 0.0039005543823661705, 0.007534783287107425, 0.003504374816874313, 0.003064219446502896, 0.003535174273336057, 0.003182217491508925, 0.003517319538326573, 0.0019783579049302462, 0.002732085993806025, 0.0030624240098860436, 0.0018645084705451696, 0.0020679265964156602, 0.0023472280655779405, 0.0024171192163653073, 0.0018501097595680568, 0.002168553077279782, 0.0018202735833844708, 0.0019209818917864491, 0.001565523971749532, 0.0020542012698717906, 0.0019428366595558811, 0.0015490635749328316, 0.0021401611612022094, 0.0040556767974919, 0.0014189336323666565, 0.0036764248938336904, 0.001334067510454012, 0.0012708283494939664, 0.0012477377896965138, 0.0013834466718589248, 0.0008642558436396653, 0.001210943299031542, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.011479002125442714, 0.010609502863961544, 0.007343632532712278, 0.005636901015737684, 0.004627116173345192, 0.0038286695083385863, 0.003351154537572664, 0.0029133027053605733, 0.0025500348136879266, 0.0023157830253303425, 0.002101475671998133, 0.0019727428331422926, 0.0017606173546196116, 0.0016288734055869925, 0.0015410790018022807, 0.001436434076852421, 0.0013483998074815657, 0.0012765980781206047, 0.001213272518472927, 0.0011577203144674494, 0.0011066610011329439, 0.0010378963221392599, 0.001010587220685206, 0.000958444317737906, 0.0009174435421655237, 0.0008817261595349017, 0.0008723010854478331, 0.0008435224976736756, 0.0008019249799509818, 0.0007616548846198709, 0.0007521123993290399, 0.0007249090020302495, 0.000706449588016134, 0.0006952444879027664, 0.0006712739943646008, 0.0007493512840709476, 0.0006560363354795101, 0.0006486277508584376, 0.0006227843994218762, 0.0006053388324242988, 0.0006055304640207168, 0.0005421309051948139, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.02168788808980529, 0.021010021904038164, 0.014768423291963569, 0.010842391294340562, 0.010901077460320992, 0.008409898201233, 0.0059439902765872025, 0.006522892184374938, 0.00666456514496097, 0.0060703612507235225, 0.0039005543823661705, 0.007534783287107425, 0.003504374816874313, 0.003064219446502896, 0.003535174273336057, 0.003182217491508925, 0.003517319538326573, 0.0019783579049302462, 0.002732085993806025, 0.0030624240098860436, 0.0018645084705451696, 0.0020679265964156602, 0.0023472280655779405, 0.0024171192163653073, 0.0018501097595680568, 0.002168553077279782, 0.0018202735833844708, 0.0019209818917864491, 0.001565523971749532, 0.0020542012698717906, 0.0019428366595558811, 0.0015490635749328316, 0.0021401611612022094, 0.0040556767974919, 0.0014189336323666565, 0.0036764248938336904, 0.001334067510454012, 0.0012708283494939664, 0.0012477377896965138, 0.0013834466718589248, 0.0008642558436396653, 0.001210943299031542, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0133463260075684, 0.9900635310206808, 1.0070792513887206, 0.9992136738587244, 1.0004490817031144, 1.0013795976244702, 0.9819184287981335, 1.0060437334074896, 1.007687931038028, 0.9994715901316029, 0.9889818617249001, 1.0157103095167836, 0.9915642328727003, 0.9875671554157701, 0.9852339522162081, 0.9999603091913989, 1.0062208499055516, 0.970832784006288, 0.9894020063100712, 1.0012261331751717, 0.9796059692960719, 1.0047762561906273, 0.9906489068845067, 0.9938294940754425, 0.9973679395329852, 1.0072870489537156, 0.9908578401720828, 0.9986373856735861, 1.0014020077785963, 1.017816100515748, 1.016608078183308, 0.9849421877910904, 1.0036519031084152, 1.0094492084755757, 0.9922028681584875, 1.0028893031737716, 0.9889235795788583, 0.9825236510063379, 1.0064998624050048, 0.9977510628112557, 0.9706944704593804, 1.026477141555583, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0068146249746082, 1.0052407284472429, 1.0051815688808263, 1.0051954283943745, 1.0052379087077568, 1.0051973803078573, 1.0053029152058741, 1.0052901783073926, 1.0052432446622634, 1.0052940532914456, 1.0053280883218554, 1.005506543569211, 1.0053951793475338, 1.0054032897276008, 1.00550374968055, 1.0055429529178626, 1.005568264552406, 1.0056370016690148, 1.005699941831713, 1.0057771133697506, 1.0058885888050846, 1.0058203306167275, 1.0059772898178083, 1.005967796509546, 1.0060261562019122, 1.0061292275576612, 1.0062922564546375, 1.0064094406754387, 1.0063679386828988, 1.0063541400681575, 1.006525174492343, 1.0065331240250894, 1.006651883356626, 1.0068095970434485, 1.0068297293039197, 1.0079607738750667, 1.0071803698254111, 1.0073467011014874, 1.0073736215695388, 1.00742757839767, 1.0077156748889853, 1.0082557730475235, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0262215587332173, 1.0004417571149213, 1.0174996533093823, 1.0092069072747918, 1.012789132485126, 1.0127959497559291, 0.9913242846212175, 1.0178884561243382, 1.0213912520417465, 1.0133488902102976, 0.9988713401187596, 1.0367422513177997, 1.0023029266544063, 0.9977317669820309, 0.9978593362846478, 1.01223994110356, 1.0207457449671502, 0.9795685067080004, 1.00223731825098, 1.0165078644104883, 0.9895270957253919, 1.0163728060824844, 1.0045319860777504, 1.0088797952307842, 1.0095202408893422, 1.022361519794555, 1.003988201231277, 1.013233818498974, 1.0138335455258285, 1.0349533668295678, 1.0334637346317754, 0.9989028703449572, 1.0238035213557646, 1.049172680160613, 1.006639495661784, 1.0419460017750983, 1.0035250544958292, 0.9969177253003719, 1.0212727858882766, 1.0147261155648934, 0.9817068265779344, 1.0449178409409672, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 0.9931853750253917, 0.9947592715527571, 0.9948184311191737, 0.9948045716056255, 0.9947620912922432, 0.9948026196921426, 0.994697084794126, 0.9947098216926075, 0.9947567553377366, 0.9947059467085544, 0.9946719116781447, 0.9944934564307889, 0.9946048206524664, 0.994596710272399, 0.9944962503194501, 0.9944570470821374, 0.9944317354475939, 0.9943629983309851, 0.994300058168287, 0.9942228866302494, 0.9941114111949154, 0.9941796693832726, 0.9940227101821918, 0.9940322034904541, 0.993973843798088, 0.9938707724423388, 0.9937077435453624, 0.9935905593245614, 0.9936320613171012, 0.9936458599318425, 0.9934748255076571, 0.9934668759749106, 0.993348116643374, 0.9931904029565514, 0.9931702706960803, 0.9920392261249333, 0.9928196301745889, 0.9926532988985127, 0.9926263784304613, 0.99257242160233, 0.9922843251110147, 0.9917442269524764, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0004710932819192, 0.9796853049264401, 0.9966588494680588, 0.989220440442657, 0.9881090309211031, 0.9899632454930111, 0.9725125729750496, 0.9941990106906412, 0.9939846100343094, 0.9855942900529081, 0.9790923833310406, 0.9946783677157677, 0.9808255390909945, 0.9774025438495093, 0.9726085681477684, 0.9876806772792377, 0.9916959548439531, 0.9620970613045755, 0.9765666943691624, 0.9859444019398551, 0.9696848428667519, 0.9931797062987703, 0.976765827691263, 0.9787791929201007, 0.9852156381766282, 0.9922125781128763, 0.9777274791128886, 0.9840409528481981, 0.9889704700313642, 1.0006788342019282, 0.9997524217348406, 0.9709815052372237, 0.983500284861066, 0.9697257367905386, 0.9777662406551909, 0.9638326045724448, 0.9743221046618875, 0.9681295767123039, 0.9917269389217328, 0.9807760100576179, 0.9596821143408265, 1.0080364421701984, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.006814624974608274, 0.005240728447242882, 0.005181568880826326, 0.0051954283943744795, 0.005237908707756755, 0.005197380307857435, 0.005302915205874004, 0.005290178307392535, 0.0052432446622634465, 0.005294053291445611, 0.005328088321855273, 0.0055065435692110976, 0.005395179347533641, 0.005403289727600957, 0.0055037496805498964, 0.005542952917862554, 0.00556826455240611, 0.005637001669014929, 0.005699941831712962, 0.005777113369750619, 0.0058885888050845825, 0.005820330616727376, 0.005977289817808207, 0.005967796509545931, 0.006026156201912047, 0.00612922755766121, 0.006292256454637601, 0.006409440675438582, 0.006367938682898755, 0.006354140068157488, 0.006525174492342911, 0.006533124025089432, 0.006651883356626032, 0.006809597043448634, 0.006829729303919674, 0.007960773875066662, 0.007180369825411148, 0.007346701101487274, 0.007373621569538691, 0.007427578397670054, 0.00771567488898528, 0.008255773047523562, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.006814624974608163, 0.005240728447242882, 0.005181568880826326, 0.0051954283943744795, 0.005237908707756755, 0.005197380307857324, 0.005302915205874115, 0.005290178307392646, 0.0052432446622634465, 0.005294053291445611, 0.005328088321855384, 0.0055065435692109865, 0.005395179347533752, 0.005403289727600846, 0.0055037496805498964, 0.005542952917862554, 0.005568264552405999, 0.005637001669014818, 0.005699941831712962, 0.005777113369750619, 0.0058885888050845825, 0.005820330616727487, 0.005977289817808318, 0.005967796509545931, 0.006026156201912158, 0.00612922755766121, 0.00629225645463749, 0.0064094406754386934, 0.006367938682898755, 0.006354140068157488, 0.006525174492342911, 0.006533124025089432, 0.006651883356626032, 0.006809597043448523, 0.006829729303919674, 0.007960773875066662, 0.007180369825411148, 0.007346701101487385, 0.007373621569538802, 0.007427578397670054, 0.00771567488898528, 0.008255773047523451, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [0.0, 0.012875232725649166, 0.010378226094240661, 0.010420401920661737, 0.009993233416067393, 0.01234005078201128, 0.011416352131459084, 0.009405855823083953, 0.011844722716848444, 0.013703321003718627, 0.01387730007869481, 0.009889478393859452, 0.021031941801015974, 0.010738693781705888, 0.010164611566260806, 0.012625384068439716, 0.012279631912161193, 0.014524895061598486, 0.008735722701712523, 0.012835311940908811, 0.01528173123531662, 0.00992112642931997, 0.011596549891856989, 0.01388307919324372, 0.015050301155341783, 0.012152301356357031, 0.015074470840839238, 0.013130361059194184, 0.014596432825387917, 0.012431537747232158, 0.017137266313819843, 0.016855656448467427, 0.013960682553866732, 0.020151618247349234, 0.03972347168503709, 0.01443662750329655, 0.03905669860132677, 0.014601474916970836, 0.014394074294033943, 0.014772923483271971, 0.016975052753637754, 0.01101235611855389, 0.018440699385384507, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.012875232725648944, 0.01037822609424055, 0.010420401920661737, 0.009993233416067393, 0.012340050782011502, 0.011416352131458973, 0.009405855823083953, 0.011844722716848555, 0.013703321003718516, 0.013877300078694699, 0.009889478393859452, 0.021031941801016085, 0.010738693781705999, 0.010164611566260806, 0.012625384068439716, 0.012279631912161193, 0.014524895061598597, 0.008735722701712412, 0.012835311940908811, 0.01528173123531662, 0.00992112642931997, 0.0115965498918571, 0.01388307919324372, 0.015050301155341672, 0.012152301356357031, 0.01507447084083946, 0.013130361059194295, 0.014596432825387917, 0.012431537747232158, 0.017137266313819843, 0.016855656448467427, 0.013960682553866732, 0.020151618247349345, 0.039723471685037204, 0.01443662750329644, 0.03905669860132677, 0.014601474916970836, 0.014394074294034054, 0.01477292348327186, 0.016975052753637754, 0.011012356118554001, 0.018440699385384285, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}