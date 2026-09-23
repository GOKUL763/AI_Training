# Day 2 Task: Reasoning and Acting

## 1. Scenario

### Student Exam Planner

For this task, I selected a student exam-planning scenario.

The scenario contains three subjects:

| Subject | Exam Date | Study Hours Required |
|---|---|---:|
| Python | 2026-10-10 | 12 |
| AI | 2026-10-14 | 15 |
| DBMS | 2026-10-18 | 10 |

The system is tested with questions involving both reasoning and information retrieval.

The main questions are:

1. If I study 3 hours per day, how many days do I need for AI if it requires 15 hours?
2. I can study 4 hours per day for 3 days. Is that enough for Python?
3. Which exam comes first, Python or AI, and how many days are between them?
4. I need to plan my study order for Python, AI and DBMS based on their exam dates. What order should I follow?

The purpose is to compare direct prompting, Chain-of-Thought style prompting, and a ReAct agent.

---

# 2. Direct Prompting

Direct prompting sends the user's question directly to the language model.

The model produces an answer without calling an external tool and without exposing a reasoning trace.

The process is:

```text
User question
      ↓
Language model
      ↓
Final answer

Direct prompting can handle arithmetic and general reasoning questions when the required information is already available to the model.

However, it cannot reliably retrieve the exam schedule from the external tool used in this project.

For example, a question requiring the exact exam date depends on information stored in the exam-schedule tool. Direct prompting does not have access to that tool.

Therefore, its limitation in this scenario is the inability to obtain external information that is not present in the prompt.

3. Chain-of-Thought Prompting

The Chain-of-Thought style prompt asks the model to solve a problem carefully by considering the required steps before producing the answer.

The implementation requests a brief reasoning summary followed by the final answer rather than exposing private internal chain-of-thought.

The process is:

User question
      ↓
Structured reasoning prompt
      ↓
LLM reasoning
      ↓
Final answer

This approach is useful for questions that require multiple arithmetic or logical steps.

For example, determining whether three days of four hours per day are sufficient for a twelve-hour study requirement requires multiplication before comparison.

However, Chain-of-Thought prompting does not itself provide access to external information. If the exact exam date is only available through the tool, the model cannot retrieve that information merely by reasoning.

4. ReAct Agent

The ReAct agent combines reasoning with tool interaction.

The agent can decide that it needs information from the exam-schedule tool, call the tool, observe its result, and continue reasoning.

The process is:

User question
      ↓
Thought / decision
      ↓
Action: call tool
      ↓
Observation: tool result
      ↓
Thought / decision
      ↓
Action if required
      ↓
Final answer

The project provides two tools:

get_exam_schedule
calculator

The get_exam_schedule tool retrieves the exam date and study-hour requirement for a subject.

The calculator tool performs arithmetic calculations.

For example, when asked about the order of exams, the agent can retrieve the relevant exam dates using the schedule tool before producing its answer.

This demonstrates the ReAct cycle of Thought, Action and Observation.

5. Comparison Table
Basis	Direct prompting	Chain-of-Thought	ReAct agent
Reasoning depth	Basic direct response	More structured multi-step reasoning	Multi-step reasoning combined with tool interaction
Tool usage	No tools	No tools	Uses exam schedule and calculator tools
Reliability on multi-step questions	Depends on the model's direct reasoning	Can improve on multi-step reasoning	Can combine reasoning with external information and calculations
Transparency	Final answer only	Brief reasoning summary and final answer	Tool calls and observations can be observed
Speed / cost	Usually lowest because it uses one direct model call	Usually slightly more processing than direct prompting	Can require multiple model calls and tool calls
Consistency across repeated runs	Can vary depending on temperature	Can vary when temperature is non-zero	Tool results are deterministic, but model decisions can vary

# 6. Self-Consistency Observation

The self-consistency experiment used the following question:

> If I study 4 hours per day for 3 days, is that enough to complete the 12 hours needed for Python?

The calculation is:

4 hours/day × 3 days = 12 hours

Therefore, the correct answer is yes. The planned study time is exactly equal to the required study time.

The Chain-of-Thought style question was run five times at temperature 0.7.

### Run 1

The model calculated:

4 hours/day × 3 days = 12 hours.

It concluded that studying for three days at four hours per day is exactly enough to meet the 12-hour requirement.

### Run 2

The model again calculated:

4 hours/day × 3 days = 12 hours.

It concluded that the planned study time exactly meets the requirement.

### Run 3

The model calculated:

4 hours/day × 3 days = 12 hours.

It concluded that the study plan meets the required 12 hours exactly.

### Run 4

The model calculated:

4 hours/day × 3 days = 12 hours.

It concluded that the planned study time is exactly the required amount.

### Run 5

The model calculated:

4 hours/day × 3 days = 12 hours.

It concluded that the plan provides exactly the 12 hours required.

### Temperature 0

When the temperature was changed to 0, the model again calculated:

4 hours/day × 3 days = 12 hours.

It concluded that the study plan provides the required 12 hours.

### Observation

All five runs at temperature 0.7 produced the same substantive conclusion: **yes, the study plan is sufficient and provides exactly 12 hours**.

Although the wording and formatting varied slightly between some runs, the reasoning and final conclusion remained the same in all five runs.

The majority answer was therefore:

> Yes, studying 4 hours per day for 3 days provides exactly the 12 hours required.

The majority answer was **correct**.

At temperature 0, the model also produced the same correct conclusion. The temperature-0 response was slightly different in wording but reached the same result.

This experiment shows that, for this particular simple arithmetic reasoning question, repeated sampling at a non-zero temperature did not change the substantive answer. It also shows that temperature 0 produced a consistent answer for the same question.


7. Suitability Analysis

Direct prompting is appropriate for simple questions where the model already has the required information and the task does not require external tools.

Chain-of-Thought style prompting is useful when the problem requires several reasoning steps, such as arithmetic or logical comparisons. It can organize the solution process more carefully than a simple direct prompt.

ReAct is useful when a problem requires both reasoning and external information. In this scenario, questions about exact exam dates require the exam-schedule tool. The ReAct agent can identify this requirement, call the tool, observe the returned information, and continue processing the question.

The self-consistency experiment also demonstrates that repeated model responses can vary when a non-zero temperature is used. Therefore, repeated sampling can be useful for observing variation in reasoning outputs, while temperature 0 provides a more deterministic comparison.

8. Conclusion

Direct prompting, Chain-of-Thought prompting, and ReAct solve problems using different mechanisms.

Direct prompting is suitable for straightforward questions where the model already has the necessary information.

Chain-of-Thought style prompting is useful for problems requiring multiple reasoning steps but does not independently provide new external information.

ReAct is useful for tasks that combine reasoning with external information or actions. It can reason about what information is required, call a tool, observe the result, and continue until it can produce a final answer.

Therefore, the appropriate approach depends on the problem. Simple questions can use direct prompting, more involved reasoning can use structured reasoning prompts, and tasks requiring external information or actions can use a ReAct-style agent.


The structure above covers every required section from the Day 2 document, including the comparison table, self-consistency experiment, suitability analysis, and conclusion. :contentReference[oaicite:7]{index=7}

## One important change from Day 1

Day 1 used:

```text
Output/