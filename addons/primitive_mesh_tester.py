import bpy


def selectable(name, context):
    exist = name in bpy.data.objects
    selected = exist and bpy.data.objects[name].select_get()
    no_selected = len(context.selected_objects) == 0
    return selected or (not exist and no_selected)


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
        return selectable('Circle', context)

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
        return selectable('Cone', context)

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


class PRIM_TEST_OT_CubeProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.cube_props'
    bl_label = 'Cube'
    bl_options = {'REGISTER', 'UNDO'}

    size: bpy.props.FloatProperty(
        name='size', default=2.0, min=0.0, step=5
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        return selectable('Cube', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_cube_add(
            size=self.size,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_CylinderProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.cylinder_props'
    bl_label = 'Cylinder'
    bl_options = {'REGISTER', 'UNDO'}

    verts: bpy.props.IntProperty(
        name='vertices', default=32, min=3, max=100000000
    )
    radius: bpy.props.FloatProperty(
        name='radius', default=1.0, min=0.0, step=5
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
        return selectable('Cylinder', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_cylinder_add(
            vertices=self.verts,
            radius=self.radius,
            depth=self.depth,
            end_fill_type=self.end_fill_type,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_GridProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.grid_props'
    bl_label = 'Grid'
    bl_options = {'REGISTER', 'UNDO'}

    x_subdivisions: bpy.props.IntProperty(
        name='x_subdivisions', default=10, min=2, max=100000000
    )
    y_subdivisions: bpy.props.IntProperty(
        name='y_subdivisions', default=10, min=2, max=100000000
    )
    size: bpy.props.FloatProperty(
        name='size', default=2.0, min=0.0, step=5
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        return selectable('Grid', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_grid_add(
            x_subdivisions=self.x_subdivisions,
            y_subdivisions=self.y_subdivisions,
            size=self.size,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_IcoSphereProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.ico_sphere_props'
    bl_label = 'Icosphere'
    bl_options = {'REGISTER', 'UNDO'}

    subdivisions: bpy.props.IntProperty(
        name='subdivisions', default=2, min=1, max=10
    )
    radius: bpy.props.FloatProperty(
        name='radius', default=1.0, min=0.0, step=5
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        return selectable('Icosphere', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_ico_sphere_add(
            subdivisions=self.subdivisions,
            radius=self.radius,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_MonkeyProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.monkey_props'
    bl_label = 'Monkey'
    bl_options = {'REGISTER', 'UNDO'}

    size: bpy.props.FloatProperty(
        name='size', default=2.0, min=0.0, step=5
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        return selectable('Suzanne', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_monkey_add(
            size=self.size,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_PlaneProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.plane_props'
    bl_label = 'Plane'
    bl_options = {'REGISTER', 'UNDO'}

    size: bpy.props.FloatProperty(
        name='size', default=2.0, min=0.0, step=5
    )
    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )

    @classmethod
    def poll(cls, context):
        return selectable('Plane', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_plane_add(
            size=self.size,
            location=self.location,
            rotation=self.rotation
        )
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class PRIM_TEST_OT_TorusProps(bpy.types.Operator):
    bl_idname = 'prim_mesh_tester.torus_props'
    bl_label = 'Torus'
    bl_options = {'REGISTER', 'UNDO'}

    location: bpy.props.FloatVectorProperty(
        name='location', subtype='XYZ', step=5
    )
    rotation: bpy.props.FloatVectorProperty(
        name='rotation', subtype='EULER', step=5
    )
    major_segments: bpy.props.IntProperty(
        name='major_segments', default=48, min=3, max=256,
    )
    minor_segments: bpy.props.IntProperty(
        name='major_segments', default=12, min=3, max=256,
    )
    mode: bpy.props.EnumProperty(
        name='mode',
        items=[
            ('MAJOR_MINOR', 'Major/Minor',
             'Use the major/minor radii for torus dimensions.'),
            ('EXT_INT', 'Exterior/Interior',
             'Use the exterior/interior radii for torus dimensions.')
        ],
        default='MAJOR_MINOR'
    )
    major_radius: bpy.props.FloatProperty(
        name='major_radius', default=1.0, min=0.01, max=100.0, step=1
    )
    minor_radius: bpy.props.FloatProperty(
        name='minor_radius', default=0.25, min=0.01, max=100.0, step=1
    )
    abso_major_rad: bpy.props.FloatProperty(
        name='abso_major_rad', default=1.25, min=0.01, max=100.0, step=1
    )
    abso_minor_rad: bpy.props.FloatProperty(
        name='abso_minor_rad', default=0.75, min=0.01, max=100.0, step=1
    )

    @classmethod
    def poll(cls, context):
        return selectable('Torus', context)

    def execute(self, context):
        bpy.ops.object.delete()
        bpy.ops.mesh.primitive_torus_add(
            location=self.location,
            rotation=self.rotation,
            major_segments=self.major_segments,
            minor_segments=self.minor_segments,
            mode=self.mode,
            major_radius=self.major_radius,
            minor_radius=self.minor_radius,
            abso_major_rad=self.abso_major_rad,
            abso_minor_rad=self.abso_minor_rad
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
        layout.operator(PRIM_TEST_OT_CubeProps.bl_idname)
        layout.operator(PRIM_TEST_OT_CylinderProps.bl_idname)
        layout.operator(PRIM_TEST_OT_GridProps.bl_idname)
        layout.operator(PRIM_TEST_OT_IcoSphereProps.bl_idname)
        layout.operator(PRIM_TEST_OT_MonkeyProps.bl_idname)
        layout.operator(PRIM_TEST_OT_PlaneProps.bl_idname)
        # [TODO] Remove below comment out in the future after fixed torus add method.
        # layout.operator(PRIM_TEST_OT_TorusProps.bl_idname)


classes = (
    PRIM_TEST_OT_CircleProps,
    PRIM_TEST_OT_ConeProps,
    PRIM_TEST_OT_CubeProps,
    PRIM_TEST_OT_CylinderProps,
    PRIM_TEST_OT_GridProps,
    PRIM_TEST_OT_IcoSphereProps,
    PRIM_TEST_OT_MonkeyProps,
    PRIM_TEST_OT_PlaneProps,
    PRIM_TEST_OT_TorusProps,
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
