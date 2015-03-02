if !has('python')
	finish
endif

let $vimdir="~/.vim/plugin/vpaste/"

vnoremap <silent> <F5> :<C-U>PASTE<CR>

function! Paste()
	pyfile $vimdir/vpaste.py
endfunc

command! PASTE call Paste()

