#!/bin/sh

# Apply dotfiles

printf "Applying dotfiles...\n\n"

git clone --bare git@github.com:patryk-mol/linux-dotfiles.git ./projects/linux-dotfiles
git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME config --local status.showUntrackedFiles no
git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME reset --hard

# Install plugins for Neovim

printf "\n\nInstalling Neovim plugins...\n\n"

sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

printf "\n\nAfter starting Neovim exectue following commands:\n"
printf ": PlugInstall\n"
printf ": TSInstall bash c cpp css dockerfile gitignore json python swift yaml\n"
printf "\n"

# Apply specific dotfiles

printf "\n\nSelect configuration version:\n"
echo "1 - desktop"
echo "2 - laptop - 2560x1600 resolution"

option=0

while [ $option -lt 1 ] || [ $option -gt 2 ]; do
    printf "Select [1-2]: "
    read option
    if [ $option -lt 1 ] || [ $option -gt 2 ]; then
        echo "Invalid option"
    fi
done

cd

if [ $option -eq 1 ]; then
       ln -s .gtkrc-2.0.mine-desktop .gtkrc-2.0.mine
       cd ~/.config/alacritty
       ln -s alacritty-desktop.yml alacritty.yml
       cd ~/.config/gtk-3.0
       ln -s settings-desktop.ini settings.ini
       cd ~/.config/qtile
       ln -s config-desktop.py config.py
       cd ~/.config/qtile/scripts
       ln -s autostart-desktop.sh autostart.sh
elif [ $option -eq 2 ]; then
       ln -s .gtkrc-2.0.mine-laptop-2560x1600 .gtkrc-2.0.mine
       cd ~/.config/alacritty
       ln -s alacritty-laptop-2560x1600.yml alacritty.yml
       cd ~/.config/gtk-3.0
       ln -s settings-laptop-2560x1600.ini settings.ini
       cd ~/.config/qtile
       ln -s config-laptop-2560x1600.py config.py
       cd ~/.config/qtile/scripts
       ln -s autostart-laptop-2560x1600.sh autostart.sh
fi

cd

papirus-folders -C grey