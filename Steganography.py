import numpy as np 
from PIL import Image

class Steganography:
    def steganography():
        img1 = Image.open("cover.jpg")
        grey_image1 = np.array(img1.convert('L'))

        img2 = Image.open("secret.png")
        grey_image2 = np.array(img2.convert('L'))

        new = np.zeros(grey_image2.size)
        new.shape = (256,256)

        for i in range (256):
            for j in range (256):
                grey_image1[i][j] = grey_image1[i][j] & 240  

        
        for i in range (256):
            for j in range (256):
                if len(np.binary_repr(grey_image2[i][j])) == 7: 
                    grey_image2[i][j] = grey_image2[i][j] >> 3
                elif len(np.binary_repr(grey_image2[i][j])) == 8:
                    grey_image2[i][j] = grey_image2[i][j] >> 4        
                    
  
        for i in range (256):
            for j in range (256):
                new[i][j] = grey_image1[i][j] + grey_image2[i][j]
        new = new.astype(int) 
        return new
    
    
    def reverse():
        final = Steganography.steganography()

        for i in range (256):
            for j in range (256):
                final[i][j] = final[i][j] & 15
                final[i][j] = final[i][j] << 4         
        return final
    
            

                
        
   
        
        
        
            
                  



        
        
    
