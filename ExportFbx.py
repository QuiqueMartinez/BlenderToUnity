import bpy
import os

# Export selected objects to fbx (compatible with Unity coordinate frame)
def export_selected_objects_to_fbx(base_path, apply_unit_scale=True, apply_scale_options='FBX_SCALE_UNITS', bake_space_transform=True):
    # Only select meshes
    selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
    
    for obj in selected_objects:
        obj_name = obj.name
        # By default, generated filename will be taken from object's name in Blender
        filepath = os.path.join(base_path, f"{obj_name}.fbx")
        
        # Deselect everything and select current object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        
        # Apply additional rotation in Z axis
        bpy.ops.transform.rotate(value=3.14159, orient_axis='Z')
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

     
        
        # Configure fbx export
        bpy.ops.export_scene.fbx(
            filepath=filepath,
            use_selection=True,
            apply_unit_scale=apply_unit_scale,
            apply_scale_options=apply_scale_options,
            bake_space_transform=bake_space_transform,
            object_types={'MESH'},
            axis_forward='-Z',
            axis_up='Y'
        )
        print(f"Exported {obj_name} to {filepath}")
        
        # Restore additional rotation in Z axis
        bpy.ops.transform.rotate(value=-3.14159, orient_axis='Z')
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
# Export to Unity project. 
# IMPORTANT!  Put the right path to the Assets directory shere.
base_export_path = "The path to the assets folder in your Unity Project."
export_selected_objects_to_fbx(base_export_path)
