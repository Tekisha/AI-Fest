# KODEST

KODEST is an innovative educational platform designed to assist students in solving programming tasks. Leveraging the Grazie API for intelligent hint generation and providing links to educational resources ensures students not only find solutions but understand the underlying concepts. The platform consists of a React-based frontend and a FastAPI-powered backend for efficient and scalable REST API communication.

## Features

- **Hint Generation**: Dynamically generates hints for programming problems without giving away the solution, encouraging learning and exploration.
- **Resource Linking**: Offers links to relevant educational resources, helping students delve deeper into programming concepts and algorithms.
- **Interactive Learning**: Through a user-friendly interface, students can input their solutions and receive immediate, constructive feedback.
- **FastAPI Backend**: Utilizes FastAPI to create RESTful endpoints, ensuring fast and reliable communication between the frontend and backend.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Node.js and npm (for the React frontend)
- Python 3.8 or higher (for the backend)
- Pip (Python package installer)

### Installing

#### Setting Up the Backend

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Tekisha/AI-Fest.git
    ```
2. Navigate to the backend directory:
    ```bash
    cd AI-Fest/backend
    ``` 

3. Create and activate a Python virtual environment:
    - **Unix/Linux/macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    - **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Install the required Python packages: 
    ```bash
    pip install -r requirements.txt
    ```

5. Set the `GRAZIE_JWT_TOKEN` environment variable to your Grazie API token:

    - **Unix/Linux/macOS:**
    ```bash
    export GRAZIE_JWT_TOKEN=your_grazie_api_token
    ```
    - **Windows:**
    ```bash
    set GRAZIE_JWT_TOKEN=your_grazie_api_token
    ```
   
6. Run the backend server:

   ```bash 
   uvicorn main:app --reload
    ```

The backend will be available at `http://localhost:8000`.

#### Setting Up the Frontend

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install npm packages:

   ```bash
    npm install
   ```

3. Start the React development server:

   ```bash
    npm start
   ```


The frontend will be available at `http://localhost:3000`.

## Usage

KODEST provides an interactive platform to help students learn programming through problem-solving. Here's how to get started:

1. **Accessing the Platform**: Navigate to `http://localhost:3000` in your web browser to access the KODEST frontend interface.

2. **Submitting Tasks**:
   - Find the problem you wish to solve from the list provided or by searching for a specific problem name.
   - Enter your solution in the code editor provided for the problem.
   - Click the "Submit" button to submit your solution for evaluation.

3. **Receiving Hints**:
   - Once your solution is submitted, KODEST will analyze your code.
   - If your solution is incorrect or could be improved, KODEST will provide hints to guide you. These hints aim to help you understand the problem better and encourage you to find the solution independently.
   - Review the hints and try to revise your solution based on the guidance provided.

4. **Learning Resources**:
   - For additional learning, KODEST may provide links to relevant educational resources that explain the concepts tested by the problem in more detail.

Remember, KODEST is designed to enhance your learning experience by providing constructive feedback. It encourages practice, exploration, and learning from mistakes.

## Contributors

KODEST Team:

- **Momir Milutinović**
  - GitHub: [@MomirMilutinovic](https://github.com/MomirMilutinovic)

- **Vladimir Popov**
  - GitHub: [@twet123](https://github.com/twet123)

- **Balša Bulatović**
  - GitHub: [@BulatovicBalsa](https://github.com/BulatovicBalsa)

- **Teodor Vidaković**
  - GitHub: [@Tekisha](https://github.com/Tekisha)

We welcome contributions from the community, whether it's in the form of bug reports, enhancements, documentation, or new features.







