import random
from modules import *
from modules.Cone import Cone
from modules.Cylinder import Cylinder
from modules.OctagonalPrism import OctagonalPrism
from modules.PentagonalPrism import PentagonalPrism
from modules.Pyramid import Pyramid
from modules.SquarePrism import SquarePrism
from modules.TriangularPrism import TriangularPrism

# List of shape names
shapes_list = ["Cone", "Cylinder", "OctagonalPrism", "PentagonalPrism", "Pyramid", "SquarePrism", "TriangularPrism"]

# Function to generate random shapes with random measurements
def generate_random_shapes(num_shapes):
    random_shapes = []
    for _ in range(num_shapes):
        shape_type = random.choice(shapes_list)

        if shape_type == "Cone":
            radius = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = Cone(radius, height)
        elif shape_type == "Cylinder":
            radius = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = Cylinder(radius, height)
        elif shape_type == "OctagonalPrism":
            side_length = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = OctagonalPrism(side_length, height)
        elif shape_type == "PentagonalPrism":
            side_length = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = PentagonalPrism(side_length, height)
        elif shape_type == "Pyramid":
            side = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = Pyramid(side, height)
        elif shape_type == "SquarePrism":
            side_length = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = SquarePrism(side_length, height)
        elif shape_type == "TriangularPrism":
            base_length = random.uniform(1, 500)
            height = random.uniform(1, 500)
            shape = TriangularPrism(base_length, height)

        if shape_type in ["Cone","Cylinder"]:
            random_shapes.append((shape_type, shape.height, shape.radius,""))
        else:
            random_shapes.append((shape_type, shape.height, shape.side,""))
            # Store shape details as a tuple

    return random_shapes

# Generate 50,000 random shapes
num_shapes = 500000
random_shapes = generate_random_shapes(num_shapes)

# Save the generated shapes to a file
with open("random_shapesHuge.txt", "w") as file:
    file.write(str(num_shapes) + "\n")  # Write the array size to the file
    for shape in random_shapes:
        shape_str = " ".join(str(val) for val in shape)  # Convert the tuple to a space-separated string
        file.write(shape_str)

print("Generated {} random shapes and saved them to 'random_shapesHuge.txt'".format(num_shapes))
