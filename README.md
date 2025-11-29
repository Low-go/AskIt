# AskIt

## Database Schema
```mermaid
erDiagram
    User ||--o{ Service : creates
    User ||--o{ ServiceProposal : submits
    User ||--o{ Message : sends
    Service ||--o{ ServiceProposal : "receives proposals"
    Service ||--o{ Message : "has chat messages"
    Service }o--|| User : "fulfilled by"

    User {
        int id PK
        string email
        string password_hash
        string name
        string location
        datetime created_at
    }

    Service {
        int id PK
        int requester_id FK
        int fulfiller_id FK "nullable"
        string title
        string description
        string location
        string status "pending/assigned/completed"
        datetime created_at
    }

    ServiceProposal {
        int id PK
        int service_id FK
        int responder_id FK
        string message
        datetime created_at
    }

    Message {
        int id PK
        int service_id FK
        int sender_id FK
        string content
        datetime created_at
    }
```

## How It Works

1. **User** creates a **Service** (request)
2. Other users submit **ServiceProposals** (single initial response)
3. Requester selects a responder → `fulfiller_id` gets set
4. **Messages** table activates for back-and-forth chat between requester and fulfiller