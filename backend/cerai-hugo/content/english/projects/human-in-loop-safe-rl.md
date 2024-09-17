---

title: "Human-in-the-loop for Safe and Verifiable Reinforcement Learning"
image: "https://rbcdsai.iitm.ac.in/images/research/humans-in-loop-safe-ai.jpg"
draft: false
researchers: ["Nirav Bhatt"]
coresearchers: ["Balaraman Ravindran"]
filters: [making-ai-understandable, safe-ai]
tags: ["reinforcement-learning", "human-in-loop", "safe-ai"]
reslinks: ["https://rbcdsai.iitm.ac.in/projects/human-in-the-loop-for-safe-and-verifiable-reinforcement-learning/", https://ieeexplore.ieee.org/abstract/document/10442899/]
reslinktitles: ["Human-in-the-loop for Safe and Verifiable Reinforcement Learning: RBCDSAI", "Human-in-the-loop for Safe and Verifiable Reinforcement Learning: IEEE Xplore"]
---

One of the main challenges in implementation of RL in real life applications is safety. Particularly, the undesired and harmful behaviour of RL agents involving humans is one of the major safety concerns. Utilizing the human in the RL agent as an active participant has been an active area of research, labelled as, human-in-the-loop RL. In this work, we propose to model human participants as a constraint provider. Humans can provide context specific constraints to ensure safety. This project aims to develop a framework for safe human-in-the-loop RL with human being a constraint provider. The framework will address the following questions:

1. How do we formulate mathematical constraints imposed by humans automatically, 

2. How does the human provide constraints such that safe optimal policy can be learnt with minimum explorations (or experiments)?, 

3. How do we identify that the imposed constraints by humans lead to a feasible problem?, 

4. How to handle the trade-off between short term actions and policy optimization?, and 

5. How can we use a nominal solution of unconstrained (or constrained) MDP for recursive improvement with additional constraints?