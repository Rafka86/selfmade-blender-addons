import bpy


class PRIM_TEST_OT_ConeProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.cone_props'
    bl_label = 'Cone'
    bl_options = {'REGISTER', 'UNDO'}

    rad1: bpy.props.FloatProperty(name='radius1', default=1.0, min=0.0, step=1)
    rad2: bpy.props.FloatProperty(name='radius2', min=0.0, step=1)

    @classmethod
    def poll(cls, context):
        exist_cone = 'Cone' in bpy.data.objects
        cone_selected = exist_cone and bpy.data.objects['Cone'].select_get()
        no_selected = len(context.selected_objects) == 0
        return cone_selected or (not exist_cone and no_selected)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_cone_add(
            radius1=self.rad1,
            radius2=self.rad2
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_PT_MeshPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mesh Test'
    bl_label = 'Meshes'

    def draw(self, context):
        layout = self.layout
        layout.operator('prim_mesh_tester.cone_props')


classes = (
    PRIM_TEST_OT_ConeProps,
    PRIM_TEST_PT_MeshPanel,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == '__main__':
    bpy.data.objects.remove(bpy.data.objects['Cube'])
    register()
