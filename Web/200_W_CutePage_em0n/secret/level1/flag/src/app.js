const express = require('express')
const app = express()
const port = 3000
app.use(express.urlencoded());

users = [];

app.all('/flag', (req, res) => {
  return res.send("f0rtn1ght{")
})


app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})