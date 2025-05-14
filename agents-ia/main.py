from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the agent with an LLM via Groq and DuckDuckGoTools
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="Voce é o melhor em automatizar criacao de relatorios com IA do mundo!",
    tools=[DuckDuckGoTools()],      # Add DuckDuckGo tool to search the web
    show_tool_calls=True,           # Shows tool calls in the response, set to False to hide
    markdown=True                   # Format responses in markdown
)

# Prompt the agent to fetch a breaking news story from New York
agent.print_response("como posso criar um fluxo usando a IA groqcloud para automatizar a documentacao dos relatorios de power bi?(resuma)", stream=True)