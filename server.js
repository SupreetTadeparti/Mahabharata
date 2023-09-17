const express = require("express");
const app = express();
const data = require("./data.json");
const sdata = require("./sdata.json");

const numSections = [
  236, 80, 313, 72, 199, 124, 23, 96, 65, 18, 27, 365, 168, 92, 39, 8, 3, 6,
];

const bookNames = [
  "Adi Parva",
  "Sabha Parva",
  "Vana Parva",
  "Virata Parva",
  "Udyoga Parva",
  "Bhishma Parva",
  "Drona Parva",
  "Karna Parva",
  "Shalya Parva",
  "Sauptika Parva",
  "Stri Parva",
  "Shanti Parva",
  "Anushasana Parva",
  "Ashvamedhika Parva",
  "Ashramavasika Parva",
  "Mausala Parva",
  "Mahaprasthanika Parva",
  "Svargarohanika Parva",
];

require("dotenv");

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (_req, res) => {
  res.render("index");
});

app.get("/read", (req, res) => {
  res.render("read", {
    ...req.query,
    bookNames: bookNames,
    numSections: numSections,
  });
});

app.get("/toc", (req, res) => {
  res.render("toc", {
    ...req.query,
    bookNames: bookNames,
    numSections: numSections,
  });
});

app.get("/data", (req, res) => {
  res.json(data[`Book ${req.query.book}`][`Section ${req.query.section}`]);
});

app.get("/sdata", (req, res) => {
  res.json(sdata[`Book ${req.query.book}`][`Section ${req.query.section}`]);
});

app.listen(3000);
