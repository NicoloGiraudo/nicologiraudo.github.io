
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
  'curve1' : [-0.05472442],
}
yedges = {
  'curve0' : [1.489845, 1.489845],
  'curve1' : [-0.05472442, -0.05472442],
}
yups = {
  'curve0' : [0.000568712757022383],
  'curve1' : [0.0007622293618065366],
}
ydowns = {
  'curve0' : [0.000568712757022383],
  'curve1' : [0.0007622293618065366],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [-0.03673161973225403, -0.03673161973225403],
}
ratio0_ymax = {
  'curve0' : [1.0003817261238737],
  'curve1' : [-0.03622000318032645],
}
ratio0_ymin = {
  'curve0' : [0.9996182738761265],
  'curve1' : [-0.0372432362841816],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0003817261238735492],
    [0.00038172612387366023],
  ],
  'curve1' : [
    [0.0005116165519275725],
    [0.0005116165519275795],
  ],
}
ratio0_variation_vals = {
}