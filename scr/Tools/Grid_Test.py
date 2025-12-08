import pyxel

TILE_WIDTH = 32
TILE_HEIGHT = 16

class IsometricGrid:
    def __init__(self, pos_x, pos_y, grid_size_x, grid_size_y,
                 grid_color = pyxel.COLOR_GRAY,
                 select_color = pyxel.COLOR_LIME,
                 hover_color = pyxel.COLOR_ORANGE):
        self.tile_select = [-1, -1]
        self.tile_hover = [-1, -1]
        self.gridPos = [pos_x, pos_y]
        self.tileSize = [TILE_WIDTH, TILE_HEIGHT]
        self.gridSize = [grid_size_x, grid_size_y]
        self.color = grid_color
        self.selectColor = select_color
        self.hoverColor = hover_color

    def draw(self):
        self.draw_grid()
        self.draw_select_tile(*self.tile_hover, self.hoverColor)
        self.draw_select_tile(*self.tile_select, self.selectColor)

    def update(self):
        self.get_hover_tile()
        if(pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT)):
            if (self.is_valid(*self.tile_hover)):
                self.tile_select[:] = self.tile_hover

    def is_valid(self, i, j):
        if(0 <= i < self.gridSize[0] and 0 <= j < self.gridSize[1]):
            return True
        return False

    def get_hover_tile(self):
        dx = (self.tileSize[0]//2)
        dy = (self.tileSize[1]//2)
        
        rx = pyxel.mouse_x - self.gridPos[0]
        ry = pyxel.mouse_y - self.gridPos[1]

        ddx = rx*dy/dx
        
        x = ry + ddx
        y = ry - ddx        
        
        self.tile_hover[0] = x//dx
        self.tile_hover[1] = y//dx
    
    def draw_select_tile(self, i, j, color):
        dx = (self.tileSize[0]//2)
        dy = (self.tileSize[1]//2)
        
        x = self.gridPos[0] + dx*i - dx*j
        y = self.gridPos[1] + dy*j + dy*i
        
        self.draw_border_tile(x, y, color)

    def draw_border_tile(self, x, y, color):
        dx = (self.tileSize[0]//2)
        dy = (self.tileSize[1]//2)
        
        p1 = (x         , y       )
        p2 = (x + dx - 1, y + dy  )
        p3 = (x         , y + 2*dy)
        p4 = (x - dx    , y + dy  )
        
        pyxel.line(p1[0], p1[1], p2[0], p2[1], color)
        pyxel.line(p2[0], p2[1], p3[0], p3[1], color)
        pyxel.line(p3[0], p3[1], p4[0], p4[1], color)
        pyxel.line(p4[0], p4[1], p1[0], p1[1], color)
    
    def draw_grid(self):
        dx = (self.tileSize[0]//2)
        dy = (self.tileSize[1]//2)
        
        for i in range(self.gridSize[0] + 1):
            x1 = self.gridPos[0] + i*dx
            y1 = self.gridPos[1] + i*dy
            x2 = self.gridPos[0] + (i - self.gridSize[1])*dx
            y2 = self.gridPos[1] + (i + self.gridSize[1])*dy
            pyxel.line(x1, y1, x2, y2, self.color)
            
        for j in range(self.gridSize[1] + 1):
            x1 = self.gridPos[0] - j*dx
            y1 = self.gridPos[1] + j*dy
            x2 = self.gridPos[0] - (j - self.gridSize[0])*dx
            y2 = self.gridPos[1] + (j + self.gridSize[0])*dy
            pyxel.line(x1, y1, x2, y2, self.color)

