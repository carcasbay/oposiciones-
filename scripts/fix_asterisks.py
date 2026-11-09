"""
Script to fix all unformatted markdown asterisks in HTML files in andalucia_comun.
Specifically:
1. Cover/header and body: **bold** -> <strong>bold</strong>
2. Titles, TOC, and body: *italic* -> <em>italic</em>
3. Diagrams inside <pre>: remove all * and pad box-drawing table rows with spaces to keep column alignments.
4. Paragraphs containing lines starting with '*' or numbers: transform into proper <ul>/<li> lists.
"""

import os
import glob
import re
import sys

def fix_pre_block(pre_content):
    # Inside <pre>, do not use HTML tags that break character widths.
    # Strip any * and keep table column widths.
    lines = pre_content.split('\n')
    new_lines = []
    for line in lines:
        if '*' in line:
            if '│' in line:
                parts = line.split('│')
                new_parts = []
                for p in parts:
                    clean_p = p.replace('*', '')
                    diff = len(p) - len(clean_p)
                    if diff > 0:
                        clean_p += ' ' * diff
                    new_parts.append(clean_p)
                new_lines.append('│'.join(new_parts))
            else:
                new_lines.append(line.replace('*', ''))
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def fix_paragraph_bullets(p_inner):
    """
    If p_inner contains lines that start with * or numbered bullets,
    split into paragraph intro and clean <ul><li> lists.
    """
    lines = p_inner.split('\n')
    has_bullets = any(re.match(r'^\s*\*+\s+', l) for l in lines)
    if not has_bullets:
        return f'<p>{p_inner}</p>'
    
    output = []
    p_lines = []
    current_list = [] # list of (indent_level, text)

    def flush_list():
        nonlocal current_list
        if not current_list:
            return
        output.append('<ul>')
        for indent, text in current_list:
            if indent > 0:
                output.append(f'  <li style="margin-left: {indent * 1.5}rem;">{text}</li>')
            else:
                output.append(f'  <li>{text}</li>')
        output.append('</ul>')
        current_list = []

    for line in lines:
        stripped = line.strip()
        m_bullet = re.match(r'^(\s*)\*+\s+(.*)$', line)
        m_num = re.match(r'^(\s*)(\d+\.)\s+(.*)$', line)

        if m_bullet:
            if p_lines:
                output.append('<p>' + '\n'.join(p_lines) + '</p>')
                p_lines = []
            indent_spaces = len(m_bullet.group(1))
            indent_level = 1 if indent_spaces >= 2 else 0
            current_list.append((indent_level, m_bullet.group(2)))
        elif m_num and current_list:
            indent_spaces = len(m_num.group(1))
            indent_level = 1 if indent_spaces >= 2 else 0
            current_list.append((indent_level, f'<strong>{m_num.group(2)}</strong> {m_num.group(3)}'))
        else:
            if current_list:
                flush_list()
            if stripped:
                p_lines.append(stripped)

    if p_lines:
        output.append('<p>' + '\n'.join(p_lines) + '</p>')
    if current_list:
        flush_list()

    return '\n'.join(output)

def fix_html_content(html):
    # 1. Protect <style> blocks
    styles = []
    def save_style(m):
        styles.append(m.group(0))
        return f'___STYLE_{len(styles)-1}___'
    html = re.sub(r'<style.*?>.*?</style>', save_style, html, flags=re.DOTALL)

    # 2. Fix <pre> blocks
    pres = []
    def save_pre(m):
        fixed_pre = fix_pre_block(m.group(1))
        pres.append(f'<pre>{fixed_pre}</pre>')
        return f'___PRE_{len(pres)-1}___'
    html = re.sub(r'<pre>(.*?)</pre>', save_pre, html, flags=re.DOTALL)

    # 3. Fix paragraph bullets
    def replace_p(m):
        inner = m.group(1)
        return fix_paragraph_bullets(inner)
    html = re.sub(r'<p>(.*?)</p>', replace_p, html, flags=re.DOTALL)

    # 4. Also check callout boxes if they have bullets inside
    def fix_callout(m):
        callout_inner = m.group(1)
        return '<div class="callout">' + re.sub(r'<p>(.*?)</p>', replace_p, callout_inner, flags=re.DOTALL) + '</div>'
    html = re.sub(r'<div class="callout">(.*?)</div>', fix_callout, html, flags=re.DOTALL)

    # 5. Convert **bold** in text to <strong>bold</strong>
    html = re.sub(r'\*\*([^\*\n\r]+?)\*\*', r'<strong>\1</strong>', html)

    # 6. Convert *italics* like *ultra vires*, *ex tunc*, *iuris tantum*, etc.
    html = re.sub(r'(?<!\*)\*([a-zA-Z0-9_\-áéíóúÁÉÍÓÚñÑüÜ,/ ]{2,60}?)\*(?!\*)', r'<em>\1</em>', html)

    # 7. Clean any remaining stray "* " at the beginning of lines or after <p> or <br>
    html = re.sub(r'(<p>|<br\s*/?>|\n)\s*\*\s+', r'\1', html)

    # 8. Restore <pre> blocks
    for idx, p in enumerate(pres):
        html = html.replace(f'___PRE_{idx}___', p)

    # 9. Restore <style> blocks
    for idx, s in enumerate(styles):
        html = html.replace(f'___STYLE_{idx}___', s)

    return html

def process_all_files():
    files = sorted(glob.glob('andalucia_comun/*.html'))
    print(f'Processing {len(files)} files in andalucia_comun/...')
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            orig = fp.read()
        fixed = fix_html_content(orig)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(fixed)
        
        # Check remaining asterisks in visible body
        body_no_style = re.sub(r'<style.*?>.*?</style>', '', fixed, flags=re.DOTALL)
        rem_doubles = body_no_style.count('**')
        rem_singles = body_no_style.count('*')
        print(f'{os.path.basename(f)}: Remaining in body: **={rem_doubles}, *={rem_singles}')

if __name__ == '__main__':
    process_all_files()
