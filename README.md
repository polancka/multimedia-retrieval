# Multimedia Retrieval
Group project which implements a multimedia retrieval pipeline for 3D shapes.

# Setup

This multimedia retrieval project is implemented in Python. The corresponding version is [Python 3.9](https://docs.python.org/3/).

In order to run the application, it is recommended to create a [virtual environment](https://docs.python.org/3/tutorial/venv.html). Run the following command to create it:

```
# Linux
python3.9 -m venv <path-to-virtual-environment>

# Windows
py -m venv <path-to-virtual-environment>
```

Before running the application, the venv has to be activated. This step has to be performed (once) every time the application shall be used.

```
# Linux
source <path-to-virtual-environment>/bin/activate

# Windows
<path-to-virtual-environment>/Scripts/activate
```

When the venv was activated, all necessary packages have to be installed.
The file `src/requirements.txt` provides all Python modules and corresponding version. Install them via:

```
pip install -r src/requirements.txt
```

Now, the setup has been completed successfully!

# Usage

Run the application via the following command and get helpful information:

```
src/main.py -h
```


## Render a Mesh

Simply render a given mesh with the `--show` option:

```
src/main.py -s <path/to/mesh.off/.ply>
```
