
from numpy import nan

xpoints  = [-9.5, -8.5, -7.5, -6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
xedges   = [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
xmins    = [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
xmaxs    = [-9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 6.122755e-08, 1.525327e-07, 3.914895e-06, 8.100813e-05, 0.004768417, 0.2066519, 0.8337172, 0.3725745, 0.06121025, 0.008337387, 0.001140921, 0.0001559554, 2.470247e-05, 2.211042e-06, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 6.122755e-08, 1.525327e-07, 3.914895e-06, 8.100813e-05, 0.004768417, 0.2066519, 0.8337172, 0.3725745, 0.06121025, 0.008337387, 0.001140921, 0.0001559554, 2.470247e-05, 2.211042e-06, 0.0, 0.0],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 3.892933341325022e-08, 7.144365612145e-08, 5.263950037756818e-07, 8.12822305304179e-06, 5.585448057228713e-05, 0.00039813264121395524, 0.0006246175629935489, 0.0006634343976611403, 0.0006007177373775473, 0.0004142378543783752, 0.0002771156798162096, 0.00012148238555444983, 1.584999684542555e-05, 1.8949306055895555e-06, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 3.892933341325022e-08, 7.144365612145e-08, 5.263950037756818e-07, 8.12822305304179e-06, 5.585448057228713e-05, 0.00039813264121395524, 0.0006246175629935489, 0.0006634343976611403, 0.0006007177373775473, 0.0004142378543783752, 0.0002771156798162096, 0.00012148238555444983, 1.584999684542555e-05, 1.8949306055895555e-06, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.6358139989800378, 1.4683825574545655, 1.1344595458564488, 1.1003383617550706, 1.0117134219956616, 1.00192658592161, 1.0007491959659625, 1.0017806758048688, 1.0098140056179732, 1.049684374058488, 1.2428877019672786, 1.7789559422402164, 1.6416361135313817, 1.857030579061617, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 0.3641860010199622, 0.5316174425454345, 0.8655404541435513, 0.8996616382449294, 0.9882865780043384, 0.99807341407839, 0.9992508040340374, 0.998219324195131, 0.9901859943820267, 0.950315625941512, 0.7571122980327213, 0.22104405775978367, 0.3583638864686183, 0.14296942093838313, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.6358139989800378, 0.4683825574545655, 0.1344595458564487, 0.1003383617550706, 0.01171342199566161, 0.0019265859216099912, 0.000749195965962568, 0.0017806758048689586, 0.009814005617973298, 0.04968437405848802, 0.2428877019672787, 0.7789559422402164, 0.6416361135313817, 0.8570305790616168, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.6358139989800378, 0.4683825574545655, 0.13445954585644881, 0.1003383617550706, 0.01171342199566161, 0.0019265859216099912, 0.000749195965962457, 0.0017806758048688476, 0.009814005617973187, 0.04968437405848802, 0.2428877019672786, 0.7789559422402164, 0.6416361135313817, 0.8570305790616171, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}