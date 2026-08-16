"""Print the LangGraph workflow as Mermaid text for development and learning."""

from mavenier.rag.graph.agentic_rag_graph import graph

if __name__ == "__main__":
    print(graph.get_graph().draw_mermaid())
