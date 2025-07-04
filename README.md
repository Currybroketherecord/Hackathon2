
## 🚀 FlexMatch – The AI Freelance Assistant

**FlexMatch** is an AI-powered platform that helps freelancers find ideal gigs, receive real-time coaching, and manage their workflow—all with a single profile submission.

Built during vibecoding hackathon to empower the gig economy with smart, personalized assistance.

---

### 🧠 Features

- 🎯 **AI-Powered Gig Matching**  
  Get freelance opportunities tailored to your skills and goals using OpenAI.

- 💡 **Micro-Coaching Engine**  
  Get personalized productivity or growth tips based on your career goals.

- 📋 **Simple Profile Intake**  
  Just enter your name, skills, and goals—FlexMatch does the rest.

- 🌐 **Full-Stack Application**  
  React frontend + Node.js backend + MongoDB database.

---

### 🛠 Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Frontend     | React (Vite), Axios    |
| Backend      | Node.js, Express       |
| AI           | OpenAI GPT-3.5 API     |
| Database     | MongoDB (Local or Atlas) |
| Auth (Future)| Firebase (planned)     |

---

### 📦 Installation

#### 1. **Clone the repository**
```bash
git clone https://github.com/yourname/flexmatch.git
cd flexmatch
```

#### 2. **Backend setup**
```bash
cd backend
npm install
```
Create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=mongodb://localhost:27017/flexmatch
```
Start the backend:
```bash
node server.js
```

#### 3. **Frontend setup**
```bash
cd ../frontend
npm install
npm run dev
```

App runs at: `http://localhost:5173`

---

### 🧪 Usage

1. Go to the app in your browser.
2. Enter your name, skills, and goals.
3. Hit “Submit” to see:
   - 💼 3 Smart gig suggestions
   - 🧠 A coaching tip just for you
4. Backend logs your profile and uses GPT to generate results.

---

### 📈 Roadmap

- 🔐 Firebase Auth (Multi-user dashboards)
- 📄 Smart Contract Generator
- 📅 Project Milestone Tracker
- 📎 Resume Upload + Parsing

---

### 👥 Contributors

- **Micky Maina** – Full-stack dev, AI architect  


