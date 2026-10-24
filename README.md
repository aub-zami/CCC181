# UniQueue
A queue management application designed for students (mostly freshmen) at MSU-IIT to manage P.E. uniform sizing, payment, and distribution efficiently.

## How to run UniQueue
 ### 1. Create and activate a virtual environment:
   ```bash
      python -m venv .venv
      .venv\Scripts\activate   # Windows
      # source .venv/bin/activate  # macOS/Linux
   ```

### 2. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```

#### 3. Start flask application: 
   ```bash
   flask --app app run --debug
   ```