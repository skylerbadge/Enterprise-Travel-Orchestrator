# Enterprise Travel Orchestrator: Autonomous Corporate Travel Management

## 1. The Problem
Corporate travel planning is a significant productivity drain. Research indicates the average person spends nearly **18 hours** researching and booking a single trip. In the enterprise sector, this friction is compounded by compliance issues: **45% of travel buyers** identify budget uncertainty as a primary challenge, and **63%** cite manual expense reporting as a critical inefficiency. Furthermore, 80% of organizations report a disconnect between their meeting schedules and travel booking tools, leading to non-compliant "bleisure" bookings that cost companies millions.

## 2. The Solution
The **Enterprise Travel Orchestrator** is an autonomous multi-agent system designed to solve this specific gridlock. It moves beyond simple "chat" to execute a complex business process: planning a compliant itinerary that balances employee preferences with strict corporate policy. By treating "Policy" as a distinct agent rather than a prompt constraint, the system ensures that no itinerary is presented to the user unless it passes a rigorous pre-audit.

## 3. Core Architecture
The system is built on the **Google Gen AI SDK** and **LangGraph**, utilizing a **Supervisor-Worker** topology to separate reasoning from action.

*   **The Supervisor (Orchestrator):** Acts as the "Prefrontal Cortex." It interprets high-level user intent (e.g., "Plan a trip to London for the Q3 summit") and delegates tasks to specialized workers. It manages the conversation state and persists memory across sessions.
*   **The Researcher (Worker):** Powered by **Google Search Grounding**, this agent retrieves real-time flight prices, hotel availability, and weather data, eliminating the "knowledge cutoff" limitations of standard LLMs.
*   **The Analyst (Worker):** Solves the "LLM Math" problem. Using **Code Execution (Python REPL)**, this agent writes and runs Python scripts to calculate total trip costs, convert currency (e.g., GBP to USD), and estimate VAT, ensuring 100% arithmetic accuracy.
*   **The Auditor (Worker):** A specialized agent that strictly enforces corporate rules (e.g., "No business class on flights under 6 hours"). It acts as a gatekeeper, rejecting non-compliant options before the user ever sees them.

## 4. Technical Implementation & Tools
*   **Model:** Gemini 2.0 Flash for low-latency tool use; Gemini 2.5 Pro for complex reasoning.
*   **Orchestration:** LangGraph StateGraph for cyclic multi-agent workflows.
*   **Tooling:** Google Search (Grounding) and Local Python Execution Sandbox.
*   **Memory:** LangGraph Checkpointing for long-running, persistent sessions.

## 5. Value Statement
By automating the "Search-Audit-Calculate" loop, the Enterprise Travel Orchestrator reduces the active time required to book a compliant business trip from hours to minutes. It directly addresses the "budget uncertainty" pain point cited by 45% of travel managers by providing mathematically verified cost estimates and pre-enforcing policy compliance.

## 🤖 Agentic Architecture
The system utilizes a **Hierarchical Agent Workflow**:
1.  **Planner Agent (Orchestrator):** Analyzes the user's request and breaks it down into research tasks.
2.  **Researcher Agent:** "Searches" for attractions, flights, and hotels (simulated tool use).
3.  **Writer Agent:** Compiles the gathered information into a formatted Markdown itinerary.

## 🛠️ Tools Used
* **DuckDuckGo Search (Simulated):** For finding real-time attraction data.
* **Calculator:** For budget estimation.
* **Gemini API:** For reasoning and content generation.

## 🚀 How to Run
1.  Clone this repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Set your `GEMINI_API_KEY` in `config.py` (or use environment variables).
4.  Run the planner: `python main.py`
