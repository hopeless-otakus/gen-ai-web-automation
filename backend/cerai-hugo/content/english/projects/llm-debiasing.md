---
title: "Responsible Design of LLM-Based Systems"
image: "/images/llm-based.png"
researchers: [<a href="https://cerai.iitm.ac.in/people/chandrasekar-subramanian/">Chandrasekar Subramanian (Research Advisor)</a>]
filters: [making-ai-understandable]
tags: ["llm-agents", "safe-ai", "llm"]
draft: false
reslinks: ["https://github.com/alphasecio/langchain-examples/tree/main/news-summary", "https://github.com/Significant-Gravitas/AutoGPT", "https://www.crewai.com/", "https://openai.com/index/our-approach-to-alignment-research/"]
reslinktitles: ["Langchain News Summary: Code Repository", "AutoGPT: Code Repository", "Crew AI", "OpenAI: Our approach to alignment research"]
---

<style>

    .rectangle {
  height: 200px;
  width: 400px;
  background-color: #4cb4ac;
  border-radius:25px;
   display: flex;
   flex-direction: column;
   justify-content: center;
   align-items: center;
   text-align: center;
}
    
    
</style>

<strong>Background</strong>

Over the last year, Large language models (LLMs) such as ChatGPT, Gemini and Llama have shown remarkable intelligence capabilities and are increasingly being used in a variety of applications. However, off-the-shelf LLMs do not suffice for all use cases. In case of open source LLMs such as Llama, one option is to fine-tune the LLM for the specific use case or task; however, this can often be prohibitively expensive. Further, Responsible AI (RAI) concerns such as safety and toxicity, and their tradeoffs with model accuracy can be different for different applications, making a one-size-fits-all approach less desirable. 

The alternative paradigm is to think of LLMs as components in a larger system which performs the desired tasks. This enables a wider and more complex set of use cases to be addressed using LLMs. Further, loosely coupled designs allow components to evolve independently.

<strong>LLM systems</strong>

One way to define “LLM systems” or “LLM-based systems” is as systems where one or more LLMs perform crucial reasoning tasks; this includes LLM-based autonomous agents. This is in contrast to the underlying standalone LLMs themselves, such as ChatGPT or Llama. 

For example, <a href="https://github.com/alphasecio/langchain-examples/tree/main/news-summary">this</a> is a simple example of a news summarization system that takes a topic, searches it on Google News and then summarizes each result into a snippet using an LLM.  LLM systems can also be much more complex; for example, <a href="https://github.com/Significant-Gravitas/AutoGPT">AutoGPT</a> is a tool that uses LLM models for autonomous goal completion on complex tasks. Frameworks such as <a href="https://www.crewai.com/">CrewAI</a> enable creating multi-agent collaborative LLM systems. 

LLM systems can also have memory and access to tools. This allows them to interact with the outside world. For example, Retrieval augmented generation (RAG) is a popular design pattern for LLM systems where an LLM’s context is augmented with relevant data retrieved from external sources so as to provide more accurate and up-to-date responses. As LLMs get widely deployed into various systems, architectural patterns have started to emerge; an example of this is “self-reflection”, which this post on X by Andrew Ng talks more about. 

<strong>Responsible AI concerns in LLM systems</strong>

Responsible AI covers a wide range of topics around responsible design of AI systems. Some of the dimensions include safety, fairness, toxicity, explainability, data traceability, etc. This has been an important part of the discussion around LLMs and other foundational models. For example, OpenAI has started talking about this early on (see <a href="https://openai.com/index/our-approach-to-alignment-research/">here</a>). And there have been methods such as Reinforcement Learning with Human Feedback (RLHF) which have been used to improve alignment of these foundational models.

With LLM-based systems, new Responsible AI (RAI) concerns emerge, and these might require newer approaches beyond those used for standalone foundational models. For example, there are higher privacy risks due to potential leak of PII data when LLMs make calls to external APIs. Another example is the use of copyrighted material by one subtask of a complex agent system, making it potentially hard to detect. Some as-yet-unpublished work by researchers at CeRAI (and other collaborators) has also shown the emergence of deception in multi-agent LLM systems. In other words, while alignment of foundational models is critical, it is also important to ensure systems built on top of them have the right RAI properties. 

With the accelerated proliferation of usage of LLMs in various systems, including critical systems such as healthcare, it is imperative to bake in Responsible AI approaches from the ground up when designing such systems. 

This project aims to conduct research (theoretical and experimental) in this area and to also identify best practices for responsible design of LLM-based systems. 
