def userEntity(item) ->dict:
    return {
        "id":str(item["_id"]),
        "profile":str
    }
def usersEntity(entity) ->list:
    return [userEntity(item) for item in entity]