#!/usr/bin/env python

def compute_stats(shapes):

    faces_per_class = {}
    vertices_per_class = {}

    for shape in shapes:
        if shape.shape_class in faces_per_class:
            faces_per_class[shape.shape_class].append(shape.num_faces)
            vertices_per_class[shape.shape_class].append(shape.num_vertices)
        else:
            faces_per_class[shape.shape_class] = [ shape.num_faces ]
            vertices_per_class[shape.shape_class] = [ shape.num_vertices ]

    avrg_faces_per_class = dict.fromkeys(faces_per_class.keys())
    avrg_vertices_per_class = dict.fromkeys(vertices_per_class.keys())
    avrg_num_faces = 0
    avrg_num_vertices = 0
    num_faces = 0
    num_vertices = 0
    sum_faces = 0
    sum_vertices = 0

    for (shape_class, faces), (_, vertices) in zip(faces_per_class.items(), vertices_per_class.items()):
        sum_faces += sum(faces)
        sum_vertices += sum(vertices)
        num_faces += len(faces)
        num_vertices += len(vertices)
        avrg_faces_per_class[shape_class] = sum(faces) / len(faces)
        avrg_vertices_per_class[shape_class] = sum(vertices) / len(vertices)

    avrg_num_faces = sum_faces / num_faces
    avrg_num_vertices = sum_vertices / num_vertices

    return (avrg_num_faces, avrg_num_vertices,
            avrg_faces_per_class, avrg_vertices_per_class,
            faces_per_class, vertices_per_class)

