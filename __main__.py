import os, sys
from time import sleep
from aiogram import Bot, Dispatcher, types, executor
from PIL import Image
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def start(message: types.Message):
    if message.text == "/img":
        createIMG()


@dp.message_handler(content_types=["photo", "document", "sticker"])
async def docs(message: types.Message):
    await message.sticker.download(destination_file=f"docs/{message.message_id}.webp")

derb = 60
pos = (derb,derb)
oldp = 0
def merge(im1, im2, maxsize_w, maxsize_h):
    global pos, oldp
    w = min(im1.size[0] + im2.size[0], maxsize_w)
    h = max(im1.size[1], im2.size[1], maxsize_h)
    
    if pos[1]+oldp+im2.getbbox()[3] >= maxsize_h:
        pos = (im1.getbbox()[2]+derb,derb+derb)

        if im1.getbbox()[2]+im2.getbbox()[2]>maxsize_w:
            return None, im1
    else:
        pos = (pos[0],pos[1]+oldp+derb)
    oldp = im2.getbbox()[3]

    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, pos)

    return True, im

def createIMG(img=Image.new("RGBA", (1, 1))):
    kf = 0
    global pos, oldp
    for f in os.listdir("docs"):
        sticker_path = f"docs/{f}"
        im = Image.open(sticker_path)
        status, img = merge(img, im.crop(im.getbbox()), 3508, 2480)
        if status == None:
            img.save(f"done/final_{kf}.png")
            img=Image.new("RGBA", (1, 1))
            pos = (derb,derb)
            oldp = 0
            kf += 1

            im = Image.open(sticker_path)
            status, img = merge(img, im.crop(im.getbbox()), 3508, 2480)
    img.save(f"done/final_{kf}.png")


def main():
    for dir in ["done", "docs"]:
        if not os.path.exists(dir):
            os.makedirs(dir)
    

    executor.start_polling(dp)

if __name__ == "__main__":
    main()