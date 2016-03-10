# -*- coding: utf-8 -*-

"""em: the technicolor cli emoji experience™

Usage:
  em <name>... [--no-copy]
  em add <name> <character>...

Options:
  -h --help     Show this screen.
  --no-copy     Does not copy emoji to clipboard.

Examples:

  $ em sparkle cake sparkles
  $ em heart

Notes:
  - If all names provided map to emojis, the resulting emojis will be
    automatically added to your clipboard.
  - Custom aliases for emoji sets are supported.
"""

from __future__ import absolute_import, print_function, unicode_literals

import sys
import json

from docopt import docopt


def parse_emojis(filename='emojis.json'):
    data = json.load(open(filename))

    return {k: v['char'] for k, v in data.iteritems()}


def parse_aliases(lookup, filename='aliases.json'):
    data = json.load(open(filename))

    return {k: [lookup[c] for c in v.split()] for k, v in data.iteritems()}

def translate(lookup, aliases, codes):
    output = []
    for code in sys.argv[1:]:
        if code[0] == ':' and code[-1] == ':':
            code = code[1:-1]

        if code in aliases:
            output.extend(aliases[code])
        else:
            output.append(lookup[code])

    return output


def cli():
    arguments = docopt(__doc__)
    # print(arguments)

    names = arguments['<name>']


    if arguments['add']:
        arguments['<charecter>']
        arguments['<name>']

    lookup = parse_emojis()
    aliases = parse_aliases(lookup)

    results = translate(lookup, aliases, names)
    print(' '.join(results))

if __name__ == '__main__':
    cli()