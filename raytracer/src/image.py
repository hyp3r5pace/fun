import sys

def image_print():
    """
      Create a image file
    """

    image_width = 256
    image_height = 256

    print("P3")
    print(f"{image_width} {image_height}")
    print("255")

    for j in range(image_height, 0, -1):
        print(f"\rScanlines Remaining: {j}", file=sys.stderr)

        for i in range(0, image_width):            
            
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0.25


            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f"{ir} {ig} {ib}")

if __name__ == "__main__":
    image_print()
