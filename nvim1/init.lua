require("config.lazy")

require("lazy").setup({
    require("plugins.lualine"),
    require("plugins.nvim_tree"),
    require("plugins.tokyonight"),
    require("plugins.render_markdown"),
    require("plugins.ultimate_autopair"),
    require("plugins.mason"),
    require("plugins.treesitter"),
		require("plugins.nightfox"),
		require("plugins.neoscroll"),
		require("plugins.csvview")
})

require("keybinds.nvimtreek")
require("keybinds.barbark")
require("keybinds.themeryk")
-- require("keybinds.tmuxk")
require("keybinds.csvview")

require("settings.settings")
-- require("config.masonc")
