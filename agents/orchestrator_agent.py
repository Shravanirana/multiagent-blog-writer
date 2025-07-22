from agents.research_agent import ResearchAgent
from agents.writing_agent import WritingAgent
from agents.review_agent import ReviewAgent

class OrchestratorAgent:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()
        self.review_agent = ReviewAgent()

    def generate_blog(self, topic):
        research = self.research_agent.fetch_research(topic)
        draft = self.writing_agent.write_article(research)
        reviewed = self.review_agent.review_content(draft)
        return reviewed
