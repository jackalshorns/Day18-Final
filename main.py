import colorgram

colors = colorgram.extract('20_001.jpg', 25)

rgb_colors = []
for color in colors:
    print(color.rgb)
    r = color.rgb
    g = color.rgb.g
    b = color.rgb.b
    new_rgb_color = (r, g, b)
    rgb_colors.append(new_rgb_color)

print(rgb_colors)





