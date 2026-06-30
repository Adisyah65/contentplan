import re
css = open('c:/semester 6/contentplan/static/css/style.css', encoding='utf-8').read()
css_no_comments = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
lines = css_no_comments.split('\n')
c = 0
for i, l in enumerate(lines):
    c += l.count('{') - l.count('}')
    if c < 0:
        print('Extra } at line:', i+1)
        break
    elif c > 0 and i == len(lines)-1:
        print('Missing } at EOF')
if c == 0:
    print('Braces are balanced!')
