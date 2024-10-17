import colorgram

# Extract colors from the image
colors = colorgram.extract('/home/dan/Desktop/PYTHON/100 Days of Python/Turtle Module/image.jpg', 30)

# Initialize an empty list to store the RGB tuples
colors_list = []

# Iterate over the extracted colors
for color in colors:
    # Extract the RGB values and append them to the list
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_list.append((new_color))

# Print the list of RGB tuples
print(colors_list)
