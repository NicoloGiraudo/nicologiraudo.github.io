
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
  'curve0' : [5.507599],
  'curve1' : [0.0],
  'curve2' : [5.564245],
  'curve3' : [3.813922],
}
yedges = {
  'curve0' : [5.507599, 5.507599],
  'curve1' : [0.0, 0.0],
  'curve2' : [5.564245, 5.564245],
  'curve3' : [3.813922, 3.813922],
}
yups = {
  'curve0' : [0.07868058845738254],
  'curve1' : [0.0],
  'curve2' : [0.07904397510247065],
  'curve3' : [0.042510751581217664],
}
ydowns = {
  'curve0' : [0.07868058845738254],
  'curve1' : [0.0],
  'curve2' : [0.07904397510247065],
  'curve3' : [0.042510751581217664],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0],
  'curve1' : [0.0, 0.0],
  'curve2' : [1.0102850625109054, 1.0102850625109054],
  'curve3' : [0.6924836031090862, 0.6924836031090862],
}
ratio0_ymax = {
  'curve0' : [1.014285823724164],
  'curve1' : [0.0],
  'curve2' : [1.0246368653749973],
  'curve3' : [0.7002021664215601],
}
ratio0_ymin = {
  'curve0' : [0.9857141762758359],
  'curve1' : [0.0],
  'curve2' : [0.9959332596468133],
  'curve3' : [0.6847650397966123],
}
ratio0_yerrs = {
  'curve0' : [
    [0.014285823724164093],
    [0.014285823724164093],
  ],
  'curve1' : [
    [0.0],
    [0.0],
  ],
  'curve2' : [
    [0.0143518028640921],
    [0.014351802864091878],
  ],
  'curve3' : [
    [0.007718563312473892],
    [0.007718563312473892],
  ],
}
ratio0_variation_vals = {
}