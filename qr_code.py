import qrcode
from PIL import Image
img = qrcode.make('https://www.linkedin.com/in/yaidekar-sudeep-453993360/')
img.show() # qrcode.image.pil.PilImage
img.save("sudeep_linkdein.png")