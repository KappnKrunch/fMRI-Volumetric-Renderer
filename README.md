# fMRI-Volumetric-Renderer
A volumetric fMRI renderer for jupyter notebook. Built using WebGL.

This project presents a method for visualizing volumetric MRI and fMRI data based on a discrete raytracing algorithm and OpenGL.
Data is pre-processed and then attached to the html template document, the renderer itself is written in html. This method presents a lightweight 
renderer that can be used to visualize fMRI data in the output of a jupyter notebook.

Interactive example: [Here](https://colab.research.google.com/github/KappnKrunch/fMRI-Volumetric-Renderer/blob/main/Volumetric_Render_Pipeline.ipynb "interactive link")

## Python Render Pipeline Usage
Get the package from the pip repository using the python pip command
```console
pip install fMRI-Volumetric-Renderer
```
Display volume from file
```python
import nibabel as nib
import torch

from volume_plot_utils import plotter

#load an example nifti file
brainData = nib.load("data/sub-0x/func/subject-data-file.nii.gz")

#load the nifti data into a pytorch tensor
activationSequence = torch.tensor(brainData.get_fdata().T)

#use the displayVolume function to display the volumetric data in ipynb
plotter.displayVolume(activationSequence)
```

## General HTML Template Usage
The example python shows usage with pytroch and nibabel but html displays can be created from a template by substituting keywords from the template file:
see plotter.py for more information


![Gif showing the renderer](view.gif "MRI view")

Interactive example: [Here](https://colab.research.google.com/github/KappnKrunch/fMRI-Volumetric-Renderer/blob/main/Volumetric_Render_Pipeline.ipynb "interactive link")
