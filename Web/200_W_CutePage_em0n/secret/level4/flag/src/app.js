const express = require('express')
const crypto = require('crypto')
const app = express()
const port = 3000
app.use(express.urlencoded());

users = [];

app.all('/flag', (req, res) => {
  return res.send("0f_")
})


app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})