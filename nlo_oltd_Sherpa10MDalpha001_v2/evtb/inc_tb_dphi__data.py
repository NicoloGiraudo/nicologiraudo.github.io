
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.873556874999995e-06, 0.0014731337500000006, 0.008223993750000004, 0.020859549999999984, 0.04076716249999997, 0.07239937500000013, 0.1273501249999999, 0.2337172499999998, 0.49045275000000094, 1.4560862499999987, 7.777412499999993],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.873556874999995e-06, 0.0014731337500000006, 0.008223993750000004, 0.020859549999999984, 0.04076716249999997, 0.07239937500000013, 0.1273501249999999, 0.2337172499999998, 0.49045275000000094, 1.4560862499999987, 7.777412499999993],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.593513543438705e-06, 3.638608615425684e-05, 0.00015646115732027556, 0.00015914344698651577, 0.00026474973441913, 0.00030762726025175395, 0.00044669170191811227, 0.00063020953856634, 0.001075002361916012, 0.002404639883381707, 0.0037461480216350197],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.593513543438705e-06, 3.638608615425684e-05, 0.00015646115732027556, 0.00015914344698651577, 0.00026474973441913, 0.00030762726025175395, 0.00044669170191811227, 0.00063020953856634, 0.001075002361916012, 0.002404639883381707, 0.0037461480216350197],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4415575772284843, 1.0246997844929266, 1.0190249606306272, 1.0076292847634065, 1.0064941908679352, 1.0042490319875241, 1.0035075874634447, 1.0026964613804346, 1.0021918571399915, 1.001651440554007, 1.0004816702240797],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5584424227715158, 0.9753002155070734, 0.9809750393693727, 0.9923707152365936, 0.9935058091320648, 0.9957509680124759, 0.9964924125365554, 0.9973035386195656, 0.9978081428600084, 0.9983485594459932, 0.9995183297759203],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4415575772284842, 0.024699784492926646, 0.019024960630627308, 0.007629284763406408, 0.0064941908679352345, 0.004249031987524132, 0.0035075874634445947, 0.002696461380434445, 0.002191857139991593, 0.001651440554006789, 0.00048167022407974436],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4415575772284843, 0.024699784492926646, 0.019024960630627197, 0.007629284763406519, 0.0064941908679352345, 0.004249031987524132, 0.0035075874634447057, 0.002696461380434556, 0.002191857139991482, 0.0016514405540069, 0.00048167022407974436],
  ],
}
ratio0_variation_vals = {
}