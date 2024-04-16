
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
  'curve0' : [0.0, 0.0, 1.556175e-08, 2.211382e-08, 8.109232e-07, 6.013851e-06, 4.901639e-05, 0.0004691709, 0.007860349, 0.2337222, 0.9037681, 0.4093139, 0.07004007, 0.009897455, 0.00123785, 0.0001794748, 6.550632e-05, -1.096677e-05, 3.411639e-07, 0.0],
  'curve1' : [0.0, 0.0, 1.331136e-07, 0.0, 2.037674e-06, 9.979257e-06, 6.311645e-05, 0.0004749832, 0.008247919, 0.2345259, 0.9044931, 0.4089457, 0.06974854, 0.00984515, 0.001478914, 0.0001782585, 2.71781e-05, 2.243686e-06, 6.627404e-08, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 1.556175e-08, 2.211382e-08, 8.109232e-07, 6.013851e-06, 4.901639e-05, 0.0004691709, 0.007860349, 0.2337222, 0.9037681, 0.4093139, 0.07004007, 0.009897455, 0.00123785, 0.0001794748, 6.550632e-05, -1.096677e-05, 3.411639e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 1.331136e-07, 0.0, 2.037674e-06, 9.979257e-06, 6.311645e-05, 0.0004749832, 0.008247919, 0.2345259, 0.9044931, 0.4089457, 0.06974854, 0.00984515, 0.001478914, 0.0001782585, 2.71781e-05, 2.243686e-06, 6.627404e-08, 0.0],
}
yups = {
  'curve0' : [0.0, 0.0, 2.200763731071557e-08, 3.1273666238546447e-08, 4.043418108481981e-07, 2.1342457684156245e-06, 5.253032457542976e-06, 2.8557860564124895e-05, 7.66647767883009e-05, 0.00029258236447195516, 0.0005165295732095114, 0.0004369002174410079, 0.0002862816096084413, 0.00016861936424978003, 0.00011130251569483953, 6.966052684268186e-05, 2.6069867663645705e-05, 2.139986214908872e-05, 3.5975783521696926e-07, 0.0],
  'curve1' : [0.0, 0.0, 1.0184876042446466e-07, 0.0, 7.235222871480878e-07, 1.8117607457939913e-06, 4.252110064426837e-06, 1.391149165258708e-05, 6.897864887050196e-05, 0.0004067688532815658, 0.0006456269820879545, 0.0006360786901005252, 0.0005811660692091375, 0.00036419967051055935, 0.0001732770902341103, 0.00012202208816439751, 1.5876536146149763e-05, 1.895211597685071e-06, 6.627404469322812e-08, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.0, 2.200763731071557e-08, 3.1273666238546447e-08, 4.043418108481981e-07, 2.1342457684156245e-06, 5.253032457542976e-06, 2.8557860564124895e-05, 7.66647767883009e-05, 0.00029258236447195516, 0.0005165295732095114, 0.0004369002174410079, 0.0002862816096084413, 0.00016861936424978003, 0.00011130251569483953, 6.966052684268186e-05, 2.6069867663645705e-05, 2.139986214908872e-05, 3.5975783521696926e-07, 0.0],
  'curve1' : [0.0, 0.0, 1.0184876042446466e-07, 0.0, 7.235222871480878e-07, 1.8117607457939913e-06, 4.252110064426837e-06, 1.391149165258708e-05, 6.897864887050196e-05, 0.0004067688532815658, 0.0006456269820879545, 0.0006360786901005252, 0.0005811660692091375, 0.00036419967051055935, 0.0001732770902341103, 0.00012202208816439751, 1.5876536146149763e-05, 1.895211597685071e-06, 6.627404469322812e-08, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 8.553896573328835, 0.0, 2.512782961444438, 1.659378823984831, 1.2876601071600744, 1.0123884494967612, 1.0493069709754617, 1.0034386977360303, 1.0008021969352536, 0.9991004458925046, 0.995837668351845, 0.9947153081271903, 1.1947441127761846, 0.9932230040094765, 0.4148927920237314, -0.20458950082841165, 0.1942586539783371, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 2.4142135242318874, 2.414213656371737, 1.4986191181214177, 1.3548883682711168, 1.10716889712896, 1.0608687805746795, 1.0097533553266276, 1.0012518381414859, 1.0005715288835815, 1.0010673964833372, 1.0040873975369877, 1.0170366386358696, 1.0899159960373546, 1.388135419806468, 1.3979748467574686, -0.9513368247067022, 2.054501473388507, 1.0],
  'curve1' : [1.0, 1.0, 15.098710647868307, 0.0, 3.405003441938877, 1.9606434788281237, 1.3744088470086606, 1.0420396739281723, 1.0580824908500246, 1.0051790923296187, 1.0015165693302164, 1.0006544578381056, 1.004135290972855, 1.031512613142526, 1.3347264129208791, 1.6731072449413371, 0.6572592712603877, -0.37740351969495767, 0.38851732171319453, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, -0.414213524231887, -0.414213656371737, 0.5013808818785822, 0.6451116317288831, 0.8928311028710401, 0.9391312194253205, 0.9902466446733725, 0.9987481618585142, 0.9994284711164186, 0.9989326035166628, 0.9959126024630123, 0.9829633613641305, 0.9100840039626453, 0.6118645801935321, 0.6020251532425313, 2.9513368247067024, -0.05450147338850705, 1.0],
  'curve1' : [1.0, 1.0, 2.00908249878936, 0.0, 1.620562480949999, 1.3581141691415382, 1.2009113673114884, 0.9827372250653502, 1.0405314511008985, 1.001698303142442, 1.000087824540291, 0.9975464339469036, 0.9875400457308348, 0.9579180031118547, 1.05476181263149, 0.3133387630776158, 0.17252631278707514, -0.0317754819618656, -1.3756520322436807e-08, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 1.414213524231887, 1.4142136563717371, 0.4986191181214178, 0.3548883682711169, 0.10716889712895994, 0.06086878057467948, 0.009753355326627466, 0.0012518381414857727, 0.0005715288835813626, 0.0010673964833372018, 0.004087397536987725, 0.01703663863586946, 0.08991599603735467, 0.38813541980646793, 0.39797484675746875, 1.9513368247067024, 1.054501473388507, 0.0],
    [0.0, 0.0, 1.4142135242318874, 1.4142136563717371, 0.4986191181214177, 0.3548883682711168, 0.10716889712895994, 0.06086878057467948, 0.009753355326627577, 0.0012518381414858837, 0.0005715288835814736, 0.0010673964833372018, 0.004087397536987725, 0.017036638635869572, 0.08991599603735456, 0.38813541980646793, 0.39797484675746864, 1.9513368247067022, 1.0545014733885072, 0.0],
  ],
  'curve1' : [
    [0.0, 0.0, 6.544814074539476, 0.0, 0.8922204804944389, 0.3012646548432929, 0.086748739848586, 0.029651224431410994, 0.008775519874563154, 0.0017403945935883236, 0.0007143723949625258, 0.0015540119456010082, 0.008297622621010192, 0.036797305015335624, 0.1399823001446947, 0.6798842409318606, 0.24236647923665627, 0.17281401886654604, 0.19425866773485742, 0.0],
    [0.0, 0.0, 6.544814074539472, 0.0, 0.8922204804944389, 0.3012646548432927, 0.08674873984858622, 0.029651224431411105, 0.008775519874562931, 0.0017403945935883236, 0.0007143723949627478, 0.0015540119456010082, 0.00829762262100997, 0.036797305015335735, 0.13998230014469448, 0.6798842409318606, 0.24236647923665633, 0.17281401886654602, 0.19425866773485742, 0.0],
  ],
}
ratio0_variation_vals = {
}