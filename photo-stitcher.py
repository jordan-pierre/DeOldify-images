import matplotlib.pyplot as plt
from PIL import Image

f = plt.figure(figsize=(12,6))
plt.subplots_adjust(left=0.1, bottom=0, right=0.2, top=1.02, wspace=0.02, hspace=0.02)
plt.axis('Off')

image_folder = 'photos/'
images = ['grammys dad original.jpg', 'grammys dad - color20.png', 'grammys dad - color20 + GFPGAN.png']
titles = ['Original', 'DeOldify', 'DeOldify + GFP-GAN']

for i, image in enumerate(images):
    print(image, i)
    sp = f.add_subplot(1, 3, i+1)
    sp.axis('Off')
    sp.get_xaxis().set_visible(False)
    sp.get_yaxis().set_visible(False)
    sp.set_title(titles[i], fontsize=16)
    data = Image.open(image_folder + image, 'r')
    data = data.convert('RGB')
    plt.imshow(data)
    plt.tight_layout()

plt.savefig(image_folder + 'demo.png')
plt.show()
