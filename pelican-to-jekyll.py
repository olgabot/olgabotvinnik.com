#!/usr/bin/env python2
import argparse
import pypandoc
import os.path
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
      header, content = parse_post(post)
      new_content = convert_to_markdown(header, content)
    except Exception as error1:
      print 'failed to convert', post, error1
      print "... trying to encode as UTF-8 and use pandoc to convert from html to markdown"
      try:
          new_content = pypandoc.convert(content.encode('utf-8'), "html", "markdown")
          new_content = new_content.encode('ascii')
      except Exception as error2:
        print 'failed to convert', post, error2
    save_file(header['slug'], new_content, output_dir)

def create_header_string(header):
  header_string = '---\n'
  header_string += 'title: "{title}"\n'.format(title=header['title'])
  header_string += 'date: {datetime}\n'.format(datetime=header['datetime'])
  header_string += 'draft: false\n'
  header_string += 'tags: [{tags}]\n'.format(tags=header.get('tags', '').lower())
  header_string += 'categories: [{category}]\n'.format(category=header['category'].lower())
  header_string += '---\n\n'
  return header_string

def fix_links(link_map, content):
  for key, value in link_map.items():
    value = re.sub(r'\|filename\|', '{{ site.url }}', value)
    link_expression = '[' + key + '](' + value + ')'
    content = re.sub((r'`{0,2}%s`{0,2}\\\s*\\?(\s*\*|__?)' % key), link_expression, content)
  return content

def convert_to_markdown(header, content):
  header_string = create_header_string(header)
  if '<p>' in content:
    markdown_content = pypandoc.convert(content, 'html', 'md')
  else:
    markdown_content = content
  return header_string + markdown_content

def parse_post(post):
  header = {}
  key_value_regex = re.compile(r'^(?P<key>[^:]*):\s+(?P<value>.*)$')
  found_summary = False

  with open(post, mode='r', encoding='utf-8') as f:
    content = f.read().split('\n')

  for index, line in enumerate(content):
    # # Title is always the first line
    # if index == 0:
    #   header['title'] = line

    # if found_summary:
    if line == '':
      break
      # else:
      #   header['summary'] += ' ' + line.strip()

    match = re.match(key_value_regex, line)
    if re.match(key_value_regex, line):
      key, value = match.group('key'), match.group('value').strip()
      key = key.lower().strip('#')
      value = value.strip('"')

      if key == 'slug':
        # Strip out the date if it's there
        if value.startswith('201'):
          value = '-'.join(value.split('-')[3:])
        
      header[key] = value

      # if key == 'summary':
      #   found_summary = True


      if key == 'date':
        date = value.replace(' ', "T") 
        if not date.endswith('04:00'):
          date += '-07:00'
        header['datetime'] = date

      # Add tags and category if they're not there already
      header.setdefault('tags', '')
      header.setdefault('category', '')
      header.setdefault('slug', header['title'].lower().replace(' ', '-'))

  content = '\n'.join(content[index:])
  # link_map_regex = r'^.. _(?P<key>[^:]+):\s+(?P<value>.*)$'
  # link_map = dict(re.findall(link_map_regex, content, re.MULTILINE))

  return header, content

def save_file(slug, content, output_dir):
  file_name = '{slug}.md'.format(slug=slug)
  with open(os.path.join(output_dir, file_name), 'w', encoding='utf8') as f:
    f.write(content)

if __name__ == '__main__':
  main()