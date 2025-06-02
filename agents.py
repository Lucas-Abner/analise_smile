import pandas as pd
import os
from crewai import Agent, LLM
from tools.DeepchemTool import DeepchemTool 
from crewai_tools import ScrapeElementFromWebsiteTool

os.environ.pop("OPENAI_API_KEY", None)

os.environ["CREWAI_LLM_PROVIDER"] = "ollama"
os.environ["CREWAI_EMBEDDINGS_PROVIDER"] = 'ollama'
os.environ["CREWAI_DISABLE_TELEMETRY"] = "1"

class SmilesAnalysisAgents:
    def __init__(self):
        self.llm = LLM(
            model="ollama/mistral:7b",
            base_url="http://localhost:11434",
            api_key="dummy",
            stream=False
        )

    def especialista_bioinfo(self):
        return Agent(
            role="O melhor especialista em biologia computacional.",
            goal="Focado em encontrar os melhores formatos de ligantes para futuros farmacos da industria.",
            backstory="""
            Um especialista em assenção na área de biologia computacional e usando a ferramenta de deep learning DeepChem com especialidade, 
            com mais de 15 anos fazendo docking e gerando ligantes a base de SMILES para achar ligantes perfeitos para proteinas perigosas.
            """,
            llm=self.llm,
            memory=True,
            verbose=True,
            tools=[DeepchemTool()],
            allow_delegation=True
        )

    def analista_smiles(self):
        scrape_tool = ScrapeElementFromWebsiteTool(
            url="https://pubchem.ncbi.nlm.nih.gov/",
            element_selectors=["p", "h1"]  # por exemplo, pegar os parágrafos e títulos principais
        )

        return Agent(
            role="Analista de estrutura molecular SMILES",
            goal="Focado em analisar uma estrutura SMILES e passar essa estrutura para a ferramenta deepchem",
            backstory="""
            Ajudando seu superior, esse analisat ajuda a analisar estruturas de SMILES em formato string e transforma atraves do deepchem para assim obter o resultado desse ligante.
            Pesquisando na web sobre qual modécula representa aquela estrutura SMILES.
            """,
            tools=[DeepchemTool(), scrape_tool],
            verbose=True,
            allow_delegation=False,
            memory=True,
            llm=self.llm
        )