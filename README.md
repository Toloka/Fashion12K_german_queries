# Fashion12K German Queries dataset

To create Fashion12K German Queries dataset we sampled 12k images from  [Fashion200K dataset](https://github.com/xthan/fashion-200k) and annotated them with German and English queries using [Toloka](https://toloka.ai/).

Each row in the dataset consists of three entries:

- image url (link to s3 bucket where the original image is hosted),
- English query,
- German query.

# Downloading dataset

Dataset can be downloaded:

 - directly via [tsv file](https://github.com/Toloka/Fashion12K_german_queries/blob/main/queries_full_dataset.tsv),
 - or by using docArray from Jina AI (our collaborator on the project) via this [python script](https://github.com/Toloka/Fashion12K_german_queries/blob/main/dataset_JinaAI_docarray_script.py).

# Acknowledgements

[Fashion200K dataset](https://github.com/xthan/fashion-200k) dataset is used under the Apache License 2.0.
