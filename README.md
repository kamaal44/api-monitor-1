# autorun-apk


## Install

```bash=
git clone https://github.com/krnick/api-monitor

cd api-monitor

pipenv install --skip-lock

# run env
pipenv shell
```


## export adb to your work path, and start the adb server.

```bash=
source start-emulator.sh
```

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
