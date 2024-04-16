
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
  'curve0' : [1.636599],
  'curve1' : [0.09432576],
}
yedges = {
  'curve0' : [1.636599, 1.636599],
  'curve1' : [0.09432576, 0.09432576],
}
yups = {
  'curve0' : [0.0005559668155564682],
  'curve1' : [0.0006412690542978041],
}
ydowns = {
  'curve0' : [0.0005559668155564682],
  'curve1' : [0.0006412690542978041],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.05763523013273258, 0.05763523013273258],
}
ratio0_ymax = {
  'curve0' : [1.0003397086369699],
  'curve1' : [0.05802706041876953],
}
ratio0_ymin = {
  'curve0' : [0.99966029136303],
  'curve1' : [0.05724339984669562],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003397086369699709],
    [0.00033970863696985987],
  ],
  'curve1' : [
    [0.00039183028603696074],
    [0.0003918302860369538],
  ],
}
ratio0_variation_vals = {
}