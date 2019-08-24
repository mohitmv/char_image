# Copyright: Mohit Saini (mohitsaini1196@gmail.com)
#
# A utility to display an image(picture) using terminal characters.
# Additionally it can print a minial C++ code to print the desired image at
# terminal.

from PIL import Image
import getopt, sys, numpy

def GetCppCode(pattern_string, on_char, off_char):
  cpp = {}
  cpp["string"] = on_char + off_char;
  buffer_sign = False;
  buffer_len = 0;
  def push(buffer_sign, buffer_len):
    if buffer_len == 0:
      return;
    assert(buffer_len < 128);
    cpp["string"] += hex((256 + (1 if buffer_sign else -1)*buffer_len)%256)[2:].zfill(2);
  for ii, i in enumerate(pattern_string):
    if i == '\n':
      push(buffer_sign, buffer_len);
      cpp["string"] += "-";
      buffer_len = 0;
    elif buffer_len == 0:
      buffer_sign = (i == on_char);
      buffer_len += 1;
    elif (i == on_char) == buffer_sign:
      buffer_len += 1;
    else:
      push(buffer_sign, buffer_len);
      buffer_sign = 1-buffer_sign;
      buffer_len = 1;
  if buffer_len > 0:
    push(buffer_sign, buffer_len);
  cpp["code"] = """
#include <iostream>
#include <sstream>

int main() {
  std::cout << ([]() {
    std::ostringstream oss;
    std::string pattern = \"""" + cpp["string"] + """\";
    auto lHex = [](char a) { return int(('0' <= a && a <= '9') ? a-'0' : 10+(a-'a')); };
    for (int i = 2; i < pattern.size(); i++) {
      if(pattern[i] == '-') {
        oss << "\\n";
      } else {
        int tmp = lHex(pattern[i])*16 + lHex(pattern[i+1]);
        char print_char = tmp < 128 ? pattern[0]: pattern[1];
        int len = tmp < 128 ? tmp: (256-tmp);
        while(len-- > 0) {
          oss << print_char;
        }
        i++;
      }
    }
    return oss.str();
  }()) << std::endl;
  return 0;
}
  """
  return cpp["code"];

def Image2CharImage(image_file_path,
                    char_width = 80,
                    char_height_width_ratio = 1.9,
                    on_char = "#",
                    off_char = " ",
                    separation_threshold_percent = 80,
                    cpp_code = False):
  pic = Image.open(image_file_path);
  width, height = pic.size;
  new_width, new_height = char_width, int((char_width*pic.size[1])/(char_height_width_ratio*pic.size[0]));
  pic = pic.resize((new_width, new_height), Image.ANTIALIAS)
  pic_data = pic.load();
  assert new_width > 0, new_height > 0;
  min_color = 255*3;
  max_color = 0;
  pic_data_color_sum = numpy.zeros((new_height, new_width), dtype=int);
  for i in range(new_height):
    for j in range(new_width):
      rgb = pic_data[j, i];
      if type(rgb) == int:
        rgb = (rgb, rgb, rgb)
      if type(rgb) == tuple and len(rgb) >= 3:
        color_sum = int(rgb[0]) + int(rgb[1]) + int(rgb[2]);
        pic_data_color_sum[i][j] = color_sum;
        min_color = min(min_color, color_sum);
        max_color = max(max_color, color_sum);
      else:
        sys.exit("This type of images are not supported yet.");
  boundary = min_color + ((max_color - min_color)*separation_threshold_percent)/100
  output = [""]*new_height;
  for i in range(new_height):
    for j in range(new_width):
      color_sum = pic_data_color_sum[i,j];
      output[i] += off_char if (color_sum > boundary) else on_char;
    output[i] += "\n";
  output = "".join(output);
  if cpp_code:
    return GetCppCode(output, on_char, off_char);
  else:
    return output;

# print(Image2CharImage("misc/images/sage_logo_icon_3.png", char_width = 80, on_char=" ", off_char = "#", return_cpp_code = True));


################################################################################
################################################################################
################################################################################
######        ##############    ###############       #########              ###
####            ############     ############           ######                ##
###     ####     ##########      ##########              #####               ###
##    ########    #########       #########    #######    ####    ##############
##    #########  #########   ##   ########    #########   ####    ##############
##    ###################    ##    #######    ################    ##############
###      ################   ####   #######    ################    ##############
####          ##########    ####    ######   #################               ###
######           #######   ######   ######   #####        ####               ###
###########       #####    ######    #####   #####        ####    ##############
##############    #####              #####    #########   ####    ##############
###############    ###                ####    #########   ####    ##############
#    ##########    ###    #########   ####    #########   ####    ##############
##    ########    ###    ##########    ####    #######    ####    ##############
##                ###   ############   #####              ####                ##
####            ####    ############    #####            #####                ##
#######      #######   ##############   ########     ##########               ##
################################################################################
################################################################################

assert len(sys.argv) > 1, "image parameter is required";
opts, args = getopt.getopt(sys.argv[2:], "-h", ["cpp_code", "on_char=",
                                                "off_char=", "char_width=",
                                                "char_height_width_ratio=",
                                                "separation_threshold_percent="])
opts = dict(opts);

if "-h" in opts or "--help" in opts:
  print("""
usage: <python script> image_file_path [options]
       This utility displays a image(picture) using terminal characters.
       Additionally it can print a minial C++ code to print the desired
       image on stdout.
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

    """);
else:
  func_params = {};
  for i in ["--cpp_code", "--on_char", "--off_char", "--char_width",
            "--char_height_width_ratio", "--separation_threshold_percent"]:
    if i in opts:
      if i == "--cpp_code":
        opts[i] = True;
      elif i == "--char_width" or i == "--separation_threshold_percent":
        opts[i] = int(opts[i]);
      elif i == "--char_height_width_ratio":
        opts[i] = float(opts[i]);
      func_params[i[2:]] = opts[i];
  print(Image2CharImage(sys.argv[1], **func_params));

