#!/usr/bin/env python

import sys
import argparse
import numpy as np
import trimesh
import database.loader as dbh
import statistics.histogram as stat
import visualization.viewer as vis
from tqdm import tqdm
from joblib import Parallel, delayed


def perform_show(options):
    mesh = trimesh.load(options.path, force="mesh")
    mesh.show()
    # TODO: Add nice opengl stuff


def perform_stats(options):
    shape_paths = dbh.determine_paths(options.path)
    print("Loading models (%i)" % len(shape_paths))

    # Parallel loading
    job_delays = [delayed(dbh.load_shape)(path) for path in shape_paths]
    shapes = Parallel(n_jobs = 12)(delayed(dbh.load_shape)(path) for path in tqdm(shape_paths))

    # Serial loading
    #shapes = []
    # for path in tqdm(shape_paths):
    #     shapes.append(dbh.load_shape(path))

    (mean_f, mean_v, mean_f_c, mean_v_c, f_c, v_c) = stat.compute_stats(shapes)
    print("Mean faces: %i" % mean_f)
    print("Mean vertices: %i" % mean_v)
    vis.plot_histogram(mean_f, mean_v, mean_f_c, mean_v_c, f_c, v_c)
    # TODO: Plot stuff


def perform_normalize(options):
    print("Normalize!")
    # TODO: Add normalization


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

    # Prepare "normalize" parser
    norm_parser = subparser.add_parser("normalize", help="Perform normalization (and refinement) on a dataset")
    norm_parser.add_argument("input", help="Path to the non-normalized dataset")
    norm_parser.add_argument("output", help="Destination root folder for the resulting dataset")

    options = parser.parse_args()


    # Evaluate parameters
    if options.command == "show":
        perform_show(options)
    elif options.command == "stats":
        perform_stats(options)
    elif options.command == "normalize":
        perform_normalize(options)
    else:
        print("No command given!")


if __name__ == "__main__":
    main()

