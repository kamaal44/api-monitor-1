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
source environment_shell/start-emulator.sh
```

### Init the adb server

```bash=
source environment_shell/.bash_profile
```

### Init the frida server

```bash=
source environment_shell/start-frida.sh
```

Make sure you have already install the Android sdk and the emulator set up.


## Usage


```bash=
python main.py test.apk
```

## [Video Demo](https://www.youtube.com/watch?v=0FWliRuwiso)

![](https://i.imgur.com/hWjkNbt.gif)
