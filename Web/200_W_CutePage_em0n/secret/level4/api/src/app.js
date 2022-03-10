const express = require('express')
const crypto = require('crypto')
const app = express()
const port = 3000
app.use(express.urlencoded());

users = [];

app.all('/robot.txt', (req, res) => {
  return res.send("Tui là một con robot 🤖<img src='https://i.pinimg.com/originals/1e/95/5d/1e955db131fe1df6719a9445b94096d2.png'>")
})

app.all('/monkey.txt', (req, res) => {
  return res.send("Tui là một con khỉ 🐵<img src='https://cdn-icons-png.flaticon.com/512/185/185852.png'>")
})

app.all('/redirect', (req, res) => {
  if (req.query.url) {
    return res.redirect(req.query.url)
  }
  return res.send("Thiếu trường url rồi 🙃")
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})