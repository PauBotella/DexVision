mkdir -p $HOME/.dex_vision
cp -r Sprites $HOME/.dex_vision
cd DexVision/
python3 -m PyInstaller --onefile main.py --name=dex-vision
mv dist/dex-vision $HOME/.local/bin
