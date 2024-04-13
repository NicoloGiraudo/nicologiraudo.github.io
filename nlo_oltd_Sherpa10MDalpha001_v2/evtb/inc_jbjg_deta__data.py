
from numpy import nan

xpoints  = [-9.5, -8.5, -7.5, -6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
xedges   = [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
xmins    = [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
xmaxs    = [-9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.687611, 1.255192, 0.4571287, 0.09355853, 0.01231541, 0.001536799, 0.0001690545, 8.649672e-05, 1.759303e-06, 4.536731e-07],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.687611, 1.255192, 0.4571287, 0.09355853, 0.01231541, 0.001536799, 0.0001690545, 8.649672e-05, 1.759303e-06, 4.536731e-07],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05949790752623154, 0.05968644737291708, 0.05916562346498176, 0.02963299006175381, 0.003137761781907607, 0.0005366034848936409, 9.168382081916089e-05, 0.00012246121835095386, 5.840428066503345e-07, 3.1095533441315974e-07],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.05949790752623154, 0.05968644737291708, 0.05916562346498176, 0.02963299006175381, 0.003137761781907607, 0.0005366034848936409, 9.168382081916089e-05, 0.00012246121835095386, 5.840428066503345e-07, 3.1095533441315974e-07],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.016134540092822, 1.0475516473757935, 1.1294288095780942, 1.316732104082373, 1.2547833796769745, 1.3491695953040321, 1.5423329211535977, 2.4157903137940244, 1.331973973016777, 1.685417174642181],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.983865459907178, 0.9524483526242065, 0.8705711904219058, 0.683267895917627, 0.7452166203230256, 0.6508304046959681, 0.4576670788464023, -0.41579031379402426, 0.6680260269832231, 0.3145828253578188],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.016134540092822003, 0.04755164737579354, 0.12942880957809422, 0.31673210408237296, 0.2547833796769744, 0.3491695953040319, 0.5423329211535977, 1.4157903137940242, 0.3319739730167769, 0.6854171746421812],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.016134540092821892, 0.04755164737579354, 0.12942880957809422, 0.31673210408237296, 0.2547833796769745, 0.34916959530403213, 0.5423329211535977, 1.4157903137940244, 0.331973973016777, 0.6854171746421811],
  ],
}
ratio0_variation_vals = {
}