
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
  'curve0' : [1.620527],
  'curve1' : [0.07733873],
}
yedges = {
  'curve0' : [1.620527, 1.620527],
  'curve1' : [0.07733873, 0.07733873],
}
yups = {
  'curve0' : [0.0005506247360952829],
  'curve1' : [0.000638003605005489],
}
ydowns = {
  'curve0' : [0.0005506247360952829],
  'curve1' : [0.000638003605005489],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.04772443162008408, 0.04772443162008408],
}
ratio0_ymax = {
  'curve0' : [1.0003397812786181],
  'curve1' : [0.048118132931450994],
}
ratio0_ymin = {
  'curve0' : [0.9996602187213818],
  'curve1' : [0.047330730308717164],
}
ratio0_yerrs = {
  'curve0' : [
    [0.00033978127861822305],
    [0.000339781278618112],
  ],
  'curve1' : [
    [0.00039370131136691466],
    [0.00039370131136691466],
  ],
}
ratio0_variation_vals = {
}