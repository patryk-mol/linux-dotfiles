# Env vars
export PATH=$PATH:$HOME/.cargo/bin
export EDITOR=nano
export VISUAL=subl
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# General
alias dotfiles='/usr/bin/git --git-dir=$HOME/projects/linux-dotfiles/ --work-tree=$HOME'
alias ls=exa
alias lsl='exa -lh'
alias lsal='exa -alh'
alias maintnance='~/projects/linux-scripts/update.sh'
alias open=xdg-open
alias less='bat --paging=always'
alias cat='bat --paging=never'
alias ps=procs

# Package managers
alias pmi="sudo pacman -Syu"
alias pmr="sudo pacman -Rcns"
alias pmc="sudo pacman -R $(pacman -Qdtq)"
alias yayi="yay -Syu"
alias yayr="yay -Rcns"
alias yayc="yay -R $(yay -Qdtq)"

# Starship
export STARSHIP_CONFIG=~/.config/starship/starship.toml
eval "$(starship init zsh)"
