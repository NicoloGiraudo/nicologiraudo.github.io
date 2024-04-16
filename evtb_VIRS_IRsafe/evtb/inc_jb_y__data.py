
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
  'curve0' : [0.0, 0.0, 1.348829e-07, 3.946215e-08, 1.444709e-06, 1.130477e-05, 6.283508e-05, 0.0004212896, 0.003414751, 0.02412597, 0.04850794, 0.01464603, 0.002587401, 0.0003811176, 0.0001582071, 7.958631e-06, 1.638043e-06, -2.705562e-06, 4.041439e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.25759e-07, 6.495742e-05, 0.004799906, 0.2105852, 0.8557747, 0.3931003, 0.06764228, 0.009472521, 0.001282176, 0.0001839175, 2.113816e-05, 3.39445e-06, 3.085863e-07, 0.0],
}
yedges = {
  'curve0' : [0.0, 0.0, 0.0, 1.348829e-07, 3.946215e-08, 1.444709e-06, 1.130477e-05, 6.283508e-05, 0.0004212896, 0.003414751, 0.02412597, 0.04850794, 0.01464603, 0.002587401, 0.0003811176, 0.0001582071, 7.958631e-06, 1.638043e-06, -2.705562e-06, 4.041439e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.25759e-07, 6.495742e-05, 0.004799906, 0.2105852, 0.8557747, 0.3931003, 0.06764228, 0.009472521, 0.001282176, 0.0001839175, 2.113816e-05, 3.39445e-06, 3.085863e-07, 0.0],
}
yups = {
  'curve0' : [0.0, 0.0, 1.0320242245218859e-07, 3.946527587639544e-08, 5.792805020022684e-07, 1.9870561139535037e-06, 4.338761343978256e-06, 1.5220890249916396e-05, 6.968378577545855e-05, 0.00031911533965010207, 0.0006405010538633016, 0.0006439225108660203, 0.0005396142140455531, 0.00035372234874262614, 0.00017664249205669624, 0.0001260191652091062, 1.5187376336945101e-05, 1.9264316754040357e-06, 3.4361519174797845e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.7793954543021825e-07, 3.165831644291907e-06, 2.7213832879622084e-05, 0.00018025498606141245, 0.00036337336170941313, 0.0002462776684963539, 0.00010216036413404172, 3.82301582523536e-05, 1.4065240844009746e-05, 5.327026375005102e-06, 1.8059551489447351e-06, 7.236991087461694e-07, 2.1820348301528094e-07, 0.0],
}
ydowns = {
  'curve0' : [0.0, 0.0, 1.0320242245218859e-07, 3.946527587639544e-08, 5.792805020022684e-07, 1.9870561139535037e-06, 4.338761343978256e-06, 1.5220890249916396e-05, 6.968378577545855e-05, 0.00031911533965010207, 0.0006405010538633016, 0.0006439225108660203, 0.0005396142140455531, 0.00035372234874262614, 0.00017664249205669624, 0.0001260191652091062, 1.5187376336945101e-05, 1.9264316754040357e-06, 3.4361519174797845e-07, 0.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.7793954543021825e-07, 3.165831644291907e-06, 2.7213832879622084e-05, 0.00018025498606141245, 0.00036337336170941313, 0.0002462776684963539, 0.00010216036413404172, 3.82301582523536e-05, 1.4065240844009746e-05, 5.327026375005102e-06, 1.8059551489447351e-06, 7.236991087461694e-07, 2.1820348301528094e-07, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.014733155428464484, 0.15418709600236985, 1.4056386541800556, 8.72856925545377, 17.641950987817665, 26.840058363938898, 26.142944213131244, 24.854588190101953, 8.104415035734807, 23.10918799979544, 12.904520821492477, -1.2546191881760609, 0.7635555058482882, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0, 1.0, 1.765126064550722, 2.000079212014435, 1.4009669089084849, 1.1757714764611313, 1.0690499851990043, 1.036129280784326, 1.0204066960593785, 1.0132270470223623, 1.013204045644142, 1.0439656692541268, 1.2085545356307559, 1.928118640395054, 2.1165269577452355, 16.83427667510985, 10.271659130404453, 0.28797356135101115, 1.8502298110845627, 1.0],
  'curve1' : [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.020747941204661762, 0.1617017169289057, 1.4136081467959511, 8.736040664315732, 17.64944199571677, 26.85687368307291, 26.182427990146888, 24.954898850780847, 8.19331901567003, 23.778527535075455, 14.007028599948072, -1.522104874605043, 1.3034708256521526, 1.0],
}
ratio0_ymin = {
  'curve0' : [1.0, 1.0, 0.234873935449278, -7.921201443502825e-05, 0.599033091091515, 0.8242285235388687, 0.9309500148009956, 0.9638707192156739, 0.9795933039406215, 0.9867729529776377, 0.986795954355858, 0.9560343307458732, 0.7914454643692441, 0.07188135960494567, -0.11652695774523544, -14.834276675109852, -8.271659130404453, 1.712026438648989, 0.1497701889154371, 1.0],
  'curve1' : [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.008718369652267202, 0.146672475075834, 1.39766916156416, 8.721097846591809, 17.634459979918557, 26.823243044804883, 26.103460436115604, 24.75427752942306, 8.015511055799584, 22.43984846451543, 11.802013043036883, -0.987133501747079, 0.22364018604442396, 1.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.0, 0.0, 0.765126064550722, 1.000079212014435, 0.40096690890848496, 0.17577147646113134, 0.0690499851990044, 0.03612928078432609, 0.020406696059378504, 0.013227047022362326, 0.013204045644142015, 0.043965669254126816, 0.20855453563075588, 0.9281186403950543, 1.1165269577452355, 15.834276675109852, 9.271659130404453, 0.712026438648989, 0.8502298110845629, 0.0],
    [0.0, 0.0, 0.7651260645507221, 1.0000792120144348, 0.40096690890848485, 0.17577147646113134, 0.0690499851990043, 0.03612928078432609, 0.020406696059378504, 0.013227047022362326, 0.013204045644142015, 0.043965669254126816, 0.20855453563075588, 0.9281186403950541, 1.1165269577452355, 15.834276675109852, 9.271659130404453, 0.7120264386489888, 0.8502298110845627, 0.0],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.006014785776197282, 0.007514620926535848, 0.007969492615895524, 0.007471408861961848, 0.007491007899108837, 0.016815319134014572, 0.03948377701563999, 0.10031066067889327, 0.08890397993522292, 0.6693395352800131, 1.1025077784555943, 0.26748568642898185, 0.5399153198038643, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.006014785776197278, 0.007514620926535848, 0.007969492615895524, 0.007471408861961848, 0.007491007899105284, 0.01681531913401102, 0.03948377701564354, 0.10031066067889327, 0.08890397993522292, 0.6693395352800131, 1.1025077784555943, 0.2674856864289821, 0.5399153198038643, 0.0],
  ],
}
ratio0_variation_vals = {
}