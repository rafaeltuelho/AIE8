
<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 6: Multi-Agent with LangGraph</h1>

| 🤓 Pre-work | 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Session 6: Pre-Work](https://www.notion.so/Session-6-Multi-Agent-Applications-with-LangGraph-22bcd547af3d80f7a2e0cc7a2c6d7d8f?source=copy_link#22bcd547af3d8021ac68fade5a7b9df2)| [Session 6: Multi-Agent Applications with LangGraph](https://www.notion.so/Session-6-Multi-Agent-Applications-with-LangGraph-22bcd547af3d80f7a2e0cc7a2c6d7d8f) | [Recording!](https://us02web.zoom.us/rec/share/CnsbWyce6zleEHYzebhqGcbg0syunLmLkWroRQ7ATRKaz3rDqGa7sj7FQfb0hb8U.aB_oEqnl75nk68ej)  (@2nEaXuk) | [Session 6 Slides](https://www.canva.com/design/DAGstHQ78gU/D_DHLWAO5KZoQ5R1RjG3YA/edit?utm_content=DAGstHQ78gU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 6 Assignment: Multi-agents](https://forms.gle/HScbKATi6nCNYZx57)| [AIE7 Feedback 7/10](https://forms.gle/itQqhBW2PY7DTFi76)

In today's assignment, we'll be creating a MULTI-Agentic LangGraph Application.

- 🤝 Breakout Room #1:
  1. Simple LCEL RAG
  2. Helper Functions for Agent Graphs
  3. Research Team - A LangGraph for Researching A Specific Topic
  
- 🤝 Breakout Room #2:
  1. Document Writing Team - A LangGraph for Writing, Editing, and Planning a LinkedIn post.
  2. Meta-Supervisor and Full Graph

### 🚧 OPTIONAL: Advanced Build

> NOTE: This is an optional task - and is not required to achieve full marks on the assignment.

Build a graph to produce a social media post about a given Machine Learning paper. 

The graph should employ an additional team that verifies the correctness of the produced paper, and verify it fits the theme and style of your selected social media platform.

## Ship 🚢

The completed notebook!

### Deliverables

- A short Loom of the notebook, and a 1min. walkthrough of the application in full

## Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Just built my first Multi-agent workflow! 🚀

This time, I dive a little deeper into the #LangGraph, implementing a Multi-agent workflow, implementing patterns like:
 * (Team) Supervisor Agent orchestrates specialized agents (workers)
 * Team of workers (agents with specific tools)
 * Sub-graphs orchestrated by a (Meta) Supervisor Agent

 Once again, #LangSmith was fundamental to observing Graph execution, helping understand the Agent's behaviour and outputs.

🔍 Three Key Takeaways:
1️⃣ How to use multiple agents (acting as specialized workers) collaborating to accomplish a given Task. 
2️⃣ How to implement the Supervisor pattern to hand over tasks between multiple agents
3️⃣ How to define specialized agents with access to the right tools to perform their job. 

Shout out to AI Makerspace !

#LangChain #QuestionAnswering #RetrievalAugmented #Innovation #AI #TechMilestone

Feel free to check it out by:
 * looking at the source code: https://github.com/rafaeltuelho/AIE8/blob/s06-assignment/06_Multi_Agent_with_LangGraph/Multi_Agent_RAG_LangGraph.ipynb
 * trying out the Notebook in Google Colab: https://colab.research.google.com/github/rafaeltuelho/AIE8/blob/s06-assignment/06_Multi_Agent_with_LangGraph/Multi_Agent_RAG_LangGraph.ipynb
 * watching a quick demo: https://www.loom.com/share/26c6687b5bd541968d44e7a6197fdc2b?sid=b1f7eded-7ab7-40ed-adc7-eebfb4c95abe
```

## Submitting Your Homework

### Main Homework Assignment

Follow these steps to prepare and submit your homework assignment:
1. Create a branch of your `AIE7` repo to track your changes. Example command: `git checkout -b s06-assignment`
2. Respond to the activities and questions in the `Multi_Agent_RAG_LangGraph.ipynb` notebook:
    + Edit the markdown cells of the activities and questions then enter your responses
    + Edit/Create code cell(s) where necessary as part of an activity
    + NOTE: Remember to create a header (example: `##### ✅ Answer:`) to help the grader find your responses
3. Commit, and push your completed notebook to your `origin` repository. _NOTE: Do not merge it into your main branch._
4. Make sure to include all of the following on your Homework Submission Form:
    + The GitHub URL to the completed notebook _on your assignment branch (not main)_
    + The URL to your Loom Video
    + Your Three lessons learned/not yet learned
    + The URLs to any social media posts (LinkedIn, X, Discord, etc.) ⬅️ _easy Extra Credit points!_

### Advanced Build
In addition to the above, include on your homework submission form the URLs to your Advanced Build's:
+ GitHub Repo
+ Production Deployment