# AI Usage Logs

During the development of this project, Artificial Intelligence tools (such as ChatGPT, Gemini, etc.) were used for support. However, discovering the project idea, building the core fundamentals of the analysis, and integrating the code structure were entirely done by myself. I utilized AI not as a tool to write the entire project, but as a *coding assistant* when I got stuck or needed guidance.

## In Which Stages Was AI Used?

1. **Visualization Enhancements (EDA):** Suggestions and debugging assistance were taken from AI on aesthetic aspects such as adjusting color palettes (`palette='Set2'`, `viridis`, etc.) and making axis labels more readable in the plots drawn with Matplotlib and Seaborn libraries.
2. **Debugging:** Minor code snippets were asked to the AI to understand the logic of the `scipy.stats` p-value generation and to resolve some data type errors encountered in `eda_hypothesis.py` (such as `TypeError` when converting pandas DataFrame columns).
3. **Documentation:** Some documentation structures, for which I prepared a rough draft at the beginning of the project, were formatted and reviewed with the AI assistant to make them look more organized.

## Which Stages Are Completely Original?

- **Data Collection Logic and Hypotheses:** Deciding what data to pull from the Steam API and defining the 4 core hypotheses for the "Personal vs Professional Player" comparison (Headshot, Utility, Win Rate, Eco Round) are completely unique to this project.
- **Interpretation of Results:** The evaluations reported based on the results of the statistical tests (T-Test, Point-Biserial, etc.) were manually produced and are specific to my dataset.
- **Project Code Architecture:** The logic of how the Python scripts connect to each other (`data_collection.py` -> `eda_hypothesis.py`) was planned entirely by me.

In conclusion, about 70-80% of the analysis was built with my own logic, while the remaining 20-30% involving "boilerplate coding" and syntax errors was accelerated using AI.
