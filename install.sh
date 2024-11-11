install_dir=$HOME/.local/bin
mkdir -p $HOME/.dex_vision
cp -r Sprites $HOME/.dex_vision
cd DexVision/
python3 -m PyInstaller --onefile main.py --name=dex-vision
mkdir -p $install_dir
mv dist/dex-vision $install_dir
cd
echo "Installation Completed"