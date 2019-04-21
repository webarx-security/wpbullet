import argparse
from core import scanner


def main():
    parser = argparse.ArgumentParser(description='Specify scan parameters.')

    parser.add_argument('--path', type=str, dest='path', help='Path to plugin to analyze')
    parser.add_argument('--enabled', type=str, dest='enabled', help='Modules to enable', default="")
    parser.add_argument('--disabled', type=str, dest='disabled', help='Modules to disable', default="")

    args = parser.parse_args()

    if args.path is None:
        argparse.ArgumentParser.print_usage(parser)
        exit(1)

    scanner.scan(args)


if __name__ == '__main__':
    main()
