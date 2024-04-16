
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
  'curve1' : [1.638043],
}
yedges = {
  'curve0' : [1.636599, 1.636599],
  'curve1' : [1.638043, 1.638043],
}
yups = {
  'curve0' : [0.0005559668155564682],
  'curve1' : [0.0006315142120332685],
}
ydowns = {
  'curve0' : [0.0005559668155564682],
  'curve1' : [0.0006315142120332685],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [1.000882317537772, 1.000882317537772],
}
ratio0_ymax = {
  'curve0' : [1.0003397086369699],
  'curve1' : [1.001268187388623],
}
ratio0_ymin = {
  'curve0' : [0.99966029136303],
  'curve1' : [1.0004964476869207],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003397086369699709],
    [0.00033970863696985987],
  ],
  'curve1' : [
    [0.00038586985085120595],
    [0.00038586985085120595],
  ],
}
ratio0_variation_vals = {
}