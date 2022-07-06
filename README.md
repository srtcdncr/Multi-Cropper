# Multi-Cropper
A python program that crops multiple similar photos to the same borders. 

## Installation
```
python -m venv venv
```
```
CALL venv/Scripts/activate
```
```
pip install -r requirements.txt
```

## Usage
```
python app.py -h
```

```
usage: app.py [-h] -l LINK [-b Sol Üst Sağ Alt] [-m Sol Üst Sağ Alt]

Toplu Fotoğraf Kırpma Scripti

options:
  -h, --help            show this help message and exit
  -l LINK, --link LINK  [TR] Fotoğralarınızın bulunduğu klasör konumu [EN] Location of photos to crop
  -b Sol Üst Sağ Alt, --bbox Sol Üst Sağ Alt
                        [TR] Fotoğrafın kırpılmasını istediğiniz alanı <Sol, Üst, Sağ, Alt>
  -m Sol Üst Sağ Alt, --margin Sol Üst Sağ Alt
                        [TR] Fotoğrafın kırpılmasını istediğiniz alanın fotoğrafın orjinal sınırlarına uzaklığı <Sol,
                        Üst, Sağ, Alt>
```

#### Link: Location of images.
#### Bbox: Absolute location of corner of new cropped photo. (in pixels)
#### Margin: Relative location to original photos edges of new cropped photos edges. (in pixels) 
