
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.584529, 1.221488, 0.4475221, 0.09119379, 0.01181616, 0.001439573, 0.0001506995, 8.343334e-05, 1.41155e-06, 4.146258e-07],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.584529, 1.221488, 0.4475221, 0.09119379, 0.01181616, 0.001439573, 0.0001506995, 8.343334e-05, 1.41155e-06, 4.146258e-07],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.059496050289073815, 0.059686279830460195, 0.059165589661559194, 0.02963297318866266, 0.003137731983455566, 0.0005365780465132728, 9.165576904919842e-05, 0.00012245729867998886, 5.649446875579945e-07, 3.0849397076766345e-07],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.059496050289073815, 0.059686279830460195, 0.059165589661559194, 0.02963297318866266, 0.003137731983455566, 0.0005365780465132728, 9.165576904919842e-05, 0.00012245729867998886, 5.649446875579945e-07, 3.0849397076766345e-07],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0165980105863488, 1.0488635826389292, 1.1322070790728753, 1.324945077824517, 1.2655458273631677, 1.3727341694469632, 1.608202210685493, 2.4677261953074017, 1.4002300220027588, 1.7440298475581197],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9834019894136513, 0.9511364173610709, 0.8677929209271247, 0.675054922175483, 0.7344541726368323, 0.627265830553037, 0.3917977893145072, -0.4677261953074019, 0.599769977997241, 0.25597015244188026],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.016598010586348688, 0.04886358263892909, 0.13220707907287532, 0.324945077824517, 0.2655458273631677, 0.372734169446963, 0.6082022106854927, 1.467726195307402, 0.40023002200275903, 0.7440298475581197],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0165980105863488, 0.048863582638929204, 0.13220707907287532, 0.3249450778245171, 0.2655458273631677, 0.37273416944696325, 0.608202210685493, 1.4677261953074017, 0.4002300220027588, 0.7440298475581197],
  ],
}
ratio0_variation_vals = {
}