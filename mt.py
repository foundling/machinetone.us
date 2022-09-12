#!/usr/bin/env python

import sys
import argparse
from freeze import freeze

# check this out for example of subcommand w/ functioning help:
# https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html

def build(**kwargs):
    freeze()

def deploy(**kwargs):
    print('kwargs: ', kwargs)

def update_db(**kwargs):
    print('kwargs: ', kwargs)

def help(**kwargs):
    print('kwargs: ', kwargs)

def run():

    parser = argparse.ArgumentParser(description='machine tone website deployment tool')
    subparser = parser.add_subparsers(dest='command')

    parser_build = subparser.add_parser('build', help='generate a static version of the machine tone website')

    parser_deploy = subparser.add_parser('deploy', help='deploy the static build contents of ./build to the hosting server')

    parser_update_db = subparser.add_parser('update', help='update the database using new data in the machine tone web google sheet')
    parser_update_db.add_argument('--clean', help='prune the google sheet of all entries marked updated after pulling new data into the local sqlite database.', action='store_true') 

    args = vars(parser.parse_args(sys.argv[1:]))
    command = args['command']
    commands = {
        'build': build,
        'deploy': deploy,
        'update': update_db
    }
    command = commands.get(command)

    if command:
        command()
    else:
        parser.print_help()

    sys.exit(0)


if __name__ == '__main__':
    run()
