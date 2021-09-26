#!/usr/bin/env python


import matplotlib.pyplot as plt
import math

def plot_histogram(mean_faces, mean_vertices, mean_face_class, mean_vert_class,
                   face_class, vert_class):

    # All faces
    n_bins = 50
    all_faces = sum([f for (_, f) in face_class.items()], [])
    all_vertices = sum([f for (_, f) in vert_class.items()], [])
    plt.hist(all_vertices, bins=n_bins)
    plt.title("Vertex histogram over all shapes")
    plt.show()

    plt.hist(all_faces, bins=n_bins)
    plt.title("Faces histogram over all shapes")
    plt.show()

    # Vertices per class
    sub_rows, sub_cols = _determine_subs(len(face_class.keys()))
    fig, axes = plt.subplots(sub_rows, sub_cols)
    fig.tight_layout()

    row = 0
    col = 0
    for shape_class, faces in face_class.items():
        axes[row, col].set_title(shape_class)
        axes[row, col].hist(faces)
        axes[row,col].axvline(mean_faces, color='red', linestyle='dashed', linewidth=1)
        axes[row,col].axvline(sum(faces) / len(faces), color='blue', linestyle='dashed', linewidth=1)
        row = (row + 1) % sub_rows
        col = (col + 1) % sub_cols

    plt.show()

    sub_rows, sub_cols = _determine_subs(len(face_class.keys()))
    fig, axes = plt.subplots(sub_rows, sub_cols)
    fig.tight_layout()

    row = 0
    col = 0
    for shape_class, vertices in vert_class.items():
        axes[row, col].set_title(shape_class)
        axes[row, col].hist(vertices)
        axes[row,col].axvline(mean_vertices, color='red', linestyle='dashed', linewidth=1)
        axes[row,col].axvline(sum(vertices) / len(vertices), color='blue', linestyle='dashed', linewidth=1)
        row = (row + 1) % sub_rows
        col = (col + 1) % sub_cols


    plt.show()


def _determine_subs(num):

    sqrt = math.sqrt(num)
    subs = ()
    if math.floor(sqrt) == sqrt:
        subs = (sqrt, sqrt)
    else:
        subs = (math.floor(sqrt), math.ceil(sqrt))
    return subs

