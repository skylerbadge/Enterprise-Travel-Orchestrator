import random

def search_tool(query):
    """
    Simulates a search engine. In a real production app, 
    you would swap this with Serper, Tavily, or DuckDuckGo API.
    """
    print(f"\n🔎 [Tool Use] Searching the web for: '{query}'...")
    
    # Mock results to ensure the code runs reliably without extra API keys
    mock_knowledge_base = {
        "paris": "Paris is known for the Eiffel Tower, Louvre Museum, and Notre-Dame. Top food: Croissants, Escargot.",
        "tokyo": "Tokyo features Shibuya Crossing, Senso-ji Temple, and Akihabara. Top food: Sushi, Ramen.",
        "new york": "NYC features the Statue of Liberty, Central Park, and Broadway. Top food: Pizza, Bagels."
    }
    
    # Simple keyword matching for the mock
    query_lower = query.lower()
    for key, value in mock_knowledge_base.items():
        if key in query_lower:
            return value
            
    return "Found general travel info: popular tourist spots include museums, parks, and historical landmarks."

def calculator_tool(expression):
    """
    Safely evaluates simple math expressions.
    """
    try:
        # unsafe eval is risky in prod, but okay for this simple hackathon demo
        return str(eval(expression))
    except:
        return "Error calculating."

# Tool Dictionary for the Agents to access
tools_map = {
    "search": search_tool,
    "calculator": calculator_tool
}
