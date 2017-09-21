if !has('python') && !has('python3')
    finish
endif

let $vimdir="~/.vim/plugin/vpaste/"

vnoremap <silent> <F5> :<C-U>PASTE<CR>

function! Paste()
    if has('python')
	    pyfile $vimdir/vpaste.py
    elseif has('python3')
        py3file $vimdir/vpaste.py
    else
        finish
    endif
endfunc

command! PASTE call Paste()

