import os
import sys
import exifread
import datetime





def main():
    #geoscrape()

    assort()








def geoscrape():
    geo_dict = {}
    dirname = r"C:\Users\perezj\Desktop\exifheader\fishtrip"
    for fi in os.listdir(dirname):
        print str(buildgeo(os.path.join(dirname, fi)))[1:-1]






def assort():
    nicedate = get_nice_date()
    path = r"C:\trans\trans\pics\20160520"
    for im in os.listdir(path):
        name = os.path.basename(im)
        shortname = name.split("_")[1].split(".")[0]
        loadname = "IMG_" + nicedate + "_" + shortname + ".jpg"
        pathname = r"C:\trans\trans\pics\load" + "\\" + loadname
        print pathname
        infile = os.path.join(path, im)
        print infile
        os.rename(infile, pathname)
        
        






def get_nice_date(alt=None):
    dtn = str(datetime.datetime.now()).split(" ")
    dayValue = "".join(dtn[0].split("-"))
    dayValueAlt = dayValue + "_" + "".join(str("".join(dtn[1].split(":"))).split("."))
    if alt == None:
        return dayValue
    else:
        return dayValueAlt
    



 
 
def buildgeo(path_name):
    #path_name = "IMG_0674.JPG"
    # Open image file for reading (binary mode)
    f = open(path_name, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    counter = 0
    for i in tags:
        #print i
        if i == "GPS GPSLatitude":
            y = convertcoord(tags[i])
            counter += 1
        if i == "GPS GPSLongitude":
            x = convertcoord(tags[i])
            counter += 1
    if counter == 2:
        return [x,y]


def convertcoord(coord):
    #print coord
    coord_list = str(coord)[1:-1].split(",")
    deg = coord_list[0]
    
    sec_raw = coord_list[2][1:].split("/")
    sec = float(sec_raw[0]) / float(sec_raw[1]) / 60
    #print "sec: " + str(sec)
    
    minutes_raw = float(coord_list[1][1:]) + sec
    minutes = minutes_raw / 60
    #print minutes
    
    return float(deg) + minutes
    



if __name__ == "__main__":
    main()






