# autorun-apk


## Install

```bash=
git clone https://github.com/krnick/android-sandbox-autorun.git

cd android-sandbox-autorun

pipenv install --skip-lock

# run env
pipenv shell
```


## export adb to your work path

```bash=
source .bash_profile 
```

Make sure you have already install the Android sdk and the emulator set up.


## Usage


```bash=
python main.py test.apk
```

## [Video Demo](https://www.youtube.com/watch?v=0FWliRuwiso)

![](https://i.imgur.com/hWjkNbt.gif)
