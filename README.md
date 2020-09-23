# Minesweeper

## Prerequisite
1. Python 3

## Setup
1. only for Python 3.8+
```
pip install --pre --extra-index-url=https://kivy.org/downloads/simple kivy[base]
```

2. for all Python 3
```
pip install --upgrade -r requirements.txt
```

## Running
1.
```
python main.py
```

## Packaging
1. for windows
```
pyinstaller minesweeper.spec
```

2. for android
```
buildozer init
```
edit `buildozer.spec`, then run
```
buildozer android debug deploy run
```
device must be connected to pc, more info check https://kivy.org/doc/stable/guide/packaging-android.html
