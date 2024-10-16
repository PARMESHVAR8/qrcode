import qrcode as qr


#qrcode a built in .py, download first it . 
# create a virtual enve. 
 


image = qr.make("https://www.youtube.com/@Yoga_asana")

#"" in this the link of any web,video...abs


image.save("YTchannel.png")

#.png save the photo in my file system
