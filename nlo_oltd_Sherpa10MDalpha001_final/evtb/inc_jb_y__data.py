
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
  'curve0' : [0.0, 0.0, 1.331136e-07, 0.0, 2.037674e-06, 9.979257e-06, 6.311645e-05, 0.0004749832, 0.008247919, 0.2345259, 0.9044931, 0.4089457, 0.06974854, 0.00984515, 0.001478914, 0.0001782585, 2.71781e-05, 2.243686e-06, 6.627404e-08, 0.0],
  'curve1' : [0.0, 0.0, 1.556175e-08, 2.211382e-08, 8.109232e-07, 6.013851e-06, 4.901639e-05, 0.0004691709, 0.007860349, 0.2337222, 0.9037681, 0.4093139, 0.07004007, 0.009897455, 0.00123785, 0.0001794748, 6.550632e-05, -1.096677e-05, 3.411639e-07, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 1.331136e-07, 0.0, 2.037674e-06, 9.979257e-06, 6.311645e-05, 0.0004749832, 0.008247919, 0.2345259, 0.9044931, 0.4089457, 0.06974854, 0.00984515, 0.001478914, 0.0001782585, 2.71781e-05, 2.243686e-06, 6.627404e-08, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 1.556175e-08, 2.211382e-08, 8.109232e-07, 6.013851e-06, 4.901639e-05, 0.0004691709, 0.007860349, 0.2337222, 0.9037681, 0.4093139, 0.07004007, 0.009897455, 0.00123785, 0.0001794748, 6.550632e-05, -1.096677e-05, 3.411639e-07, 0.0],
}
yups = {
  'curve0' : [0.0, 0.0, 1.0184876042446466e-07, 0.0, 7.235222871480878e-07, 1.8117607457939913e-06, 4.252110064426837e-06, 1.391149165258708e-05, 6.897864887050196e-05, 0.0004067688532815658, 0.0006456269820879545, 0.0006360786901005252, 0.0005811660692091375, 0.00036419967051055935, 0.0001732770902341103, 0.00012202208816439751, 1.5876536146149763e-05, 1.895211597685071e-06, 6.627404469322812e-08, 0.0],
  'curve1' : [0.0, 0.0, 2.200763731071557e-08, 3.1273666238546447e-08, 4.043418108481981e-07, 2.1342457684156245e-06, 5.253032457542976e-06, 2.8557860564124895e-05, 7.66647767883009e-05, 0.00029258236447195516, 0.0005165295732095114, 0.0004369002174410079, 0.0002862816096084413, 0.00016861936424978003, 0.00011130251569483953, 6.966052684268186e-05, 2.6069867663645705e-05, 2.139986214908872e-05, 3.5975783521696926e-07, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.0, 1.0184876042446466e-07, 0.0, 7.235222871480878e-07, 1.8117607457939913e-06, 4.252110064426837e-06, 1.391149165258708e-05, 6.897864887050196e-05, 0.0004067688532815658, 0.0006456269820879545, 0.0006360786901005252, 0.0005811660692091375, 0.00036419967051055935, 0.0001732770902341103, 0.00012202208816439751, 1.5876536146149763e-05, 1.895211597685071e-06, 6.627404469322812e-08, 0.0],
  'curve1' : [0.0, 0.0, 2.200763731071557e-08, 3.1273666238546447e-08, 4.043418108481981e-07, 2.1342457684156245e-06, 5.253032457542976e-06, 2.8557860564124895e-05, 7.66647767883009e-05, 0.00029258236447195516, 0.0005165295732095114, 0.0004369002174410079, 0.0002862816096084413, 0.00016861936424978003, 0.00011130251569483953, 6.966052684268186e-05, 2.6069867663645705e-05, 2.139986214908872e-05, 3.5975783521696926e-07, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 0.11690578573489112, nan, 0.397965130830545, 0.6026351460835211, 0.7766024546691076, 0.987763146149169, 0.9530099653015508, 0.9965730863840624, 0.9991984460688533, 1.0009003640336602, 1.0041797290667303, 1.0053127682158218, 0.8369993116570673, 1.0068232370405898, 2.410261202953849, -4.887836354997981, 5.147775810860481, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.7651266318728114, 1.0, 1.3550726402496611, 1.1815526692812892, 1.0673692843058638, 1.0292883867315457, 1.0083631578911603, 1.0017344304116584, 1.0007137997869613, 1.0015554111220646, 1.008332304435464, 1.036992800567849, 1.1171650888652824, 1.6845232522679003, 1.5841665218006324, 1.8446866440692107, 2.0000000708154824, 1.0],
  'curve1' : [1.0, 1.0, 0.2822355289821294, nan, 0.5963981534083459, 0.816503349739928, 0.859830083243639, 1.047887084351878, 0.9623050101229538, 0.9978206345843762, 0.9997695168412113, 1.0019687215624007, 1.0082842108180106, 1.0224399185639406, 0.9122589384472927, 1.3976069968202463, 3.369484535844879, 4.649978717649761, 10.576112988086576, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 0.23487336812718856, 1.0, 0.644927359750339, 0.8184473307187107, 0.9326307156941362, 0.9707116132684543, 0.9916368421088396, 0.9982655695883416, 0.9992862002130387, 0.9984445888779353, 0.991667695564536, 0.963007199432151, 0.8828349111347176, 0.31547674773209966, 0.4158334781993678, 0.15531335593078924, -7.081548255745082e-08, 1.0],
  'curve1' : [1.0, 1.0, -0.04842395751234711, nan, 0.19953210825274403, 0.3887669424271141, 0.6933748260945762, 0.9276392079464602, 0.9437149204801478, 0.9953255381837487, 0.9986273752964953, 0.9998320065049198, 1.00007524731545, 0.9881856178677033, 0.7617396848668418, 0.6160394772609337, 1.4510378700628186, -14.425651427645724, -0.28056136636561285, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.7651266318728114, 0.0, 0.355072640249661, 0.18155266928128933, 0.06736928430586375, 0.029288386731545657, 0.008363157891160378, 0.0017344304116584386, 0.0007137997869612889, 0.0015554111220646982, 0.008332304435463955, 0.03699280056784904, 0.11716508886528243, 0.6845232522679003, 0.5841665218006322, 0.8446866440692108, 1.0000000708154826, 0.0],
    [0.0, 0.0, 0.7651266318728114, 0.0, 0.3550726402496611, 0.18155266928128921, 0.06736928430586375, 0.029288386731545657, 0.008363157891160267, 0.0017344304116584386, 0.0007137997869612889, 0.0015554111220645872, 0.008332304435463955, 0.03699280056784904, 0.11716508886528243, 0.6845232522679003, 0.5841665218006324, 0.8446866440692107, 1.0000000708154824, 0.0],
  ],
  'curve1' : [
    [0.0, 0.0, 0.16532974324723823, nan, 0.198433022577801, 0.21386820365640696, 0.08322762857453136, 0.06012393820270889, 0.009295044821402976, 0.0012475482003136973, 0.0005710707723580732, 0.00106835752874046, 0.004104481751280309, 0.017127150348118514, 0.07525962679022546, 0.3907837597796562, 0.9592233328910305, 9.537815072647742, 5.428337177226094, 0.0],
    [0.0, 0.0, 0.16532974324723826, nan, 0.19843302257780088, 0.2138682036564069, 0.08322762857453136, 0.06012393820270889, 0.009295044821402976, 0.0012475482003138083, 0.0005710707723579622, 0.00106835752874046, 0.004104481751280309, 0.017127150348118736, 0.07525962679022535, 0.3907837597796564, 0.95922333289103, 9.537815072647742, 5.428337177226095, 0.0],
  ],
}
ratio0_variation_vals = {
}