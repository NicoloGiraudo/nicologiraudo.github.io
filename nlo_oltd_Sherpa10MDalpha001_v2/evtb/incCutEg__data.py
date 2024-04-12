
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
  'curve0' : [1.488669],
}
yedges = {
  'curve0' : [1.488669, 1.488669],
}
yups = {
  'curve0' : [0.0007561977915863018],
}
ydowns = {
  'curve0' : [0.0007561977915863018],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0005079690593317],
}
ratio0_ymin = {
  'curve0' : [0.9994920309406683],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0005079690593317032],
    [0.0005079690593317032],
  ],
}
ratio0_variation_vals = {
}