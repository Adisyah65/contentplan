import os
import glob

templates_dir = r'c:\semester 6\contentplan\templates'
html_files = glob.glob(os.path.join(templates_dir, '*.html'))

replacements = {
    "url_for('dashboard')": "url_for('main.dashboard')",
    "url_for('kalender')": "url_for('main.kalender')",
    "url_for('analitik')": "url_for('main.analitik')",
    "url_for('konten_list')": "url_for('content.konten_list')",
    "url_for('konten_baru')": "url_for('content.konten_baru')",
    "url_for('konten_edit'": "url_for('content.konten_edit'",
    "url_for('konten_hapus'": "url_for('content.konten_hapus'",
    "url_for('logout')": "url_for('auth.logout')",
    "url_for('login')": "url_for('auth.login')",

    "request.endpoint == 'dashboard'": "request.endpoint == 'main.dashboard'",
    "request.endpoint == 'kalender'": "request.endpoint == 'main.kalender'",
    "request.endpoint == 'analitik'": "request.endpoint == 'main.analitik'",
    "request.endpoint == 'konten_list'": "request.endpoint == 'content.konten_list'",
    "request.endpoint == 'konten_baru'": "request.endpoint == 'content.konten_baru'",
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
