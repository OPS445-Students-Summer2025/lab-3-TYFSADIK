#!/usr/bin/env python3

"""
lab3d.py

Define functions using subprocess for OPS445 Lab 3, Investigation 2 - Part 2.
"""
import subprocess


def free_space():
    """Return the available space on the root filesystem (e.g. '797G') as a string."""
    # Use human-readable output to get units (G, M, etc.)
    output = subprocess.check_output(['df', '-h', '/'], text=True)
    lines = output.splitlines()
    if len(lines) < 2:
        raise RuntimeError("Unexpected df output")
    # Available space is the 4th column on the second line
    parts = lines[1].split()
    try:
        avail = parts[3]
    except IndexError:
        raise RuntimeError("Could not parse available space")
    return avail


if __name__ == '__main__':
    # Print only the available space value
    print(free_space())

