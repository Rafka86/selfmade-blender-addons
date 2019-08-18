import bpy


class PRIM_TEST_OT_CircleProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.circle_props'
    bl_label = 'Circle'
    bl_options = {'REGISTER', 'UNDO'}

    verts: bpy.props.IntProperty(
        name='vertices', default=32, min=3, max=100000000
    )
    radius: bpy.props.FloatProperty(
        name='radius', default=1.0, min=0.0, step=5
    )
    fill_type: bpy.props.EnumProperty(
        name='fill_type',
        items=[
            ('NOTHING', 'Nothing', 'Don’t fill at all.'),
            ('NGON', 'Ngon', 'Use ngons.'),
            ('TRIFAN', 'Triangle Fan', 'Use triangle fans.')
        ],
        default='NOTHING'
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        exist_circle = 'Circle' in bpy.data.objects
        circle_selected = exist_circle and bpy.data.objects['Circle'].select_get(
        )
        no_selected = len(context.selected_objects) == 0
        return circle_selected or (not exist_circle and no_selected)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_circle_add(
            vertices=self.verts,
            radius=self.radius,
            fill_type=self.fill_type,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_ConeProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.cone_props'
    bl_label = 'Cone'
    bl_options = {'REGISTER', 'UNDO'}

    verts: bpy.props.IntProperty(
        name='vertices', default=32, min=3, max=100000000
    )
    radius1: bpy.props.FloatProperty(
        name='radius1', default=1.0, min=0.0, step=5
    )
    radius2: bpy.props.FloatProperty(
        name='radius2', min=0.0, step=5
    )
    depth: bpy.props.FloatProperty(
        name='depth', default=2.0, min=0.0, step=5
    )
    end_fill_type: bpy.props.EnumProperty(
        name='end_fill_type',
        items=[
            ('NOTHING', 'Nothing', 'Don’t fill at all.'),
            ('NGON', 'Ngon', 'Use ngons.'),
            ('TRIFAN', 'Triangle Fan', 'Use triangle fans.')
        ],
        default='NGON'
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        exist_cone = 'Cone' in bpy.data.objects
        cone_selected = exist_cone and bpy.data.objects['Cone'].select_get()
        no_selected = len(context.selected_objects) == 0
        return cone_selected or (not exist_cone and no_selected)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_cone_add(
            vertices=self.verts,
            radius1=self.radius1,
            radius2=self.radius2,
            depth=self.depth,
            end_fill_type=self.end_fill_type,
            location=self.location,
            rotation=self.rotation
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
        layout.operator(PRIM_TEST_OT_CircleProps.bl_idname)
        layout.operator(PRIM_TEST_OT_ConeProps.bl_idname)


classes = (
    PRIM_TEST_OT_CircleProps,
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
