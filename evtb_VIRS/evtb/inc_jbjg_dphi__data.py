
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [1.9510712499999998, 1.9608125, 2.2826737500000003, 2.0046549999999996, 1.9956662499999995, 1.9484956250000012, 2.077560624999998, 1.6244768750000007, 1.7360006250000009, 1.6170906249999983, 1.6813475000000009, 1.4979118750000007, 1.5904612499999988, 1.6036893749999985, 1.6196668750000032, 1.7559981249999983, 1.6623237499999983, 1.608176250000003, 1.6001524999999985, 0.9582993749999991],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [1.9510712499999998, 1.9510712499999998, 1.9608125, 2.2826737500000003, 2.0046549999999996, 1.9956662499999995, 1.9484956250000012, 2.077560624999998, 1.6244768750000007, 1.7360006250000009, 1.6170906249999983, 1.6813475000000009, 1.4979118750000007, 1.5904612499999988, 1.6036893749999985, 1.6196668750000032, 1.7559981249999983, 1.6623237499999983, 1.608176250000003, 1.6001524999999985, 0.9582993749999991],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.11476383699253873, 0.18628450812869546, 0.22538786014335382, 0.1444692333163016, 0.22933071779637368, 0.20197037220840103, 0.2853605860354577, 0.14746612428791916, 0.23297029048786472, 0.19253320533417068, 0.16522685635967305, 0.17082181871763347, 0.16372360235699052, 0.1575349167645064, 0.15297225800369849, 0.21921700150763834, 0.20050044809800283, 0.1850571280037603, 0.16623005049478853, 0.1285455597735681],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.11476383699253873, 0.18628450812869546, 0.22538786014335382, 0.1444692333163016, 0.22933071779637368, 0.20197037220840103, 0.2853605860354577, 0.14746612428791916, 0.23297029048786472, 0.19253320533417068, 0.16522685635967305, 0.17082181871763347, 0.16372360235699052, 0.1575349167645064, 0.15297225800369849, 0.21921700150763834, 0.20050044809800283, 0.1850571280037603, 0.16623005049478853, 0.1285455597735681],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
    [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
  ],
}
ratio0_variation_vals = {
}