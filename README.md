# SelectCode LLM-App

Dieses Repository enthält das Grundgerüst einer LLM-Chat-Anwendung basierend auf [Chainlit](https://github.com/Chainlit/chainlit).
Deine Aufgabe ist es, innerhalb der gegebenen Zeit die coolste Anwendung zu bauen.

## Colab
Falls du lokal keine Python-Installation hast, kannst du das [hier](https://colab.research.google.com/drive/1lTHXzEa7o7hPqyUXvYVkyADaV1AR4zg8?usp=sharing) hinterlegte Notebook nutzen.

## Installieren

Bevor du mit der Installation beginnst, stelle bitte sicher, dass du entweder [venv](https://docs.python.org/3/library/venv.html) oder [Conda](https://docs.python.org/3/library/venv.html) auf deinem System installiert hast.


### Mit venv

Folge diesen Schritten, um ein virtuelles Environment mit venv zu erstellen und zu aktivieren:

```bash
# Navigiere in das Repository
cd ./llm-example

# Erstelle ein virtuelles Environment
python3 -m venv env

# Aktiviere das virtuelle Environment
# Für Windows
env\Scripts\activate

# Für Unix oder MacOS
source env/bin/activate
```

Danach installiere die Abhängigkeiten aus der `requirements.txt` Datei:

```bash
pip install -r requirements.txt
```

### Mit conda

Folge diesen Schritten, um ein virtuelles Environment mit Conda zu erstellen und zu aktivieren:

```bash
# Navigiere in das Repository
cd ./llm-example

# Erstelle ein Conda Environment
conda create --name env

# Aktiviere das Environment
conda activate env
```

Danach installiere die Abhängigkeiten aus der `requirements.txt` Datei:

```bash
pip install -r requirements.txt
```

## API Key hinterlegen
In `.env`, hinterlege den API Schlüssel, den du von uns erhalten hast. Du möchtest nach dem Workshop weiterbauen?
Du kannst dir mit sehr wenig Aufwand bei [OpenAI](platform.openai.com/) deinen eigenen Schlüssel holen.

## Starten

Nach der Installation der Abhängigkeiten kannst du die Anwendung mit folgendem Befehl starten:

```bash
chainlit run app.py -w
```

## Loslegen!
Jetzt kannst du loslegen indem du verschiedene Langchain Komponenten in deine Anwendung integrierst - schau dir `app.py` an!
In `utils.py` haben wir einige nützliche Methoden hinterlegt.

Du suchst Inspiration? Schau in der [Chainlit Dokumentation](https://docs.chainlit.io/integrations/langchain) oder der [LangChain Übersicht an beliebten Chains](https://python.langchain.com/docs/modules/chains/popular/) vorbei.
Ebenfalls nützlich: Das [Chainlit Cookbook](https://github.com/Chainlit/cookbook/).
Spannende Beispiele mit offenen APIs findest du z.B. in der [Übersicht der Langchain API Chains](https://python.langchain.com/docs/modules/chains/popular/api).

Du fühlst dich eingeschränkt? Mit [Streamlit](https://streamlit.io/) kannst du mit ein wenig mehr Komplexität noch kreativer werden!
