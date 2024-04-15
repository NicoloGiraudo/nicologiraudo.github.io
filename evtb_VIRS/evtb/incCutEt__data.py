
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
  'curve0' : [1.542932],
  'curve1' : [0.07733873],
}
yedges = {
  'curve0' : [1.542932, 1.542932],
  'curve1' : [0.07733873, 0.07733873],
}
yups = {
  'curve0' : [0.00048791782094938896],
  'curve1' : [0.000638003605005489],
}
ydowns = {
  'curve0' : [0.00048791782094938896],
  'curve1' : [0.000638003605005489],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.050124522662048615, 0.050124522662048615],
}
ratio0_ymax = {
  'curve0' : [1.000316227689198],
  'curve1' : [0.0505380234546989],
}
ratio0_ymin = {
  'curve0' : [0.9996837723108022],
  'curve1' : [0.04971102186939833],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003162276891978122],
    [0.0003162276891979232],
  ],
  'curve1' : [
    [0.0004135007926502829],
    [0.0004135007926502829],
  ],
}
ratio0_variation_vals = {
}