#! usr/bin/env python
# -*- coding : utf-8 -*-

import codecs
import os
from glob import glob
from PIL import Image
import torch
import json

from clip_text_decoder.model import ImageCaptionInferenceModel

FB_MEME_PATH = "/home/aggarwalp/meme_datasets/fb"



def extract_CLIPcaption(img_path):
    '''
    :param img_path: pass path of the image whose caption need to be evaluated
    :return: caption text
    '''
    model = ImageCaptionInferenceModel.download_pretrained()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    image = Image.open(img_path)
    # The beam_size argument is optional. Larger beam_size is slower, but has
    # slightly higher accuracy. Recommend using beam_size <= 3.
    caption = model(image, beam_size=1)
    return caption

def main():
    memes_array = glob(os.path.join(FB_MEME_PATH,'*'))
    meme_caption_dataset = []
    meme_details = {}
    for meme in memes_array:
        meme_details['id'] = os.path.basename(meme)
        meme_details['path'] = meme
        meme_details['clip_caption'] = extract_CLIPcaption(meme)
        meme_caption_dataset.append(meme_details)
    with codecs.open(os.path.join(os.path.basename(FB_MEME_PATH),"_clipCaption.json"), "w", 'utf-8') as final:
        json.dump(meme_caption_dataset, final)
        

if __name__ == '__main__':
    main()




