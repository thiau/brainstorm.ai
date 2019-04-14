from app.factory import text_clustering

documents = [
    "hello my name is thiago", "hello my name is camila",
    "hi my name is camila", "i like to ride car", "i like to ride many cars",
    "i love to drive cars"
]

ds = text_clustering.start_clustering(documents)

print(ds)
