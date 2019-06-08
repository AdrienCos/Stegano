#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Stegano - Stegano is a basic Python Steganography module.
# Copyright (C) 2010-2019  Cédric Bonhomme - https://www.cedricbonhomme.org
#
# For more information : https://github.com/cedricbonhomme/Stegano
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.9.4 $"
__date__ = "$Date: 2010/10/01 $"
__revision__ = "$Date: 2019/06/07 $"
__license__ = "GPLv3"

from PIL import Image


def steganalyse(img: Image.Image) -> Image.Image:
    """
    Steganlysis of the LSB technique. 
    Extracts the LSB layer of the given image and outputs it as a greyscale image.
    """
    encoded = Image.new("L", (img.size))
    width, height = img.size
    mask = (2 ** 1 - 1)
    factor = int(255 / mask)
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))[0:3]
            # Extract the LSB
            r = (r & mask)
            g = (g & mask)
            b = (b & mask)
            # Convert to RGB and scale up to 255
            value = int(factor * (r+g+b)/3)
            encoded.putpixel((col, row), (value))
    return encoded
