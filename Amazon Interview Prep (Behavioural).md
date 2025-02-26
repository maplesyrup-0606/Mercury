
#### Why Amazon (Introduction)
- Mercury Mcindoe, 4th year Computer Engineering Student.
- Coming into this internship, I bring experience from software development at UBC UAS and the experience of an undergraduate teaching assistant for the Math department at UBC.
- From my experience of software development at UBC UAS, I currently work as the software lead mainly in charge of the computer vision team. One of the notable projects is the IR detection system within the drone. Which used CPP for a TCP server to enable connection among the raspberry pi and the ground station, python was used implement the IR emitter detection from the photos stored in the raspberry pi.
- Amazon is one of the most innovative and advanced technology companies out in the market. With its online stores and AWS, the average person (for say in Vancouver) has benefited from its service at least one.
- I applied to Amazon to learn from the best and seek the opportunity in positively impacting customer’s quality of life with my work.

#### Strengths and Weaknesses
My greatest strength in my opinion is to lead teams and collaborate with others to fulfill our tasks.

I am able to pivot my role as a leader and take charge of not only my tasks but figuring out requirements and distributing tasks in a natural flow.

For instance, as a software lead at UBC UAS I have the role of not only working on my personal task but to collaborate with other teams (such as payload etc.) for integration. In our previous competition, I coordinated test flights with each team to discover bugs and seek potential solutions whenever we integrated. Through my actions, we were able to find and fix major issues with the drone and eventually take 3rd place in the national competition.

On the other hand, my weakness would be being lenient when it comes to handling teammates. Although being lenient would help in some aspects, I realize that always being lenient, especially as a lead, is one of the main reasons that progress might be delayed. It has been something I have been working on and has greatly improved on.


#### Stories
**Insist on High Standards + Deliver Results + Learn and Be Curious + Have Backbone; Disagree, and Commit + Earn Trust**


1. Times when time was critical, what tradeoff did you make? How did you analyze risk? ← This could be mentioned in a way that we were short in time. (Just tweak so that we had to migrate to a smaller processing unit.)
*UBC UAS - IR detection Mechanism*
“Situation”
From previous year competitions, the vision teams were always hiring machine learning models to perform vision tasks. Similarly in this year, many members were insisting on training a ml model for the IR detection. 

“Task”
However, I had a different opinion. I believed running another model for detection would be unnecessary and costly. I spoke up and suggested that we deal the IR light detection via detection algorithms used in the military on the ground station rather than the drone. This would allow us to reduce the computation power on the raspberry pi the camera and save time by a significant amount.

“Action”
I first read relevant papers on this topic since a lot of IR detection has been adapted in the military before. I realized that our requirements were much less than military situations and the detection mechanism can be simplified by a big fraction. I developed an algorithm that involved in filtering potential targets and adaptive thresholds, that were used to detect the exact IR emitters present in a photo via salient maps.

“Result”
After implementing this algorithm, not only the power assumption was reduced on the drone but I was able to reduce the detection time by cutting it down to more than half. Though a tradeoff of accuracy dropping roughly by 5% existed, the design team saw the benefits since we were able to utilize the drone battery on different tasks such as mapping etc..

**Give me an example of how you dealt with a mistake** (Customer Obsession (Work Hard for Customer Trust) + Insist on the Highest Standards)

**Was there a time you went out of your way to help a co-worker? How did you help them?**

“Situation”
I am currently in the process of a game developing project. We had some issues where members would experience bugs whenever a new change was made from other tasks. After analyzing what the issue might’ve been I realized that the lack of modularity within the code base was causing such problems. This not only lead to spaghetti code, but also frame drops since so much computation was happening at once.

“Task”
I immediately got off my task and attempted to remedy this problem. I first started by suggesting that I create a state machine within the main game logic. This way it would be easier to make only necessary parts of the code to run at specific game states along with giving me a baseline to make it more modular.

“Action”
By firstly clearing out the state logic of the game, I straight went into implementing the state machine. Then I went into the systems such as enemy_ai, rendering, physics simulator and made the code modular. This was to ensure that only parts of each system would be called depending on the game state. During this process, it required a significant amount of QA to ensure robustness. 

“Result”
My drive to deliver results, despite that I had my own task in the way allowed me to finish making a modular game system that day. And regression testing was employed to ensure that none of the original functionality was broken. Once the major changes were made, not only was each other member free from the bug prone version of the game per version, but also the major frame drops / game lags were improved significantly. 

**Was there a time that you couldn’t meet the deadline. How did you communicate that with your manager?**

“S”
During my experience as a volunteer student researcher with Professor Christoph Ortner, I had a deadline to present the benchmark results of the Julia implementation of ACE (which is our project to find out if regular julia code can approximate a Cuda Engineer’s code). Though, I wasn’t able to finish the required benchmarks on the deadline mentioned.

“T”
I had to immediately deliver to my supervisor that my results wouldn’t be readily presentation-able by the deadline. And suggest an alternative solution.

“A”
I had to identify which benchmarks that were done can be used to make the presentation more informative. By communicating with my supervisor, I asked for inputs on the critical aspects of each benchmark that could help me narrow down which to use. By prioritizing the most important benchmarks first and offering a realistic plan for the rest, I aimed to maintain the project’s momentum and ensure transparency about my progress.

“R”
Though the presentation wasn’t completely perfect, it was informative enough for my supervisor to address suggestions and provide opinions on the project so far. My supervisor also appreciated my transparency and proactive approach. This solution was able to minimize any negative impact on the research timeline, maintained the project’s momentum. And reinforced trust in my ability to manage unforseen delays.

**What was a time you went out of the comfort zone?**
“S”
During the creation of my project “My Game Manager”, I had nearly 0 experience with regard to backend development. However, I was assigned with the role to create the backend for the project which included handling various endpoints along with interactions with databases.

“T”
Knowing that I’d be working in an unfamiliar territory, I had to gain some knowledge on how backend works so that I didn’t drag the team due to my lack of knowledge. 

“A”
I spent extra time studying documentation along with how various systems interact in the backend. Frequently following tutorials and asking for guidance to more experienced team members. I was able to implement the backend which was a mix of interaction with php but mainly in tsx. One of the notable features was allowing to take text input and transform it into SQL queries in the backend and then interact with the DB.

“R”
Thanks to the effort I put in for the project, we delivered a fast, responsive application that could interact with the database directly from front end interactions. Not only did it work seamlessly with our own database setup, but I also put in extra effort to ensure it would handle any SQLite database.