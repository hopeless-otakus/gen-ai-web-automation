---
title: "Explainable Graphs for Legal Judgement Prediction"
image: "/images/explainable-1.png"
draft: false
filters: ["making-ai-understandable", "ai-and-society"]
researchers: ["Ambreesh Parthasarathy (Post Baccalaureate Fellow)", "Bavish Kulur (Post Baccalaureate Fellow)", "Shubham Kashyapi (Post Baccalaureate Fellow)", "Yogesh Tripathi (Post Baccalaureate Fellow)", "Dr. Gokul Krishnan (Research Scientist)", "Dr. Balaraman Ravindran (Principal Investigator)"]
tags: ["law", "making-ai-understandable", "ai-and-society"]
---

Problem Statement- Given the facts / description of a case, predict the legal articles violated in the given case. [Dataset- ECtHR  (European Court of Human Rights)]

<img src="/images/explainable-1.png">

<img src="/images/explainable-2.png">

Ongoing Work:
1. Heterogeneous Graphs
Existing LJP techniques use a single embedding for large case documents [Chalkidis et al. (2019)].
Compute fine-grained embeddings with different kinds of nodes- facts, cases, articles

2. Summarization
Query LLMs to summarize an entire case or parts of it.
Could learn better case embeddings and improve the performance of the GNN models.

<h2>References:</h2>

<ol>
<li>Cui, J., Shen, X., & Wen, S. (2023). A survey on legal judgment prediction: Datasets, metrics, models and challenges. IEEE Access.</li>
<li>Chalkidis, I., Fergadiotis, M., Malakasiotis, P., Aletras, N., & Androutsopoulos, I. (2020). LEGAL-BERT: The muppets straight out of law school. arXiv preprint arXiv:2010.02559.</li>
<li>Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2017). Graph attention networks. arXiv preprint arXiv:1710.10903.</li>
<li>Chalkidis, I., Androutsopoulos, I., & Aletras, N. (2019). Neural legal judgment prediction in English. arXiv preprint arXiv:1906.02059.</li>
<li>Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems, 33, 9459-9474.</li>
<li>Chalkidis, I., Fergadiotis, M., Tsarapatsanis, D., Aletras, N., Androutsopoulos, I., & Malakasiotis, P. (2021). Paragraph-level rationale extraction through regularization: A case study on European court of human rights cases. arXiv preprint arXiv:2103.13084.</li>
</ol>
