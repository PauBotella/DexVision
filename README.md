# DexVision

A script to print out animated sprites of pokemon to the terminal. Inspired by
[Pokemon Color Scripts](https://gitlab.com/phoneybadger/pokemon-colorscripts)


Gen 1 to 5 original sprites are from EBDX

For the next generations original sprites are from pokemon showdown

5% chance of shiny in random

## Visuals
![galarian zigzagoon](./Assets/r1.gif)
![latios](./Assets/r2.gif)
![zacian](./Assets/zacian.gif)
![salamence](./Assets/salamence.gif)
![cinderace](./Assets/cinderace.gif)

### Startup
![dhelmise](./Assets/dhelmise.gif)
![flygon](./Assets/flygon.gif)
![lapras](./Assets/lapras.gif)

## Requeriments
The program requires `python3`,`pip`,`pyinstaller`
```
sudo apt install python3-pip
```
```
pip install -U pyinstaller
```
## Installation

```
git clone https://github.com/PauBotella/DexVision.git
```
```
cd DexVision
./install.sh
```
Make sure that the folder `~/.local/bin` is in PATH.
```
echo $PATH
```
#### If not then:
#### In bash
```
export PATH="$PATH:~/.local/bin"
source ~/.profile
source ~/.bashrc
```
#### In fish
```
set -U fish_user_paths ~/.local/bin $fish_user_paths
```
## Uninstallation
Go to the proyect folder and:
```
./uninstall.sh
```

## Usage
```
usage: DexVision [-h] [-s] [-n] [-l] [-r] [pokemon]

Show pokemon animated sprites

positional arguments:
  pokemon       Display any Pokémon that you want

options:
  -h, --help    show this help message and exit
  -s, --shiny   Displays the pokemon in its shiny form. Only with -p flag
  -n, --name    Displays the name of selected pokemon. Only with -r flag
  -l, --list    Displays a list of available pokemon
  -r, --random  Displays a pokemon randomly
```
