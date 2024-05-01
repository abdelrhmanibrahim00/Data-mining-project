from sklearn.datasets import load_files

# load all subdirectories of the corpus-30docs directory
corpus_30_docs = load_files('DataSetEx7/corpus-30docs',encoding='utf-8')

# load the 'corpus-4docs' directory in the 'DataSetEx6' directory
corpus_4_docs = load_files('DataSetEx7', categories=['corpus-4docs'], encoding='utf-8') 

# show the first 30 characters of each document
print("First 30 characters of the 4docs corpus:")
for text in corpus_4_docs.data:
    print("\t" + text[:30])