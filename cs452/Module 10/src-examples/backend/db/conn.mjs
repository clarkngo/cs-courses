import { MongoClient } from "mongodb";

const connectionString = process.env.ATLAS_URI || "mongodb+srv://clarkngo:YPvrRMUAgamd74n1@cluster0.rhkmsrr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const client = new MongoClient(connectionString);

let conn;
try {
  conn = await client.connect();
} catch(e) {
  console.error(e);
}

let db = conn.db("hos08");

export default db;

