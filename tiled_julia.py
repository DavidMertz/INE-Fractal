#!/usr/bin/env python
from gzip import GzipFile
from pickle import dumps
import numpy as np
from fractal.julia import fast_julia
from fractal.visualize import make_canvas
from utility.exchange import make_archive

# We take random 0.5 wide/tall sections of the complex plane to render
# Choose 100 random center points
np.random.seed(1)  # Deterministic for now
zs = np.random.normal(scale=0.5, size=(100, 2)).round(1).view(complex)

# Generate and archive each section
for z in zs:
    canvas = make_canvas(fast_julia, z.real, z.imag, 0.5, pixels=512)
    name = f"Julia centered at {z}"
    archive = make_archive(canvas, comment=name)
    with GzipFile(f"{name}.pkl.gz", 'w') as gz:
        gz.write(dumps(archive))
    print(f"Saved {name}")
