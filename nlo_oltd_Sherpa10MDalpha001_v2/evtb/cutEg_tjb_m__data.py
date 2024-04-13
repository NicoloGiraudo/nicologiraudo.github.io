
from numpy import nan

xpoints  = [0.07, 0.21000000000000002, 0.35, 0.49, 0.63, 0.77, 0.9099999999999999, 1.05, 1.19, 1.33, 1.47, 1.6099999999999999, 1.75, 1.8900000000000001, 2.0300000000000002, 2.17, 2.31, 2.45, 2.59, 2.73, 2.87, 3.01, 3.1500000000000004, 3.29, 3.4299999999999997, 3.5700000000000003, 3.71, 3.8499999999999996, 3.9899999999999998, 4.13, 4.27, 4.41, 4.550000000000001, 4.6899999999999995, 4.83, 4.970000000000001, 5.109999999999999, 5.25, 5.390000000000001, 5.529999999999999, 5.67, 5.8100000000000005, 5.949999999999999, 6.09, 6.23, 6.37, 6.51, 6.65, 6.79, 6.93, 7.07, 7.21, 7.35, 7.49, 7.63, 7.77, 7.91, 8.05, 8.19, 8.33, 8.469999999999999, 8.61, 8.75, 8.89, 9.030000000000001, 9.17, 9.31, 9.45, 9.59, 9.73, 9.870000000000001, 10.01, 10.15, 10.29, 10.43, 10.57, 10.71, 10.85, 10.99, 11.129999999999999, 11.27, 11.41, 11.55, 11.69, 11.83, 11.969999999999999, 12.11, 12.25, 12.39, 12.530000000000001, 12.67, 12.81, 12.95, 13.09, 13.23, 13.370000000000001, 13.51, 13.65, 13.79, 13.93]
xedges   = [0.0, 0.14, 0.28, 0.42, 0.56, 0.7, 0.84, 0.98, 1.12, 1.26, 1.4, 1.54, 1.68, 1.82, 1.96, 2.1, 2.24, 2.38, 2.52, 2.66, 2.8, 2.94, 3.08, 3.22, 3.36, 3.5, 3.64, 3.78, 3.92, 4.06, 4.2, 4.34, 4.48, 4.62, 4.76, 4.9, 5.04, 5.18, 5.32, 5.46, 5.6, 5.74, 5.88, 6.02, 6.16, 6.3, 6.44, 6.58, 6.72, 6.86, 7.0, 7.14, 7.28, 7.42, 7.56, 7.7, 7.84, 7.98, 8.12, 8.26, 8.4, 8.54, 8.68, 8.82, 8.96, 9.1, 9.24, 9.38, 9.52, 9.66, 9.8, 9.94, 10.08, 10.22, 10.36, 10.5, 10.64, 10.78, 10.92, 11.06, 11.2, 11.34, 11.48, 11.62, 11.76, 11.9, 12.04, 12.18, 12.32, 12.46, 12.6, 12.74, 12.88, 13.02, 13.16, 13.3, 13.44, 13.58, 13.72, 13.86, 14.0]
xmins    = [0.0, 0.14, 0.28, 0.42, 0.56, 0.7, 0.84, 0.98, 1.12, 1.26, 1.4, 1.54, 1.68, 1.82, 1.96, 2.1, 2.24, 2.38, 2.52, 2.66, 2.8, 2.94, 3.08, 3.22, 3.36, 3.5, 3.64, 3.78, 3.92, 4.06, 4.2, 4.34, 4.48, 4.62, 4.76, 4.9, 5.04, 5.18, 5.32, 5.46, 5.6, 5.74, 5.88, 6.02, 6.16, 6.3, 6.44, 6.58, 6.72, 6.86, 7.0, 7.14, 7.28, 7.42, 7.56, 7.7, 7.84, 7.98, 8.12, 8.26, 8.4, 8.54, 8.68, 8.82, 8.96, 9.1, 9.24, 9.38, 9.52, 9.66, 9.8, 9.94, 10.08, 10.22, 10.36, 10.5, 10.64, 10.78, 10.92, 11.06, 11.2, 11.34, 11.48, 11.62, 11.76, 11.9, 12.04, 12.18, 12.32, 12.46, 12.6, 12.74, 12.88, 13.02, 13.16, 13.3, 13.44, 13.58, 13.72, 13.86]
xmaxs    = [0.14, 0.28, 0.42, 0.56, 0.7, 0.84, 0.98, 1.12, 1.26, 1.4, 1.54, 1.68, 1.82, 1.96, 2.1, 2.24, 2.38, 2.52, 2.66, 2.8, 2.94, 3.08, 3.22, 3.36, 3.5, 3.64, 3.78, 3.92, 4.06, 4.2, 4.34, 4.48, 4.62, 4.76, 4.9, 5.04, 5.18, 5.32, 5.46, 5.6, 5.74, 5.88, 6.02, 6.16, 6.3, 6.44, 6.58, 6.72, 6.86, 7.0, 7.14, 7.28, 7.42, 7.56, 7.7, 7.84, 7.98, 8.12, 8.26, 8.4, 8.54, 8.68, 8.82, 8.96, 9.1, 9.24, 9.38, 9.52, 9.66, 9.8, 9.94, 10.08, 10.22, 10.36, 10.5, 10.64, 10.78, 10.92, 11.06, 11.2, 11.34, 11.48, 11.62, 11.76, 11.9, 12.04, 12.18, 12.32, 12.46, 12.6, 12.74, 12.88, 13.02, 13.16, 13.3, 13.44, 13.58, 13.72, 13.86, 14.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023663164285714192, 0.060111028571429095, 0.06453292142857117, 0.069155564285714, 0.07395735714285778, 0.07951914285714254, 0.08820014285714249, 0.09279335714285794, 0.1019207857142853, 0.11101199999999956, 0.12235300000000104, 0.1327688571428566, 0.1483267142857137, 0.1624436428571422, 0.1859294285714302, 0.208587642857142, 0.2400688571428562, 0.2800097142857167, 0.3352826428571415, 0.40720835714285547, 0.5079887142857187, 0.6642267142857116, 0.9698357142857104, 1.6969771428571576, -19.59877142857135],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023663164285714192, 0.060111028571429095, 0.06453292142857117, 0.069155564285714, 0.07395735714285778, 0.07951914285714254, 0.08820014285714249, 0.09279335714285794, 0.1019207857142853, 0.11101199999999956, 0.12235300000000104, 0.1327688571428566, 0.1483267142857137, 0.1624436428571422, 0.1859294285714302, 0.208587642857142, 0.2400688571428562, 0.2800097142857167, 0.3352826428571415, 0.40720835714285547, 0.5079887142857187, 0.6642267142857116, 0.9698357142857104, 1.6969771428571576, -19.59877142857135],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00047660577128743204, 0.0007337678830001067, 0.0008198154969135351, 0.0008056373443505704, 0.001889164052253428, 0.0012554767774736009, 0.0021903830854954234, 0.0010329183937578437, 0.0011884705486035181, 0.0011638592558152932, 0.00135105268859026, 0.0013398358869957238, 0.0015973936041347454, 0.0012594609310076596, 0.002626926892389528, 0.0017181888601616674, 0.002218941648808343, 0.0024364337018834663, 0.004106427266853639, 0.0038369497877180085, 0.004052224760573426, 0.0050104345202419765, 0.007513742511599117, 0.01245335582999916, 0.4199846935986375],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00047660577128743204, 0.0007337678830001067, 0.0008198154969135351, 0.0008056373443505704, 0.001889164052253428, 0.0012554767774736009, 0.0021903830854954234, 0.0010329183937578437, 0.0011884705486035181, 0.0011638592558152932, 0.00135105268859026, 0.0013398358869957238, 0.0015973936041347454, 0.0012594609310076596, 0.002626926892389528, 0.0017181888601616674, 0.002218941648808343, 0.0024364337018834663, 0.004106427266853639, 0.0038369497877180085, 0.004052224760573426, 0.0050104345202419765, 0.007513742511599117, 0.01245335582999916, 0.4199846935986375],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0201412526884734, 1.0122068761829317, 1.0127038336211225, 1.0116496387914948, 1.0255439637817814, 1.0157883590336114, 1.0248342351218545, 1.011131382951989, 1.011660727890532, 1.0104840851062524, 1.011042252242203, 1.0100914922055408, 1.010769426207728, 1.007753217724348, 1.0141286234921134, 1.008237251433626, 1.0092429383603385, 1.008701247055298, 1.0122476583692503, 1.0094225713210792, 1.007976997611593, 1.0075432595715907, 1.007747438458825, 1.007338552485764, 0.9785708662846908],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9798587473115264, 0.9877931238170683, 0.9872961663788775, 0.9883503612085051, 0.9744560362182187, 0.9842116409663886, 0.9751657648781457, 0.988868617048011, 0.9883392721094678, 0.9895159148937476, 0.9889577477577971, 0.989908507794459, 0.989230573792272, 0.992246782275652, 0.9858713765078866, 0.9917627485663739, 0.9907570616396615, 0.9912987529447019, 0.9877523416307498, 0.9905774286789208, 0.9920230023884069, 0.9924567404284093, 0.992252561541175, 0.992661447514236, 1.0214291337153092],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.020141252688473554, 0.012206876182931703, 0.012703833621122484, 0.011649638791494943, 0.025543963781781254, 0.01578835903361142, 0.024834235121854342, 0.01113138295198901, 0.011660727890532185, 0.010484085106252428, 0.011042252242202899, 0.010091492205540953, 0.010769426207728028, 0.007753217724348005, 0.014128623492113412, 0.00823725143362608, 0.009242938360338515, 0.008701247055298067, 0.012247658369250236, 0.009422571321079154, 0.007976997611593095, 0.0075432595715907436, 0.007747438458824973, 0.007338552485763983, 0.02142913371530919],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.020141252688473443, 0.012206876182931703, 0.012703833621122484, 0.011649638791494832, 0.025543963781781365, 0.01578835903361142, 0.024834235121854453, 0.01113138295198901, 0.011660727890532074, 0.010484085106252428, 0.011042252242202899, 0.010091492205540842, 0.010769426207728028, 0.007753217724348005, 0.014128623492113412, 0.00823725143362597, 0.009242938360338515, 0.008701247055298067, 0.012247658369250347, 0.009422571321079154, 0.007976997611593095, 0.0075432595715907436, 0.007747438458824973, 0.007338552485764094, 0.02142913371530919],
  ],
}
ratio0_variation_vals = {
}