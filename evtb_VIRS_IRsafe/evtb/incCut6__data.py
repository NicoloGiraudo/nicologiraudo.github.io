
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
  'curve0' : [5.564245],
  'curve1' : [0.0],
}
yedges = {
  'curve0' : [5.564245, 5.564245],
  'curve1' : [0.0, 0.0],
}
yups = {
  'curve0' : [0.07904397510247065],
  'curve1' : [0.0],
}
ydowns = {
  'curve0' : [0.07904397510247065],
  'curve1' : [0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.0, 0.0],
}
ratio0_ymax = {
  'curve0' : [1.0142056963887232],
  'curve1' : [0.0],
}
ratio0_ymin = {
  'curve0' : [0.985794303611277],
  'curve1' : [0.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.014205696388723044],
    [0.014205696388723155],
  ],
  'curve1' : [
    [0.0],
    [0.0],
  ],
}
ratio0_variation_vals = {
}