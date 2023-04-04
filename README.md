# cloudinaryDownloader
Bu dosya cloudinary assetlerinizi terminal üzerinden topluca indirmek için geliştirilmiştir.
Çalıştırmak için terminalinizden dosyanın bulunduğu dizine gidip python download.py komutunu kullanmanız gerekmektedir.


# Ayarlar
bu kısma cloudinary api bilfgileriniz girmeniz gerekmektedir.
# Cloudinary Api Ayarları
cloudinary.config(
  cloud_name = "",
  api_key = "",
  api_secret = ""
)


bu kısım ise resimlerinizi indireceğiniz klasörün ismidir
folder_name = "Resimler" 

This file has been developed to collectively download cloudinary assets via terminal.
To run it, you need to go to the directory where the file is located from the terminal and use the python download.py command.

# Settings
You need to enter your cloudinary api information in this part.

# Cloudinary Api Settings
cloudinary.config(
  cloud_name = "",
  api_key = "",
  api_secret = ""
)


this part is the name of the folder where you will download your images
folder_name = "Resimler" 
