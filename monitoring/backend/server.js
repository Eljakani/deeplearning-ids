const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const { MongoClient } = require('mongodb');

const app = express();
const server = http.createServer(app);
const io = new Server(server);


//client = MongoClient('mongodb://localhost:27017/')
//db = client['deeplearning_db']
//collection = db['valid_packets']

const MONGODB_URI = "mongodb://localhost:27017/";
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

io.on('connection', (socket) => {
  console.log('New client connected');

  // Simulate real-time data updates
  setInterval(async () => {
    const data = await db.collection('valid_packets').findOne({}, { sort: { $natural: -1 } });

    if (data) {
      socket.emit('data', data);
    }
  }, 5000); // Update every 5 seconds

  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});