
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
  'curve0' : [0.5095108125, 0.5582728125, 0.7488331250000001, 0.6340981249999998, 0.4776914374999999, 0.40039325000000014, 0.3345546249999997, 0.30004831250000014, 0.27307443750000016, 0.2584685624999998, 0.24743950000000012, 0.2400906250000001, 0.23900749999999982, 0.23743699999999981, 0.23644068750000044, 0.23481481249999978, 0.23043887499999982, 0.2213180625000004, 0.20778987499999982, 0.1259307499999999],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.5095108125, 0.5095108125, 0.5582728125, 0.7488331250000001, 0.6340981249999998, 0.4776914374999999, 0.40039325000000014, 0.3345546249999997, 0.30004831250000014, 0.27307443750000016, 0.2584685624999998, 0.24743950000000012, 0.2400906250000001, 0.23900749999999982, 0.23743699999999981, 0.23644068750000044, 0.23481481249999978, 0.23043887499999982, 0.2213180625000004, 0.20778987499999982, 0.1259307499999999],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.005090609077630102, 0.007626150015735331, 0.009880146997261733, 0.00781200248415859, 0.005182087537855762, 0.004114369825684125, 0.0025292244982405157, 0.002170470319135925, 0.0018193456928247594, 0.001496480506471767, 0.0018292148460815102, 0.0013733559773871455, 0.0019368343614646023, 0.0012676163346513791, 0.0012979369146360721, 0.0016461502200209417, 0.0012211733919165605, 0.0011864905248778876, 0.0021139205652649278, 0.0008867214895332122],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.005090609077630102, 0.007626150015735331, 0.009880146997261733, 0.00781200248415859, 0.005182087537855762, 0.004114369825684125, 0.0025292244982405157, 0.002170470319135925, 0.0018193456928247594, 0.001496480506471767, 0.0018292148460815102, 0.0013733559773871455, 0.0019368343614646023, 0.0012676163346513791, 0.0012979369146360721, 0.0016461502200209417, 0.0012211733919165605, 0.0011864905248778876, 0.0021139205652649278, 0.0008867214895332122],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ratio0_ymax = {
  'curve0' : [1.0099911698687065, 1.0136602568582638, 1.0131940570834947, 1.0123198637185036, 1.0108481901308013, 1.0102758221465624, 1.0075599746924453, 1.0072337361308636, 1.0066624533203508, 1.0057897969950282, 1.0073925741285505, 1.0057201566174736, 1.0081036551633928, 1.0053387481085567, 1.0054894820699423, 1.0070104189871791, 1.005299337587534, 1.0053610198439085, 1.010173356932165, 1.0070413420831148],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ratio0_ymin = {
  'curve0' : [0.9900088301312935, 0.9863397431417363, 0.9868059429165054, 0.9876801362814965, 0.9891518098691987, 0.9897241778534375, 0.9924400253075548, 0.9927662638691364, 0.9933375466796494, 0.9942102030049718, 0.9926074258714493, 0.9942798433825264, 0.9918963448366072, 0.9946612518914433, 0.9945105179300578, 0.9929895810128208, 0.994700662412466, 0.9946389801560915, 0.9898266430678351, 0.9929586579168853],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.009991169868706518, 0.013660256858263664, 0.013194057083494637, 0.012319863718503465, 0.010848190130801294, 0.01027582214656253, 0.007559974692445182, 0.007233736130863644, 0.0066624533203506475, 0.00578979699502824, 0.007392574128550655, 0.005720156617473604, 0.008103655163392842, 0.0053387481085567234, 0.005489482069942153, 0.0070104189871792455, 0.005299337587533981, 0.0053610198439084655, 0.010173356932164923, 0.007041342083114688],
    [0.009991169868706518, 0.013660256858263775, 0.013194057083494748, 0.012319863718503576, 0.010848190130801294, 0.010275822146562419, 0.007559974692445293, 0.007233736130863644, 0.0066624533203507585, 0.00578979699502824, 0.007392574128550544, 0.005720156617473604, 0.008103655163392842, 0.0053387481085567234, 0.005489482069942264, 0.0070104189871791345, 0.005299337587534092, 0.0053610198439084655, 0.010173356932164923, 0.007041342083114799],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}