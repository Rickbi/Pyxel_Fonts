import pyxel
from os.path import join
from math import ceil
from Tools.Button import *
from Tools.Group import *

GLYPH_TEMPLATE = """STARTCHAR {hex_encoding}
ENCODING {encoding}
SWIDTH 500 0
DWIDTH {dwidth} 0
BBX {bbx}
BITMAP
{bitmap}
ENDCHAR"""

FONT_TEMPLATE = """STARTFONT 2.1
FONT PyxelFont
SIZE 8 75 75
FONTBOUNDINGBOX {bbx}
CHARS {glyphs_num}
{glyphs}
ENDFONT
"""

MAX_TILES_X = 32
MAX_TILES_Y = 32
SAVE_PATH = join("fonts", "pyxelFont.bdf")
BG_FONT_COLOR = pyxel.COLOR_BLACK
FONT_COLOR = pyxel.COLOR_WHITE

li_1 = [[1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

li_2 = [[0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]]

li_3 = [[1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

li_4 = [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]

class BoundingBox:
    def __init__(self, width = 0, height = 0, x = 0, y = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{self.width} {self.height} {self.x} {self.y}"

class Glyph:
    font_bounding_box = BoundingBox(4, 8, 0, 0)
    
    def __init__(self, encoding, width, height,
                 dwidth = -1, dx = 0, dy = 0, bitmap = None):
        self.encoding = encoding
        self.dwidth = width + 1 if dwidth == -1 else dwidth
        self.bbx = BoundingBox(width, height, dx, dy)
        self.bitmap = [[0 for j in range(MAX_TILES_Y)] for i in range(MAX_TILES_X)]
        
        if(bitmap is not None):
            self.set_bitmap(bitmap)

    @classmethod
    def getDefaultGlyph(cls):
        w = Glyph.font_bounding_box.width
        h = Glyph.font_bounding_box.height
        x = Glyph.font_bounding_box.x
        y = Glyph.font_bounding_box.y
        return cls(0, w, h, w + 1, x, y, None)

    def set_encoding(self, encoding):
        self.encoding = encoding
        
    def set_dwidth(self, dwidth):
        self.dwidth = dwidth
        
    def set_bbx(self, bbx):
        self.bbx = bbx
        
    def set_bitmap(self, bitmap):
        for i in range(len(bitmap[0])):
            for j in range(len(bitmap)):
                self.bitmap[i][j] = bitmap[j][i]

    @staticmethod
    def draw_font_bounding_box(x, y):
        pyxel.pset(x, y, pyxel.COLOR_DARK_BLUE)
        x += -1 + Glyph.font_bounding_box.x
        y += -1 + Glyph.font_bounding_box.y
        w = Glyph.font_bounding_box.width + 2
        h = Glyph.font_bounding_box.height + 2
        pyxel.rectb(x, y, w, h, pyxel.COLOR_DARK_BLUE)

    def draw_bbx(self, x, y):
        pyxel.pset(x, y, pyxel.COLOR_LIGHT_BLUE)
        x += -1 + Glyph.font_bounding_box.x + self.bbx.x
        y += -1 + Glyph.font_bounding_box.y + Glyph.font_bounding_box.height - self.bbx.height - self.bbx.y
        w = self.bbx.width + 2
        h = self.bbx.height + 2
        pyxel.rectb(x, y, w, h, pyxel.COLOR_LIGHT_BLUE)
        
    def draw_glyph(self, x, y, draw_bbx = False):
        if draw_bbx:
            Glyph.draw_font_bounding_box(x, y)
            self.draw_bbx(x, y)
        
        xx = x + Glyph.font_bounding_box.x + self.bbx.x
        yy = y + Glyph.font_bounding_box.y + Glyph.font_bounding_box.height - self.bbx.height - self.bbx.y
        
        for i in range(self.bbx.width):
            for j in range(self.bbx.height):
                if(self.bitmap[i][j] == 1):
                    pyxel.pset(xx + i, yy + j, FONT_COLOR)

    def bin_to_hex(self, bin_list):
        hex_width = ceil(self.bbx.width/4)
        width_fix = hex_width*4
        zeros = width_fix - self.bbx.width
        
        b_num_str = ''.join(map(str, bin_list))
        b_num_str_z = b_num_str + "0"*zeros
        
        h_num_str = hex(int(b_num_str_z, 2))[2:].zfill(hex_width).upper()
        return h_num_str
        
    def create_bitmap(self):
        bitmap = []
        for j in range(self.bbx.height):
            line = []
            for i in range(self.bbx.width):
                bit = self.bitmap[i][j]
                line.append(bit)

            hex_num = self.bin_to_hex(line)
            bitmap.append(hex_num)
        return "\n".join(bitmap)

    def __repr__(self):
        s = GLYPH_TEMPLATE.format(hex_encoding = hex(self.encoding),
                                  encoding = self.encoding,
                                  dwidth = self.dwidth,
                                  bbx = self.bbx,
                                  bitmap = self.create_bitmap()
                                  )
        return s

    def get_data(self):
        data = ["Glyph Data\n",
                f"Encoding = {self.encoding}",
                f"dwidth = {self.dwidth}",
                f"width = {self.bbx.width}",
                f"height = {self.bbx.height}",
                f"dx = {self.bbx.x}",
                f"dy = {self.bbx.y}"]
        return "\n".join(data)
        
    @staticmethod
    def get_font_bounding_box_data():
        data = ["Font Bounding Box\n",
                f"width = {Glyph.font_bounding_box.width}",
                f"height = {Glyph.font_bounding_box.height}",
                f"dx = {Glyph.font_bounding_box.x}",
                f"dy = {Glyph.font_bounding_box.y}"]
        return "\n".join(data)

class Font:
    def __init__(self, bbx, glyphs = None):
        self.glyphs = glyphs if glyphs is not None else [Glyph.getDefaultGlyph()]
        self.current_glyph = 0
        
        b01 = TextHoldButton(10, 20, "+", lambda: self.add_encoding(1))
        b02 = TextHoldButton(2, 20, "-", lambda: self.add_encoding(-1))
        b03 = TextHoldButton(10, 28, "+", lambda: self.add_dwidth(1))
        b04 = TextHoldButton(2, 28, "-", lambda: self.add_dwidth(-1))
        b05 = TextHoldButton(10, 36, "+", lambda: self.add_width(1))
        b06 = TextHoldButton(2, 36, "-", lambda: self.add_width(-1))
        b07 = TextHoldButton(10, 44, "+", lambda: self.add_height(1))
        b08 = TextHoldButton(2, 44, "-", lambda: self.add_height(-1))
        b09 = TextHoldButton(10, 52, "+", lambda: self.add_dx(1))
        b10 = TextHoldButton(2, 52, "-", lambda: self.add_dx(-1))
        b11 = TextHoldButton(10, 60, "+", lambda: self.add_dy(1))
        b12 = TextHoldButton(2, 60, "-", lambda: self.add_dy(-1))
        b13 = TextHoldButton(10, 78, "+", lambda: self.add_font_width(1))
        b14 = TextHoldButton(2, 78, "-", lambda: self.add_font_width(-1))
        b15 = TextHoldButton(10, 86, "+", lambda: self.add_font_height(1))
        b16 = TextHoldButton(2, 86, "-", lambda: self.add_font_height(-1))
        b17 = TextHoldButton(10, 94, "+", lambda: self.add_font_dx(1))
        b18 = TextHoldButton(2, 94, "-", lambda: self.add_font_dx(-1))
        b19 = TextHoldButton(10, 102, "+", lambda: self.add_font_dy(1))
        b20 = TextHoldButton(2, 102, "-", lambda: self.add_font_dy(-1))
        b21 = TextHoldButton(108, 30, ">", lambda: self.add_current_glyph(1))
        b22 = TextHoldButton(100, 30, "<", lambda: self.add_current_glyph(-1))
        b23 = TextHoldButton(100, 20, "Add Glyph", lambda: self.add_glyph())
        b24 = TextHoldButton(100, 10, "Save Font", lambda: self.save_font())
        
        self.buttons = Group(b01, b02, b03, b04, b05, b06,
                             b07, b08, b09, b10, b11, b12,
                             b13, b14, b15, b16, b17, b18,
                             b19, b20, b21, b22, b23, b24)

    def add_encoding(self, v):
        glyph = self.glyphs[self.current_glyph]
        glyph.encoding += v
        
    def add_dwidth(self, v):
        glyph = self.glyphs[self.current_glyph]
        if(glyph.dwidth + v >= 0):
            glyph.dwidth += v
            
    def add_width(self, v):
        glyph = self.glyphs[self.current_glyph]
        if(glyph.bbx.width + v >= 0):
            glyph.bbx.width += v
            
    def add_height(self, v):
        glyph = self.glyphs[self.current_glyph]
        if(glyph.bbx.height + v >= 0):
            glyph.bbx.height += v
            
    def add_dx(self, v):
        glyph = self.glyphs[self.current_glyph]
        glyph.bbx.x += v
            
    def add_dy(self, v):
        glyph = self.glyphs[self.current_glyph]
        glyph.bbx.y += v

    def add_font_width(self, v):
        if(Glyph.font_bounding_box.width + v >= 0):
            Glyph.font_bounding_box.width += v
            
    def add_font_height(self, v):
        if(Glyph.font_bounding_box.height + v >= 0):
            Glyph.font_bounding_box.height += v
            
    def add_font_dx(self, v):
        Glyph.font_bounding_box.x += v
            
    def add_font_dy(self, v):
        Glyph.font_bounding_box.y += v

    def add_current_glyph(self, v):
        self.current_glyph = (self.current_glyph + v) % (len(self.glyphs))

    def save_font(self):
        with open(SAVE_PATH, 'w') as f:
            f.writelines(str(self))

    def __repr__(self):
        s = []
        for glyph in self.glyphs:
            s.append(str(glyph))
        glyphs = '\n'.join(s)
        
        s = FONT_TEMPLATE.format(bbx = Glyph.font_bounding_box,
                                 glyphs_num = len(self.glyphs),
                                 glyphs = glyphs)
        return s        

    def add_glyph(self):
        self.glyphs.append(Glyph.getDefaultGlyph())

    def draw(self, draw_bbx=True):
        glyph = self.glyphs[self.current_glyph]
        glyph.draw_glyph(120, 50, draw_bbx)
        
        data = glyph.get_data() + "\n\n" + Glyph.get_font_bounding_box_data()
        pyxel.text(20, 10, data, pyxel.COLOR_WHITE)
        pyxel.text(120, 32, f"Current Glyph: {self.current_glyph + 1} / {len(self.glyphs)}", pyxel.COLOR_WHITE)
        
            

class Grid:
    def __init__(self, x, y, nx, ny, size):
        self.pos_x = x
        self.pos_y = y
        self.nx = nx
        self.ny = ny
        self.size = size
        self.hover = [-1, -1]
        self.hoverColor = pyxel.COLOR_CYAN
        
        # self.fountBoundingBox = [0, 0, 0, 0]
        # self.dwidth = self.size + 1
        # self.bbx_x = 0
        # self.bbx_y = 0
        
        self.grid = [[BG_FONT_COLOR for i in range(MAX_TILES_Y)] for j in range(MAX_TILES_X)]
    
    def __getitem__(self, indexes):
        return self.grid[indexes[0]][indexes[1]]
        
    def __setitem__(self, indexes, value):
        self.grid[indexes[0]][indexes[1]] = value
    
    def draw(self):
        for j in range(self.ny):
            for i in range(self.nx):
                x = self.pos_x + i*self.size
                y = self.pos_y + j*self.size
                c = self[i, j]
                
                pyxel.rect(x, y, self.size, self.size, c)
                pyxel.rectb(x, y, self.size, self.size, pyxel.COLOR_GRAY)
                
                if self.hover[0] == i and self.hover[1] == j:
                    pyxel.rectb(x, y, self.size, self.size, self.hoverColor)
   
    def get_hover_tile(self):
        return (self.hover[0], self.hover[1])
    
    def update_hover(self):
        x = pyxel.mouse_x - self.pos_x
        y = pyxel.mouse_y - self.pos_y
        i = x // self.size
        j = y // self.size
        
        if (0 <= i < self.nx) and (0 <= j < self.ny):
            self.hover[0] = i
            self.hover[1] = j
        else:
            self.hover[0] = -1
            self.hover[1] = -1

    def add_size(self, ds):
        new_size = self.size + ds
        if(new_size > 0):
            self.size = new_size

    def add_nx(self, dnx):
        new_nx = self.nx + dnx
        if(0 < new_nx <= MAX_TILES_X):
            self.nx = new_nx

    def add_ny(self, dny):
        new_ny = self.ny + dny
        if(0 < new_ny <= MAX_TILES_Y):
            self.ny = new_ny

    def clear(self):
        for i in range(MAX_TILES_X):
            for j in range(MAX_TILES_Y):
                self[i, j] = 0

    def create_bitmap_OLD(self):
        bitmap = []
        for j in range(self.ny):
            row = 0
            for i in range(self.nx):
                row <<= 1
                if(self[i, j] == FONT_COLOR):
                    row += 1
            # row <<= 4 - (self.nx % 4)
            hex_num = hex(row)[2:].zfill(ceil(self.nx/4)).upper()
            bitmap.append(hex_num)
        return "\n".join(bitmap)
        
    def bin_to_hex(self, bin_list):
        hex_width = ceil(self.nx/4)
        width_fix = hex_width*4
        zeros = width_fix - self.nx
        
        b_num_str = ''.join(map(str, bin_list))
        b_num_str_z = b_num_str + "0"*zeros
        
        h_num_str = hex(int(b_num_str_z, 2))[2:].zfill(hex_width).upper()
        return h_num_str
        
    def create_bitmap(self):
        bitmap = []
        for j in range(self.ny):
            line = []
            for i in range(self.nx):
                bit = 1 if self[i, j] == FONT_COLOR else 0
                line.append(bit)

            hex_num = self.bin_to_hex(line)
            bitmap.append(hex_num)
        return "\n".join(bitmap)
    
    def save_preview(self):
        dic = {"bitmap": self.create_bitmap(),
               "width": self.nx,
               "height": self.ny,
               "dwidth": self.nx + 1,
               "ascent": self.nx - 1}
        lines = PREVIEW_TEMPLATE.format(**dic)
        
        with open(PREVIEW_FONT, 'w') as f:
            f.writelines(lines)

    def draw_preview(self, x, y):
        pyxel.rect(x, y, self.nx, self.ny, BG_FONT_COLOR)
        for j in range(self.ny):
            for i in range(self.nx):
                px = x + i
                py = y + j
                if (self[i, j] == FONT_COLOR):
                    pyxel.pset(px, py, FONT_COLOR)
        

class App:
    def __init__(self):
        pyxel.init(240, 160, "Font Maker", display_scale = 5)
        pyxel.mouse(True)
        
        bbx = BoundingBox(5, 10, 0, 0)
        self.font = Font(bbx)
        
        # glyphs = [Glyph(ord('a'), 5, 5, bitmap=li_1),
                  # Glyph(ord('b'), 5, 5, bitmap=li_2),
                  # Glyph(ord('c'), 5, 4, bitmap=li_3),
                  # Glyph(ord('1'), 4, 5, bitmap=li_4),
                  # Glyph(ord(' '), 4, 4)]
        
        # self.font = Font(bbx, glyphs)
   
    def change_cursor(self):
        pass
    
    def run(self):
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.font.buttons.update()
        
        if(pyxel.btnr(pyxel.KEY_SPACE)):
            self.font.save_font()
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        
        self.font.draw()
        self.font.buttons.draw()
        
        


class App_test:
    def __init__(self):
        pyxel.init(240, 160, "Font Maker", display_scale = 3)
        pyxel.mouse(True)
        
        self.grid = Grid(20, 10, 8, 8, 10)
        self.change_cursor()
        
        self.buttons = Group()
        self.buttons.add( TextButton(150, 10, "Increase Size", lambda: self.grid.add_size(1)) )
        self.buttons.add( TextButton(150, 20, "Decrease Size", lambda: self.grid.add_size(-1)) )
        self.buttons.add( TextButton(150, 30, "Add Col", lambda: self.grid.add_nx(1)) )
        self.buttons.add( TextButton(150, 40, "Remove Col", lambda: self.grid.add_nx(-1)) )
        self.buttons.add( TextButton(150, 50, "Add Row", lambda: self.grid.add_ny(1)) )
        self.buttons.add( TextButton(150, 60, "Remove Row", lambda: self.grid.add_ny(-1)) )
        def clear_grid():
            self.grid.clear()
            self.grid.save_preview()
            self.myFont = pyxel.Font(PREVIEW_FONT)
        self.buttons.add( TextButton(150, 70, "Clear", clear_grid) )
        
        # self.grid.save_preview()
        self.myFont = pyxel.Font(PREVIEW_FONT)
    
    def change_cursor(self):
        pyxel.cursor.rect(0, 0, 8, 8, 0)
        pyxel.cursor.tri(0, 0, 2, 2, 2, 4, pyxel.COLOR_CYAN)
        pyxel.cursor.tri(0, 0, 2, 2, 4, 2, pyxel.COLOR_LIGHT_BLUE)
    
    def run(self):
        pyxel.run(self.update, self.draw)
    
    def handle_events(self):
        if (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)):
            i, j = self.grid.get_hover_tile()
            if(i >= 0 and j >= 0):
                self.grid[i, j] = FONT_COLOR
                
                self.grid.save_preview()
                self.myFont = pyxel.Font(PREVIEW_FONT)
        
        elif (pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
            i, j = self.grid.get_hover_tile()
            if(i >= 0 and j >= 0):
                self.grid[i, j] = BG_FONT_COLOR
                
                self.grid.save_preview()
                self.myFont = pyxel.Font(PREVIEW_FONT)
                
        elif (pyxel.btnr(pyxel.KEY_SPACE)):
            self.grid.save_preview()
            self.myFont = pyxel.Font(PREVIEW_FONT)
    
    def update(self):
        self.grid.update_hover()
        self.buttons.update()
        self.handle_events()
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        self.grid.draw()
        self.buttons.draw()
        
        pyxel.text(10, 140, f"Pixel Size = {self.grid.size}", pyxel.COLOR_WHITE)
        pyxel.text(10, 130, f"Dimentions = {self.grid.nx}, {self.grid.ny}", pyxel.COLOR_WHITE)
        pyxel.text(10, 110, "Preview: ", pyxel.COLOR_WHITE)
        
        prev_pos = 10 + pyxel.FONT_WIDTH * len("Preview: ")
        # pyxel.rect(prev_pos - 1, 110 - 1, 3*self.grid.nx + 4, self.grid.ny + 2, BG_FONT_COLOR)
        # pyxel.text(prev_pos, 110, "AAA\nAAA", FONT_COLOR, self.myFont)
        self.grid.draw_preview(prev_pos, 110)
        

if __name__ == "__main__":
    App().run()
