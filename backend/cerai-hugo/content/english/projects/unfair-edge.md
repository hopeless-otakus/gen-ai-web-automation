---

title: "A Causal Approach for Unfair Edge Prioritization and Discrimination Removal"
image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREH_-qk6MhBc5ThPIv922G6hxDtvxAdPn5qg&s"
draft: false
researchers: ["Pavan Ravishankar", "Pranshu Malviya", "Balaraman Ravindran"]
filters: [ai-and-society]
tags: ["ai-and-society"]
reslinks: ["https://arxiv.org/abs/2111.14348"]
reslinktitles: ["A Causal Approach for Unfair Edge Prioritization and Discrimination Removal: arxiv.org"]
---

In budget-constrained settings aimed at mitigating unfairness, like law enforcement, it is essential to prioritize the sources of unfairness before taking measures to mitigate them in the real world. Unlike previous works, which only serve as a caution against possible discrimination and de-bias data after data generation, this work provides a toolkit to mitigate unfairness during data generation, given by the Unfair Edge Prioritization algorithm, in addition to de-biasing data after generation, given by the Discrimination Removal algorithm. We assume that a non-parametric Markovian causal model representative of the data generation procedure is given. The edges emanating from the sensitive nodes in the causal graph, such as race, are assumed to be the sources of unfairness. We first quantify Edge Flow in any edge X -> Y, which is the belief of observing a specific value of Y due to the influence of a specific value of X along X -> Y. We then quantify Edge Unfairness by formulating a non-parametric model in terms of edge flows. We then prove that cumulative unfairness towards sensitive groups in a decision, like race in a bail decision, is non-existent when edge unfairness is absent. We prove this result for the non-trivial non-parametric model setting when the cumulative unfairness cannot be expressed in terms of edge unfairness. We then measure the Potential to mitigate the Cumulative Unfairness when edge unfairness is decreased. Based on these measurements, we propose the Unfair Edge Prioritization algorithm that can then be used by policymakers. We also propose the Discrimination Removal Procedure that de-biases a data distribution by eliminating optimization constraints that grow exponentially in the number of sensitive attributes and values taken by them. Extensive experiments validate the theorem and specifications used for quantifying the above measures. 

