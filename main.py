import os
import json
import mne

import matplotlib.pyplot as plt
import numpy as np


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)
    
# == LOAD DATA (mne/raw) ==
fname = config['mne']
raw = mne.io.read_raw_fif(fname, preload=True)

# == LOAD DATA (bem) ==

# subjects_dir: path to the directory containing the FreeSurfer subjects reconstructions (SUBJECTS_DIR)
subjects_dir = config['output']
subject= 'output'
mne.gui.coregistration(subject=subject, subjects_dir=subjects_dir, inst=raw)

# Start MNE-Report
report = mne.Report(title='Report')

#add report coregistration 

# == SAVE REPORT ==
report.save(os.path.join('out_dir_report','report.html'))

# == SAVE DATA ==
raw.save(os.path.join('out_dir','raw.fif'))