#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jonas Gröger <jonas.groeger@gmail.com>'


import argparse


def main(filename, url):
	with open(filename + '.url', 'w') as f:
		f.write('[InternetShortcut]\r\n')
		f.write('URL=' + url)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', help='The filename without .url')
	parser.add_argument('url', help='The URL for the shortcut')
	args = parser.parse_args()
	main(args.filename, args.url)
