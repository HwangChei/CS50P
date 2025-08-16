# Gooey Expense Tracker(Visual Data).
 Gooey requires a local machine with GUI support (e.g., Windows, macOS, Linux Desktop).
It will not run in CS50's web-based IDE (which is headless).

#### Video Demo: (https://www.youtube.com/watch?v=T4IylYla2Wk)
#### Description:
This project uses the Gooey library to create a simple and clean GUI for entering data, and the Pilot library to display that data visually. The idea is pretty straightforward: I wanted to build something that helps track student expenses in a visual and interactive way. Since I’m going to be a freshman in college soon, I figured this would be a useful personal tool while adding features once I am more experienced in Python— and also a good opportunity to get comfortable with working across multiple Python libraries and experimenting with visuals.

The program focuses on four main categories of student expenses: rent, grocery, utility, and tuition. These are the things I expect to spend on the most in the coming months, so I chose them as the expense options for the project. When the program starts, the Gooey interface lets the user input how much they’re spending in each category (default is 0 if they skip one). You can also choose how you want the data to be shown: either as a bar graph, a pie chart, or both. This part is also done through the GUI since GUI stores and returns values upton the called variables.

Once you hit submit, the program reads your input and then uses Pilot to draw the graphs. If you choose a bar graph, it shows each category on the x-axis with the corresponding values on the y-axis. It also labels everything, so it’s easy to see which expense is which. If you choose a pie chart, it breaks down your expenses into percentages, giving you a quick look at which area is taking up most of your budget. If you didn’t enter anything for a certain expense (like utility = 0), then the graph adjusts accordingly — which I thought would make it more flexible ,and I joined the rent and tuition expenses togtether while breaking the other two just cause rent and tuition are heavy expenses and others are lighter.

After showing the visuals, the program gives you a quick summary: the total amount spent, the average of all four categories, and which expense is the highest. I wanted it to be simple but still informative enough to give you a rough idea of how you’re spending. There’s nothing too fancy in terms of logic or algorithms — the focus here was on GUI design, visual output, and making the experience smooth for everyday use.

I didn’t build this project with any big ambitions — it’s honestly more of a personal utility tool that I plan to improve over time with experience. But for now, it does exactly what I need: lets me log my expenses and visualize them in a quick and clean way. Plus, I got to explore how to integrate Gooey and Pilot in one workflow, which was fun and helpful for learning.


## 🚀 Features

- Simple GUI using Gooey
- Input fields for 4 categories
- Automatically finds the highest expense
- Displays Total and Mean
- Shows Data in Either PieChart, Bargraph or both

## 🖥️ How to Run
>This project requires a GUI-supported environment i.e Gooey specifically.



