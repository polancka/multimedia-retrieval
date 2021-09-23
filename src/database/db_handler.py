#!/usr/bin/env python

import os
import trimesh

class Shape:

    def __init__(self, mesh: trimesh.Trimesh, filepath: str):
        self._mesh = mesh
        self._filepath = filepath
        self._filename = os.path.basename(filepath)
        self._shape_class = os.path.basename(os.path.dirname(filepath))
        self._faces_type = self._determine_faces_type(mesh)
        self._num_faces = self._count_faces(mesh)
        self._num_vertices = self._count_vertices(mesh)

    def _determine_faces_type(self, mesh):
        return "None"

    def _count_faces(self, mesh):
        return 0

    def _count_vertices(self, mesh):
        return 0

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, mesh_):
        self._mesh = mesh_
        self._faces_type = _determine_faces_type(self._mesh)
        self._num_faces = _count_faces(self._mesh)
        self._num_vertices = _count_vertices(self._mesh)

    @property
    def num_faces(self):
        return self._num_faces

    @property
    def num_vertices(self):
        return self._num_vertices

    @property
    def faces_type(self):
        return self._faces_type

    @property
    def shape_class(self):
        return self._shape_class

    @property
    def filename(self):
        return self._filename

    @property
    def filepath(self):
        return self._filepath


def determine_paths(root: str, extension=".off"):

    paths = []
    for dirpath, _, files in os.walk(root):
        for name in files:
            if name.lower().endswith(extension):
                paths.append(os.path.join(dirpath, name))

    return paths


def load_shape(path: str) -> Shape:
    """ Load a shape from a file.

    Parameters
    ----------
    path : str
        The path to load the mesh from.
    """
    _mesh = trimesh.load(path, force="mesh")

    return Shape(_mesh, path)


def save_shape(shape: Shape, new_root=None):
    """ Save a given shape to some file

    Parameters
    ----------
    shape :  database.db_handler.Shape
        Shape to store.
    new_root :  str, optional
        Set a new root directory of the file
    """

    save_filepath = shape.filepath
    if new_root is not None:
        save_filepath = os.path.join(new_root, shape.shape_class, shape.filename)

    if not os.path.isdir(os.path.dirname(save_filepath)):
        os.makedirs(os.path.dirname(save_filepath))

    shape.mesh.export(save_filepath)

    return Shape(shape.mesh, save_filepath)

