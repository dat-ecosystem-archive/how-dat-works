import os
import subprocess
import re

# This script converts SVG images into PNG.
# Requires Python 3, Inkscape and pngquant.

self_dir = os.path.dirname(__file__)
svg_dir = os.path.join(self_dir, "svg")
png_dir = os.path.join(self_dir, "png")

for svg_name in os.listdir(svg_dir):
    svg_path = os.path.join(svg_dir, svg_name)
    base, ext = os.path.splitext(svg_name)
    if ext == ".svg":
        png_name = "{0}.png".format(base)
        png_path = os.path.join(png_dir, png_name)
        if not os.path.exists(png_path) or os.path.getmtime(svg_path) > os.path.getmtime(png_path):
            print(svg_name)
            subprocess.run(["inkscape", "-z", "-e", png_path, "-d", "192", svg_path])
            subprocess.run(["pngquant", "--ext", ".png", "--force", "--skip-if-larger", "--strip", png_path])
