import pymongo  
from bson.objectid import ObjectId
#Çalıştırmadan once mongodb atlastan bağla ce Command Paltten kotrol et 

myclient = pymongo.MongoClient("mongodb+srv://Odevdb:{VeriTabaniSifresi}@cluster0.yyq2t5s.mongodb.net/test")
mydb = myclient["Odevdb"]
mycollection = mydb["bilgiler"]

isimler = [
  { "name": "ibrahim", "address": "sivas"},
  { "name": "yusuf", "address": "ankara "},
  { "name": "sercan", "address": "hatay"},
  { "name": "eren", "address": "nevsehir"}
]

sonuc = mycollection.insert_many(isimler) #İnsert ekleme yaptık
print(sonuc.inserted_ids) #obje kayıt bilgilerini geri yaz

for i in mycollection.find({},{"_id":0,"name":1,"address":1}):#Bütün kayıtları çeker 
    print(i)
 
#İçinden seçmek için kullnırız    
sonuc2=mycollection.find_one({"name":"sercan"})
print(sonuc2)
sonuc3 = mycollection.find_one({"_id":ObjectId("63aad1  461e02b26e11d8d536")})
print(sonuc3) 

sonuc = mycollection.find().sort('name',1) #artan şekilde -1 azalan şekiilde sırala


#Update islemi
mycollection.update_one(
  {'name':'eren'},
  {'$set': {
    'name':'Murat'
  }}
)

mycollection.delete_one({"name":"yusuf"})
print(sonuc.insterdde)