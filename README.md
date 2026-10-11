# LLM-Scraper

I miei esercizi del corso **AI Engineer Core Track** (LLM Engineering di Ed Donner).

## Week 1

| Notebook | Cosa fa |
| --- | --- |
| [week1/day1.ipynb](week1/day1.ipynb) | Generatore di oggetti per email: incolli un'email e GPT propone 3 oggetti e un riassunto |
| [week1/day1_aviatrix.ipynb](week1/day1_aviatrix.ipynb) | Scarica la documentazione di [docs.aviatrix.com](https://docs.aviatrix.com/) e ne fa un riassunto strutturato, con un bonus su `llms.txt` |

## Come eseguirli

1. Installa le librerie: `pip install openai python-dotenv requests beautifulsoup4 ipython`
2. Crea un file `.env` nella cartella principale con la riga `OPENAI_API_KEY=sk-proj-...`
3. Apri il notebook ed esegui le celle dall'alto verso il basso.

Il file `.env` è escluso dal repository tramite `.gitignore`.
