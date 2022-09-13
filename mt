#!/usr/bin/env python

import sys
import argparse


# TODO: add color to output

# TODO: ignore certain urls
# might have to modify this fn: https://github.com/Frozen-Flask/Frozen-Flask/blob/e795c1869a70f3d3735b2f2b1d27dbddbac48368/flask_frozen/__init__.py#L396

# TODO: rsync copy only new/changed files. prune unused files.

def build(**kwargs):

    from freeze import freeze

    print('building static site...')
    freeze()
    print('build complete!')

    return False


def deploy(**kwargs):

    import os

    from dotenv import load_dotenv

    load_dotenv()
    build()

    mt_deploy_target = os.environ.get('MT_DEPLOY_TARGET') 
    if not mt_deploy_target:
        print("error: no MT_DEPLOY_TARGET found in environment.")
        return True 

    rc = os.system(f"rsync -aP build/ {mt_deploy_target}")
    if rc != 0:
        return True

    return False


def run():

    parser = argparse.ArgumentParser(description='machine tone website deployment tool')
    subparser = parser.add_subparsers(dest='command')

    parser_build = subparser.add_parser('build', help='generate a static version of the machine tone website')

    parser_deploy = subparser.add_parser('deploy', help='deploy the static build contents of ./build to the hosting server')

    args = vars(parser.parse_args(sys.argv[1:]))
    command = args['command']
    commands = {
        'build': build,
        'deploy': deploy,
    }

    command = commands.get(command)
    command_failed = False

    if command:
        command_failed = command()

        if command_failed:
            print('mt: command failed')

    else:
        parser.print_help()

    sys.exit(0)


if __name__ == '__main__':
    run()
