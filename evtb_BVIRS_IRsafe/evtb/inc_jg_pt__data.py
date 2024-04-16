
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
  'curve0' : [0.9944441428571428, 2.6254685714285713, 1.9796300000000007, 1.3834409999999993, 1.0625911428571435, 0.8406291428571427, 0.6972708571428571, 0.5950928571428566, 0.5150560000000004, 0.45475814285714317, 0.40771357142857106, 0.3658751428571431, 0.32832357142857116, 0.29816371428571453, 0.27413442857142833, 0.25084614285714263, 0.23157271428571483, 0.21639428571428554, 0.2001629999999998, 0.18830657142857188, 0.1748405714285713, 0.1641171428571427, 0.15169742857142843, 0.14533457142857176, 0.13676754285714274, 0.129520457142857, 0.12452658571428599, 0.11674194285714275, 0.1087014571428574, 0.10597299999999957, 0.09916067142857166, 0.09560502857142819, 0.08960538571428592, 0.08748351428571448, 0.08226918571428538, 0.07889687142857162, 0.0755164714285716, 0.072575314285714, 0.06908331428571444, 0.06691035714285729, 0.06459797142857117, 0.061098657142857275, 0.05828058571428585, 0.055979157142856915, 0.053669871428571554, 0.051380642857142646, 0.04969587142857154, 0.04744268571428582, 0.04576565714285696, 0.04410668571428581, 0.04217785714285724, 0.03975511428571413, 0.03901455714285723, 0.03811020000000009, 0.03673101428571414, 0.03486381428571436, 0.03378848571428558, 0.03214772857142885, 0.03137791428571416, 0.029713457142857023, 0.02887702857142882, 0.026887342857142747, 0.026475099999999894, 0.025868142857142753, 0.02534442857142879, 0.023940014285714187, 0.02230222857142848, 0.021660028571428756, 0.02125568571428563, 0.020373285714285632, 0.018623442857143017, 0.0177795285714285, 0.017106899999999932, 0.01719305714285729, 0.01594742857142851, 0.015561014285714221, 0.014873071428571557, 0.013519941428571373, 0.013444857142857088, 0.012434801428571535, 0.012583047142857092, 0.01041697857142853, 0.01029215857142866, 0.009065957142857106, 0.008769899999999964, 0.007625972857142923, 0.0076357571428571115, 0.006788221428571401, 0.005954865714285691, 0.005584770000000048, 0.0035176657142856997, 0.001390350428571423, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [1.0096031428571426, 2.635347142857143, 1.9784300000000006, 1.3829849999999995, 1.0506512857142865, 0.8398129999999999, 0.7048567142857142, 0.5970318571428566, 0.5175960000000004, 0.4564288571428575, 0.4051702857142853, 0.3632895714285717, 0.32768685714285684, 0.29840814285714307, 0.27616499999999977, 0.2524375714285712, 0.23209642857142912, 0.2155471428571427, 0.20083785714285698, 0.18707528571428614, 0.17548771428571414, 0.16523885714285702, 0.15466399999999986, 0.1449014285714289, 0.1372463714285713, 0.1301137857142856, 0.12365948571428599, 0.11601238571428561, 0.1101247571428574, 0.10486059999999958, 0.10069867142857165, 0.09498242857142819, 0.09006811428571448, 0.08702731428571447, 0.08297001428571395, 0.07903462857142876, 0.0749045714285716, 0.07177888571428542, 0.06883498571428587, 0.06606311428571443, 0.06328077142857116, 0.06079917142857157, 0.05791155714285728, 0.05593158571428549, 0.05376468571428584, 0.05127742857142836, 0.04896620000000011, 0.047922100000000106, 0.0453706142857141, 0.04367324285714296, 0.042269900000000096, 0.040100057142856985, 0.038800128571428665, 0.03716651428571437, 0.035608957142856994, 0.03532407142857151, 0.03281177142857129, 0.032554557142857425, 0.030783599999999876, 0.029446628571428456, 0.028071500000000246, 0.027601928571428458, 0.025445728571428468, 0.02498232857142847, 0.02458914285714307, 0.023555528571428473, 0.021915842857142768, 0.0211945857142859, 0.020466214285714202, 0.019266528571428493, 0.01890277142857159, 0.016827642857142788, 0.01652261428571422, 0.01587838571428585, 0.014664614285714228, 0.014760957142857084, 0.013555124285714404, 0.012892907142857091, 0.012905289999999948, 0.011820838571428674, 0.010875677142857098, 0.010395244285714244, 0.009337982857142938, 0.008620337142857107, 0.008790521428571393, 0.007598314285714352, 0.006856935714285687, 0.00559692714285712, 0.004765129999999981, 0.004294965714285752, 0.002948249999999988, 0.0005590921428571406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.9944441428571428, 0.9944441428571428, 2.6254685714285713, 1.9796300000000007, 1.3834409999999993, 1.0625911428571435, 0.8406291428571427, 0.6972708571428571, 0.5950928571428566, 0.5150560000000004, 0.45475814285714317, 0.40771357142857106, 0.3658751428571431, 0.32832357142857116, 0.29816371428571453, 0.27413442857142833, 0.25084614285714263, 0.23157271428571483, 0.21639428571428554, 0.2001629999999998, 0.18830657142857188, 0.1748405714285713, 0.1641171428571427, 0.15169742857142843, 0.14533457142857176, 0.13676754285714274, 0.129520457142857, 0.12452658571428599, 0.11674194285714275, 0.1087014571428574, 0.10597299999999957, 0.09916067142857166, 0.09560502857142819, 0.08960538571428592, 0.08748351428571448, 0.08226918571428538, 0.07889687142857162, 0.0755164714285716, 0.072575314285714, 0.06908331428571444, 0.06691035714285729, 0.06459797142857117, 0.061098657142857275, 0.05828058571428585, 0.055979157142856915, 0.053669871428571554, 0.051380642857142646, 0.04969587142857154, 0.04744268571428582, 0.04576565714285696, 0.04410668571428581, 0.04217785714285724, 0.03975511428571413, 0.03901455714285723, 0.03811020000000009, 0.03673101428571414, 0.03486381428571436, 0.03378848571428558, 0.03214772857142885, 0.03137791428571416, 0.029713457142857023, 0.02887702857142882, 0.026887342857142747, 0.026475099999999894, 0.025868142857142753, 0.02534442857142879, 0.023940014285714187, 0.02230222857142848, 0.021660028571428756, 0.02125568571428563, 0.020373285714285632, 0.018623442857143017, 0.0177795285714285, 0.017106899999999932, 0.01719305714285729, 0.01594742857142851, 0.015561014285714221, 0.014873071428571557, 0.013519941428571373, 0.013444857142857088, 0.012434801428571535, 0.012583047142857092, 0.01041697857142853, 0.01029215857142866, 0.009065957142857106, 0.008769899999999964, 0.007625972857142923, 0.0076357571428571115, 0.006788221428571401, 0.005954865714285691, 0.005584770000000048, 0.0035176657142856997, 0.001390350428571423, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [1.0096031428571426, 1.0096031428571426, 2.635347142857143, 1.9784300000000006, 1.3829849999999995, 1.0506512857142865, 0.8398129999999999, 0.7048567142857142, 0.5970318571428566, 0.5175960000000004, 0.4564288571428575, 0.4051702857142853, 0.3632895714285717, 0.32768685714285684, 0.29840814285714307, 0.27616499999999977, 0.2524375714285712, 0.23209642857142912, 0.2155471428571427, 0.20083785714285698, 0.18707528571428614, 0.17548771428571414, 0.16523885714285702, 0.15466399999999986, 0.1449014285714289, 0.1372463714285713, 0.1301137857142856, 0.12365948571428599, 0.11601238571428561, 0.1101247571428574, 0.10486059999999958, 0.10069867142857165, 0.09498242857142819, 0.09006811428571448, 0.08702731428571447, 0.08297001428571395, 0.07903462857142876, 0.0749045714285716, 0.07177888571428542, 0.06883498571428587, 0.06606311428571443, 0.06328077142857116, 0.06079917142857157, 0.05791155714285728, 0.05593158571428549, 0.05376468571428584, 0.05127742857142836, 0.04896620000000011, 0.047922100000000106, 0.0453706142857141, 0.04367324285714296, 0.042269900000000096, 0.040100057142856985, 0.038800128571428665, 0.03716651428571437, 0.035608957142856994, 0.03532407142857151, 0.03281177142857129, 0.032554557142857425, 0.030783599999999876, 0.029446628571428456, 0.028071500000000246, 0.027601928571428458, 0.025445728571428468, 0.02498232857142847, 0.02458914285714307, 0.023555528571428473, 0.021915842857142768, 0.0211945857142859, 0.020466214285714202, 0.019266528571428493, 0.01890277142857159, 0.016827642857142788, 0.01652261428571422, 0.01587838571428585, 0.014664614285714228, 0.014760957142857084, 0.013555124285714404, 0.012892907142857091, 0.012905289999999948, 0.011820838571428674, 0.010875677142857098, 0.010395244285714244, 0.009337982857142938, 0.008620337142857107, 0.008790521428571393, 0.007598314285714352, 0.006856935714285687, 0.00559692714285712, 0.004765129999999981, 0.004294965714285752, 0.002948249999999988, 0.0005590921428571406, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.019398942744176462, 0.02190694606087954, 0.014517582583943953, 0.011855710756889284, 0.008158951513271694, 0.0063738928610450945, 0.005317619921793307, 0.004746695950761914, 0.0037758310343552217, 0.0037253428824521317, 0.0031960035631253894, 0.003006748871374232, 0.0024271121666267804, 0.0024200767402236313, 0.002249921994112646, 0.001981635585024837, 0.0017645089505963715, 0.0018005299673333128, 0.001670948038371861, 0.0015557057588642127, 0.0014111010319778582, 0.0017058919505463324, 0.001214649273306025, 0.0013625004774386012, 0.001179491934898155, 0.0010548252587659296, 0.0019060333851499398, 0.0012671745043559678, 0.0009469536548795828, 0.0010401260716364868, 0.0009260539500306399, 0.0011737333598394438, 0.0008336500758589271, 0.0010393761865382823, 0.0013264167627753407, 0.0009491790222747944, 0.0008374671483048151, 0.0008913272607265411, 0.0008133044212548313, 0.0007844752568254982, 0.0008530961617686976, 0.0006981517874841754, 0.0007449270612151332, 0.0007233709354156258, 0.0007404043296932926, 0.0008311394931916372, 0.000674852364807086, 0.0007134995673811327, 0.0006874817993880217, 0.0006255965316465279, 0.0006742701269384806, 0.0005591100800671103, 0.0006451815121913144, 0.0005846013817210884, 0.0006616528468886949, 0.0006294424160334626, 0.0006155833470317842, 0.0005837171526396327, 0.0006195335638483929, 0.0006435015817496351, 0.0005547325150604671, 0.0005050358645579479, 0.0005273323314145453, 0.0005598720699355121, 0.0005744530673002085, 0.0005599768581224143, 0.00046436504816704495, 0.0005335675081133507, 0.0005898060905838401, 0.00048480103219395544, 0.000458425878102763, 0.00046774818796756126, 0.0004954945993239298, 0.0006133699153538841, 0.0005001585462916428, 0.0005661082682920015, 0.0005366530821790274, 0.0004633551113170888, 0.0004678991257063139, 0.0004867291917714132, 0.0007330125148582193, 0.0003883038469433688, 0.00044669139691921097, 0.00045098603987625124, 0.00045361000960772994, 0.0003580398735063043, 0.0005835402159864105, 0.000551586949868562, 0.0005220628236493502, 0.000631372977513847, 0.0005517835644895685, 0.0004831455182827766, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.007390573146148506, 0.012010990715140182, 0.00831746993516953, 0.005829943816020798, 0.004464527536307623, 0.003614988356319634, 0.003073814023824672, 0.002635827330134829, 0.0023176025614097574, 0.0020531677864177784, 0.0018602452109595532, 0.0017001824631971915, 0.0015721342571323148, 0.0014233087349911275, 0.0013445323138017694, 0.0012531676598418373, 0.0012414819978640106, 0.00117657510580151, 0.0011088059398492126, 0.0010155066092691826, 0.001035859103176031, 0.001024525076634564, 0.0009048026056008236, 0.0008540473867271731, 0.0008278719954294416, 0.0008854481166883451, 0.0008669666801497042, 0.0007656739061847699, 0.0007749812374292359, 0.000730198603121093, 0.0007981368610580486, 0.000737244317491471, 0.0007096193288212611, 0.0007304239752865947, 0.00068373538860633, 0.0006441241482566454, 0.0006838428331189597, 0.0006421299061144304, 0.0006913965458935066, 0.0006135610343373709, 0.000587165275901502, 0.0007344193874991975, 0.0006063662259723918, 0.0005951449831935117, 0.0008220721702266947, 0.0005476731857297237, 0.0005949477768198304, 0.0006134841946968633, 0.0005312384452524905, 0.0005465504065855014, 0.0007162447421183957, 0.0006244698976421693, 0.0006427657077832036, 0.0005913605896056797, 0.0005371937665844053, 0.0006741868874308337, 0.0005283895439957903, 0.0005457935619306105, 0.0005511248238181338, 0.0005228663152981526, 0.0005514006284555992, 0.0007597236339617159, 0.0004770996558714449, 0.0005764838882999117, 0.0006869946380089654, 0.0006167558310239456, 0.00047403521784262007, 0.0006315769056537049, 0.0005732730944465507, 0.0005531691625976425, 0.0006328440824192545, 0.0005116114996074758, 0.0005100772250455827, 0.000492458016443217, 0.0004496749619765034, 0.0005400425153331399, 0.0005220450367623161, 0.0006131684191183354, 0.0005754487157773429, 0.0004891041373193047, 0.0005896991623199184, 0.0005481769414921344, 0.0006079309171279303, 0.0005572433975217922, 0.0006433866073603093, 0.000574056101930178, 0.0006170841572612719, 0.0006585145621559367, 0.0005775744496581861, 0.0007092525528142131, 0.0006615427238736743, 0.000333976963644047, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.019398942744176462, 0.02190694606087954, 0.014517582583943953, 0.011855710756889284, 0.008158951513271694, 0.0063738928610450945, 0.005317619921793307, 0.004746695950761914, 0.0037758310343552217, 0.0037253428824521317, 0.0031960035631253894, 0.003006748871374232, 0.0024271121666267804, 0.0024200767402236313, 0.002249921994112646, 0.001981635585024837, 0.0017645089505963715, 0.0018005299673333128, 0.001670948038371861, 0.0015557057588642127, 0.0014111010319778582, 0.0017058919505463324, 0.001214649273306025, 0.0013625004774386012, 0.001179491934898155, 0.0010548252587659296, 0.0019060333851499398, 0.0012671745043559678, 0.0009469536548795828, 0.0010401260716364868, 0.0009260539500306399, 0.0011737333598394438, 0.0008336500758589271, 0.0010393761865382823, 0.0013264167627753407, 0.0009491790222747944, 0.0008374671483048151, 0.0008913272607265411, 0.0008133044212548313, 0.0007844752568254982, 0.0008530961617686976, 0.0006981517874841754, 0.0007449270612151332, 0.0007233709354156258, 0.0007404043296932926, 0.0008311394931916372, 0.000674852364807086, 0.0007134995673811327, 0.0006874817993880217, 0.0006255965316465279, 0.0006742701269384806, 0.0005591100800671103, 0.0006451815121913144, 0.0005846013817210884, 0.0006616528468886949, 0.0006294424160334626, 0.0006155833470317842, 0.0005837171526396327, 0.0006195335638483929, 0.0006435015817496351, 0.0005547325150604671, 0.0005050358645579479, 0.0005273323314145453, 0.0005598720699355121, 0.0005744530673002085, 0.0005599768581224143, 0.00046436504816704495, 0.0005335675081133507, 0.0005898060905838401, 0.00048480103219395544, 0.000458425878102763, 0.00046774818796756126, 0.0004954945993239298, 0.0006133699153538841, 0.0005001585462916428, 0.0005661082682920015, 0.0005366530821790274, 0.0004633551113170888, 0.0004678991257063139, 0.0004867291917714132, 0.0007330125148582193, 0.0003883038469433688, 0.00044669139691921097, 0.00045098603987625124, 0.00045361000960772994, 0.0003580398735063043, 0.0005835402159864105, 0.000551586949868562, 0.0005220628236493502, 0.000631372977513847, 0.0005517835644895685, 0.0004831455182827766, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.007390573146148506, 0.012010990715140182, 0.00831746993516953, 0.005829943816020798, 0.004464527536307623, 0.003614988356319634, 0.003073814023824672, 0.002635827330134829, 0.0023176025614097574, 0.0020531677864177784, 0.0018602452109595532, 0.0017001824631971915, 0.0015721342571323148, 0.0014233087349911275, 0.0013445323138017694, 0.0012531676598418373, 0.0012414819978640106, 0.00117657510580151, 0.0011088059398492126, 0.0010155066092691826, 0.001035859103176031, 0.001024525076634564, 0.0009048026056008236, 0.0008540473867271731, 0.0008278719954294416, 0.0008854481166883451, 0.0008669666801497042, 0.0007656739061847699, 0.0007749812374292359, 0.000730198603121093, 0.0007981368610580486, 0.000737244317491471, 0.0007096193288212611, 0.0007304239752865947, 0.00068373538860633, 0.0006441241482566454, 0.0006838428331189597, 0.0006421299061144304, 0.0006913965458935066, 0.0006135610343373709, 0.000587165275901502, 0.0007344193874991975, 0.0006063662259723918, 0.0005951449831935117, 0.0008220721702266947, 0.0005476731857297237, 0.0005949477768198304, 0.0006134841946968633, 0.0005312384452524905, 0.0005465504065855014, 0.0007162447421183957, 0.0006244698976421693, 0.0006427657077832036, 0.0005913605896056797, 0.0005371937665844053, 0.0006741868874308337, 0.0005283895439957903, 0.0005457935619306105, 0.0005511248238181338, 0.0005228663152981526, 0.0005514006284555992, 0.0007597236339617159, 0.0004770996558714449, 0.0005764838882999117, 0.0006869946380089654, 0.0006167558310239456, 0.00047403521784262007, 0.0006315769056537049, 0.0005732730944465507, 0.0005531691625976425, 0.0006328440824192545, 0.0005116114996074758, 0.0005100772250455827, 0.000492458016443217, 0.0004496749619765034, 0.0005400425153331399, 0.0005220450367623161, 0.0006131684191183354, 0.0005754487157773429, 0.0004891041373193047, 0.0005896991623199184, 0.0005481769414921344, 0.0006079309171279303, 0.0005572433975217922, 0.0006433866073603093, 0.000574056101930178, 0.0006170841572612719, 0.0006585145621559367, 0.0005775744496581861, 0.0007092525528142131, 0.0006615427238736743, 0.000333976963644047, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.015243691773825, 1.015243691773825, 1.0037625936703545, 0.9993938261190222, 0.9996703870999921, 0.9887634512831035, 0.9990291285234665, 1.0108793549381097, 1.003258315028867, 1.0049315025938927, 1.003673852380559, 0.9937620773687409, 0.9929331864187861, 0.9980607110146131, 1.0008197797374978, 1.0074072105395633, 1.0063442417463637, 1.0022615543775513, 0.9960851884126859, 1.0033715379108885, 0.9934612706028011, 1.0037013311719083, 1.0068348392263367, 1.0195558451880717, 0.9970196846291611, 1.003501039511463, 1.0045809641543666, 0.9930368282802721, 0.9937506852721314, 1.0130936607236964, 0.989502986609797, 1.0155101813838348, 0.9934877902417565, 1.0051640709734124, 0.9947853032228439, 1.0085187250286212, 1.0017460406269958, 0.9918971319975037, 0.9890261781258955, 0.9964053755382734, 0.9873376425814924, 0.9796092668102359, 0.995098325752308, 0.9936680703032448, 0.9991501939114584, 1.0017666203251572, 0.997991183450132, 0.98531726262975, 1.0101051253422173, 0.9913681375554221, 0.9901728536133818, 1.0021822554149944, 1.0086766913726823, 0.9945038829828721, 0.9752379752852066, 0.9694520512249086, 1.0132015716664067, 0.9710932802975145, 1.0126549709577348, 0.9810594713114866, 0.9910199419022262, 0.9721048663495256, 1.0265770298717294, 0.9611192619264354, 0.965756556602992, 0.9701991421050555, 0.9839396205158011, 0.982675017743262, 0.9785114384494944, 0.9628583410959621, 0.9456760603872016, 1.014998761162007, 0.9464617011378252, 0.9658450266099812, 0.9235347490764545, 0.9195598036405331, 0.9485857972901144, 0.9113870225671517, 0.9536215235082909, 0.9598681386403723, 0.9506254393630964, 0.8643118808492105, 0.9979135710450726, 0.907291001429521, 0.950846888753374, 1.0023513869680873, 0.996373109117132, 0.8980033788397821, 0.8245056826372572, 0.8002078012554439, 0.769049703799031, 0.8381268259876884, 0.40212318518260504, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.019507322642015, 1.0083440138264383, 1.007333482814437, 1.008569726325076, 1.0076783545280958, 1.0075822887122154, 1.0076263332495823, 1.007976395437767, 1.0073309135984343, 1.0081919212244264, 1.0078388451773312, 1.0082179643249178, 1.0073924395865523, 1.0081166038128457, 1.0082073674796612, 1.0078998048861902, 1.007619675556505, 1.0083205984917303, 1.008347936623511, 1.0082615585163173, 1.0080707871202215, 1.0103943556465105, 1.0080070524909004, 1.0093749234201186, 1.0086240632116217, 1.0081440822711312, 1.0153062366097723, 1.0108544921674518, 1.0087115083805647, 1.0098150101595358, 1.0093389237556514, 1.012276899838616, 1.009303571087982, 1.01188082343313, 1.0161228867316359, 1.0120306294164543, 1.0110898606947882, 1.0122814109659597, 1.0117728054836972, 1.01172427244934, 1.013206237640326, 1.0114266306352986, 1.0127817360118352, 1.012922147676672, 1.013795530154729, 1.0161761209469977, 1.0135796464657443, 1.0150391900593074, 1.0150217836322564, 1.0141837120952368, 1.0159863533288263, 1.0140638529183659, 1.0165369431166138, 1.0153397615788184, 1.0180134651807324, 1.018054318752248, 1.0182187314411524, 1.0181573373478838, 1.0197442557273622, 1.0216569071264847, 1.019210166090611, 1.0187834055317884, 1.0199180487104693, 1.021643303619723, 1.0226658520108756, 1.0233908322459344, 1.0208214639483135, 1.0246337398103513, 1.0277481563526996, 1.0237959178010259, 1.0246155279461087, 1.0263082446808645, 1.0289646048859777, 1.035675442142569, 1.0313629588652136, 1.0363799080122764, 1.0360821962535662, 1.0342719762334098, 1.0348013460265657, 1.039142498138575, 1.058253975093332, 1.0372760531550291, 1.0434011382373412, 1.0497450001990771, 1.0517235099154758, 1.0469500587286964, 1.0764220502392856, 1.0812564757459076, 1.0876699574260633, 1.1130526373537033, 1.15686071653958, 1.3474990968853844, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0226755552919855, 1.0083373925637211, 1.0035953536444535, 1.003884476328243, 0.9929649991374392, 1.0033294652260853, 1.0152877049965359, 1.0076875856855336, 1.0094312124534222, 1.0081887089447938, 0.9983247050105962, 0.9975800789349608, 1.0028490795447549, 1.0055933610513772, 1.0123118564857452, 1.0113400038719766, 1.007622643665179, 1.0015223703693066, 1.008911052905414, 0.9988541074091065, 1.009625923471695, 1.0130774843199475, 1.0255203668950088, 1.0028961074123453, 1.00955417154948, 1.011417321408045, 0.9999989293864476, 1.0003093726422887, 1.0202231073548556, 0.9963934077842574, 1.0235591069261853, 1.0011991452667766, 1.0130834535324467, 1.003134578869237, 1.0168296786702544, 1.0099101685143708, 1.000952677366381, 0.997873951124666, 1.0064135309523874, 0.9965075388507258, 0.9886987979969969, 1.0071185471752113, 1.0040723278881811, 1.0097817398933804, 1.0170838206154686, 1.0086503180049966, 0.9972890373409542, 1.023036184903041, 1.002975934283747, 1.002564408266251, 1.0191637900551365, 1.0243846049043652, 1.010978905509198, 0.9907550964130328, 0.9840771242600777, 1.0325392976508834, 0.9867314343261927, 1.029632642046313, 0.9986235712959476, 1.0086168951205712, 0.9911996505338361, 1.0548328392314814, 0.9791399551767517, 0.9880420330472638, 0.9973054797394904, 1.0097021711836167, 1.0039300782554617, 1.0076700752246464, 0.9898286822156213, 0.97282775159476, 1.0489798079144086, 0.9752370141362604, 0.9956620726583936, 0.9521775909137948, 0.9477571371455814, 0.9832906375670701, 0.9464870380057553, 0.9989744137081361, 1.002668795401762, 0.9899589293370887, 0.9111764563073632, 1.0505369817330492, 0.9663583887913486, 1.0123123676588013, 1.0757144364168052, 1.0716495509146509, 0.9788184369559932, 0.9215140918479925, 0.8971998204495272, 0.8960473335696765, 1.026189813663596, 0.642333823292888, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [0.980492677357985, 0.9916559861735617, 0.992666517185563, 0.9914302736749241, 0.9923216454719043, 0.9924177112877846, 0.9923736667504176, 0.9920236045622332, 0.9926690864015657, 0.9918080787755736, 0.9921611548226686, 0.991782035675082, 0.9926075604134478, 0.9918833961871544, 0.9917926325203387, 0.9921001951138098, 0.992380324443495, 0.9916794015082698, 0.9916520633764888, 0.9917384414836828, 0.9919292128797786, 0.9896056443534894, 0.9919929475090997, 0.9906250765798815, 0.9913759367883784, 0.9918559177288689, 0.9846937633902277, 0.9891455078325482, 0.9912884916194354, 0.9901849898404641, 0.9906610762443486, 0.987723100161384, 0.9906964289120178, 0.98811917656687, 0.9838771132683641, 0.9879693705835457, 0.9889101393052117, 0.9877185890340404, 0.9882271945163028, 0.9882757275506601, 0.9867937623596741, 0.9885733693647014, 0.9872182639881648, 0.987077852323328, 0.9862044698452709, 0.9838238790530023, 0.9864203535342557, 0.9849608099406926, 0.9849782163677436, 0.9858162879047632, 0.9840136466711736, 0.9859361470816341, 0.9834630568833861, 0.9846602384211816, 0.9819865348192676, 0.981945681247752, 0.9817812685588476, 0.9818426626521163, 0.9802557442726377, 0.9783430928735154, 0.9807898339093889, 0.9812165944682116, 0.9800819512895307, 0.9783566963802769, 0.9773341479891245, 0.9766091677540656, 0.9791785360516866, 0.9753662601896487, 0.9722518436473004, 0.9762040821989741, 0.9753844720538913, 0.9736917553191355, 0.9710353951140223, 0.9643245578574311, 0.9686370411347865, 0.9636200919877236, 0.9639178037464338, 0.9657280237665903, 0.9651986539734342, 0.9608575018614248, 0.941746024906668, 0.9627239468449709, 0.9565988617626587, 0.9502549998009228, 0.9482764900845242, 0.9530499412713036, 0.9235779497607143, 0.9187435242540924, 0.9123300425739367, 0.8869473626462966, 0.84313928346042, 0.6525009031146156, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0078118282556643, 0.9991877947769878, 0.9951922985935909, 0.9954562978717412, 0.9845619034287678, 0.9947287918208475, 1.0064710048796834, 0.9988290443722002, 1.0004317927343633, 0.9991589958163244, 0.9891994497268856, 0.9882862939026115, 0.9932723424844713, 0.9960461984236185, 1.0025025645933814, 1.0013484796207506, 0.9969004650899237, 0.9906480064560652, 0.997832022916363, 0.9880684337964957, 0.9977767388721217, 1.000592194132726, 1.0135913234811347, 0.9911432618459769, 0.9974479074734459, 0.997744606900688, 0.9860747271740965, 0.9871919979019741, 1.0059642140925373, 0.9826125654353365, 1.0074612558414844, 0.9857764352167364, 0.9972446884143781, 0.9864360275764509, 1.0002077713869881, 0.9935819127396207, 0.9828415866286264, 0.9801784051271251, 0.9863972201241594, 0.9781677463122589, 0.9705197356234748, 0.9830781043294047, 0.9832638127183085, 0.9885186479295366, 0.9864494200348457, 0.9873320488952675, 0.9733454879185457, 0.9971740657813939, 0.9797603408270973, 0.9777812989605125, 0.9852007207748523, 0.9929687778409995, 0.9780288604565461, 0.9597208541573804, 0.9548269781897396, 0.9938638456819299, 0.9554551262688363, 0.9956772998691567, 0.9634953713270255, 0.9734229886838812, 0.9530100821652151, 0.9983212205119772, 0.9430985686761192, 0.9434710801587203, 0.9430928044706207, 0.9581770698479853, 0.9614199572310623, 0.9493528016743423, 0.9358879999763029, 0.9185243691796433, 0.9810177144096054, 0.9176863881393902, 0.9360279805615688, 0.894891907239114, 0.891362470135485, 0.9138809570131585, 0.876287007128548, 0.9082686333084455, 0.9170674818789828, 0.9112919493891041, 0.8174473053910578, 0.945290160357096, 0.8482236140676935, 0.8893814098479466, 0.9289883375193694, 0.921096667319613, 0.817188320723571, 0.7274972734265218, 0.7032157820613607, 0.6420520740283857, 0.6500638383117807, 0.161912547072322, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.019507322642015046, 0.008344013826438346, 0.00733348281443702, 0.00856972632507591, 0.007678354528095732, 0.007582288712215446, 0.0076263332495823954, 0.007976395437766848, 0.007330913598434297, 0.008191921224426357, 0.007838845177331355, 0.008217964324917948, 0.007392439586552224, 0.008116603812845624, 0.008207367479661332, 0.007899804886190243, 0.007619675556505001, 0.008320598491730169, 0.008347936623511187, 0.008261558516317158, 0.008070787120221357, 0.010394355646510589, 0.00800705249090028, 0.009374923420118475, 0.008624063211621569, 0.008144082271131059, 0.015306236609772261, 0.010854492167451824, 0.008711508380564559, 0.009815010159535897, 0.009338923755651374, 0.012276899838616018, 0.009303571087982188, 0.011880823433130017, 0.016122886731635866, 0.012030629416454275, 0.011089860694788345, 0.012281410965959583, 0.01177280548369719, 0.011724272449339934, 0.013206237640325913, 0.011426630635298585, 0.012781736011835187, 0.012922147676671991, 0.013795530154729119, 0.01617612094699772, 0.013579646465744277, 0.015039190059307428, 0.01502178363225637, 0.014183712095236833, 0.015986353328826364, 0.014063852918365871, 0.01653694311661391, 0.015339761578818445, 0.018013465180732435, 0.018054318752248055, 0.01821873144115238, 0.018157337347883717, 0.01974425572736227, 0.021656907126484604, 0.019210166090611103, 0.018783405531788366, 0.019918048710469316, 0.02164330361972311, 0.022665852010875454, 0.023390832245934412, 0.020821463948313412, 0.02463373981035133, 0.02774815635269956, 0.023795917801025857, 0.024615527946108662, 0.026308244680864457, 0.02896460488597774, 0.0356754421425689, 0.03136295886521345, 0.03637990801227642, 0.036082196253566234, 0.03427197623340972, 0.034801346026565816, 0.03914249813857518, 0.05825397509333197, 0.03727605315502913, 0.043401138237341264, 0.04974500019907724, 0.05172350991547581, 0.0469500587286964, 0.07642205023928572, 0.08125647574590755, 0.08766995742606332, 0.11305263735370341, 0.15686071653958, 0.3474990968853844, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.019507322642015046, 0.008344013826438346, 0.007333482814436909, 0.00856972632507591, 0.007678354528095843, 0.007582288712215446, 0.007626333249582284, 0.007976395437766959, 0.007330913598434297, 0.008191921224426357, 0.007838845177331244, 0.008217964324917837, 0.007392439586552335, 0.008116603812845735, 0.00820736747966122, 0.007899804886190243, 0.007619675556505001, 0.00832059849173028, 0.008347936623511076, 0.008261558516317269, 0.008070787120221468, 0.010394355646510478, 0.00800705249090039, 0.009374923420118586, 0.00862406321162168, 0.00814408227113117, 0.015306236609772261, 0.010854492167451824, 0.00871150838056467, 0.009815010159535786, 0.009338923755651374, 0.012276899838616018, 0.009303571087982077, 0.011880823433130017, 0.016122886731635866, 0.012030629416454275, 0.011089860694788234, 0.012281410965959694, 0.01177280548369719, 0.011724272449340045, 0.013206237640325913, 0.011426630635298585, 0.012781736011835187, 0.012922147676672102, 0.013795530154729008, 0.01617612094699772, 0.013579646465744277, 0.015039190059307428, 0.01502178363225637, 0.014183712095236833, 0.015986353328826253, 0.014063852918365871, 0.0165369431166138, 0.015339761578818445, 0.018013465180732435, 0.018054318752247944, 0.01821873144115238, 0.01815733734788383, 0.01974425572736216, 0.021656907126484715, 0.01921016609061099, 0.018783405531788366, 0.019918048710469316, 0.021643303619722998, 0.022665852010875565, 0.023390832245934412, 0.020821463948313523, 0.02463373981035133, 0.02774815635269956, 0.023795917801025857, 0.024615527946108662, 0.026308244680864457, 0.02896460488597774, 0.0356754421425689, 0.031362958865213564, 0.03637990801227642, 0.036082196253566234, 0.03427197623340983, 0.034801346026565705, 0.039142498138575066, 0.05825397509333197, 0.03727605315502913, 0.04340113823734115, 0.04974500019907713, 0.05172350991547581, 0.0469500587286964, 0.07642205023928561, 0.08125647574590755, 0.08766995742606332, 0.1130526373537033, 0.1568607165395799, 0.3474990968853844, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [0.0074318635181607196, 0.0045747988933666495, 0.004201527525431237, 0.00421408922825095, 0.0042015478543356855, 0.004300336702618979, 0.004408350058426214, 0.004429270656666762, 0.0044997098595294105, 0.0045148565642346705, 0.004562627641855332, 0.004646892516174672, 0.004788368530141862, 0.004773581313879283, 0.004904645946181896, 0.004995762125613146, 0.005361089287627574, 0.005437181956620685, 0.005539514994525541, 0.005392836806305423, 0.005924592299786591, 0.00624264509361061, 0.005964521706937065, 0.005876422783184232, 0.006053132038017051, 0.006836357253678593, 0.006962101106175567, 0.006558687370157301, 0.007129446631159109, 0.0068904211744604815, 0.008048925542350371, 0.007711355025020072, 0.00791938255903435, 0.008349275646392984, 0.008310953641633034, 0.008164127887375083, 0.009055545368877316, 0.008847772998770487, 0.010008155414113928, 0.00916989626923348, 0.009089531186761035, 0.012020221422903377, 0.010404257584936238, 0.010631545981921842, 0.015317200290311472, 0.010659134554864558, 0.011971774711204253, 0.01293105956082341, 0.011607796728324793, 0.012391554652869341, 0.01698153464014207, 0.015707913531682882, 0.016475022526325933, 0.015517121127826217, 0.014625073035169023, 0.019337725984476806, 0.015638154028678186, 0.016977671088578172, 0.01756409998446118, 0.01759695321834498, 0.019094784184310543, 0.028255809359752138, 0.01802069325031619, 0.0222854764442717, 0.02710633763443482, 0.025762550667815742, 0.02125506051219972, 0.02915863677515207, 0.026970341119659236, 0.027151691207558337, 0.033981046752401656, 0.028775312998435054, 0.0298170460484124, 0.02864284183734045, 0.02819733350504816, 0.03470484027695586, 0.03510001543860364, 0.04535289019984534, 0.042800656761389555, 0.03933348997399233, 0.0468645754581527, 0.0526234106879766, 0.059067387361827484, 0.06146547890542742, 0.07336304944871797, 0.07527644179751891, 0.08081505811621115, 0.09700840921073539, 0.09699201919408318, 0.12699762977064533, 0.18806298767590768, 0.24021063811028304, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0074318635181604975, 0.0045747988933666495, 0.004201527525431348, 0.00421408922825095, 0.0042015478543356855, 0.004300336702618868, 0.004408350058426214, 0.004429270656666651, 0.0044997098595294105, 0.0045148565642347815, 0.004562627641855332, 0.004646892516174672, 0.004788368530141751, 0.004773581313879394, 0.004904645946181896, 0.004995762125612924, 0.005361089287627685, 0.005437181956620685, 0.00553951499452543, 0.005392836806305423, 0.005924592299786813, 0.006242645093610832, 0.005964521706937065, 0.005876422783184121, 0.006053132038017051, 0.006836357253678482, 0.006962101106175567, 0.006558687370157301, 0.007129446631159109, 0.0068904211744604815, 0.008048925542350593, 0.007711355025020072, 0.007919382559034238, 0.008349275646393095, 0.008310953641633256, 0.008164127887374972, 0.009055545368877316, 0.008847772998770487, 0.01000815541411404, 0.00916989626923348, 0.009089531186761035, 0.012020221422903266, 0.01040425758493635, 0.010631545981921953, 0.015317200290311472, 0.010659134554864558, 0.011971774711204253, 0.012931059560823632, 0.011607796728324904, 0.01239155465286923, 0.01698153464014207, 0.015707913531682882, 0.016475022526325933, 0.015517121127826217, 0.014625073035169023, 0.019337725984476695, 0.015638154028678186, 0.016977671088578283, 0.017564099984460957, 0.01759695321834498, 0.01909478418431043, 0.028255809359752027, 0.0180206932503163, 0.022285476444271812, 0.02710633763443482, 0.02576255066781563, 0.02125506051219961, 0.029158636775151958, 0.026970341119659125, 0.027151691207558337, 0.033981046752401545, 0.028775312998435165, 0.0298170460484124, 0.028642841837340338, 0.028197333505048272, 0.03470484027695575, 0.03510001543860364, 0.04535289019984523, 0.042800656761389555, 0.03933348997399233, 0.0468645754581527, 0.0526234106879766, 0.059067387361827595, 0.061465478905427307, 0.07336304944871785, 0.07527644179751891, 0.08081505811621115, 0.09700840921073528, 0.09699201919408329, 0.12699762977064544, 0.18806298767590768, 0.24021063811028298, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}