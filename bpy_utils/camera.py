import os
import bpy
import numpy as np
import numpy.linalg as LA


class Camera:
    def __init__(self, name='Camera'):
        self.dirpath = f'{os.getcwd()}/img/{name}/'
        self.__camera = (bpy.data.cameras[name] if name in bpy.data.cameras else
                         bpy.data.cameras.new(name))
        self.__object = (bpy.data.objects[name] if name in bpy.data.objects else
                         bpy.data.objects.new(name, self.__camera))
        self.__render_option = bpy.data.scenes['Scene'].render
        if name not in bpy.context.scene.objects:
            bpy.context.scene.objects.link(self.__object)
        self.look_at = (0, 0, 0)

    @property
    def render_option(self):
        return self.__render_option

    def take_photo(self, filename='image.png'):
        bpy.context.scene.camera = self.__object
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render(
            filepath=self.dirpath + filename)

    @property
    def look_at(self):
        return self.__look_at

    @look_at.setter
    def look_at(self, target):
        [x, y, z] = np.subtract(target, self.__object.location)
        x_vec = np.array([-z, 0, y])
        y_vec = np.array([LA.norm((x, y, 0)), +0, -x])
        self.__object.rotation_euler = np.arctan2(y_vec, x_vec)
        self.__look_at = target

    @property
    def location(self):
        return self.__object.location

    @location.setter
    def location(self, position):
        self.__object.location = position

    @property
    def near_clip(self):
        return self.__camera.clip_start

    @near_clip.setter
    def near_clip(self, value=1.0):
        self.__camera.clip_start = value

    @property
    def far_clip(self):
        return self.__camera.clip_end

    @far_clip.setter
    def far_clip(self, value=100.0):
        self.__camera.clip_end = value


if __name__ == "__main__":
    camera = Camera()
    camera.render_option.film_transparent = True
    camera.location = (5, 5, 5)
    camera.look_at = (0, 0, 0)
    camera.take_photo()
