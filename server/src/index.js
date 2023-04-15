import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import { MongoClient } from "mongodb";
import * as dotenv from "dotenv";

const app = express();
dotenv.config();

app.use(cors());
app.use(bodyParser.json());

let emails = [];
console.log(emails);

// Connecting to MongoDB and defining collection
const url = process.env.MONGO_URL;
const dbName = "flashfin";
const client = new MongoClient(url);
client.connect(function (err) {
  console.log("Connected successfully to server");
});

// name of the collection
const collectionName = "userEmails";

// fetching exixting data
const getInputsFromDb = async () => {
  const db = client.db(dbName);
  const collection = db.collection(collectionName);
  const result = await collection.findOne({ name: "inputs" });
  return result ? result.inputs : [];
};

getInputsFromDb()
  .then((result) => {
    emails = result;
    console.log(emails);
  })
  .catch((error) => {
    console.log(error);
  });

app.post("/submit", async (req, res) => {
  let userInput = req.body.userInput;
  emails.push(userInput);
  console.log(emails);

  // Define collection and insert new input into MongoDB collection
  const db = client.db(dbName);
  const collection = db.collection(collectionName);

  try {
    await collection.updateOne(
      { name: "inputs" },
      { $set: { inputs: emails } },
      { upsert: true }
    );
    console.log("Input saved to database");
    res.send({ message: "Input received" });
  } catch (error) {
    console.log(error);
    res.status(500).send({ error: "Error saving input to database" });
  }
});

app.listen(5000, () => {
  console.log("Server is running on port 5000");
});
