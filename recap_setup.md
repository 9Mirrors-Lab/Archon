Welcome to the Archon beta launch party live stream recap/condensed version. We had a super exciting live
0:07
stream yesterday that ended up going three hours long. So I wanted to create a shorter version for you so you can
0:13
still get basically all the value that I gave yesterday but in a third of the time. So I cut out a lot of things like
0:20
the Q&A and waiting for Claude Code to finish different parts of our development flow. But if you really do
0:25
want to be a part of the live stream definitely check out the full thing. I'll have that linked in the description. And also be sure to check
0:31
out the video that I'll link to right here where I introduce Archon on my channel for the first time. And the
0:36
purpose of this live stream was twofold. First of all, I wanted to give you a live demonstration of using Archon to
0:41
give you a deeper understanding of its purpose and how you can leverage it. And then second of all, I wanted to show you
0:47
that archon works really, really well with existing strategies for context engineering that you might be using like
0:53
cloud flow, the BMAD method, spectrum of development, the PRP framework, all these different strategies. And I prove
0:58
that because the focus of this live stream is using Archon with the BMAD method, which also has been highly
1:05
requested on my channel recently. So, I'm super excited to bring that to you. So, that's everything that we've got
1:10
here for the condensed version of this live stream that you're about to watch. With that, let's get right into it. Welcome everyone to the Archon beta
1:17
launch party live stream. I've been looking forward to this all week, all
1:22
month, all summer because we've been working our butts off on Archon for so long and now we have the beta launch and
1:28
I cannot wait for it. So yeah, with that I want to really quickly talk about the
1:35
plan for the stream today and just like the general structure for it and then
1:40
I'll share my screen and we'll just dive right into things. So, first of all, this is going to be a pretty casual
1:45
stream. I'm going to be kind of like leveraging Archon as you would as a new
1:51
user just getting used to the platform, figuring out how you want to integrate it in your own AI development workflow.
1:58
And uh maybe I can actually go ahead and share my screen. Okay, so what we're
Start of the Livestream - What We're Covering
2:03
going to be doing today is you guys hopefully saw the launch the beta launch
2:09
video for Archon on Wednesday. Now, I want to dive deeper into using Archon. We're going to be building something
2:15
from scratch. I'll talk about how we can use Archon in existing code bases as well, but I want to start by showing you
2:21
guys kind of talking about what Archon is all about. Uh, just to sort of recap some of the things I talked about in the
2:27
the launch video on Wednesday. Then I'll I'll quickly show like how you can get it set up. We'll poke around the user
2:34
interface a little bit. I'll show like how you connect it to your AI coding assistant with MCP. Then we'll get into
2:40
using it. And to kind of more simulate what it'd be like for you guys to play
2:46
around with it for the first time, I'm going to be using Archon in a development workflow that I'm not very
2:52
familiar with myself. So, we're going to be doing some freestyling in this stream. It's going to be fun. And so the
2:57
development workflow that we are going to be covering in this stream is the BMAD method which by the way it is
3:05
insane how many comments I get from you guys in my videos and in the Dynamis community asking for me to cover BMAD.
3:11
So there's a lot of love for this. It is a really really cool framework. Um just one of the methods that we have for
3:17
context engineering. So I cover the PRP framework a lot on my channel. Um, I've
3:23
talked about the spectriven development that we have in AI idees like Curo. BMAD
3:28
is another method for context engineering. And so, we're going to be integrating BMAD with Archon in this
3:34
stream. And I've done a little bit of prep just to make sure I understand how BMAD works overall, but I haven't used
3:40
it ever to build a project end to end. And so, like I said, very much freestyling. I'm going to be playing
3:47
around with how I can integrate Archon with BMAD with you guys live so that you get a sense of if you're integrating
3:54
Archon into your development workflow. What does it look like to just poke around and experiment with prompting and
3:59
using the Archon MCP to really build it into what you're doing already? Like everyone here has an existing process or
4:06
at least you're starting to get yourself introduced to using coding assistance. And so I want to make it really easy to
4:12
see how Archon can fit in no matter what you already are doing for your AI
4:17
development workflow. So that's what we're going to be doing and it's going to be fun. So the first thing that I
4:23
want to talk about before we get into this is just you know what Archon is about. And so I'll I'll dive into that
4:30
in a second. And I guess the the last thing that I want to say here before we dive into things is
4:35
um there might be a lot of like let's just dive into things and and get things
4:40
to work. It's going to be kind of scrappy. It's going to be fun, but I don't know for sure if we're going to have something working end to end by the
4:46
end of this live stream because more of the point is diving into how we can experiment with integrating Archon into
4:52
our workflow versus like let's fully build something end to end. Like I don't have the live stream structured in that
4:58
way and I'm doing that intentionally. um for the reasons that I've already been talking about. So I don't I don't want
5:03
to repeat myself here. The the one thing I'll say though is if you're interested in seeing my full development workflow
5:09
in a much more structured way talking about context engineering and archon and
5:15
how I use it in my workflow. Something really exciting that I've got going on um in the Dynamis community and let me
5:22
I'll actually uh bring this over from my other monitor here. I'm hosting a half-day workshop, a 4hour workshop.
5:30
It's going to be the end of this month, Wednesday, August 27th. And this is where I'm going to dive into a much more
5:37
structured approach. So, it's going to be a lot different from this live stream. Like, this live stream is going to be more casual. We're just building
5:43
things, freestyling together. I'm going to be answering a lot of your guys' questions in the chat throughout as well. But, this workshop is going to be
5:49
a lot more structured. Like, I'll dive into my full AI development workflow. We're going to build something from
5:54
scratch using PRPs and archon. A lot of the things that I've been covering on my
6:00
channel is going to be in this very comprehensive workshop. So, if you're interested in this, like my goal is to
6:06
make it so that this this workshop alone is worth the investment of Dynamist. And so, uh, yeah, I just wanted to mention
6:12
that really quickly because it's it's very much like related to like here's what you'd want to do if you like what we're diving into in this live stream
6:18
and you want something that's a lot more structured. So definitely check out Dynamus also because the prices will for
6:24
Dynamis are going to increase after um this weekend. So this is like the special Archon beta launch weekend and
6:30
then prices are going to go up after. So I just wanted to mention that quickly. U but for our workshop right now, we're
6:36
just going to have a really good time. And so yeah, let's go over to the Archon
6:42
repo here. It is the operating system for AI coding. And so what that means is
Introduction to Archon (+ Quick Setup Guide)
6:48
it's the command center. So for us, it's a sleek user interface. Like if I go to
6:54
the project management for example, we've got a sleek user interface to manage all of our tasks. We've got a
7:00
place to manage the knowledge that we want to give our coding assistants. So I can perform rag to like actually search
7:06
through the pyantic AI documentation or the cloud code documentation. So it's a UI for us to manage everything. And then
7:12
for the coding assistant, it's an MCP server. So it's kind of like leveraging what's native to humans and what's
7:19
native to coding assistants. So we all can work on the same set of context as we are context engineering. That's the
7:26
beauty of it. And it's possible to connect it to any AI coding assistant that supports MCP. And so we have
7:34
instructions if I go to like the MCP server tab. And I'll talk about how you can get this all running in a second by
7:39
the way. Uh but like we have a tab for all the popular coding assistants and um really just to keep the UI concise. We
7:46
didn't include like 20 different coding assistants, but you can connect this to every single coding assistant basically.
7:52
So we have instructions for popular ones like Klein and Claude Code like we'll be using today. I'll actually copy this
7:58
command right here. So this is the command that you run when you have Claude installed to hook in the Archon
8:04
MCP server. And um actually maybe I'll actually just go ahead and do that right now. So, I've got my terminal open.
8:10
We're going to be living and breathing in this terminal today as we do our demo. And so, to add the archon mcp
8:16
after I have it up and running, I just have to run this command. Like, it's that easy. And I already have it running, which is why I get this message
8:23
right here. But if I do a cloud MCP list, then it'll check and even validate the connection to Archon. So, that's how
8:29
easy it is to get it connected once you have the UI up and running. And I I cover instructions for like how to set
8:35
up everything in the video that I put out on Wednesday. But really, if you go to this link, so you can just go to the
8:42
Archon GitHub repository. Also, if you just go to the URL archon.y,
8:48
this will take you to the GitHub repository as well. So, I have a a URL that just like redirects you right to
8:54
the to the GitHub repo. So, it's really easy for you guys to access it. Um, so yeah, just archon.diy.
9:01
And then in the read me here, I have your quick start instructions. So, super super easy to get started. There are a
9:08
couple of things that people have been tripping up on that I want to address really quickly. Uh because honestly, like if you guys want to follow along in
9:14
this live stream as I start using Archon, I'd welcome it. Um and so, yeah, prerex, you just need to have Docker
9:19
Desktop. Uh you need a Superbase account. You can the free tier works like you don't have to pay anything to
9:25
use Archon. Um or you can even use local Superbase. So like if you're following
9:31
along with my all my local AI stuff and you have the local AI package up and running, you can use that superbase. Um
9:37
and then also you just need your API key for OpenAI. We also support Gemini and
9:42
Olama. So Olama is kind of more experimental right now. It's in the works. Um but we are we have actually an
9:49
active effort on that with a PR coming into Archon soon as well. And that's kind of the other big preface I want to
9:55
give for Archon is like when I say that it's in beta like there there are things that are like not working 100% at this
10:00
point and there are more experimental parts of the platform that um we have like things that are saying coming soon
10:07
or it just does like it needs to be tidied up. We're working on that. Like I'm I'm putting in a lot of my effort a
10:14
majority of my effort into Archon and everything related to context engineering that I have like kind of playing into Archon. So yeah, these are
10:21
the prerexs and then you just have to clone the repo and then set up your environment variables and really it's
10:27
just you have to get your superbase URL and service ro key. And maybe I could actually show that really quick as well.
10:33
I feel like that'd be useful just for the people that have been tripping up. One thing that I've been seeing a lot is
10:39
um people are using their anonymous key in Superbase instead of their service roll one. And so I'm just going to bring
10:45
over my Superbase here and show you what I'm talking about. So, I have a just like a basic $10 a month micro instance
10:52
set up for a lot of the testing I've been doing with Archon. You just go to your project settings in Superbase. And
10:58
when you go to the API key section, you just reveal and copy the service role key. So, that's the key that you put
11:05
into the environment variables for archon. And then for the data API, you get your URL here.
11:10
And then you can do a similar thing for uh self-hosted superbase. You just get your values from the environment
11:16
variables. So, not to dive too much into the setup right now just because I covered that in the video on Wednesday
11:21
already, but I wanted to at least call that out because a couple of uh issues have been created around that. Um, so
11:28
yeah, and then once you have your environment variable set up, you can set up your database. And so within the
11:34
migrations folder, I've got a single script that you can run. You can copy
11:39
this script, go into your Superbase SQL editor, and you can create a new
11:44
snippet, and then you just paste this in and run it. So, this is going to create all of the archon tables for managing your knowledge and your tasks and your
11:51
documents. Uh, very, very easy setup. And then I'll go back to the readme here. Um, because then the last thing is
11:57
to build spin up the containers. So, you just run this docker compose command. We got docker as one of our pre-wax for
12:03
this. And so, you run that and it'll spin up all the containers. And then you have everything running for archon. And
12:08
so what that'll look like in your Docker desktop is you'll have four containers running under the archon umbrella. We've
12:15
got our agents, which this is a feature that is more coming soon. But then we have our MCP server, the user interface
12:22
that we've already been looking at a bit, and then we have our server that has all of our API endpoints so that our
12:27
UI can interact with everything that the MCP server can for our coding assistant.
12:33
So that's what the setup looks like. And then if you go to local host port 3737, that'll take you through an onboarding
12:39
flow where we have you set your OpenAI API key um or you can just skip past
12:45
that and then go and set your uh Google API key. So we support Gemini as well. And then Olama, like I said, is
12:51
experimental coming soon. So a lot of things that we're working on that are coming soon. Um it's like things like
12:56
Olama. So yeah. Uh, and then once you're in Archon and you have everything set
13:02
up, this is where the fun begins because this is where we can start to scrape knowledge and get our global rule set up
13:07
for Archon. This is where the fun begins. And so yeah, um, to start, I think now is a
13:15
good time. I'm I'm going to kind of like treat this as if I'm using Archon from scratch. So, I have some things that are
13:21
crawled already that I'm going to be using in the the demo today, but I'm
13:27
going to act like I don't have that. And so, I'm going to start from scratch, talk about like what we're going to be building, and I put a lot of thought
13:33
into just having like a really cool use case for you guys. And then, we'll get into the BMAD method. We'll actually
13:38
start more with BMAD and then start seeing how Archon can play into it because I want to show you guys how your
13:43
existing strategies work with Archon. So, what we're going to be building today is going to be something kind of
What We're Building with Archon + BMAD
13:51
like this tool. So, if you guys haven't heard of Claude Code UI, and there's a
13:56
lot of tools that are like it, it's basically a user interface. So, like in mobile and on the web, we can manage
14:03
different Claude Code instances. And so, I'll open this image in a new tab so you
14:08
guys can see kind of like like what what I envision creating. And again, we might not like have an end result that looks
14:14
like this by the end of this stream because I want to focus so much on like answering your guys's questions, talking
14:19
about Archon, and integrating with BMAD, but we might get something kind of like we'll see. Well, this is kind of what
14:25
I'm envisioning here where we have a user interface. We'll build a website with Nex.js JS where we have just like
14:31
an easier way to manage the our cloud code instances and we'll use the cloud code SDK that they offer so that we can
14:38
build our own application that is invoking cloud code and we can manage um
14:43
the different instances at the same time. We can see like a log of the terminals that we have open and all the
14:49
work that they're doing which is also going to be a cool way to manage sub agents by the way within cloud codes. you can have them all running at the
14:55
same time and managing them separately and like having that integrated with Archon as well. So like this is kind of
15:01
just to give you guys like a rough idea of what I'm envisioning here, what we're going to create together. Um just to
15:06
give you a demo of BMAD plus Archon and yeah, Cloud Code UI is not a tool that
15:12
I've actually tried myself. I've used other similar ones, but I just found this one recently and I thought that
15:17
this was like a they just had nice screenshots showing what it looks like. So, I thought it'd be a nice way to give
15:22
you guys a visual of what I'm hoping to create because obviously I can't give you guys a demo of something like I do in my YouTube videos because in my
15:29
YouTube videos, I'll fully build it out first, then I'll record basically like recreating it. So, that way I can like
15:35
give you guys a demo up front and then create basically a replica so you see
15:40
the full process. So, that's what it looks like in something a lot more structured like a YouTube video or like
15:45
that workshop that I have in Dynamus coming up here. Um, but then for this live stream, we're just freestyling. So,
15:51
that's what I want to create. So, all right. Now, we can dive into BMAD. And,
15:57
uh, by the way, once we start using BMAD, that's when we'll have more natural breaks for me to take a look at
16:03
the chat here. So, I have the chat on my left monitor. I see that it's going crazy. I appreciate all you guys being
16:09
here and commenting. So, I'll definitely be diving into uh some of your guys's questions once uh we got some things
16:16
running in Cloud Code. So, let's start with a little intro to BMAD and then
16:22
once we start looking into how we use it, that's when we'll really start to see Archon play into it in a way where
16:29
like I think you guys will be able to use your imagination to see how Archon can fit into any AI development
16:36
workflow. So BMAD it is the foundation of agentic agiled driven development and
Overview of the BMAD Method
16:42
um yeah actually I think 125% is a good zoom here. So I'll stay at this level of zoom. Um so there's kind of two main
16:51
workflows that we have with BMAD. Essentially what BMAD gives us is a bunch of different sub aents that are
16:57
experts at different parts of our development workflow. So like in the agentic planning workflow, we have our
17:04
analyst, we have our project manager, we have our architect, and then when we go into development, we have our scrum
17:10
master agent that's kind of guiding all these different development agents to knock out the different stories like the
17:17
different tasks that we have for developing our project. And there are some diagrams that we have in the user
17:24
guide here um that walk us through what this workflow looks like. And yeah, so
17:29
the the BMAD method in general, it's like I said, it's a strategy for context engineering and it gets pretty in-depth.
17:37
Like these workflow diagrams that like these mermaid diagrams, they look kind
17:42
of intimidating. Like there's a lot that goes into this here. So um yeah, by the way, like this first one is the planning
17:50
workflow. And we're going to walk through this and I'll show you how to integrate Archon with this. It's not as complex as it looks. This is the
17:56
planning workflow. Then once we get into development, we have this second
18:01
workflow, which I might go through this one or I might actually switch to PRP. Um, we'll see. Like I said, we're
18:07
freestyling here. So, two different workflows that we have for the BMAD method. And the guy that created the
18:13
BMAD method, he he's a genius. Like, he's very, very smart. And he's actually
18:18
got a YouTube channel where he started covering BMAD. I went through his entire 1 hour and 15 minute master class that
18:24
he had on YouTube. By the way, if you just search the BMAT method, you'll find him. Um, but yeah, he's done so much
18:30
research into project management and best practices for architecting and different like mental models that we can
18:37
apply to planning projects. And he's done a ton of research into best practices for prompting at different
18:43
stages of our AI development workflow. And he talks a lot about that in his master class as well. And so I I just
18:50
think this is a great use case. So like apply BMAD with archon. And the other thing that he talks about is the whole
18:57
idea of um green field versus brownfield projects. So a green field project, you
19:03
can think of it like fresh green pastures. This is a new project that you're starting from scratch. And then
19:08
brownfield is when you're working in an existing codebase. And the BMAD method has different workflows depending on if
19:15
you're working on an existing codebase or not. And I know that that's something that um a lot of you guys like in
19:20
comments in my videos and in the Dynamis community have said like I want to see more of like let's use AI coding on an
19:28
existing project versus something that is green field. And so generally I focus
19:34
on green field new projects just because it's a lot easier to show how I apply
19:41
different strategies. And it's going to be the same in this live stream. on creating something from scratch because
19:46
going through the full planning workflow, it's much easier to integrate Archon and show the different parts of Archon when we're doing a lot more of
19:53
that like initial research and task management. Um, where we're it's going to be a lot more sparse if we're just
19:59
like adding new features on an existing codebase. There's going to be less tasks overall. There's going to be less research that we have to perform with
20:05
Archon and like all the knowledge that we have for Rag because it's going to be more looking at the existing codebase
20:11
versus looking at documentation. You see what I'm saying? Like brownfield projects, it's more let's reference the
20:18
existing codebase to figure out the patterns that we need to develop. With a new project, it's let's look at the
20:23
documentation for pideanti for example to figure out the patterns for developing agents that are that's
20:30
recommended for this library. So that's why we're going with green field here. The sponsor of this live stream recap is
Snyk Event
20:36
Sneak and they're bringing us a free webinar that you don't want to miss. If you're using AI coding assistance, if
20:41
you're vibe coding or even using a more structured approach to using AI coders like we're doing with Archon and PRPs,
20:48
there are still security concerns that go beyond traditional code review. That's why Sneak is hosting this free
20:54
webinar Thursday, August 28th at 11:00 a.m. Eastern time. Securing Vibe Coding,
20:59
addressing the security challenges of AI generated code. The focus is going to be specific to the unique risks that we
21:06
have with these AIdriven development workflows. How it differs from typical security concerns. This is the kind of
21:12
thing that we have to be focusing on. Sonia, a staff developer advocate at Sneak, is going to be introducing us to
21:19
how vibe coding is changing the landscape of development, what these new security concerns are with AI powered
21:25
coding, and how we can implement strategies today to reduce these risks and protect our AI powered development
21:32
life cycle. If you're in security, DevOps, or just using AI coding assistance at all, this is the webinar
21:38
for you to give you the frameworks you need to work with AI coding assistants securely. Plus, if you are an ISC2
21:44
member, you get one CPE credit just for attending this webinar. So, go ahead and register with the link that I have in
21:50
the description. Again, it's Thursday, August 28th at 11:00 a.m. Eastern. I'm going to be there myself, so I will see
21:56
you there. So, let's let's go ahead and start actually. So, going back to BMAD here,
BMAD Setup and Deep Dive
22:01
I'm going to copy the command to get started. And so, it's super super easy to get BMAD started in any project. Um,
22:10
all you have to do, and I mean I've already run this, and so I'll probably just do it on a new folder, show you
22:15
guys what it looks like, and then I'll go back to my current folder where I already have BMAD set up. I think
22:21
that'll be the best way to do it. So, let me go and get things set up in a new folder here. Okay. All right. So, I take
22:28
that command from the repo. It's just npx bad method install. Super easy. And
22:33
it's going to install the following packages. That is good. All right. BMAD method. And then the first thing you
22:38
want to do is enter the full path to your project because essentially what BMAD will do is just it's going to
22:45
install a bunch of configuration and sub aents like a lot of different markdown files to get us set up with BMAD in our
22:52
codebase. So this can be an existing codebase that you install BMAD into or in our case it can just be a brand new
22:59
folder. And so I'm going to pass in a path here. I'll call it uh BMAD
23:05
example. There we go. And then I'm going to install the full system here. And uh
23:12
will the PRD product requirement document be sharded into multiple files? Yes. Is the default. Just go with this.
23:18
PRDS. By the way, guys, this is like the document that has like a very fully
23:23
written out spec of what you want to create. So when we plan our initial
23:28
implementation, we put that in a PRD that we'll then use to break into tasks and start implementing. And we'll see
23:34
that in action as well. So I'm going to say yes. Will the architecture documentation be sharded into multiple
23:39
files? Sharded just means split up to make things more concise, by the way. So yeah, now we get to pick the IDE that we
23:46
want to configure because based on the coding assistant, there are different ways that we need to set up our global
23:52
rules and set up our sub aents, things like that. So I'm going to pick cloud code. So select with spacebar and then
23:58
confirm with enter. And you can install this in multiple ones, by the way, but uh I'm just going to go ahead and put
24:04
this in cloud code. So there we go. Enter to confirm. Uh pre-built web
24:09
bundles. I don't really care about that. So I'll just select the default. And then it says the directory does not
24:14
exist. Would you like to create the directory and continue? I will say yes. There we go. All right. Boom. Super
24:19
super quick. So there we go. We have everything created. So it created some agents for us. So we have these
24:26
different commands that we can use to invoke these sub aents. So like for example when we are first starting our
24:32
project and we'll see this in a sec when we want to start planning things we'll call into the analyst agent that BMAD
24:38
gives us and we'll use the an the analyst will actually leverage archon to
24:44
crawl through the documentation for cloud code in next.js JS to help us create some kind of more like initial
24:49
pseudo code like that first layer of like okay let's think about generally how we want to structure the codebase
24:56
and we'll actually use archon with the analyst to do that and then the analyst is going to output a brief like a
25:02
project brief that we're going to store as a document in a new project in archon. So that's kind of a little teaser for what we're about to do here.
25:08
Um, but yeah, whenever we do this and we create a new setup with BMAD, I'll open
25:14
my VS Code and I'll show you really quickly what this looks like in general. So, that's going to create this uh BMAD
25:22
core folder. So, this this works on an existing project as well. It's not going to like overwrite anything in your codebase. It creates a new folder where
25:29
we have our different agent teams, our agents. We got the core user guide here.
25:34
These are all the files that are going to be referenced by our agents as we call upon them in our development
25:40
workflow. And so like here's the markdown file for the analyst agent for
25:45
example. And so yeah basically like we have each agent starts with an activation notice.
25:51
So it's like when we call upon the analyst agent here's what you got to do and then here are the steps that you
25:58
have to follow to act as the analyst agent. So when we tell claude code or
26:05
cursor or winds surf whatever to act as this agent it reads this file and then
26:10
basically uses these instructions to change its persona. That's how we're doing. So it's not the BMAD doesn't
26:17
actually use like the slash agent feature in cloud code. And the reason for that is it's more of like a general
26:23
implementation so that you can use basically sub aents as prompts in any
26:28
coding assistant even the ones that don't have sub aents built into it. And so yeah, sub aents, if you guys didn't
26:34
know, sub aents, even in cloud code, it's really just prompts. Like you have some file that you tell cloud code to
26:41
look at and you say read the instructions here to act as this persona. That's all we're doing here.
26:47
And so we're telling it that like you your name is Mary, you're a business analyst, uh here is your role and your
26:53
style, here are your core principles, and then here are the different commands that a user can invoke. like we have our
26:59
help command, we have our command to create our project brief, which is one of the first things we're going to do. So that's essentially how BMAD works is
27:06
we have all these different agents that are fit together in this workflow that I was showing you guys in the mermaid diagram earlier, which was um if I pull
27:13
that up quick, I'll just reference that for you guys again. Um that is this diagram here. So the
27:19
analyst is at the beginning here. And so we can go ahead and invoke this. And so let's let's just dive right in. So I'm
27:25
going to clear and then I'm going to enter in a clot. And by the way, cloud MCP list, remember we've got Archon
27:31
connected already. I showed you guys how to do that. Maybe I didn't kind of do it in the right order. Like I showed you how to connect Archon, then I went
27:36
through like setting it up, but yeah. So we we we connected it with um this command right here, assuming we have
27:42
everything up and running. The MCP for Archon is on port 8051 by default. And you can configure that as well if you
27:49
want. So yeah, we'll jump into a cloud session here and let's get right into it. And so I've I came with a little bit
27:56
of prep. Um, so I know some of the commands that I want to run here. So I have that
28:02
referenced on my other monitor here just to try to make this smooth. Um, though we are mostly freestyling like I haven't
28:08
done that much. And so the first thing that we want to do is if you just do slanalyst and then you press tab, we're
28:15
going to start Mary as our analyst and it's going to help us create our brief
28:20
for the project that we want to create. So there we go. Slanalyst. Hello, I'm Mary, your business analyst. Specialize
28:26
in blah blah blah. And then type help to see my available commands. So, we can do star help. And then Mary is going to be
28:32
prompted to give us the commands that she has everything that we had in the um that markdown file that I showed you.
28:39
And while she outputs that, the other thing I want to show you guys, if I go back to Archon here,
28:47
we have the global rules that we want to create for Archon. So, in the settings,
28:52
and you're going to want to do this whenever you use archon, we have the IDE global rules. And so, based on if you're
28:58
using cloud code or not, really, there's just like special instructions for cloud code that we have, and then the rest of
29:03
your coding assistants can use the same rules here. You can just copy the cloud code rules and then you can either
29:11
create a new cloudMD and paste these in along with the typical global rules that
29:17
you use or if it's an existing project where you already have global rules then you'll just paste in the instructions
29:23
for archon along with everything else that you already have. So whether it's your claw.md or your cursor rules or
29:29
your winds surf rules this is just part like this is the part of your global rules now for archon. So you can add
29:34
this in with any of your other existing global rules. So I just wanted to call that out really quickly because I have that set up in this repository already
29:41
or this folder already. Otherwise, I literally just have my global rules and then everything for BMAD and then some stuff for PRP that we'll get into
29:48
towards the end here. So that's what I have set up right now. So going back to the terminal here, here are the commands
29:53
that we have for the business analyst. And so uh we can create a project brief.
Integrating the BMAD Analyst with Archon (Brief Creation)
29:58
we can go into YOLO mode, which I I saw someone in the chat was asking about YOLO mode. Um, yolo mode is instead of
30:08
like it working alongside you more to plan your project, implement your project, it it operates more
30:13
autonomously. So, if you want to just trust it more with the implementation, that's what yolo mode means. We're going to do some of that here because I want
30:19
to be pretty concise in going through the BMAD method here. But the first thing that I want to do is I want to
30:27
brainstorm. So I'm going to use the brainstorm command. So you do like uh star brainstorm. So the star is just the
30:34
way to like signal that we were invoking a command here. That's just the convention for BMAD. We do star
30:40
brainstorm and then we just send in a prompt for what we want it to research. And so what I want to do, I have this
30:47
pre-selected just so you guys don't have to see me type it out here. I want to create a nex.js front end where I can
30:52
spin off and manage different cloud code instances through the cloud code SDK. And I'm speaking to the specific pieces
31:00
of technology cloud code and next.js that I have the documentation for in archon. And so we'll see in a little bit
31:05
how I'm actually going to ask Mary to reference the documentation through archon so that we can get a better
31:13
planning. Basically just get a better brief outputed. So there we go. So now
31:18
there's quite a few different things that we can do after the brainstorming just based on those same commands that we saw when I did the help command
31:24
earlier. And so what I want to do is I want to do a uh I want to create a project brief.
31:32
So I'm going to do create project brief. That's just one of the commands that we
31:38
have for the analyst. I can just say two. I want to do command number two. So
31:43
instead of yeah like it it's I'm just going to like go through the flow that it's walking me through here and just kind of trust it more. So I'm going to say two. I want to create a detailed
31:49
project brief for this concept. And the analyst here is prompted to guide me
31:55
through it so that I can really be a part of creating the brief. It's not just going to go and off and do it all itself. And so in a second here, we'll
32:02
see it maybe ask a couple of follow-up questions for us.
32:07
Um, so let's see. All right, got some output here. So it's
32:13
starting to it's got the executive summary here. So it's starting to do some planning. We'll see if it I mean
32:19
it's kind of it's not always the same how the analyst works. Like sometimes we'll ask people more follow questions,
32:24
sometimes it won't. I mean the BMAD method is not always going to like perform the same because LLMs are just
32:30
unreliable. They don't always do the exact same thing. Like they won't always ask me the same follow-up questions. So
32:35
I'll just kind of let it rip here. We got success metrics and KPIs.
32:40
We've got a timeline and milestones. So Mary is very much acting like a project manager here, outlining really important
32:48
things like what's the timeline for our project. I mean, this isn't actually going to take 24 weeks. This is this is hilarious. It's not going to be 24
32:54
weeks. I promise guys, you're not stuck in this live stream for 24 weeks. Uh but yeah, we got key milestones, risk
32:59
assessment, resource requirements, which I mean this isn't really accurate
33:05
to what we're doing here. I I guess maybe if we create like sub agents for each of these things, I suppose. Um, I'm
33:12
about to spend $200,000 on development. That's kind of funny. So may maybe the
33:17
prompting for the business analyst could be a bit more accurate to like actually integrating this in development workflow, not with like real people that
33:23
we have to pay. But you guys get the idea in general. Like it's pretty cool how we have this entire project brief.
33:30
And so the next thing that I want to do with this brief is I actually want to refine it and then store it as a
33:36
document in Archon. So, we'll start to see more how archon is integrated with
33:41
uh the BMAD method here. So, okay, I'm going back to my instructions here. I'm trying to remember exactly what I want
33:48
to do next with this. Um, yeah, let's see. So, I'm going to I'm
33:53
actually going to run the the help command again because I want to remember what commands I have. Um,
34:00
and then also there are some follow-up questions that we've got here. create user stories, develop competitive
34:06
analysis, which I'm not really interested in doing that right now. Generate technical implementations. Um, what else could I do?
34:14
Um, and actually, does it did the project brief get created? No, it didn't get created yet. Okay. So, I'm going to
34:21
let's just say this. I'm going to say use archon to
34:26
uh search how to leverage the cloud code SDK.
34:34
and then add technical implementation
34:39
ideas to the project brief and save that brief in a new project I want you to
34:47
create in Archon. Okay, so here we go. This is where we really start to see the integration here. So, we're going to have Mary instead of just going through
34:53
the typical flow that you do with the BMAD method where you store all your documents in your source control like
34:59
just in your your project folder, we're going to actually have her use archon.
35:04
So, she's going to do some research on how to leverage the cloud code SDK so
35:09
that she can help me generate a more technical implementation plan and actually do it based on the cloud code
35:15
documentation instead of just like simple research or hallucinating something random. It's going to use
35:21
archon. That's going to help a lot. And then we'll store the brief in Archon as well. And we'll do that in a brand new
35:27
project that we create. So going back to Archon here within a single project, we've got the tasks tab and then we have
35:33
the docs tab. So we'll see Mary create a new project in Archon. In a second here,
35:39
this will pop up and then there'll be a project brief as well. So first of all, before she does that,
35:46
she's going to search through our documentation. So everything that we crawled like I showed you crawling the
35:52
cloud code um the cloud code documentation in real time that is what we're searching through using the archon
35:58
mcp. So we're performing rag queries and then we're also searching through the code examples that you saw being
36:04
generated as well. So I'm going to do if I do controlr and cloud code we can zoom
36:10
into the output of our different rag searches. So like when we searched for code examples, we were looking for
36:16
TypeScript implementations and um let's see what we got here. Trying to like I mean there's just a lot
36:22
of information here. I mean it's okay that we don't have to like understand all this in detail but the coding assistant definitely needs to. So let's
36:28
go up to uh the first chunk that we retrieved. So uh let's see.
36:36
It's kind of hard to like Okay, so here we go. But we got some some implementations with the cloud SDK.
36:43
So it's pulling things from the cloud SDK which is good. Um and then we got some things for the TypeScript SDK. So
36:49
that's what we actually care about using here. Um so this is good. We're getting some of the code examples. And I'll do
36:54
control R to go out of this. We don't need to like dive into that forever here. Uh but the important thing is if I
37:00
go back into Archon, I didn't even have to refresh my page because we have websockets. So there's real time updates
37:05
with Archon through the MCP and the UI. We have our cloud code instance manager Nex.js control center project. So there
37:12
we go. We got a a blank slate here. So we got no tasks at this point, no docs, but we're about to create the brief. And
37:19
so we'll see that here. Now we'll add the enhanced project brief with technical implementation to the newly
37:25
created project. So now Mary is generating that project brief. And once it is generated, we can uh go back into
37:30
Archon and see that. So we'll have to wait a little bit because it's usually a pretty long document. So, I'm going to
37:36
give it some time. So, all right, we have our brief created from our analyst.
37:41
So, I'm going to actually go back. Sorry, I'm jumping around a little bit here. I'm going to go back in. Let's take a look at this brief really quickly
37:47
that we've created. Plus one for Dynamus, not just because of Cole, but everyone in the community. I appreciate that, Sean. Appreciate that a lot. Enjoy
37:54
Dynamus as well. Thank you. What is happening in the community is really crazy. Thank you, Toby. I appreciate it,
38:00
guys. Yeah, I I just like I have to call out Dynamus a couple of times throughout this stream because it is where a lot of
38:06
big things are happening. Um even like with Archon and everything else around building agents and context engineering,
38:13
but yeah. Okay, so here we go. We got our document created. It's untitled probably just because um Mary didn't
38:18
really understand exactly how to create the document in Archon. I mean, it's just, you know, the little things that
38:24
we're working through still. But here we go. We got next steps. We've got a risk assessment. And so again like all the
38:30
like genius things that the guy behind BMAD uh created like all the research he's done around prompting and project
38:36
management providing the right context like we see that in the different sections that we have here. We've got
38:42
our objective goal uh we got our project overview the scope requirements
38:48
and uh if I scroll down a bit more I'm curious if I can get to the things where it's like more specific to the research
38:55
I did with claude code. Uh, okay. So, technical specifications. Let's see if this gets into it more. Uh, okay. We got
39:02
our tech stack. This looks pretty good. Real time with sockets. Next.js.
39:08
Um, nice. Looks good. Um,
39:15
okay. Direct SDK integration using TypeScript Python wrappers. I don't actually like that. I don't want Python
39:21
wrappers. So that's another thing I'll say in general with context engineering is like it's so important to validate
39:26
the output that you have uh from these kinds of um sub aents just any coding
39:32
assistant in general they they'll hallucinate weird things like this and so I'm actually going to go back into
39:38
our analyst here and I'll say I don't want a Python wrapper for anything.
39:44
Also, I need you to write out some more pseudo code.
39:50
Uh, do some more research on integrating
39:55
Cloud Code SDK with a Nex.js backend. Search the
40:02
Cloud Code docs some more for this. Okay. So, I'm going to have it correct itself in a couple of ways here. So you
40:08
guys are seeing live how I'm like looking through something finding those those code smells or like the doc
40:13
smells. I'm like that is bad. Like I I if I'm using Nex.js, it can be my front end and my back end. I don't need Python
40:19
wrappers for anything. So clearly it got confused just as it was searching through the docs. But that's okay. So
40:25
yeah, it's going through and it's it's performing rag and searching through the code examples again. So we'll see what
40:31
kind of token or what kind of output we're getting here. U okay. Th this is actually what I wanted because now the
40:38
main thing that I needed to understand is this import right here is actually super crucial because we need to
40:43
leverage this query in order to call into cloud code from our Nex.js backend
40:49
and I'll show you guys specifically the docs that it is referencing
40:56
is uh I'm talking about this or not where is it this thing right here. So
41:02
import query from cloud code and then like here's like a super basic example of how you can call cloud code within
41:08
your TypeScript code. So like this would be within our API endpoint in Nex.js. So like this is what it just found when it
41:14
searched through using the knowledge that we have crawled with archon. So that's really good. That's exactly what we wanted it to find. So now we can use
41:22
that and it's just wrapping up here. So I'll let it wrap up. And it it also did
41:27
a web search here just to like supplement his information, which by the way, Archon doesn't have to fully
41:32
replace the web search that most coding assistants have. Like you can use these things together. Like I I love seeing it
41:38
when it performs some queries like looking at code examples and performing rag. And then it also does a web search and it combines all that together. Um so
41:46
yeah, we'll see that. And then it's going to update the archon project. So it'll go ahead and update the brief that we have in the UI as well. Uh did you
41:53
update the brief in Archon? make sure you do so. Okay, because I need I need
41:59
to see that like I don't just want the output here. I needed to update the brief. And this is a a good example where um okay, this sucks. I'll come to
42:05
this in a second. This is a good example where um there's definitely an opportunity to customize the prompting
42:12
and the global rules to make Archon integrate more closely with BMAD. Like the analyst here, Mary, she didn't quite
42:18
understand that like, oh, I have to go back in and update Archon. I mean, she apparently she said she did, but she
42:24
didn't, which is super weird. Like, that seems like a problem in the prompting somewhere. But like, yeah, there's definitely an opportunity to have like a
42:31
like BMAD specific set of prompts where it's like for the analyst, this is how you work with Archon. For the PM, this
42:37
is how you work with Archon. Like, that's kind of going back to what Maxim said earlier. Like that's the goal that one of the goals I have for Archon is
42:43
making it so that like there's a preconfigured setup to work with these different strategies. We have now
42:48
updated our brief. So, we did a bunch of searching here. Now we've updated our brief in Archon with some more technical
42:54
implementation. So let's actually go back into Archon. Let's check this out. So I'm going to refresh.
43:01
Go into docs. Oh, this is the wrong project. Here we go. All right, we got a
43:06
title now, by the way. That's good. So she Mary fixed things with version 1.1 to actually add a title. And cool. She
43:11
even labeled herself. This is cool. So this is this is another neat integration. Something that that another
43:17
big thing. I know that I'm talking a lot about like the vision of Archon here um as well as showing it, but I think that's important. Another big thing we
43:24
want to do in Archon is make it integrate really really deeply with the idea of sub agents. And so different
43:31
documents can be labeled by the agent that created them. Different tasks can be assigned to different agents like we
43:37
can have Mary tasked with the um the research and the like initial like kind
43:43
of like all the analyst stuff, right? like we're creating our uh brief here and then have like the project manager
43:49
tasked with the things that we have related to creating the PRD having the developer tasked with things related to
43:55
the coding and the QA agent like we can have these different tasks that are assigned to different things that we
44:00
have in our task list here and then have them all coordinate together and so we have like clear boundaries and what sub
44:07
aents are implementing what things based on their assignment in archon that's another thing that we're looking to do
44:13
as well so here's Mary has added version 1.1 for the brief. So we have a lot of
44:18
the same things as before like our scope requirements and our text stack and resource requirements but then we should
44:24
also have more of a technical implementation. Um like here for example we got some
44:31
actual like code in here and I don't I'm not going to like go through and like validate all this right now because I I
44:37
do want to move forward but like we have some more like technical pieces to our implementation now. Um so I think that's
44:43
a good starting point. we'll kind of go with that. Um like talking about the context manager pattern like things that
44:48
are specific from the clown code docs that I found. So that's really good that we have that now and we used archon to fetch those things because who knows if
44:54
a web search would have been able to get something that specific and um also it's just nice that like we can pull code
45:00
examples and things from archon as well. So okay, there we go. We'll go ahead and um
BMAD Project Manager + Archon (PRD Creation)
45:06
move on to the next thing here. So we have our brief created now. And so
45:11
actually what the founder of BMAD recommends doing is clearing the conversation entirely when we go on to
45:16
the next agent. So we've been working with the analyst agent this entire time. Now it is time to move on to the project
45:23
manager. So I do PM uh / PM and then tab. So I'm now invoking the project
45:28
manager because essentially what we want to do now is we want to take the brief that we've created in Archon based on
45:33
all the research we've done and everything and we want to turn it into a PRD. So, it's going to be more
45:39
specifically like let's dive into the specs for what we want to have created. So, now we have John, our project
45:44
manager. It's actually pretty cool because I invoke John and right away he goes into
45:50
the existing project that we have for Archon. That's pretty cool. So, we have uh no tasks yet, but yeah, that's right.
45:57
Like right now, we just have the doc in the project. So, I can do star help to see what we can do with our project
46:02
manager. Now, the thing that I want to do is create a PRD.
46:07
Um, so yeah, let's go ahead and I'm going to copy the command here. So, specifically what we want to do is we
46:15
want to create a PRD. And I I promised that I would talk about working with brownfield projects as well. So, we're
46:22
creating something from scratch here. But if you're working in an existing codebase, like I said, the big
46:27
difference is with existing code bases, generally you're going to be more referencing existing code versus with a
46:33
new project, you're looking to external documentation for things like architecture and best practices. And so
46:39
there are actually different commands that we invoke in John, our project manager in BMAD, based on if it's a new
46:46
project, this is for a new project, this is for an existing project. like if we're creating a PRD to add a new
46:52
feature into an existing codebase and so I won't showcase this right now but yeah the diagrams that we have for BMAD if I
47:00
go back to that here there is a different step that we take based on if it is a new project or an existing one
47:06
we're kind of at this stage in our diagram now so I'm going to paste in my command here uh whoops I did not mean to
47:14
do that let me copy the other thing that I have uh just from my notes here my other monitor okay this is what I meant
47:19
to do So we're going to call the create PRD command and I'm telling it to pull the brief that I have in the archon
47:25
project and then I want it to create the PRD in archon as well. So we'll have a
47:30
second document after we invoke this command. And also the big risk that I have to tell you guys with claude in
47:37
general and with BMAD is it oftentimes loves to overengineer.
47:43
And I'll show you guys what it looked like. This this is really unfortunate. the other example that I showed you guys. So like this project that I had
47:51
created to like play around with BMAD initially, it created 123 to-dos. It
47:58
completely overengineered with like super random tasks and things like this is the risk that you have when you have
48:05
Mary and John working together to create your initial PRD. like things just get
48:10
so overly complex because it's trying to build like this full productionready software for you and you don't need that
48:16
to get started. It's way too much to to go through in in one time at one time. So yeah, I would say like my biggest tip
48:23
is in your global rules for your coding assistant and just generally in your prompting. It's important to be clear
48:30
quite often that you want things to be simple because Claude loves to overengineer. It's so annoying. You we
48:35
don't want 123 tasks. We want like 10 to 20. Like that's what I'm hoping to create here. And so I'm telling it to
48:41
not overengineer and just keep things simple. And so first we'll see it call into archon. So it'll use the MCP to
48:47
grab the brief. U there we go. So we pulled the brief. I can do control R to
48:52
expand it. We can see it. It pulled the brief here. And then it's going to uh do
48:58
some research. I I forget exactly what the project manager does to like create the um to create the PRD. like I forget
49:05
if it does research or if it more just like takes this and transforms it into a a PRD like just with its own reasoning,
49:12
but we'll see in a second. This will obviously go for a little bit though because um or no, I guess it wait I
49:19
guess it's almost done. Here's our simple PRD. Okay, product vision core
49:24
problem. Here's our solution. A lightweight Nex.js app that wraps cloud code SDK to enable multi-instance
49:30
management. This that's perfect. That is a oneliner for exactly what I want to create here. So it's good. it understands what I'm looking for. And
49:36
then here's our MVP. Here are things that are out of scope. So it's avoiding complexity. I actually love this a lot.
49:41
So when I was playing with BMAD initially, it was like including like all of these things. Like I actually
49:46
remember seeing this explicitly that it was like trying to implement like team features so we could have multiple people managing this this whole like
49:53
application which that's cool, but like let's not try to implement that right now. It's good that we're excluding some
49:58
of these things. So we're starting with a simple local app like we have with Archon. Then we can build these things
50:04
after which by the way that is actually what we're doing for archon like in scope what we built for the beta of
50:10
archon is let's give a simple and beautiful user interface to manage
50:15
projects knowledge and documents. Then when we start to move out of beta and
50:20
get a lot of feedback for how we can improve the platform, then we'll start to add in different context engineering strategies and being able to manage the
50:27
full suite of context and let's get into enterprise f features and make it so you can host archon like that. Those are all
50:33
the things that are coming for archon. But we not we got to start simple because if you try to do too much at
50:39
once like coding assistants like to do, you are just in for a world of hurt. And so we're starting simple. I I actually
50:45
appreciate this a lot. So, let me go back down. Okay, so uh yeah, out of scope. Here's
50:51
our simple architecture. I mean, I kind of wish it expanded on this a little bit more at least, but that's okay because I actually love it
50:58
when coding assistants will output like the code base, like the structure that they're they're looking to implement.
51:04
But yeah, here is our text stack. Xterm for terminal display sounds good to me. NextJS14 Tailwind looks good. Um, no
51:12
need for Okay, so it's just going to do local storage for the config. So, we're not even using a database, which I think that's fine, I guess, for this
51:20
implementation, we'll call it good. U maybe it's actually a little too simple, but I think for the cases of our live
51:26
stream here, because we're already at one and a half hours, this is probably this is probably good.
51:31
So, yeah. All right. Um, let me go to success criteria, development principles. Good. Good. User journey.
51:39
Okay. Now, now we create this document in uh Archcom. So, cool. All right. So,
51:44
let's actually take a look and make sure this was created, that it's looking good. So, I'll go to my projects. I'll go to this one that we have new here. Go
51:52
to docs. And there we go. Here is our PRD. Nice. Cloud code instance manager
51:57
simplified PRD. And um yeah, looks like there's a couple of little issues here. Like I said, the
52:04
docs part of Archon is like the most experimental right now. And so, it's
52:09
expected to not like look the perfect right now. There actually is a PR out from Sean to improve a lot of these
52:14
things. So, we got we got improvements coming for this like really really soon. Um but yeah, um this is looking really
52:21
good though. We got our text stack folder structure. Here's our scope looking really good. Like perfect. All right, we got our PRD. Like now we're
52:27
ready to dive into the implementation. Um yeah, like this is this is great. I
52:34
love how it looks overall even though it's not like perfect yet. And then there's also a markdown editor. If you want to edit things yourself, you can do
52:39
so. So you can be a part of the process of editing the doc right in archon and then saving it to your superbase. So
52:44
like all these documents are stored in superbase so you can reference them between sessions even between users very
52:50
easily. Like one thing that us like core maintainers for archon like everyone in the dynamis community what we're looking
52:56
to do is actually like spin up a shared archon instance which it doesn't
53:02
actually mean like here here's the cool thing with archon. If you guys want to share your Archon instance with other
53:09
people because everything is stored in Superbase, it's not like you have to host one Archon instance and then deploy
53:16
it to the cloud. Like you can have everyone running their own Archon instances locally just pointing to the
53:22
same Superbase database that you have in the cloud. And so obviously that wouldn't work for like localhosted
53:28
superbase. But if you're going to like superbase.com and creating a project there, then everyone can can use the
53:34
same archon instance. You can have everyone working on the same projects and docs. They're just all running their
53:39
own archon pointing to the super basease in the cloud. It's pretty cool. So I'm going to I'm going to clear and I'm
BMAD Architect + Archon (Task Creation)
53:45
going to go on to the next agent here. So going to our flow within BMAD.
53:52
Let's go back. So, next up, we have our architect. So, we're going to create uh
53:58
the architecture from the PRD. And also, I'm going to actually have the architect create tasks for us in Archon. So, I'll
54:03
do slash architect. Good. Good. And then I'll do the help command after it runs its little intro
54:08
message for me here. Um or I guess it's going right away. Wait, what is it doing? I'll help you
54:14
set up the Archon project management system for a BMAD app. Let me start by checking what's available in the Archon MCP and create a project structure. Um,
54:24
all right. It's just going right away. This is interesting. I'm just going to let it run. Like I said, we're freestyling today. When I tested the
54:32
architect before, it didn't do this, but now it's just like running right away. Um, and it's okay. So, now now we're
54:39
integrating BMAD with PRP. Let's go. Okay, this is interesting. I'm I'm just
54:44
going to see what it does. Um, what is it doing?
54:50
Okay, I need to stop it now. Sorry. Sorry. Sorry. Uh, architect. What's the
54:55
architect's name? The architect didn't even tell me what its name is. It just went right into it. Uh, what is your
55:01
name? All right, cuz it create the the thing that I made me have to stop it is that it created a third project and
55:08
that's that's not good. Like I needed to I'm going to just go ahead and delete this project because I need it to reference the existing one because we
55:14
got our docs here. So, but that's all good. Like it's fine just to correct it quick. Okay. So, it's Winston. So,
55:20
Winston dove in right away before even introducing himself to me. Okay. Okay.
55:25
Winston, I need you to use the existing project in Archon and then I'll just
55:31
call out the name. Uh, so let me go back here. I'll copy this because I I just don't want to
55:37
reference the old one that I had just to like show you guys a previous attempt. So, um, yeah. Okay. So using this
55:43
project read the PRD that we have stored in that project in archon.
55:50
Then I want you to shard the PRD into tasks
55:57
uh no more than 20 tasks and put those in the tasks for the archon project. All
56:03
right. So basically what I'm telling it to do is pull down this document right here. And then based on all the
56:09
requirements that we have and everything, I want it to just create 20 tasks. So we start building up our cananban board here. So we can dive into
56:15
the implementation. And so I don't know if 20 is enough or not. I just want to like really keep it simple here. And so
56:22
yeah, so it's pulling the document here. And now we're starting to create some tasks. And so we should be able to see
56:27
this pop up in real time as we go. So let's see what it's doing here. Here, I'm going to go ahead and refresh.
56:34
Um, okay, there we go. All right, so it's creating some tasks there. I got to Sorry, I'm having an
56:41
issue with my browser here. Um, okay. Yeah, there we go. So, it's creating some tasks here. Like, let's
56:48
see this one right here. Create cloud SDK wrapper class with TypeScript. Looks good. And it's referencing the specific
56:54
file to implement. It's talking about error handling with some like specific errors that so like this class the CLI
57:00
not found error like it found this from the cloud code documentation. So this is based on its research that it did with
57:06
the archon a rag the functionality that we gave it. So yeah it's looking good. So it's going through it's creating all
57:12
these tasks here and um yeah I'll just kind of let it run with that. So I'll go
57:17
to the chat here while we got the the tasks being created in archon.
57:22
Um, Winston is defin on the chopping block. Yeah, come on, Winston. No, it's
57:28
all good. Um, because like I said, there's probably a lot of opportunities to integrate BMAD with Archon a lot more
57:37
with like just even the way we're setting up the global rules, telling Winston how to use Archon, so it doesn't
57:42
make those assumptions like he did in in um initially, which yeah, so I don't really blame him, but it was funny. So,
57:49
yeah, LLMs and and sub agents, they're they're inconsistent in the way that they leverage the tools that we give them. And so, that's why it's really
57:55
important to be super specific with our prompts. Let's go back to um I'll just
58:00
refresh to make sure. Oh, no, it was already loaded here. So, we got the 20 tasks for our project here. So, it's
58:07
starting all the way at the beginning with initialize next.js 14 with TypeScript and Tailwind.
58:14
Um and then we get create API routes. um for different things. Looks good.
58:20
Build, create the instance model form. Okay. All right. Good. Good. All the way to final testing and GitHub release
58:26
preparation, which maybe that's a little bit of overengineering, but yeah, within each of these tasks, we also have a
58:31
description. So, we're giving more context to whatever ends up implementing this, what exactly we're looking for.
58:36
And here we're specifying things like using externs. So, it's very much referencing the plan that we have in our
58:42
PRD. It's putting those things into the descriptions here. like we have our text stack being referenced throughout our
58:48
tasks. And so everything is like very integrated here. That's the beauty of it. And so now going back to my um
58:57
architect here, there's a lot of other things we can do. So, I'll kind of like continue with the common theme here of
59:03
like I'm not going to be using everything within these sub aents just to keep things concise, but I want to like show you guys some of the other
59:09
things you can do with these different sub aents with the BMAD method and probably some other things that could like integrate more with Archon as well.
59:16
So, our Winston is a devious little architect that didn't even introduce himself at first.
59:22
He can do a lot of other things. We can um do some more research if we wanted to. Like I could actually have him like
59:29
research best practices for architecture. Going back to Archon for the docs, we can have him create a
59:35
front-end architecture specifically, which if I had the time here, I probably would actually do this. I think that
59:41
would make sense because a lot of what I'm building here is relying on the front end being quite robust, especially
59:46
being able to like have terminal output for our different cloud code instances. Like definitely that would be important.
59:51
Um, however, to keep things concise, I'm going to clear. I'm going to say we're good here. So we got our tasks, we've
Generating Our PRP
59:58
got our PRD, like we have all the context we need to really start diving into the implementation. So our PRD plus
1:00:06
our tasks plus probably leveraging our knowledge base even more. Like that's
1:00:11
everything that our development agent now needs. And so there are some different agents within BMAD. Like we
1:00:18
have the dev agent. I could dive into using this. Uh we also have the
1:00:25
um scrum master agent. If I wanted to invoke the scrum master agent, we could dive into these things. That's really
1:00:30
going to be that second part of the flow that we have in BMAD. So like we basically went through this whole
1:00:36
planning workflow and I know I skipped a lot of things, but like we went through it and a lot of it is optional. And now
1:00:41
we've gotten to the point we're ready to go to the development workflow. And so we kind of go in a cycle here where we generate these stories based on our PRD.
1:00:49
I kind of did something a little bit differently in Archon where instead of stories, I more just have like the different tasks in our project. And so
1:00:55
now we can start knocking these off one by one. And in order to do this, I actually kind
1:01:02
of want to use PRP. Like I said, freestyling. I'm going to switch from BMAD to PRP. So we used BMAD
1:01:09
for the planning. And that's kind of equivalent to creating like our initial MD file where we're just describing
1:01:14
those initial requirements that we have to create our PRP. And so I'm going to do something kind of interesting here.
1:01:21
So within my uh VS Code, I'll I'll just pop this up quick. Within my VS Code,
1:01:27
the same place that I have BMAD set up, I also downloaded the um the starter for
1:01:33
PRP. So we have our two commands to execute and generate PRPS. I've got my
1:01:39
template to base a PRP off of. By the way, this is all available to you guys
1:01:46
in the context engineering intro repository that I've covered on my channel a couple of times. And so I'm
1:01:52
just pulling all of the like getting started stuff from this repository so we
1:01:57
can implement PRP because what I'm going to do is I'm going to take the spec the PRD that we generated with BMAD and I'm
1:02:04
going to turn that into a PRP so we can just start implementing it with all the tasks that we have in Archon as well.
1:02:09
So, this might be a little bit of overengineering, but I think this is cool to experiment with. So, we're just
1:02:16
going to do it. We're going to go ahead and do it. So, I'm going to do slashgenerate PRP. And then, typically
1:02:23
with PRPS, you want to reference a file that has your initial requirements, but
1:02:28
instead, I'm going to say uh look at the or I'm going to say use the PRD we have
1:02:34
in the Archon project. And then I'm going to go back to Archon because I got to copy that name again of the project
1:02:40
here. Cloud code instance manager Nex.js control center. There we go. So copy
1:02:46
this, paste it. There we go. Okay. So we're going to generate a PRP which is
1:02:52
going to it's going to take the PRD and turn it more into a prompt for our coding assistant. So we have things like
1:02:57
validation gates so it understands how to validate its work. We're going to be more explicit with like the final
1:03:03
codebase architecture that we want. And so yeah, I'm gonna I'm gonna let it run and do that. Um, so yeah, let's actually
1:03:08
go back in the terminal here because we have our PRP. I'm gonna get get back to the the coding for a bit, but I really
1:03:14
appreciate being in the chat with you guys. Um, so like I said, like we're we're going through this thing. I don't think we're going to build it from like
1:03:20
fully build it here. Um, because the focus is showing you how to integrate BMAD with Archon and now we're talking
1:03:26
about PRP as well. We're freestyling and I just want to talk with you guys, have a chat with you guys and and answer your
1:03:32
questions. So I'm putting a lot of emphasis into that as well. But yeah, here is our PRP.
1:03:37
So, I'm going to open a preview of it so we can take a look. Uh, there we go. At our purpose, our
1:03:44
core principles, and our goal. So, we're following the base PRP. This is the template that we're basing this off of.
1:03:51
Um, let me go back. There we go. So, we got our why. We got our what, what we're building here. We got our success
1:03:57
criteria. Here's all the documentation that we want it to uh read through,
1:04:02
which that's good. But also, I want to tell it to use Archon as well. So, I'll
1:04:07
say use Archon for Claude Code SDK and Nex.js Docs.
1:04:14
Um, yeah. So, I'll just I think I'll just leave it there. That's good. So, within the documentation and reference,
1:04:20
I didn't really I should have been explicit in creating the PRP that I wanted to use Archon, but this is going to work as well. So, I'll just add it
1:04:25
here. must read. You must use Archon for cloud code SDK and Nex.js doc so we can kind of more supplement the research
1:04:31
that we've already did with the Archon MCP and then doing some research on like Xterm and and real-time patterns. Looks
1:04:38
good. Here's our desired codebase. See this this is beautiful. Like this is what I like seeing. And Claude actually
1:04:43
does a really good job at respecting the desired codebase tree. And so this is what our end result is going to look
1:04:49
like where we have um we have our API where we have the routes for managing cloud code instances. We have the
1:04:56
different components for displaying the terminal and the logs. Like this is really good. We've got known gotas and
1:05:01
then we have a lot of pseudo code here and the list of tasks that need to be implemented here which I'm going to just
1:05:06
tell it to use archon. So maybe there's a little bit of a disconnect here. Um but yeah, it looks pretty close to what
1:05:12
we actually had in in um Archon. So I might have even referenced it. I'm not totally sure exactly but yeah then we
1:05:18
just have a lot of pseudo code. So yeah and then uh yeah I guess the very last thing is the validation gates or
1:05:23
validation loops. So one of the really important parts of the PRP framework is telling the coding assistant how it can iterate and validate its own output. So
1:05:31
like with linting checks and we're going to have it write unit tests and integration tests. Uh which I'm actually
1:05:37
going to take out integration tests because that's probably too much for right now. So I'm going to go ahead and
1:05:42
take this out. So again, just like with out with validating code that's outputed from your coding assistant, you want to
1:05:48
validate the PRP before you execute it. Make sure that it's aligned with what you want to create and that it's not
1:05:53
overengineering because that's another big thing that coding assistants do. Like I was talking about earlier, we got
1:05:58
our final validation checklist and then some anti-atterns here. So we're looking good. And our confidence score
1:06:05
is not as high as I want it to be, but just for the sake of brevity, I'm going
1:06:11
to go ahead and kick this off. So, I'm going to clear the conversation,
Executing Our PRP (Implementation)
1:06:16
and I'm going to say execute PRP. And then the path to our PRP is PRP's claude
1:06:23
code instance manager MD. And then, uh, the other
1:06:30
thing is I'm going to kick this off. I'm going to say use the archon project for
1:06:35
task management and archon for rag. Um, and then I'll say the project is and
1:06:41
then I'll go back into here. I got to I keep I should just like
1:06:47
memorize this. Let me copy this. Cool. Go back in here and paste that. All right. There we go. Okay. And it
1:06:54
actually was checking for projects already. So it it knew to use archon, but now I'm just being explicit telling it which project to use. So there we So
1:07:00
now now it's it knows which project to use, but it's going to look there already anyway. So all right, we're using Archon right away for our
1:07:06
implementation. So we got one task that's done. Okay, now it moved on to the next one is in progress. So now it's installing configuring cloud code with
1:07:13
Xterm. Okay, so we're good. So it's moving through the implementation. Now the rest of this we're just going to have to wait a while because it's going
1:07:18
to have to knock through all these tasks. But you can very much see that it's doing so and it's leveraging Archon
1:07:24
and this is beautiful. I want to ask again, wouldn't it be better idea to have ready-made boiler plates to start
1:07:29
with and have the agent choose the best one that fulfills most requirements and build on that? Yes, definitely. And um
1:07:36
yeah, that's one of the things that I was talking about earlier for one of my long-term visions for Archon. So, I I
1:07:42
love talking about the long term for Archon because as exciting as it is what we have built right now, there's so many
1:07:47
more things we have to make it like way better. And so, let me talk about that again. And this might be like a little
1:07:53
bit of reiterating, but still it's it's it's really cool to talk about and just like get our brain juices flowing for
1:07:58
what's what's possible with a tool like Archon. So, one of the things that we have in the Dynamis community
1:08:07
is, and I've kind of been referencing this, but I haven't been showing it yet. We have the context engineering hub. So,
1:08:13
this is private to the Dynamus community, but I definitely want to like share a lot of these resources um with
1:08:18
all of like just to my YouTube channel as well. But one thing we're working on in Dynamis together
1:08:25
is we're working on the context engineering hub. This is going to be basically a a gold mine of resources for
1:08:34
PRP templates and slash commands and global rules and cloud hooks and sub aents that everyone is contributing
1:08:40
together as a community. We started this like really recently actually. And so the goal with one of the goals
1:08:46
with this is to eventually integrate it with archon where archon can look at this context
1:08:51
engineering hub and it can say you would tell it like I want to build a nex.js JS application or I want to build a
1:08:58
pideantic AI agent and archon will search through these different things just like it searches through knowledge
1:09:04
with rag and it'll be like oh sweet here is the pyantic AI PRP template so you
1:09:09
have a boilerplate like you said Ramy and like oh here are some slash commands uh in uh cloud hooks and sub aents that
1:09:16
will work well to help you build out this agent and then oh here's the Python global rules like if we go to our global
1:09:22
rules here and we're continue like we just started building this out so there's not a ton here yet, but we're working on a lot of resources here. Like
1:09:28
here, here's Raasmus' global rules that he uses for all Python applications. And so Archon would pull this because you're
1:09:34
building a Python Pantic AI agent and then it would go into your knowledge and be like, "Oh, you're building with
1:09:39
Pyantic AI, so let me go ahead and and find the what I want to crawl for Pantic AI." And then I'll go ahead and crawl
1:09:45
that and add that and then I'll make a new project for you in Archon. So you have like all this boiler plate set up for you to just like And by the way,
1:09:52
look at how much it implemented already. We're already on task eight out of 20, which is pretty sweet. But yeah, anyway,
1:09:57
like that that's like the the dream for Archon to make it so that it is the command center for all context
1:10:03
engineering, just getting you started no matter the project that you have. And a lot of that does rely on us building out
1:10:08
this context engineering hub. But this and Archon are like the two big things
1:10:14
that we have going on in Dynamis. U maybe that like and the AI agent mastery course where I show how to build agents
1:10:20
from start to finish. So, like I said, a lot of really exciting things going on in the community. So, if this sounds
1:10:25
interesting to you, like if you want to dive in and contribute and even just leverage these resources and be a part of the long-term vision for Archon,
1:10:32
dynamis.ai, that's the place to check out. So, I'm going to plug it again because it just relates so much to what
1:10:38
we're talking about here. Um, and everything that we got going on. So, yeah, let me go back and see where we
1:10:43
are at with Claude Code. Okay, so yeah, it's just chugging away like it's it's killing it. Nice job,
1:10:51
Cloud Code. So, yeah. Okay. Um, our application is Wait, is it actually
1:10:56
ready? Okay, I'm going to try this. I I doubt it's going to work first try because I cut a lot of corners to just
1:11:03
like speed up things and show you guys the whole BMAD, but let's try this out actually. This would be so cool if we at
1:11:09
least get some kind of visual here. Uh, let me make sure npm install. Let me
1:11:14
make sure everything's installed first and then I'll try to run it. Okay. npm rundev.
1:11:20
Um, okay. No errors. Oh, that'd be so cool. All
1:11:25
right. Let me let me spin this up.
1:11:33
Uh, okay. So, it looks really bad. It looks so bad. I guess maybe there's
1:11:39
an there must there's probably a tailwind issue.
1:11:44
Yeah, there's a tailwind issue. Okay. So, so the the uh CSS isn't working. It's probably a simple thing, but
1:11:55
help me help me make a million dollars. Create instance.
1:12:02
Okay, that's actually really cool. Um,
1:12:08
okay, so we got another error. Okay, so we got a couple of errors, but like clearly it's like kind of there. Um,
1:12:18
there's two things we'd have to fix. Okay, let's try to fix I'm actually
1:12:24
let's try to fix these. So, I'm going to go back to my claw code and say I'm getting this error for Tailwind CSS.
1:12:33
And then also uh when I start a claude instance, I get this error and it is
1:12:39
stuck on what is it stuck on right now. So I'm just trying to be like kind of specific here. Usually when you're troubleshooting things with coding
1:12:45
assistance, it's helpful to be like quite specific on like when the error is happening, what the error is. So it's stuck on processing prompt this error.
1:12:54
I'm just typing this off camera really quick. So I'm going to copy this. Uh if I go to the issues that we're getting,
1:13:00
uh there we go. If I look at the I forget how to Oh, yeah. Here we go. Um,
1:13:06
I'll just copy the full call stack here. Okay, there we go. So, I'm sending it
1:13:11
in. I accidentally pasted the call stack twice, but it's probably fine. But, yeah, let's just have it lock out these
1:13:16
things and we'll see what we can get. So, I'll just be ready to run it again here. But, okay, that'd be so I mean, we
1:13:22
got like kind of something. and it looks terrible, but um I there's no way I would expect to oneshot this application
1:13:29
even if I spent a lot of time architecting and validating the PRP,
1:13:35
which especially because I didn't like I definitely wasn't expecting it to be great out the gate, but I I feel like
1:13:41
just just with like my intuition and experience with coding assistance and what I was looking at there, I don't and like how specific the errors were, I
1:13:48
don't think we're that far from at least having something pretty cool. Um, okay. I'm gonna try something right now. I'm
1:13:54
gonna try running the server even though it's in the middle of stuff, just because maybe it's to the point now where it's working. Um, oh,
1:14:01
okay. It is. It's kind of It's getting there. This is cool. Okay, now we got a
1:14:06
real UI. So, we fixed the we fixed the stupid Tailwind stuff for the most part. Um Oh, yeah. So, it's just running the
1:14:13
the type checks at the end here. So, I think it is pretty much done. Okay. Well,
1:14:18
yeah, 24-hour stream. Definitely not a 24-hour stream. Um, if you guys uh if
1:14:24
you guys look on my live tab on my channel, I do have a 12-h hour stream from before I really started diving into
1:14:29
YouTube. Um, I'll just leave that there and move on. But yeah. Okay. So, create a new instance. Code review assistant.
1:14:38
Help me make a million dollars. All right. Create instance. Okay.
1:14:45
I don't see any logs and Okay. So 2% right before the auto
1:14:51
compact we finished and it's um view terminal. Okay. So it doesn't look like
1:14:58
it's working. So okay. So I don't know. I don't know
1:15:04
if we're 80% of the way there. Like I said, it's the expectation that especially cuz I rush through some of
1:15:09
the things that it's not going to be like perfect perfect, but like we've got something to start with and Vive coding
1:15:15
is never going to get you 100% of the way there. And we definitely did like Archon helps with structured approach,
1:15:22
context engineering, but what we did today rushing through things was more vibe coding than I'd want to do
1:15:29
definitely. Um, but like I hope that like I explain things well enough like when you'd want to dive in deeper so
1:15:35
that you understand how to not vibe code as well. So it's like let's go through things quick, but I'll speak to like
1:15:40
when you'd want to slow down. I hope that makes sense. And so we definitely could be making this a lot better if we
1:15:46
put more time into it. But yeah, I mean it's it's we've got something working here. All right. So yeah, I think I'm
Final Thoughts
1:15:52
going to go ahead and wrap up the stream now. I've been talking for three hours straight and I think I'm going to take uh most of the day off and and get that
1:16:00
recap uploaded tomorrow. And uh I'll um I'm going to be super active in Dynamis
1:16:06
tomorrow as well and then going into next week. Well, I mean, I always am, but uh yeah, I know that I already heard
1:16:12
from my wife that there's influx of people joining Dynamis, which I appreciate a lot, guys, because we're going to be doing some amazing things
1:16:18
together. So, yeah. All right. Um I'm going to eat some lunch, too. Right.
1:16:24
Yeah. I have not been drinking any water. I have I have my water here specifically so I could drink,
1:16:32
but I I never remember to do that while I'm in a live stream. I always forget.
1:16:37
There was one live stream uh a couple ago that I did. I actually gave myself co like I brought coffee to the live
1:16:44
stream and I remember holding it up at the start of the of the live stream. I'm like here's my NHN mug. I got coffee cuz
1:16:49
we got a a a chill casual live stream today and I'm going to be sipping my coffee and then I sipped it once the
1:16:55
entire live stream cuz I totally forgot about it because I get so into it. Like you guys have no idea how much it takes
1:17:02
like mental effort to be like watching the chat, watching my stream and like kind of checking on viewership and then
1:17:07
like diving into Claude Code or whatever and and like it's a lot but it's really fun. Like it's so worth it. So yeah,
1:17:12
thank you everyone for being here and being a part of Archon. Um as you can see like not perfect right now, but it's
1:17:19
freaking awesome and there's so much more that we got coming really soon for it and a really amazing long-term vision. So yeah, definitely check out
1:17:25
Dynamus if you guys want to be a really big part of it. Um, but also like it's totally public open source project and
1:17:31
we got a public community as well. So yeah, options either way for you guys. But yeah, big things coming for Archon
1:17:38
short and long term. So thank you everyone for being here and following along and your questions and comments.
1:17:43
Hope that you guys have a great rest of your weekend. And with that, I will see