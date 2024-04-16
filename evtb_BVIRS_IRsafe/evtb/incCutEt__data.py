
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
  'curve0' : [1.621026],
  'curve1' : [1.620527],
}
yedges = {
  'curve0' : [1.621026, 1.621026],
  'curve1' : [1.620527, 1.620527],
}
yups = {
  'curve0' : [0.0006282377734584255],
  'curve1' : [0.0005506247360952829],
}
ydowns = {
  'curve0' : [0.0006282377734584255],
  'curve1' : [0.0005506247360952829],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.9996921702674726, 0.9996921702674726],
}
ratio0_ymax = {
  'curve0' : [1.0003875556428203],
  'curve1' : [1.0000318469513108],
}
ratio0_ymin = {
  'curve0' : [0.9996124443571798],
  'curve1' : [0.9993524935836344],
}
ratio0_yerrs = {
  'curve0' : [
    [0.00038755564282022537],
    [0.0003875556428203364],
  ],
  'curve1' : [
    [0.00033967668383816374],
    [0.00033967668383816374],
  ],
}
ratio0_variation_vals = {
}