import colorgram

# Extract colors from the image
colors = colorgram.extract('/home/dan/Desktop/PYTHON/100 Days of Python/Turtle Module/image.jpg', 20)

# Initialize an empty list to store the RGB tuples
colors_list = []

# Iterate over the extracted colors
for color in colors:
    # Extract the RGB values and append them to the list
    rgb = color.rgb
    colors_list.append((rgb.r, rgb.g, rgb.b))

# Print the list of RGB tuples
print(colors_list)
