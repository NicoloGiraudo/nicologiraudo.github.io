
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
  'curve0' : [1.638043],
  'curve1' : [1.636599],
}
yedges = {
  'curve0' : [1.638043, 1.638043],
  'curve1' : [1.636599, 1.636599],
}
yups = {
  'curve0' : [0.0006315142120332685],
  'curve1' : [0.0005559668155564682],
}
ydowns = {
  'curve0' : [0.0006315142120332685],
  'curve1' : [0.0005559668155564682],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.9991184602602008, 0.9991184602602008],
}
ratio0_ymax = {
  'curve0' : [1.0003855296912434],
  'curve1' : [0.9994578694305072],
}
ratio0_ymin = {
  'curve0' : [0.9996144703087567],
  'curve1' : [0.9987790510898943],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003855296912432804],
    [0.0003855296912433914],
  ],
  'curve1' : [
    [0.00033940917030650386],
    [0.00033940917030639284],
  ],
}
ratio0_variation_vals = {
}