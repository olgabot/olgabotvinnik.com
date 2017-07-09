#!/usr/bin/env python2
import argparse
import dateutil.parser
import inflection
import os.path
import pypandoc
import re

from codecs import open

def main():
  parser = argparse.ArgumentParser(description='Migrate Pelican RST posts to Jekyll Markdown')
  parser.add_argument('input', help='path to posts', nargs='*')
  parser.add_argument('output', help='output directory', default='_posts')
  args = parser.parse_args()

  convert_posts(args.input, args.output)

def convert_posts(posts, output_dir):
  for post in posts:
    print 'converting:', post
    try:
      header, link_map, content = parse_post(post)
      markdown_content = convert_to_jekyll(header, link_map, content)
      save_file(header['date'], header['slug'], markdown_content, output_dir)
    except Exception as error:
      print 'failed to convert', post, error

def create_header_string(header):
  header_string = '---\n'
  header_string += 'layout: post\n'
  header_string += 'title: {title}\n'.format(title=header['title'])
  header_string += 'date: {datetime}\n'.format(datetime=header['datetime'])
  header_string += 'category: {category}\n'.format(category=header['category'].lower())
  header_string += 'tags: {tags}\n'.format(tags=header.get('tags', '').lower())
  header_string += '---\n\n'
  return header_string

def fix_links(link_map, content):
  for key, value in link_map.items():
    value = re.sub(r'\|filename\|', '{{ site.url }}', value)
    link_expression = '[' + key + '](' + value + ')'
    content = re.sub((r'`{0,2}%s`{0,2}\\\s*\\?(\s*\*|__?)' % key), link_expression, content)
  return content

def convert_to_jekyll(header, link_map, content):
  header_string = create_header_string(header)
  markdown_content = pypandoc.convert(content, 'rst', 'md')
  markdown_content = fix_links(link_map, markdown_content)
  return header_string + markdown_content

def parse_post(post):
  header = {}
  key_value_regex = re.compile(r'^:(?P<key>[^:]*):\s+(?P<value>.*)$')
  found_summary = False

  with open(post, mode='r', encoding='utf-8') as f:
    content = f.read().split('\n')

  for index, line in enumerate(content):
    # Title is always the first line
    if index == 0:
      header['title'] = line

    if found_summary:
      if line == '':
        break
      else:
        header['summary'] += ' ' + line.strip()

    match = re.match(key_value_regex, line)
    if re.match(key_value_regex, line):
      key, value = match.group('key'), match.group('value').strip()
      header[key] = value

      if key == 'summary':
        found_summary = True

      if key == 'date':
        header[key] = dateutil.parser.parse(value).date().isoformat()
        header['datetime'] = value

  content = '\n'.join(content[index:])
  link_map_regex = r'^.. _(?P<key>[^:]+):\s+(?P<value>.*)$'
  link_map = dict(re.findall(link_map_regex, content, re.MULTILINE))

  return header, link_map, content

def save_file(date, slug, content, output_dir):
  file_name = '{date}-{slug}.md'.format(date=date, slug=slug)
  with open(os.path.join(output_dir, file_name), r'w') as f:
    f.write(content)

if __name__ == '__main__':
  main()