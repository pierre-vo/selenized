#!/bin/bash
grep -ioE "#[0-9a-f]{6}" "$1" | tr [[:upper:]] [[:lower:]] | sort -u
