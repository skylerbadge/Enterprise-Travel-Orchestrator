import google.generativeai as genai
from config import GOOGLE_API_KEY
from tools import tools_map

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

class Agent:
    def __init__(self, name, role, model_name="gemini-1.5-flash"):
        self.name = name
        self.role = role
        self.model = genai.GenerativeModel(model_name)
    
    def generate(self, prompt):
        """
        Sends a prompt to Gemini and returns the text response.
        """
        response = self.model.generate_content(prompt)
        return response.text

class PlannerAgent(Agent):
    def plan(self, user_request):
        prompt = f"""
        You are a Senior Travel Planner.
        User Request: "{user_request}"
        
        Your goal is to create a high-level plan.
        1. Identify the destination and duration.
        2. Create a list of 3 specific questions or topics a Researcher needs to find out to plan this trip (e.g., top landmarks, local food, weather).
        
        Output strictly in this format:
        Destination: [Destination]
        Duration: [Number] days
        Research Tasks:
        1. [Task 1]
        2. [Task 2]
        3. [Task 3]
        """
        return self.generate(prompt)

class ResearcherAgent(Agent):
    def research(self, query):
        # The agent "decides" to use a tool (simulated here for simplicity)
        tool_result = tools_map["search"](query)
        
        prompt = f"""
        You are a Travel Researcher.
        You looked up: "{query}"
        The search tool returned: "{tool_result}"
        
        Summarize this information into one concise paragraph useful for a tourist.
        """
        return self.generate(prompt)

class WriterAgent(Agent):
    def write_itinerary(self, request, research_data):
        prompt = f"""
        You are a Travel Content Writer.
        Original Request: "{request}"
        Research Data gathered:
        {research_data}
        
        Create a fun, engaging day-by-day itinerary based on the data.
        Use Emojis. Format clearly with Markdown.
        """
        return self.generate(prompt)
