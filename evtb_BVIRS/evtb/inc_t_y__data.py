
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2067814, 1.198166, 0.2324624, 0.0006334642, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2178735, 1.109607, 0.2147798, 0.0006711753, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve2' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.01147903, 0.08794201, 0.01789739, -3.460573e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve3' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2064018, 1.197662, 0.2318965, 0.0006387675, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2067814, 1.198166, 0.2324624, 0.0006334642, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2178735, 1.109607, 0.2147798, 0.0006711753, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve2' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.01147903, 0.08794201, 0.01789739, -3.460573e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve3' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2064018, 1.197662, 0.2318965, 0.0006387675, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00025699250961847117, 0.0005571107609802561, 0.00024714855856346803, 7.687882673402346e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00018334775700836923, 0.0004137690176898217, 0.00018204136892475842, 1.0176335293218282e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve2' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002579494911799595, 0.0005622401622082862, 0.0002516479684003032, 8.177952066379455e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve3' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00024149573495198628, 0.0004884055691738168, 0.00022130966991977554, 2.2190229832067985e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00025699250961847117, 0.0005571107609802561, 0.00024714855856346803, 7.687882673402346e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00018334775700836923, 0.0004137690176898217, 0.00018204136892475842, 1.0176335293218282e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve2' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002579494911799595, 0.0005622401622082862, 0.0002516479684003032, 8.177952066379455e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'curve3' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00024149573495198628, 0.0004884055691738168, 0.00022130966991977554, 2.2190229832067985e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0536416718331532, 0.9260878709627881, 0.9239335049453158, 1.0595315410089472, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve2' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.055512874949100836, 0.07339718369574834, 0.07699047243769314, -0.054629338169386685, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve3' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9981642449465957, 0.9995793571174612, 0.9975656278176599, 1.0083719016796846, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.001242822176552, 1.0004649695960162, 1.0010631764903204, 1.012136254382493, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0545283461520638, 0.926433206264983, 0.9247166052184126, 1.0755961193911483, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve2' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.05426542478588519, 0.07386643433564988, 0.07807300435855562, -0.04171944986570756, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve3' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9993321243349353, 0.9999869847493367, 0.9985176513273535, 1.0434018683803568, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.998757177823448, 0.9995350304039838, 0.9989368235096795, 0.987863745617507, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0527549975142427, 0.9257425356605931, 0.923150404672219, 1.0434669626267463, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve2' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.05676032511231648, 0.07292793305584679, 0.07590794051683067, -0.06753922647306582, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve3' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9969963655582562, 0.9991717294855855, 0.9966136043079664, 0.9733419349790122, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0012428221765520275, 0.0004649695960161626, 0.0010631764903205054, 0.012136254382492995, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0012428221765519165, 0.0004649695960161626, 0.0010631764903203944, 0.012136254382492995, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0008866743189104298, 0.00034533530219504893, 0.000783100273096804, 0.016064578382200878, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0008866743189106518, 0.0003453353021949379, 0.000783100273096804, 0.0160645783822011, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve2' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0012474501632156465, 0.0004692506399015528, 0.0010825319208624673, 0.012909888303679132, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0012474501632156465, 0.0004692506399015389, 0.0010825319208624812, 0.012909888303679125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
  'curve3' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00116787938833951, 0.0004076276318756289, 0.0009520235096934782, 0.03502996670067238, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001167879388339621, 0.00040762763187551787, 0.0009520235096935892, 0.035029966700672155, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}