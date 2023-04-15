import express from "express";
import cors from "cors";
import bodyParser from "body-parser";

const app = express();

app.use(cors());
app.use(bodyParser.json());

let emails = [];
console.log(emails);

app.post("/submit", async (req, res) => {
  let userInput = req.body.userInput;
  emails.push(userInput);
  console.log(emails);
});

app.listen(5000, () => {
  console.log("Server is running on port 5000");
});
