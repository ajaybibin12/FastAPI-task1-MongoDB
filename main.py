from fastapi import FastAPI,UploadFile,File
from fastapi.encoders import jsonable_encoder
from config.db import conn,db
from models.users import User
from schemas.users import userEntity,usersEntity
from secrets import token_hex
app = FastAPI()


#Here is the function used to upload userprofiles and stores in mongoDB
@app.post("/file_upload")
async def CreateUserProfile(file:UploadFile =File(...)):
    file_ext=file.filename.split(".").pop()
    file_name=token_hex(10)
    file_path=f"{file_name}.{file_ext}"
    with open(file_path,"wb") as f:
        content= await file.read()
        f.write(content)
        profile_url=jsonable_encoder(content)
        profile= await db["profiles"].insert_one(profile_url)
    return {"sucess":True,"file_path":file_path,"message":"file uploaded successfully !"}