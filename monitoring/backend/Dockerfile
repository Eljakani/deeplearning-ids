# Use Node.js image as base
FROM node:lts

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to work directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the backend server
CMD ["node", "server.js"]
