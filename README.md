<h1 align="center">Coregistration MRI with MEG</h1>

<p align="center">
  Coregisters MEG head coordinates with an MRI (FreeSurfer/BEM subject) using MNE-Python Coregistration with fiducial fitting and ICP, and saves the head-MRI transform with a report.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.826"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.826-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Coregisters MEG head coordinates with an MRI (FreeSurfer/BEM subject) using MNE-Python Coregistration with fiducial fitting and ICP, and saves the head-MRI transform with a report.**

Estimates fiducials from fsaverage, fits them, then refines the alignment with iterative closest point on the head-shape points, dropping outliers over 5 mm. Writes the transform (trans.fif), a plot and an HTML report with digitisation-to-MRI distances. Needed before forward modelling and source estimation; requires digitised head-shape points in the MEG file.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/raw` · `raw` |
| **Outputs** | `neuro/meeg/mne/covariance` · `generic/image/png` · `report/html` |
| **Container** | `brainlife/mne:1.2.1` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.826](https://doi.org/10.25663/brainlife.app.826) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif1` | `neuro/meeg/mne/raw` | yes | MEG data (MNE raw) with digitised head-shape points. |
| `bem1` | `raw` (bem) | yes | FreeSurfer subject directory with BEM surfaces for the MRI. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/covariance` | Head-to-MRI transform (trans.fif). |
| `out_figs` | `generic/image/png` | Plot of the coregistration. |
| `out_dir_report` | `report/html` | HTML report of the coregistration. |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `fiducials` | string | `auto` | The fiducials given in the MRI (surface RAS) coordinate system. If a dictionary is provided, it must contain the keys 'lpa', 'rpa', and 'nasion', with values being the respective coordinates in meters. If a list, it must be a list of DigPoint instances as returned by the mne.io.read_fiducials() function. If 'estimated', the fiducials are derived from the fsaverage template. If 'auto' (default), tries to find the fiducials in a file with the canonical name ({subjects_dir}/{subject}/bem/{subject}-fiducials.fif) and if absent, falls back to 'estimated'. |
| `on_defects` | enum |  | What to do if the surface is found to have topological defects. Can be 'raise' (default) to raise an error, 'warn' to emit a warning, or 'ignore' to ignore when one or more defects are found. Note that a lot of computations in MNE-Python assume the surfaces to be topologically correct, topological defects may still make other computations (e.g., mne.make_bem_model and mne.make_bem_solution) fail irrespective of this parameter. Options: `raise`, `warn`, `ignore`. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.826](https://doi.org/10.25663/brainlife.app.826), choose `neuro/meeg/mne/raw`, `raw` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/covariance`, `generic/image/png`, `report/html`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.2.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "mne": "/path/to/fif1/mne",
       "output": "/path/to/bem1/output",
       "fiducials": "auto",
       "on_defects": ""
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Coregistration MRI with MEG. brainlife.io App. [doi:10.25663/brainlife.app.826](https://doi.org/10.25663/brainlife.app.826)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso
- Antonio Caulín

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
