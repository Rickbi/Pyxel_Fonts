import pyxel

class TextBox:
    def __init__(self, pos_x, pos_y, width, height, bg_color, text_color, border_color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = width
        self.h = height
        self.border_width = 2
        self.bg_color = bg_color
        self.border_color = border_color
        self.text_color = text_color
        self.text = "This is a test This is another test! This is a test"
        self.font_width = pyxel.FONT_WIDTH
        self.font_height = pyxel.FONT_HEIGHT
    
    def get_lines(self, textBlock):
        lines = [[]]
        line_len = 0
        words = textBlock.split(' ')
        width = self.w - 2*self.border_width - 2
        for word in words:
            word_len = len(word) * self.font_width
            total_len = line_len + word_len + len(lines[-1]) * self.font_width
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
        pyxel.text(text_pos_x, text_pos_y, text, self.text_color)
    
    def load_file(self, fileName):
        with open(fileName, 'r') as f:
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
        pyxel.init(240, 160, "TextBox Test", display_scale = 3)
        pyxel.mouse(True)
        self.textBox = TextBox(10, 10, 100, 100, pyxel.COLOR_BLACK, pyxel.COLOR_WHITE, pyxel.COLOR_GRAY)
    
    def run(self):
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.textBox.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_NAVY)
        
        self.textBox.draw()


if __name__ == "__main__":
    App().run()

