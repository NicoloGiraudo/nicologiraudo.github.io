
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
  'curve0' : [3.813922],
  'curve1' : [5.507599],
}
yedges = {
  'curve0' : [3.813922, 3.813922],
  'curve1' : [5.507599, 5.507599],
}
yups = {
  'curve0' : [0.042510751581217664],
  'curve1' : [0.07868058845738254],
}
ydowns = {
  'curve0' : [0.042510751581217664],
  'curve1' : [0.07868058845738254],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [1.4440775139082551, 1.4440775139082551],
}
ratio0_ymax = {
  'curve0' : [1.0111462037192207],
  'curve1' : [1.4647073507159776],
}
ratio0_ymin = {
  'curve0' : [0.9888537962807793],
  'curve1' : [1.4234476771005327],
}
ratio0_yerrs = {
  'curve0' : [
    [0.011146203719220704],
    [0.011146203719220704],
  ],
  'curve1' : [
    [0.020629836807722457],
    [0.020629836807722457],
  ],
}
ratio0_variation_vals = {
}