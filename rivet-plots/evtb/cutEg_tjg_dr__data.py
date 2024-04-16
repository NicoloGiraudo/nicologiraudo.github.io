
from numpy import nan

xpoints  = [0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25, 6.75, 7.25, 7.75, 8.25, 8.75, 9.25, 9.75]
xedges   = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
xmins    = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]
xmaxs    = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.02159352, 0.11495644, 0.1781857, 0.2213918, 0.2977518, 0.5087174, 0.4186934, 0.178559, 0.09260408, 0.0510246, 0.02862054, 0.01658436, 0.009235532, 0.005346096, 0.003291284, 0.0015382896, 0.0011626104, 0.000687696, 0.0003824702, 0.00016912028],
  'curve1' : [0.02146718, 0.11515882, 0.177666, 0.2206248, 0.2980448, 0.5069756, 0.41638, 0.18017228, 0.09403004, 0.0497137, 0.02855288, 0.015218234, 0.008998076, 0.006547192, 0.00248983, 0.002707682, 0.0008134018, 0.000244827, 0.00017146554, 0.0002326836],
}
yedges = {
  'curve0' : [0.02159352, 0.02159352, 0.11495644, 0.1781857, 0.2213918, 0.2977518, 0.5087174, 0.4186934, 0.178559, 0.09260408, 0.0510246, 0.02862054, 0.01658436, 0.009235532, 0.005346096, 0.003291284, 0.0015382896, 0.0011626104, 0.000687696, 0.0003824702, 0.00016912028],
  'curve1' : [0.02146718, 0.02146718, 0.11515882, 0.177666, 0.2206248, 0.2980448, 0.5069756, 0.41638, 0.18017228, 0.09403004, 0.0497137, 0.02855288, 0.015218234, 0.008998076, 0.006547192, 0.00248983, 0.002707682, 0.0008134018, 0.000244827, 0.00017146554, 0.0002326836],
}
yups = {
  'curve0' : [0.0001638092060905003, 0.0006268951746504354, 0.000730252011294731, 0.0007542429316871322, 0.0008666265631747045, 0.0012724849704416944, 0.0012511303689064542, 0.000931781090170862, 0.0007650424824805482, 0.0006475853611687033, 0.0005546752202866106, 0.0004996967880625209, 0.00040639734251099626, 0.0003611618473759376, 0.0003105587223054603, 0.00020522933513511172, 0.00024284834773990124, 0.0001967526060818509, 0.00011621526577864029, 8.897817709978105e-05],
  'curve1' : [0.00013059205182552267, 0.00043550265211591996, 0.00041857080643542256, 0.0003892440365631823, 0.0006326989805586856, 0.0018225867331899462, 0.002211235853544348, 0.0021000228570184657, 0.0020246402149517824, 0.001878569349265552, 0.001829298991417204, 0.001573189626205309, 0.0013272729937733232, 0.0015903007262778948, 0.0007367189423382569, 0.0015380472034368777, 0.0006267830565674219, 0.0002713112603634431, 0.00023581755659831606, 0.00024202355257288495],
}
ydowns = {
  'curve0' : [0.0001638092060905003, 0.0006268951746504354, 0.000730252011294731, 0.0007542429316871322, 0.0008666265631747045, 0.0012724849704416944, 0.0012511303689064542, 0.000931781090170862, 0.0007650424824805482, 0.0006475853611687033, 0.0005546752202866106, 0.0004996967880625209, 0.00040639734251099626, 0.0003611618473759376, 0.0003105587223054603, 0.00020522933513511172, 0.00024284834773990124, 0.0001967526060818509, 0.00011621526577864029, 8.897817709978105e-05],
  'curve1' : [0.00013059205182552267, 0.00043550265211591996, 0.00041857080643542256, 0.0003892440365631823, 0.0006326989805586856, 0.0018225867331899462, 0.002211235853544348, 0.0021000228570184657, 0.0020246402149517824, 0.001878569349265552, 0.001829298991417204, 0.001573189626205309, 0.0013272729937733232, 0.0015903007262778948, 0.0007367189423382569, 0.0015380472034368777, 0.0006267830565674219, 0.0002713112603634431, 0.00023581755659831606, 0.00024202355257288495],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.9941491706771289, 0.9941491706771289, 1.0017604929310615, 0.9970833798671834, 0.9965355537106614, 1.0009840410704485, 0.9965760950971994, 0.9944747158660728, 1.0090349968357797, 1.0153984576057555, 0.9743084708160377, 0.9976359635422671, 0.9176256424727877, 0.9742888660880609, 1.2246678697875983, 0.7564919952213179, 1.7601900188365052, 0.6996340304542261, 0.3560105046415858, 0.44831084879292554, 1.3758468233378043],
}
ratio0_ymax = {
  'curve0' : [1.0075860353518324, 1.0054533280140758, 1.004098263841008, 1.0034068241537724, 1.002910566999678, 1.0025013592427579, 1.0029881779099132, 1.0052183373012331, 1.008261433864259, 1.0126916303345583, 1.0193803198781928, 1.0301306042598282, 1.044003674342853, 1.0675561844336385, 1.0943579230189375, 1.1334139781840245, 1.2088819674586613, 1.2861040431845625, 1.3038544330476995, 1.526123638748594],
  'curve1' : [1.000196913325179, 1.0055489075002315, 0.9994324505638523, 0.9982937219741796, 1.0031089618284714, 1.0001588047375416, 0.9997559929378975, 1.0207959433969638, 1.0372618594661465, 1.0111254051823149, 1.0615515637167294, 1.0124854758462376, 1.1180026222391222, 1.5221374113517407, 0.9803313668277357, 2.7600324434598518, 1.2387510524311685, 0.7505325905101135, 1.064875372246821, 2.8069203325165084],
}
ratio0_ymin = {
  'curve0' : [0.9924139646481677, 0.9945466719859241, 0.9959017361589918, 0.9965931758462276, 0.997089433000322, 0.9974986407572421, 0.9970118220900868, 0.994781662698767, 0.991738566135741, 0.9873083696654417, 0.9806196801218073, 0.969869395740172, 0.9559963256571472, 0.9324438155663615, 0.9056420769810626, 0.8665860218159755, 0.7911180325413386, 0.7138959568154376, 0.6961455669523003, 0.4738763612514061],
  'curve1' : [0.9881014280290789, 0.9979720783618915, 0.9947343091705146, 0.9947773854471431, 0.9988591203124257, 0.9929933854568569, 0.9891934387942481, 0.9972740502745957, 0.9935350557453646, 0.9374915364497605, 0.9337203633678048, 0.8227658090993377, 0.8305751099369996, 0.927198328223456, 0.5326526236149003, 0.7603475942131588, 0.16051700847728365, -0.03851158122694201, -0.16825367466096983, -0.055226685840899375],
}
ratio0_yerrs = {
  'curve0' : [
    [0.007586035351832332, 0.005453328014075942, 0.004098263841008198, 0.0034068241537723587, 0.002910566999677955, 0.00250135924275785, 0.0029881779099132366, 0.005218337301233, 0.008261433864259038, 0.012691630334558335, 0.019380319878192664, 0.030130604259828053, 0.044003674342852794, 0.06755618443363853, 0.09435792301893742, 0.13341397818402445, 0.2088819674586614, 0.2861040431845624, 0.30385443304769966, 0.5261236387485939],
    [0.007586035351832443, 0.005453328014075831, 0.004098263841008087, 0.0034068241537723587, 0.002910566999678066, 0.00250135924275785, 0.0029881779099132366, 0.005218337301233111, 0.008261433864259038, 0.012691630334558335, 0.019380319878192775, 0.030130604259828164, 0.044003674342852905, 0.06755618443363853, 0.09435792301893753, 0.13341397818402445, 0.20888196745866128, 0.2861040431845625, 0.30385443304769955, 0.5261236387485939],
  ],
  'curve1' : [
    [0.006047742648050081, 0.0037884145691700066, 0.002349070696668787, 0.0017581682635182672, 0.0021249207580227303, 0.003582709640342463, 0.005281277071824686, 0.011760946561183983, 0.02186340186039093, 0.0368169343662772, 0.0639156001744623, 0.09485983337344994, 0.1437137561510613, 0.2974695415641423, 0.22383937160641765, 0.9998424246233464, 0.5391170219769424, 0.39452208586852777, 0.6165645234538953, 1.4310735091787037],
    [0.00604774264804997, 0.0037884145691700066, 0.002349070696668898, 0.0017581682635182672, 0.0021249207580229523, 0.003582709640342241, 0.005281277071824686, 0.011760946561184094, 0.02186340186039093, 0.0368169343662772, 0.0639156001744623, 0.09485983337344994, 0.1437137561510613, 0.2974695415641424, 0.22383937160641776, 0.9998424246233466, 0.5391170219769423, 0.39452208586852766, 0.6165645234538955, 1.4310735091787041],
  ],
}
ratio0_variation_vals = {
}