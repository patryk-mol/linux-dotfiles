#!/bin/sh

# Apply dotfiles

echo "Applying dotfiles...\n\n"

git clone --bare git@github.com:patryk-mol/linux-dotfiles.git ./projects/linux-dotfiles
git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME config --local status.showUntrackedFiles no
git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME reset --hard

# Apply theme

echo "\n\nApplying themes...\n\n"

git clone https://gitlab.com/pwyde/monochrome-kde.git ./projects/monochrome-kde
cd .projects/monochrome-kde
chmod +x install.sh
./install.sh --install
cd

git clone https://anongit.kde.org/breeze-gtk.git ./projects/breeze-gtk
cd ./projects/breeze-gtk/src/
cp build_theme.sh.cmake build_theme.sh
sed -i 's/@PYTHON_EXECUTABLE@/python/g' build_theme.sh
sudo sh build_theme.sh -c Monochrome -t /usr/share/themes/Monochrome

mkdir -p ~/.config/ulauncher/user-themes
git clone git@github.com:patryk-mol/ulauncher-monochrome-theme.git ~/.config/ulauncher/user-themes/monochrome


# Install plugins for Neovim

echo "\n\nInstalling Neovim plugins...\n\n"
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

echo "\n\nAfter starting Neovim exectue following commands:\n"
echo ": PlugInstall\n"
echo ": TSInstall bash c cpp css dockerfile gitignore json python swift yaml\n"
echo "\n"

