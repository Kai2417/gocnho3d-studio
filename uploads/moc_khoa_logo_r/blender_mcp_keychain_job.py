import bpy
import math

bpy.ops.wm.read_factory_settings(use_empty=True)

# Import Base Plate STL & Raised Relief STL
bpy.ops.wm.stl_import(filepath=r"C:\Users\style\.gemini\antigravity\brain\f6ec75e5-5a23-4b11-94e4-fcb1f733a0d5\scratch\base_part.stl")
base_obj = bpy.context.selected_objects[0]
base_obj.name = "1_De_Nen_Base_Plate_2_2mm"

bpy.ops.wm.stl_import(filepath=r"C:\Users\style\.gemini\antigravity\brain\f6ec75e5-5a23-4b11-94e4-fcb1f733a0d5\scratch\relief_part.stl")
rel_obj = bpy.context.selected_objects[0]
rel_obj.name = "2_Chu_Noi_Va_Vien_Noi_1_0mm"

# Add Bevel & Weighted Normal modifiers for smooth industrial edges
for obj in (base_obj, rel_obj):
    bpy.context.view_layer.objects.active = obj
    bev = obj.modifiers.new(name="SmoothBevel", type='BEVEL')
    bev.width = 0.08
    bev.segments = 2
    bev.limit_method = 'ANGLE'
    bev.angle_limit = math.radians(35)
    bpy.ops.object.shade_auto_smooth(angle=math.radians(35))

# Create PBR Materials
mat_base = bpy.data.materials.new(name="Titanium_Dark_Base")
mat_base.use_nodes = True
bsdf_b = mat_base.node_tree.nodes.get("Principled BSDF")
if bsdf_b:
    bsdf_b.inputs["Base Color"].default_value = (0.18, 0.22, 0.28, 1.0)
    bsdf_b.inputs["Metallic"].default_value = 0.85
    bsdf_b.inputs["Roughness"].default_value = 0.32
base_obj.data.materials.append(mat_base)

mat_rel = bpy.data.materials.new(name="Brushed_Silver_Relief")
mat_rel.use_nodes = True
bsdf_r = mat_rel.node_tree.nodes.get("Principled BSDF")
if bsdf_r:
    bsdf_r.inputs["Base Color"].default_value = (0.88, 0.91, 0.95, 1.0)
    bsdf_r.inputs["Metallic"].default_value = 0.92
    bsdf_r.inputs["Roughness"].default_value = 0.18
rel_obj.data.materials.append(mat_rel)

# Center objects for GLB viewer
for obj in (base_obj, rel_obj):
    obj.location.x = -30.0
    obj.location.y = -14.25

# Export GLB
bpy.ops.export_scene.gltf(
    filepath=r"D:\Code\Studio_2D_to_3D\output\moc_khoa_logo_r\MOC_KHOA_LOGO_R_3D_PBR.glb",
    export_format='GLB',
    export_apply=True
)
print("BLENDER_GLB_EXPORT_OK:", r"D:\Code\Studio_2D_to_3D\output\moc_khoa_logo_r\MOC_KHOA_LOGO_R_3D_PBR.glb")
