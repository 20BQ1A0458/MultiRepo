# Use an official Node.js image as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only package.json and package-lock.json first for dependency installation
COPY package*.json ./

# Install dependencies, including TypeScript and any devDependencies needed for builds
RUN npm install

# Copy the entire application code to the working directory
COPY . .

# Build the TypeScript code into JavaScript
RUN npm run build

# Expose the application port
EXPOSE 8000

# Define the command to run the application
CMD ["node", "dist/index.js"]

