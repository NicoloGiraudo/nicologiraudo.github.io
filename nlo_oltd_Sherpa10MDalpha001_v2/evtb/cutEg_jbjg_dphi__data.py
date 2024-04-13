
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
  'curve0' : [2.503746875, 2.639140625, 3.697143750000001, 3.1637012499999995, 2.5921743749999995, 1.8894500000000012, 1.6615131249999986, 1.4731887500000007, 1.2375931250000005, 1.6045187499999984, 1.2588900000000007, 1.1152381250000005, 0.9866787499999992, 1.139474374999999, 1.3434356250000026, 1.0735143749999991, 1.3410368749999988, 1.1527975000000021, 0.9509912499999992, 0.6646762499999994],
}
yedges = {
  'curve0' : [2.503746875, 2.503746875, 2.639140625, 3.697143750000001, 3.1637012499999995, 2.5921743749999995, 1.8894500000000012, 1.6615131249999986, 1.4731887500000007, 1.2375931250000005, 1.6045187499999984, 1.2588900000000007, 1.1152381250000005, 0.9866787499999992, 1.139474374999999, 1.3434356250000026, 1.0735143749999991, 1.3410368749999988, 1.1527975000000021, 0.9509912499999992, 0.6646762499999994],
}
yups = {
  'curve0' : [0.11151914423653904, 0.18474676502580498, 0.23534955717506678, 0.2029884156177391, 0.2655610952539923, 0.17952482854051144, 0.18874980339393718, 0.16420114379930495, 0.11402937875280218, 0.26984312572307617, 0.1523308744559028, 0.11431484073601297, 0.09700235580257824, 0.13718367021989156, 0.23686510533423916, 0.12323778146838724, 0.2851047641876576, 0.20755797382900074, 0.14214216310176922, 0.16024831804889547],
}
ydowns = {
  'curve0' : [0.11151914423653904, 0.18474676502580498, 0.23534955717506678, 0.2029884156177391, 0.2655610952539923, 0.17952482854051144, 0.18874980339393718, 0.16420114379930495, 0.11402937875280218, 0.26984312572307617, 0.1523308744559028, 0.11431484073601297, 0.09700235580257824, 0.13718367021989156, 0.23686510533423916, 0.12323778146838724, 0.2851047641876576, 0.20755797382900074, 0.14214216310176922, 0.16024831804889547],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0445409020177165, 1.070002622549075, 1.063657129148702, 1.0641616889767134, 1.102447234188862, 1.0950143314406369, 1.113601150995384, 1.1114596780618267, 1.0921380189089223, 1.1681769849826165, 1.1210041182755466, 1.1025026298630285, 1.0983119944587623, 1.1203920625418995, 1.1763129553261913, 1.114798445496724, 1.212600242023664, 1.1800472102246928, 1.1494673721779978, 1.2410922882364093],
}
ratio0_ymin = {
  'curve0' : [0.9554590979822835, 0.9299973774509249, 0.936342870851298, 0.9358383110232866, 0.8975527658111379, 0.9049856685593632, 0.886398849004616, 0.8885403219381733, 0.9078619810910777, 0.8318230150173835, 0.8789958817244534, 0.8974973701369714, 0.901688005541238, 0.8796079374581006, 0.8236870446738088, 0.8852015545032759, 0.7873997579763361, 0.8199527897753072, 0.8505326278220022, 0.7589077117635907],
}
ratio0_yerrs = {
  'curve0' : [
    [0.044540902017716544, 0.07000262254907508, 0.06365712914870203, 0.06416168897671337, 0.10244723418886215, 0.09501433144063676, 0.11360115099538404, 0.11145967806182666, 0.09213801890892226, 0.16817698498261646, 0.12100411827554658, 0.1025026298630286, 0.09831199445876204, 0.12039206254189938, 0.17631295532619118, 0.11479844549672413, 0.2126002420236639, 0.18004721022469283, 0.14946737217799777, 0.24109228823640927],
    [0.044540902017716544, 0.07000262254907508, 0.06365712914870203, 0.06416168897671337, 0.10244723418886204, 0.09501433144063687, 0.11360115099538404, 0.11145967806182666, 0.09213801890892226, 0.16817698498261646, 0.12100411827554658, 0.1025026298630285, 0.09831199445876226, 0.12039206254189949, 0.1763129553261913, 0.11479844549672391, 0.2126002420236639, 0.18004721022469283, 0.14946737217799777, 0.24109228823640927],
  ],
}
ratio0_variation_vals = {
}