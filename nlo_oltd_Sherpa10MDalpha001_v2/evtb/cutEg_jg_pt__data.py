
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
  'curve0' : [61.42724285714285, 3.406564285714285, 1.9746842857142861, 1.3776648571428565, 1.0561132857142865, 0.8326939999999999, 0.6885951428571429, 0.5858138571428566, 0.5064727142857146, 0.440974285714286, 0.39459314285714253, 0.35029828571428595, 0.3148418571428569, 0.2830812857142859, 0.25778342857142833, 0.2349855714285712, 0.21498700000000048, 0.19769814285714268, 0.1818541428571427, 0.16796671428571466, 0.15503242857142843, 0.14213711428571416, 0.13149089999999988, 0.12254472857142884, 0.11338781428571419, 0.10600617142857134, 0.09854338571428595, 0.09105528571428563, 0.08301075714285733, 0.07836995714285683, 0.07192447142857158, 0.0657034285714283, 0.060591185714285845, 0.055593871428571556, 0.05026328571428551, 0.04534712857142867, 0.040485400000000095, 0.036366199999999856, 0.031094057142857214, 0.02713044285714292, 0.02184229999999991, 0.01598471428571432, 0.007249802857142874, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [61.42724285714285, 61.42724285714285, 3.406564285714285, 1.9746842857142861, 1.3776648571428565, 1.0561132857142865, 0.8326939999999999, 0.6885951428571429, 0.5858138571428566, 0.5064727142857146, 0.440974285714286, 0.39459314285714253, 0.35029828571428595, 0.3148418571428569, 0.2830812857142859, 0.25778342857142833, 0.2349855714285712, 0.21498700000000048, 0.19769814285714268, 0.1818541428571427, 0.16796671428571466, 0.15503242857142843, 0.14213711428571416, 0.13149089999999988, 0.12254472857142884, 0.11338781428571419, 0.10600617142857134, 0.09854338571428595, 0.09105528571428563, 0.08301075714285733, 0.07836995714285683, 0.07192447142857158, 0.0657034285714283, 0.060591185714285845, 0.055593871428571556, 0.05026328571428551, 0.04534712857142867, 0.040485400000000095, 0.036366199999999856, 0.031094057142857214, 0.02713044285714292, 0.02184229999999991, 0.01598471428571432, 0.007249802857142874, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [1.1237291234355111, 0.02421274331370797, 0.01414943786292356, 0.01134035686729262, 0.008025966786446535, 0.0061665357588605715, 0.005165985691353132, 0.004485169439158252, 0.0037034710690356, 0.0031334264351488787, 0.002779961459136745, 0.00239195206763797, 0.002221323378308615, 0.00194268801784895, 0.001789022079237703, 0.001551954002053473, 0.0014419721472585375, 0.0013121889330116926, 0.0012237950341925249, 0.001123537779897565, 0.0010026715334952075, 0.0009204822382970823, 0.0008753798009540579, 0.0008127784295305869, 0.000717814284434891, 0.0006982035256752184, 0.0006686710853687075, 0.0006251829120100669, 0.0005702328561246565, 0.000566235510243946, 0.000528076215896834, 0.0004956840254246878, 0.00047136319893063713, 0.0004459413112296565, 0.00042527606879987507, 0.0004009614211174069, 0.0003782082894439019, 0.00035892847903339103, 0.0003304388238789914, 0.0003107854434119062, 0.0002781179459091665, 0.000236715449604864, 0.00015912772433822255, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [1.1237291234355111, 0.02421274331370797, 0.01414943786292356, 0.01134035686729262, 0.008025966786446535, 0.0061665357588605715, 0.005165985691353132, 0.004485169439158252, 0.0037034710690356, 0.0031334264351488787, 0.002779961459136745, 0.00239195206763797, 0.002221323378308615, 0.00194268801784895, 0.001789022079237703, 0.001551954002053473, 0.0014419721472585375, 0.0013121889330116926, 0.0012237950341925249, 0.001123537779897565, 0.0010026715334952075, 0.0009204822382970823, 0.0008753798009540579, 0.0008127784295305869, 0.000717814284434891, 0.0006982035256752184, 0.0006686710853687075, 0.0006251829120100669, 0.0005702328561246565, 0.000566235510243946, 0.000528076215896834, 0.0004956840254246878, 0.00047136319893063713, 0.0004459413112296565, 0.00042527606879987507, 0.0004009614211174069, 0.0003782082894439019, 0.00035892847903339103, 0.0003304388238789914, 0.0003107854434119062, 0.0002781179459091665, 0.000236715449604864, 0.00015912772433822255, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0182936604536994, 1.007107672506063, 1.0071654177659117, 1.0082315788259355, 1.007599532071996, 1.0074055244289746, 1.0075022104714801, 1.0076563047877245, 1.0073122815199602, 1.0071056896890787, 1.0070451337268758, 1.006828329355825, 1.0070553623284617, 1.0068626508211134, 1.0069400197256744, 1.0066044650853179, 1.0067072527513687, 1.0066373356575224, 1.0067295416808508, 1.0066890501768488, 1.0064674954958424, 1.0064760160843478, 1.0066573413137645, 1.0066325042211575, 1.0063306122351574, 1.0065864422445034, 1.006785550146485, 1.0068659705705802, 1.0068693850743142, 1.0072251603916509, 1.007342093802125, 1.0075442642218557, 1.007779402125473, 1.0080214113493178, 1.0084609683341694, 1.0088420465363277, 1.0093418439596473, 1.0098698373498851, 1.0106270732815867, 1.0114552292805674, 1.0127329972534562, 1.0148088633536867, 1.021949248479418, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [0.9817063395463005, 0.992892327493937, 0.9928345822340884, 0.9917684211740646, 0.9924004679280042, 0.9925944755710253, 0.99249778952852, 0.9923436952122755, 0.9926877184800397, 0.9928943103109212, 0.9929548662731243, 0.9931716706441751, 0.9929446376715384, 0.9931373491788866, 0.9930599802743255, 0.9933955349146821, 0.9932927472486313, 0.9933626643424776, 0.9932704583191492, 0.9933109498231512, 0.9935325045041578, 0.9935239839156521, 0.9933426586862356, 0.9933674957788425, 0.9936693877648427, 0.9934135577554966, 0.9932144498535149, 0.9931340294294196, 0.9931306149256859, 0.9927748396083491, 0.992657906197875, 0.9924557357781442, 0.9922205978745271, 0.9919785886506822, 0.9915390316658306, 0.9911579534636723, 0.9906581560403528, 0.9901301626501149, 0.9893729267184131, 0.9885447707194326, 0.9872670027465438, 0.9851911366463134, 0.9780507515205822, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.018293660453699512, 0.007107672506063034, 0.007165417765911619, 0.008231578825935393, 0.007599532071995818, 0.007405524428974686, 0.007502210471480031, 0.007656304787724499, 0.007312281519960329, 0.007105689689078765, 0.007045133726875652, 0.006828329355824891, 0.007055362328461601, 0.00686265082111337, 0.0069400197256744844, 0.006604465085317868, 0.006707252751368742, 0.006637335657522447, 0.006729541680850826, 0.006689050176848843, 0.006467495495842246, 0.006476016084347891, 0.006657341313764387, 0.006632504221157465, 0.006330612235157296, 0.006586442244503443, 0.006785550146485075, 0.00686597057058036, 0.006869385074314116, 0.007225160391650887, 0.007342093802125027, 0.007544264221855834, 0.007779402125472901, 0.008021411349317775, 0.008460968334169428, 0.008842046536327697, 0.009341843959647211, 0.009869837349885113, 0.010627073281586852, 0.011455229280567414, 0.012732997253456224, 0.014808863353686585, 0.021949248479417816, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0182936604536994, 0.007107672506063034, 0.00716541776591173, 0.008231578825935504, 0.007599532071995929, 0.007405524428974575, 0.007502210471480142, 0.007656304787724499, 0.007312281519960218, 0.007105689689078654, 0.007045133726875763, 0.006828329355824891, 0.007055362328461712, 0.00686265082111337, 0.006940019725674373, 0.006604465085317868, 0.006707252751368742, 0.006637335657522447, 0.006729541680850826, 0.006689050176848843, 0.006467495495842357, 0.00647601608434778, 0.006657341313764498, 0.006632504221157465, 0.006330612235157407, 0.006586442244503443, 0.006785550146485075, 0.006865970570580249, 0.006869385074314227, 0.007225160391650887, 0.007342093802124916, 0.007544264221855723, 0.007779402125472901, 0.008021411349317775, 0.008460968334169428, 0.008842046536327697, 0.009341843959647322, 0.009869837349885113, 0.01062707328158674, 0.011455229280567414, 0.012732997253456224, 0.014808863353686696, 0.021949248479417927, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}