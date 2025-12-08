DEFAULT_RETURN_VALUE = None

class Group():
    def __init__(self, *values):
        self.values = list(values)
        
    def __iter__(self):
        return iter(self.values)
    
    def add(self, *values):
        for value in values:
            self.values.append(value)

    def update(self):
        for value in self:
            value.update()
    
    def draw(self):
        for value in self:
            value.draw()

class GroupSprite():
    def __init__(self):
        self.sprite_dict = dict()

    def __getitem__(self, key):
        return self.sprite_dict.setdefault(key, DEFAULT_RETURN_VALUE)

    def __setitem__(self, key, sprite):
        self.sprite_dict[key] = sprite

    def __delitem__(self, key):
        del self.sprite_dict[key]

    def __len__(self):
        return len(self.sprite_dict)

