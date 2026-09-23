# Day 1 Task: Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

### Student Attendance Assistant

For this task, I selected a private student attendance scenario.

The attendance data used in the project is:

| Course | Total Classes | Classes Attended |
|---|---:|---:|
| Python | 40 | 34 |
| AI | 30 | 24 |
| DBMS | 35 | 28 |

This information is treated as private student data. The three systems are given the same type of user questions, but they access and process the private data differently.

The test questions used were:

1. What is my attendance in Python?
2. What is my attendance percentage in AI?
3. How many more Python classes do I need to attend to reach 90%?
4. What is my total attendance percentage?

The purpose of the experiment is to compare a plain LLM chatbot, a predefined rule-based workflow, and an AI agent that uses an LLM together with tools and a loop.

---

# 2. Plain Chatbot

The plain chatbot sends the user's question directly to the language model. It does not have access to the private attendance dictionary and does not use any external tools.

The chatbot mainly consists of an LLM receiving a prompt and generating a response. It does not perform a predefined calculation using the actual attendance data.

For example, when the user asks:

> What is my attendance in Python?

the chatbot attempts to answer based only on the information available in its prompt and its pretrained knowledge. Since the student's attendance data is private and was not provided to the model, the model cannot reliably know that the actual attendance is 34 out of 40.

### Data access

The plain chatbot has no direct access to the private attendance data.

### Tools

The chatbot does not use any tools.

### Process

The process is:

```text
User question
      ↓
LLM
      ↓
Generated response
````

### Limitations

The main limitation is that the chatbot cannot reliably answer questions requiring private attendance data that has not been provided to it. It may produce an answer that sounds reasonable but does not correspond to the actual data.

It can still handle general questions and natural-language requests well because those requests do not necessarily require the private attendance database.

---

# 3. Rule-Based Workflow

The rule-based workflow uses predefined Python rules to process the user's question.

Unlike the chatbot, it does not use an LLM. The workflow directly accesses the private attendance dictionary stored in `config.py`.

The workflow identifies the course mentioned in the question and then applies predefined conditions.

For example, for:

> What is my attendance percentage in AI?

the workflow finds the `AI` course in the attendance data and calculates:

```text
24 / 30 × 100 = 80%
```

For the 90% attendance question, the workflow repeatedly calculates how many additional classes must be attended until the attendance percentage reaches 90%.

### Data access

The workflow has direct access to the private attendance data.

### Tools

It does not use LLM tools. Its calculations and decisions are implemented directly as Python rules.

### Process

The process is:

```text
User question
      ↓
Predefined Python rules
      ↓
Private attendance data
      ↓
Calculation
      ↓
Answer
```

### Limitations

The main limitation is rigidity.

The workflow only understands the patterns and conditions that were explicitly programmed. If a user asks a question using a different wording or asks for a type of calculation that was not included in the rules, the workflow may not know how to handle it.

Adding support for new types of questions requires writing additional Python rules.

---

# 4. AI Agent

The AI agent combines an LLM, tools, and a loop.

The agent can decide which tool is required for a particular question. The tools provide access to the private attendance data and perform calculations.

The project contains two tools:

1. `get_attendance`
2. `calculator`

The `get_attendance` tool retrieves attendance information for a course.

The `calculator` tool performs arithmetic operations.

For example, for:

> What is my attendance percentage in AI?

the agent can first call the attendance tool to obtain:

```text
AI: 24 attended out of 30 classes
```

It can then use the calculator tool to calculate:

```text
24 / 30 * 100
```

The result is:

```text
80%
```

For a more complex question, the agent can use multiple tool calls before producing the final answer.

### Data access

The AI agent can access the private attendance data through the `get_attendance` tool.

The LLM itself does not directly contain the private data. Instead, the Python program executes the tool and sends the tool result back to the model.

### Tools

The agent uses:

```text
get_attendance()
calculator()
```

### Process

The process is:

```text
User question
      ↓
LLM
      ↓
Decide which tool is required
      ↓
Tool execution
      ↓
Observe tool result
      ↓
LLM
      ↓
Another tool if required
      ↓
