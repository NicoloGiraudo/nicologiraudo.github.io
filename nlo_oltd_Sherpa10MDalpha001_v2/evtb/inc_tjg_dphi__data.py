
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
  'curve0' : [1.0656525, 0.8838874999999999, 1.2196837500000002, 1.2312537499999998, 1.1009156249999998, 1.2693512500000006, 1.026079374999999, 1.0785937500000007, 1.0405962500000003, 1.3887731249999988, 1.5408843750000007, 1.3318537500000007, 1.4775481249999987, 1.7217699999999985, 2.3216481250000043, 2.8464193749999973, 3.436809999999997, 3.579518125000007, 2.8562206249999975, 2.0050368749999983],
}
yedges = {
  'curve0' : [1.0656525, 1.0656525, 0.8838874999999999, 1.2196837500000002, 1.2312537499999998, 1.1009156249999998, 1.2693512500000006, 1.026079374999999, 1.0785937500000007, 1.0405962500000003, 1.3887731249999988, 1.5408843750000007, 1.3318537500000007, 1.4775481249999987, 1.7217699999999985, 2.3216481250000043, 2.8464193749999973, 3.436809999999997, 3.579518125000007, 2.8562206249999975, 2.0050368749999983],
}
yups = {
  'curve0' : [0.1150486819513809, 0.11195395258765989, 0.2701505656573756, 0.22649322216680123, 0.18713315154255802, 0.1891459216782113, 0.1230167830267479, 0.12165054652055624, 0.08772586918919645, 0.16913861502847288, 0.2624270732032045, 0.14880173732604746, 0.13357655225562595, 0.188951268932627, 0.2655488126032581, 0.21656579182202323, 0.20050044809800283, 0.21759220387573672, 0.18489452229582123, 0.16720152978516659],
}
ydowns = {
  'curve0' : [0.1150486819513809, 0.11195395258765989, 0.2701505656573756, 0.22649322216680123, 0.18713315154255802, 0.1891459216782113, 0.1230167830267479, 0.12165054652055624, 0.08772586918919645, 0.16913861502847288, 0.2624270732032045, 0.14880173732604746, 0.13357655225562595, 0.188951268932627, 0.2655488126032581, 0.21656579182202323, 0.20050044809800283, 0.21759220387573672, 0.18489452229582123, 0.16720152978516659],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.1079607864208838, 1.126660861916997, 1.2214923054089846, 1.1839533257598616, 1.1699795581905363, 1.1490099148507642, 1.1198901235362497, 1.1127862520254324, 1.0843034646619152, 1.1217899540131675, 1.1703093869085437, 1.1117252831446751, 1.0904041973290217, 1.1097424562703655, 1.1143794400812816, 1.0760835854772888, 1.0583391133341684, 1.060788127417496, 1.0647339777177827, 1.0833907504993727],
}
ratio0_ymin = {
  'curve0' : [0.8920392135791161, 0.8733391380830028, 0.7785076945910154, 0.8160466742401383, 0.8300204418094638, 0.8509900851492358, 0.8801098764637502, 0.8872137479745678, 0.9156965353380848, 0.8782100459868325, 0.8296906130914563, 0.8882747168553248, 0.9095958026709782, 0.8902575437296346, 0.8856205599187184, 0.9239164145227112, 0.9416608866658316, 0.939211872582504, 0.9352660222822173, 0.9166092495006274],
}
ratio0_yerrs = {
  'curve0' : [
    [0.10796078642088391, 0.1266608619169972, 0.22149230540898457, 0.18395332575986167, 0.16997955819053623, 0.1490099148507642, 0.11989012353624984, 0.11278625202543224, 0.08430346466191518, 0.1217899540131675, 0.1703093869085437, 0.11172528314467522, 0.09040419732902183, 0.10974245627036538, 0.11437944008128165, 0.07608358547728877, 0.05833911333416841, 0.06078812741749595, 0.06473397771778266, 0.08339075049937261],
    [0.1079607864208838, 0.1266608619169971, 0.22149230540898457, 0.18395332575986156, 0.16997955819053634, 0.1490099148507642, 0.11989012353624973, 0.11278625202543235, 0.08430346466191518, 0.1217899540131675, 0.1703093869085437, 0.11172528314467511, 0.09040419732902172, 0.1097424562703655, 0.11437944008128165, 0.07608358547728877, 0.05833911333416841, 0.06078812741749595, 0.06473397771778266, 0.08339075049937272],
  ],
}
ratio0_variation_vals = {
}