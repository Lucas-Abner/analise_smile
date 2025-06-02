from crewai import Task
from agents import SmilesAnalysisAgents

class SmilesAnalysisTasks:
    def usando_deepchem(self, smile:str):

        agent_bioinfo = SmilesAnalysisAgents()
        return Task(
            description=(
        f"Dado um SMILES {smile}, identifique qual molécula ele representa. Informe o nome da molécula (nome comum ou IUPAC) "
        "e descreva, de forma clara e objetiva, para que essa substância é usualmente utilizada, ou se não possui aplicações conhecidas. "
        "Caso haja múltiplos usos, liste-os. Se a substância for tóxica, perigosa ou regulamentada, aponte esses aspectos também. "
        "Utilize suas ferramentas computacionais e sua vasta experiência em biologia computacional e química para garantir uma resposta precisa."
        ),
            expected_output=(
                "1. Nome da molécula (comum e/ou IUPAC).\n"
                "2. Aplicações ou usos conhecidos.\n"
                "3. Observações relevantes (toxicidade, regulamentações, etc.)."
            ),
            agent= agent_bioinfo.especialista_bioinfo()
        )
    
    def analise_smiles(self, smile:str):

        agent_analista = SmilesAnalysisAgents()
        return Task(
            description=(
                f"Receba uma estrutura molecular {smile}. Analise essa estrutura utilizando a ferramenta DeepChem "
                "para transformá-la em uma representação computacional apropriada, como fingerprints ou descritores moleculares. "
                "Em seguida, pesquise na web para identificar qual molécula corresponde a essa estrutura, encontrando seu nome, principais características "
                "e potenciais aplicações. Apresente os resultados de forma clara e estruturada."
            ),
            expected_output=(
                "1. Representação computacional da molécula (fingerprints, descritores ou vetores).\n"
                "2. Nome da molécula identificado via pesquisa.\n"
                "3. Aplicações ou características relevantes encontradas.\n"
                "4. Links ou referências das fontes consultadas."
            ),
            agent=agent_analista.analista_smiles()
        )