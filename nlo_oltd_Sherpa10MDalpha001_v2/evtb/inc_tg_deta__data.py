
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.632765, 1.13323, 0.5955181, 0.2700252, 0.1161873, 0.04794554, 0.01255038, 0.00313241, 0.001894656, 0.000440782],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.632765, 1.13323, 0.5955181, 0.2700252, 0.1161873, 0.04794554, 0.01255038, 0.00313241, 0.001894656, 0.000440782],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.024613323627661502, 0.028872608126042233, 0.024853027984533396, 0.022483825297310956, 0.015388654911979799, 0.014183772417801973, 0.0026435945226149942, 0.0003337972438472193, 0.0008700198273602735, 0.00014654828555803716],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.024613323627661502, 0.028872608126042233, 0.024853027984533396, 0.022483825297310956, 0.015388654911979799, 0.014183772417801973, 0.0026435945226149942, 0.0003337972438472193, 0.0008700198273602735, 0.00014654828555803716],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0150746271678175, 1.0254781537075812, 1.0417334552627928, 1.0832656555658915, 1.132446962034403, 1.295830903516823, 1.2106386039797197, 1.1065624371800689, 1.4591967235003471, 1.3324733894715235],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9849253728321825, 0.9745218462924189, 0.9582665447372072, 0.9167343444341085, 0.8675530379655969, 0.7041690964831772, 0.7893613960202803, 0.8934375628199313, 0.540803276499653, 0.6675266105284763],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01507462716781749, 0.025478153707581108, 0.04173345526279282, 0.0832656555658915, 0.1324469620344031, 0.29583090351682284, 0.21063860397971967, 0.10656243718006875, 0.459196723500347, 0.3324733894715237],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01507462716781749, 0.02547815370758122, 0.04173345526279282, 0.0832656555658915, 0.1324469620344031, 0.29583090351682295, 0.21063860397971967, 0.10656243718006886, 0.4591967235003471, 0.3324733894715235],
  ],
}
ratio0_variation_vals = {
}