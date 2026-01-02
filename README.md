# Pyxel_Fonts

Pyxel Fonts is a font editor for the [Pyxel](https://github.com/kitao/pyxel) library.

In Pyxel, you can load a font with a .bdf file (Bitmap Distribution Format), this editor can create, edit and visualize these kind of files. You can see the [Observations.md](Observations.md) document to learn more about the .bdf files and how Pyxel read these files.

## Requirements
pyxel==2.5.10

---
---

## ToDo

### Font Creation
- [ ] Show the glyph in a grid.
- The following values should be able to be set:
	- [ ] Font bounding box
	- [ ] Encoding number
	- [ ] Glyph dwidth
	- [ ] Glyph bounding box
	- [ ] Bitmap
- [ ] The minimum and maximun shall be 0x0 and 32x32 pixels.

### Font Preview
- [ ] Show a small preview of the current bitmap in the grid. This can be done in two ways:
- [ ] Show a editable text as an example. For this a text box would need to be created.

### Font Edit
- [ ] If open a file the fonts needs to be added and able to be change.


### Other
The following is a expectation of how the editor could look.



    ┌────────────────────────────────────────────────────┐
    │                                                    │
    │                                                    │
    │          ┌─┬─┬─┬─┬─┬─┬─┬─┐                         │
    │          │ │ │ │ │ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │ │ │ │ │ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│█│█│█│ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│ │ │ │█│ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│ │ │ │█│ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│█│█│█│ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│ │ │ │█│ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│ │ │ │█│ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │█│ │ │ │█│ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │ │ │ │ │ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │ │ │ │ │ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │ │ │ │ │ │ │ │ │                         │
    │          ├─┼─┼─┼─┼─┼─┼─┼─┤                         │
    │          │ │ │ │ │ │ │ │ │                         │
    │          └─┴─┴─┴─┴─┴─┴─┴─┘                         │
    │                                                    │
    │                                                    │
    │                                                    │
    └────────────────────────────────────────────────────┘
