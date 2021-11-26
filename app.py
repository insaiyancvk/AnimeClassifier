import gradio as gr
from torchvision import transforms
from torchvision.models import resnet50
import torch.nn as nn
import torch, warnings
warnings.filterwarnings("ignore")
from PIL import Image

labels = [
    'Armin Arlert',
    'Tony Tony Chopper',
    'Eren Yeager',
    'Frieza',
    'Itachi Uchiha',
    'Kakashi Hatake',
    'Levi Ackerman',
    'Monkey D. Luffy',
    'Mikasa Ackerman',
    'Muten Roshi',
    'Naruto Uzumaki',
    'Reiner Braun',
    'Sakura Haruno',
    'Vinsmoke Sanji',
    'Sasuke Uchiha',
    'Son Gohan',
    'Son Goku',
    'Usopp',
    'Vegeta',
    'Roronoa Zoro'
]

model = resnet50(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, len(labels))

model.load_state_dict(torch.load('./assets/ResNet50.pth'))
model.eval()

transform = transforms.Compose([
    transforms.Resize([256,256]),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406),(0.229, 0.224, 0.225))
])

def predict(img):
    img = Image.fromarray(img.astype('uint8'), 'RGB')
    img = transform(img)
    img = img.unsqueeze(0)
    preds = nn.functional.softmax(model(img)[0], dim=0)
    return {labels[i]: float(preds[i]) for i in range(len(labels))}

title = "Anime Character Classifier"
description = "A fun-to-play-with anime character classifier. To use it, simply upload A picture, or click one of the examples from below to load them."

inputs = gr.inputs.Image()
outputs = gr.outputs.Label(num_top_classes=3)
gr.Interface(
    fn = predict, 
    inputs = inputs,
    outputs = outputs,
    title = title, 
    description = description, 
    allow_flagging = False,
    layout = 'horizontal',
    theme = 'darkdefault',
    examples = [
            ['./assets/armin.jpg'],
            ['./assets/chopper.jpg'],
            ['./assets/eren.jpg'],
            ['./assets/frieza.jpg'],
            ['./assets/gohan.jpeg'],
            ['./assets/goku.jpg'],
            ['./assets/itachi.jpg'],
            ['./assets/kakashi.jpg'],
            ['./assets/levi.jpg'],
            ['./assets/luffy.jpeg'],
            ['./assets/mikasa.jpg'],
            ['./assets/naruto.jpg'],
            ['./assets/reiner.png'],
            ['./assets/ResNet50.pth'],
            ['./assets/roshi.jpeg'],
            ['./assets/sakura.jpg'],
            ['./assets/sanji.jpg'],
            ['./assets/sasuke.jpg'],
            ['./assets/usopp.jpeg'],
            ['./assets/vegeta.jpg'],
            ['./assets/zoro.jpg']
        ]
    ).launch()