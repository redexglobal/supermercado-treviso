content = open('index.html', 'r', encoding='utf-8').read()

# 1. Cores: azul vibrante
content = content.replace('--azul-escuro:   #071529;', '--azul-escuro:   #021a5e;')
content = content.replace('--azul:          #1056A8;', '--azul:          #0D47C8;')
content = content.replace('--azul-medio:    #1565C0;', '--azul-medio:    #1056D0;')
content = content.replace('--azul-claro:    #1E88E5;', '--azul-claro:    #5B9BFF;')
content = content.replace('--destaque-bg:   rgba(255,215,0,0.12);', '--destaque-bg:   rgba(255,255,255,0.1);')

# 2. Backgrounds azul vibrante
content = content.replace(
    'background: linear-gradient(135deg, #032166 0%, #0D47C8 100%);',
    'background: linear-gradient(135deg, #021a5e 0%, #0D47C8 100%);'
)
content = content.replace(
    'background: linear-gradient(160deg, #0d3a7a 0%, #0a2a6e 40%, #071f52 100%);',
    'background: linear-gradient(160deg, #0D47C8 0%, #0A35A0 50%, #021a5e 100%);'
)
content = content.replace('#0d2847 0%, var(--azul-escuro) 70%', '#0a35a0 0%, #021a5e 70%')
content = content.replace(
    'background: linear-gradient(180deg, var(--azul-escuro) 0%, #040e1e 100%);',
    'background: linear-gradient(180deg, #021a5e 0%, #010f3a 100%);'
)

# 3. Remover emoji do destaque-header
content = content.replace('<div class="destaque-emoji" id="dest-emoji">&#x1F414;</div>', '')
content = content.replace('<div class="destaque-emoji" id="dest-emoji">\U0001f414</div>', '')

open('index.html', 'w', encoding='utf-8').write(content)
print('cores OK')
