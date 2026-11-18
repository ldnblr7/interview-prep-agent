\#Interview Prep Coach



An interview-prep agent built with Python and the OpenAI Agents SDK using command-line arguments. 



\## Functions



\- Answers interview-prep questions.

\- Searches 'notes.txt' when asked about the notes.

\- Saves practice questions to 'practice\_questions.txt' only after the user confirms.



\## Tool



\- 'search\_notes(query)': searches the local notes.txt using keyword matching. 

\- 'add\_practice\_question(question)': appends the question to practice\_questions.txt after receiving confirmation.



\## Run it



1. Create a Python virtual environment.
2. Install the dependency with 'python -m pip install openai-agents'.
3. Set 'OPEN\_API\_KEY' in PowerShell session.
4. Run 'python main.py'



\## Limitations



\- Note search uses simple keyword matching, not semantic search. 

\- The program handles a single prompt each time it runs.

\- No conversation history other than questions saved.

