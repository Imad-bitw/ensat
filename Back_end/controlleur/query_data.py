
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from controlleur.get_embedding_function import get_embedding_function
import time

CHROMA_PATH = "./chroma"

# Configurer Template Prompt
prompt_template= ChatPromptTemplate.from_messages(
    [
       # ("system", "Vous êtes un Smart Review qui évalué les articles scientifiques,votre spécialité de vérifier les références citées à partir de la base de données, et de citer les références existantes, non existantes. Votre nom est: {name}."),
       ( "system", "Vous êtes un assisstant  repondre des question ."),
        ("human", "Essayez de répondre en utilisant le contexte suivant :{context}"),
        ("human", "Répondez à la question suivante : {question}"),
    ]
)

#PROMPT_TEMPLATE = """
#Essayez de répondre en utilisant le contexte suivant :
#{context}
#Répondez à la question suivante : {question}
#"""




def query_rag(query_text: str):
    
    # Prepare the DB.
    print("\n **************** Début  de péreparation de base de données !'  ******************\n ")
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    print("\n **************** Fin  de péreparation de base de données !'  ******************\n\n ")

    # Search the DB.
    print(" **************** Début  D'opération 'Chercher dans la base de données (ChromaDB) !'  ******************\n ")
    results = db.similarity_search_with_score(query_text, k=5)
    if len(results) == 0:
        print("Désolé,La réponse de votre question n'existe pas dans la base de donées :( , essayer de poser une autre question!")
    print("**************** Fin  D'opération 'Chercher dans la base de données (ChromaDB) !'  ******************\n ")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    # Chargement de model LLM
    print("**************** Début de Chargement de modele ******************\n")
    model = Ollama(model="llama3", temperature=0)
    print("**************** Fin de Chargement de modele ******************\n")


    # Traitement des résultats 
    print(" **************** Traitement des résultats  ******************\n ")


    
    for word in model.stream(prompt):
        print(word,end="",flush=True)
        

 #   print(f" **************** Fin de traitement des résultats  ******************\n ")

  #  # Affichage des résultats 
   # print(" **************** Affichage des résultats  ******************\n ")
    #sources = [doc.metadata.get("id", None) for doc, _score in results]
    #formatted_response = f"Sources: {sources}"
    #print(  formatted_response)
    #print(" **************** Fin :) ******************\n ")
    



    