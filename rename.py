import os

def main():
	os.system('rm -r dream_r')
	os.mkdir('dream_r')
	for i, f in enumerate(os.listdir('dream')):
		os.system(f'cp dream/{f} dream_r/gmap\\ \\({i+1}\\).jpg')

if __name__ == '__main__':
	main()
