
from numpy import nan

xpoints  = [0.5]
xedges   = [0.0, 1.0]
xmins    = [0.0]
xmaxs    = [1.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [1.489845],
  'curve1' : [1.488669],
}
yedges = {
  'curve0' : [1.489845, 1.489845],
  'curve1' : [1.488669, 1.488669],
}
yups = {
  'curve0' : [0.000568712757022383],
  'curve1' : [0.0007561977915863018],
}
ydowns = {
  'curve0' : [0.000568712757022383],
  'curve1' : [0.0007561977915863018],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.9992106561420818, 0.9992106561420818],
}
ratio0_ymax = {
  'curve0' : [1.0003817261238737],
  'curve1' : [0.9997182242391565],
}
ratio0_ymin = {
  'curve0' : [0.9996182738761265],
  'curve1' : [0.9987030880450072],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003817261238735492],
    [0.00038172612387366023],
  ],
  'curve1' : [
    [0.0005075680970746399],
    [0.0005075680970746399],
  ],
}
ratio0_variation_vals = {
}