#!/usr/bin/env python3
from argparse import ArgumentParser, Namespace

from scanning.scanner import Scanner


def scan(arguments: Namespace):
    """Scan sites."""
    scanner = Scanner()
    if arguments.concurrent:
        scanner.concurrent = arguments.concurrent

    domains = None
    if arguments.domains_from_file:
        with open(arguments.domains_from_file, 'r') as fh:
            domains = fh.read().splitlines()

    scanner.scan_sites(arguments.count, domains=domains, skip=arguments.skip)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('count', type=int, default=1000)
    parser.add_argument('--concurrent', '-c', type=int, default=80)
    parser.add_argument('--skip', '-s', type=int, default=0)
    parser.add_argument('--domains-from-file', type=str, help='Read newline-separated URLs from file instead of majestic million')
    scan(parser.parse_args())
