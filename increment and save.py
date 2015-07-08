# This Pythonista script increments and saves the current file.  
# I wrote it so I could quickly save different versions of scripts.
# It is meant to be added to the editor's action menu. 

import editor, os, sys, re
text = editor.get_text()
if not text:
    sys.exit('No text in the Editor.')

filename = os.path.split(editor.get_path())[1][:-3]

#find number at end of filename
num = re.split('[^\d]', filename)[-1]

#converts num from string to integer
num = int(num) if num else 0

#rebuild filename with incremented number
filename = '{}{}.py'.format(filename[:-len(num)] + num + 1)

#write new file
editor.make_new_file(filename, text)
