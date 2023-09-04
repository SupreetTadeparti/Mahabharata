const express = require("express");
const app = express();
const data = require("./data.json");
const sdata = require("./sdata.json");

require("dotenv");

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (_req, res) => {
  res.render("index");
});

app.get("/read", (req, res) => {
  res.render("read", req.query);
});

app.get("/toc", (req, res) => {
  res.render("toc", req.query);
});

app.get("/data", (req, res) => {
  res.json(data[`Book ${req.query.book}`][`Section ${req.query.section}`]);
});

app.get("/sdata", (req, res) => {
  res.json(sdata[`Book ${req.query.book}`][`Section ${req.query.section}`]);
});

app.listen(3000);
