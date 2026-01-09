mydict={
  "Name":"Yash" , "Class": "XIIA" , "RNO":27 , "Stream":"Non med"
}


#get method tb use krenge jb kisi key ki value chahiye hogi

Cls = mydict.get("Yash" , "Nhi mila") #agr key nhi mile to dusri value aajayegi "Nhi mila"

print(Cls)