import express from "express";
import db from "../db/conn.mjs";
import bcrypt from "bcrypt";
import { signToken } from "../auth.mjs";

const router = express.Router();

// Register a new user
router.post("/", async (req, res) => {
  const { username, email, password } = req.body;

  if (!username || !email || !password) {
    return res.status(400).json({ message: "You must provide a username, email, and password." });
  }

  const hashedPassword = await bcrypt.hash(password, 10);

  const newUser = {
    username,
    email,
    password: hashedPassword,
  };

  const collection = await db.collection("users");
  const result = await collection.insertOne(newUser);

  const token = signToken(newUser);

  res.json({ token, result });
});

// Login a user
router.post("/login", async (req, res) => {
  const { email, password } = req.body;

  const collection = await db.collection("users");
  const user = await collection.findOne({ email });

  if (!user) {
    return res.status(400).json({ message: "Can't find this user" });
  }

  const correctPw = await bcrypt.compare(password, user.password);

  if (!correctPw) {
    return res.status(400).json({ message: "Wrong password!" });
  }

  const token = signToken(user);

  res.json({ token, user });
});

export default router;
