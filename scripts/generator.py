import os
from PIL import Image, ImageFont, ImageDraw
from random import choice, random
from string import ascii_lowercase
from src.shared import genereated_dir

WIDTH, HEIGHT = 108, 30

count = 100

font = ImageFont.truetype(
    os.path.join(os.path.dirname(__file__), "..", "fonts", "NotoSans-Regular.ttf"), 18
)


def gen():
    image = Image.new("RGB", (WIDTH, HEIGHT))

    if random() > 0.5:
        # alphabetical
        a = choice(ascii_lowercase)
        b = choice(ascii_lowercase)
        c = choice(ascii_lowercase)
        d = choice(ascii_lowercase)
        ans = a + b + c + d

        image = draw(image, [a, b, c, d])

    else:
        # arithmetic
        a = choice(range(10))
        b = choice(range(10))
        op = choice(["+", "-", "x"])

        if op == "+":
            ans = f"{a}+{b}="
        elif op == "-":
            ans = f"{a}-{b}="
        else:
            ans = f"{a}x{b}="

        if op == "x" and random() > 0.5:
            op = "X"

        image = draw(image, [str(a), op, str(b), "="])

    return image, str(ans)


def draw(image: Image, text: list[str]) -> Image:
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=(255, 255, 255))

    for i, t in enumerate(text):
        txt = Image.new("RGBA", (30, 30))
        d = ImageDraw.Draw(txt)
        d.text(
            (choice(range(0, 15)), -5 + choice(range(0, 15))),
            t,
            font=font,
            fill=(255, 0, 0),
        )
        image.paste(txt, (14 + (i * 20), 0), txt)

    # draw noise lines
    for i in range(30):
        fill = choice([120, 200])
        x = random() * WIDTH
        y = random() * HEIGHT

        draw.line(
            (
                x,
                y,
                x + 15 * (random() - 1),
                y + 15 * (random() - 1),
            ),
            fill=(fill, fill, fill),
            width=1,
        )

    return image


if __name__ == "__main__":
    for i in range(count):
        image, ans = gen()
        image.save(os.path.join(genereated_dir, f"{i}.png"))
        with open(os.path.join(genereated_dir, f"{i}.txt"), "w") as f:
            f.write(ans)
            print(f"Generated {i}.png and {i}.txt")

    print("Done")
