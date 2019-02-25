import os
import json
import hashlib
from shutil import copyfile

sourceLocation = "inputs/"
outputLocation = "out/"
docLocation = "../docs/"

hasher = hashlib.md5()


def render():
    print("Rendering \"{}\"".format(name))
    # Use imagemagick to convert the SVG to a PNG
    os.system("magick convert -background none -size 192x192 {}{} {}{}.png".format(sourceLocation, item, outputLocation+"drawable-xxxhdpi/", name))
    copyfile("{}{}.png".format(outputLocation+"drawable-xxxhdpi/", name), "{}{}.png".format(docLocation+"icons/", name))


# Get current json
data = {}
with open("store.json", "r") as read:
    data = json.load(read)

with open("drawable.xml", "w") as drawable, open("iconpack.xml", "w") as iconpack, open("{}iconList.txt".format(docLocation), "w") as meta:

    # For each input
    for item in os.listdir(sourceLocation):

        # Get file hash
        currentHash = ""
        with open("{}{}".format(sourceLocation, item), "rb") as afile:
            buf = afile.read()
            hasher.update(buf)
            currentHash = hasher.hexdigest()

        name = os.path.splitext(item)[0].lower().replace(" ", "_")

        # Auto generate portions of drawable and iconpack
        drawable.write("<item drawable=\""+name+"\" />\n")
        iconpack.write("<item>"+name+"</item>\n")
        meta.write("{}.png\n".format(name))

        # New file
        if name not in data.keys():
            data[name] = currentHash
            print("Added new file \"{}\" to store.json".format(name))
            render()

        # If file changed
        elif data[name] != currentHash:

            print(data[name], currentHash)
            print("Updating hash for \"{}\"".format(name))
            data[name] = currentHash

            render()


# Update json to reflect the py object
with open("store.json", "w") as outfile:
    json.dump(data, outfile)

print("Finished!")
