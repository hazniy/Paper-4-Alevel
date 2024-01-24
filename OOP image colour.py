class Image:
    def __init__(self, thewidth, theheight, thecolour, thedescription):
        self.__Description = thedescription #STRING
        self.__Width = thewidth #INTEGER
        self.__Height = theheight #INTEGER
        self.__FrameColour = thecolour #STRING

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, thedesc):
        self.__Description = thedesc

ThisImage = Image(0,0,'','')
for i in range(0, 49):
    ThisImage = ''

def NewImage (ThisImage, i):
    Description = input('enter description of the image ')
    Height = int(input('enter the height '))
    Width = int(input('enter the width '))
    FrameColour = input('enter the frame colour ')
    ThisImage[i] = Image(Height, Width, FrameColour, Description)
    ThisImage[i].SetDescription(Description)
    print(ThisImage[i].GetDescription(Description))
    print(ThisImage[i].GetHeight(Height))
    print(ThisImage[i].GetWidth(Width))
    print(ThisImage[i].GetColour(FrameColour))

#main
image = NewImage(ThisImage,0)

class Picture(Image):
    # .__PictureText = '' STRING
    # .__PictureLabel = '' STRING
    def __init__(self, text, label, width, height, colour, description):
        Image.__init__(width, height, colour, description)
        self.__PictureText = text
        self.__PictureLabel = label 
