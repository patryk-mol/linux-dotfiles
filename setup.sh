#!/bin/sh

git clone --bare git@github.com:patryk-mol/linux-dotfiles.git ./projects/linux-dotfiles
git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME config --local status.showUntrackedFiles no
git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME reset --hard