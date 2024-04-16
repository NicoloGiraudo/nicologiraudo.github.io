
from numpy import nan

xpoints  = [0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25, 6.75, 7.25, 7.75, 8.25, 8.75, 9.25, 9.75]
xedges   = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
xmins    = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]
xmaxs    = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
xerrs = [
  [abs(xpoints[i] - xmins[i])   for i in range(len(xpoints))],
  [abs(xmaxs[i]   - xpoints[i]) for i in range(len(xpoints))]
]

yvals = {
  'curve0' : [0.2032604, 0.6448896, 0.40525, 0.3272028, 0.308775, 0.3058932, 0.1804538, 0.04738838, 0.015625692, 0.005460674, 0.0018680892, 0.0006642558, 0.0002457722, 7.680116e-05, 3.21618e-05, 1.5591664e-05, 5.17497e-06, 1.6212026e-06, 2.749628e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.2032604, 0.2032604, 0.6448896, 0.40525, 0.3272028, 0.308775, 0.3058932, 0.1804538, 0.04738838, 0.015625692, 0.005460674, 0.0018680892, 0.0006642558, 0.0002457722, 7.680116e-05, 3.21618e-05, 1.5591664e-05, 5.17497e-06, 1.6212026e-06, 2.749628e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.002415420460292576, 0.0043075375796387426, 0.0020014934424074436, 0.0010599699995754597, 0.0009688135011445702, 0.0010385915462779388, 0.0005665412606333276, 0.0002848533657866798, 0.00016436614006540398, 8.888637690895045e-05, 4.877656814496075e-05, 2.8080662385349816e-05, 1.6337982739616297e-05, 8.695739186521179e-06, 5.980787573555844e-06, 4.516685953218355e-06, 1.633572036979086e-06, 9.249957837741749e-07, 1.5637274698616764e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.002415420460292576, 0.0043075375796387426, 0.0020014934424074436, 0.0010599699995754597, 0.0009688135011445702, 0.0010385915462779388, 0.0005665412606333276, 0.0002848533657866798, 0.00016436614006540398, 8.888637690895045e-05, 4.877656814496075e-05, 2.8080662385349816e-05, 1.6337982739616297e-05, 8.695739186521179e-06, 5.980787573555844e-06, 4.516685953218355e-06, 1.633572036979086e-06, 9.249957837741749e-07, 1.5637274698616764e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0118833794496744, 1.0066794961178451, 1.0049389104069277, 1.003239489391825, 1.0031376034366273, 1.0033952750380786, 1.0031395363280426, 1.0060110382711265, 1.0105189671001709, 1.0162775468575767, 1.0261104063686899, 1.0422738685689306, 1.0664761219520202, 1.1132240605027475, 1.1859593546864866, 1.2896859471329267, 1.3156679240612188, 1.5705614978499138, 1.5687051011488375, 1.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
}
ratio0_ymin = {
  'curve0' : [0.9881166205503257, 0.9933205038821548, 0.9950610895930723, 0.9967605106081749, 0.9968623965633727, 0.9966047249619215, 0.9968604636719575, 0.9939889617288736, 0.989481032899829, 0.9837224531424235, 0.9738895936313101, 0.9577261314310694, 0.9335238780479798, 0.8867759394972526, 0.8140406453135134, 0.7103140528670734, 0.6843320759387811, 0.42943850215008605, 0.4312948988511623, 1.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.011883379449674325, 0.0066794961178452406, 0.004938910406927732, 0.0032394893918250567, 0.0031376034366272787, 0.00339527503807846, 0.003139536328042536, 0.006011038271126368, 0.010518967100170973, 0.01627754685757654, 0.026110406368689887, 0.04227386856893056, 0.06647612195202024, 0.11322406050274736, 0.1859593546864866, 0.2896859471329266, 0.3156679240612189, 0.570561497849914, 0.5687051011488378, 0.0],
    [0.011883379449674436, 0.0066794961178451295, 0.004938910406927732, 0.0032394893918250567, 0.0031376034366272787, 0.0033952750380785712, 0.003139536328042647, 0.006011038271126479, 0.010518967100170862, 0.016277546857576652, 0.026110406368689887, 0.04227386856893056, 0.06647612195202024, 0.11322406050274747, 0.1859593546864866, 0.2896859471329267, 0.3156679240612188, 0.5705614978499138, 0.5687051011488375, 0.0],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}