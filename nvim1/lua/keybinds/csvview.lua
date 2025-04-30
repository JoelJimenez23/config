local function map(m,k,v)
	vim.keymap.set(m,k,v, {silent = true  })
end

local maps = {
	map('n','<F4>',':CsvViewToggle delimiter=, display_mode=border header_lnum=1')
}

return maps
