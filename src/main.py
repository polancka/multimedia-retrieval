#!/usr/bin/env python

import sys
import argparse
import numpy as np
import trimesh
import database.db_handler as dbh
import statistics.histogram as stat


def perform_show(options):
    mesh = trimesh.load(options.path, force="mesh")
    mesh.show()


def perform_stats(options):
    print("Statistics!")
    shape_paths = dbh.determine_paths(options.path)
    i = 0
    shapes = []
    for path in shape_paths:
        shapes.append(dbh.load_shape(path))

        i += 1
        if i >= 20:
            break

    (mean_f, mean_v, mean_f_c, mean_v_c, f_c, v_c) = stat.compute_stats(shapes)


def perform_refine(options):
    print("Refine!")


def perform_normalize(options):
    print("Normalize!")


def main():

    # Prepare parser
    parser = argparse.ArgumentParser("Multimedia Retrieval")
    subparser = parser.add_subparsers(dest="command")

    # Prepare "show" parser
    show_parser = subparser.add_parser("show", help="Visualize a shape")
    show_parser.add_argument("path", help="Path to the mesh file which shall be displayed [.off/.ply]")

    # Prepare "stats" parser
    show_parser = subparser.add_parser("stats", help="Create statistical information for a dataset")
    show_parser.add_argument("path", help="Path to the dataset")

    # Prepare "refine" parser
    refine_parser = subparser.add_parser("refine", help="Perform refinement on a dataset")
    refine_parser.add_argument("input", help="Path to the unrefined dataset")
    refine_parser.add_argument("output", help="Destination root folder for the resulting dataset")

    # Prepare "normalize" parser
    norm_parser = subparser.add_parser("normalize", help="Perform normalization on a dataset")
    norm_parser.add_argument("input", help="Path to the non-normalized dataset")
    norm_parser.add_argument("output", help="Destination root folder for the resulting dataset")

    options = parser.parse_args()


    # Evaluate parameters
    if options.command == "show":
        perform_show(options)
    elif options.command == "stats":
        perform_stats(options)
    elif options.command == "refine":
        perform_refine(options)
    elif options.command == "normalize":
        perform_normalize(options)
    else:
        print("No command given!")



if __name__ == "__main__":
    main()

