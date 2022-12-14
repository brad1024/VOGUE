import os
from PIL import Image
import numpy as np

mask_folder = '/data/suparna/Data/soccershirt/schalke_mask'
maskvis_folder = '/data/suparna/Data/soccershirt/schalke_maskvis'
vogue_mask = '/data/suparna/Data/soccershirt/schalke_voguemask'
LIPTOVOGUE = {
    'background': [0],
    'tops': [5,6,7,11], 
    'bottoms': [8,9,10,12], 
    'face': [13], 
    'hair': [1,2], 
    'arms': [3, 14, 15], 
    'skin': [85,51,0], 
    'legs': [16,17,18,19], 
    'other':[]
}
colorspace = [(0, 0, 0), (255, 85, 0), (85, 85, 0), (0, 0, 255), (0, 119, 221), (51, 170, 221), (85,51,0), (170, 255, 85), (52, 86, 128)]
for i in range(len(os.listdir(mask_folder))):
    maskpath = os.path.join(mask_folder, str(i)+'.png')
    im_parse = Image.open(maskpath).convert('L')
    im_parse_rgb = np.array(Image.open(os.path.join(maskvis_folder, str(i)+'.png')))
    parse_array = np.array(im_parse)
    new_mask = np.zeros((512,512,3))
    for j, key in enumerate(LIPTOVOGUE.keys()):
        LIPlabels = LIPTOVOGUE[key]
        if key=='skin':
            new_mask[(im_parse_rgb == LIPlabels).all(-1)] = colorspace[j]
            continue
        for label in LIPlabels:
            #indexes = np.where(parse_array == int(label))
            new_mask[parse_array == int(label)] = colorspace[j]
    im = Image.fromarray(new_mask.astype(np.uint8))
    im.save(os.path.join(vogue_mask, str(i)+'.png'))
    print(maskpath)
    #exit()



