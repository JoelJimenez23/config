local o = vim.o
local g = vim.g
local opt = vim.opt

o.termguicolors = true
o.number = true
o.numberwidth = 2
o.tabstop = 2
o.shiftwidth = 2

o.swapfile = false

g.loaded_netrw = 1
g.loaded_netrwPlugin = 1


opt.fillchars = { eob = " " }


