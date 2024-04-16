#! /usr/bin/env python

# This Python script was auto-generated using YODA v2.0.0.
# Analysis object: /evtb/cutEg_jbjg_dphi
# Timestamp: 16-04-2024 (10:05:22)

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg') # comment out for interactive use
import os
import numpy as np

plotDir = os.path.split(os.path.realpath(__file__))[0]
if 'YODA_USER_PLOT_PATH' in globals():
    plot_outdir = globals()['YODA_USER_PLOT_PATH']
else:
    plot_outdir = plotDir

#plot style
plt.style.use(os.path.join(plotDir, '../default.mplstyle'))
# plot metadata
figW, figH = plt.rcParams['figure.figsize']
ax_xLabel = r''
ax_yLabel = r''
ax_title  = r''
ax_xScale = 'linear'
ax_yScale = 'log'
xLims = (0.0, 3.2)
yLims = (0.09000000000000001, 1.1)

# TeX-friendly labels for the legend
labels = [ r"Sherpa VIRS, 10M, Dalpha=0.01", r"OLTD, nb=10M, nq=1" ]

# Create figure and axis objects
fig, (ax, ratio0_ax) = plt.subplots(2, 1, sharex=True,
                  figsize=(figW,figH), gridspec_kw={'height_ratios': (2, 1)})
ratio0_ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
ratio0_ax.set_ylim(0.5, 1.4999)
ratio0_ax.set_ylabel('Ratio')

# LineColor map: curve index -> color
linecolors = {0: '#EE3311', 1: '#3366FF'}
# the numerical data is stored in a separate file
dataf = dict()
prefix = os.path.split(__file__)[0]
if prefix:    prefix = prefix + '/'
exec(open(prefix+'cutEg_jbjg_dphi__data.py').read(), dataf)


legend_handles = [] # keep track of handles for the legend

# style options for curves
# starts at zorder>=5 to draw curve on top of legend
styles = {
  'curve0': {
    'color' : linecolors[0],
    'linestyle' : '-',
    'marker' : 'o',
    'zorder' : 5,
    'histstyle' : True,
  },
  'curve1': {
    'color' : linecolors[1],
    'linestyle' : '-',
    'marker' : 'o',
    'zorder' : 6,
    'histstyle' : True,
  },
}
# curve from input yoda files in main panel
for label in dataf['yvals'].keys():
    if all(np.isnan(v) for v in dataf['yvals'][label]):
        continue
    tmp = None
    if styles[label]['histstyle']: # draw as histogram
        tmp, = ax.plot(dataf['xedges'], dataf['yedges'][label],
                       color=styles[label]['color'],
                       linestyle=styles[label]['linestyle'],
                       drawstyle='steps-pre', solid_joinstyle='miter',
                       zorder=styles[label]['zorder'], label=label)
        ax.errorbar(dataf['xpoints'], dataf['yvals'][label], color=styles[label]['color'],
                    xerr=dataf['xerrs'], yerr=[dataf['ydowns'][label], dataf['yups'][label]],
                    linestyle='none', zorder=styles[label]['zorder'])
    else: # draw as scatter
        tmp = ax.errorbar(dataf['xpoints'], dataf['yvals'][label],
                          xerr=dataf['xerrs'],
                          yerr=[ dataf['ydowns'][label],
                          dataf['yups'][label] ],
                          fmt=styles[label]['marker'],
                          ecolor=styles[label]['color'],
                          color=styles[label]['color'], zorder=2)
        tmp[-1][0].set_linestyle(styles[label]['linestyle'])
    legend_handles += [tmp]
    for varLabel in dataf['variation_yvals'].keys():
        if varLabel.startswith(label):
            tmp, = ax.plot(dataf['xedges'], dataf['variation_yvals'][varLabel],
                           color=styles[label]['color'],
                           linestyle=styles[label]['linestyle'],
                           drawstyle='steps-pre', solid_joinstyle='miter',
                           zorder=styles[label]['zorder'], alpha=0.5)


# plots on ratio panel
# curve from input yoda files in ratio panel
for label, yvals in dataf['ratio0_yvals'].items():
    if all(np.isnan(v) for v in yvals):
        continue
    if styles[label]['histstyle']: # plot as histogram
        ratio0_ax.plot(dataf['xedges'], yvals,
                       color=styles[label]['color'],
                       linestyle=styles[label]['linestyle'],
                       drawstyle='steps-pre', zorder=1,
                       solid_joinstyle='miter')
        ratio0_ax.vlines(dataf['xpoints'],
                         dataf['ratio0_ymin'][label],
                         dataf['ratio0_ymax'][label],
                         color=styles[label]['color'], zorder=1)
    else: # plot as scatter
        tmp = ratio0_ax.errorbar(dataf['xpoints'],
                                 yvals, xerr=dataf['xerrs'],
                                 yerr=dataf['ratio0_yerrs'][label],
                                 fmt=styles[label]['marker'],
                                 ecolor=styles[label]['color'],
                                 color=styles[label]['color'])
        tmp[-1][0].set_linestyle(styles[label]['linestyle'])

    for varlabel in dataf['ratio0_variation_vals'].keys():
        if varlabel.startswith(label):
            ratio0_ax.plot(dataf['xedges'],
                            dataf['ratio0_variation_vals'][varlabel],
                            color=styles[label]['color'],
                            linestyle=styles[label]['linestyle'],
                            drawstyle='steps-pre', solid_joinstyle='miter',
                            zorder=1, alpha=0.5)

legend_pos = (0.5, 0.97)
ax.legend(legend_handles, labels, loc='upper left', bbox_to_anchor=legend_pos)

# set plot metadata as defined above
ratio0_ax.set_xlabel(ax_xLabel)
ratio0_ax.xaxis.set_label_coords(1., -.15)
ax.set_ylabel(ax_yLabel, loc='top')
ax.set_title(ax_title, loc='left')
ax.set_xscale(ax_xScale)
ax.set_yscale(ax_yScale)
ax.set_xlim(xLims)
ax.set_ylim(yLims)

# tick formatting
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
ax.yaxis.set_major_locator(mpl.ticker.LogLocator(base=10.0, numticks=np.inf))
ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(
                           base=10.0, subs=np.arange(0.1, 1, 0.1), numticks=np.inf))
fig.align_ylabels((ax, ratio0_ax))
plt.savefig(os.path.join(plot_outdir, 'cutEg_jbjg_dphi.pdf'), format='PDF')
plt.savefig(os.path.join(plot_outdir, 'cutEg_jbjg_dphi.png'), format='PNG')

plt.close(fig)