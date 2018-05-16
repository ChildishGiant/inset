import os


sourceLocation = "inputs/"
outputLocation = "out/" 

drawable = open("drawable.xml","w") 
iconpack = open("iconpack.xml","w") 

# For each input
for item in os.listdir("inputs"):

    name = os.path.splitext(item)[0].lower().replace(" ","_")

    drawable.write("<item drawable=\""+name+"\" />\n")
    iconpack.write("<item>"+name+"</item>\n") 

    os.system("magick convert -background none -size 192x192 {}{} {}{}.png".format(sourceLocation, item, outputLocation+"drawable-xxxhdpi/", name ) )

 
drawable.close()
iconpack.close() 
