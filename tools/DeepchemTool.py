from crewai.tools import BaseTool
import deepchem as dc
from deepchem.feat import CircularFingerprint

class DeepchemTool(BaseTool):
    name: str = "FeaturizerSMILES"
    description: str = "Recebe uma string SMILES e retorna o fingerprint de 1024 bits"
    
    def _run(self, smile: str) -> list:
        featurizer = CircularFingerprint(size=1024)
        features = featurizer.featurize([smile])
        return features.tolist()
