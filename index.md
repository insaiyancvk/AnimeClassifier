# Anime Character Classifier

[![](https://img.shields.io/badge/heroku-deployed-green)](https://animeclassifier.herokuapp.com/)

![](https://raw.githubusercontent.com/insaiyancvk/AnimeClassifier/main/assets/demo.png)

Anime character classifier trained on _ResNet50_. Trained and deployed using `PyTorch`.

The anime include: Attack On Titan, Dragon Ball Z/Super, Naruto, One Piece.

List Of Characters

```python
[
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
 ```

# Setup

Clone the repository:

```
git clone https://github.com/RudCodera8/AnimeClassifier
```

Navigate into the folder:

```
cd AnimeClassifier
```

## For running CLI app:

Install dependencies:

```
pip install torch torchvision pillow requests
```

Run the CLI app:

```
python cli.py
```
## For running the web app:

Install dependencies:
```
pip install -r requirements.txt
```

Run the app:
```
python app.py
```

# Usage
- For the web app: Select an image and click on submit button
- For the CLI app:

```bash
usage: cli.py [-h] [-p PATH | -u URL]
args
optional arguments:

-h, --help            show this help message and exit
-p PATH, --path PATH  Path to image from your PC
-u URL, --url URL     URL of the image
```

## Examples:
### Web App:
![](https://raw.githubusercontent.com/insaiyancvk/AnimeClassifier/main/assets/webapp.png)

### CLI App:
![](https://raw.githubusercontent.com/insaiyancvk/AnimeClassifier/main/assets/cliapp.png)

## Contributions for data collection:
[Susil Kessav](https://github.com/susilkessav) - [Attack On Titan Data](https://www.kaggle.com/susilkessav/wwwkagglecomsusilkessavaot)

[Vamshi Krishna](https://github.com/insaiyancvk) - [Dragon Ball Z/Super Data](https://www.kaggle.com/insaiyancvk/dragon-ball-z-dataset)

[Abhijith Menon](https://github.com/rudCodera8) - [Naruto Data](https://www.kaggle.com/abhijimenon/narutocharactersdataset)

[Vysnav](https://github.com/vysnav) - [One Piece Data](https://www.kaggle.com/vyshnavp/one-piece)
