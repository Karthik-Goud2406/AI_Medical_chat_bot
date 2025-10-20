# step:1 create an grow api key 

import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

# step:2 convert image to required format 

import base64

#image_file=open('acne.jpg',"rb")



def encode_image(image_path):

      image_file=open('acne.jpg',"rb")
      return base64.b64encode(image_file.read()).decode("utf-8")

#step:3 multimodel llm


from groq import Groq

query="is there any wrong thing in my face"

model="meta-llama/llama-4-scout-17b-16e-instruct"


#function
def analyse_the_image(query,model,encoded_image):

   client=Groq()

   messages=[

    {
   "role":"user",
   "content":[
       {
           "type":"text",
           "text":query
       },

       {
           "type":"image_url",
           "image_url":{
               
               "url":f"data:image/jpeg;base64,{encoded_image}",


           },
    
       },
   ],



    }]

   chat_completion=client.chat.completions.create(
   messages=messages,
   model=model

   )

   return chat_completion.choices[0].message.content