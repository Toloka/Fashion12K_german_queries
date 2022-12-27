# installing: 
# pip install docarray

from docarray import login, DocumentArray

login()

train_data = DocumentArray.pull('DE-Fashion-Image-Text-Multimodal-train', show_progress=True)
eval_data = DocumentArray.pull('DE-Fashion-Image-Text-Multimodal-test', show_progress=True)