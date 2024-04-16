
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5146127, 0.36656, 0.1966858, 0.08752149, 0.03557096, 0.01339846, 0.005535338, 0.00182907, 0.0006313246, 0.0001275306],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5138725, 0.368195, 0.1952097, 0.0875809, 0.0353431, 0.01382344, 0.005242356, 0.001718316, 0.0007948807, 0.0003051916],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5146127, 0.36656, 0.1966858, 0.08752149, 0.03557096, 0.01339846, 0.005535338, 0.00182907, 0.0006313246, 0.0001275306],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5138725, 0.368195, 0.1952097, 0.0875809, 0.0353431, 0.01382344, 0.005242356, 0.001718316, 0.0007948807, 0.0003051916],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007376923477981861, 0.001068584577841174, 0.0012176694953886296, 0.0012651604641309338, 0.0011972660523041651, 0.0009631126102382836, 0.0009302423877678333, 0.0007236359581999778, 0.0004028755390936511, 0.0001212964137969462],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0006058098711642127, 0.0007511098454953178, 0.0006120999101453944, 0.0004913393939020155, 0.00038673388783503314, 0.00030921667160746687, 0.00023253711531710374, 0.00016617241046575692, 0.00012490804617797845, 0.00014346239925499643],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007376923477981861, 0.001068584577841174, 0.0012176694953886296, 0.0012651604641309338, 0.0011972660523041651, 0.0009631126102382836, 0.0009302423877678333, 0.0007236359581999778, 0.0004028755390936511, 0.0001212964137969462],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0006058098711642127, 0.0007511098454953178, 0.0006120999101453944, 0.0004913393939020155, 0.00038673388783503314, 0.00030921667160746687, 0.00023253711531710374, 0.00016617241046575692, 0.00012490804617797845, 0.00014346239925499643],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9985616367415727, 1.0044603884766476, 0.9924951369137986, 1.0006788047141337, 0.9935942128073013, 1.0317185706417007, 0.9470706215230218, 0.939447916154111, 1.2590681560642496, 2.393085267378966],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0014334903662467, 1.0029151696252758, 1.0061909375022937, 1.0144554264801813, 1.0336585251650268, 1.07188233649526, 1.1680552095947587, 1.3956305435002367, 1.6381432611586038, 1.9511161540598583],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9997388519000097, 1.0065094659687235, 0.995607206570812, 1.0062927332921552, 1.00446639303058, 1.0547970939650875, 0.9890801817914469, 1.03029868209842, 1.4569189069742863, 3.51801057357996],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9985665096337534, 0.9970848303747241, 0.9938090624977064, 0.9855445735198186, 0.9663414748349731, 0.9281176635047398, 0.8319447904052412, 0.6043694564997633, 0.36185673884139624, 0.048883845940141515],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9973844215831357, 1.002411310984572, 0.9893830672567853, 0.9950648761361124, 0.9827220325840227, 1.0086400473183137, 0.9050610612545966, 0.8485971502098023, 1.061217405154213, 1.2681599611779726],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0014334903662466258, 0.0029151696252759374, 0.006190937502293603, 0.014455426480181388, 0.033658525165026876, 0.07188233649526021, 0.16805520959475884, 0.39563054350023674, 0.6381432611586038, 0.9511161540598585],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0014334903662467369, 0.0029151696252758263, 0.006190937502293714, 0.014455426480181277, 0.033658525165026765, 0.0718823364952601, 0.16805520959475873, 0.39563054350023674, 0.6381432611586038, 0.9511161540598583],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0011772151584370505, 0.0020490774920756127, 0.0031120696570133832, 0.005613928578021343, 0.010872180223278627, 0.023078523323387, 0.04200956026842517, 0.09085076594430874, 0.19785075091003668, 1.1249253062009936],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0011772151584369395, 0.002049077492075835, 0.0031120696570133832, 0.005613928578021454, 0.010872180223278627, 0.02307852332338678, 0.04200956026842506, 0.09085076594430885, 0.19785075091003668, 1.1249253062009936],
  ],
}
ratio0_variation_vals = {
}