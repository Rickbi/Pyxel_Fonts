## Bitmap Distribution Format
This section is to explaing how the .bdf(Bitmap Distribution Format) files works.
The .bdf file store the font as a collection of bitmaps witch represent each letter (glyph in the code) in the font.
As example consider a bitmap for the letter 'R':

00
00
F0
88
88
F0
88
88
88
00
00
00
00

As you may notice each line is a hexadecimal number, lets see this looks as a binary numbers:

00000000
00000000
11110000
10001000
10001000
11110000
10001000
10001000
10001000
00000000
00000000
00000000
00000000

If you remove all the '0' in the bitmap you can see how the letter 'R' appears.

1111
1   1
1   1
1111
1   1
1   1
1   1

To see it better we can replace the 1's with a solid block (█)

████
█   █
█   █
████
█   █
█   █
█   █

For each bitmap there are some other important data that is store in the file.

## ENCODING
The encoding is the unicode code point of the character.
For example, for the letter 'R' the encoding value is 82.

## DWIDTH
This value indicates how many spaces after the next letter should be draw.
For example, lets say we want to keep one space between letters, therefore for the previous 'R' bitmap we would need a spacing of 6, since our bit map takes a maximun of 5 bits, this would give us that the dwidth is 6.

## BBX
Bounding Box gave us the width and height of the box that surrounds the character, also it gave us the horizontal and vertical offset positions.
For example, lets take the previous 'R' case.
The width and height are 6 and 13
The horizontal and vertical offset are 0 and -4
Note: The y-offset is -4 since the reference point is taken as the base of the letter.


Beside the previous data there is also the font bounding box, whitch is general for the font:
## FONTBOUNDINGBOX
Font bounding box is similar to the BBX, but it is general for the font.
For example:
The width and height can be 10 and 11
The horizontal and vertical offset can be 0 and -2


There can be more data store in the file, but for the pyxel library these are the only data that is taken, all other parameters are ignored.


---

Important, this is done on the pyxel version: 2.5.10

To create a font editor, we first need to undestand how the pyxel lib read the files and print the font in the screen.

All this proccess can be seem in the following file:
rust/pyxel-engine/src/font.rs [https://github.com/kitao/pyxel/blob/main/rust/pyxel-engine/src/font.rs]

We need to focus on two importatn parts, what part is readed from the file and how the font is draw:

## Reading the File
On lines 49 to 107 you can see how data is extracted from the .bdf file

• The font bounding box (width, height, x, y) is extracted from the line that start with "FONTBOUNDINGBOX". Only one per file.
Example:
FONTBOUNDINGBOX 10 11 0 -2

• The encoding number is extracted from the line that start with "ENCODING". One per glyph. This is the char value, like "a" is 97.
Example:
ENCODING 12288

• The dwidth number is extracted from the line that start with "DWIDTH". One per glyph. Only the first number is taken.
Example:
DWIDTH 10 0

• The bounding box (width, height, x, y) is extracted from the line that start with "BBX". One per glyph.
Example:
BBX 10 11 0 -2

• The bitmap data is taken from the lines that are between "BITMAP" and "ENDCHAR". One per glyph.
Example:
BITMAP
00
00
F0
88
88
F0
88
88
88
00
00
00
00
ENDCHAR

All data is store as the readed number, except for the bitmap, these pass for a proccess to reverse the binary values.
The steps to reverse the binary values per line is:
• The hex value is transform to a 32-bit integer.
• Bits are reversed
• Right shift by (32 - line_lenght * 4)
Example:
Lets consider the line "F0"
This value as binary is: 11110000
Since the value is store as a 32-bit, we can see it as: 00000000000000000000000011110000
Reversing the bits led to: 00001111000000000000000000000000
The value we should shift this number is 32 - line_lenght * 4 = 32 - 2 * 4 = 24
The shift would be: 00001111000000000000000000000000 >> 24 = 00001111

As you can see the binary value pass from 11110000 to 00001111
Some important points to note:
• 32 is the maximun width.
• The character size needs to be a multiple of 4.




## Drawing the font
Line 121 to 161

One font bounding box's height is added to the glyph vertical position each time a new line '\n' is found, horizontal position is set to the horizontal starting position.
The glyph's dwidth is added to the horizontal position when a glyph is finished to draw.


When a single glyph is draw the following happens:
• Font bounding box and glyph bounding box horizontal positions are added to the horizontal position.
• Font bounding box vertical position and font bounding box height are added to the vertical position and glyph bounding box vertical position and glyph bounding box height are substrated to the vertical position.
• The bitmap is draw from the stored binaries from right to left.
Example:
Consider the bitmap line: 00001111
This will be draw in the screen as: 11110000


