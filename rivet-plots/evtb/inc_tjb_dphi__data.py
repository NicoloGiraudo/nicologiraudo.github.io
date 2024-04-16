
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
  'curve0' : [0.00909519375, 0.009472325, 0.009966043750000002, 0.010996543749999997, 0.012222212499999998, 0.013435587500000007, 0.015576681249999986, 0.01852916875000001, 0.02097385625000001, 0.02504038124999998, 0.030826968750000013, 0.037980931250000016, 0.04984525624999995, 0.06710674999999994, 0.09619800000000017, 0.14795662499999987, 0.24991118749999977, 0.49074756250000096, 1.3322993749999987, 7.580562499999993],
  'curve1' : [0.011706993749999998, 0.0117851, 0.012619793750000002, 0.012718699999999996, 0.013868706249999996, 0.014592643750000009, 0.016218424999999988, 0.01850703125000001, 0.021211875000000012, 0.02511843749999998, 0.031193981250000016, 0.03780046875000002, 0.04949158124999995, 0.06732624999999993, 0.09735350000000018, 0.14676937499999987, 0.2486489999999998, 0.49045162500000095, 1.3310431249999988, 7.579343749999993],
}
yedges = {
  'curve0' : [0.00909519375, 0.00909519375, 0.009472325, 0.009966043750000002, 0.010996543749999997, 0.012222212499999998, 0.013435587500000007, 0.015576681249999986, 0.01852916875000001, 0.02097385625000001, 0.02504038124999998, 0.030826968750000013, 0.037980931250000016, 0.04984525624999995, 0.06710674999999994, 0.09619800000000017, 0.14795662499999987, 0.24991118749999977, 0.49074756250000096, 1.3322993749999987, 7.580562499999993],
  'curve1' : [0.011706993749999998, 0.011706993749999998, 0.0117851, 0.012619793750000002, 0.012718699999999996, 0.013868706249999996, 0.014592643750000009, 0.016218424999999988, 0.01850703125000001, 0.021211875000000012, 0.02511843749999998, 0.031193981250000016, 0.03780046875000002, 0.04949158124999995, 0.06732624999999993, 0.09735350000000018, 0.14676937499999987, 0.2486489999999998, 0.49045162500000095, 1.3310431249999988, 7.579343749999993],
}
yups = {
  'curve0' : [0.00019003690019967176, 0.0002740853396982407, 0.00022008547700268645, 0.0003418008374770313, 0.00029715953469895587, 0.00023881838025997926, 0.00028791172963687996, 0.00034221971880284764, 0.00028679798802903075, 0.0003043601125722617, 0.00037990526162781706, 0.0003620396322400355, 0.00044795799712417193, 0.000542713523647605, 0.0006757397566741221, 0.0008087775304433222, 0.0010274165492267478, 0.0013592574661832862, 0.0023842500786410785, 0.004024225468956725],
  'curve1' : [0.00021856331319551319, 0.0002454161803192691, 0.00043127531628589646, 0.00018858169234445846, 0.00026887765863399657, 0.00019467785891056033, 0.00022436002735558736, 0.00022098014970241118, 0.00023266820192604758, 0.0002719572433076565, 0.00039750054048705416, 0.00035461009617959293, 0.0004447845335103275, 0.0005440415884838212, 0.0016185311145449166, 0.0009508135907605646, 0.0015242915875087666, 0.002939538521392437, 0.0047052455767472925, 0.006737340559337929],
}
ydowns = {
  'curve0' : [0.00019003690019967176, 0.0002740853396982407, 0.00022008547700268645, 0.0003418008374770313, 0.00029715953469895587, 0.00023881838025997926, 0.00028791172963687996, 0.00034221971880284764, 0.00028679798802903075, 0.0003043601125722617, 0.00037990526162781706, 0.0003620396322400355, 0.00044795799712417193, 0.000542713523647605, 0.0006757397566741221, 0.0008087775304433222, 0.0010274165492267478, 0.0013592574661832862, 0.0023842500786410785, 0.004024225468956725],
  'curve1' : [0.00021856331319551319, 0.0002454161803192691, 0.00043127531628589646, 0.00018858169234445846, 0.00026887765863399657, 0.00019467785891056033, 0.00022436002735558736, 0.00022098014970241118, 0.00023266820192604758, 0.0002719572433076565, 0.00039750054048705416, 0.00035461009617959293, 0.0004447845335103275, 0.0005440415884838212, 0.0016185311145449166, 0.0009508135907605646, 0.0015242915875087666, 0.002939538521392437, 0.0047052455767472925, 0.006737340559337929],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.2871626566503873, 1.2871626566503873, 1.244161280361474, 1.2662791842550358, 1.1566088663085616, 1.1347132321582527, 1.0861187685317073, 1.0411990037993493, 0.9988052621086956, 1.011348354215978, 1.0031172149186027, 1.0119055656420972, 0.9952486025471006, 0.992904540439593, 1.0032709079190991, 1.0120116842345994, 0.9919756888209635, 0.9949494557941709, 0.9993969659299122, 0.9990570812960113, 0.9998392269702941],
}
ratio0_ymax = {
  'curve0' : [1.0208942113189916, 1.0289353817249978, 1.0220835351041566, 1.0310825696916845, 1.0243130721789493, 1.0177750604698141, 1.018483509100302, 1.0184692429228832, 1.0136740704527825, 1.0121547715082118, 1.012323795593033, 1.0095321420598404, 1.0089869735021009, 1.0080873164569528, 1.0070244678337816, 1.0054663150801346, 1.004111126674658, 1.0027697691645352, 1.0017895753187163, 1.0005308610632728],
  'curve1' : [1.3111932951615806, 1.2700700388045456, 1.3095536597745616, 1.1737580448715494, 1.1567123308184992, 1.1006084854056855, 1.0556025871913883, 1.010731331361123, 1.0224416028371535, 1.013977961829461, 1.0248001367467263, 1.00458513234005, 1.001827847630141, 1.0113780147076683, 1.0288366817869905, 0.998401988358146, 1.0010487889323034, 1.005386885689101, 1.002588754180529, 1.000727992224764],
}
ratio0_ymin = {
  'curve0' : [0.9791057886810085, 0.9710646182750021, 0.9779164648958434, 0.9689174303083156, 0.9756869278210508, 0.9822249395301859, 0.9815164908996978, 0.9815307570771167, 0.9863259295472175, 0.9878452284917882, 0.987676204406967, 0.9904678579401596, 0.9910130264978992, 0.9919126835430473, 0.9929755321662185, 0.9945336849198655, 0.9958888733253418, 0.9972302308354649, 0.9982104246812837, 0.9994691389367271],
  'curve1' : [1.2631320181391943, 1.2182525219184024, 1.2230047087355103, 1.1394596877455738, 1.1127141334980064, 1.0716290516577291, 1.0267954204073102, 0.9868791928562682, 1.0002551055948024, 0.9922564680077443, 0.9990109945374681, 0.985912072754151, 0.9839812332490451, 0.9951638011305296, 0.9951866866822084, 0.9855493892837811, 0.9888501226560386, 0.9934070461707236, 0.9955254084114936, 0.9989504617158241],
}
ratio0_yerrs = {
  'curve0' : [
    [0.020894211318991496, 0.028935381724997877, 0.022083535104156615, 0.031082569691684436, 0.02431307217894918, 0.01777506046981414, 0.018483509100302165, 0.018469242922883322, 0.01367407045278246, 0.012154771508211759, 0.012323795593032982, 0.009532142059840432, 0.008986973502100759, 0.008087316456952709, 0.0070244678337815225, 0.0054663150801345095, 0.004111126674658183, 0.0027697691645350853, 0.0017895753187162633, 0.000530861063272936],
    [0.020894211318991607, 0.028935381724997766, 0.022083535104156615, 0.031082569691684547, 0.02431307217894929, 0.01777506046981414, 0.018483509100301942, 0.01846924292288321, 0.01367407045278246, 0.012154771508211759, 0.012323795593033093, 0.009532142059840432, 0.00898697350210087, 0.00808731645695282, 0.0070244678337816335, 0.0054663150801346205, 0.004111126674658072, 0.0027697691645351963, 0.0017895753187162633, 0.000530861063272825],
  ],
  'curve1' : [
    [0.024030638511193025, 0.025908758443071722, 0.04327447551952557, 0.01714917856298781, 0.021999098660246297, 0.014489716873978153, 0.014403583392039065, 0.01192606925242734, 0.011093248621175666, 0.010860746910858476, 0.012894571104629104, 0.009336529792949522, 0.008923307190547902, 0.008107106788569518, 0.016824997552390974, 0.006426299537182434, 0.006099333138132379, 0.005989919759188611, 0.0035316728845177225, 0.0008887652544700142],
    [0.024030638511193247, 0.0259087584430715, 0.04327447551952579, 0.01714917856298781, 0.02199909866024652, 0.014489716873978153, 0.014403583392039065, 0.011926069252427451, 0.011093248621175444, 0.010860746910858365, 0.012894571104629104, 0.009336529792949522, 0.008923307190548013, 0.008107106788569185, 0.016824997552391086, 0.006426299537182434, 0.00609933313813249, 0.005989919759188833, 0.0035316728845176115, 0.0008887652544699032],
  ],
}
ratio0_variation_vals = {
}