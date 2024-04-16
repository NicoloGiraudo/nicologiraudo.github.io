
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
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7322855, 0.2499494, 0.07273791, 0.0169017, 0.003047034, 0.0004641645, 7.26669e-05, 1.042284e-05, 1.231733e-06, 1.026001e-07],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7312645, 0.249899, 0.07267484, 0.0170008, 0.00312325, 0.0004613486, 6.814332e-05, 1.138318e-05, 1.192077e-06, 4.380184e-08],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7322855, 0.2499494, 0.07273791, 0.0169017, 0.003047034, 0.0004641645, 7.26669e-05, 1.042284e-05, 1.231733e-06, 1.026001e-07],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7312645, 0.249899, 0.07267484, 0.0170008, 0.00312325, 0.0004613486, 6.814332e-05, 1.138318e-05, 1.192077e-06, 4.380184e-08],
}
yups = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009070050716506496, 0.0006023704840046531, 0.00031752842392453624, 0.00015614762246028596, 6.400112499011248e-05, 2.3477193188283817e-05, 9.505501564883359e-06, 3.88606613428027e-06, 8.994172001913239e-07, 6.557324149376787e-08],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0020511630846912197, 0.0007722829792245845, 0.0002858533889951281, 0.00011452379665379592, 4.9465088699000633e-05, 1.787702995466529e-05, 7.038400386451456e-06, 2.5674382173676544e-06, 5.555051754934422e-07, 4.380183786098478e-08],
}
ydowns = {
  'curve0' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009070050716506496, 0.0006023704840046531, 0.00031752842392453624, 0.00015614762246028596, 6.400112499011248e-05, 2.3477193188283817e-05, 9.505501564883359e-06, 3.88606613428027e-06, 8.994172001913239e-07, 6.557324149376787e-08],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0020511630846912197, 0.0007722829792245845, 0.0002858533889951281, 0.00011452379665379592, 4.9465088699000633e-05, 1.787702995466529e-05, 7.038400386451456e-06, 2.5674382173676544e-06, 5.555051754934422e-07, 4.380183786098478e-08],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9986057350582525, 0.9997983591878997, 0.999132914322119, 1.005863315524474, 1.025013176748274, 0.9939334007663231, 0.9377490989707832, 1.092138035314751, 0.9678047109235524, 0.4269181024190035],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0012385948808908, 1.0024099697138886, 1.0043653773379595, 1.0092385749634822, 1.0210044013260478, 1.0505794673834037, 1.130809234532963, 1.3728413881706203, 1.7302046792538026, 1.6391147912503774],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0014067779365987, 1.0028881164716723, 1.003062823622443, 1.0126391899426566, 1.041247025369261, 1.032447828204581, 1.03460750887201, 1.3384661203057566, 1.4187995088979852, 0.8538361839899258],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.998761405119109, 0.9975900302861113, 0.9956346226620406, 0.9907614250365178, 0.9789955986739522, 0.9494205326165964, 0.8691907654670371, 0.6271586118293796, 0.2697953207461975, 0.3608852087496224],
  'curve1' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9958046921799062, 0.9967086019041271, 0.9952030050217949, 0.9990874411062913, 1.0087793281272868, 0.9554189733280651, 0.8408906890695563, 0.8458099503237453, 0.5168099129491195, 2.0848081239633157e-08],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001238594880890953, 0.0024099697138887377, 0.004365377337959386, 0.009238574963482238, 0.02100440132604775, 0.050579467383403576, 0.1308092345329629, 0.3728413881706204, 0.7302046792538025, 0.6391147912503776],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001238594880890842, 0.0024099697138886267, 0.004365377337959497, 0.009238574963482238, 0.02100440132604775, 0.05057946738340369, 0.130809234532963, 0.3728413881706203, 0.7302046792538026, 0.6391147912503774],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0028010428783462604, 0.0030897572837725873, 0.003929909300324108, 0.006775874418182726, 0.0162338486209872, 0.03851442743825795, 0.09685840990122685, 0.24632808499100567, 0.45099479797443287, 0.42691808157092226],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0028010428783462604, 0.0030897572837725873, 0.003929909300323997, 0.006775874418182504, 0.01623384862098698, 0.03851442743825795, 0.09685840990122674, 0.24632808499100567, 0.45099479797443287, 0.42691808157092226],
  ],
}
ratio0_variation_vals = {
}