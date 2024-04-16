
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
  'curve0' : [0.04167241428571428, 0.041522814285714284, 0.048529928571428585, 0.051153171428571405, 0.049422114285714316, 0.04712445714285714, 0.04464767142857143, 0.04514539999999996, 0.060283728571428614, 0.03781210000000002, 0.048569557142857094, 0.05147294285714289, 0.05646748571428567, 0.057494142857142896, 0.04632408571428567, 0.05059662857142853, 0.046937271428571535, 0.051511242857142814, 0.0503872571428571, 0.04757750000000011, 0.053860171428571385, 0.05138081428571424, 0.051170428571428526, 0.0495219142857144, 0.051242528571428525, 0.04789111428571424, 0.06603067142857158, 0.04250611428571425, 0.05872874285714299, 0.042141628571428405, 0.0503111142857144, 0.043523257142856965, 0.05896274285714299, 0.04952187142857154, 0.06273962857142831, 0.04864498571428583, 0.038378914285714376, 0.05226872857142836, 0.0565867285714287, 0.04669557142857153, 0.038517299999999845, 0.04887264285714297, 0.04021845714285723, 0.04507387142857124, 0.056210728571428704, 0.049373042857142654, 0.04231972857142867, 0.04246322857142867, 0.05111857142857122, 0.065200042857143, 0.03339124285714293, 0.0434748285714284, 0.058707842857142985, 0.037801328571428656, 0.03799728571428556, 0.05712281428571441, 0.037990971428571274, 0.041673914285714646, 0.053770271428571215, 0.04048512857142841, 0.038205314285714616, 0.044692242857142676, 0.0485169999999998, 0.03526382857142843, 0.03408154285714315, 0.04017679999999984, 0.04137758571428555, 0.040336800000000346, 0.03882967142857127, 0.042311228571428404, 0.04122237142857178, 0.03757174285714271, 0.029355414285714164, 0.033278842857143144, 0.03827149999999984, 0.0427099285714284, 0.020696671428571605, 0.04040207142857126, 0.030634957142857015, 0.019087457142857308, 0.0055626042857142635, 0.044733242857142676, -0.01080445285714295, 0.014864385714285654, 0.0007852375714285682, -0.008531137142857217, -0.01547275714285708, -0.03945624285714269, -0.0619110571428569, -0.1503967142857156, -0.2751869999999989, -1.8122414285714212, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0019595228571428567, 0.005730888571428571, 0.00922232285714286, 0.013286845714285707, 0.016890700000000012, 0.020803128571428568, 0.0245238, 0.02806151428571426, 0.032048900000000026, 0.035725485714285736, 0.039459371428571394, 0.04335417142857146, 0.04685882857142853, 0.05071617142857147, 0.05438614285714281, 0.058186157142857096, 0.062120628571428714, 0.06530788571428567, 0.07008657142857137, 0.07368601428571445, 0.07814728571428564, 0.08129487142857135, 0.08561948571428564, 0.08904258571428592, 0.09223645714285705, 0.09536419999999991, 0.1004360428571431, 0.10453802857142848, 0.10755335714285738, 0.11188458571428526, 0.11556558571428598, 0.11894019999999952, 0.12248452857142886, 0.1274175000000003, 0.13203527142857088, 0.13411602857142887, 0.13962650000000032, 0.1437087142857137, 0.14655428571428605, 0.15126685714285748, 0.15488614285714225, 0.15967142857142894, 0.16263828571428607, 0.1669649999999993, 0.17081357142857181, 0.17460257142857072, 0.17947828571428612, 0.18365514285714327, 0.18685557142857068, 0.19191428571428615, 0.19487228571428616, 0.19995957142857063, 0.2048748571428576, 0.20955214285714333, 0.21260057142857056, 0.2195855714285719, 0.22353328571428482, 0.2273685714285734, 0.2327952857142848, 0.2364587142857133, 0.24366414285714497, 0.24792928571428471, 0.25237299999999896, 0.2582514285714275, 0.2637774285714308, 0.27085057142857033, 0.2766057142857131, 0.2819531428571453, 0.2890109999999988, 0.2949864285714274, 0.30041314285714543, 0.3091881428571416, 0.3157014285714273, 0.3271874285714314, 0.3335972857142844, 0.34413542857142715, 0.35541871428571736, 0.36592614285714137, 0.37927685714285564, 0.3932977142857177, 0.40771742857142695, 0.4249938571428554, 0.4435664285714324, 0.46799328571428384, 0.49776957142856937, 0.531740571428576, 0.576485571428569, 0.6348657142857117, 0.7173089999999971, 0.8531772857142931, 1.1309622857142811, 2.3284271428571333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.04167241428571428, 0.04167241428571428, 0.041522814285714284, 0.048529928571428585, 0.051153171428571405, 0.049422114285714316, 0.04712445714285714, 0.04464767142857143, 0.04514539999999996, 0.060283728571428614, 0.03781210000000002, 0.048569557142857094, 0.05147294285714289, 0.05646748571428567, 0.057494142857142896, 0.04632408571428567, 0.05059662857142853, 0.046937271428571535, 0.051511242857142814, 0.0503872571428571, 0.04757750000000011, 0.053860171428571385, 0.05138081428571424, 0.051170428571428526, 0.0495219142857144, 0.051242528571428525, 0.04789111428571424, 0.06603067142857158, 0.04250611428571425, 0.05872874285714299, 0.042141628571428405, 0.0503111142857144, 0.043523257142856965, 0.05896274285714299, 0.04952187142857154, 0.06273962857142831, 0.04864498571428583, 0.038378914285714376, 0.05226872857142836, 0.0565867285714287, 0.04669557142857153, 0.038517299999999845, 0.04887264285714297, 0.04021845714285723, 0.04507387142857124, 0.056210728571428704, 0.049373042857142654, 0.04231972857142867, 0.04246322857142867, 0.05111857142857122, 0.065200042857143, 0.03339124285714293, 0.0434748285714284, 0.058707842857142985, 0.037801328571428656, 0.03799728571428556, 0.05712281428571441, 0.037990971428571274, 0.041673914285714646, 0.053770271428571215, 0.04048512857142841, 0.038205314285714616, 0.044692242857142676, 0.0485169999999998, 0.03526382857142843, 0.03408154285714315, 0.04017679999999984, 0.04137758571428555, 0.040336800000000346, 0.03882967142857127, 0.042311228571428404, 0.04122237142857178, 0.03757174285714271, 0.029355414285714164, 0.033278842857143144, 0.03827149999999984, 0.0427099285714284, 0.020696671428571605, 0.04040207142857126, 0.030634957142857015, 0.019087457142857308, 0.0055626042857142635, 0.044733242857142676, -0.01080445285714295, 0.014864385714285654, 0.0007852375714285682, -0.008531137142857217, -0.01547275714285708, -0.03945624285714269, -0.0619110571428569, -0.1503967142857156, -0.2751869999999989, -1.8122414285714212, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0019595228571428567, 0.0019595228571428567, 0.005730888571428571, 0.00922232285714286, 0.013286845714285707, 0.016890700000000012, 0.020803128571428568, 0.0245238, 0.02806151428571426, 0.032048900000000026, 0.035725485714285736, 0.039459371428571394, 0.04335417142857146, 0.04685882857142853, 0.05071617142857147, 0.05438614285714281, 0.058186157142857096, 0.062120628571428714, 0.06530788571428567, 0.07008657142857137, 0.07368601428571445, 0.07814728571428564, 0.08129487142857135, 0.08561948571428564, 0.08904258571428592, 0.09223645714285705, 0.09536419999999991, 0.1004360428571431, 0.10453802857142848, 0.10755335714285738, 0.11188458571428526, 0.11556558571428598, 0.11894019999999952, 0.12248452857142886, 0.1274175000000003, 0.13203527142857088, 0.13411602857142887, 0.13962650000000032, 0.1437087142857137, 0.14655428571428605, 0.15126685714285748, 0.15488614285714225, 0.15967142857142894, 0.16263828571428607, 0.1669649999999993, 0.17081357142857181, 0.17460257142857072, 0.17947828571428612, 0.18365514285714327, 0.18685557142857068, 0.19191428571428615, 0.19487228571428616, 0.19995957142857063, 0.2048748571428576, 0.20955214285714333, 0.21260057142857056, 0.2195855714285719, 0.22353328571428482, 0.2273685714285734, 0.2327952857142848, 0.2364587142857133, 0.24366414285714497, 0.24792928571428471, 0.25237299999999896, 0.2582514285714275, 0.2637774285714308, 0.27085057142857033, 0.2766057142857131, 0.2819531428571453, 0.2890109999999988, 0.2949864285714274, 0.30041314285714543, 0.3091881428571416, 0.3157014285714273, 0.3271874285714314, 0.3335972857142844, 0.34413542857142715, 0.35541871428571736, 0.36592614285714137, 0.37927685714285564, 0.3932977142857177, 0.40771742857142695, 0.4249938571428554, 0.4435664285714324, 0.46799328571428384, 0.49776957142856937, 0.531740571428576, 0.576485571428569, 0.6348657142857117, 0.7173089999999971, 0.8531772857142931, 1.1309622857142811, 2.3284271428571333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.00447578792516138, 0.003591641089291316, 0.0063135972475350105, 0.0074321735772001855, 0.007630695263479057, 0.004993918750820434, 0.008935509304489154, 0.00786968998170596, 0.009434759873868076, 0.00807230842233535, 0.00615882476199636, 0.008084271703721488, 0.009264524173602504, 0.011654795807139764, 0.009166790104301855, 0.008366451470251978, 0.007461382210408214, 0.01035179467827798, 0.009449468185013995, 0.008705466263052382, 0.008482832603534725, 0.009071892001660722, 0.011612678679893315, 0.009945209081435636, 0.010633653738801848, 0.008320025019585607, 0.010184692395142523, 0.011574525158859044, 0.012031021976370878, 0.010369159531406305, 0.008199749871745113, 0.006974353894440514, 0.007965575167877229, 0.00810824095772762, 0.007307943679060895, 0.008750527680881758, 0.008529808476927343, 0.009006200811730983, 0.009477000085060954, 0.010718661963403585, 0.007903868853741334, 0.008488914740376892, 0.008621661140193743, 0.00685244184095517, 0.008106043348978001, 0.010045017040649456, 0.00771211609701759, 0.008318937088697966, 0.007558896636900552, 0.011140955881753784, 0.010526496209517207, 0.008781123074469403, 0.009885359200889602, 0.01059260909063198, 0.0075657471945766485, 0.011096649613872729, 0.010348683244643171, 0.00806981526228129, 0.010659159135193864, 0.010947672383307966, 0.01052826128637999, 0.00972310838850895, 0.010153357743593343, 0.009727696625237255, 0.008134445530067418, 0.009143312488661067, 0.008682321940916131, 0.008482336990259687, 0.009035201001796056, 0.009152227341260801, 0.009292316334323985, 0.010070291729150813, 0.011553537315030182, 0.010645125357531164, 0.010555052953781993, 0.01216719996967419, 0.01020779314133708, 0.0119919028804388, 0.015566709638828299, 0.0140610200808579, 0.011310729058585644, 0.016575953815631754, 0.01505252707782236, 0.014725529684523885, 0.0141750420220375, 0.01329986113169803, 0.01428130503383308, 0.014931271116112498, 0.0185304272669001, 0.01736342038156492, 0.02157830543175526, 0.017560798178131276, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [6.572029475631666e-05, 0.0001123919798867212, 0.00014257536496140404, 0.00017113361530019243, 0.00019295145841926798, 0.00021413547113918329, 0.00023249744347947097, 0.0002487023875056697, 0.0002657852439816166, 0.0002806165951425323, 0.00029491676445937, 0.00030912902662487223, 0.0003213809171023551, 0.00033434706396747924, 0.00034623299339358964, 0.0003581246220213837, 0.00037003455437103713, 0.00037940858918983394, 0.0003930445007780117, 0.00040301096354155756, 0.0004150317174995327, 0.0004233074339926823, 0.0004344208201497616, 0.0004430198779342738, 0.0004508952319597994, 0.0004584764031494942, 0.0004705103612036625, 0.0004800223209095887, 0.00048689604137027234, 0.0004966031553237948, 0.0005047062188510658, 0.0005120220020782728, 0.0005195950149797801, 0.0005299549461019875, 0.0005394725315017398, 0.0005437066661128145, 0.0005547639689313747, 0.0005628152631265083, 0.0005683601545728939, 0.0005774258499971225, 0.0005842928745631795, 0.0005932501279272647, 0.0005987364245830135, 0.0006066485382654349, 0.0006136002820423493, 0.0006203683895682525, 0.0006289703279721466, 0.0006362472885953227, 0.0006417670122086211, 0.0006503961116433725, 0.0006553892751951456, 0.0006638888215258149, 0.0006719991496593274, 0.0006796266982539708, 0.0006845521402004799, 0.000695706805474602, 0.0007019327544977017, 0.0007079288561049981, 0.0007163272254197427, 0.0007219414018845975, 0.0007328585352256399, 0.000739244788377201, 0.0007458400277128944, 0.0007544765721738344, 0.0007625058045948414, 0.0007726614486861043, 0.0007808272693046721, 0.0007883386043459064, 0.0007981444040998554, 0.0008063533433214678, 0.000813736531598007, 0.0008255354477611477, 0.0008341855370384193, 0.0008492248566444988, 0.0008575029005722313, 0.0008709416672516569, 0.0008851043983160297, 0.0008980924228608063, 0.0009143290168316881, 0.0009310757438663847, 0.0009479905708650125, 0.0009678670004769444, 0.0009887890965979739, 0.0010156500883871412, 0.0010474625315981627, 0.001082615408374091, 0.001127245604587223, 0.0011829469427610622, 0.0012574115784225177, 0.0013713363064201847, 0.0015788771520370004, 0.0022654562094056576, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.00447578792516138, 0.003591641089291316, 0.0063135972475350105, 0.0074321735772001855, 0.007630695263479057, 0.004993918750820434, 0.008935509304489154, 0.00786968998170596, 0.009434759873868076, 0.00807230842233535, 0.00615882476199636, 0.008084271703721488, 0.009264524173602504, 0.011654795807139764, 0.009166790104301855, 0.008366451470251978, 0.007461382210408214, 0.01035179467827798, 0.009449468185013995, 0.008705466263052382, 0.008482832603534725, 0.009071892001660722, 0.011612678679893315, 0.009945209081435636, 0.010633653738801848, 0.008320025019585607, 0.010184692395142523, 0.011574525158859044, 0.012031021976370878, 0.010369159531406305, 0.008199749871745113, 0.006974353894440514, 0.007965575167877229, 0.00810824095772762, 0.007307943679060895, 0.008750527680881758, 0.008529808476927343, 0.009006200811730983, 0.009477000085060954, 0.010718661963403585, 0.007903868853741334, 0.008488914740376892, 0.008621661140193743, 0.00685244184095517, 0.008106043348978001, 0.010045017040649456, 0.00771211609701759, 0.008318937088697966, 0.007558896636900552, 0.011140955881753784, 0.010526496209517207, 0.008781123074469403, 0.009885359200889602, 0.01059260909063198, 0.0075657471945766485, 0.011096649613872729, 0.010348683244643171, 0.00806981526228129, 0.010659159135193864, 0.010947672383307966, 0.01052826128637999, 0.00972310838850895, 0.010153357743593343, 0.009727696625237255, 0.008134445530067418, 0.009143312488661067, 0.008682321940916131, 0.008482336990259687, 0.009035201001796056, 0.009152227341260801, 0.009292316334323985, 0.010070291729150813, 0.011553537315030182, 0.010645125357531164, 0.010555052953781993, 0.01216719996967419, 0.01020779314133708, 0.0119919028804388, 0.015566709638828299, 0.0140610200808579, 0.011310729058585644, 0.016575953815631754, 0.01505252707782236, 0.014725529684523885, 0.0141750420220375, 0.01329986113169803, 0.01428130503383308, 0.014931271116112498, 0.0185304272669001, 0.01736342038156492, 0.02157830543175526, 0.017560798178131276, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [6.572029475631666e-05, 0.0001123919798867212, 0.00014257536496140404, 0.00017113361530019243, 0.00019295145841926798, 0.00021413547113918329, 0.00023249744347947097, 0.0002487023875056697, 0.0002657852439816166, 0.0002806165951425323, 0.00029491676445937, 0.00030912902662487223, 0.0003213809171023551, 0.00033434706396747924, 0.00034623299339358964, 0.0003581246220213837, 0.00037003455437103713, 0.00037940858918983394, 0.0003930445007780117, 0.00040301096354155756, 0.0004150317174995327, 0.0004233074339926823, 0.0004344208201497616, 0.0004430198779342738, 0.0004508952319597994, 0.0004584764031494942, 0.0004705103612036625, 0.0004800223209095887, 0.00048689604137027234, 0.0004966031553237948, 0.0005047062188510658, 0.0005120220020782728, 0.0005195950149797801, 0.0005299549461019875, 0.0005394725315017398, 0.0005437066661128145, 0.0005547639689313747, 0.0005628152631265083, 0.0005683601545728939, 0.0005774258499971225, 0.0005842928745631795, 0.0005932501279272647, 0.0005987364245830135, 0.0006066485382654349, 0.0006136002820423493, 0.0006203683895682525, 0.0006289703279721466, 0.0006362472885953227, 0.0006417670122086211, 0.0006503961116433725, 0.0006553892751951456, 0.0006638888215258149, 0.0006719991496593274, 0.0006796266982539708, 0.0006845521402004799, 0.000695706805474602, 0.0007019327544977017, 0.0007079288561049981, 0.0007163272254197427, 0.0007219414018845975, 0.0007328585352256399, 0.000739244788377201, 0.0007458400277128944, 0.0007544765721738344, 0.0007625058045948414, 0.0007726614486861043, 0.0007808272693046721, 0.0007883386043459064, 0.0007981444040998554, 0.0008063533433214678, 0.000813736531598007, 0.0008255354477611477, 0.0008341855370384193, 0.0008492248566444988, 0.0008575029005722313, 0.0008709416672516569, 0.0008851043983160297, 0.0008980924228608063, 0.0009143290168316881, 0.0009310757438663847, 0.0009479905708650125, 0.0009678670004769444, 0.0009887890965979739, 0.0010156500883871412, 0.0010474625315981627, 0.001082615408374091, 0.001127245604587223, 0.0011829469427610622, 0.0012574115784225177, 0.0013713363064201847, 0.0015788771520370004, 0.0022654562094056576, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.04702206221381804, 0.04702206221381804, 0.13801782634469106, 0.19003371998722438, 0.25974627463399835, 0.34176401078984886, 0.4414507844273765, 0.5492738863041009, 0.6215808096885682, 0.5316343358229099, 0.9448162285164198, 0.812430125984266, 0.8422710850027726, 0.8298373476114193, 0.8821102273771988, 1.1740359689467312, 1.1500006776284362, 1.3234818872239515, 1.2678375067634335, 1.3909582581537057, 1.5487575909981457, 1.4509290193760986, 1.5822028622690458, 1.6732219780956077, 1.7980440982260668, 1.7999981600105046, 1.9912712707218576, 1.5210513642253265, 2.459364501510371, 1.831358069497243, 2.654965873581399, 2.29701900574085, 2.7327963899760657, 2.077320739101108, 2.5729540569520366, 2.1044955865215287, 2.757037063576366, 3.638104479989756, 2.749420508465728, 2.5899056088618457, 3.2394261921442538, 4.021209764369332, 3.2670921652048985, 4.043871825728912, 3.704252479501111, 3.0388072841203924, 3.5363947880176374, 4.241007486883017, 4.32503954682135, 3.655336332895509, 2.9434687049942783, 5.8360297203672316, 4.599433235257972, 3.4897357349918448, 5.543512642979668, 5.5951515333802035, 3.844095816607675, 5.883852855264861, 5.455896700025436, 4.3294422648308855, 5.840631427624746, 6.377755226273682, 5.547479156657739, 5.201743718696539, 7.323408689114057, 7.739597637263236, 6.741467001567358, 6.684916713016811, 6.989972998778854, 7.443045211743448, 6.971823757692149, 7.287623987806898, 8.229273367295026, 10.75445318191485, 9.83169486919832, 8.716598139981077, 8.057504193571583, 17.172747584670276, 9.057113408258772, 12.380525142379366, 20.605034570196434, 73.29614109321354, 9.50062705044858, -41.054038963036014, 31.484199529652372, 633.9095192847005, -62.329389684443335, -37.25810248981389, -16.090374255459125, -11.586121011386378, -5.672845246429205, -4.109795468951242, -1.2848327524951342, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.1074040945761985, 1.0864980168390705, 1.1300969820765832, 1.1452925277092199, 1.1543983978379644, 1.1059729714377704, 1.2001338259887624, 1.1743187563230355, 1.15650591125413, 1.2134847951405858, 1.1268042190271879, 1.1570586652905865, 1.1640682962312006, 1.2027127499943555, 1.197883886167557, 1.1653559082190792, 1.1589649756646556, 1.2009618503476382, 1.1875368638984063, 1.1829744367201378, 1.1574973190492819, 1.1765618573348116, 1.2269412042090528, 1.2008244072322651, 1.2075161791436437, 1.1737279481523244, 1.1542418420833382, 1.2723025934823944, 1.2048574750805787, 1.246055026417192, 1.16298088380987, 1.160244300456386, 1.1350950580297208, 1.1637305037921, 1.116480505949137, 1.1798855021209709, 1.222252469505172, 1.172305718120223, 1.1674774337431129, 1.2295434371072966, 1.205203086762088, 1.1736946120386897, 1.2143707579226455, 1.1520269198933635, 1.1442081174713365, 1.2034514475786715, 1.1822345359328292, 1.1959091988190307, 1.1478698724486602, 1.1708734441504012, 1.315247211807973, 1.201981775731264, 1.1683822589929627, 1.2802179047917956, 1.1991128327287919, 1.1942595047640683, 1.2723984898385725, 1.1936418836722407, 1.1982351744188897, 1.2704121925657925, 1.2755705975259213, 1.2175569576937222, 1.209274228488847, 1.2758548070165832, 1.2386759767350883, 1.2275769222203137, 1.2098315257170398, 1.2102878014681286, 1.232688062231396, 1.2163072936019883, 1.2254192568815523, 1.2680283362802895, 1.3935743233796811, 1.3198766676842624, 1.2757940753245114, 1.2848798950652816, 1.493209411791951, 1.2968140606760685, 1.508135512194046, 1.7366628239487445, 3.0333513724198506, 1.3705511328245907, -0.39317809766470113, 1.990658475067132, 19.05191516275655, -0.558978704595492, 0.07700321914339801, 0.6215739250649529, 0.7006927660087923, 0.8845492039900631, 0.9215867557996731, 0.9903099013733649, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.04859913174249294, 0.1407245788088512, 0.1929716053119793, 0.26309178793299604, 0.34566816303440473, 0.4459948255500155, 0.5544812674740557, 0.6270897294789713, 0.5360432410164016, 0.952237572349281, 0.8185021756756382, 0.8482767456366095, 0.8355287807084847, 0.8879255512928581, 1.1815101152370446, 1.1570787109309082, 1.3313654846958274, 1.2752030558774794, 1.398758732382014, 1.557228211849211, 1.4586347452676311, 1.590441490634077, 1.6817116631007538, 1.806990034269215, 1.808797398544007, 2.0008445790482057, 1.5281769976775417, 2.470657519679075, 1.8396486614234935, 2.6667500208049, 2.3070507099878457, 2.7445607209496794, 2.0861329990096857, 2.5836554890832186, 2.1130941795286193, 2.7682140977172796, 3.6525593956447793, 2.7601882328491016, 2.5999496628109173, 3.251791944020326, 4.036379386190259, 3.279230860664061, 4.058758931478799, 3.7177114640311353, 3.0497233547289175, 3.5489597091500706, 4.255869830031333, 4.340023035124061, 3.6678908115179283, 2.9534440989225987, 5.8556572999095415, 4.614703883661681, 3.5011822320347448, 5.561491553349704, 5.613167350229539, 3.8562749575371615, 5.902329159715707, 5.472884037745897, 4.342764258683405, 5.85846368918249, 6.396937336116963, 5.564019941839189, 5.217116475208955, 7.344803886480265, 7.7619706210154975, 6.760698534409348, 6.703787491865445, 7.0095169042038235, 7.4636002248232804, 6.990881425610257, 7.307364155667158, 8.251245609863064, 10.78286993423588, 9.857213330290552, 8.739003922366722, 8.077896212392105, 17.215513127978568, 9.07934227898508, 12.410371079899958, 20.6538140245207, 73.4665631693083, 9.522263465308283, -41.14555577648986, 31.55252728351381, 635.2434627557095, -62.45629133779215, -37.33095606039472, -16.120355491813637, -11.606430979208785, -5.681963373197686, -4.115532938933608, -1.2860828377065685, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [0.8925959054238015, 0.9135019831609293, 0.8699030179234167, 0.8547074722907801, 0.8456016021620357, 0.8940270285622296, 0.7998661740112376, 0.8256812436769645, 0.8434940887458698, 0.7865152048594143, 0.8731957809728123, 0.8429413347094136, 0.8359317037687995, 0.7972872500056445, 0.8021161138324432, 0.8346440917809207, 0.8410350243353443, 0.7990381496523619, 0.8124631361015937, 0.8170255632798621, 0.8425026809507181, 0.8234381426651884, 0.773058795790947, 0.799175592767735, 0.7924838208563563, 0.8262720518476756, 0.8457581579166619, 0.7276974065176055, 0.7951425249194214, 0.7539449735828081, 0.8370191161901299, 0.8397556995436141, 0.8649049419702793, 0.8362694962079, 0.883519494050863, 0.8201144978790291, 0.777747530494828, 0.827694281879777, 0.8325225662568873, 0.7704565628927035, 0.7947969132379121, 0.8263053879613103, 0.7856292420773545, 0.8479730801066365, 0.8557918825286636, 0.7965485524213285, 0.8177654640671709, 0.8040908011809693, 0.8521301275513398, 0.8291265558495989, 0.6847527881920269, 0.7980182242687359, 0.8316177410070374, 0.7197820952082044, 0.8008871672712082, 0.8057404952359316, 0.7276015101614275, 0.8063581163277592, 0.8017648255811102, 0.7295878074342075, 0.7244294024740788, 0.7824430423062778, 0.7907257715111532, 0.724145192983417, 0.7613240232649116, 0.7724230777796862, 0.7901684742829601, 0.7897121985318712, 0.7673119377686038, 0.7836927063980116, 0.7745807431184476, 0.7319716637197105, 0.6064256766203188, 0.6801233323157377, 0.7242059246754886, 0.7151201049347184, 0.5067905882080489, 0.7031859393239316, 0.49186448780595393, 0.2633371760512554, -1.033351372419851, 0.6294488671754092, 2.393178097664701, 0.009341524932868188, -17.05191516275655, 2.558978704595492, 1.922996780856602, 1.3784260749350472, 1.2993072339912077, 1.115450796009937, 1.078413244200327, 1.009690098626635, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.04544499268514314, 0.1353110738805309, 0.18709583466246948, 0.2564007613350007, 0.337859858545293, 0.43690674330473744, 0.5440665051341461, 0.616071889898165, 0.5272254306294182, 0.9373948846835586, 0.8063580762928938, 0.8362654243689358, 0.8241459145143538, 0.8762949034615395, 1.1665618226564176, 1.142922644325964, 1.3155982897520755, 1.2604719576493875, 1.383157783925397, 1.5402869701470803, 1.443223293484566, 1.5739642339040145, 1.6647322930904616, 1.7890981621829185, 1.7911989214770023, 1.98169796239551, 1.5139257307731113, 2.448071483341667, 1.8230674775709925, 2.6431817263578985, 2.2869873014938547, 2.721032059002452, 2.0685084791925306, 2.5622526248208546, 2.095896993514438, 2.7458600294354527, 3.623649564334733, 2.7386527840823542, 2.579861554912774, 3.2270604402681813, 4.006040142548406, 3.254953469745736, 4.028984719979024, 3.6907934949710866, 3.0278912135118676, 3.523829866885204, 4.226145143734701, 4.31005605851864, 3.64278185427309, 2.9334933110659582, 5.8164021408249225, 4.584162586854262, 3.478289237948945, 5.525533732609633, 5.577135716530868, 3.8319166756781886, 5.865376550814013, 5.438909362304974, 4.316120270978365, 5.822799166067003, 6.358573116430401, 5.530938371476289, 5.186370962184123, 7.30201349174785, 7.717224653510975, 6.7222354687253665, 6.666045934168178, 6.970429093353885, 7.422490198663616, 6.95276608977404, 7.267883819946638, 8.207301124726985, 10.726036429593817, 9.806176408106088, 8.69419235759543, 8.037112174751064, 17.129982041361988, 9.034884537532463, 12.350679204858775, 20.55625511587217, 73.12571901711877, 9.478990635588877, -40.96252214958217, 31.415871775790936, 632.5755758136914, -62.20248803109452, -37.18524891923306, -16.06039301910461, -11.565811043563974, -5.663727119660724, -4.1040579989688775, -1.2835826672836999, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.10740409457619848, 0.08649801683907066, 0.13009698207658327, 0.14529252770921985, 0.15439839783796427, 0.1059729714377704, 0.2001338259887624, 0.1743187563230355, 0.15650591125413016, 0.21348479514058571, 0.12680421902718775, 0.15705866529058643, 0.16406829623120045, 0.2027127499943555, 0.1978838861675568, 0.1653559082190793, 0.15896497566465573, 0.20096185034763814, 0.1875368638984063, 0.1829744367201379, 0.15749731904928188, 0.17656185733481156, 0.22694120420905295, 0.20082440723226502, 0.20751617914364373, 0.1737279481523244, 0.15424184208333813, 0.2723025934823945, 0.2048574750805786, 0.2460550264171919, 0.16298088380987008, 0.16024430045638594, 0.13509505802972066, 0.16373050379209997, 0.11648050594913695, 0.17988550212097087, 0.22225246950517197, 0.172305718120223, 0.16747743374311275, 0.22954343710729652, 0.20520308676208787, 0.17369461203868974, 0.21437075792264548, 0.15202691989336348, 0.14420811747133644, 0.2034514475786715, 0.18223453593282912, 0.19590919881903068, 0.14786987244866023, 0.17087344415040107, 0.3152472118079731, 0.20198177573126408, 0.16838225899296255, 0.28021790479179565, 0.19911283272879177, 0.1942595047640684, 0.2723984898385725, 0.19364188367224078, 0.19823517441888983, 0.2704121925657925, 0.27557059752592117, 0.21755695769372219, 0.2092742284888468, 0.27585480701658305, 0.23867597673508845, 0.22757692222031378, 0.2098315257170399, 0.21028780146812875, 0.23268806223139615, 0.21630729360198842, 0.2254192568815524, 0.26802833628028955, 0.39357432337968123, 0.31987666768426226, 0.2757940753245114, 0.28487989506528155, 0.4932094117919511, 0.2968140606760684, 0.5081355121940461, 0.7366628239487446, 2.033351372419851, 0.37055113282459085, 1.393178097664701, 0.9906584750671318, 18.05191516275655, 1.558978704595492, 0.922996780856602, 0.3784260749350472, 0.29930723399120773, 0.1154507960099369, 0.07841324420032691, 0.009690098626635057, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.10740409457619848, 0.08649801683907055, 0.13009698207658316, 0.14529252770921985, 0.15439839783796439, 0.1059729714377704, 0.2001338259887624, 0.1743187563230355, 0.15650591125413005, 0.21348479514058583, 0.12680421902718786, 0.15705866529058654, 0.16406829623120056, 0.2027127499943555, 0.19788388616755692, 0.1653559082190792, 0.15896497566465562, 0.20096185034763825, 0.1875368638984063, 0.1829744367201378, 0.15749731904928188, 0.17656185733481156, 0.22694120420905284, 0.20082440723226513, 0.20751617914364373, 0.1737279481523244, 0.15424184208333824, 0.2723025934823944, 0.20485747508057872, 0.2460550264171919, 0.16298088380987008, 0.16024430045638605, 0.13509505802972077, 0.16373050379209997, 0.11648050594913695, 0.17988550212097087, 0.22225246950517197, 0.172305718120223, 0.16747743374311286, 0.22954343710729663, 0.20520308676208798, 0.17369461203868974, 0.21437075792264548, 0.15202691989336348, 0.14420811747133655, 0.2034514475786715, 0.18223453593282923, 0.19590919881903068, 0.14786987244866023, 0.17087344415040118, 0.315247211807973, 0.20198177573126408, 0.16838225899296266, 0.28021790479179565, 0.19911283272879188, 0.19425950476406828, 0.2723984898385725, 0.19364188367224067, 0.19823517441888971, 0.2704121925657925, 0.2755705975259213, 0.21755695769372219, 0.20927422848884691, 0.27585480701658316, 0.23867597673508834, 0.22757692222031367, 0.20983152571703978, 0.21028780146812864, 0.23268806223139604, 0.2163072936019883, 0.2254192568815523, 0.26802833628028955, 0.3935743233796811, 0.3198766676842624, 0.2757940753245114, 0.28487989506528155, 0.493209411791951, 0.2968140606760685, 0.5081355121940461, 0.7366628239487445, 2.0333513724198506, 0.37055113282459073, 1.393178097664701, 0.9906584750671319, 18.05191516275655, 1.558978704595492, 0.922996780856602, 0.3784260749350471, 0.29930723399120773, 0.1154507960099369, 0.07841324420032691, 0.009690098626635057, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [0.0015770695286749029, 0.0027067524641601615, 0.002937885324754891, 0.0033455132989976266, 0.0039041522445558696, 0.004544041122639064, 0.005207381169954783, 0.005508919790403244, 0.004408905193491686, 0.007421343832861194, 0.0060720496913722055, 0.006005660633836785, 0.005691433097065435, 0.0058153239156593095, 0.007474146290313621, 0.007078033302472253, 0.007883597471876058, 0.007365549114046077, 0.0078004742283086514, 0.008470620851065425, 0.007705725891532733, 0.008238628365031309, 0.00848968500514613, 0.008945936043148306, 0.008799238533502285, 0.009573308326347618, 0.007125633452215174, 0.011293018168704094, 0.008290591926250368, 0.011784147223500518, 0.01003170424699551, 0.011764330973613735, 0.008812259908577591, 0.01070143213118202, 0.008598593007090649, 0.0111770341409132, 0.014454915655023104, 0.0107677243833737, 0.010044053949071596, 0.012365751876072473, 0.015169621820926515, 0.012138695459162463, 0.01488710574988783, 0.013458984530024587, 0.01091607060852473, 0.012564921132433238, 0.014862343148315915, 0.014983488302710235, 0.012554478622419207, 0.009975393928320031, 0.019627579542309093, 0.015270648403709508, 0.011446497042899573, 0.017978910370035628, 0.01801581684933584, 0.012179140929486465, 0.01847630445084736, 0.01698733772046168, 0.013321993852520642, 0.017832261557743756, 0.019182109843280948, 0.016540785181450524, 0.01537275651241643, 0.021395197366206986, 0.022372983752260822, 0.019231532841991417, 0.018870778848633307, 0.01954390542496931, 0.020555013079832207, 0.01905766791810848, 0.01974016786025956, 0.0219722425680402, 0.028416752321032135, 0.025518461092230993, 0.022405782385646944, 0.020392018820519553, 0.0427655433082883, 0.02222887072630897, 0.029845937520590837, 0.048779454324265004, 0.17042207609476634, 0.021636414859703024, 0.09151681345384333, 0.06832775386143553, 1.3339434710090927, 0.12690165334881698, 0.07285357058083264, 0.029981236354515772, 0.020309967822404573, 0.009118126768481005, 0.005737469982364907, 0.0012500852114343264, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.001577069528674896, 0.0027067524641601337, 0.0029378853247549186, 0.003345513298997682, 0.0039041522445558696, 0.004544041122639009, 0.005207381169954783, 0.005508919790403133, 0.004408905193491686, 0.007421343832861194, 0.0060720496913722055, 0.006005660633836896, 0.005691433097065435, 0.0058153239156593095, 0.007474146290313399, 0.007078033302472031, 0.007883597471875836, 0.007365549114045855, 0.007800474228308429, 0.008470620851065203, 0.007705725891532511, 0.008238628365031087, 0.00848968500514613, 0.008945936043148084, 0.008799238533502285, 0.009573308326348062, 0.007125633452215174, 0.011293018168704094, 0.00829059192625059, 0.011784147223500963, 0.01003170424699551, 0.011764330973613735, 0.008812259908577591, 0.01070143213118202, 0.008598593007090649, 0.011177034140913644, 0.014454915655023104, 0.0107677243833737, 0.010044053949071596, 0.012365751876072029, 0.015169621820926515, 0.012138695459162463, 0.014887105749886942, 0.013458984530024143, 0.010916070608525175, 0.012564921132433238, 0.014862343148315915, 0.014983488302711123, 0.012554478622419207, 0.009975393928320475, 0.01962757954230998, 0.015270648403709508, 0.011446497042900017, 0.017978910370035628, 0.01801581684933584, 0.012179140929486465, 0.01847630445084647, 0.016987337720460793, 0.013321993852519753, 0.017832261557743756, 0.019182109843280948, 0.016540785181449635, 0.015372756512415542, 0.021395197366207874, 0.02237298375226171, 0.01923153284199053, 0.018870778848634195, 0.01954390542496931, 0.020555013079832207, 0.01905766791810848, 0.01974016786026045, 0.021972242568038425, 0.02841675232103036, 0.02551846109223277, 0.022405782385645168, 0.02039201882052133, 0.04276554330829185, 0.02222887072630897, 0.029845937520592614, 0.048779454324265004, 0.17042207609476634, 0.021636414859703024, 0.09151681345384333, 0.06832775386143908, 1.333943471008979, 0.12690165334881698, 0.07285357058082553, 0.02998123635451222, 0.02030996782240635, 0.009118126768481005, 0.005737469982365795, 0.0012500852114343264, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}