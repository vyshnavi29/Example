# Create a function to calculate both area and perimeter.
def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Create separate functions for volume and surface area.
def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

def calculate_surface_area(length, width, height):
    lw = length * width
    lh = length * height
    wh = width * height
    return 2 * (lw + lh + wh)

