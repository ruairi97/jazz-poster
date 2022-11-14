# !/usr/bin/env python

from gimpfu import *

'''
write the python function to achive filterin
'''
 
def jazz_poster(file1, file2, file3, file4, file5, file6, file7, file8, file9, file10, file11, text1, font1, text2, font2, text3, font3):# args are following soon
       # make a new image
       posterW, posterH = 2500, 3500
       posterImage = gimp.Image(posterW, posterH, RGB)
       gimp.Display(posterImage)
       gimp.message("new image created")
       

       # make the colors
       bColor = gimpcolor.RGB(250, 149, 61)
       fColor = gimpcolor.RGB(255, 255, 255)
       gimp.set_background(bColor)
       gimp.set_foreground(fColor)
       gimp.message("b and f colors made")

       # make background
       backLayer = gimp.Layer(posterImage, "background",posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(backLayer)
       pdb.gimp_drawable_fill(backLayer, 1)
       gimp.message("background made")
       
       
       # make image 1 block red 1 (behind smile and piano key)
       image1 = pdb.file_jpeg_load(file1, file1)
       pdb.gimp_image_scale(image1, 1550, 900)
       pdb.gimp_edit_copy(image1.layers[0])
       layer1 = gimp.Layer(posterImage, "image1",1550, 900, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer1)
       floatingLayer = pdb.gimp_edit_paste(layer1, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer1.translate(500, 450)
       pdb.gimp_item_transform_rotate(layer1 ,0.174533, 1, 0, 0)
       gimp.message("layer1 made")
       

       # make image 2 Smile- load, scale, copy, make_layer, paste, anchor, translate
       image2 = pdb.file_png_load(file2, file2)
       pdb.gimp_image_scale(image2, 2400, 1500)
       pdb.gimp_edit_copy(image2.layers[0])
       layer2 = gimp.Layer(posterImage, "image2", 2400, 1500, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer2)
       floatingLayer = pdb.gimp_edit_paste(layer2, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer2.translate(0, 160)
       gimp.message("layer2 made")

       
       # make image 3 paino key (in front of smile and red block)
       image3 = pdb.file_png_load(file3, file3)
       pdb.gimp_image_scale(image3, 240, 240)
       pdb.gimp_edit_copy(image3.layers[0])
       layer3 = gimp.Layer(posterImage, "image3",250, 250, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer3)
       floatingLayer = pdb.gimp_edit_paste(layer3, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer3.translate(1140, 759)
       pdb.gimp_item_transform_rotate(layer3 ,6.19592, 1, 0, 0)
       gimp.message("layer3 made")
       
       # make image 4 red block 2 (behind jazz man left)
       image4 = pdb.file_jpeg_load(file4, file4)
       pdb.gimp_image_scale(image4, 764, 405)
       pdb.gimp_edit_copy(image4.layers[0])
       layer4 = gimp.Layer(posterImage, "image4",764, 405, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer4)
       floatingLayer = pdb.gimp_edit_paste(layer4, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer4.translate(100, 2350)
       pdb.gimp_item_transform_rotate(layer4 ,1.91986, 1, 0, 0)
       gimp.message("layer4 made")

       # make image 5 Jazz Man Left (in front of red block 2)- load, scale, copy, make_layer, paste, anchor, translate
       image5 = pdb.file_png_load(file5, file5)
       pdb.gimp_image_scale(image5,850, 750)
       pdb.gimp_edit_copy(image5.layers[0])
       layer5 = gimp.Layer(posterImage, "image5",850, 750, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer5)
       floatingLayer = pdb.gimp_edit_paste(layer5, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer5.translate(-100, 2280)
       gimp.message("layer5 made")
       
       # make image 6 red block 3 (behind jazz man right)
       image6 = pdb.file_jpeg_load(file6, file6)
       pdb.gimp_image_scale(image6, 764, 405)
       pdb.gimp_edit_copy(image6.layers[0])
       layer6 = gimp.Layer(posterImage, "image6",764, 405, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer6)
       floatingLayer = pdb.gimp_edit_paste(layer6, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer6.translate(1700, 2400)
       pdb.gimp_item_transform_rotate(layer6 ,4.36332, 1, 0, 0)
       gimp.message("layer6 made")
       
       # make image 7 Jazz Man Right- load, scale, copy, make_layer, paste, anchor, translate
       image7 = pdb.file_png_load(file7, file7)
       pdb.gimp_image_scale(image7, 565, 690)
       pdb.gimp_edit_copy(image7.layers[0])
       layer7 = gimp.Layer(posterImage, "image7", 565, 690, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer7)
       floatingLayer = pdb.gimp_edit_paste(layer7, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer7.translate(1932, 2387)
       gimp.message("layer7 made")
       
       # make image 8 red block 4 (behind 'Cork')
       image8 = pdb.file_jpeg_load(file8, file8)
       pdb.gimp_image_scale(image8, 743, 418)
       pdb.gimp_edit_copy(image8.layers[0])
       layer8 = gimp.Layer(posterImage, "image8",743, 418, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer8)
       floatingLayer = pdb.gimp_edit_paste(layer8, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer8.translate(902, 2354)
       pdb.gimp_item_transform_rotate(layer8 ,0.139626, 1, 0, 0)
       gimp.message("layer8 made")

       
       # make image 9 red block 5 (behind 'Jazz')
       image9 = pdb.file_jpeg_load(file9, file9)
       pdb.gimp_image_scale(image9, 660, 363)
       pdb.gimp_edit_copy(image9.layers[0])
       layer9 = gimp.Layer(posterImage, "image9",660, 363, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer9)
       floatingLayer = pdb.gimp_edit_paste(layer9, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer9.translate(1094, 2711)
       gimp.message("layer9 made")
       
       
       # make image 10 red block 6 (behind 'Smile') 
       image10 = pdb.file_jpeg_load(file10, file10)
       pdb.gimp_image_scale(image10, 654, 369)
       pdb.gimp_edit_copy(image10.layers[0])
       layer10 = gimp.Layer(posterImage, "image10",654, 369, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer10)
       floatingLayer = pdb.gimp_edit_paste(layer10, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer10.translate(535, 1600)
       pdb.gimp_item_transform_rotate(layer10 ,6.10865, 1, 0, 0)
       gimp.message("layer10 made")
       
       # make image 11 red block 7 (behind 'for Jazz') 
       image11 = pdb.file_jpeg_load(file11, file11)
       pdb.gimp_image_scale(image11, 715, 400)
       pdb.gimp_edit_copy(image11.layers[0])
       layer11 = gimp.Layer(posterImage, "image11",715, 400, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer11)
       floatingLayer = pdb.gimp_edit_paste(layer11, True)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer11.translate(1155, 1678)
       pdb.gimp_item_transform_rotate(layer11 ,0.261799, 1, 0, 0)
       gimp.message("layer11 made")
       
       
       # make a text layer Cork
       textLayer1 = pdb.gimp_text_fontname(posterImage, None, 725, 2250, text1, 100, True, 300, PIXELS, font2)
       pdb.gimp_item_transform_rotate(textLayer1, 6.10865, 1, 0, 0)

       # make a text layer Jazz
       textLayer2 = pdb.gimp_text_fontname(posterImage, None, 1150, 2585, text2, 100, True, 300, PIXELS, font2)
       pdb.gimp_item_transform_rotate(textLayer2, 6.10865, 1, 0, 0)

       # make a text layer Smile for Jazz
       textLayer3 = pdb.gimp_text_fontname(posterImage, None, 318, 1627, text3, 100, True, 250, PIXELS, font3)
       pdb.gimp_item_transform_rotate(textLayer3, 0.174533, 1, 0, 0)

       

# end filter

register(
     "python_fu_jazz_poster",
     "Poster maker",
     "Poster maker with some interface",
     "RH",
     "@MSCIM2021",
     "2021",
     "Jazz Poster",
     "",
     [# add input arguments
         (PF_FILE, "file1", "Choose Image 1", ""),
         (PF_FILE, "file2", "Choose Image 2", ""),
         (PF_FILE, "file3", "Choose Image 3", ""),
         (PF_FILE, "file4", "Choose Image 4", ""),
         (PF_FILE, "file5", "Choose Image 5", ""),
         (PF_FILE, "file6", "Choose Image 6", ""),
         (PF_FILE, "file7", "Choose Image 7", ""),
         (PF_FILE, "file8", "Choose Image 8", ""),
         (PF_FILE, "file9", "Choose Image 9", ""),
         (PF_FILE, "file10", "Choose Image 10", ""),
         (PF_FILE, "file11", "Choose Image 11", ""),
         (PF_STRING, "text1", "String1", "Cork"),
         (PF_FONT, "font1", "Cork", "Arial"),
         (PF_STRING, "text1", "String2", "Jazz"),
         (PF_FONT, "font2", "Jazz", "Arial"),
         (PF_STRING, "text3", "String3", "Smile for Jazz"),
         (PF_FONT,"font3", "Copyright","Arial"),
     ],
     [],
     jazz_poster,
     menu = "<Image>/File/Create/CS6102/"
)
 
main()


       
       
       
       
       
       
       
       









       

       

       
