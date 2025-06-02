🧪 SMILES Analyzer with CrewAI and Ollama

Este é um projeto de demonstração de um Analisador de SMILES utilizando a biblioteca CrewAI com o modelo Mistral rodando localmente via Ollama.

O objetivo do projeto é, a partir de uma entrada no formato SMILES, identificar a molécula representada, descrever suas aplicações e características, além de realizar análise computacional utilizando ferramentas como DeepChem.
🚀 Funcionalidades

    ✅ Identificação da molécula a partir de um SMILES.

    ✅ Geração de descritores moleculares e fingerprints.

    ✅ Pesquisa automática sobre aplicações e características da molécula.

    ✅ Armazenamento do relatório de análise em arquivo .txt.

    ✅ Execução com agentes e tarefas orquestradas via CrewAI.

    ✅ Integração com LLM local via Ollama.

🛠️ Tecnologias e Ferramentas

    Python 3.12+

    CrewAI

    Ollama

    Modelos LLM (mistral:7b via Ollama)

    DeepChem (emulada nas tasks)

    dotenv para variáveis de ambiente

⚙️ Instalação

    Clone este repositório:

git clone https://github.com/seu-usuario/smiles-analyzer.git
cd smiles-analyzer

    Crie um ambiente virtual e ative:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

    Instale as dependências:

pip install -r requirements.txt

    Configure o Ollama localmente e baixe o modelo mistral:7b:

ollama pull mistral

    Configure o arquivo .env (opcional):

touch .env

🏃‍♂️ Como executar

Execute o script principal:

python main.py

Digite o SMILES quando solicitado, por exemplo:

Qual smile você deseja analisar? CC(O)C

O resultado será exibido no terminal e salvo no arquivo smile.txt.
📝 Estrutura do Projeto

smiles-analyzer/
│
├── agents.py            # Definição dos agentes de análise
├── tasks.py             # Definição das tarefas com prompts dinâmicos
├── main.py              # Script principal de execução
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente
└── README.md            # Este arquivo

📂 Saída

O relatório gerado será salvo em:

smile.txt

Contendo:

    Nome comum e/ou IUPAC da molécula.

    Aplicações e usos conhecidos.

    Representação computacional (fingerprints).

    Observações importantes sobre toxicidade ou regulamentações.

❗ Observações importantes

    O projeto depende de uma instância funcional do Ollama local.

    O DeepChem está conceitualmente incluído, mas não implementado diretamente.

    O ScrapeElementFromWebsiteTool pode ser integrado para enriquecer ainda mais a busca automática de informações.

    Desative a telemetria do CrewAI configurando:

export CREWAI_DISABLE_TELEMETRY=1

ou via código (já configurado):

os.environ["CREWAI_DISABLE_TELEMETRY"] = "1"

🤝 Contribuições

Contribuições são bem-vindas!

    Fork este repositório.

    Crie sua feature branch (git checkout -b feature/sua-feature).

    Commit suas mudanças (git commit -m 'Adiciona nova feature').

    Push para o branch (git push origin feature/sua-feature).

    Abra um Pull Request.

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
💡 Inspiração

Este projeto é inspirado na necessidade de automatizar a análise e interpretação de representações químicas utilizando ferramentas de inteligência artificial.
📞 Contato

    Lucas Abner Caixeta de Oliveira

    LinkedIn: https://www.linkedin.com/in/lucas-abner-caixeta/
