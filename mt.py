#!/usr/bin/env python

import sys
import argparse
import freeze

def build(**kwargs):

    print('kwargs: ', kwargs)

def deploy(**kwargs):
    print('kwargs: ', kwargs)

def update_db(**kwargs):
    print('kwargs: ', kwargs)

def help(**kwargs):
    print('kwargs: ', kwargs)

def parse_args():


    parser = argparse.ArgumentParser(description='machine tone website deployment tool')
    subparser = parser.add_subparsers(dest='command')

    parser_build = subparser.add_parser('build', help='generate a static version of the machine tone website')
    #parser_build.set_defaults(func=build)

    parser_deploy = subparser.add_parser('deploy', help='deploy the static build contents of ./build to the hosting server')
    #parser_deploy.set_defaults(func=deploy)

    parser_update_db = subparser.add_parser('update', help='update the database using new data in the machine tone web google sheet')
    parser_update_db.add_argument('--clean', help='prune the google sheet of all entries marked updated after pulling new data into the local sqlite database.', action='store_true') 
    #parser_update_db.set_defaults(func=update_db)

    return parser.parse_args(sys.argv[1:])

def run():

    args = vars(parse_args())
    command = args['command']
    commands = {
        'build': build,
        'deploy': deploy,
        'update': update_db
    }
    command = commands.get(command)


if __name__ == '__main__':
    run()
