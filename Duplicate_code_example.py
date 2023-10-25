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
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

