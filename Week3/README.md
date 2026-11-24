
In Week 3, I implemented an LLM monitoring system using MongoDB to track the performance and usage of different language models. The application records token consumption, response time and estimated API costs for both Gemini and Ollama.

Steps I followed:

1. Created a Week 3 project folder in VS Code with the required Python files.
2. Installed the necessary libraries, including Google GenAI, Requests, PyMongo and python-dotenv.
3. Generated a Gemini API key and configured a MongoDB Atlas database.
4. Stored the API key and MongoDB connection URL in the `.env` file.
5. Created a usage logger to save LLM request details in MongoDB.
6. Updated the common LLM client to track input tokens, output tokens and response latency.
7. Implemented API cost estimation for Gemini and usage tracking for Ollama.
8. Added timeout and retry mechanisms to handle temporary errors.
9. Created unit tests to verify the client and logging functionality.
10. Executed the application and checked the stored usage records in MongoDB.

Commands used:

pip install -r requirements.txt

python -m unittest test_client.py

python main.py

ollama pull llama3.2

ollama run llama3.2
