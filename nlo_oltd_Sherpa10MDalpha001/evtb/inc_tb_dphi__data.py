
from numpy import nan

xpoints  = [0.08, 0.24, 0.4, 0.56, 0.72, 0.88, 1.04, 1.2000000000000002, 1.3599999999999999, 1.52, 1.6800000000000002, 1.8399999999999999, 2.0, 2.16, 2.3200000000000003, 2.48, 2.64, 2.8, 2.96, 3.12]
xedges   = [0.0, 0.16, 0.32, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92, 2.08, 2.24, 2.4, 2.56, 2.72, 2.88, 3.04, 3.2]
xmins    = [0.0, 0.16, 0.32, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92, 2.08, 2.24, 2.4, 2.56, 2.72, 2.88, 3.04]
xmaxs    = [0.16, 0.32, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92, 2.08, 2.24, 2.4, 2.56, 2.72, 2.88, 3.04, 3.2]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0325924999999992e-05, 0.0015576575000000009, 0.008169837500000004, 0.02084326874999998, 0.041028731249999964, 0.07275475000000013, 0.1270711874999999, 0.2329756874999998, 0.49254256250000095, 1.4546606249999987, 7.786156249999992],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.873556874999995e-06, 0.0014731337500000006, 0.008223993750000004, 0.020859549999999984, 0.04076716249999997, 0.07239937500000013, 0.1273501249999999, 0.2337172499999998, 0.49045275000000094, 1.4560862499999987, 7.777412499999993],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0325924999999992e-05, 0.0015576575000000009, 0.008169837500000004, 0.02084326874999998, 0.041028731249999964, 0.07275475000000013, 0.1270711874999999, 0.2329756874999998, 0.49254256250000095, 1.4546606249999987, 7.786156249999992],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.873556874999995e-06, 0.0014731337500000006, 0.008223993750000004, 0.020859549999999984, 0.04076716249999997, 0.07239937500000013, 0.1273501249999999, 0.2337172499999998, 0.49045275000000094, 1.4560862499999987, 7.777412499999993],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.920405352128779e-06, 4.603162975063996e-05, 0.00015547860835578, 0.0002491329495721108, 0.0002845647718446538, 0.000462150247822611, 0.0005079239685351534, 0.0010034102008899442, 0.002317407798867092, 0.004913470403518267, 0.006237957773783014],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.593513543438705e-06, 3.638608615425684e-05, 0.00015646115732027556, 0.00015914344698651577, 0.00026474973441913, 0.00030762726025175395, 0.00044669170191811227, 0.00063020953856634, 0.001075002361916012, 0.002404639883381707, 0.0037461480216350197],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.920405352128779e-06, 4.603162975063996e-05, 0.00015547860835578, 0.0002491329495721108, 0.0002845647718446538, 0.000462150247822611, 0.0005079239685351534, 0.0010034102008899442, 0.002317407798867092, 0.004913470403518267, 0.006237957773783014],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.593513543438705e-06, 3.638608615425684e-05, 0.00015646115732027556, 0.00015914344698651577, 0.00026474973441913, 0.00030762726025175395, 0.00044669170191811227, 0.00063020953856634, 0.001075002361916012, 0.002404639883381707, 0.0037461480216350197],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5688165345961742, 0.9457366269542565, 1.0066288038164772, 1.000781127480305, 0.9936247419300835, 0.995115439198128, 1.00219512782943, 1.0031830038059228, 0.9957570925659851, 1.0009800395882718, 0.99887701328881],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.3796662625506948, 1.0295518300721693, 1.0190308079390538, 1.0119526813457276, 1.006935743884224, 1.0063521659798516, 1.0039971607925295, 1.0043069309577204, 1.0047049899344833, 1.0033777434537476, 1.0008011601069249],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8199817854999633, 0.969096117827094, 1.0257798771787412, 1.008416371687695, 1.0000775306552803, 0.9993437165305599, 1.00571041489573, 1.0058880480331938, 0.9979396498590231, 1.002633098619399, 0.9993581426036289],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6203337374493053, 0.9704481699278307, 0.9809691920609462, 0.9880473186542724, 0.9930642561157761, 0.9936478340201484, 0.9960028392074706, 0.9956930690422795, 0.9952950100655168, 0.9966222565462522, 0.9991988398930751],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3176512836923852, 0.922377136081419, 0.9874777304542134, 0.9931458832729146, 0.9871719532048867, 0.9908871618656959, 0.9986798407631304, 1.000477959578652, 0.9935745352729471, 0.9993269805571442, 0.9983958839739911],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3796662625506947, 0.029551830072169327, 0.019030807939053762, 0.011952681345727578, 0.0069357438842239105, 0.006352165979851554, 0.003997160792529431, 0.004306930957720501, 0.004704989934483206, 0.00337774345374775, 0.0008011601069248808],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3796662625506948, 0.029551830072169327, 0.019030807939053762, 0.011952681345727578, 0.0069357438842239105, 0.006352165979851554, 0.003997160792529542, 0.00430693095772039, 0.004704989934483317, 0.003377743453747639, 0.0008011601069248808],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.251165250903789, 0.023359490872837507, 0.01915107336226385, 0.007635244207390257, 0.006452788725196834, 0.004228277332432029, 0.003515287066299666, 0.002705044227270914, 0.0021825572930379566, 0.0016530590311275573, 0.0004811293148188067],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25116525090378905, 0.023359490872837507, 0.01915107336226396, 0.007635244207390146, 0.006452788725196723, 0.004228277332431918, 0.003515287066299999, 0.002705044227270914, 0.0021825572930379566, 0.0016530590311272242, 0.00048112931481891774],
  ],
}
ratio0_variation_vals = {
}