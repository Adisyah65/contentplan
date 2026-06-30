import os
import glob

templates_dir = r'c:\semester 6\contentplan\templates'
html_files = glob.glob(os.path.join(templates_dir, '*.html'))

replacements = {
    "url_for('konten_list',": "url_for('content.konten_list',",
    "url_for('dashboard',": "url_for('main.dashboard',",
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {os.path.basename(file_path)}')
print('Selesai.')
