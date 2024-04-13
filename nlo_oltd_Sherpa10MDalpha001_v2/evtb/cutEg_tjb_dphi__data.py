
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
  'curve0' : [0.00171965875, 0.00167865625, 0.0017932050000000004, 0.0018752418749999997, 0.0020827824999999993, 0.002148873125000001, 0.002389600624999998, 0.0031127287500000013, 0.0034995156250000018, 0.004304191249999996, 0.005948116875000003, 0.007831512500000004, 0.01119393124999999, 0.017629099999999984, 0.029410700000000053, 0.05798629374999995, 0.13569624999999988, 0.33696481250000065, 1.178739374999999, 7.498174999999994],
}
yedges = {
  'curve0' : [0.00171965875, 0.00171965875, 0.00167865625, 0.0017932050000000004, 0.0018752418749999997, 0.0020827824999999993, 0.002148873125000001, 0.002389600624999998, 0.0031127287500000013, 0.0034995156250000018, 0.004304191249999996, 0.005948116875000003, 0.007831512500000004, 0.01119393124999999, 0.017629099999999984, 0.029410700000000053, 0.05798629374999995, 0.13569624999999988, 0.33696481250000065, 1.178739374999999, 7.498174999999994],
}
yups = {
  'curve0' : [0.00012006777057666223, 5.319279497732752e-05, 8.52868780205959e-05, 6.938451511324409e-05, 0.00011769850253932714, 5.778056888457402e-05, 6.495638560796e-05, 0.00010052032599181128, 7.485334620108846e-05, 9.074567396713732e-05, 0.0002122098202546245, 0.00017038384973347686, 0.00016069735724335966, 0.00022634502493428015, 0.0003700808610965994, 0.00037370233809811754, 0.0009007410143875977, 0.0015159824320799397, 0.004313156652905151, 0.0068350001143013825],
}
ydowns = {
  'curve0' : [0.00012006777057666223, 5.319279497732752e-05, 8.52868780205959e-05, 6.938451511324409e-05, 0.00011769850253932714, 5.778056888457402e-05, 6.495638560796e-05, 0.00010052032599181128, 7.485334620108846e-05, 9.074567396713732e-05, 0.0002122098202546245, 0.00017038384973347686, 0.00016069735724335966, 0.00022634502493428015, 0.0003700808610965994, 0.00037370233809811754, 0.0009007410143875977, 0.0015159824320799397, 0.004313156652905151, 0.0068350001143013825],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
}
ratio0_ymax = {
  'curve0' : [1.0698206958657712, 1.0316877234260007, 1.047561142212182, 1.0370003016881457, 1.0565102225217118, 1.0268887763602021, 1.0271829463586453, 1.0322933137016232, 1.0213896305152483, 1.0210830952196042, 1.0356768074189235, 1.0217561869094223, 1.0143557570307, 1.0128392841911544, 1.0125832047892978, 1.0064446667295082, 1.006637921198173, 1.0044989339415964, 1.0036591266435848, 1.0009115551603291],
}
ratio0_ymin = {
  'curve0' : [0.9301793041342288, 0.9683122765739993, 0.952438857787818, 0.9629996983118542, 0.9434897774782881, 0.9731112236397977, 0.9728170536413547, 0.9677066862983769, 0.9786103694847517, 0.9789169047803958, 0.9643231925810765, 0.9782438130905777, 0.9856442429693, 0.9871607158088456, 0.9874167952107022, 0.9935553332704917, 0.993362078801827, 0.9955010660584035, 0.9963408733564151, 0.9990884448396709],
}
ratio0_yerrs = {
  'curve0' : [
    [0.06982069586577122, 0.03168772342600068, 0.047561142212181995, 0.03700030168814583, 0.056510222521711895, 0.02688877636020226, 0.027182946358645266, 0.03229331370162314, 0.021389630515248337, 0.021083095219604164, 0.03567680741892354, 0.02175618690942227, 0.014355757030700023, 0.012839284191154432, 0.012583204789297753, 0.006444666729508275, 0.006637921198172969, 0.004498933941596506, 0.00365912664358492, 0.0009115551603291472],
    [0.06982069586577122, 0.03168772342600068, 0.047561142212181995, 0.03700030168814572, 0.056510222521711784, 0.02688877636020215, 0.027182946358645266, 0.03229331370162325, 0.021389630515248337, 0.021083095219604164, 0.03567680741892354, 0.02175618690942227, 0.014355757030700023, 0.012839284191154432, 0.012583204789297753, 0.006444666729508164, 0.00663792119817308, 0.004498933941596395, 0.003659126643584809, 0.0009115551603291472],
  ],
}
ratio0_variation_vals = {
}