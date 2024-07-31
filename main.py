# set up environment, all are necessary for coregistration
import os
import json
import mne

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == CONFIG PARAMETERS ==
fname        = config['mne']
subjects_dir = config['output'] # BEM

subject = 'output'


# Read the information about the file of events
info = mne.io.read_info(fname)

# Configure some parameters of visualization
plot_kwargs = dict(
    subject=subject,
    subjects_dir=subjects_dir,
    surfaces="head-dense",
    dig=True,
    eeg=[],
    meg="sensors",
    show_axes=True,
    coord_frame="meg",
)
view_kwargs = dict(azimuth=45, elevation=90, distance=0.6, focalpoint=(0.0, 0.0, 0.0))


fiducials = "estimated"  # get fiducials from fsaverage
coreg = mne.coreg.Coregistration(info, subject, subjects_dir, fiducials=fiducials)

coreg.fit_fiducials(verbose=True)

coreg.fit_icp(n_iterations=6, nasion_weight=2.0, verbose=True)
coreg.omit_head_shape_points(distance=5.0 / 1000)  # distance is in meters

#fig = mne.viz.plot_alignment(info, trans=coreg.trans, **plot_kwargs)

# ICP and visualization
#if config['final'] == True:
coreg.fit_icp(n_iterations=20, nasion_weight=10.0, verbose=True)
#fig = mne.viz.plot_alignment(info, trans=coreg.trans, **plot_kwargs)
#mne.viz.set_3d_view(fig, **view_kwargs)

dists = coreg.compute_dig_mri_distances() * 1e3  # in mm
print(
        f"Distance between HSP and MRI (mean/min/max):\n{np.mean(dists):.2f} mm "
        f"/ {np.min(dists):.2f} mm / {np.max(dists):.2f} mm"
    )


# == SAVE RESULTS ==

# SAVE DATA (trans.fif)
fname_trans=os.path.join('out_dir','cov.fif')
mne.write_trans(fname_trans, trans=coreg.trans)

# SAVE FIGURE
#fig.savefig(os.path.join('out_figs','coregistration.png'))

# SAVE REPORT
report = mne.Report(title='Report')
#report.add_figs_to_section(fig, captions='Alignment', section='Coregistration')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)


   