
# Coregistration MRI with MEG

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Coregisters MEG head coordinates with an MRI (FreeSurfer/BEM subject) using MNE-Python Coregistration with fiducial fitting and ICP, and saves the head-MRI transform with a report.**

Estimates fiducials from fsaverage, fits them, then refines the alignment with iterative closest point on the head-shape points, dropping outliers over 5 mm. Writes the transform (trans.fif), a plot and an HTML report with digitisation-to-MRI distances. Needed before forward modelling and source estimation; requires digitised head-shape points in the MEG file.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/raw` · `raw` |
| 📤 **Outputs** | `neuro/meeg/mne/covariance` · `generic/image/png` · `report/html` |
| 🐳 **Container** | `brainlife/mne:1.2.1` |
| ⚙️ **Resources** | 8 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.826](https://doi.org/10.25663/brainlife.app.826) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif1` | `neuro/meeg/mne/raw` | yes | MEG data (MNE raw) with digitised head-shape points. |
| `bem1` | `raw` (bem) | yes | FreeSurfer subject directory with BEM surfaces for the MRI. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/covariance` | Head-to-MRI transform (trans.fif). |
| `out_figs` | `generic/image/png` | Plot of the coregistration. |
| `out_dir_report` | `report/html` | HTML report of the coregistration. |

<details>
<summary><b>⚙️ Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `fiducials` | string | `auto` | The fiducials given in the MRI (surface RAS) coordinate system. If a dictionary is provided, it must contain the keys 'lpa', 'rpa', and 'nasion', with values being the respective coordinates in meters. If a list, it must be a list of DigPoint instances as returned by the mne.io.read_fiducials() function. If 'estimated', the fiducials are derived from the fsaverage template. If 'auto' (default), tries to find the fiducials in a file with the canonical name ({subjects_dir}/{subject}/bem/{subject}-fiducials.fif) and if absent, falls back to 'estimated'. |
| `on_defects` | enum |  | What to do if the surface is found to have topological defects. Can be 'raise' (default) to raise an error, 'warn' to emit a warning, or 'ignore' to ignore when one or more defects are found. Note that a lot of computations in MNE-Python assume the surfaces to be topologically correct, topological defects may still make other computations (e.g., mne.make_bem_model and mne.make_bem_solution) fail irrespective of this parameter. Options: `raise`, `warn`, `ignore`. |

</details>

📚 **References used by this App:**
- Avesani P, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.826-blue.svg)](https://doi.org/10.25663/brainlife.app.826)

Brainlife App to perform MRI<->head coregistration for epoched data using mne.coreg.Coregistration class.



1) Input file is:
    * `meg/fif` meg data file
    * `output`  meeg data file

2) Input parameters are:
* `fiducials` Surface RAS coordinate system.
* `on_defects` Surface is found to have topological defects.

3) Ouput files are:
    * Noise Covariance Matrix
    * a plot of the Trans Matrix
    * a html report
   

## Authors
- Guiomar Niso (guiomar.niso@gmail.com)
- Antonio Caulín (antoniocaulinatienzar@gmail.com)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University