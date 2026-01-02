import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerplyWebSearchTool,
	ScrapeWebsiteTool,
	ArxivPaperTool
)


from crewai_tools import CrewaiEnterpriseTools



@CrewBase
class AdvancedAiEnhancedResearchAutomationCrew:
    """AdvancedAiEnhancedResearchAutomation crew"""

    
    @agent
    def research_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["research_specialist"],
            
            
            tools=[
				SerplyWebSearchTool(),
				ScrapeWebsiteTool(),
				ArxivPaperTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def data_analyst(self) -> Agent:

        
        return Agent(
            config=self.agents_config["data_analyst"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def report_writer(self) -> Agent:
        enterprise_actions_tool = CrewaiEnterpriseTools(
            actions_list=[
                
                "microsoft_word_create_text_document",
                
                "microsoft_onedrive_upload_file",
                
            ],
        )

        
        return Agent(
            config=self.agents_config["report_writer"],
            
            
            tools=[
				*enterprise_actions_tool
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def email_distribution_specialist(self) -> Agent:
        enterprise_actions_tool = CrewaiEnterpriseTools(
            actions_list=[
                
                "microsoft_outlook_send_email",
                
                "microsoft_word_get_document_content",
                
            ],
        )

        
        return Agent(
            config=self.agents_config["email_distribution_specialist"],
            
            
            tools=[
				*enterprise_actions_tool
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def research_coordinator(self) -> Agent:

        
        return Agent(
            config=self.agents_config["research_coordinator"],
            
            
            tools=[
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def fact_verification_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["fact_verification_specialist"],
            
            
            tools=[
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def content_optimizer(self) -> Agent:

        
        return Agent(
            config=self.agents_config["content_optimizer"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def strategic_research_planning(self) -> Task:
        return Task(
            config=self.tasks_config["strategic_research_planning"],
            markdown=False,
            
            
        )
    
    @task
    def conduct_targeted_research(self) -> Task:
        return Task(
            config=self.tasks_config["conduct_targeted_research"],
            markdown=False,
            
            
        )
    
    @task
    def intelligent_fact_verification(self) -> Task:
        return Task(
            config=self.tasks_config["intelligent_fact_verification"],
            markdown=False,
            
            
        )
    
    @task
    def analyze_and_synthesize_findings(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_and_synthesize_findings"],
            markdown=False,
            
            
        )
    
    @task
    def generate_structured_report(self) -> Task:
        return Task(
            config=self.tasks_config["generate_structured_report"],
            markdown=False,
            
            
        )
    
    @task
    def advanced_content_optimization(self) -> Task:
        return Task(
            config=self.tasks_config["advanced_content_optimization"],
            markdown=False,
            
            
        )
    
    @task
    def email_report_distribution(self) -> Task:
        return Task(
            config=self.tasks_config["email_report_distribution"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AdvancedAiEnhancedResearchAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
