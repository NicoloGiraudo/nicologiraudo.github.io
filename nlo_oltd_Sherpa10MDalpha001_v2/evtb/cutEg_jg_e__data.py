
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
  'curve0' : [59.42987142857143, 3.4867799999999995, 2.001024285714286, 1.417149142857142, 1.0803631428571436, 0.8836875714285714, 0.7354657142857143, 0.6131651428571423, 0.5564697142857147, 0.48498642857142893, 0.4414498571428567, 0.3917924285714289, 0.36570228571428537, 0.32383657142857164, 0.3007839999999998, 0.2770288571428569, 0.25772028571428635, 0.24282657142857123, 0.22258557142857122, 0.21267714285714334, 0.1992217142857141, 0.1829517142857141, 0.17827242857142842, 0.1685302857142861, 0.1601751428571427, 0.15149771428571415, 0.14599657142857175, 0.13845285714285702, 0.13173190000000032, 0.12540747142857092, 0.12126282857142884, 0.11578817142857097, 0.10972418571428597, 0.10597938571428596, 0.10499582857142814, 0.09786925714285737, 0.09424785714285736, 0.0905521428571425, 0.08775837142857162, 0.08493507142857162, 0.08089371428571396, 0.07757001428571446, 0.06688294285714301, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [59.42987142857143, 59.42987142857143, 3.4867799999999995, 2.001024285714286, 1.417149142857142, 1.0803631428571436, 0.8836875714285714, 0.7354657142857143, 0.6131651428571423, 0.5564697142857147, 0.48498642857142893, 0.4414498571428567, 0.3917924285714289, 0.36570228571428537, 0.32383657142857164, 0.3007839999999998, 0.2770288571428569, 0.25772028571428635, 0.24282657142857123, 0.22258557142857122, 0.21267714285714334, 0.1992217142857141, 0.1829517142857141, 0.17827242857142842, 0.1685302857142861, 0.1601751428571427, 0.15149771428571415, 0.14599657142857175, 0.13845285714285702, 0.13173190000000032, 0.12540747142857092, 0.12126282857142884, 0.11578817142857097, 0.10972418571428597, 0.10597938571428596, 0.10499582857142814, 0.09786925714285737, 0.09424785714285736, 0.0905521428571425, 0.08775837142857162, 0.08493507142857162, 0.08089371428571396, 0.07757001428571446, 0.06688294285714301, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [1.1234530407159338, 0.032665422022658264, 0.02031992587966556, 0.01450489713222146, 0.01042174434065819, 0.010843126290655385, 0.008223035091889671, 0.0055697323425230125, 0.006480652524465202, 0.005069017535529961, 0.006390464835700644, 0.0040812873119212036, 0.007561191192193057, 0.003631814074176674, 0.0033075374648872283, 0.0035344901199696748, 0.0029698271783704508, 0.003121461261679095, 0.0023463884536687857, 0.004610887736031513, 0.002704086476699548, 0.0016959591831823084, 0.0020656219106000525, 0.002342942942679801, 0.0025475394291074537, 0.0018961895195041937, 0.002189301910916555, 0.0018398036718683878, 0.00193777275894418, 0.0015168798534478266, 0.0019635006223267587, 0.0017990672186282623, 0.0015394287305122447, 0.002125019087549333, 0.004236783772473375, 0.0014200134377058955, 0.0036157221877206732, 0.001349252022569597, 0.0013414634104710651, 0.0012185560206696329, 0.0013841107806318138, 0.0010803659621836036, 0.0011667684309358808, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [1.1234530407159338, 0.032665422022658264, 0.02031992587966556, 0.01450489713222146, 0.01042174434065819, 0.010843126290655385, 0.008223035091889671, 0.0055697323425230125, 0.006480652524465202, 0.005069017535529961, 0.006390464835700644, 0.0040812873119212036, 0.007561191192193057, 0.003631814074176674, 0.0033075374648872283, 0.0035344901199696748, 0.0029698271783704508, 0.003121461261679095, 0.0023463884536687857, 0.004610887736031513, 0.002704086476699548, 0.0016959591831823084, 0.0020656219106000525, 0.002342942942679801, 0.0025475394291074537, 0.0018961895195041937, 0.002189301910916555, 0.0018398036718683878, 0.00193777275894418, 0.0015168798534478266, 0.0019635006223267587, 0.0017990672186282623, 0.0015394287305122447, 0.002125019087549333, 0.004236783772473375, 0.0014200134377058955, 0.0036157221877206732, 0.001349252022569597, 0.0013414634104710651, 0.0012185560206696329, 0.0013841107806318138, 0.0010803659621836036, 0.0011667684309358808, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0189038443750666, 1.0093683633675363, 1.01015476225088, 1.0102352650780129, 1.0096465196999378, 1.0122703166155504, 1.0111807184647295, 1.009083576272079, 1.011646011198981, 1.0104518750152685, 1.0144760831435329, 1.0104169632037112, 1.020675810591188, 1.011214959626565, 1.0109963876565482, 1.0127585629757951, 1.0115234513656517, 1.012854693962507, 1.0105415119165608, 1.0216802223035726, 1.01357325172306, 1.0092699824639726, 1.0115868837775575, 1.0139022071478112, 1.0159047114531345, 1.0125162912750492, 1.0149955707143963, 1.0132883041190697, 1.0147099735063732, 1.0120956099040066, 1.0161921063977999, 1.0155375734535896, 1.014029985463012, 1.0200512493370952, 1.0403519247394777, 1.0145092900381694, 1.0383639723738238, 1.0149002771220799, 1.0152858740269912, 1.0143469122963464, 1.017110238945676, 1.013927623607291, 1.0174449326105164, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [0.9810961556249334, 0.9906316366324637, 0.98984523774912, 0.9897647349219872, 0.9903534803000621, 0.9877296833844496, 0.9888192815352705, 0.9909164237279211, 0.988353988801019, 0.9895481249847317, 0.9855239168564672, 0.9895830367962889, 0.979324189408812, 0.988785040373435, 0.9890036123434517, 0.9872414370242049, 0.9884765486343482, 0.9871453060374932, 0.9894584880834392, 0.9783197776964274, 0.98642674827694, 0.9907300175360274, 0.9884131162224425, 0.9860977928521888, 0.9840952885468655, 0.9874837087249508, 0.9850044292856038, 0.9867116958809303, 0.985290026493627, 0.9879043900959936, 0.9838078936022, 0.9844624265464104, 0.9859700145369882, 0.9799487506629048, 0.9596480752605223, 0.9854907099618306, 0.9616360276261762, 0.98509972287792, 0.9847141259730087, 0.9856530877036537, 0.9828897610543239, 0.9860723763927091, 0.9825550673894835, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.018903844375066647, 0.009368363367536325, 0.010154762250879967, 0.010235265078012756, 0.009646519699937905, 0.012270316615550447, 0.011180718464729456, 0.009083576272078897, 0.01164601119898101, 0.010451875015268342, 0.01447608314353277, 0.010416963203711105, 0.02067581059118795, 0.011214959626565046, 0.010996387656548312, 0.01275856297579514, 0.011523451365651805, 0.012854693962506825, 0.01054151191656083, 0.021680222303572583, 0.01357325172306001, 0.009269982463972593, 0.011586883777557455, 0.013902207147811207, 0.015904711453134546, 0.012516291275049163, 0.014995570714396167, 0.013288304119069672, 0.014709973506373042, 0.012095609904006377, 0.0161921063978, 0.015537573453589637, 0.014029985463011818, 0.020051249337095234, 0.040351924739477685, 0.014509290038169365, 0.03836397237382383, 0.014900277122079975, 0.01528587402699133, 0.014346912296346326, 0.017110238945676093, 0.01392762360729094, 0.017444932610516495, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.018903844375066647, 0.009368363367536325, 0.010154762250879967, 0.010235265078012867, 0.009646519699937794, 0.012270316615550447, 0.011180718464729456, 0.009083576272078897, 0.011646011198980899, 0.010451875015268453, 0.01447608314353288, 0.010416963203711216, 0.02067581059118795, 0.011214959626564935, 0.010996387656548201, 0.01275856297579514, 0.011523451365651693, 0.012854693962506936, 0.01054151191656083, 0.021680222303572583, 0.01357325172306001, 0.009269982463972593, 0.011586883777557455, 0.013902207147811207, 0.015904711453134546, 0.012516291275049163, 0.014995570714396278, 0.013288304119069672, 0.014709973506373153, 0.012095609904006599, 0.016192106397799888, 0.015537573453589637, 0.01402998546301193, 0.020051249337095234, 0.040351924739477685, 0.014509290038169365, 0.03836397237382383, 0.014900277122079864, 0.01528587402699122, 0.014346912296346437, 0.017110238945676093, 0.01392762360729094, 0.017444932610516384, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}