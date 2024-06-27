from PIL import Image, ImageDraw

CANVAS_SIZE = 250
NUM_FRAMES = 60
SPHERE_RADIUS = 75
CENTER = (CANVAS_SIZE // 2, CANVAS_SIZE // 2)
SPHERE_COLOR = (255, 0, 0)


def draw_sphere_slice(draw: ImageDraw.ImageDraw, current_radius: int) -> None:
    """
    Draw a sphere slice on the given draw object.

    :param draw: ImageDraw object
    :param current_radius: Current radius of the sphere
    """

    draw.ellipse(
        [
            (CENTER[0] - current_radius, CENTER[1] - current_radius),
            (CENTER[0] + current_radius, CENTER[1] + current_radius),
        ],
        fill=SPHERE_COLOR,
    )


def get_data_as_images() -> list[Image.Image]:
    """
    Generate frames of a sphere being sliced.

    :return: List of frames
    """

    images = []

    # Generate frames
    for frame in range(NUM_FRAMES):
        if frame < NUM_FRAMES // 2:
            # Growing phase
            current_radius = (SPHERE_RADIUS * frame) // (NUM_FRAMES // 2)
        else:
            # Shrinking phase
            current_radius = (SPHERE_RADIUS * (NUM_FRAMES - frame - 1)) // (
                NUM_FRAMES // 2
            )

        image = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw_sphere_slice(draw, current_radius)

        images.append(image)

    return images
