# Version 1.0 creada por Fejendee :)

import argparse
import math
import shutil
import sys
import time

LOGO = [
    "                   -`",
    "                .o+`",
    "               `ooo/",
    "              `+oooo:",
    "             `+oooooo:",
    "             -+oooooo+:",
    "           `/:-:++oooo+:",
    "          `/++++/+++++++:",
    "         `/++++++++++++++:",
    "        `/+++ooooooooooooo/`",
    "       ./ooosssso++osssssso+`",
    "      .oossssso-````/ossssss+`",
    "     -osssssso.      :ssssssso.",
    "    :ssssssss/        osssso+++.",
    "   /ossssssss/        +ssssooo/-",
    " `/ossssso+/:-        -:/+osssso+-",
    "`+sso+:-`                 `.-/+oso:",
    "++:.                           `-/+/",
    ".`                                 `/",
]

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}


def rotate_logo(angle):
    width = max(len(line) for line in LOGO)
    center = width / 2
    scale = abs(math.cos(angle))

    rotated = []

    for line in LOGO:
        output = [" "] * width

        for input, char in enumerate(line):
            if char == " ":
                continue

            distance = input - center
            new_x = round(center + distance * scale)

            if 0 <= new_x < width:
                output[new_x] = char

        rotated.append("".join(output).rstrip())

    return rotated


def draw(lines, color):
    terminal_width = shutil.get_terminal_size((80, 24)).columns
    logo_width = max(len(line) for line in lines)
    padding = max((terminal_width - logo_width) // 2, 0)

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.write(color)

    for line in lines:
        sys.stdout.write(" " * padding + line + "\n")

    sys.stdout.write("\033[0m")
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(
        description="A spinning Arch Linux logo for the terminal."
    )

    parser.add_argument(
        "--color",
        choices=COLORS,
        default="cyan",
    )

    parser.add_argument(
        "--speed",
        type=float,
        default=1.0,
    )

    args = parser.parse_args()

    angle = 0
    delay = max(0.02, 0.08 / args.speed)
    color = COLORS[args.color]

    sys.stdout.write("\033[?25l")

    try:
        while True:
            draw(rotate_logo(angle), color)
            angle += 0.12

            if angle >= math.pi * 2:
                angle = 0

            time.sleep(delay)

    except KeyboardInterrupt:
        pass

    finally:
        sys.stdout.write("\033[?25h")
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
