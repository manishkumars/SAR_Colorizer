#install library requirements from requirements.txt

import fastai
from SAR_Colorizer.visualize import *

torch.backends.cudnn.benchmark = True

source_url = '' #@param {type:"string"}
render_factor = 35  #@param {type: "slider", min: 7, max: 45}


if source_url is not None and source_url !='':
    image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
    show_image_in_notebook(image_path)
else:
    print('Provide an image url and try again.')
