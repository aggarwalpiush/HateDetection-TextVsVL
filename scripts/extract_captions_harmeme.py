#! usr/bin/env python
# -*- coding : utf-8 -*-

import codecs
import os
from glob import glob
from PIL import Image
import torch
import json
from tqdm import tqdm

from clip_text_decoder.model import ImageCaptionInferenceModel

FB_MEME_PATH = "/home/aggarwalp/meme_datasets/fb"
HARMEME_MEME_PATH = "/home/aggarwalp/meme_datasets/harmeme"


def extract_CLIPcaption(model, img_path):
    '''
    :param img_path: pass path of the image whose caption need to be evaluated
    :return: caption text
    '''

    image = Image.open(img_path).convert('RGB')
    # The beam_size argument is optional. Larger beam_size is slower, but has
    # slightly higher accuracy. Recommend using beam_size <= 3.
    caption = model(image, beam_size=1)
    return caption

def main():
    model = ImageCaptionInferenceModel.load('/home/aggarwalp/meme_datasets/pretrained-model-1.4.0.pt')
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    memes_array = glob(os.path.join(HARMEME_MEME_PATH,'img','*'))
    meme_caption_dataset = []
    #count = 0
    for meme in tqdm(memes_array):
        #count += 1
        meme_details = {}
        meme_details['id'] = os.path.basename(meme)
        meme_details['path'] = meme
        meme_details['clip_caption'] = extract_CLIPcaption(model, meme)
        meme_caption_dataset.append(meme_details)
        #print(meme_caption_dataset)
        #if count == 4:
         #   break
    with codecs.open(os.path.join(os.path.dirname(HARMEME_MEME_PATH),os.path.basename(HARMEME_MEME_PATH)+"_clipCaption.json"), "w", 'utf-8') as final:
        json.dump(meme_caption_dataset, final)
        

if __name__ == '__main__':
    main()