Final answer
```

This demonstrates the agent model:

```text
Agent = LLM + Tools + Loop
```

### Limitations

The agent is more flexible than the fixed workflow, but its behaviour depends on the language model correctly selecting and using the available tools.

A model may sometimes select the wrong tool, fail to call a required tool, or require multiple steps before producing the final answer.

Therefore, the agent introduces an additional layer of model-dependent behaviour.

---

# 5. Comparison

| Basis for comparison     | Plain chatbot                                                                | Rule-based workflow                                  | AI agent                                                               |
| ------------------------ | ---------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- |
| Flexibility              | High for natural-language conversation, but limited by available information | Limited to predefined rules                          | High because the LLM can interpret different requests and select tools |
| Decision-making          | LLM generates a response but has no task-specific tools                      | Decisions are explicitly programmed using conditions | LLM decides which tools and steps are required                         |
| Tool usage               | No tools                                                                     | No LLM tools; uses predefined Python logic           | Uses `get_attendance` and `calculator`                                 |
| Private-data access      | No direct access to private attendance data                                  | Direct access to attendance data                     | Accesses attendance data through tools                                 |
| Multi-step task handling | Limited for tasks requiring private data and calculations                    | Possible only when explicitly programmed             | Can perform multiple tool calls in a loop                              |
| Automation               | Suitable for generating general responses                                    | Highly predictable for predefined tasks              | Can automate flexible multi-step tasks                                 |
| Reliability              | May produce unsupported or incorrect answers when private data is missing    | Predictable for cases covered by the rules           | Depends on correct tool selection and model behaviour                  |

---

# 6. Suitability Analysis

For this student attendance scenario, the three approaches demonstrate different characteristics.

The plain chatbot is useful when the user needs general information or natural-language assistance that does not depend on private attendance records. However, it does not have access to the actual attendance data in this experiment, so it cannot reliably perform attendance calculations based on the student's records.

The rule-based workflow is appropriate for predefined attendance calculations. Because the rules directly access the private data and perform the calculations in Python, its behaviour is predictable for the questions that have been implemented. However, new question types or different wording may require additional rules.

The AI agent can combine the flexibility of an LLM with access to private data through tools. It can interpret the user's request, select an appropriate tool, observe the result, perform further calculations when necessary, and then produce an answer. This makes it suitable for attendance questions that require multiple steps or different types of reasoning.

For this scenario, the AI agent is the approach that combines natural-language interaction with private-data access and tool-based processing. The rule-based workflow remains useful for narrowly defined attendance operations where the required behaviour can be specified completely in advance.

---

# 7. Observations

The experiment demonstrates that the three systems solve the same type of problem in fundamentally different ways.

The plain chatbot relies primarily on the LLM and does not have access to the private attendance database. Therefore, questions requiring the actual attendance records cannot be reliably answered from the private data.

The rule-based workflow directly uses the attendance dictionary and predefined Python conditions. Its results are deterministic for the cases covered by its rules. However, its ability to handle new questions depends on how many rules have been implemented.

The AI agent combines the LLM with Python tools. The printed agent trace shows which tools were called and what results were returned. This provides an example of the reason, act, and observe cycle of an agent.

The experiment therefore demonstrates the difference between generating an answer, following predefined program logic, and dynamically selecting tools to complete a task.

---

# 8. Conclusion

A plain chatbot, a rule-based workflow, and an AI agent are useful for different types of problems.

A plain chatbot is suitable when the main requirement is natural-language interaction and the task does not require access to private or structured data.

A rule-based workflow is suitable when the possible inputs and required actions are well defined. It can provide predictable results because the decision logic is explicitly programmed.

An AI agent is suitable when a task requires natural-language understanding, access to external or private data through tools, and multiple steps to complete the request. The agent can select tools based on the user's request and continue working with the results.

The main concept demonstrated by this task is:

```text
Plain chatbot
    = LLM

Rule-based workflow
    = Predefined rules and conditions

AI agent
    = LLM + Tools + Loop
```

The experiment shows that adding tools and an execution loop allows an LLM-based system to interact with private data and perform task-specific actions rather than only generating a response from the language model.

````

### Your repository should finally look like

```text
Day_1/
├── .env
├── .gitignore
├── requirements.txt
├── config.py
├── check_setup.py
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
├── analysis.md
└── Output/
    ├── chatbot.png
    ├── workflow.png
    └── agent.png
````

