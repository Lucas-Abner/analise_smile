from crewai import Crew, Process, LLM
from agents import SmilesAnalysisAgents
from tasks import SmilesAnalysisTasks
from dotenv import load_dotenv
import os
load_dotenv()

os.environ.pop("OPENAI_API_KEY", None)

os.environ["CREWAI_LLM_PROVIDER"] = "ollama"
os.environ["CREWAI_EMBEDDINGS_PROVIDER"] = 'ollama'
os.environ["CREWAI_DISABLE_TELEMETRY"] = "1"
os.environ["CHROMA_OPENAI_API_KEY"] = "dummy_key"


class SmileCrew:

    def __init__(self, smile):
        self.llm = LLM(
            model="ollama/llama3.2:latest",
            base_url="http://localhost:11434",
            api_key="dummy_key",
            stream=False,
            timeout=120
        )

        self.smile = smile

    def run(self):
        agents = SmilesAnalysisAgents()
        tasks = SmilesAnalysisTasks()

        agent_bioinfo = agents.especialista_bioinfo()  # <- instância
        agent_analise = agents.analista_smiles()
        task_smile = tasks.analise_smiles(self.smile)     # <- idem, se for classe de métodos de instância
        task_deep = tasks.usando_deepchem(self.smile)

        crew = Crew(
            agents=[agent_bioinfo, agent_analise],
            tasks=[task_deep, task_smile],
            verbose=True,
            process=Process.sequential,
            memory=True,
            output_file="smile.txt",
            llm=self.llm
        )

        result = crew.kickoff()
        return result

if __name__=="__main__":
    print("## Bem vindo ao Analisador de Smiles")
    print("---------------------------------------------")
    smile =input("Qual smile você deseja analisar?")
    
    smile_crew = SmileCrew(smile)
    result = smile_crew.run()
    print("\n\n####################")
    print("## Vamos te reportar")
    print('########################\n')
    print(result)