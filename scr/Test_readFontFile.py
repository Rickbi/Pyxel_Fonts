import pyxel
from os.path import join

# FONT_TEST = join("fonts", "umplus_j10r.bdf")
FONT_TEST = join("fonts", "pyxelFont.bdf")

class TextBox:
    def __init__(self, pos_x, pos_y, width, height, bg_color, text_color, border_color, font_file):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = width
        self.h = height
        self.border_width = 2
        self.bg_color = bg_color
        self.border_color = border_color
        self.text_color = text_color
        self.font = pyxel.Font(font_file)
        self.text = "This is a test This is another test! This is a test"
        self.font_width = pyxel.FONT_WIDTH
    
    def get_lines(self, textBlock):
        lines = [[]]
        line_len = 0
        words = textBlock.split(' ')
        width = self.w - 2*self.border_width - 2
        for word in words:
            word_len = self.font.text_width(word) #len(word) * self.font_width
            total_len = line_len + word_len + len(lines[-1]) * self.font.text_width(' ')
            if (total_len <= width):
                lines[-1].append(word)
                line_len += word_len
            else:
                lines.append([word])
                line_len = word_len
                
        lines = [' '.join(line) for line in lines]
        return lines

    def draw_text(self):
        lines = []
        for block in self.text.split('\n'):
            lines += self.get_lines(block)
        
        text = '\n'.join(lines)
        text_pos_x = self.pos_x + self.border_width + 1
        text_pos_y = self.pos_y + self.border_width + 1
        pyxel.text(text_pos_x, text_pos_y, text, self.text_color, self.font)
    
    def load_file(self, fileName):
        with open(fileName, 'r', encoding='utf-8') as f:
            self.text = ''.join(f.readlines())
    
    def update(self):
        if (pyxel.KEY_RETURN in pyxel.input_keys
            or pyxel.KEY_KP_ENTER in pyxel.input_keys):
            self.text += "\n"
        elif (pyxel.KEY_BACKSPACE in pyxel.input_keys):
            self.text = self.text[:-1]

        text = pyxel.input_text
        if text:
            self.text += text

        if (pyxel.dropped_files):
            self.load_file(pyxel.dropped_files[0])
        
    def draw(self):
        # Border
        pyxel.rect(self.pos_x, self.pos_y, self.w, self.h, self.border_color)
        x = self.pos_x + self.border_width
        y = self.pos_y + self.border_width
        w = self.w - 2 * self.border_width
        h = self.h - 2 * self.border_width
        
        # Back ground
        pyxel.rect(x, y, w, h, self.bg_color)
                
        # Text
        self.draw_text()

class App:
    def __init__(self):
        pyxel.init(240, 160*2, "TextBox Test", display_scale = 3)
        pyxel.mouse(True)
        self.textBox = TextBox(10, 10, 220, 140, pyxel.COLOR_BLACK, pyxel.COLOR_WHITE, pyxel.COLOR_GRAY, FONT_TEST)
        self.encode_values = self.read_font_file(FONT_TEST)
        self.encode_selected = 0
        self.font = pyxel.Font(FONT_TEST)
        self.text_y = 170
    
    def read_font_file(self, fileName):
        encode_values = []
        lines = []
        with open(fileName, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            if line.startswith("ENCODING"):
                num = int(line.split(' ')[1])
                if (0 <= num < 0x110000):
                    encode_values.append(num)
        return encode_values
    
    def run(self):
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.textBox.update()
        
        self.encode_selected = (self.encode_selected + 1)%len(self.encode_values)
        
        self.text_y += pyxel.mouse_wheel*20

    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)

        s = ""
        for i, num in enumerate(self.encode_values):
            s += chr(num)
            if (i+1)%22 == 0:
                s += '\n'
        
        pyxel.text(10, self.text_y, s, 7, self.font)
        pyxel.rect(0, 0, 240, 160, pyxel.COLOR_NAVY)
        pyxel.rect(0, 310, 240, 10, pyxel.COLOR_NAVY)
        self.textBox.draw()


if __name__ == "__main__":
    App().run()

