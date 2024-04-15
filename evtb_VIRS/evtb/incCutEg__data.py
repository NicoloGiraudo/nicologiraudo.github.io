
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
  'curve1' : [-0.05472442],
}
yedges = {
  'curve0' : [1.542932, 1.542932],
  'curve1' : [-0.05472442, -0.05472442],
}
yups = {
  'curve0' : [0.00048791782094938896],
  'curve1' : [0.0007622293618065366],
}
ydowns = {
  'curve0' : [0.00048791782094938896],
  'curve1' : [0.0007622293618065366],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [-0.03546781063585434, -0.03546781063585434],
}
ratio0_ymax = {
  'curve0' : [1.000316227689198],
  'curve1' : [-0.034973797055342336],
}
ratio0_ymin = {
  'curve0' : [0.9996837723108022],
  'curve1' : [-0.03596182421636634],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003162276891978122],
    [0.0003162276891979232],
  ],
  'curve1' : [
    [0.0004940135805120011],
    [0.0004940135805120011],
  ],
}
ratio0_variation_vals = {
}