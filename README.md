# PasaBuy

Welcome to **PasaBuy** - the Expo Go community-centered application designed to allow people to make requests in their community, connect or fulfill requests, and help those around them.

## Tech Stack

- **Frontend**: React Native with Expo Go
- **Backend**: Django/Python
- **Database**: PostgreSQL

## Getting Started

### Prerequisites

- Node.js and npm installed
- Docker and Docker Compose installed
- VS Code (recommended)
- Git

### Installation

1. **Clone the repository**
```bash
   git clone <repository-url>
   cd askit
```

2. **Install frontend dependencies** (first time only)
```bash
   cd frontend
   npm install
   cd ..
```

### Running the Development Environment

The backend and database are fully dockerized for easy setup. To run this project in development you will also need docker desktop installed. We've configured VS Code tasks to start everything with a single command.

**To start the entire development environment:**

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Select **Tasks: Run Task**
3. Choose **"start dev environment"**

This will automatically:
- Open two terminal windows
- Start the frontend server (with logs in terminal 1)
- Start the backend and database services via Docker (with logs in terminal 2)

## Documentation

For information on the database schema, [click here](backend/README.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Licensew

[Add your license information here]