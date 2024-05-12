const express = require('express');
const http = require('http');
const { MongoClient } = require('mongodb');
const cors = require('cors'); 

const app = express();
const server = http.createServer(app);

// Middleware to allow CORS
app.use(cors());

// MongoDB configuration
// get the MONGODB_URI environment variables set by the docker-compose file
const MONGODB_URI = process.env.MONGODB_URI;
const MONGODB_DB = "deeplearning_db";

if (!MONGODB_URI) {
  throw new Error('Please define the MONGODB_URI environment variable');
}

if (!MONGODB_DB) {
  throw new Error('Please define the MONGODB_DB environment variable');
}

let db;

const connectToDatabase = async () => {
  const client = await MongoClient.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  db = client.db(MONGODB_DB);
};

connectToDatabase();


// Route handler for anomalies retrieval via http
app.get('/overview', async (req, res) => {
  const anomalies = await db.collection('anomaly').find({}).toArray();
  const all_packets = await db.collection('valid_packets').find({}).toArray();
  res.json({ anomalies: anomalies.length, all_packets: all_packets.length, latest_anomalies: anomalies.slice(-5) });
});
app.get('/anomaly/:id', async (req, res) => {
  const anomaly = await db.collection('anomaly').findOne({ _id: req.params.id });
  res.json(anomaly);
});


const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
