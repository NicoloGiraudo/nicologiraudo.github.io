
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
  'curve0' : [0.510227625, 0.55737125, 0.7486775000000001, 0.6334737499999998, 0.4778209999999999, 0.39559337500000014, 0.3353498749999997, 0.29953581250000016, 0.27219818750000013, 0.2572204999999998, 0.24650175000000013, 0.2396143125000001, 0.23873581249999978, 0.23661981249999978, 0.23631231250000043, 0.2363344999999998, 0.2303813124999998, 0.22241081250000044, 0.2073083124999998, 0.1252178124999999],
  'curve1' : [0.5076833749999999, 0.558825875, 0.7499618750000001, 0.62937375, 0.48282999999999987, 0.3951929375000002, 0.34088987499999973, 0.30381962500000015, 0.27599168750000014, 0.25750106249999977, 0.24708081250000014, 0.24066525000000014, 0.23667568749999982, 0.2364981874999998, 0.23696525000000046, 0.23711493749999982, 0.23154899999999978, 0.21993243750000044, 0.20670693749999983, 0.1264293124999999],
}
yedges = {
  'curve0' : [0.510227625, 0.510227625, 0.55737125, 0.7486775000000001, 0.6334737499999998, 0.4778209999999999, 0.39559337500000014, 0.3353498749999997, 0.29953581250000016, 0.27219818750000013, 0.2572204999999998, 0.24650175000000013, 0.2396143125000001, 0.23873581249999978, 0.23661981249999978, 0.23631231250000043, 0.2363344999999998, 0.2303813124999998, 0.22241081250000044, 0.2073083124999998, 0.1252178124999999],
  'curve1' : [0.5076833749999999, 0.5076833749999999, 0.558825875, 0.7499618750000001, 0.62937375, 0.48282999999999987, 0.3951929375000002, 0.34088987499999973, 0.30381962500000015, 0.27599168750000014, 0.25750106249999977, 0.24708081250000014, 0.24066525000000014, 0.23667568749999982, 0.2364981874999998, 0.23696525000000046, 0.23711493749999982, 0.23154899999999978, 0.21993243750000044, 0.20670693749999983, 0.1264293124999999],
}
yups = {
  'curve0' : [0.005069863472027624, 0.007656994861726107, 0.009568825522236259, 0.007674742972080561, 0.005124754186178104, 0.0038506640052398777, 0.0025655522979954994, 0.0021409885640166332, 0.0016645918465572882, 0.0014169410273543485, 0.0017737120106925486, 0.0013349496713359653, 0.0019265066141529318, 0.0012932734629613324, 0.0013114670042075043, 0.0016522998886022461, 0.0012152096012622668, 0.0011984511488792547, 0.0020717670597825404, 0.0008263859097752084],
  'curve1' : [0.002068383653363176, 0.0032249388317842557, 0.003731150543063092, 0.0030967397170249874, 0.0024882230419015893, 0.0021302444475341333, 0.00187000240223776, 0.0017092641645968603, 0.0015756093811205248, 0.0014915954650138877, 0.0014685462624650278, 0.0014313242338827362, 0.0014279002831955726, 0.0014349937390978388, 0.001449890755582988, 0.0014552111369574507, 0.0014252847851394458, 0.0013659557665788476, 0.0013124843749069918, 0.0010268481813296444],
}
ydowns = {
  'curve0' : [0.005069863472027624, 0.007656994861726107, 0.009568825522236259, 0.007674742972080561, 0.005124754186178104, 0.0038506640052398777, 0.0025655522979954994, 0.0021409885640166332, 0.0016645918465572882, 0.0014169410273543485, 0.0017737120106925486, 0.0013349496713359653, 0.0019265066141529318, 0.0012932734629613324, 0.0013114670042075043, 0.0016522998886022461, 0.0012152096012622668, 0.0011984511488792547, 0.0020717670597825404, 0.0008263859097752084],
  'curve1' : [0.002068383653363176, 0.0032249388317842557, 0.003731150543063092, 0.0030967397170249874, 0.0024882230419015893, 0.0021302444475341333, 0.00187000240223776, 0.0017092641645968603, 0.0015756093811205248, 0.0014915954650138877, 0.0014685462624650278, 0.0014313242338827362, 0.0014279002831955726, 0.0014349937390978388, 0.001449890755582988, 0.0014552111369574507, 0.0014252847851394458, 0.0013659557665788476, 0.0013124843749069918, 0.0010268481813296444],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.9950135001020377, 0.9950135001020377, 1.0026097955357405, 1.0017155250424916, 0.9935277507552603, 1.010483005142093, 0.9989877547873496, 1.0165200598330328, 1.0143015035973368, 1.0139365365906414, 1.0010907470438786, 1.002349121253703, 1.0043859546161293, 0.9913706913997247, 0.9994859897879431, 1.0027630278468882, 1.0033022580283455, 1.005068499208242, 0.9888567692724022, 0.9970991274168036, 1.0096751410666913],
}
ratio0_ymax = {
  'curve0' : [1.0099364738865866, 1.0137376925374715, 1.0127809711420956, 1.0121153291230782, 1.0107252594301592, 1.00973389406544, 1.0076503749941623, 1.0071476881049628, 1.0061153671221903, 1.005508662907328, 1.0071955351663529, 1.005571243459574, 1.0080696171805097, 1.0054656178166033, 1.0055497193114198, 1.0069913613484374, 1.0052747750591198, 1.0053884572220573, 1.0099936516524515, 1.0065995874969882],
  'curve1' : [0.9990673449979568, 1.0083957754042467, 1.006699180278642, 0.9984162559490825, 1.0156904427429971, 1.004372689374624, 1.0220963326801236, 1.0200078802416885, 1.01972500048745, 1.0068896451294274, 1.0083066702871888, 1.0103594051122584, 0.9973517809909461, 1.0055505442474215, 1.0088985132993569, 1.0094596795514725, 1.0112551328794928, 0.994998358124243, 1.0034302019360997, 1.0178756371528983],
}
ratio0_ymin = {
  'curve0' : [0.9900635261134133, 0.9862623074625286, 0.9872190288579045, 0.9878846708769218, 0.9892747405698409, 0.99026610593456, 0.9923496250058376, 0.9928523118950372, 0.9938846328778098, 0.994491337092672, 0.992804464833647, 0.994428756540426, 0.9919303828194903, 0.9945343821833967, 0.9944502806885803, 0.9930086386515627, 0.9947252249408803, 0.9946115427779427, 0.9900063483475485, 0.9934004125030118],
  'curve1' : [0.9909596552061187, 0.9968238156672341, 0.9967318698063411, 0.9886392455614382, 1.0052755675411889, 0.9936028202000752, 1.010943786985942, 1.0085951269529854, 1.0081480726938328, 0.9952918489583299, 0.9963915722202173, 0.9984125041200004, 0.9853896018085031, 0.9934214353284646, 0.9966275423944194, 0.9971448365052185, 0.9988818655369911, 0.9827151804205614, 0.9907680528975076, 1.0014746449804843],
}
ratio0_yerrs = {
  'curve0' : [
    [0.009936473886586694, 0.013737692537471369, 0.012780971142095532, 0.012115329123078222, 0.010725259430159118, 0.009733894065440007, 0.007650374994162434, 0.007147688104962802, 0.006115367122190185, 0.005508662907327988, 0.007195535166352962, 0.005571243459574049, 0.008069617180509692, 0.005465617816603263, 0.005549719311419676, 0.006991361348437253, 0.005274775059119663, 0.005388457222057275, 0.009993651652451474, 0.006599587496988191],
    [0.009936473886586583, 0.01373769253747148, 0.012780971142095643, 0.012115329123078222, 0.010725259430159229, 0.009733894065439896, 0.007650374994162323, 0.007147688104962802, 0.006115367122190296, 0.005508662907327988, 0.007195535166352851, 0.005571243459574049, 0.008069617180509692, 0.005465617816603263, 0.005549719311419787, 0.006991361348437364, 0.005274775059119774, 0.005388457222057275, 0.009993651652451474, 0.006599587496988191],
  ],
  'curve1' : [
    [0.004053844895918979, 0.005785979868506375, 0.004983655236150519, 0.0048885051938221125, 0.005207437600904141, 0.005384934587274404, 0.005576272847090946, 0.005706376644351474, 0.005788463896808649, 0.005798898085548676, 0.005957549033485665, 0.0059734504961289625, 0.005981089591221567, 0.006064554459478511, 0.006135485452468781, 0.006157421523127038, 0.00618663367125083, 0.006141588851840796, 0.006331074519296043, 0.008200496086206988],
    [0.00405384489591909, 0.0057859798685062636, 0.004983655236150408, 0.0048885051938221125, 0.005207437600904141, 0.005384934587274515, 0.005576272847090724, 0.005706376644351696, 0.005788463896808649, 0.005798898085548787, 0.005957549033485776, 0.0059734504961290735, 0.005981089591221456, 0.0060645544594783996, 0.00613548545246867, 0.006157421523127038, 0.00618663367125083, 0.006141588851840796, 0.006331074519296043, 0.008200496086206988],
  ],
}
ratio0_variation_vals = {
}