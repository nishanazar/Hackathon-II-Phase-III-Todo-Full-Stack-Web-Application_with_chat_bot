# Hackathon II Phase III - Full-Stack Todo Web Application with AI Chatbot

A comprehensive full-stack todo application featuring Next.js frontend, FastAPI backend, and an intelligent AI chatbot for natural language task management. This application combines traditional task management with cutting-edge AI capabilities to provide an intuitive user experience.

## 🌟 Key Features

### Core Functionality
- **Full-stack web application** with Next.js 16+ frontend and FastAPI backend
- **User authentication and authorization** with JWT tokens
- **CRUD operations** for todo tasks with comprehensive validation
- **User isolation** - users can only access their own tasks
- **Responsive UI** with Tailwind CSS styling and dark mode support

### AI-Powered Assistant
- **Natural Language Processing** with Google's Gemini AI model
- **Intelligent Task Management** - create, update, complete, and delete tasks using conversational commands
- **Context-Aware Interactions** with conversation history persistence
- **Smart Task Recognition** that understands various command formats

### Advanced Capabilities
- **MCP (Model Context Protocol) Integration** for standardized tool interactions
- **Real-time Task Syncing** across all application views
- **Cross-Platform Compatibility** with responsive design
- **Secure Authentication** with Better Auth integration

## 🏗️ Architecture

The application follows a modern microservices architecture:

- `frontend/`: Next.js 16+ frontend with App Router, Tailwind CSS, and Better Auth
- `backend/`: FastAPI backend with SQLModel ORM, JWT authentication, and AI integration
- `specs/`: Specification files and project documentation
- `src/`: Source code for AI agents and core services
- `history/`: Historical records and project evolution

### Tech Stack
- **Frontend**: Next.js 16+, React, TypeScript, Tailwind CSS
- **Backend**: Python, FastAPI, SQLModel, Pydantic
- **Database**: PostgreSQL (with Neon compatibility)
- **Authentication**: Better Auth with JWT tokens
- **AI Services**: Google Gemini via OpenAI-compatible API
- **State Management**: Client-side with React hooks
- **Styling**: Tailwind CSS with custom components

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL database (or Neon for cloud deployment)
- Google Gemini API key

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/nishanazar/Hackathon-II-Phase-III-Todo-Full-Stack-Web-Application_with_chat_bot.git
   cd Hackathon-II-Phase-III-Todo-Full-Stack-Web-Application_with_chat_bot
   ```

2. **Setup Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Setup Frontend**:
   ```bash
   cd ../frontend
   npm install
   ```

4. **Configure Environment Variables**:

   Backend (.env):
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   BETTER_AUTH_SECRET=your_secret_key
   DATABASE_URL=postgresql://user:password@localhost:5432/todo_db
   ```

   Frontend (.env.local):
   ```env
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

5. **Terminal 1 - Start the backend**:
   ```bash
   cd ../backend
   uvicorn main:app --reload --port 8000
   ```

6. **Terminal 2 - Start the frontend**:
   ```bash
   cd ../frontend
   npm run dev
   ```

The frontend will be available at http://localhost:3000
The backend API will be available at http://localhost:8000

## 🤖 AI Chatbot Capabilities

The integrated AI assistant supports natural language commands:

- **Task Creation**: "Add a task to buy groceries" or "Create a task to call mom"
- **Task Listing**: "Show my tasks" or "What do I have to do?"
- **Task Completion**: "Complete the grocery task" or "Mark 'buy groceries' as done"
- **Task Updates**: "Update 'grocery' to 'buy organic groceries'" or "Change description of task X"
- **Task Deletion**: "Delete the meeting task" or "Remove 'schedule meeting'"

The AI agent intelligently parses these commands and executes the appropriate backend operations.

## 🔐 Security Features

- JWT-based authentication with secure token handling
- User isolation with strict access controls
- Input validation and sanitization
- Secure API communication with HTTPS enforcement
- Role-based access control

## 🧪 Testing

### Backend Testing
```bash
cd backend
pytest tests/ -v
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 📊 API Endpoints

### Task Management
- `GET /api/{user_id}/tasks` - List all tasks for the authenticated user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task completely
- `PATCH /api/{user_id}/tasks/{id}` - Partially update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task

### AI Chat Interface
- `POST /api/{user_id}/chat` - Natural language task management

### Health Check
- `GET /health` - Health check endpoint

## 🚢 Deployment

### Frontend (Vercel)
The frontend is optimized for deployment on Vercel with Next.js static generation capabilities.

### Backend (Hugging Face Spaces or Self-hosted)
The backend can be deployed on Hugging Face Spaces or any Python-compatible hosting platform.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## 🙏 Acknowledgments

- Built with Next.js and FastAPI for optimal developer experience
- Powered by Google's Gemini AI for intelligent task management
- Designed with accessibility and user experience in mind
- Developed using Spec-Driven Development methodology