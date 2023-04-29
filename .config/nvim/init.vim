" This line makes pacman-installed global Arch Linux vim packages work.
source /usr/share/nvim/archlinux.vim

" Plugins
call plug#begin('~/.config/nvim/plugged')

Plug 'yunlingz/equinusocio-material.vim'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}

call plug#end()

" Config
set relativenumber
set termguicolors
set nocompatible
set showmatch
set ignorecase
set hlsearch
set incsearch
set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4
set autoindent
set wildmode=longest,list
set cc=160
filetype plugin indent on
syntax on
set cursorline
set ttyfast
let g:equinusocio_material_style = 'pure'
colorscheme equinusocio_material

" Lua config
lua <<EOF
require'nvim-treesitter.configs'.setup {
  highlight = { enable = true },
  incremental_selection = { enable = true },
  textobjects = { enable = true },
}
EOF
