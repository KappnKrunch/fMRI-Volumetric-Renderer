import nibabel as nib
import torch
from string import Template

import volume_plot_utils

#load an example nifti file
brainData = nib.load("data/sub-01/func/sub-01_task-1_bold.nii.gz")

#load the nifti data into a pytorch tensor
activationSequence = torch.tensor(brainData.get_fdata().T)

#use the displayVolume function to create interactive displays
displayVolume(activationSequence, fileName="exampleView.html")
