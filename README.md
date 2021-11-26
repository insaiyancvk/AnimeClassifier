# Anime Character Classifier

Steps:

Name: Anime classifier
Anime: Naruto? AoT? Jujutsu kaisen? Highschool dxd(MoC)?
1) Take an anime.
2) Upload an image.
3) Top 3 predictions. 

Reference: [derenet](https://nbviewer.org/github/insaiyancvk/Dere-Net/blob/main/Dere_Net_dirty_work_colab.ipynb#Import-stuff)

  
- Collect data - 30 Characters
  - Use scraping or whatever technique
    - Scrape 1000 images per character for 30 characters from that anime
  - Store each character data in separate folders with the character name being the name of the folder
- Train yo model
  - Refer [derenet](https://nbviewer.org/github/insaiyancvk/Dere-Net/blob/main/Dere_Net_dirty_work_colab.ipynb#Import-stuff) for that
- Deploy da model on the Heroku app
  - Refer app.py


Steps to be followed:
1. Collect the data - 
2. Train the model 
3. Validate - Tuning the model’s performance
4. Ensemble of models (Maybe)
5. Predict 

Order Of Characters

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
