
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
  'curve0' : [-0.05472442],
  'curve1' : [1.542932],
}
yedges = {
  'curve0' : [-0.05472442, -0.05472442],
  'curve1' : [1.542932, 1.542932],
}
yups = {
  'curve0' : [0.0007622293618065366],
  'curve1' : [0.00048791782094938896],
}
ydowns = {
  'curve0' : [0.0007622293618065366],
  'curve1' : [0.00048791782094938896],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [-28.194579312124276, -28.194579312124276],
}
ratio0_ymax = {
  'curve0' : [0.986071494922988],
  'curve1' : [-28.203495218788053],
}
ratio0_ymin = {
  'curve0' : [1.013928505077012],
  'curve1' : [-28.185663405460495],
}
ratio0_yerrs = {
  'curve0' : [
    [0.013928505077011932],
    [0.013928505077012043],
  ],
  'curve1' : [
    [0.008915906663780504],
    [0.008915906663776951],
  ],
}
ratio0_variation_vals = {
}