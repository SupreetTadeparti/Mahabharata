const express = require("express");
const ejs = require("ejs");
const app = express();
const data = require("./data.json");

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("index", req.query);
});

app.get("/toc", (req, res) => {
  res.render("toc", req.query);
});

app.get("/data", (_req, res) => {
  res.json(data);
});

app.listen(3000, () => {
  console.log("Listening on port ", 3000);
});
