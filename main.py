from agents import PlannerAgent, ResearcherAgent, WriterAgent
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    console.print(Panel("✈️  Starting Gemini-Powered Travel Agent System...", style="bold blue"))
    
    # 1. Get User Input
    user_request = input("\nWhere would you like to go? (e.g., 'Plan a 3-day trip to Paris'): ")
    if not user_request:
        user_request = "Plan a 3-day trip to Paris"

    # 2. Initialize Agents
    planner = PlannerAgent(name="Alice", role="Planner")
    researcher = ResearcherAgent(name="Bob", role="Researcher")
    writer = WriterAgent(name="Charlie", role="Writer")

    # 3. Planning Phase
    with console.status("[bold green]Planner is thinking..."):
        plan = planner.plan(user_request)
    console.print(Panel(plan, title="📋 High-Level Plan", style="green"))

    # 4. Research Phase (Parsing the plan manually for the demo)
    # In a complex system, the LLM would parse its own output.
    research_summary = ""
    tasks = [line for line in plan.split('\n') if line.strip().startswith(('1.', '2.', '3.'))]
    
    for task in tasks:
        with console.status(f"[bold yellow]Researching: {task}..."):
            # Extract relevant keyword for the mock tool
            keyword = task.split(' ')[-1] # Simple heuristic for demo
            if "Paris" in user_request: keyword = "Paris" 
            elif "Tokyo" in user_request: keyword = "Tokyo"
            
            result = researcher.research(keyword)
            research_summary += f"\n- {task}: {result}"
            
    console.print(Panel(research_summary, title="🔍 Research Data", style="yellow"))

    # 5. Writing Phase
    with console.status("[bold magenta]Writer is compiling itinerary..."):
        final_itinerary = writer.write_itinerary(user_request, research_summary)
    
    console.print(Panel(final_itinerary, title="✨ Final Itinerary", style="bold magenta"))

if __name__ == "__main__":
    main()
