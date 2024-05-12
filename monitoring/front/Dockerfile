# Use Node.js image as base for the builder stage
FROM node:lts AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to work directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Debugging: Print out the list of files in the working directory
RUN ls -la

# Copy the rest of the application
COPY . .

# Debugging: Print out the list of files after copying
RUN ls -la

# Build the React app
RUN npm run build

# Debugging: Print out the list of files after build
RUN ls -la /app/

# Use Nginx as base image for serving the application
FROM nginx:alpine

# Remove default Nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy build files from the builder stage to Nginx server directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
