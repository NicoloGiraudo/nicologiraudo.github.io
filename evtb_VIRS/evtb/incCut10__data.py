
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
  'curve1' : [0.09432576],
}
yedges = {
  'curve0' : [1.542932, 1.542932],
  'curve1' : [0.09432576, 0.09432576],
}
yups = {
  'curve0' : [0.00048791782094938896],
  'curve1' : [0.0006412690542978041],
}
ydowns = {
  'curve0' : [0.00048791782094938896],
  'curve1' : [0.0006412690542978041],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.06113410053067796, 0.06113410053067796],
}
ratio0_ymax = {
  'curve0' : [1.000316227689198],
  'curve1' : [0.06154971771555571],
}
ratio0_ymin = {
  'curve0' : [0.9996837723108022],
  'curve1' : [0.0607184833458002],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003162276891978122],
    [0.0003162276891979232],
  ],
  'curve1' : [
    [0.000415617184877759],
    [0.00041561718487775207],
  ],
}
ratio0_variation_vals = {
}