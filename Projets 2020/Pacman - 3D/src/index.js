require("dotenv").config();
const express = require("express");

const api = express();

api.use(express.static("static"));

const port = process.env.PORT || 8080;
api.listen(port, () => console.log("Server is listening in http://localhost:", port));
