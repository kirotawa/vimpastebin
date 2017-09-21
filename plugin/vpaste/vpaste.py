
import vim
import json

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

data = {
    'paste_data': '',
    'paste_lang': '',
    'api_submit': 'true',
    'mode': 'json',
    # paste'll always expire after 1 day
    'paste_expire': 86400
}

lang_name = {
    'py': 'python',
    'php': 'php',
    'c': 'c',
    'cpp': 'cpp',
    'java': 'java',
    'js': 'javascript',
    'rb': 'ruby',
    'pl': 'perl',
    'S': 'asm',
    's': 'asm',
    'diff': 'diff'
}

URL_BASE = 'https://pastebin.osuosl.org'

# Get the type of file and language of file
bname = vim.current.buffer.name
lang_type = bname.split('/')[-1].split('.')[1]

try:
    data['paste_lang'] = lang_name[lang_type]
except:
    # if we are using a non supported lang, try text
    data['paste_lang'] = 'text'

# Gets start - s, and end's - e, selection
s = vim.current.buffer.mark("<")[0]
e = vim.current.buffer.mark(">")[0]

# Gets the current lines are selected
buffer_code = vim.current.buffer[s-1:e]

code_to_paste = ""
for code_line in buffer_code:
    if code_line == '':
        code_to_paste += '\n'
    else:
        code_to_paste += code_line
        code_to_paste += '\n'

data['paste_data'] = code_to_paste
response = urlopen(URL_BASE, urlencode(data).encode('utf-8'))

result = response.read().decode('utf-8')
url_result = json.loads(result)

print(URL_BASE+'/'+url_result['result']['id'])
