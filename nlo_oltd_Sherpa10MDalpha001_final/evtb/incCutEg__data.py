
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
  'curve1' : [1.489845],
}
yedges = {
  'curve0' : [1.488669, 1.488669],
  'curve1' : [1.489845, 1.489845],
}
yups = {
  'curve0' : [0.0007561977915863018],
  'curve1' : [0.000568712757022383],
}
ydowns = {
  'curve0' : [0.0007561977915863018],
  'curve1' : [0.000568712757022383],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [1.0007899674138443, 1.0007899674138443],
}
ratio0_ymax = {
  'curve0' : [1.0005079690593317],
  'curve1' : [1.0011719950889166],
}
ratio0_ymin = {
  'curve0' : [0.9994920309406683],
  'curve1' : [1.0004079397387717],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0005079690593317032],
    [0.0005079690593317032],
  ],
  'curve1' : [
    [0.0003820276750725604],
    [0.00038202767507233837],
  ],
}
ratio0_variation_vals = {
}