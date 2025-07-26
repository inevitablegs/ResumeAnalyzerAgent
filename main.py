import os
from dotenv import load_dotenv
from typing import TypedDict, Optional
from langgraph.graph import StateGraph
from tools.pdf_extractor import extract_text_from_pdf
from tools.analyzer import analyze_resume
from tools.improver import improve_resume

load_dotenv()

# Define agent state using TypedDict
class ResumeAgentState(TypedDict):
    file_path: str
    extracted_text: Optional[str]
    analysis: Optional[str]
    improvement: Optional[str]

# === Node 1: Extract Resume Text ===
def extract_node(state: dict) -> dict:
    text = extract_text_from_pdf(state["file_path"])
    return {
        **state,
        "extracted_text": text
    }

# === Node 2: Analyze Resume ===
def analyze_node(state: dict) -> dict:
    analysis = analyze_resume(state["extracted_text"])
    return {
        **state,
        "analysis": analysis
    }

# === Node 3: Improve Resume ===
def improve_node(state: dict) -> dict:
    improvement = improve_resume(state["extracted_text"])
    return {
        **state,
        "improvement": improvement
    }

# === Build LangGraph Agent ===
graph = StateGraph(state_schema=ResumeAgentState)
graph.add_node("extract", extract_node)
graph.add_node("analyze", analyze_node)
graph.add_node("improve", improve_node)

# Define flow between nodes
graph.set_entry_point("extract")
graph.add_edge("extract", "analyze")
graph.add_edge("analyze", "improve")

# Compile the agent
app = graph.compile()

# === Run the Agent ===
if __name__ == "__main__":
    file_path = "REsume.pdf"  # Replace with your actual PDF path

    final_state = app.invoke({"file_path": file_path})

    print("\n=== Extracted Text ===\n")
    print(final_state["extracted_text"][:800])  # Preview first 800 chars

    print("\n=== Analysis ===\n")
    print(final_state["analysis"])

    print("\n=== Improved Resume ===\n")
    print(final_state["improvement"])
