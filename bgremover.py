from rembg import remove
from PIL import Image

input_path = 'C://Users//USER//Pictures//c2.jpg'

output_path = input_path+'_removebg'+'.png'
inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)