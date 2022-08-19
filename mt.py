#!/usr/bin/env python

import sys
import argparse

def parse_args():

    def build(args):
        print('build!')

    def deploy(args):
        print('deploy!')

    def update_db(args):
        print('update db!')


    parser = argparse.ArgumentParser(description='machine tone website deployment tool')
    subparsers = parser.add_subparsers()

    parser_build = subparsers.add_parser('build', help='generate a static version of the machine tone website')
    parser_build.set_defaults(func=build)

    parser_deploy = subparsers.add_parser('deploy', help='deploy the static build contents of ./build to the hosting server')
    parser_deploy.set_defaults(func=deploy)

    parser_update_db = subparsers.add_parser('update', help='update the database using new data in the machine tone web google sheet')
    parser_update_db.add_argument('--clean', help='prune the google sheet of all entries marked updated after pulling new data into the local sqlite database.')
    parser_update_db.set_defaults(func=update_db)

    return parser.parse_args(sys.argv[1:])

def run():

    args = parse_args()

    # TODO: doesn't call help if you just call 'mt.py'
    args.func(args)


if __name__ == '__main__':
    run()
