
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
  'curve0' : [6.190658571428571, 3.453108571428571, 2.030852857142858, 1.4298085714285707, 1.111053714285715, 0.8859371428571428, 0.7427554285714285, 0.6417835714285709, 0.5610028571428575, 0.4977708571428575, 0.4462672857142853, 0.40539028571428604, 0.36826671428571395, 0.3357458571428574, 0.3092212857142854, 0.2854745714285712, 0.26641257142857205, 0.24719442857142837, 0.23014585714285693, 0.2169340000000005, 0.20175199999999982, 0.18891899999999984, 0.17698242857142843, 0.1677995714285718, 0.15665942857142845, 0.14985814285714275, 0.1406842285714289, 0.13101592857142846, 0.12317031428571458, 0.11788117142857095, 0.11055667142857169, 0.10317094285714244, 0.0962146142857145, 0.09048511428571449, 0.08395737142857108, 0.07922062857142875, 0.07296515714285731, 0.06823845714285687, 0.06240382857142871, 0.0575265285714287, 0.05259962857142836, 0.04712528571428582, 0.0420985000000001, 0.03641468571428557, 0.02969900000000007, 0.02359377142857133, 0.019427742857142903, 0.015874128571428607, 0.013801759999999944, 0.01203952571428574, 0.010217865714285738, 0.009230789999999963, 0.008041872857142874, 0.007243242857142873, 0.006231152857142832, 0.005181217142857154, 0.004697825714285695, 0.004223234285714322, 0.003385317142857129, 0.002939309999999988, 0.002574630000000022, 0.0020366242857142777, 0.0017528557142857072, 0.001428384142857137, 0.0011592795714285816, 0.0008012174285714253, 0.0005967741428571405, 0.0004702755714285755, 0.00028689871428571315, 0.00015011171428571367, 4.63835000000004e-05, 2.759112857142846e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [6.164684285714285, 3.4794671428571426, 2.023381428571429, 1.4295114285714279, 1.0969834285714293, 0.8865775714285713, 0.7503605714285714, 0.642934428571428, 0.5617094285714289, 0.4988431428571432, 0.44654128571428536, 0.4033271428571431, 0.3665022857142854, 0.33619100000000024, 0.312242714285714, 0.28714985714285685, 0.2652967142857149, 0.24742799999999976, 0.23067842857142837, 0.21538257142857192, 0.20241757142857125, 0.18973399999999985, 0.1782077142857141, 0.16758457142857183, 0.15803799999999987, 0.14856942857142844, 0.13973962857142888, 0.13094649999999988, 0.12359680000000028, 0.11691121428571383, 0.10942001428571453, 0.10274872857142815, 0.0963651142857145, 0.08991370000000021, 0.08420622857142823, 0.07913570000000018, 0.07263624285714303, 0.06757247142857115, 0.06254842857142871, 0.05652851428571441, 0.0517168857142855, 0.046496671428571536, 0.04124442857142867, 0.035932057142856993, 0.030092900000000068, 0.023897328571428473, 0.018637128571428616, 0.015719214285714322, 0.013314241428571376, 0.011465774285714311, 0.010214811428571452, 0.008815628571428535, 0.007773471428571446, 0.006697927142857158, 0.005960572857142833, 0.005096242857142869, 0.004465325714285697, 0.003867928571428605, 0.0032918371428571295, 0.0028020399999999887, 0.002388398571428592, 0.0020175457142857065, 0.0016295471428571363, 0.001269510571428566, 0.0010437875714285805, 0.0007510834285714256, 0.000588406571428569, 0.0003620557142857174, 0.0002488785714285704, 0.00013343544285714231, 4.1216271428571784e-05, 1.8281599999999927e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [6.190658571428571, 6.190658571428571, 3.453108571428571, 2.030852857142858, 1.4298085714285707, 1.111053714285715, 0.8859371428571428, 0.7427554285714285, 0.6417835714285709, 0.5610028571428575, 0.4977708571428575, 0.4462672857142853, 0.40539028571428604, 0.36826671428571395, 0.3357458571428574, 0.3092212857142854, 0.2854745714285712, 0.26641257142857205, 0.24719442857142837, 0.23014585714285693, 0.2169340000000005, 0.20175199999999982, 0.18891899999999984, 0.17698242857142843, 0.1677995714285718, 0.15665942857142845, 0.14985814285714275, 0.1406842285714289, 0.13101592857142846, 0.12317031428571458, 0.11788117142857095, 0.11055667142857169, 0.10317094285714244, 0.0962146142857145, 0.09048511428571449, 0.08395737142857108, 0.07922062857142875, 0.07296515714285731, 0.06823845714285687, 0.06240382857142871, 0.0575265285714287, 0.05259962857142836, 0.04712528571428582, 0.0420985000000001, 0.03641468571428557, 0.02969900000000007, 0.02359377142857133, 0.019427742857142903, 0.015874128571428607, 0.013801759999999944, 0.01203952571428574, 0.010217865714285738, 0.009230789999999963, 0.008041872857142874, 0.007243242857142873, 0.006231152857142832, 0.005181217142857154, 0.004697825714285695, 0.004223234285714322, 0.003385317142857129, 0.002939309999999988, 0.002574630000000022, 0.0020366242857142777, 0.0017528557142857072, 0.001428384142857137, 0.0011592795714285816, 0.0008012174285714253, 0.0005967741428571405, 0.0004702755714285755, 0.00028689871428571315, 0.00015011171428571367, 4.63835000000004e-05, 2.759112857142846e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [6.164684285714285, 6.164684285714285, 3.4794671428571426, 2.023381428571429, 1.4295114285714279, 1.0969834285714293, 0.8865775714285713, 0.7503605714285714, 0.642934428571428, 0.5617094285714289, 0.4988431428571432, 0.44654128571428536, 0.4033271428571431, 0.3665022857142854, 0.33619100000000024, 0.312242714285714, 0.28714985714285685, 0.2652967142857149, 0.24742799999999976, 0.23067842857142837, 0.21538257142857192, 0.20241757142857125, 0.18973399999999985, 0.1782077142857141, 0.16758457142857183, 0.15803799999999987, 0.14856942857142844, 0.13973962857142888, 0.13094649999999988, 0.12359680000000028, 0.11691121428571383, 0.10942001428571453, 0.10274872857142815, 0.0963651142857145, 0.08991370000000021, 0.08420622857142823, 0.07913570000000018, 0.07263624285714303, 0.06757247142857115, 0.06254842857142871, 0.05652851428571441, 0.0517168857142855, 0.046496671428571536, 0.04124442857142867, 0.035932057142856993, 0.030092900000000068, 0.023897328571428473, 0.018637128571428616, 0.015719214285714322, 0.013314241428571376, 0.011465774285714311, 0.010214811428571452, 0.008815628571428535, 0.007773471428571446, 0.006697927142857158, 0.005960572857142833, 0.005096242857142869, 0.004465325714285697, 0.003867928571428605, 0.0032918371428571295, 0.0028020399999999887, 0.002388398571428592, 0.0020175457142857065, 0.0016295471428571363, 0.001269510571428566, 0.0010437875714285805, 0.0007510834285714256, 0.000588406571428569, 0.0003620557142857174, 0.0002488785714285704, 0.00013343544285714231, 4.1216271428571784e-05, 1.8281599999999927e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.033339407949886865, 0.024370599550462016, 0.014847922963382143, 0.011580814535520475, 0.008438700934941814, 0.006437869466314622, 0.00544313085176057, 0.004822458091141517, 0.0040995283451954875, 0.003533586372661809, 0.0030134910936368397, 0.0027813933521873254, 0.0024972098716081375, 0.0022139372997776936, 0.002015999777291855, 0.0018092833173521978, 0.0017028523489865447, 0.0015249329192339122, 0.0014175388991531208, 0.001387888279924227, 0.001195858499581119, 0.001099268959307938, 0.0010728968035279096, 0.000996748079854625, 0.000921132289021262, 0.0009089654356824052, 0.0008421149274418614, 0.0007501922202655381, 0.0007083795823236745, 0.0007005366747380591, 0.000655546352600764, 0.0006359020589457353, 0.0006029905065756922, 0.0005793079967530591, 0.0005515362589150025, 0.0005366694342261859, 0.0005127896891573812, 0.0004969314000206956, 0.00047360148579469194, 0.0004559656718192193, 0.00043587385836748883, 0.00041035790749649107, 0.000386592333929505, 0.000359882378744238, 0.000322651514795763, 0.00028702264719007687, 0.00026064547037017564, 0.0002331864455051948, 0.0002179052405922139, 0.00020520368179057695, 0.00018491051338197033, 0.00017488836089205582, 0.00016295548409279905, 0.00015219918474398869, 0.0001397578080035567, 0.00012267421597591808, 0.00011614075731716222, 0.00010958988483041243, 9.389079631493702e-05, 8.682465322800433e-05, 7.915853377487397e-05, 6.648599668427935e-05, 6.138287336755352e-05, 5.402705293627969e-05, 4.6428945053442116e-05, 3.7279096292803985e-05, 3.0332958433804828e-05, 2.6893596081671454e-05, 1.9178075279562557e-05, 1.2627132270937602e-05, 6.376348196776217e-06, 9.840795969133882e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.01882237595880748, 0.01467497522857138, 0.008435221347639521, 0.005960031844867668, 0.0045863484207738425, 0.0037313913802565733, 0.003158066445385433, 0.0027313482504627835, 0.00240725222303483, 0.0021547905812351227, 0.0019440280085325872, 0.001781745303496158, 0.0016291383724947029, 0.0015086512424773908, 0.0014118189888023371, 0.0013136332231250686, 0.0012299691384878972, 0.0011584930394477892, 0.0010997215788645807, 0.0010515159125214033, 0.0009903406958605453, 0.0009395977211291112, 0.0008948065575923116, 0.0008525045933205618, 0.0008198621088640573, 0.0007850265821574938, 0.0007520662693336209, 0.0007165428622695134, 0.0006892194638776224, 0.0006632211131274061, 0.0006393662359504694, 0.00063015741473614, 0.0005943121560051686, 0.0005606728829118227, 0.0005380363010285528, 0.0005198143310601503, 0.0004928639751079245, 0.0004699494110854806, 0.00045089740450323735, 0.00042349011505703557, 0.0004069591565526441, 0.000379299004340742, 0.0003514475314281484, 0.00031662837935384766, 0.00028231690834006783, 0.0002247735368257181, 0.000188880482672758, 0.00016841706006948674, 0.0001835218387716355, 0.00011839318789007911, 0.0002923446735674616, 0.00011519066713895817, 9.595599544178849e-05, 9.004843367967765e-05, 0.00012795186435467286, 7.170063899752279e-05, 6.678431625733056e-05, 5.943679544744387e-05, 7.375926091975521e-05, 6.192006038071176e-05, 5.535309662631805e-05, 4.372750267046934e-05, 4.5594933481513676e-05, 2.968488243025315e-05, 3.204298133852782e-05, 2.391568096288213e-05, 2.393644646533295e-05, 1.828861584122103e-05, 2.113499853951503e-05, 1.9851247840282568e-05, 3.291669448031231e-06, 4.000773139567599e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.033339407949886865, 0.024370599550462016, 0.014847922963382143, 0.011580814535520475, 0.008438700934941814, 0.006437869466314622, 0.00544313085176057, 0.004822458091141517, 0.0040995283451954875, 0.003533586372661809, 0.0030134910936368397, 0.0027813933521873254, 0.0024972098716081375, 0.0022139372997776936, 0.002015999777291855, 0.0018092833173521978, 0.0017028523489865447, 0.0015249329192339122, 0.0014175388991531208, 0.001387888279924227, 0.001195858499581119, 0.001099268959307938, 0.0010728968035279096, 0.000996748079854625, 0.000921132289021262, 0.0009089654356824052, 0.0008421149274418614, 0.0007501922202655381, 0.0007083795823236745, 0.0007005366747380591, 0.000655546352600764, 0.0006359020589457353, 0.0006029905065756922, 0.0005793079967530591, 0.0005515362589150025, 0.0005366694342261859, 0.0005127896891573812, 0.0004969314000206956, 0.00047360148579469194, 0.0004559656718192193, 0.00043587385836748883, 0.00041035790749649107, 0.000386592333929505, 0.000359882378744238, 0.000322651514795763, 0.00028702264719007687, 0.00026064547037017564, 0.0002331864455051948, 0.0002179052405922139, 0.00020520368179057695, 0.00018491051338197033, 0.00017488836089205582, 0.00016295548409279905, 0.00015219918474398869, 0.0001397578080035567, 0.00012267421597591808, 0.00011614075731716222, 0.00010958988483041243, 9.389079631493702e-05, 8.682465322800433e-05, 7.915853377487397e-05, 6.648599668427935e-05, 6.138287336755352e-05, 5.402705293627969e-05, 4.6428945053442116e-05, 3.7279096292803985e-05, 3.0332958433804828e-05, 2.6893596081671454e-05, 1.9178075279562557e-05, 1.2627132270937602e-05, 6.376348196776217e-06, 9.840795969133882e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.01882237595880748, 0.01467497522857138, 0.008435221347639521, 0.005960031844867668, 0.0045863484207738425, 0.0037313913802565733, 0.003158066445385433, 0.0027313482504627835, 0.00240725222303483, 0.0021547905812351227, 0.0019440280085325872, 0.001781745303496158, 0.0016291383724947029, 0.0015086512424773908, 0.0014118189888023371, 0.0013136332231250686, 0.0012299691384878972, 0.0011584930394477892, 0.0010997215788645807, 0.0010515159125214033, 0.0009903406958605453, 0.0009395977211291112, 0.0008948065575923116, 0.0008525045933205618, 0.0008198621088640573, 0.0007850265821574938, 0.0007520662693336209, 0.0007165428622695134, 0.0006892194638776224, 0.0006632211131274061, 0.0006393662359504694, 0.00063015741473614, 0.0005943121560051686, 0.0005606728829118227, 0.0005380363010285528, 0.0005198143310601503, 0.0004928639751079245, 0.0004699494110854806, 0.00045089740450323735, 0.00042349011505703557, 0.0004069591565526441, 0.000379299004340742, 0.0003514475314281484, 0.00031662837935384766, 0.00028231690834006783, 0.0002247735368257181, 0.000188880482672758, 0.00016841706006948674, 0.0001835218387716355, 0.00011839318789007911, 0.0002923446735674616, 0.00011519066713895817, 9.595599544178849e-05, 9.004843367967765e-05, 0.00012795186435467286, 7.170063899752279e-05, 6.678431625733056e-05, 5.943679544744387e-05, 7.375926091975521e-05, 6.192006038071176e-05, 5.535309662631805e-05, 4.372750267046934e-05, 4.5594933481513676e-05, 2.968488243025315e-05, 3.204298133852782e-05, 2.391568096288213e-05, 2.393644646533295e-05, 1.828861584122103e-05, 2.113499853951503e-05, 1.9851247840282568e-05, 3.291669448031231e-06, 4.000773139567599e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.9958042774585949, 0.9958042774585949, 1.0076332877705223, 0.9963210389442295, 0.9997921799721442, 0.9873360886756664, 1.0007228826295318, 1.0102390942759856, 1.001793216894436, 1.001259479197967, 1.0021541753577952, 1.0006139818193518, 0.9949107244799719, 0.9952088296254229, 1.0013258327621104, 1.0097710885731854, 1.0058684236074065, 0.9958115447147495, 1.0009448895346114, 1.0023140604622782, 0.9928483844329217, 1.0032989582684257, 1.0043140181771024, 1.0069232054513884, 0.9987187094807838, 1.0087997986533117, 0.9914004387005996, 0.9932856723913411, 0.9994700753398033, 1.0034625690188335, 0.9917717381741081, 0.9897187828814878, 0.9959076240458622, 1.001564211436249, 0.9936849912803338, 1.002964089258903, 0.9989279487810174, 0.9954921732701774, 0.9902403169390028, 1.0023171655218956, 0.9826512339524348, 0.983217697897921, 0.9866607856867863, 0.9797125448989529, 0.9867463205582675, 1.013263072830735, 1.0128659864225669, 0.9593048821199728, 0.9902410841000047, 0.9646770722408903, 0.9523443495875727, 0.9997010837879758, 0.955024279766799, 0.9666245123071013, 0.9247138712534048, 0.956576253832414, 0.983599551346457, 0.9505090196741472, 0.915868812798857, 0.9723866343815857, 0.9532985632682501, 0.9276667215982768, 0.9906322577205839, 0.9296527544032229, 0.888773918260684, 0.9003760586778217, 0.9374277215993805, 0.9859786629016624, 0.7698799093176067, 0.8674788663595064, 0.8889075945343564, 0.8885977002289915, 0.6625897868828438, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.005385438005539, 1.007057582768207, 1.0073111761451154, 1.0080995559594035, 1.0075952231889769, 1.0072667338966652, 1.0073282949439086, 1.0075141501057858, 1.0073074999405065, 1.0070988213189982, 1.006752659650625, 1.0068610261523325, 1.006780981757886, 1.00659408672565, 1.0065196022086091, 1.006337809032511, 1.0063917867683774, 1.0061689615257379, 1.0061593066099521, 1.006397744382735, 1.005927368747676, 1.00581873162206, 1.0060621656747968, 1.0059401109989063, 1.0058798394544206, 1.0060655058067076, 1.0059858516906484, 1.0057259619379528, 1.0057512200600582, 1.0059427359454307, 1.0059295051499837, 1.0061635770822241, 1.0062671405072112, 1.0064022463951787, 1.006569241622628, 1.006774364757057, 1.0070278706883808, 1.0072822777774761, 1.0075893017565838, 1.0079261808967503, 1.0082866337692022, 1.0087078073114386, 1.0091830429571007, 1.009882891247996, 1.0108640531598962, 1.0121651872427018, 1.013416147840064, 1.0146897163177133, 1.0157882212552758, 1.0170441665776824, 1.018096784451125, 1.0189461964676974, 1.020263374836629, 1.021012575133236, 1.0224288845431468, 1.0236767177660249, 1.0247222362813477, 1.0259492790161122, 1.0277347120972233, 1.0295391276279142, 1.0307455959787903, 1.0326451948700797, 1.0350187827025839, 1.0378238957681312, 1.0400498259416644, 1.0465280646219501, 1.050828204936262, 1.0571868872541597, 1.0668461527522348, 1.084118233750258, 1.1374701822151447, 1.356665220984268, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.9988447255372012, 1.011883074571318, 1.0004745753848296, 1.003960592418373, 0.991464015491268, 1.0049346841217042, 1.0144909197408756, 1.0060490881445878, 1.0055504595243325, 1.0064830559065747, 1.004970178365153, 0.9993058601462269, 0.9996326298476464, 1.005819264953101, 1.0143368123898402, 1.0104700006114504, 1.000428328119123, 1.0056314556766677, 1.0070924283743368, 0.997695554136709, 1.0082076615073554, 1.0092875662115992, 1.0119791116496197, 1.003799202750598, 1.014033202836771, 0.9966389033391599, 0.9986314476567739, 1.004939203178552, 1.0090582311544263, 0.9973979217714545, 0.9955019366947206, 1.0020155202934395, 1.0077411541015318, 0.9998812909406454, 1.0093725354962448, 1.0054895519951532, 1.0022469586281113, 0.9971271873455486, 1.00954264214449, 0.9900128830137233, 0.9909546186254127, 0.994709522126081, 0.9880607647031775, 0.9954413943490494, 1.0227690127054805, 1.0223928031719027, 0.9690270862927192, 1.0008506151562553, 0.9779740603620891, 0.9621780582152805, 1.0283122127401532, 0.9675032406291909, 0.9785565581310488, 0.9371459317897813, 0.9771104739499643, 0.9974381219024835, 0.9647250251879842, 0.9299425750924851, 0.9941746258184837, 0.974364752401316, 0.949166159042227, 1.0121028367454892, 0.9556645550950406, 0.9095560605007088, 0.9280164847909473, 0.9672768987516097, 1.0260883874127376, 0.8087690563461564, 0.9411459742520408, 1.0211507571332386, 0.9595640880184253, 0.8075919432538788, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [0.9946145619944611, 0.9929424172317931, 0.9926888238548847, 0.9919004440405965, 0.992404776811023, 0.9927332661033349, 0.9926717050560915, 0.9924858498942142, 0.9926925000594934, 0.9929011786810016, 0.9932473403493749, 0.9931389738476674, 0.9932190182421138, 0.99340591327435, 0.9934803977913907, 0.9936621909674891, 0.9936082132316226, 0.993831038474262, 0.9938406933900478, 0.993602255617265, 0.994072631252324, 0.9941812683779402, 0.9939378343252031, 0.9940598890010938, 0.9941201605455794, 0.9939344941932924, 0.9940141483093516, 0.9942740380620472, 0.9942487799399419, 0.9940572640545692, 0.9940704948500164, 0.993836422917776, 0.9937328594927889, 0.9935977536048212, 0.993430758377372, 0.993225635242943, 0.9929721293116193, 0.9927177222225237, 0.9924106982434163, 0.9920738191032497, 0.9917133662307978, 0.9912921926885615, 0.9908169570428993, 0.9901171087520041, 0.9891359468401036, 0.9878348127572982, 0.9865838521599359, 0.9853102836822866, 0.9842117787447242, 0.9829558334223176, 0.9819032155488748, 0.9810538035323026, 0.979736625163371, 0.9789874248667642, 0.9775711154568532, 0.9763232822339752, 0.9752777637186523, 0.9740507209838878, 0.9722652879027768, 0.9704608723720858, 0.9692544040212095, 0.9673548051299204, 0.9649812172974163, 0.962176104231869, 0.9599501740583356, 0.9534719353780499, 0.9491717950637379, 0.9428131127458403, 0.9331538472477652, 0.9158817662497419, 0.8625298177848554, 0.643334779015732, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.9927638293799886, 1.0033835009697267, 0.9921675025036294, 0.9956237675259153, 0.9832081618600648, 0.9965110811373596, 1.0059872688110953, 0.9975373456442839, 0.9969684988716014, 0.9978252948090154, 0.9962577852735507, 0.9905155888137168, 0.9907850294031993, 0.99683240057112, 1.0052053647565307, 1.0012668466033623, 0.9911947613103761, 0.9962583233925552, 0.99753569255022, 0.9880012147291344, 0.9983902550294961, 0.9993404701426055, 1.0018672992531572, 0.9936382162109696, 1.0035663944698523, 0.9861619740620391, 0.9879398971259084, 0.9940009475010544, 0.9978669068832409, 0.9861455545767618, 0.983935629068255, 0.9897997277982851, 0.9953872687709661, 0.9874886916200223, 0.9965556430215609, 0.9923663455668816, 0.9887373879122434, 0.983353446532457, 0.9950916888993014, 0.9752895848911464, 0.9754807771704294, 0.9786120492474917, 0.9713643250947284, 0.9780512467674856, 1.0037571329559896, 1.0033391696732308, 0.9495826779472264, 0.9796315530437542, 0.9513800841196914, 0.9425106409598651, 0.9710899548357983, 0.9425453189044072, 0.9546924664831538, 0.9122818107170281, 0.9360420337148637, 0.9697609807904306, 0.9362930141603103, 0.9017950505052288, 0.9505986429446878, 0.9322323741351842, 0.9061672841543265, 0.9691616786956788, 0.9036409537114052, 0.867991776020659, 0.8727356325646959, 0.9075785444471511, 0.9458689383905872, 0.7309907622890571, 0.793811758466972, 0.7566644319354743, 0.8176313124395578, 0.5175876305118089, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.005385438005538923, 0.007057582768206894, 0.007311176145115339, 0.008099555959403482, 0.007595223188976985, 0.007266733896665101, 0.00732829494390852, 0.007514150105785822, 0.007307499940506612, 0.007098821318998416, 0.0067526596506251035, 0.006861026152332639, 0.0067809817578862175, 0.0065940867256499835, 0.006519602208609254, 0.0063378090325109104, 0.006391786768377372, 0.0061689615257379815, 0.006159306609952231, 0.006397744382734993, 0.005927368747675965, 0.005818731622059814, 0.006062165674796893, 0.005940110998906234, 0.00587983945442061, 0.006065505806707616, 0.005985851690648358, 0.005725961937952828, 0.0057512200600581265, 0.0059427359454308215, 0.005929505149983583, 0.0061635770822240366, 0.006267140507211111, 0.006402246395178834, 0.006569241622627953, 0.00677436475705695, 0.007027870688380733, 0.007282277777476254, 0.007589301756583677, 0.007926180896750346, 0.008286633769202245, 0.008707807311438498, 0.009183042957100707, 0.009882891247995906, 0.010864053159896359, 0.01216518724270177, 0.013416147840064063, 0.01468971631771343, 0.01578822125527579, 0.017044166577682374, 0.01809678445112517, 0.01894619646769735, 0.02026337483662899, 0.021012575133235845, 0.022428884543146843, 0.023676717766024757, 0.02472223628134773, 0.025949279016112214, 0.027734712097223224, 0.02953912762791422, 0.030745595978790452, 0.03264519487007955, 0.03501878270258374, 0.037823895768131055, 0.040049825941664396, 0.04652806462195014, 0.050828204936262056, 0.05718688725415966, 0.06684615275223482, 0.08411823375025806, 0.13747018221514462, 0.356665220984268, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.005385438005538923, 0.007057582768206894, 0.00731117614511545, 0.008099555959403482, 0.007595223188976874, 0.007266733896665212, 0.007328294943908631, 0.007514150105785822, 0.007307499940506501, 0.007098821318998194, 0.0067526596506251035, 0.006861026152332528, 0.0067809817578861065, 0.0065940867256499835, 0.006519602208609143, 0.0063378090325110215, 0.006391786768377372, 0.0061689615257378705, 0.00615930660995212, 0.006397744382734993, 0.005927368747675965, 0.005818731622059925, 0.006062165674796782, 0.005940110998906345, 0.00587983945442061, 0.006065505806707616, 0.005985851690648358, 0.005725961937952828, 0.0057512200600582375, 0.0059427359454307105, 0.005929505149983694, 0.006163577082224148, 0.006267140507211222, 0.006402246395178723, 0.006569241622627953, 0.006774364757057061, 0.007027870688380844, 0.007282277777476143, 0.007589301756583788, 0.007926180896750346, 0.008286633769202245, 0.008707807311438609, 0.009183042957100707, 0.009882891247996017, 0.010864053159896248, 0.01216518724270177, 0.013416147840064063, 0.01468971631771332, 0.01578822125527579, 0.017044166577682374, 0.01809678445112506, 0.01894619646769735, 0.02026337483662899, 0.021012575133235956, 0.022428884543146843, 0.02367671776602487, 0.02472223628134773, 0.025949279016112214, 0.027734712097223335, 0.02953912762791422, 0.03074559597879034, 0.032645194870079663, 0.03501878270258385, 0.037823895768131166, 0.040049825941664396, 0.04652806462195014, 0.050828204936262056, 0.05718688725415966, 0.06684615275223482, 0.08411823375025795, 0.13747018221514473, 0.356665220984268, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [0.0030404480786062615, 0.004249786800795574, 0.004153536440600125, 0.004168412446228897, 0.00412792681560159, 0.004211801492172151, 0.004251825464890224, 0.004255871250152032, 0.0042909803263655455, 0.004328880548779779, 0.004356196545801105, 0.004395135666255046, 0.004423800222223551, 0.00449343219099041, 0.004565723816654765, 0.004601577004044177, 0.004616783404373437, 0.004686566142056203, 0.004778367912058212, 0.004847169703787291, 0.004908703238929668, 0.0049735480344969, 0.005055906198231153, 0.00508049326981419, 0.005233404183459411, 0.0052384646385604805, 0.005345775265432784, 0.005469127838748866, 0.005595662135592594, 0.005626183597346346, 0.0057831538132328, 0.006107896247577127, 0.006176942665283014, 0.006196299660311544, 0.006408446237342047, 0.006561603214135792, 0.006754785357933946, 0.006886870406545786, 0.007225476622594207, 0.007361649061288444, 0.0077369207274916585, 0.008048736439294601, 0.00834821980422451, 0.008695073790781938, 0.009505939874745462, 0.009526816749336087, 0.009722204172746385, 0.01060953105625051, 0.013296988121198838, 0.009833708627707605, 0.028611128952177545, 0.012478960862391864, 0.011932045823947579, 0.012432060536376688, 0.02053422011755024, 0.013838570556026442, 0.014216005513836949, 0.014073762293628223, 0.021787991436897913, 0.021066189133065905, 0.02149943744395033, 0.021470579024905123, 0.026011800691817744, 0.020782142240024948, 0.027640426113125782, 0.029849177152229345, 0.040109724511075195, 0.03888914702854962, 0.07366710789253439, 0.13224316259888214, 0.07096638778943376, 0.14500215637103486, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0030404480786062615, 0.004249786800795796, 0.004153536440600125, 0.004168412446228786, 0.00412792681560159, 0.004211801492172373, 0.004251825464890002, 0.004255871250151921, 0.0042909803263655455, 0.004328880548779557, 0.004356196545801216, 0.004395135666255046, 0.004423800222223551, 0.004493432190990632, 0.004565723816654765, 0.004601577004043955, 0.004616783404373548, 0.004686566142056314, 0.004778367912058545, 0.004847169703787291, 0.004908703238929668, 0.004973548034496789, 0.005055906198231375, 0.00508049326981419, 0.005233404183459189, 0.0052384646385603695, 0.005345775265432784, 0.005469127838748755, 0.005595662135592816, 0.005626183597346346, 0.0057831538132328, 0.006107896247577349, 0.006176942665282681, 0.006196299660311544, 0.006408446237341936, 0.006561603214135792, 0.006754785357933946, 0.006886870406545786, 0.007225476622594318, 0.007361649061288444, 0.0077369207274916585, 0.008048736439294712, 0.008348219804224621, 0.008695073790781938, 0.009505939874745462, 0.009526816749335865, 0.009722204172746385, 0.01060953105625062, 0.013296988121198838, 0.009833708627707716, 0.028611128952177323, 0.012478960862391864, 0.011932045823947468, 0.012432060536376577, 0.02053422011755035, 0.013838570556026442, 0.014216005513836949, 0.014073762293628111, 0.021787991436898024, 0.021066189133065905, 0.02149943744395022, 0.021470579024905234, 0.026011800691817633, 0.020782142240024837, 0.02764042611312567, 0.029849177152229234, 0.040109724511075195, 0.03888914702854962, 0.07366710789253439, 0.13224316259888214, 0.07096638778943376, 0.14500215637103508, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}