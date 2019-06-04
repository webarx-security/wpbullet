import argparse
from core import scanner
import signal
import sys


def signal_handler(sig, frame):
    sys.exit(0)


# Register signal handler
signal.signal(signal.SIGINT, signal_handler)


def main():
    parser = argparse.ArgumentParser(description='Specify scan parameters.')

    parser.add_argument('--path', type=str, dest='path', help='Path to plugin to analyze')
    parser.add_argument('--enabled', type=str, dest='enabled', help='Modules to enable', default="")
    parser.add_argument('--disabled', type=str, dest='disabled', help='Modules to disable', default="")
    parser.add_argument('--cleanup', type=bool, dest='cleanup', help='Clean .temp folder after scanning remotely '
                                                                     'downloaded plugin', default=False)
    parser.add_argument('--report', type=bool, dest='report', help='Saves JSON report inside reports folder', default=False)

    args = parser.parse_args()

    if args.path is None:
        argparse.ArgumentParser.print_usage(parser)
        exit(1)

    scanner.scan(args)


if __name__ == '__main__':
    main()
