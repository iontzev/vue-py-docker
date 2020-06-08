db.createUser(
    {
        user: "devbase_admin",
        pwd: "devbase_password",
        roles :[ { role: "readWrite", db: "devbase"}]
    }
)

