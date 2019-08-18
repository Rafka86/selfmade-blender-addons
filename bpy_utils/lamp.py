import os
import bpy
import numpy as np
import numpy.linalg as LA


class Lamp:
    def __init__(self, name='Lamp', type='POINT'):
        self.__lamp = (bpy.data.lamps[name] if name in bpy.data.lamps else
                       bpy.data.lamps.new(name, type))
        self.__object = (bpy.data.objects[name] if name in bpy.data.objects else
                         bpy.data.objects.new(name, self.__lamp))
        if name not in bpy.context.scene.objects:
            bpy.context.scene.objects.link(self.__object)
        self.focus_to = (0, 0, 0)

    @property
    def focus_to(self):
        return self.__focus_to

    @focus_to.setter
    def focus_to(self, target):
        [x, y, z] = np.subtract(target, self.__object.location)
        x_vec = np.array([-z, 0, y])
        y_vec = np.array([LA.norm((x, y, 0)), +0, -x])
        self.__object.rotation_euler = np.arctan2(y_vec, x_vec)
        self.__focus_to = target

    @property
    def location(self):
        return self.__object.location

    @location.setter
    def location(self, position):
        self.__object.location = position


if __name__ == "__main__":
    lamp = Lamp()
    lamp.location = (5, 5, 5)
    lamp.focus_to = (0, 0, 0)
