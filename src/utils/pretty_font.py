from libs import ptext
from src.utils.constants import FONT_PATH


def get_text(
    text,
    color=(0, 0, 0),
    ocolor=(255, 255, 255),
    owidth=1.1,
    fontname=FONT_PATH,
    fontsize=20,
    bold=False,
):
    text_object = ptext.draw(
        text,
        (-999, -999),
        owidth=owidth,
        ocolor=ocolor,
        color=color,
        fontname=fontname,
        fontsize=fontsize,
        bold=bold,
    )
    return text_object[0]
