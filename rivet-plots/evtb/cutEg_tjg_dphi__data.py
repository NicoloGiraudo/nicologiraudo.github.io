
from numpy import nan

xpoints  = [0.08, 0.24, 0.4, 0.56, 0.72, 0.88, 1.04, 1.2000000000000002, 1.3599999999999999, 1.52, 1.6800000000000002, 1.8399999999999999, 2.0, 2.16, 2.3200000000000003, 2.48, 2.64, 2.8, 2.96, 3.12]
xedges   = [0.0, 0.16, 0.32, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92, 2.08, 2.24, 2.4, 2.56, 2.72, 2.88, 3.04, 3.2]
xmins    = [0.0, 0.16, 0.32, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92, 2.08, 2.24, 2.4, 2.56, 2.72, 2.88, 3.04]
xmaxs    = [0.16, 0.32, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92, 2.08, 2.24, 2.4, 2.56, 2.72, 2.88, 3.04, 3.2]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.1643615, 0.1751835, 0.18541693750000002, 0.19762418749999996, 0.20344549999999997, 0.2084903750000001, 0.21205993749999982, 0.2162298750000001, 0.22486168750000013, 0.23626924999999982, 0.2504474375000001, 0.27507443750000016, 0.30461787499999976, 0.3510356874999997, 0.4182695000000008, 0.5231593124999995, 0.7055231249999994, 0.8228356250000016, 0.6601612499999995, 0.3866207499999997],
  'curve1' : [0.1637974375, 0.17552399999999999, 0.1879359375, 0.19587574999999996, 0.20382112499999996, 0.2065411250000001, 0.2126323749999998, 0.2194920000000001, 0.2252633125000001, 0.2361418124999998, 0.25148781250000013, 0.27258031250000014, 0.3000793749999997, 0.3483504999999997, 0.41758343750000076, 0.5228051249999995, 0.7088818749999993, 0.8200356250000016, 0.6578081249999994, 0.38901593749999963],
}
yedges = {
  'curve0' : [0.1643615, 0.1643615, 0.1751835, 0.18541693750000002, 0.19762418749999996, 0.20344549999999997, 0.2084903750000001, 0.21205993749999982, 0.2162298750000001, 0.22486168750000013, 0.23626924999999982, 0.2504474375000001, 0.27507443750000016, 0.30461787499999976, 0.3510356874999997, 0.4182695000000008, 0.5231593124999995, 0.7055231249999994, 0.8228356250000016, 0.6601612499999995, 0.3866207499999997],
  'curve1' : [0.1637974375, 0.1637974375, 0.17552399999999999, 0.1879359375, 0.19587574999999996, 0.20382112499999996, 0.2065411250000001, 0.2126323749999998, 0.2194920000000001, 0.2252633125000001, 0.2361418124999998, 0.25148781250000013, 0.27258031250000014, 0.3000793749999997, 0.3483504999999997, 0.41758343750000076, 0.5228051249999995, 0.7088818749999993, 0.8200356250000016, 0.6578081249999994, 0.38901593749999963],
}
yups = {
  'curve0' : [0.0008763739213372338, 0.0012930390558679966, 0.0013342050535805959, 0.0013942560740409198, 0.001407383709671957, 0.0014166041040107155, 0.00140969910353238, 0.001391987675053196, 0.0014317263126641913, 0.0014438901447132314, 0.0014993581960292218, 0.0015878622864168677, 0.0017154470536131377, 0.0019005622112285602, 0.0022198500793972594, 0.0026140590443790644, 0.0033628879887679843, 0.003754061862669561, 0.003195205147952159, 0.002417606318758286],
  'curve1' : [0.0007784266483587262, 0.002092602297379987, 0.0012171165335537926, 0.0011094049291737438, 0.0016155252628789185, 0.0011689249534829007, 0.00129062394067753, 0.0018234223703314058, 0.001446186121104404, 0.0018367958897561247, 0.0015589845453050529, 0.0019282795724103402, 0.0020551032136488893, 0.003191405695379386, 0.0037618578147971056, 0.006405978652789902, 0.00803562137843116, 0.00938933279378787, 0.007980745872880547, 0.006092289247996186],
}
ydowns = {
  'curve0' : [0.0008763739213372338, 0.0012930390558679966, 0.0013342050535805959, 0.0013942560740409198, 0.001407383709671957, 0.0014166041040107155, 0.00140969910353238, 0.001391987675053196, 0.0014317263126641913, 0.0014438901447132314, 0.0014993581960292218, 0.0015878622864168677, 0.0017154470536131377, 0.0019005622112285602, 0.0022198500793972594, 0.0026140590443790644, 0.0033628879887679843, 0.003754061862669561, 0.003195205147952159, 0.002417606318758286],
  'curve1' : [0.0007784266483587262, 0.002092602297379987, 0.0012171165335537926, 0.0011094049291737438, 0.0016155252628789185, 0.0011689249534829007, 0.00129062394067753, 0.0018234223703314058, 0.001446186121104404, 0.0018367958897561247, 0.0015589845453050529, 0.0019282795724103402, 0.0020551032136488893, 0.003191405695379386, 0.0037618578147971056, 0.006405978652789902, 0.00803562137843116, 0.00938933279378787, 0.007980745872880547, 0.006092289247996186],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.996568159210034, 0.996568159210034, 1.0019436762023821, 1.0135855981333959, 0.9911527150491131, 1.0018463175641634, 0.990650647541883, 1.0026994136976013, 1.0150863750903987, 1.0017860979541033, 0.9994606259595779, 1.004154065261698, 0.9909329088421748, 0.9851010056451872, 0.9923506708986675, 0.9983597596764765, 0.9993229834745607, 1.0047606518921686, 0.9965971332366655, 0.9964355299557494, 1.0061951861093847],
}
ratio0_ymax = {
  'curve0' : [1.0053319902856646, 1.0073810550415307, 1.0071957021379483, 1.007055088203922, 1.0069177431286116, 1.0067945779463954, 1.006647644624211, 1.0064375363258808, 1.006367142080014, 1.0061112063660982, 1.005986718055477, 1.0057724821719098, 1.0056314720651673, 1.005414156676673, 1.0053072243598857, 1.0049966787973006, 1.0047665170277273, 1.0045623472642784, 1.0048400374119992, 1.0062531726989776],
  'curve1' : [1.0013042236068588, 1.0138888782184394, 1.0201498125464066, 0.9967664253100281, 1.0097871433031398, 0.9962572610533359, 1.0087855417795617, 1.0235191708376625, 1.0082175453793316, 1.0072347899261378, 1.0103788626118608, 0.9979429370728434, 0.9918475014430747, 1.001442070460085, 1.0073536208468394, 1.011567778701808, 1.0161502450801043, 1.0080080791273323, 1.0085246155736656, 1.0219529778161058],
}
ratio0_ymin = {
  'curve0' : [0.9946680097143356, 0.9926189449584693, 0.9928042978620516, 0.992944911796078, 0.9930822568713884, 0.9932054220536046, 0.993352355375789, 0.993562463674119, 0.993632857919986, 0.9938887936339018, 0.9940132819445229, 0.9942275178280902, 0.9943685279348327, 0.9945858433233271, 0.9946927756401143, 0.9950033212026995, 0.9952334829722727, 0.9954376527357216, 0.9951599625880009, 0.9937468273010224],
  'curve1' : [0.9918320948132092, 0.9899984741863247, 1.0070213837203852, 0.985539004788198, 0.993905491825187, 0.9850440340304301, 0.9966132856156408, 1.0066535793431348, 0.9953546505288748, 0.9916864619930179, 0.9979292679115352, 0.983922880611506, 0.9783545098472999, 0.9832592713372499, 0.9893658985061136, 0.9870781882473135, 0.9933710587042328, 0.9851861873459989, 0.9843464443378331, 0.990437394402664],
}
ratio0_yerrs = {
  'curve0' : [
    [0.005331990285664445, 0.0073810550415307485, 0.007195702137948401, 0.0070550882039219776, 0.006917743128611598, 0.006794577946395375, 0.006647644624210969, 0.006437536325880955, 0.006367142080013988, 0.0061112063660981875, 0.005986718055477125, 0.005772482171909843, 0.005631472065167342, 0.005414156676672888, 0.005307224359885732, 0.00499667879730048, 0.004766517027727346, 0.004562347264278399, 0.004840037411999121, 0.006253172698977627],
    [0.005331990285664556, 0.0073810550415307485, 0.00719570213794829, 0.0070550882039219776, 0.006917743128611598, 0.006794577946395375, 0.006647644624210969, 0.006437536325880844, 0.006367142080013988, 0.0061112063660981875, 0.005986718055476903, 0.005772482171909843, 0.005631472065167342, 0.005414156676672999, 0.005307224359885732, 0.004996678797300591, 0.004766517027727346, 0.004562347264278399, 0.004840037411999232, 0.006253172698977627],
  ],
  'curve1' : [
    [0.004736064396824835, 0.011945202016057421, 0.006564214413010694, 0.005613710260915061, 0.007940825738976476, 0.005606613511452974, 0.006086128081960518, 0.008432795747263855, 0.006431447425228498, 0.007774163966559944, 0.006224797350162792, 0.007010028230668763, 0.006746495797887331, 0.009091399561417579, 0.008993861170362938, 0.012244795227247196, 0.011389593187935754, 0.011410945890666602, 0.012089085617916218, 0.01575779170672076],
    [0.004736064396824724, 0.01194520201605731, 0.006564214413010694, 0.005613710260915061, 0.007940825738976365, 0.005606613511452863, 0.006086128081960407, 0.008432795747263855, 0.006431447425228276, 0.007774163966559944, 0.006224797350162792, 0.007010028230668652, 0.006746495797887442, 0.009091399561417579, 0.008993861170362938, 0.012244795227247307, 0.011389593187935754, 0.011410945890666713, 0.012089085617916218, 0.01575779170672109],
  ],
}
ratio0_variation_vals = {
}