
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0010308230000000088, 0.002129274285714277, 0.0031384257142857016, 0.00397240428571432, 0.004906847142857123, 0.005467564285714263, 0.006254685714285689, 0.006460117142857199, 0.008021097142857111, 0.008527569999999965, 0.009187851428571507, 0.010201821428571387, 0.012618305714285663, 0.013795035714285833, 0.014374271428571369, 0.017165128571428503, 0.01717540000000015, 0.01994499999999992, 0.020800657142857056, 0.022648571428571625, 0.02583501428571418, 0.028490099999999883, 0.027917528571428808, 0.03206155714285701, 0.036261057142856996, 0.037168742857143174, 0.042149028571428396, 0.04521675714285696, 0.050238442857143295, 0.05571139999999977, 0.06343117142857117, 0.07329691428571398, 0.07696537142857209, 0.08742382857142822, 0.09296788571428534, 0.10556722857142949, 0.11716099999999953, 0.13420061428571373, 0.15648357142857278, 0.17279785714285645, 0.21919142857142768, 0.22009542857143047, 0.28461371428571314],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007608281428571495, 0.0015498942857142795, 0.002209235714285705, 0.0028719642857143106, 0.003872638571428556, 0.004561478571428553, 0.005343111428571407, 0.006051837142857195, 0.0073479057142856845, 0.007994968571428538, 0.008830600000000077, 0.01020898999999996, 0.011155608571428527, 0.012719654285714395, 0.013555047142857088, 0.015374714285714224, 0.01671457142857157, 0.018141728571428498, 0.020345685714285633, 0.02170362857142876, 0.023754171428571332, 0.025687185714285608, 0.029313528571428826, 0.03126858571428559, 0.03481611428571415, 0.038368800000000335, 0.04146148571428555, 0.0461224142857141, 0.050598442857143294, 0.056903199999999765, 0.06165028571428546, 0.06800447142857116, 0.07545117142857208, 0.08538065714285681, 0.09310994285714248, 0.10358865714285803, 0.12145835714285665, 0.13646745714285657, 0.15500100000000133, 0.17547242857142786, 0.20272014285714204, 0.23508900000000202, 0.2835527142857131],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0010308230000000088, 0.002129274285714277, 0.0031384257142857016, 0.00397240428571432, 0.004906847142857123, 0.005467564285714263, 0.006254685714285689, 0.006460117142857199, 0.008021097142857111, 0.008527569999999965, 0.009187851428571507, 0.010201821428571387, 0.012618305714285663, 0.013795035714285833, 0.014374271428571369, 0.017165128571428503, 0.01717540000000015, 0.01994499999999992, 0.020800657142857056, 0.022648571428571625, 0.02583501428571418, 0.028490099999999883, 0.027917528571428808, 0.03206155714285701, 0.036261057142856996, 0.037168742857143174, 0.042149028571428396, 0.04521675714285696, 0.050238442857143295, 0.05571139999999977, 0.06343117142857117, 0.07329691428571398, 0.07696537142857209, 0.08742382857142822, 0.09296788571428534, 0.10556722857142949, 0.11716099999999953, 0.13420061428571373, 0.15648357142857278, 0.17279785714285645, 0.21919142857142768, 0.22009542857143047, 0.28461371428571314],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007608281428571495, 0.0015498942857142795, 0.002209235714285705, 0.0028719642857143106, 0.003872638571428556, 0.004561478571428553, 0.005343111428571407, 0.006051837142857195, 0.0073479057142856845, 0.007994968571428538, 0.008830600000000077, 0.01020898999999996, 0.011155608571428527, 0.012719654285714395, 0.013555047142857088, 0.015374714285714224, 0.01671457142857157, 0.018141728571428498, 0.020345685714285633, 0.02170362857142876, 0.023754171428571332, 0.025687185714285608, 0.029313528571428826, 0.03126858571428559, 0.03481611428571415, 0.038368800000000335, 0.04146148571428555, 0.0461224142857141, 0.050598442857143294, 0.056903199999999765, 0.06165028571428546, 0.06800447142857116, 0.07545117142857208, 0.08538065714285681, 0.09310994285714248, 0.10358865714285803, 0.12145835714285665, 0.13646745714285657, 0.15500100000000133, 0.17547242857142786, 0.20272014285714204, 0.23508900000000202, 0.2835527142857131],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.409834787964645e-05, 7.98231335707962e-05, 0.00012195937764648624, 0.00015799857917211976, 0.0002074233568805391, 0.00025287255804504443, 0.0003014194649944663, 0.00030866645362241483, 0.0003906325587023771, 0.00040377673665185714, 0.00048072479292274523, 0.0005285907332382056, 0.0006327328159077316, 0.0007062749363486532, 0.0007338143289605013, 0.0008732419072464527, 0.0008839437372436428, 0.0010516612708336367, 0.001021306885858522, 0.0011863072527634685, 0.0013586590027355175, 0.001552895912250945, 0.0013083325577362517, 0.001543858801833892, 0.0017759579191558056, 0.0018397432163323431, 0.0018529226775501355, 0.001966721087682405, 0.002319178689950056, 0.002486712032924968, 0.0026757188620203302, 0.0031838501913275135, 0.0033650281255458298, 0.0037490847862770137, 0.0037875906401223904, 0.004303147637699299, 0.004517724729849497, 0.004943102801492424, 0.006300604117455614, 0.006410181633263463, 0.0077753010309857765, 0.007639912650424968, 0.009728613383588956],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00019028464178162094, 0.00010280985023878969, 9.974111386944848e-05, 0.0001250371455012562, 0.0002607941560632334, 0.0002050080137806456, 0.00022779228812804843, 0.00021873243369701997, 0.0003664670266649538, 0.0003103114630200307, 0.0004262981614421797, 0.00032171368307479584, 0.0003465087683314973, 0.00043373611840399743, 0.00042848220499805883, 0.00046769037376696556, 0.0005534603575207027, 0.0004618891995414695, 0.000625709067166755, 0.0005214585118605712, 0.0005539581137926695, 0.0006222428163096594, 0.0006351170549350684, 0.0007150049236308253, 0.0007827026698483595, 0.0007911194600058899, 0.0008271748081665087, 0.0008923779285408914, 0.0009848274478510602, 0.0010534452708971173, 0.0011538434442668296, 0.0012367993584495474, 0.0012810066194925388, 0.0014146369693677685, 0.0015130574533516032, 0.0016572986379980682, 0.0018281059675443877, 0.0020092474984939133, 0.0022316640629351015, 0.0024827030200396975, 0.0027490688590569488, 0.0031453081351922093, 0.0036184899319681675],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.409834787964645e-05, 7.98231335707962e-05, 0.00012195937764648624, 0.00015799857917211976, 0.0002074233568805391, 0.00025287255804504443, 0.0003014194649944663, 0.00030866645362241483, 0.0003906325587023771, 0.00040377673665185714, 0.00048072479292274523, 0.0005285907332382056, 0.0006327328159077316, 0.0007062749363486532, 0.0007338143289605013, 0.0008732419072464527, 0.0008839437372436428, 0.0010516612708336367, 0.001021306885858522, 0.0011863072527634685, 0.0013586590027355175, 0.001552895912250945, 0.0013083325577362517, 0.001543858801833892, 0.0017759579191558056, 0.0018397432163323431, 0.0018529226775501355, 0.001966721087682405, 0.002319178689950056, 0.002486712032924968, 0.0026757188620203302, 0.0031838501913275135, 0.0033650281255458298, 0.0037490847862770137, 0.0037875906401223904, 0.004303147637699299, 0.004517724729849497, 0.004943102801492424, 0.006300604117455614, 0.006410181633263463, 0.0077753010309857765, 0.007639912650424968, 0.009728613383588956],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00019028464178162094, 0.00010280985023878969, 9.974111386944848e-05, 0.0001250371455012562, 0.0002607941560632334, 0.0002050080137806456, 0.00022779228812804843, 0.00021873243369701997, 0.0003664670266649538, 0.0003103114630200307, 0.0004262981614421797, 0.00032171368307479584, 0.0003465087683314973, 0.00043373611840399743, 0.00042848220499805883, 0.00046769037376696556, 0.0005534603575207027, 0.0004618891995414695, 0.000625709067166755, 0.0005214585118605712, 0.0005539581137926695, 0.0006222428163096594, 0.0006351170549350684, 0.0007150049236308253, 0.0007827026698483595, 0.0007911194600058899, 0.0008271748081665087, 0.0008923779285408914, 0.0009848274478510602, 0.0010534452708971173, 0.0011538434442668296, 0.0012367993584495474, 0.0012810066194925388, 0.0014146369693677685, 0.0015130574533516032, 0.0016572986379980682, 0.0018281059675443877, 0.0020092474984939133, 0.0022316640629351015, 0.0024827030200396975, 0.0027490688590569488, 0.0031453081351922093, 0.0036184899319681675],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7380783537592225, 0.7278979021692167, 0.7039311793264866, 0.7229788508794422, 0.7892315490336682, 0.8342798242623054, 0.8542573796102579, 0.9367999076531561, 0.9160724004981149, 0.9375435876138889, 0.9611169780716651, 1.000702675642655, 0.8840813358007992, 0.9220457669813934, 0.9430075959129358, 0.8956946766658982, 0.9731692670081294, 0.9095877950076996, 0.9781270646669131, 0.958278037088432, 0.9194564851356216, 0.9016179555103602, 1.050004426302574, 0.9752672203337421, 0.9601516621137042, 1.032286729402432, 0.9836878124966107, 1.0200292369485018, 1.0071658271938022, 1.021392390067383, 0.97192412383096, 0.9277944657190793, 0.9803262172078873, 0.9766291243250452, 1.0015280238091433, 0.9812577117411707, 1.0366790753139452, 1.016891449187533, 0.9905257055738393, 1.0154780358552726, 0.9248543347628296, 1.0681230479246664, 0.9962721402843753],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.042779747715802, 1.037488422279058, 1.0388600491932447, 1.0397740430752023, 1.0422722271229672, 1.0462495811353794, 1.0481909849292708, 1.0477803183435612, 1.048700639294743, 1.047349565779215, 1.052321785638352, 1.0518133685184712, 1.0501440391629908, 1.0511977606275604, 1.0510505407252793, 1.050873018725882, 1.0514656856459608, 1.0527280657224187, 1.0490997413612597, 1.0523788997687915, 1.0525898297446195, 1.054506509708669, 1.0468641969645986, 1.048152957604489, 1.0489770034050332, 1.0494970524939016, 1.043961219044706, 1.0434954032963661, 1.0461634270103635, 1.0446356047940812, 1.0421830277095452, 1.043437711155435, 1.0437213263976612, 1.0428840151196752, 1.0407408494989618, 1.0407621540882612, 1.038559970722762, 1.0368336823777016, 1.0402636779052012, 1.037096418550862, 1.0354726509228076, 1.0347118188688116, 1.0341818151946913],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9226732277401284, 0.7761818883745456, 0.735711798958629, 0.7544552909666001, 0.8423805770083567, 0.8717751335202676, 0.8906768415198741, 0.9706588035307437, 0.9617602933309921, 0.973932789112092, 1.0075150031982487, 1.032237601570078, 0.9115421357035312, 0.9534872309534533, 0.9728165644667351, 0.9229412173382144, 1.0053932826072245, 0.9327459398831808, 1.0082082809895245, 0.9813019400972876, 0.9408986298027909, 0.9234586235427527, 1.072754185591262, 0.9975682246313491, 0.9817368758807701, 1.0535712657949199, 1.0033128154018314, 1.0397647948462414, 1.026768891935508, 1.040301361496877, 0.9901146036578407, 0.9446682914524309, 0.9969701519504277, 0.9928104903494347, 1.0178030788104115, 0.9969566995845117, 1.052282441344829, 1.0318634186467504, 1.004787036923589, 1.029845708354748, 0.9373961977224076, 1.0824137042804454, 1.008985828172007],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.957220252284198, 0.9625115777209422, 0.9611399508067554, 0.9602259569247976, 0.9577277728770328, 0.9537504188646206, 0.9518090150707293, 0.9522196816564387, 0.9512993607052571, 0.9526504342207852, 0.947678214361648, 0.9481866314815288, 0.9498559608370091, 0.9488022393724396, 0.9489494592747207, 0.9491269812741181, 0.9485343143540392, 0.9472719342775814, 0.9509002586387403, 0.9476211002312085, 0.9474101702553807, 0.945493490291331, 0.9531358030354012, 0.9518470423955111, 0.9510229965949668, 0.9505029475060984, 0.956038780955294, 0.9565045967036339, 0.9538365729896364, 0.9553643952059188, 0.9578169722904548, 0.9565622888445652, 0.9562786736023388, 0.9571159848803249, 0.959259150501038, 0.9592378459117388, 0.961440029277238, 0.9631663176222983, 0.9597363220947986, 0.962903581449138, 0.9645273490771924, 0.9652881811311884, 0.9658181848053087],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5534834797783166, 0.6796139159638878, 0.6721505596943443, 0.6915024107922844, 0.7360825210589798, 0.7967845150043432, 0.8178379177006416, 0.9029410117755686, 0.8703845076652376, 0.9011543861156858, 0.9147189529450813, 0.9691677497152319, 0.8566205358980672, 0.8906043030093336, 0.9131986273591366, 0.868448135993582, 0.9409452514090343, 0.8864296501322184, 0.9480458483443018, 0.9352541340795765, 0.8980143404684522, 0.8797772874779678, 1.0272546670138865, 0.9529662160361352, 0.9385664483466383, 1.0110021930099442, 0.9640628095913902, 1.000293679050762, 0.9875627624520966, 1.0024834186378888, 0.9537336440040795, 0.9109206399857278, 0.9636822824653468, 0.9604477583006557, 0.9852529688078752, 0.9655587238978297, 1.0210757092830614, 1.0019194797283157, 0.9762643742240896, 1.0011103633557972, 0.9123124718032518, 1.0538323915688874, 0.9835584523967434],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04277974771580195, 0.0374884222790578, 0.038860049193244595, 0.03977404307520238, 0.04227222712296719, 0.04624958113537936, 0.04819098492927065, 0.047780318343561334, 0.04870063929474289, 0.047349565779214786, 0.05232178563835199, 0.05181336851847118, 0.05014403916299093, 0.05119776062756043, 0.05105054072527926, 0.0508730187258819, 0.05146568564596077, 0.052728065722418616, 0.04909974136125972, 0.05237889976879151, 0.05258982974461934, 0.05450650970866899, 0.04686419696459876, 0.0481529576044889, 0.04897700340503319, 0.04949705249390157, 0.04396121904470596, 0.04349540329636614, 0.04616342701036358, 0.04463560479408124, 0.042183027709545184, 0.04343771115543482, 0.04372132639766124, 0.0428840151196751, 0.04074084949896195, 0.04076215408826123, 0.03855997072276196, 0.03683368237770168, 0.040263677905201356, 0.03709641855086199, 0.0354726509228076, 0.034711818868811584, 0.03418181519469132],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04277974771580206, 0.03748842227905791, 0.038860049193244706, 0.03977404307520227, 0.04227222712296719, 0.04624958113537936, 0.048190984929270764, 0.04778031834356122, 0.04870063929474311, 0.0473495657792149, 0.05232178563835199, 0.05181336851847118, 0.05014403916299082, 0.05119776062756043, 0.05105054072527926, 0.0508730187258819, 0.05146568564596077, 0.05272806572241873, 0.04909974136125972, 0.05237889976879151, 0.052589829744619454, 0.05450650970866899, 0.04686419696459865, 0.04815295760448901, 0.04897700340503319, 0.04949705249390157, 0.04396121904470607, 0.04349540329636614, 0.04616342701036347, 0.04463560479408124, 0.042183027709545184, 0.04343771115543493, 0.04372132639766124, 0.04288401511967521, 0.04074084949896184, 0.04076215408826123, 0.03855997072276196, 0.03683368237770157, 0.040263677905201245, 0.03709641855086199, 0.0354726509228076, 0.034711818868811584, 0.03418181519469132],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1845948739809059, 0.04828398620532892, 0.03178061963214229, 0.031476440087157886, 0.053149027974688456, 0.037495309257962184, 0.03641946190961631, 0.0338588958775875, 0.04568789283287733, 0.03638920149820313, 0.04639802512658375, 0.03153492592742302, 0.02746079990273198, 0.031441463972059824, 0.02980896855379922, 0.027246540672316244, 0.03222401559909516, 0.02315814487548118, 0.030081216322611293, 0.023023903008855484, 0.021442144667169427, 0.021840668032392374, 0.02274975928868761, 0.022301004297606952, 0.021585213767065903, 0.02128453639248784, 0.019625002905220512, 0.01973555789773984, 0.01960306474170559, 0.018908971429494104, 0.0181904798268806, 0.0168738257333515, 0.016643934742540445, 0.016181366024389576, 0.016275055001268135, 0.015698987843341006, 0.015603366030883858, 0.014971969459217194, 0.014261331349749717, 0.014367672499475459, 0.01254186295957782, 0.014290656355778975, 0.01271368788763183],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1845948739809059, 0.04828398620532892, 0.031780619632142404, 0.031476440087157886, 0.053149027974688456, 0.037495309257962184, 0.0364194619096162, 0.033858895877587614, 0.04568789283287722, 0.03638920149820313, 0.04639802512658364, 0.03153492592742313, 0.02746079990273198, 0.031441463972059935, 0.02980896855379933, 0.027246540672316244, 0.032224015599095046, 0.02315814487548118, 0.030081216322611404, 0.023023903008855595, 0.021442144667169316, 0.021840668032392485, 0.022749759288687832, 0.022301004297606952, 0.021585213767065903, 0.02128453639248784, 0.019625002905220623, 0.01973555789773962, 0.01960306474170581, 0.018908971429494104, 0.0181904798268806, 0.01687382573335161, 0.016643934742540445, 0.016181366024389465, 0.016275055001268246, 0.015698987843341006, 0.015603366030883858, 0.014971969459217416, 0.014261331349749606, 0.014367672499475459, 0.012541862959577932, 0.014290656355778975, 0.01271368788763172],
  ],
}
ratio0_variation_vals = {
}