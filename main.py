import asyncio
from pathlib import Path
from agents import Agent, Runner, function_tool

BASE_DIR = Path(__file__).parent

@function_tool
def search_notes(query: str) -> str:
    """Search the local notes file for information relevant to a query."""
    notes_path = BASE_DIR / "notes.txt"

    if not notes_path.exists():
        return "The notes file was not found."

    lines = notes_path.read_text(encoding="utf-8").splitlines()
    ignored_words = {"what", "do", "my", "the", "say", "about", "is", "are", "a", "an", "in", "to"}
    keywords = [
        word.strip(".,?!:;").lower()
        for word in query.split()
        if word.strip(".,?!:;").lower() not in ignored_words
    ]

    matches = [
        line for line in lines
        if any(keyword in line.lower() for keyword in keywords)
    ]

    if not matches:
        return "No relevant information was found in the notes."

    return "\n".join(matches)


@function_tool
def add_practice_question(question: str) -> str:
    """Ask the user to confirm before saving a practice question."""
    print(f"\nThe agent wants to save this question:\n{question}")
    confirmation = input("Save it? Type y to confirm: ")

    if confirmation.strip().lower() != "y":
        return "The user declined. The question was not saved."

    questions_path = BASE_DIR / "practice_questions.txt"
    with questions_path.open("a", encoding="utf-8") as file:
        file.write(question.strip() + "\n")

    return "The practice question was saved."


agent = Agent(
    name="Interview Prep Coach",
    instructions=(
        "Help the user prepare for an Agentic AI interview. "
        "When asked what the notes say, use the search_notes tool. "
        "If the notes do not contain the answer, say so. "
        "Only use add_practice_question when the user explicitly asks to save a question. "
        "Do not say a question was saved unless the tool confirms it."
    ),
    model="gpt-6-luna",
    tools=[search_notes, add_practice_question],
)


async def main():
    question = input("Ask an interview-prep question: ")
    result = await Runner.run(agent, question)
    print("\n" + result.final_output)


if __name__ == "__main__":
    asyncio.run(main())