# DocuMind
this is a rag pdf reader which user can use it for answering query
Here I have used :
1. Python 3.11.9 as Using groq is not compatible to newer versions
2. Langchain for binding up the whole RAG (Retrival-Augumented-generation)
3. I have used the Groq ai for answering the query related to the context
4. Used vectordb faiss for vectorstore
5. Also used llama-3b-instant under groq ai cloud
6. Huggingface is also being used for embeddings

since this DocuMind is not only can be used for solving question from pdf 
or to sumarize pdf, it can be used as an conssultant like user uploads the whole constitution 
it uses context and can be used as a legal consultant , huh no it can't generate formats 
for writting Notary , but it will in future . 



Here is the live demo of Arcane
at railway:-"arcane-production-82cd.up.railway.app"
at Hugging-face:-"https://huggingface.co/spaces/Invictus0091/Arcane-rag"


Here is its work flow :-
            user uploads the data into pdf format
                         ||
                         ||
                         ||
             vector DB breaks into chuncks and 
                         ||
                         ||
                         ||
              Huggingface interface embeds it 
                         ||
                         ||
                         ||
                context is used under the prompt if the
                query asked is relevant then the Answered 
                otherwise "not answerable"
                         ||
                         ||
                         ||
                  user types "exit" to get out from the loop 
   


