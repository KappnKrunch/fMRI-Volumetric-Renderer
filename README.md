# fMRI-Volumetric-Renderer
A volumetric fMRI renderer for the web. Built using WebGL.

This project presents a method for visualizing volumetric MRI and fMRI data based on a discrete raytracing algorithm and OpenGL.
Data is pre-processed and then attached to the html template document, the renderer itself is written in html. This method presents a lightweight 
renderer that can be used to visualize fMRI data in a browser as well as in the output of a jupyter notebook. Includes support for rgba color mapping.

Implementation looks like:

import nibabel as nib
import torch
from string import Template

#load an example nifti file
brainData = nib.load("data/sub-01/func/sub-01_task-1_bold.nii.gz")

#load the nifti data into a pytorch tensor
activationSequence = torch.tensor(brainData.get_fdata().T)

#use the displayVolume function to create interactive displays
displayVolume(activationSequence, fileName="exampleView.html")

Live version:
https://kappnkrunch.github.io/fMRI-Volumetric-Renderer/view.html

![Gif showing the renderer](view.gif "MRI view")
