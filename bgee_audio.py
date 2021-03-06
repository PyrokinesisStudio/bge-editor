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

import bpy
from . import bgee_config

class GameEditorAudioPanel(bpy.types.Panel):
    bl_idname = "bgee_audio_panel"
    bl_label = "Audio"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = bgee_config.GAME_EDITOR_TAB
            
    def draw(self, context):
        gm = context.blend_data.objects["GameManager"]
        layout = self.layout
        row = layout.row(align=True)
        row.prop(gm, "AudioVolume")
