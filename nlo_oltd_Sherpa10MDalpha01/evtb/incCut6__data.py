
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
  'curve0' : [5.479467],
  'curve1' : [3.819005],
}
yedges = {
  'curve0' : [5.479467, 5.479467],
  'curve1' : [3.819005, 3.819005],
}
yups = {
  'curve0' : [0.2323893500141519],
  'curve1' : [0.14003056809139924],
}
ydowns = {
  'curve0' : [0.2323893500141519],
  'curve1' : [0.14003056809139924],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.6969665115238399, 0.6969665115238399],
}
ratio0_ymax = {
  'curve0' : [1.0424109407017421],
  'curve1' : [0.7225220204978695],
}
ratio0_ymin = {
  'curve0' : [0.957589059298258],
  'curve1' : [0.6714110025498102],
}
ratio0_yerrs = {
  'curve0' : [
    [0.042410940701742006],
    [0.04241094070174212],
  ],
  'curve1' : [
    [0.025555508974029695],
    [0.025555508974029584],
  ],
}
ratio0_variation_vals = {
}