from Graphic_Image import *


class Animation():
    def __init__(self):
        self.pics = []
        self.pic_number = 0
        self.frames_per_pic = 7
        self.frame_count = 0

    def Add_Pic(self, sprite_name, sheet_name = None, rectangle = None, key = (255, 255, 255)):
        if sheet_name is None:
            self.pics.append(get_image(sprite_name, key))
        else:
            self.pics.append(get_sprite(sprite_name, sheet_name, rectangle, key))

    def Load(self, sheet_name, animation_name, num_pics, start_x, start_y, w, h, space = 0):
        for i in range(num_pics):
            sprite_name = animation_name + "_" + i.__str__()
            self.Add_Pic(sprite_name, sheet_name, (start_x + i * (w+space), start_y, w, h))



    def Update(self):
        self.frame_count += 1
        if self.frame_count == self.frames_per_pic:
            self.frame_count = 0
            if self.pic_number < self.pics.__len__() -1:
                self.pic_number += 1
            else:
                self.pic_number = 0
        return self.pics[self.pic_number]

    def Reset(self):
        self.frame_count = 0
        self.pic_number = 0

