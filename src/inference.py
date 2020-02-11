

import pickle
from fastai.vision import *
from fastai.callbacks import *
from skimage import io
from fastai.utils.collect_env import *
import torch 
from app import app
import matplotlib
matplotlib.use('Agg')



def import_model():
    import src.inference_classes as inference_classes
    inference_learner = load_learner(
        path='src/', 
        file='single_chan_dice.pkl')
    return inference_learner



def prep_input(input_img):
    read_img = io.imread(input_img)
    t_img = Image(pil2tensor(read_img[:,:,:3],np.float32).div_(255))
    return t_img


def inference_mask(model, t_img):
    outputs = model.predict(t_img)
    inference_mask = image2np(outputs[2])
    inference_mask = (inference_mask*255).astype('uint8')
    return inference_mask

# def visualize_inference(inference_mask, input_img):
    
#     fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
#     ax1.imshow(io.imread(input_img))
#     ax2.imshow(inference_mask[:,:,1], alpha=1)
#     ax1.axis('off')
#     
#     

def visualize_inference(inference_mask, input_img):
    
    fig, ax= plt.subplots(1,1, figsize=(10,10))
    ax.imshow(inference_mask[:,:,1], alpha=1)
    ax.axis('off')
    plt.savefig('static/mask.png', dpi = 500, pad_inches = 0)

    fig2, ax2= plt.subplots(1,1, figsize=(10,10))
    ax2.imshow(io.imread(input_img))
    ax2.axis('off')
    plt.savefig('static/img.png')


    
def make_prediction(input_image):
    learner = import_model()
    tens_img = prep_input(input_image)
    mask = inference_mask(learner, tens_img)
    visualize_inference(inference_mask=mask, input_img=input_image)
    
