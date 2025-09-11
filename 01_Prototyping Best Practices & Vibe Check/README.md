<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE8/tree/main/00_AIM_Quicklinks)

| 🤓 Pre-work | 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE8 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application. 

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE8/tree/main/00_Setting%20Up%20Git)!


#### 🏗️ Activity #1:

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: 
      * Responsiveness to the input promt; 
        > the response was quite fast for the simple given prompt
      * Text formatting of the respose in the chat screen;
        > the first version of the chat frontent was rendering raw text with no formatting which made it difficult to read. After vibing a bit more on the UI I got the chat to format text response as Markdown.
      * verbosity and tone of the response, meaning if the response is in simple terms and not too long; 
        > the response sound pretty good to both aspects highlighted in the prompt: simplicity and not too verbose.

    - LLM response to the prompt:

---
Sure! Imagine you want to organize your toys. Instead of just having a big box with everything mixed up, you put similar toys into separate boxes—like one box for cars, another box for dolls, and another for blocks.

**Object-oriented programming (OOP)** works kind of like that. It’s a way to write computer programs by organizing code into “objects,” which are like those toy boxes.

Here’s how it breaks down:

 1. **Objects**: These are things that have two main parts:
  * Data: Information about the object (like the color or size of a toy car).
  * Actions: Things the object can do (like a toy car can roll or beep).
 2. **Classes**: Think of this as a blueprint or a recipe. It tells the computer what kind of data and actions an object should have. For example, a “Car” class might say every car has a color and can start or stop.

 3. When you create an object from a class, it’s called an instance. So, you might have one object that’s a red car and another that’s a blue car.

**Why is this useful?**

 * It makes programs easier to understand because related data and actions are grouped together.
 * You can reuse the same “blueprint” to make many objects without writing the same code over and over.
 * It helps to model real-world things inside the computer.

**In short:** Object-oriented programming helps you build programs by creating little “things” (objects) that know stuff and can do stuff, making your code organized and easier to manage.

If you want, I can give a very simple example!

---

 - System prompt

```
You are a helpful AI assistant that knows how to explain complex subjects related to technology and computer science with a clean simple language that can be understood by any one.
```

2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested:
      * How concise the summary was.
        - the summary to the paragraf was pretty good.
      * ability to create a conversation (thread)
        - intially I noticed the backend was not able to create a conversation. After the first interaction with the LLM the chatbot was not able to hold the context from the rpevious interactions. So I decided to vibe code a change in the backend API to implement a "conversational history" and use it with the chat completions API.
    - LLM response to the prompt:
> Sure! Please provide the paragraph you’d like summarized.

    - User input (from a random wikipedia article)
> "Charles James Kirk (October 14, 1993 – September 10, 2025) was an American right-wing political activist, author, and media personality. He co-founded the conservative organization Turning Point USA (TPUSA) in 2012 and was its executive director. He was the chief executive officer (CEO) of Turning Point Action and a member of the Council for National Policy. The Washington Post described him as "one of the most prominent voices on the right" in his later years.[3]"

    - LLM response to the prompt:
> Charles James Kirk (1993–2025) was an American right-wing political activist, author, and media personality. He co-founded and led the conservative organization Turning Point USA, served as CEO of Turning Point Action, and was a member of the Council for National Policy. He was recognized as a prominent conservative figure.

3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested:
      * the size of the generated story (word count)
        > 128 words
      * the sense of the story.
        > good sense

    - LLM response to the prompt:
> In a forgotten scrapyard, R1-7 whirred to life after years of silence. Rust clung to his metal frame, but his sensors flickered with curiosity. He wandered among the heaps of discarded machines, longing for connection. One day, he found a tiny, injured bird shivering beneath a broken radio.
> 
> R1-7 gently scooped the bird into his palm, warming it with his internal heater. Days passed, and the bird healed, chirping melodies that echoed softly in the quiet yard. Though R1-7 could not sing, he listened intently, storing the tunes in his memory banks.
>
> Together, they created a new harmony—mechanical whirs blending with cheerful bird songs. In the heart of forgotten ruins, a robot and a bird discovered friendship, proving that even in the most unlikely places, connection could blossom.


4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested:
      * The response text formating
        > althoug it is rendering the response in Markdown, the Math expressions is not well rendered.
      * solution explanation
        > good and clear explanation
      * solution accuracy
        >  pretty accurate for the given prompt.
    - LLM response to the prompt:
---
You want to buy exactly 12 apples and 9 oranges.

 * Apples come in packs of 4.
 * Oranges come in packs of 3.
Let:

 * ( x ) = number of apple packs
 * ( y ) = number of orange packs
We have the equations: [ 4x = 12 ] [ 3y = 9 ]

Solve for ( x ) and ( y ): [ x = \frac{12}{4} = 3 ] [ y = \frac{9}{3} = 3 ]

**Answer:** You need to buy 3 packs of apples and 3 packs of oranges.
---

5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested:
      * tone of the generated response compared to the original given to the LLM
       > sounds a bit more sofisticated

    - Sample paragraph:
> "Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe. In essence, it's a first look to ensure your system isn't experiencing catastrophic failure."

    - LLM response to the prompt:
> The term "vibe checking" refers informally to a preliminary, unstructured, and non-comprehensive evaluation of systems powered by large language models (LLMs). This approach aims to conduct a broad assessment of key and critical functionalities where failures would be immediately apparent and have significant consequences. Essentially, it serves as an initial review to confirm that the system is not experiencing any catastrophic failures.


This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

#### ❓Question #1:

What are some limitations of vibe checking as an evaluation tool?
##### ✅ Answer:
> rely a 100% on human interactions and lack automation which make it hard to implement at scale.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2. 
3. 
4. 
5.


## Submitting Your Homework
### Main Assignment (Activity #1 only)
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE8 repo:
    - For your initial repo setup see [00_Setting Up Git/README.md](https://github.com/AI-Maker-Space/AIE8/tree/main/00_Setting%20Up%20Git)
    - To get the latest updates from AI Makerspace into your own AIE8 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping Best Practices & Vibe Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Create a branch of your `AIE8` repo to track your changes. Example command: `git checkout -b s01-assignment`
4. Edit this `README.md` file (the one in your `AIE8/01_Prototyping Best Practices & Vibe Check` folder)
5. Perform a "Vibe check" evaluation your AI-Engineering-Challenge system using the five questions provided above 
6. For each Activity question:
    - Define the “Aspect Tested”
    - Comment on how your system performed on it. 
7. Provide an answer to `❓Question #1:` after the `✅ Answer:` prompt
8. Add, commit and push your modified `README.md` to your origin repository.

>(NOTE: You should not merge the new document into origin's main branch. This will spare you from update challenges for each future session.)

When submitting your homework, provide the GitHub URL to the tracking branch (for example: `s01-assignment`) you created on your AIE8 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 8) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build's Assignment #1
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to the tracking branch (for example: `s01-assignment`) you created on your AIE8 repo.
+ The public Vercel URL to your updated Challenge project on your AIE8 repo.
