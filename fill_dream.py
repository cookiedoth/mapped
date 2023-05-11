import os
import random
from PIL import Image

TARGET_PATH = 'dream'
BASE_PATH = 'dataset/train'
SEED = 42
IMG_CNT = 25
TARGET_SIZE = (512, 512)

def save(filename):
	img = Image.open(os.path.join(BASE_PATH, filename))
	width, height = img.size
	new_img = img.crop((width // 2, 0, width, height)).resize(TARGET_SIZE)
	new_img.save(os.path.join(TARGET_PATH, filename))

def main():
	try:
		images = os.listdir(BASE_PATH)
	except FileNotFoundError:
		print('Dataset not found')
		return

	random.seed(42)
	random.shuffle(images)
	filenames = images[:IMG_CNT]

	os.system(f'rm -r {TARGET_PATH}')
	os.mkdir(TARGET_PATH)

	for f in filenames:
		save(f)

if __name__ == '__main__':
	main()
