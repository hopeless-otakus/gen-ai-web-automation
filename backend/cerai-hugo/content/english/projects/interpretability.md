---
title: "On the Interpretability of Attention Networks"
image: "/images/blackbox.webp"
researchers: ["Lakshmi Narayan Pandey", "Rahul Vashisht", "Harish G. Ramaswamy"]
filters: [making-ai-understandable]
tags: ["making-ai-understandable"]
reslinks: ["https://proceedings.mlr.press/v189/pandey23a.html"]
reslinktitles: ["On the Interpretability of Attention Networks: Proceedings.mlr"]
draft: false
---

Attention mechanisms form a core component of several successful deep learning architectures, and are based on one key idea: “The output depends only on a small (but unknown) segment of the input.” In several practical applications like image captioning and language translation, this is mostly true. In trained models with an attention mechanism, the outputs of an intermediate module that encodes the segment of input responsible for the output is often used as a way to peek into the ‘reasoning’ of the network. We make such a notion more precise for a variant of the classification problem that we term selective dependence classification (SDC) when used with attention model architectures. Under such a setting, we demonstrate various error modes where an attention model can be accurate but fail to be interpretable, and show that such models do occur as a result of training. We illustrate various situations that can accentuate and mitigate this behaviour. Finally, we use our objective definition of interpretability for SDC tasks to evaluate a few attention model learning algorithms designed to encourage sparsity and demonstrate that these algorithms help improve interpretability. 