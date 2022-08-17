import re
replacements = {}
with open('selenized-dark.reverse-mapping') as f:
    pattern = re.compile(r'(#\w+) (\w+)')
    for line in f:
        m = pattern.search(line)
        if m:
            replacements[m.group(1)] = m.group(2)

print(replacements)
with open('Selenized Dark-color-theme.json') as infile:
    with open('Selenized Dark-color-theme.json.template', 'w') as outfile:
        p = re.compile(r'#[0-9a-f]{6}')
        for line in infile:
            m = p.search(line)
            if m and (m.group(0) in replacements):
                hexcolor = m.group(0)
                colorstr = replacements[hexcolor]
                repl = "!!COL!{" + colorstr + ".srgb}!"
                print(f"Replacing '{hexcolor}' with '{repl}'")
                line = p.sub(repl, line)

            # print(line)
            outfile.write(line)
