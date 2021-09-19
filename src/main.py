#!/usr/bin/env python

import sys
import argparse
import numpy as np
import trimesh



def main():

  # Parse arguments
  parser = argparse.ArgumentParser("Multimedia Retrieval")
  parser.add_argument("-s", "--show", metavar="path", type=str,
                       help="Display the given mesh file.")
  options = parser.parse_args()


  # Evaluate arguments
  if options.show is not None:
    # trimesh.util.attach_to_log()
    mesh = trimesh.load(options.show, force="mesh")
    mesh.show()


if __name__ == "__main__":
  main()

