# Pyxel_Fonts

The idea of this project is to have a tool to easily create a font file in a ".bdf" format.
This format was choseen since the pyxel library only can read this type of files.

The following are the only attributes that pyxel will read, any other will be ignore.

- FONTBOUNDINGBOX
- ENCODING
- DWIDTH
- BBX
- BITMAP
- ENDCHAR

## Thinks that the tool should be able to do

### Font Creation
- Show grid lines.
- The following values should be able to be set:
	- Global font bounding box: x, y, width (Not used), height
	- Encoding number i.e. 65 for 'A'
	- Space left after the letter (dwidth) i.e. normally the letter width + 1
	- Individual bounding box: x, y, width, height
	- bitmap: taken from the grid.
- The minimum and maximun shall be 0x0 and 32x32 pixels.

### Font Preview
Show a small preview of the current bitmap in the grid. This can be done in two ways:

- Save the only letter in a bdf file, read it and show it.
- Create a replica of the drawing code to draw the text.

Show a editable text as an example. For this a text box would need to be created.

### Font Edit
If open a file the fonts needs to be added and able to be change.

### Read Font File
Read the file to collect all the encoding numbers in the file and show an example of all the letters.
