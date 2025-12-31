## Bitmap Distribution Format
This section is to explaing how the .bdf (Bitmap Distribution Format) files works.
The .bdf file store the font as a collection of bitmaps witch represent each letter (glyph in the code) in the font.
These bitmaps are stored as hexadecimal numbers.
As example consider a bitmaps for the letters 'R' and 'P':

In the first column is the hexadecimal numbers for each line in the bitmap.
In the second column is the same number but in binary.
In the third column we remove the 0's to visualice the character.
In the Forth column we replace the 1's with a solid block (█).

    ┌──┬────────┬────────┬────────┐
    │00│00000000│        │        │
    │00│00000000│        │        │
    │F0│11110000│1111    │████    │
    │88│10001000│1   1   │█   █   │
    │88│10001000│1   1   │█   █   │
    │F0│11110000│1111    │████    │
    │88│10001000│1   1   │█   █   │
    │88│10001000│1   1   │█   █   │
    │88│10001000│1   1   │█   █   │
    │00│00000000│        │        │
    │00│00000000│        │        │
    │00│00000000│        │        │
    │00│00000000│        │        │
    ├──┼────────┼────────┼────────┤
    │00│00000000│        │        │
    │00│00000000│        │        │
    │00│00000000│        │        │
    │00│00000000│        │        │
    │F0│11110000│1111    │████    │
    │88│10001000│1   1   │█   █   │
    │88│10001000│1   1   │█   █   │
    │88│10001000│1   1   │█   █   │
    │F0│11110000│1111    │████    │
    │80│10000000│1       │█       │
    │80│10000000│1       │█       │
    │00│00000000│        │        │
    │00│00000000│        │        │
    └──┴────────┴────────┴────────┘



For each bitmap there are some other important data that is store in the file.

## ENCODING
The encoding is the unicode code of the character.
For example:
For the letter 'R' the encoding value is 82.
For the letter 'P' the encoding value is 112.

## DWIDTH
This value indicates at what distance the next character is draw after the current character.
For example, in the following diagram the character 'R' has a dwith of 6, since the next character is draw after 6 spaces, and the character 'P' has a dwidth of 7, since the next character is draw after 7 spaces.

       6     7
     ╭─^──╮╭─^───╮
    ┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐
    │                   │
    │                   │
    │████         ████  │
    │█   █        █   █ │
    │█   █ ████   █   █ │
    │████  █   █  ████  │
    │█   █ █   █  █   █ │
    │█   █ █   █  █   █ │
    │█   █ ████   █   █ │
    │      █            │
    │      █            │
    │                   │
    │                   │
    └───────────────────┘

### Bounding Box
The bounding box is a box that surrounds the character, it contains the following data:
Width, height, x-offset and y-offset.
The origin of the bounding box is at the botton left of the box, if our character base is not aligned with this origin we can use the offset to move the character at the point that aligns with the base of the box.
For example, consider the 'R' and 'P' characters, lets give them a bounding box with:
width = 6
height = 11
x-offset = 0
y-offset = -2

                         width        ┌──────┐    ╮     
                         ╭─^──╮       │      │    ├ y-offset
    ┌--------┐          ┌──────┬-┐    ├------┼-┐  ╯
    ¦        ¦        ╭ │      │ ¦    │      │ ¦
    ¦        ¦        │ │      │ ¦    │      │ ¦
    ¦████    ¦        │ │████  │ ¦    │████  │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦████    ¦ height ┤ │████  │ ¦    │████  │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦        ¦        │ │      │ ¦    ├──────┘ ¦
    ¦        ¦        ╰ │      │ ¦    ¦        ¦
    ¦        ¦          ├──────┘ ¦    ¦        ¦
    ¦        ¦          ¦        ¦    ¦        ¦
    └--------┘          └--------┘    └--------┘

                         width        ┌──────┐    ╮     
                         ╭─^──╮       │      │    ├ y-offset
    ┌--------┐          ┌──────┬-┐    ├------┼-┐  ╯
    ¦        ¦        ╭ │      │ ¦    │      │ ¦
    ¦        ¦        │ │      │ ¦    │      │ ¦
    ¦        ¦        │ │      │ ¦    │      │ ¦
    ¦        ¦        │ │      │ ¦    │      │ ¦
    ¦████    ¦        │ │████  │ ¦    │████  │ ¦
    ¦█   █   ¦ height ┤ │█   █ │ ¦    │█   █ │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦█   █   ¦        │ │█   █ │ ¦    │█   █ │ ¦
    ¦████    ¦        │ │████  │ ¦    │████  │ ¦
    ¦█       ¦        │ │█     │ ¦    ├█─────┘ ¦
    ¦█       ¦        ╰ │█     │ ¦    ¦█       ¦
    ¦        ¦          ├──────┘ ¦    ¦        ¦
    ¦        ¦          ¦        ¦    ¦        ¦
    └--------┘          └--------┘    └--------┘


