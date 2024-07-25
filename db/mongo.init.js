db.createUser({
    user: 'admin',
    pwd: 'admin',
    roles: [
      {
        role: 'readWriteAnyDatabase',
        db: 'admin'
      }
    ]
})