import pandas as pd
states_details={"Andhra Pradesh":[162910,93], "Assam":[78438,117],
      "Arunachal Pradesh":[83743,115], "Bihar":[94163,109],
      "Goa":[3702,172], "Gujarat":[196244,88],
      "Jammu and Kashmir":[55538,126], "Jharkhand":[79716,116],
      "West Bengal":[88752,112], "Karnataka":[191171,88],
      "Kerala": [38852,134], "Madhya Pradesh":[308252,72],
      "Maharashtra":[307713,72], "Manipur":[22327,149],
      "Meghalaya":[22429,149], "Mizoram":[21081,150],
      "Nagaland":[16579,156], "Orissa":[155707,93],
      "Punjab":[50362,128], "Rajasthan":[342359,65],
      "Sikkim":[7096,167], "Tamil Nadu":[130060,92],
      "Tripura":[10486,164], "Uttaranchal":[53643,126],
      "Uttar Pradesh":[240928,81], "Haryana":[44212,131],
      "Himachal Pradesh":[55673,126], "Chhattisgarh":[135192,96]}
#calling pandas module dataframe to create the dataframe from the dictionary
ans=pd.DataFrame.from_dict(states_details,orient="index")
print(ans)
ans.to_csv("python files")   #storing the read values into the state csv file