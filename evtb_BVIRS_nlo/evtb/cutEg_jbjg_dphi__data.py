
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
  'curve0' : [1.788218125, 1.945315, 2.053128125, 1.8742256249999996, 1.7669781249999996, 1.867450625000001, 1.9275031249999983, 1.6493712500000008, 1.665072500000001, 1.5596356249999987, 1.6546637500000008, 1.580093750000001, 1.4724993749999986, 1.6848612499999984, 1.505547500000003, 1.6522331249999986, 1.7866099999999983, 1.5849962500000028, 1.6059287499999988, 0.8645724999999992],
  'curve1' : [1.325596875, 1.40922625, 1.5297268750000004, 1.3406968749999997, 1.2894437499999998, 1.2255693750000005, 1.192196874999999, 1.0480775000000004, 1.1599943750000006, 1.0527918749999992, 1.0290750000000004, 1.0474781250000005, 1.081666874999999, 1.1126181249999991, 1.056881250000002, 1.0884693749999992, 1.094932499999999, 1.020431250000002, 1.200772499999999, 0.6141491249999994],
}
yedges = {
  'curve0' : [1.788218125, 1.788218125, 1.945315, 2.053128125, 1.8742256249999996, 1.7669781249999996, 1.867450625000001, 1.9275031249999983, 1.6493712500000008, 1.665072500000001, 1.5596356249999987, 1.6546637500000008, 1.580093750000001, 1.4724993749999986, 1.6848612499999984, 1.505547500000003, 1.6522331249999986, 1.7866099999999983, 1.5849962500000028, 1.6059287499999988, 0.8645724999999992],
  'curve1' : [1.325596875, 1.325596875, 1.40922625, 1.5297268750000004, 1.3406968749999997, 1.2894437499999998, 1.2255693750000005, 1.192196874999999, 1.0480775000000004, 1.1599943750000006, 1.0527918749999992, 1.0290750000000004, 1.0474781250000005, 1.081666874999999, 1.1126181249999991, 1.056881250000002, 1.0884693749999992, 1.094932499999999, 1.020431250000002, 1.200772499999999, 0.6141491249999994],
}
yups = {
  'curve0' : [0.09864428677069949, 0.18006392094198104, 0.17671402789889096, 0.12441175650335458, 0.18877127363558255, 0.22003275679430107, 0.2692112321208011, 0.16115428360735568, 0.22425336187558048, 0.18650643001650088, 0.18571014461385796, 0.20412255050581754, 0.1372105333738994, 0.19293730766106365, 0.14481297205361154, 0.2057309757304425, 0.2674631984030698, 0.1755133096804915, 0.20128212088384784, 0.10477281971007546],
  'curve1' : [0.05287003153370537, 0.08112695009212413, 0.08589608092776993, 0.052513141956323645, 0.08726801837586319, 0.08190834244751878, 0.09397616469749116, 0.0670741194500532, 0.09951193395769177, 0.0706631534110953, 0.07055153812107859, 0.07087739744622402, 0.07799431569832502, 0.09335897620207703, 0.10365679171549753, 0.0769138875220203, 0.08752579976783981, 0.06960067461059569, 0.1397002371150456, 0.0532765632102897],
}
ydowns = {
  'curve0' : [0.09864428677069949, 0.18006392094198104, 0.17671402789889096, 0.12441175650335458, 0.18877127363558255, 0.22003275679430107, 0.2692112321208011, 0.16115428360735568, 0.22425336187558048, 0.18650643001650088, 0.18571014461385796, 0.20412255050581754, 0.1372105333738994, 0.19293730766106365, 0.14481297205361154, 0.2057309757304425, 0.2674631984030698, 0.1755133096804915, 0.20128212088384784, 0.10477281971007546],
  'curve1' : [0.05287003153370537, 0.08112695009212413, 0.08589608092776993, 0.052513141956323645, 0.08726801837586319, 0.08190834244751878, 0.09397616469749116, 0.0670741194500532, 0.09951193395769177, 0.0706631534110953, 0.07055153812107859, 0.07087739744622402, 0.07799431569832502, 0.09335897620207703, 0.10365679171549753, 0.0769138875220203, 0.08752579976783981, 0.06960067461059569, 0.1397002371150456, 0.0532765632102897],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.7412948434352772, 0.7412948434352772, 0.7244205951221268, 0.7450713164820146, 0.7153337661787652, 0.7297451687467835, 0.6562793996226808, 0.6185187767205306, 0.6354406262386348, 0.6966629831433765, 0.6750242544632821, 0.6219239407402258, 0.6629215038664635, 0.7345788347108806, 0.6603618695604758, 0.7019913021674838, 0.6587868010454033, 0.6128547920363147, 0.6438067282493571, 0.7477121883520672, 0.7103500573983096],
}
ratio0_ymax = {
  'curve0' : [1.0551634531557494, 1.0925628604837678, 1.0860706283972856, 1.0663803518871187, 1.1068328299964567, 1.1178252071828143, 1.1396683764758107, 1.097706494888495, 1.1346808393481846, 1.1195833353809812, 1.1122343706471227, 1.1291838224825694, 1.0931820656113347, 1.1145122826351808, 1.0961862525450783, 1.124516917508504, 1.1497042994291256, 1.11073421131469, 1.1253368936099113, 1.1211845388444295],
  'curve1' : [0.7708606054609279, 0.7661243552289084, 0.7869080045492876, 0.743352346895974, 0.7791334532655084, 0.7001404481296627, 0.6672741657409719, 0.676107104116222, 0.7564273080948076, 0.7203317303111073, 0.6645619317647338, 0.707777954596823, 0.7875461344072386, 0.7157723528878578, 0.7708412001052756, 0.7053382751432371, 0.6618446665852312, 0.6877189296886953, 0.834702496679909, 0.7719719146864951],
}
ratio0_ymin = {
  'curve0' : [0.9448365468442506, 0.9074371395162321, 0.9139293716027143, 0.9336196481128815, 0.8931671700035434, 0.8821747928171858, 0.8603316235241895, 0.9022935051115051, 0.8653191606518152, 0.8804166646190189, 0.8877656293528773, 0.8708161775174306, 0.9068179343886652, 0.8854877173648193, 0.9038137474549217, 0.8754830824914961, 0.8502957005708744, 0.88926578868531, 0.8746631063900886, 0.8788154611555704],
  'curve1' : [0.7117290814096264, 0.682716835015345, 0.7032346284147416, 0.6873151854615563, 0.6803568842280585, 0.6124183511156988, 0.5697633877000893, 0.5947741483610477, 0.6368986581919455, 0.6297167786154568, 0.579285949715718, 0.618065053136104, 0.6816115350145224, 0.6049513862330937, 0.6331414042296922, 0.6122353269475697, 0.563864917487398, 0.599894526810019, 0.6607218800242254, 0.648728200110124],
}
ratio0_yerrs = {
  'curve0' : [
    [0.05516345315574944, 0.09256286048376794, 0.08607062839728574, 0.06638035188711855, 0.1068328299964566, 0.1178252071828142, 0.13966837647581054, 0.09770649488849492, 0.13468083934818476, 0.11958333538098109, 0.11223437064712272, 0.12918382248256943, 0.0931820656113348, 0.11451228263518065, 0.09618625254507829, 0.12451691750850391, 0.14970429942912555, 0.11073421131468997, 0.1253368936099114, 0.12118453884442959],
    [0.05516345315574944, 0.09256286048376783, 0.08607062839728563, 0.06638035188711866, 0.10683282999645671, 0.1178252071828143, 0.13966837647581065, 0.09770649488849492, 0.13468083934818464, 0.1195833353809812, 0.11223437064712272, 0.12918382248256943, 0.09318206561133469, 0.11451228263518076, 0.09618625254507829, 0.12451691750850391, 0.14970429942912555, 0.11073421131469008, 0.1253368936099113, 0.12118453884442948],
  ],
  'curve1' : [
    [0.029565762025650755, 0.041703760106781784, 0.04183668806727303, 0.028018580717208863, 0.04938828451872501, 0.043861048506982026, 0.0487553890204413, 0.04066647787758715, 0.059764324951431025, 0.04530747584782524, 0.042637991024507826, 0.04485645073035949, 0.05296729969635816, 0.055410483327382076, 0.06884989793779162, 0.04655147409783367, 0.04898987454891668, 0.04391220143933816, 0.08699030832784183, 0.06162185728818559],
    [0.029565762025650755, 0.04170376010678167, 0.04183668806727292, 0.028018580717208752, 0.0493882845187249, 0.043861048506981914, 0.0487553890204413, 0.04066647787758715, 0.059764324951431136, 0.04530747584782524, 0.04263799102450794, 0.04485645073035949, 0.05296729969635805, 0.055410483327381965, 0.06884989793779173, 0.04655147409783378, 0.04898987454891657, 0.04391220143933816, 0.08699030832784183, 0.06162185728818548],
  ],
}
ratio0_variation_vals = {
}