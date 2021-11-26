from torchvision import transforms
from torchvision.models import resnet50
import torch.nn as nn
import torch, warnings, sys, os, requests, argparse
from rich.table import Table
from rich.console import Console

warnings.filterwarnings("ignore")
from PIL import Image


parser = argparse.ArgumentParser(description='args')
grp = parser.add_mutually_exclusive_group()
grp.add_argument('-p','--path', type=str, help='Path to image from your PC', default=None)
grp.add_argument('-u', '--url', type=str, help='URL of the image', default=None)

args = parser.parse_args()

img = None


if args.path is not None:

    if os.path.isfile(args.path):
        img = Image.open(args.path)
    else:
        print(f'{args.path} does not exist. Please check the path')
        sys.exit()

if args.url is not None:

    req = requests.get(args.url, stream=True)
    
    if req.status_code == 200:
        img = Image.open(req.raw)
        
    else:
        print(f'Error HTTP {req.status_code}')
        sys.exit()

if img is None:
    
    print("\nusage: cli.py [-h] [-p PATH | -u URL]\n")
    exit()

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

if img is not None:

    img_processed = transform(img)
    img_processed = img_processed.unsqueeze(0)
    
    preds = nn.functional.softmax(model(img_processed)[0], dim=0)
    preds = preds.detach().numpy()
    
    labelspreds = {}

    for i in range(len(labels)):
        labelspreds[labels[i]] = preds[i]
    sortedlabels = sorted(labelspreds, key=labelspreds.get,reverse=True)

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column(sortedlabels[0])
    table.add_column(sortedlabels[1])
    table.add_column(sortedlabels[2])

    table.add_row(f"{float(labelspreds[sortedlabels[0]])*100:.2f}%",f"{float(labelspreds[sortedlabels[1]])*100:.2f}%",f"{float(labelspreds[sortedlabels[2]])*100:.2f}%")
    Console().print("\t\t",table)