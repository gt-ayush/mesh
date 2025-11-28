# System Architecture

## Components

### 1. Django Backend
Handles:
- message routing
- encryption
- storing messages
- simple API endpoints (`/send/`, `/receive/`)

### 2. Mesh Logic (routing.py)
Implements:
- flood routing
- message queue
- encryption using timestamp-based XOR key

### 3. Communication Layer (comm.py)
Handles:
- local broadcast (UDP)
- inbox collection
- discovery of nearby nodes

### 4. Frontend (HTML/CSS/JS)
Displays:
- live chat feed
- connected nodes
- message status

---

## Data Flow Diagram

