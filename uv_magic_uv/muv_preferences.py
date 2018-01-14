# <pep8-80 compliant>

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Nutti <nutti.metro@gmail.com>"
__status__ = "production"
__version__ = "4.5"
__date__ = "19 Nov 2017"

from bpy.props import (
    BoolProperty,
    FloatProperty,
    FloatVectorProperty,
)
from bpy.types import AddonPreferences


class MUV_Preferences(AddonPreferences):
    """Preferences class: Preferences for this add-on"""

    bl_idname = __package__

    # for UV Sculpt
    uvsculpt_brush_color = FloatVectorProperty(
        name="Color",
        description="Color",
        default=(1.0, 0.4, 0.4, 1.0),
        min=0.0,
        max=1.0,
        size=4,
        subtype='COLOR'
    )

    # for Overlapped UV
    uvinsp_overlapped_color = FloatVectorProperty(
        name="Color",
        description="Color",
        default=(0.0, 0.0, 1.0, 0.3),
        min=0.0,
        max=1.0,
        size=4,
        subtype='COLOR'
    )

    # for Flipped UV
    uvinsp_flipped_color = FloatVectorProperty(
        name="Color",
        description="Color",
        default=(1.0, 0.0, 0.0, 0.3),
        min=0.0,
        max=1.0,
        size=4,
        subtype='COLOR'
    )

    # for Texture Projection
    texproj_canvas_padding = FloatVectorProperty(
        name="Canvas Padding",
        description="Canvas Padding",
        size=2,
        max=50.0,
        min=0.0,
        default=(20.0, 20.0))

    # for UV Bounding Box
    uvbb_cp_size = FloatProperty(
        name="Size",
        description="Control Point Size",
        default=6.0,
        min=3.0,
        max=100.0)
    uvbb_cp_react_size = FloatProperty(
        name="React Size",
        description="Size event fired",
        default=10.0,
        min=3.0,
        max=100.0)

    def draw(self, _):
        layout = self.layout

        layout.label("Configuration:")

        layout.label("UV Sculpt:")
        sp = layout.split(percentage=0.05)
        col = sp.column()  # spacer
        sp = sp.split(percentage=0.3)
        col = sp.column()
        col.label("Brush:")
        col.prop(self, "uvsculpt_brush_color")

        layout.label("UV Inspection:")
        sp = layout.split(percentage=0.05)
        col = sp.column()  # spacer
        sp = sp.split(percentage=0.3)
        col = sp.column()
        col.label("Overlapped UV:")
        col.prop(self, "uvinsp_overlapped_color")
        sp = sp.split(percentage=0.5)
        col = sp.column()
        col.label("Flipped UV:")
        col.prop(self, "uvinsp_flipped_color")

        layout.label("Texture Projection:")
        sp = layout.split(percentage=0.05)
        col = sp.column()       # spacer
        sp = sp.split(percentage=0.3)
        col = sp.column()
        col.label("Texture Display: ")
        col.prop(self, "texproj_canvas_padding")

        layout.label("UV Bounding Box:")
        sp = layout.split(percentage=0.05)
        col = sp.column()       # spacer
        sp = sp.split(percentage=0.3)
        col = sp.column()
        col.label("Control Point: ")
        col.prop(self, "uvbb_cp_size")
        col.prop(self, "uvbb_cp_react_size")

        layout.label("Description:")
        column = layout.column(align=True)
        column.label("Magic UV is composed of many UV editing features.")
        column.label("See tutorial page if you are new to this add-on.")
        column.label("https://github.com/nutti/Magic-UV/wiki/Tutorial")

        layout.label("Location:")

        row = layout.row(align=True)
        sp = row.split(percentage=0.3)
        sp.label("View3D > U")
        sp = sp.split(percentage=1.0)
        col = sp.column(align=True)
        col.label("Copy/Paste UV Coordinates")
        col.label("Copy/Paste UV Coordinates (by selection sequence)")
        col.label("Flip/Rotate UVs")
        col.label("Transfer UV")
        col.label("Move UV from 3D View")
        col.label("Texture Lock")
        col.label("Mirror UV")
        col.label("World Scale UV")
        col.label("Unwrap Constraint")
        col.label("Preserve UV Aspect")
        col.label("UVW")

        row = layout.row(align=True)
        sp = row.split(percentage=0.3)
        sp.label("View3D > Object")
        sp = sp.split(percentage=1.0)
        col = sp.column(align=True)
        col.label("Copy/Paste UV Coordinates (Among same objects)")

        row = layout.row(align=True)
        sp = row.split(percentage=0.3)
        sp.label("ImageEditor > Property Panel")
        sp = sp.split(percentage=1.0)
        col = sp.column(align=True)
        col.label("Manipulate UV with Bounding Box in UV Editor")
        col.label("Align UV Cursor")

        row = layout.row(align=True)
        sp = row.split(percentage=0.3)
        sp.label("View3D > Property Panel")
        sp = sp.split(percentage=1.0)
        col = sp.column(align=True)
        col.label("Texture Projection")

        row = layout.row(align=True)
        sp = row.split(percentage=0.3)
        sp.label("ImageEditor > UVs")
        sp = sp.split(percentage=1.0)
        col = sp.column(align=True)
        col.label("Pack UV (with same UV island packing)")
