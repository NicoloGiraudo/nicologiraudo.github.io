
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
  'curve0' : [0.09432576],
  'curve1' : [1.542932],
}
yedges = {
  'curve0' : [0.09432576, 0.09432576],
  'curve1' : [1.542932, 1.542932],
}
yups = {
  'curve0' : [0.0006412690542978041],
  'curve1' : [0.00048791782094938896],
}
ydowns = {
  'curve0' : [0.0006412690542978041],
  'curve1' : [0.00048791782094938896],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [16.357482833957555, 16.357482833957555],
}
ratio0_ymax = {
  'curve0' : [1.0067984509671357],
  'curve1' : [16.36265552295523],
}
ratio0_ymin = {
  'curve0' : [0.9932015490328644],
  'curve1' : [16.35231014495988],
}
ratio0_yerrs = {
  'curve0' : [
    [0.006798450967135605],
    [0.006798450967135716],
  ],
  'curve1' : [
    [0.005172688997674868],
    [0.005172688997674868],
  ],
}
ratio0_variation_vals = {
}