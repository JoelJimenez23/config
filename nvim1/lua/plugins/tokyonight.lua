return {
  -- the colorscheme should be available when starting Neovim
  {
    "folke/tokyonight.nvim",
    priority = 1000, -- make sure to load this before all the other start plugins
    config = function()
      -- load the colorscheme here
      vim.cmd([[colorscheme tokyonight]])
      require("tokyonight").setup()
    end,
  }
}