The file stores two types of bounding boxes
## BBX
A specific bounding box for each character in the file.

## FONTBOUNDINGBOX
A general bounding box for the font, it is the same for all the characters.


## Other
The following data is stored in the .bdf file, but it is not readed by pyxel.

### STARTFONT
This is the first line in the file, the number indicates the bdf version.
Example: STARTFONT 2.1

### FONT
This indicates the name of the font.
Example: FONT MyPixelFont

### CHARS
This indicates the total number of bitmaps in the file.
Example: CHARS 97

### STARTCHAR
This is the first line of each bitmap in the file, the number indicates the unicode code of the character in hexadecimal.
Example: STARTCHAR 0x112


The following is an example of a .bdf file.

```
STARTFONT 2.1
FONT MyPixelFont
SIZE 8 75 75
FONTBOUNDINGBOX 8 8 0 0
STARTPROPERTIES 3
FONT_ASCENT 7
FONT_DESCENT 1
DEFAULT_CHAR 0
ENDPROPERTIES
CHARS 3
STARTCHAR 0x00
ENCODING 0
SWIDTH 500 0
DWIDTH 9 0
BBX 8 8 0 0
BITMAP
18
24
42
81
81
42
24
18
ENDCHAR
STARTCHAR 0x01
ENCODING 1
SWIDTH 500 0
DWIDTH 9 0
BBX 8 8 0 0
BITMAP
FF
81
81
81
81
81
81
FF
ENDCHAR
STARTCHAR 0x02
ENCODING 2
SWIDTH 500 0
DWIDTH 9 0
BBX 8 8 0 0
BITMAP
00
7E
42
66
0C
18
00
10
ENDCHAR
ENDFONT
```

----

The following description uses pyxel 2.5.10

To create a font editor, we first need to undestand how the pyxel lib read the files and print the font in the screen.

All this proccess can be seem in the following file:
rust/pyxel-engine/src/font.rs [https://github.com/kitao/pyxel/blob/main/rust/pyxel-engine/src/font.rs]

We need to focus on two importatn parts, what part is readed from the file and how the font is draw:

## Reading the File
On lines 49 to 107 you can see how data is extracted from the .bdf file

The following data is extracted from the file:
• Font bounding box, this is readed as "FONTBOUNDINGBOX width, height, x-offset, y-offset" ( FONTBOUNDINGBOX 10 11 0 -2 )
• Encoding, this is readed as "ENCODING encoding" ( ENCODING 122 )
• Dwidth, this is readed as "DWIDTH dwidth 0" ( DWIDTH 7 0 ), only the first number is taken.
• Bounding box, this is readed as "BBX width, height, x-offset, y-offset" ( BBX 6 13 0 -4 )
• Bitmap, read all the lines between BITMAP and ENDCHAR, each bitmap line is store as the reversed binary.

### Bitmap
Steps to reverse the binary from the file:
• The hex value is transform to a 32-bit integer.
• Bits are reversed
• Right shift by (32 - line_lenght * 4)

For example:
Consider the following bitmap.

    ┌───────┐
    │BITMAP │
    │00     │
    │00     │
    │F0     │
    │88     │
    │88     │
    │F0     │
    │88     │
    │88     │
    │88     │
    │00     │
    │00     │
    │00     │
    │00     │
    │ENDCHAR│
    └───────┘

Lets take the line "F0"
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


