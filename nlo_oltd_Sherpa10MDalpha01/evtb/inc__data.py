
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
  'curve0' : [1.638963],
  'curve1' : [1.637618],
}
yedges = {
  'curve0' : [1.638963, 1.638963],
  'curve1' : [1.637618, 1.637618],
}
yups = {
  'curve0' : [0.001230145519847144],
  'curve1' : [0.001754107750396195],
}
ydowns = {
  'curve0' : [0.001230145519847144],
  'curve1' : [0.001754107750396195],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.999179359143556, 0.999179359143556],
}
ratio0_ymax = {
  'curve0' : [1.0007505633256193],
  'curve1' : [1.0002496137804187],
}
ratio0_ymin = {
  'curve0' : [0.9992494366743806],
  'curve1' : [0.9981091045066934],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0007505633256194022],
    [0.0007505633256192912],
  ],
  'curve1' : [
    [0.001070254636862611],
    [0.001070254636862611],
  ],
}
ratio0_variation_vals = {
}