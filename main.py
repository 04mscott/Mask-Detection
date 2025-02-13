from PIL import Image


if __name__=='__main__':   
    path = '/Users/masonscott/git-repos/Python-Projects/Mask-Detection/Dataset/mask_weared_incorrect/2.png'
    img = Image.open(path)
    img.show()