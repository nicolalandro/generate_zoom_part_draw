from PIL import Image, ImageDraw

# the two image should have the same size
img_a = Image.open('11_hr_magma.png')
img_b = Image.open('11_sr_magma.png')

padding = 10
big_space = 70
scale_down = 6
rect_width = 10
line_width = 3
box_position = [1200, 2200]
box_dim = 600
fill_color = (255, 0, 0)

def draw_and_crop(img, rect, width=rect_width, color=fill_color):
    crop = img.crop(rect)

    draw = ImageDraw.Draw(img)
    draw.rectangle(rect, outline=color, width=width)
    return img, crop

size_h = max(int(img_a.height/scale_down), (box_dim * 2) + padding) + (padding * 2)
size_w = (int(img_a.width/scale_down) * 2) + box_dim + (padding * 2) + (big_space * 2)
new_image = Image.new('RGB', (size_w, size_h), color = 'white')

rect = box_position + [x + box_dim for x in box_position]
img1, crop1 = draw_and_crop(img_a, rect)
img1 = img1.resize([int(img_a.height/scale_down), int(img_a.width/scale_down)])
img1_pad_w = padding
img1_pad_h = int(size_h/2 - (img_a.height/scale_down/2))
new_image.paste(img1, (img1_pad_w, img1_pad_h))
crop1_pad_w = padding + int(img_a.width/scale_down) + big_space
crop1_pad_h = padding
new_image.paste(crop1, (crop1_pad_w, crop1_pad_h))

img2, crop2 = draw_and_crop(img_b,rect)
img2 = img2.resize([int(img_a.height/scale_down), int(img_a.width/scale_down)])
img2_pad_w = padding + int(img_a.width/scale_down) + big_space*2 + box_dim
img2_pad_h = int(size_h/2 - (img_a.height/scale_down/2))
new_image.paste(img2, (img2_pad_w, img2_pad_h))
crop2_pad_w = padding + int(img_a.width/scale_down) + big_space
crop2_pad_h = padding * 2 + box_dim
new_image.paste(crop2, (crop2_pad_w, crop2_pad_h))

draw = ImageDraw.Draw(new_image)
draw.line((img1_pad_w + int(rect[0]/scale_down), img1_pad_h + int(rect[1]/scale_down), crop1_pad_w, crop1_pad_h), fill=fill_color, width=line_width)
draw.line((img1_pad_w + int(rect[0]/scale_down) + int(box_dim/scale_down), img1_pad_h + int(rect[1]/scale_down) + int(box_dim/scale_down), crop1_pad_w, crop1_pad_h + box_dim), fill=fill_color, width=line_width)

draw.line((img2_pad_w + int(rect[0]/scale_down), img2_pad_h + int(rect[1]/scale_down), crop2_pad_w + box_dim, crop2_pad_h), fill=fill_color, width=line_width)
draw.line((img2_pad_w + int(rect[0]/scale_down) + int(box_dim/scale_down), img2_pad_h + int(rect[1]/scale_down) + int(box_dim/scale_down), crop2_pad_w + box_dim, crop2_pad_h + box_dim), fill=fill_color, width=line_width)


new_image.save('out.png')
