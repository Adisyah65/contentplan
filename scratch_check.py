import sys
css = open('c:/semester 6/contentplan/static/css/style.css', encoding='utf-8').read()
lines = css.split('\n')
c = 0
for i, l in enumerate(lines):
    # Ignore comments in this line for brace counting
    # Actually, just count braces
    c += l.count('{') - l.count('}')
    if c < 0:
        print('Extra } at line:', i+1)
        break
