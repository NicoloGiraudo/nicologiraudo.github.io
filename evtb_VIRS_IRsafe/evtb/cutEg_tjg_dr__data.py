
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
  'curve0' : [0.02141974, 0.11521516, 0.17762104, 0.2209304, 0.2982238, 0.5072088, 0.4162362, 0.1789471, 0.09496076, 0.05141292, 0.0286138, 0.016310698, 0.0093584, 0.005876638, 0.002591798, 0.002589024, 0.0007841238, 0.0002938086, 0.00017906688, 0.0002356988],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yedges = {
  'curve0' : [0.02141974, 0.02141974, 0.11521516, 0.17762104, 0.2209304, 0.2982238, 0.5072088, 0.4162362, 0.1789471, 0.09496076, 0.05141292, 0.0286138, 0.016310698, 0.0093584, 0.005876638, 0.002591798, 0.002589024, 0.0007841238, 0.0002938086, 0.00017906688, 0.0002356988],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
yups = {
  'curve0' : [0.0001312521847437215, 0.00043818443605404334, 0.0004212030389254095, 0.00039228453958829425, 0.0006388304939496861, 0.0018380458100928823, 0.002229325458518787, 0.002098057196551133, 0.002076078033215515, 0.0019820343084820708, 0.0018659879956741416, 0.0016461646333219531, 0.0014980379167430977, 0.0014329715977645895, 0.0007721849519383294, 0.00154732116898852, 0.0006329928909553408, 0.0002824379577889629, 0.00023907044986781618, 0.0002452403718803248],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ydowns = {
  'curve0' : [0.0001312521847437215, 0.00043818443605404334, 0.0004212030389254095, 0.00039228453958829425, 0.0006388304939496861, 0.0018380458100928823, 0.002229325458518787, 0.002098057196551133, 0.002076078033215515, 0.0019820343084820708, 0.0018659879956741416, 0.0016461646333219531, 0.0014980379167430977, 0.0014329715977645895, 0.0007721849519383294, 0.00154732116898852, 0.0006329928909553408, 0.0002824379577889629, 0.00023907044986781618, 0.0002452403718803248],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
variation_yvals = {
}


# lists for ratio plot
ratio0_yvals = {
  'curve0' : [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ratio0_ymax = {
  'curve0' : [1.006127627354194, 1.0038031838523165, 1.0023713578015612, 1.0017756023597852, 1.002142117744961, 1.0036238444800107, 1.0053559144027329, 1.0117244548615267, 1.0218624833374912, 1.0385512884403778, 1.0652128691636253, 1.1009254559996116, 1.1600741490792332, 1.243842073948504, 1.2979340797154444, 1.5976465142804854, 1.8072614183568216, 1.9612991511785662, 2.3350902739122734, 2.0404820554042904],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ratio0_ymin = {
  'curve0' : [0.9938723726458061, 0.9961968161476836, 0.9976286421984388, 0.9982243976402149, 0.997857882255039, 0.9963761555199894, 0.9946440855972671, 0.9882755451384732, 0.9781375166625087, 0.9614487115596221, 0.9347871308363748, 0.8990745440003884, 0.8399258509207667, 0.7561579260514959, 0.7020659202845556, 0.4023534857195144, 0.19273858164317825, 0.038700848821433695, -0.3350902739122733, -0.040482055404290514],
  'curve1' : [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
}
ratio0_yerrs = {
  'curve0' : [
    [0.006127627354193921, 0.003803183852316372, 0.002371357801561169, 0.0017756023597851334, 0.0021421177449609807, 0.0036238444800106295, 0.005355914402732864, 0.011724454861526845, 0.0218624833374913, 0.03855128844037792, 0.06521286916362523, 0.10092545599961156, 0.16007414907923334, 0.2438420739485041, 0.2979340797154444, 0.5976465142804857, 0.8072614183568217, 0.9612991511785663, 1.3350902739122734, 1.0404820554042906],
    [0.006127627354193921, 0.003803183852316483, 0.002371357801561169, 0.0017756023597852444, 0.0021421177449609807, 0.0036238444800107406, 0.005355914402732864, 0.011724454861526734, 0.02186248333749119, 0.03855128844037781, 0.06521286916362534, 0.10092545599961156, 0.16007414907923323, 0.2438420739485041, 0.2979340797154444, 0.5976465142804854, 0.8072614183568216, 0.9612991511785662, 1.3350902739122734, 1.0404820554042904],
  ],
  'curve1' : [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ],
}
ratio0_variation_vals = {
}