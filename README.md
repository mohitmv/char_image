CharImage is a python utility to convert a image(picture) into image of ASCII characters. which can be displayed on terminal (stdout) or in a text file.
Additionally it can print a minial C++ code, which prints the desired image on stdout.

It requires PIL.Image and numpy packages.


-------------------------------------------------------------------------------------------------------
## Required dependency
- Python3
- Python PIL (pip install pillow)
- Python numpy (pip install numpy)
- Either clone the repo or copy-paste `image_to_char_image_tool.py` script.

-------------------------------------------------------------------------------------------------------
## How to use

usage: `<python script> image_file_path [options]`

This utility displays a image(picture) using terminal characters. Additionally it can print a minial C++ code to print the desired image on stdout.

```
options:
  --cpp_code:
      If this flag is not present then char-image will be printed on stdout.
      Otherwise a C++ program will be printed which can print the char-image
      on stdout.
      Default: Flag not applied. i.e. char-image will be printed.

  --on_char: 
      By default char-image will printed using '#' and ' '(whitespace)
      chars unless on_char or off_char are set to different characters.

  --off_char:
      Similar to on_char.

  --char_width:
      Width of desired char-image. Height will be adjusted
      accordingly. Original image is resized to fit into new
      resolution.
      Default: 80

  --char_height_width_ratio:
      char-image is displayed using terminal characters,
      which are not perfect square (unlike a pixel in
      actual image), So char-image will look vertically
      stretched unless height is compressed beforehand.
      Default: 1.9

  --separation_threshold_percent:
      char-image supports on-off characters (i.e. 0 and 1). Each pixel in
      original image is reduced down to 0/1.
      Algorithms is: Find minimum and maximum pixel value. pixel value =
      red_value + blue_value + green_value.
      Minimum-pixel is considered 0 (i.e. off) and maximum-pixel is considered
      1 (i.e. on). Which means pure white black color is off and pure white
      color is on. `separation_threshold_percent` is used for categorising each
      pixel in one of these two category.
      Default: 80 (i.e. 79.9% white and 20.1% black is considered black)
```
-------------------------------------------------------------------------------------------------------


## Demo

**Demo-1**

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/original_pic_1.png "Showcase-1")

`python3 image_to_char_image_tool.py image.png`

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_1_2.png "Showcase-1.1")

`python3 image_to_char_image_tool.py image.png --char_width="100" -on_char=" " --off_char="#"`

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_1.png "Showcase-1.2")

**Demo-2**

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/original_pic_2.png "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_2.png "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_2_2.png "Showcase-")

**Demo-3**

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/original_pic_3.png "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_3.png "Showcase-")

**Demo-4**

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/original_pic4.png "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/original_pic_4_2.jpg "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_4.png "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_4_2.png "Showcase-")


**Demo-5**

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/original_pic_5.jpg "Showcase-")

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/showcase_5.png "Showcase-")

**Demo-6 [Generated C++ Program]**

`python3 image_to_char_image_tool.py demo/original_pic_3.png --on_char="#" --cpp_code --off_char=" " --char_width=110`

![alt text](https://raw.githubusercontent.com/mohitmv/char_image/master/demo/generated_cpp_code_to_print_pic_3.png "Showcase-1.2")




-------------------------------------------------------------------------------------------------------
