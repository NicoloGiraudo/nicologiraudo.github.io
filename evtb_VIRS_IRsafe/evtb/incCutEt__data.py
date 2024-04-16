
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
  'curve0' : [0.07733873],
  'curve1' : [1.542932],
}
yedges = {
  'curve0' : [0.07733873, 0.07733873],
  'curve1' : [1.542932, 1.542932],
}
yups = {
  'curve0' : [0.000638003605005489],
  'curve1' : [0.00048791782094938896],
}
ydowns = {
  'curve0' : [0.000638003605005489],
  'curve1' : [0.00048791782094938896],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [19.950314674161316, 19.950314674161316],
}
ratio0_ymax = {
  'curve0' : [1.0082494709313883],
  'curve1' : [19.956623516069495],
}
ratio0_ymin = {
  'curve0' : [0.9917505290686117],
  'curve1' : [19.944005832253136],
}
ratio0_yerrs = {
  'curve0' : [
    [0.00824947093138828],
    [0.00824947093138828],
  ],
  'curve1' : [
    [0.0063088419081793745],
    [0.0063088419081793745],
  ],
}
ratio0_variation_vals = {
}