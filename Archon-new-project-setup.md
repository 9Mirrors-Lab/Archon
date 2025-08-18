Okay, there we go. I think my audio is actually working now. I was looking at my uh OBS and it wasn't showing it. So,
0:38
now we're good. Okay. Welcome everyone to the Archon beta launch party live stream. I've been looking forward to
0:44
this all week, all month, all summer because we've been working our butts off
0:50
on Archon for so long and now we have the beta launch and I cannot wait for it. So, yeah. Okay, let me go ahead and
0:56
uh mute my stream on the other monitor there. Cool. So, yeah. What do we got? We got um 28 people watching right now.
1:03
Love to see it. Welcome everybody. This is going to be a fun stream. So yeah,
1:09
I'm going to give a couple of minutes before I dive into the main content for us here. In the meantime, I just want to
1:15
give a warning quickly that there are some really bad thunderstorms that are going on right now where I'm at um in
1:22
Minnesota. So, you might hear loud thunder. I might get disconnected. Probably not. I'll probably be okay. But
1:29
just like a fair warning that I want to give there. Um yeah. And also, I'm curious before we get started, where's everyone uh tuning in from? I'm curious
1:36
if you guys just want to like put in the chat really quick where you guys are at. I'd love to see it just before we get
1:43
started here. So, I've got the chat on my left monitor here and then I'll just be like bringing in things from my right
1:49
monitor as I'm going through different stuff that I'm sharing today and then obviously presenting from my main
1:55
monitor in front of me here. So, that that's what that's what's up. So, if you see me looking around at different places, that's what I'm doing here. Um,
2:01
all right, cool. We got um UK, Germany, London, St. Louis, nice. Nice. Egypt,
2:08
Portugal, Oklahoma, Jersey, Baltimore, Hong Kong, Austin, Texas, Spain. Oh my
2:14
goodness, it's so cool. Okay, I I do this. I ask for, you know, where everyone's at last couple of live
2:20
streams and yeah, the thing that just amazes me every time is how global we
2:26
are as a community. It's super cool. So, thanks guys for for sharing your location. Uh, and by the way, I have it
2:33
set up so I can showcase any given message. Um, and so I'll do
2:38
that just as I like answer questions throughout the the live stream today. So I can show any of the the questions.
2:45
Colorado Springs, home of Skynet. Love it. Baja California. Nice.
2:54
Holland. I'm not going to like showcase every single one of them here, but I'm just showing you guys that I can do that. Also, the other thing that I have
3:00
is I can show the chat on my screen as well. And I got some feedback in
3:05
previous live streams that it was kind of distracting. So, I think I'll mostly have this off here. Um, but the main
3:10
thing is being able to show the featured message. So, that's what I'm going to go ahead
3:15
and and do just as we got some questions coming in. Um, so yeah, with that I want
3:21
to really quickly talk about the plan for the stream today and just like the
3:27
general structure for it and then I'll share my screen and we'll just dive right into things. So first of all, this
3:33
is going to be a pretty casual stream. I'm going to be kind of like leveraging Archon as you would as a new user just
3:41
getting used to the platform, figuring out how you want to integrate it in your own AI development workflow.
3:47
And uh maybe I can actually go ahead and share my screen and show you guys what I mean by that. So I'm going to let me
3:54
take care of this quick. Go and share my screen. So I'm going to swap my
4:04
Okay, I think my audio. So I had to fix my audio in the new scene here. So yeah, you all should be looking at my screen,
4:10
which I need to fix this so that it shows the full thing. Okay, there we go. We're doing some adjustments live, but
4:16
that's all good. Okay, cool. Now you guys can see my full screen. Okay, so what we're going to be doing today is
4:23
you guys hopefully saw the launch the beta launch video for Archon on Wednesday. Now, I want to dive deeper
4:30
into using Archon. We're going to be building something from scratch. I'll talk about how we can use Archon in
4:36
existing code bases as well. But I want to start by showing you guys kind of talking about what Archon is all about.
4:42
uh just to sort of recap some of the things I talked about in the the launch video on Wednesday. Then I'll I'll
4:49
quickly show like how you can get it set up. We'll poke around the user interface a little bit. I'll show like how you
4:54
connect it to your AI coding assistant with MCP. Then we'll get into using it
4:59
and to kind of more simulate what it'd be like for you guys to play around with it for the first time. I'm going to be
5:06
using Archon in a development workflow that I'm not very familiar with myself. So, we're going to be doing some
5:12
freestyling in this stream. It's going to be fun. And so, the development workflow that we are going to be
5:17
covering in this stream is the BMAD method, which by the way, it is insane
5:24
how many comments I get from you guys in my videos and in the Dynamis community asking for me to cover BMAD. So, there's
5:29
a lot of love for this. It is a really, really cool framework. Um, just one of the methods that we have for context
5:36
engineering. So, I cover the PRP framework a lot on my channel. Um, I've
5:41
talked about the spectriven development that we have in AI idees like Curo. BMAD
5:46
is another method for context engineering. And so, we're going to be integrating BMAD with Archon in this
5:52
stream. And I've done a little bit of prep just to make sure I understand how BMAD works overall, but I haven't used
5:58
it ever to build a project end to end. And so, like I said, very much freestyling. I'm going to be playing
6:05
around with how I can integrate Archon with BMAD with you guys live so that you get a sense of if you're integrating
6:12
Archon into your development workflow. What does it look like to just poke around and experiment with prompting and
6:17
using the Archon MCP to really build it into what you're doing already? Like everyone here has an existing process or
6:24
at least you're starting to get yourself introduced to using coding assistance. And so I want to make it really easy to
6:30
see how Archon can fit in no matter what you already are doing for your AI
6:35
development workflow. So that's what we're going to be doing and it's going to be fun. So the first thing that I
6:41
want to talk about before we get into this is just you know what Archon is about. And so I'll I'll dive into that
6:48
in a second. And I guess the the last thing that I want to say here before we dive into things is
6:53
um there might be a lot of like let's just dive into things and and get things
6:58
to work. It's going to be kind of scrappy. It's going to be fun, but I don't know for sure if we're going to have something working end to end by the
7:04
end of this live stream because more of the point is diving into how we can experiment with integrating Archon into
7:10
our workflow versus like let's fully build something end to end. Like I don't have the live stream structured in that
7:16
way and I'm doing that intentionally. um for the reasons that I've already been talking about. So I don't I don't want to repeat myself here. The the one thing
7:22
I'll say though is if you're interested in seeing my full development workflow in a much more structured way talking
7:30
about context engineering and archon and how I use it in my workflow. Something
7:35
really exciting that I've got going on um in the Dynamis community and let me I'll actually uh bring this over from my
7:42
other monitor here. I'm hosting a half-day workshop, a 4hour workshop.
7:48
It's going to be at the end of this month, Wednesday, August 27th. And this is where I'm going to dive into a much
7:55
more structured approach. So, it's going to be a lot different from this live stream. Like, this live stream is going to be more casual. We're just building
8:01
things, freestyling together. I'm going to be answering a lot of your guys' questions in the chat throughout as well. But, this workshop is going to be
8:08
a lot more structured. like I'll dive into my full AI development workflow and we're going to build something from scratch using PRPs and archon. A lot of
8:16
the things that I've been covering on my channel is going to be in this very comprehensive workshop. So, if you're
8:22
interested in this, like my goal is to make it so that this this workshop alone is worth the investment of Dynamis. And
8:28
so, uh yeah, I just wanted to mention that really quickly cuz it's it's very much like related to like here's what
8:33
you'd want to do if you like what we're diving into in this live stream and you want something that's a lot more structured. So definitely check out
8:39
Dynamus also because the prices will for Dynamis are going to increase after um this weekend. So this is like the
8:46
special Archon beta launch weekend and then prices are going to go up after. So I just wanted to mention that quickly. U
8:52
but for our workshop right now, we're just going to have a really good time. And so yeah, let's go over to the Archon
9:00
repo here. And I'm going to be answering questions in the chat um as they come up as well. So, actually, I'm going to take
9:07
a second here and I'm just going to like read through some of the things that we've got in the chat before we
9:12
continue. So, um yeah, I'll have basically I'll have time for Q&A as
9:18
we're waiting for Claude code to finish certain things like we'll get into the BMAD method and we'll start like
9:24
planning our our um solution and architecting it and everything. And so, I'll have time to like look at the chat
9:29
as we're waiting for things. So, it's going to be a really smooth stream in that way because there's natural breaks in the the actual like what I'm
9:35
showcasing for you guys. Um, cool. Coding with cloud code plus
9:42
archon now and it's a game changer. I appreciate it. Yeah, we're going to be using cloud code in this workshop. I'll
9:47
talk about how we can use other coding assistants as well. Um, but yeah, cloud code is is a beast right now.
9:54
I have to know who came up with the name Archon. Someone should really look at at that up. Um, I came up with the name
10:01
Archon. So, I'm curious like why you're asking, but yeah, I thought Archon was a cool
10:07
name because um, it's Greek for something. I actually forgot Archon Greek. It means something u, yeah, it
10:14
means like ruler or leader. U, because it's like we like you think of archon as
10:20
like the operating system for AI coding assistants. Like that's kind of like the catchphrase that I've started to um use
10:26
to speak about Archon. And I mean maybe there's like more accurate ways to describe exactly what it is, but it's
10:32
just like it's nice and catchy and it's concise. Like it's the operating system for coding assistants. And so it kind of
10:38
dictates how we manage knowledge and task for our coding assistants. So it's like the ruler of our context
10:45
engineering setup, so to speak, right? So like that's kind of where the name comes from. And back when I had it as
10:50
like the AI agent that builds other agents, well, it's kind of like the main agent in that way. So that that's kind
10:56
of part of the the inspiration for the name as well. Um, part of the Dynamus community.
11:02
Honestly, say I've gotten a ton of value out of it. I just mailed my first agent out of Pantic AI. Congratulations.
11:07
That's really cool. I appreciate it. Thank you for the the kind words on Dynamus. Um, so yeah,
11:16
love that I'm vibe coding right now as I'm watching. Cole, sweet. Hopefully you're using Archon.
11:22
But yeah, it's it's really nice. Like, by the way, just using AI coding assistants in general, something that I
11:27
love about them is, sure, it can be slow as you are waiting for it to output the
11:33
next uh changes or implementing the next feature, whatever it is. But it's really easy to multitask then. Like you said,
11:39
you're watching the live stream as you're vive coding. I'll I'll be like in the Dynamis community responding to things cuz I'm I'm active every single
11:46
day in the community. But I'll like be doing that like as I've got Cloud Code running in the background and then it'll finish and I'll go over and like have it
11:53
do the next thing or maybe I'll like validate what it outputed and ask it to correct some stuff and then I'll just go back to what I'm doing. So I'm really
11:59
I'm able to be efficient with my time. So even if it takes like three or four hours for Claude Code to get through
12:05
that like next big thing I'm working on, I only actually have to be dedicating my attention to it like a half hour out of
12:10
that full 3 hours, right? Uh it's really nice. So yeah. All right, let's go ahead
12:15
and uh dive into Archon. So it is the operating system for AI
12:21
coding. And so what that means is it's the command center. So for us, it's a
12:27
sleek user interface. Like if I go to the project management for example, we've got a sleek user interface to
12:34
manage all of our tasks. We've got a place to manage the knowledge that we want to give our coding assistants. So I
12:40
can perform rag to like actually search through the pyantic AI documentation or the cloud code documentation. So it's a
12:46
UI for us to manage everything. And then for the coding assistant, it's an MCP server. So it's kind of like leveraging
12:53
what's native to humans and what's native to coding assistants. So we all can work on the same set of context as
13:00
we are context engineering. That's the beauty of it. And it's possible to connect it to any AI coding assistant
13:07
that supports MCP. And so we have instructions if I go to like the MCP server tab. And I'll talk about how you
13:13
can get this all running in a second by the way. Uh but like we have a tab for all the popular coding assistants. And
13:20
um really just to keep the UI concise, we didn't include like 20 different coding assistants, but you can connect
13:25
this to every single coding assistant basically. So we have instructions for popular ones like Klein and Claude Code
13:31
like we'll be using today. I'll actually copy this command right here. So this is the command that you run when you have
13:38
Claude installed to hook in the Archon MCP server. And um actually maybe I'll
13:43
actually just go ahead and do that right now. So I've got my terminal open. We're going to be living and breathing in this
13:48
terminal today as we do our demo. And so to add the archon mcp after I have it up
13:53
and running, I just have to run this command. Like it's that easy. And I already have it running, which is why I
13:58
get this message right here. But if I do a claw mcp list, then it'll check and even validate the connection to archon.
14:05
So that's how easy it is to get it connected once you have the UI up and running. And I I cover instructions for
14:11
like how to set up everything in the video that I put out on Wednesday. But really, if you go to this link, so you
14:17
can just go to the Archon GitHub repository. Also, if you just go to the URL archon.diy,
14:24
this will take you to the GitHub repository as well. So, I have a a URL that just like redirects you right to
14:30
the to the GitHub repo, so it's really easy for you guys to access it. Um, so yeah, just archon.
14:37
Why? And then in the read me here, I have your quick start instructions. So, super super easy to get started. There
14:44
are a couple of things that people have been tripping up on that I want to address really quickly. Uh because honestly, like if you guys want to
14:49
follow along in this live stream as I start using Archon, I'd welcome it. Um and so, yeah, prerex, you just need to
14:54
have Docker Desktop. Uh you need a Superbase account. You can the free tier works like you don't have to pay
15:00
anything to use Archon. Um or you can even use local Superbase. So like if
15:06
you're following along with my all my local AI stuff and you have the local AI package up and running, you can use that
15:11
superbase. Um and then also you just need your API key for OpenAI. We also
15:17
support Gemini and Olama. So Olama is kind of more experimental right now. It's in the works. U but we are we have
15:24
actually an active effort on that with a PR coming into Archon soon as well. And
15:29
that's kind of the other big preface I want to give for Archon is like when I say that it's in beta like there there are things that are like not working
15:36
100% at this point and there are more experimental parts of the platform that
15:41
um we have like things that are saying coming soon or it just does like it needs to be tidied up. We're working on
15:47
that. Like I'm I'm putting in a lot of my effort a majority of my effort into archon and everything related to context
15:54
engineering that I have like kind of playing into archon. So yeah, these are the prerexs and then you just have to
15:59
clone the repo and then set up your environment variables and really it's just you have to get your superbase URL
16:05
and service ro key and maybe I could actually show that really quick as well. I feel like that'd be useful just for
16:11
the people that have been tripping up. One thing that I've been seeing a lot is um people are using their anonymous key
16:18
in Superbase instead of their service ro one. And so I'm just going to bring over my superbase here and show you what I'm
16:24
talking about. So, I have a just like a basic $10 a month micro instance set up for a lot of the testing I've been doing
16:30
with Archon. You just go to your project settings in Superbase. And when you go to the API key section, you just reveal
16:37
and copy the service role key. So, that's the key that you put into the environment variables for archon. And
16:43
then for the data API, you get your URL here. And then you can do a similar thing for uh self-hosted superbase. You
16:50
just get your values from the environment variables. So, not to dive too much into the setup right now just
16:55
because I covered that in the video on Wednesday already, but I wanted to at least call that out cuz a couple of of
17:01
uh issues have been created around that. Um, so yeah, and then once you have your
17:06
environment variable set up, you can set up your database. And so within the migrations folder, I've got a single
17:13
script that you can run. You can copy this script, go into your Superbase SQL
17:18
editor, and you can create a new snippet, and then you just paste this in and run it. So, this is going to create all of the archon tables for managing
17:25
your knowledge and your tasks and your documents. Uh, very, very easy setup. And then I'll go back to the readme here
17:32
u because then the last thing is to build spin up the containers. So, you just run this docker compose command. We
17:37
got docker as one of our prewax for this. And so you run that and it'll spin up all the containers and then you have
17:43
everything running for Archon. And so what that'll look like in your Docker desktop is you'll have four containers
17:49
running under the Archon umbrella. We've got our agents which this is a feature that is more coming soon. But then we
17:56
have our MCP server, the user interface that we've already been looking at a bit, and then we have our server that has all of our API endpoints so that our
18:03
UI can interact with everything that the MCP server can for our coding assistant.
18:09
So that's what the setup looks like. And then if you go to localhost port 3737, that'll take you through an onboarding
18:15
flow where we have you set your OpenAI API key. Um or you can just skip past
18:21
that and then go and set your uh Google API key. So we support Gemini as well. And then Olama, like I said, is
18:27
experimental coming soon. So a lot of things that we're working on that are coming soon. Um it's like things like
18:33
Olama. So yeah. Uh, and then once you're in Archon and you have everything set
18:38
up, this is where the fun begins because this is where we can start to scrape knowledge and get our global rule set up
18:43
for Archon. This is where the fun begins. And so, yeah, um, to start, I think now is a
18:52
good time. I'm I'm going to kind of like treat this as if I'm using Archon from scratch. So, I have some things that are
18:57
crawled already that I'm going to be using in the the demo today, but I'm
19:03
going to act like I don't have that. And so, I'm going to start from scratch, talk about like what we're going to be building, and I put a lot of thought
19:09
into just having like a really cool use case for you guys. And then, we'll get into the BMAD method. We'll actually
19:14
start more with BMAD and then start seeing how Archon can play into it because I want to show you guys how your
19:19
existing strategies work with Archon. So, what we're going to be building today is going to be something kind of
19:27
like this tool. So, if you guys haven't heard of Claude Code UI, and there's a
19:32
lot of tools that are like it, it's basically a user interface. So, like in mobile and on the web, we can manage
19:39
different Claude Code instances. And so, I'll open this image in a new tab so you
19:44
guys can see kind of like like what what I envision creating. And again, we might not like have an end result that looks
19:50
like this by the end of this stream because I want to focus so much on like answering your guys' questions, talking
19:55
about Archon, and integrating with BMAD, but we might get something kind of like we'll see. But this is kind of what I'm
20:01
envisioning here where we have a user interface. We'll build a website with Nex.js JS where we have just like an
20:07
easier way to manage the our cloud code instances and we'll use the cloud code SDK that they offer so that we can build
20:14
our own application that is invoking cloud code and we can manage um the
20:19
different instances at the same time. We can see like a log of the terminals that we have open and all the work that
20:26
they're doing which is also going to be a cool way to manage sub aents by the way within quad codes. you can have them
20:31
all running at the same time and managing them separately and like having that integrated with Archon as well. So
20:36
like this is kind of just to give you guys like a rough idea of what I'm envisioning here, what we're going to create together. Um just to give you a
20:43
demo of BMAD plus Archon and yeah, Cloud Code UI is not a tool that I've actually
20:48
tried myself. I've used other similar ones, but I just found this one recently and I thought that this was like a they
20:54
just had nice screenshots showing what it looks like. So, I thought it'd be a nice way to give you guys a visual of
20:59
what I'm hoping to create because obviously I can't give you guys a demo of something like I do in my YouTube videos because in my YouTube videos,
21:05
I'll fully build it out first, then I'll record basically like recreating it. So, that way I can like give you guys a demo
21:12
up front and then create basically a replica so you see the full process. So,
21:17
that's what it looks like in something a lot more structured like a YouTube video or like that workshop that I have in Dynamus coming up here. Um, but then for
21:24
this live stream, we're just freestyling. So, that's what I want to create. So, all right. Now, we can dive
21:31
into BMAD. And, uh, by the way, once we start using BMAD, that's when we'll have
21:37
more natural breaks for me to take a look at the chat here. So, I have the chat on my left monitor. I see that it's
21:44
going crazy. I appreciate all you guys being here and commenting. So, I'll definitely be diving into uh some of
21:49
your guys's questions once uh we got some things running in cloud code. So,
21:55
let's start with a little intro to BMAD and then once we start looking into how we use it, that's when we'll really
22:02
start to see archon play into it in a way where like I think you guys will be able to use your imagination to see how
22:09
archon can fit into any AI development workflow. So BMAD it is the foundation
22:16
of agentic agiled driven development and um yeah actually I think 125% is a good
22:21
zoom here. So I'll stay at this level of zoom. Um so there's kind of two main
22:27
workflows that we have with BMAD. Essentially what BMAD gives us is a bunch of different sub aents that are
22:33
experts at different parts of our development workflow. So like in the agentic planning workflow, we have our
22:40
analyst, we have our project manager, we have our architect, and then when we go into development, we have our scrum
22:46
master agent that's kind of guiding all these different development agents to knock out the different stories like the
22:53
different tasks that we have for developing our project. And there are some diagrams that we have in the user
23:00
guide here um that walk us through what this workflow looks like. And yeah, so
23:05
the the BMAD method in general, it's like I said, it's a strategy for context engineering and it gets pretty in-depth.
23:13
Like these workflow diagrams, like these mermaid diagrams, they look kind of
23:18
intimidating. Like there's a lot that goes into this here. So um yeah, by the way, like this first one is the planning
23:26
workflow. And we're going to walk through this and I'll show you how to integrate Archon with this. It's not as complex as it looks. This is the
23:32
planning workflow. Then once we get into development, we have this second
23:37
workflow, which I might go through this one or I might actually switch to PRP. Um, we'll see. Like I said, we're
23:43
freestyling here. So, two different workflows that we have for the BMAD method. And the guy that created the
23:50
BMAD method, he he's a genius. Like, he's very, very smart. And he's actually
23:55
got a YouTube channel where he started covering BMAD. I went through his entire 1 hour and 15 minute master class that
24:00
he had on YouTube. By the way, if you just search the BMAT method, you'll find him. Um, but yeah, he's done so much
24:06
research into project management and best practices for architecting and different like mental models that we can
24:13
apply to planning projects. And he's done a ton of research into best practices for prompting at different
24:19
stages of our AI development workflow. And he talks a lot about that in his master class as well. And so I I just
24:26
think this is a great use case. So like apply BMAD with archon. And the other thing that he talks about is the whole
24:33
idea of um green field versus brownfield projects. So a green field project, you
24:39
can think of it like fresh green pastures. This is a new project that you're starting from scratch. And then
24:44
brownfield is when you're working in an existing codebase. And the BMAD method has different workflows depending on if
24:51
you're working on an existing codebase or not. And I know that that's something that um a lot of you guys like in
24:56
comments in my videos and in the Dynamis community have said like I want to see more of like let's use
25:03
AI coding on an existing project versus something that is green field. And so
25:09
generally I focus on green field new projects just because it's a lot easier
25:15
to show how I apply different strategies. And it's going to be the same in this live stream. on creating
25:21
something from scratch because going through the full planning workflow, it's much easier to integrate Archon and show
25:27
the different parts of Archon when we're doing a lot more of that like initial research and task management. Um, where
25:32
we're it's going to be a lot more sparse if we're just like adding new features on an existing codebase. There's going to be less tasks overall. There's going
25:39
to be less research that we have to perform with Archon and like all the knowledge that we have for Rag because
25:45
it's going to be more looking at the existing codebase versus looking at documentation. You see what I'm saying?
25:50
Like brownfield projects, it's more let's reference the existing codebase to figure out the patterns that we need to
25:56
develop. With a new project, it's let's look at the documentation for Pantai, for example, to figure out the patterns
26:04
for developing agents that are that's recommended for this library. So that's why we're going with green field here.
26:10
But yeah, so let's let's go ahead and start actually. So let me go to VMAD. We'll go to the quick start here. Let me
26:18
do a time check as well. Okay. 25 after um
26:24
Okay, I I'm going to look at the chat quick before I
26:30
um continue. Let's see. Archon is amazing. The UI is
26:36
clean. Appreciate that a lot. Really want to see this work with an existing BMAD project. Yeah, I mean I'll be I'll
26:42
be speaking to that like I'll we'll do like the like a help command that we have for the different sub aents in BMAD
26:47
and I'll show you like how you would do things a bit differently for a brownfield project and I've already kind of talked about it as well. Like the
26:53
main thing is for context engineering on an existing codebase you're referencing a lot of your existing codebase for like
26:59
best practices and architecture versus with a new project it's more documentation that you upload or you're
27:05
crawling like what we're doing with Archon. So, uh, my OpenAI bill ended up being 3K.
27:13
That is unfortunate. That's not from Archon, though. Um, if you're saying that's from Archon, that's
27:19
not true because we don't uh we're never going to do anything with your API key. And it's stored, all the credentials for Archon are stored encrypted in your own
27:26
database, your superbase. So, yeah.
27:32
Um, okay. I I realize there's some drama going on here. Um,
27:39
I'm going to I'm going to move past that. All right. All right. I'm just going to move past that. Uh, oh, Sean's popping
27:45
in. What's up, Sean? Let me go let me go to this. Where is it? Was a great master class. I appreciate it, Sean. Thanks for
27:51
being here. So, Sean is one of the other maintainers of of of Archon. He's the one who built the beautiful user
27:57
interface that you're looking at right here. So, yeah, thank you, Sean, for being a huge part of Archon and doing amazing things. I would not have been
28:02
able to build this in user interface that you did.
28:11
All right. Oh. Oh, yeah. Yeah. One thing that I I appreciate you bringing this up, Nicolay, uh adding support for open
28:17
router. I saw there's a PR for that. I really prefer open router over all providers. Yeah. So, one thing with
28:23
archon is it relies a lot more on embedding models than large language
28:28
models. most of the things that we do with rag and I'll actually show this by the way guys um for crawling here we for
28:37
the knowledge that we want for this project we're making this like let's manage cloud code instances in a UI we
28:44
probably want the documentation for cloud code so we know how to use the cloud code SDK to interact with cloud
28:52
code from our NexJS application and so I can actually take this link right here.
28:59
This is actually what I already have um scraped. And so I'm just going to do a recall here so you can you guys can see
29:04
what this looks like in action. But I go to the knowledge here. I paste this in. And Nicollay, I'll get to your question in a second. Don't worry. Um well, I
29:11
just realized that this is like smashing. You can't guys can't even see my face right now. Um
29:17
let me move this. No, it's it's fine. Um it's all right for now. Uh anyway, so I add in the URL
29:25
for cloud code. I want to scrape this documentation. And you click add source. Now, I'm not going to do this here
29:31
because I already have it crawled. So, I'll just do a rec crawl so you guys can see what it looks like.
29:37
And so, what it does behind the scenes is it uses crawl for AAI to recursively
29:43
navigate through all the URLs that we have. So, it starts with one URL and you see that it moved all the way up to 40.
29:48
Excuse me, it moved up to 45. So, it found all the URLs. It's crawling them in batches of five. You can see the
29:53
progress going up right here. And then it's going to with some more advanced chunking strategies that I have
29:58
implemented behind the scenes. It's going to use an embedding model to chunk up and uh create the vectors for all of
30:05
the documentation that we've crawled here with crawl for AAI and we're storing that all in our superbase database. So we're using PG vector uh
30:13
for semantic search and storing the embeddings. And it's really cool how we can watch in
30:18
real time the progress of the crawl here. And we also have a gentic rag. It's extracting code examples as well.
30:24
So, we're giving like a couple different ways for Archon. Like with our AI coding assistant using the Archon MCP, it can
30:30
search through the documentation in a few different ways. Like it can just look up the raw docs with a search or it
30:36
can look at the code examples. It can search through the code examples that we're extracting as well. So, it's an implementation of a gentic rag where
30:43
there's multiple different ways that our coding assistant can search through what we've crawled. And so, all that to say,
30:50
I just wanted to to show you guys an example of that. All that to say, nicicolay for open router, it is a
30:56
fantastic platform, but they don't have embedding models. They only have large language models. And so, the reason that
31:02
we started with OpenAI, Gemini, and Olama is they are the three most popular providers that have both LLMs and
31:09
embedding models. And so, like right now, I'm using um text embed 3 small
31:14
from OpenAI. That's what's doing the the chunking here. And then for the large language model to extract code examples
31:20
and provide summaries, I'm just using GPT 4.1 nano. So it's just like a super cheap and lightweight model. This entire
31:26
crawl, by the way, guys, is like a tenth of a penny or less for everything. Like
31:32
it is so so cheap. Everything you do in Archon because it's all like embedding
31:38
models are incredibly cheap compared to LLMs. And then our usage of LLMs here is very light and I'm able to do everything
31:44
with just GPT 4.1 nano or you could use like GPT5 nano. So there we go. We're
31:50
crawled. We've got the docs. We can look at the code examples that they have here which aren't really the best for cloud
31:56
code. If I were to go to like pideantic AI, it looks a lot better. Like we can see like full code examples that we've
32:01
extracted from the documentation here which is just so cool. And we can see this all in the UI of Archon. It's a
32:07
beautiful thing. Um, so yeah, what we're planning on doing, Nicolet, um, I need
32:12
to remove the message here. What we're planning on doing for Open Router in general, we want to make it so that
32:19
you can set your LLM provider separately from your embedding provider. So that way you could use Open Router for the
32:25
LLM and then you could use OpenAI or you could use Olama for your embedding model and you would just set those things
32:31
separately. So we're working on the settings quite a bit and making changes like that. Also just making it easier to
32:36
configure things like having a automatic dropdown for the models that are available versus you having to type it
32:41
yourself. So we're working on a lot of things like that. So trust me guys there are a lot of features that are coming soon for archon. So yeah we've got our
32:49
documentation crawled for uh the cloud code docs and then I also because we're building a nex.js application I took the
32:57
llm's full dash or llm-full.ext from nex.js and I crawled this as well.
33:04
Now, this one takes a little bit longer. There's a lot of text here. If you can see my scroll bar on the right hand side
33:09
of my screen, this is a lot of information. So, it took a while to crawl it. And so, to save you guys from
33:15
having to go through that and we already saw crawling the cloud code docs, I have this crawled already. So, we we have 471
33:22
code examples that we have pulled from the docs here. So, we've got all of our knowledge primed for cloud code and
33:29
nex.js. And we'll start to see this in the BMAD method in a second here. will leverage this documentation even in the
33:35
planning process. So going back to BMAD here, I'm going to copy the command to get
33:42
started. And so it's super super easy to get BMAD started in any project. Um, all
33:48
you have to do, and I mean I've already run this, and so I'll probably just do it on a new folder, show you guys what
33:54
it looks like, and then I'll go back to my current folder where I already have BMAD set up. I think that'll be the best
34:00
way to do it. So, let me go and get things set up in a new folder here. Okay. All right. So, I take that command
34:06
from the repo. It's just npxbad method install. Super easy. And it's going to install the following packages. That is
34:13
good. All right. BMAD method. And then the first thing you want to do is enter the full path to your project because
34:20
essentially what BMAD will do is just it's going to install a bunch of
34:25
configuration and sub aents like a lot of different markdown files to get us set up with BMAD in our codebase. So
34:31
this can be an existing codebase that you install BMAD into or in our case it can just be a brand new folder. And so
34:38
I'm going to pass in a path here. I'll call it uh BMAD example.
34:45
There we go. And then I'm going to install the full system here. And uh
34:50
will the PRD product requirement document be sharded into multiple files? Yes. Is the default. Just go with this.
34:56
PRDs. By the way, guys, this is like the document that has like a very fully
35:01
written out spec of what you want to create. So when we plan our initial
35:06
implementation, we put that in a PRD that we'll then use to break into tasks and start implementing. And we'll see
35:12
that in action as well. So I'm going to say yes. Will the architecture documentation be sharded into multiple
35:18
files? Sharded just means split up to make things more concise by the way. So yeah, now we get to pick the IDE that we
35:24
want to configure because based on the coding assistant, there are different ways that we need to set up our global
35:30
rules and set up our sub aents, things like that. So I'm going to pick cloud code. So select with spacebar and then
35:37
confirm with enter. You can install this in multiple ones, by the way, but uh I'm just going to go ahead and put this in
35:42
cloud code. So, there we go. Enter to confirm. Uh pre-built web bundles. I
35:47
don't really care about that. So, I'll just select the default. And then it says the directory does not exist. Would
35:52
you like to create the directory and continue? I will say yes. There we go. All right. Boom. Super super quick. So,
35:59
there we go. We have everything created. So, it created some agents for us. So, we have these different commands that we
36:05
can use to invoke these sub aents. So like for example when we are first starting our project and we'll see this
36:11
in a sec when we want to start planning things we'll call into the analyst agent that BMAD gives us and we'll use the an
36:18
the analyst will actually leverage archon to crawl through the documentation for cloud code in Nex.js
36:24
JS to help us create some kind of more like initial pseudo code like that first
36:30
layer of like okay let's think about generally how we want to structure the codebase and we'll actually use archon
36:36
with the analyst to do that and then the analyst is going to output a brief like a project brief that we're going to
36:41
store as a document in a new project in archon so that's kind of a little teaser for what we're about to do here um but
36:47
yeah whenever we do this and we create a new setup with BMAD I'll open my VS code
36:52
and I'll show you really quickly what this looks like in general. So that's going to create this uh BMAD core
37:00
folder. So this this works on an existing project as well. It's not going to like overwrite anything in your codebase. It creates a new folder where
37:07
we have our different agent teams, our agents. We got the core user guide here.
37:12
These are all the files that are going to be referenced by our agents as we call upon them in our development
37:18
workflow. And so like here's the markdown file for the analyst agent for
37:23
example. And so yeah, basically like we have each agent starts with an activation notice.
37:30
So it's like when we call upon the analyst agent, here's what you got to do and then here are the steps that you
37:37
have to follow to act as the analyst agent. So when we tell Claude code or
37:43
cursor or windurf whatever to act as this agent, it reads this file and then
37:48
basically uses these instructions to change its persona. That's how we're doing. So it's not the BMAD doesn't
37:55
actually use like the slash agent feature in cloud code. And the reason for that is it's more of like a general
38:01
implementation so that you can use basically sub aents as prompts in any
38:06
coding assistant. Even the ones that don't have sub aents built into it. And so yeah, sub agents, if you guys didn't
38:12
know, sub aents, even in cloud code, it's really just prompts. like you have some file that you tell Claude code to
38:19
look at and you say read the instructions here to act as this persona. That's all we're doing here.
38:25
And so we're telling it that like you your name is Mary, you're a business analyst. Uh here is your role and your
38:31
style. Here are your core principles. And then here are the different commands that a user can invoke. Like we have our
38:37
help command. We have our command to create our project brief, which is one of the first things we're going to do. So that's essentially how BMAD works is
38:44
we have all these different agents that are fit together in this workflow that I was showing you guys in the mermaid diagram earlier which was um if I pull
38:51
that up quick I'll just reference that for you guys again. Um that is this diagram here. So the
38:57
analyst is at the beginning here and so we can go ahead and invoke this. And so let's let's just dive right in. So I'm
39:03
going to clear and then I'm going to enter in a cloud. And by the way cloud MCP list remember we've got archon
39:09
connected already. I showed you guys how to do that. Maybe I didn't kind of do it in the right order. Like I showed you how to connect Archon, then I went
39:15
through like setting it up, but yeah. So, we we we connected it with um this command right here, assuming we have
39:20
everything up and running. The MCP for Archon is on port 8051 by default. And
39:25
you can configure that as well if you want. So, yeah, we'll jump into a cloud session here and let's get right into
39:31
it. And so, I've I came with a little bit of prep. Um so, I know some of the commands that
39:39
I want to run here. So, I have that referenced on my other monitor here just to try to make this smooth. Um, though we are mostly freestyling like I haven't
39:46
done that much. And so, the first thing that we want to do is if you just do slanalyst and then you press tab, we're
39:53
going to start Mary as our analyst and it's going to help us create our brief
39:59
for the project that we want to create. So, there we go. Slan analyst. Hello Mary, your business analyst. Specialize
40:04
in blah blah blah. And then type help to see my available commands. So we can do star help and then Mary is going to be
40:10
prompted to give us the commands that she has everything that we had in the um that markdown file that I showed you.
40:18
And while she outputs that, the other thing I want to show you guys, if I go back to Archon here,
40:25
we have the global rules that we want to create for Archon. So in the settings,
40:30
and you're going to want to do this whenever you use Archon, we have the IDE global rules. And so based on if you're
40:36
using cloud code or not really there's just like special instructions for cloud code that we have and then the rest of
40:41
your coding assistants can use the same rules here. You can just copy the cloud code rules and then you can either
40:49
create a new cloud MD and paste these in along with the typical global rules that
40:55
you use or if it's an existing project where you already have global rules then you'll just paste in the instructions
41:01
for archon along with everything else that you already have. So whether it's your cloud.mmd or your cursor rules or
41:07
your wind surf rules, this is just part like this is the part of your global rules now for archons. You can add this
41:12
in with any of your other existing global rules. So I just wanted to call that out really quickly because I have that set up in this repository already
41:19
or this folder already. Otherwise, I literally just have my global rules and then everything for BMAD and then some stuff for PRP that we'll get into
41:26
towards the end here. So that's what I have set up right now. So going back to the terminal here, here are the commands that we have for the business analyst.
41:34
And so uh we can create a project brief. We can go into YOLO mode, which I I saw
41:40
someone in the chat was asking about YOLO mode. Um YOLO mode is instead of
41:46
like it working alongside you more to plan your project, implement your project, it it operates more
41:51
autonomously. So if you want to just trust it more with the implementation, that's what YOLO mode means. We're going to do some of that here because I want
41:57
to be pretty concise in going through the BMAD method here. But the first thing that I want to do is I want to
42:05
brainstorm. So I'm going to use the brainstorm command. So you do like uh star brainstorm. So the star is just the
42:12
way to like signal that we were invoking a command here. That's just the convention for BMAD. We do star
42:18
brainstorm and then we just send in a prompt for what we want it to research. And so what I want to do, I have this
42:25
pre-selected just so you guys don't have to see me type it out here. I want to create a Nex.js front end where I can
42:31
spin off and manage different cloud code instances through the cloud code SDK. And I'm speaking to the specific pieces
42:38
of technology, cloud code and nex.js that I have the documentation for in archon. And so we'll see in a little bit
42:43
how I'm actually going to ask Mary to reference the documentation through Archon so that we can get a better
42:51
planning. Basically just get a better brief outputed. So all right, she's
42:57
going to do some brainstorming for me here. Um, and let's see, there's one
43:02
other thing that I wanted to cover. Uh, yes. Okay, so I'll show you guys really
43:07
quickly. So, exactly what we walk through here. It's going to be kind of similar to this project that I have in
43:14
Archon. And so, I did a little bit of testing ahead of time. Um, so we have
43:20
this project in Archon where we have all these different tasks. I actually had one of the sub agents in BMAD make
43:25
these. It's not the same process as what we're going through right here, but in the docs tab, the docs in Archon is one
43:32
of the more experimental things that we don't have super tidied up at this point. But what you can see here is like
43:38
the project brief that we're about to create with our business analyst. We're
43:43
actually going to store this in archon. So the beauty of archon is it can be our place not just for task management and
43:48
knowledge like we've been covering but also our place to manage documents and share it with our team. Like you can
43:53
actually have your superbase instance that you have many different people
43:59
pointing to with their archon instances. You guys can share tasks and share documents and we can have our coding
44:04
assistant upload the brief here and then pull it later to go and create the PRD. We'll see this in action in a little
44:10
bit. Um, so yeah, I just wanted to show that quick. And then going back to our business analyst, we are we're done. So
44:17
we have our output here. Technical architecture considerations. We here's our front-end stack. Here's our backend
44:23
requirements. So we're just doing a little bit of the brainstorming initially for what needs to go into our project. That's what our business
44:28
analyst did. So there we go. So now there's quite a few different things that we can do
44:34
after the brainstorming just based on those same commands that we saw when I did the help command earlier.
44:40
And so what I want to do is I want to do a uh I want to create a project brief.
44:45
So I'm going to do create project brief. That's just one of the commands that we
44:51
have for the analyst. And I'm going to say, well,
44:57
let me see. Um, oh, no, sorry. I can just say two. I want to do command
45:03
number two because instead of Yeah, like it it's I'm just going to like go through the flow that it's walking me through here and just kind of trust it
45:09
more. So, I'm going to say two. I want to create a detailed project brief for this concept. And the analyst here is
45:14
prompted to guide me through it so that I can really be a part of creating the brief. It's not just going to go and off
45:21
and do it all itself. And so in a second here, we'll see it maybe ask a couple of follow-up questions for us.
45:29
Um, so let's see. All right, we got some output here. So
45:35
it's starting to it's got the executive summary here. So it's starting to do some planning. We'll see if it I mean
45:41
it's kind of it's not always the same how the analyst works. Like sometimes we'll ask people more follow questions,
45:46
sometimes it won't. I mean, the BMAD method is not always going to like perform the same because LLMs are just
45:51
unreliable. They don't always do the exact same thing. Like, they won't always ask me the same follow-up questions. So, I'll just kind of let it
45:58
rip here and uh we'll get through our project brief. So, yeah, I'm going to go through some of the questions that we
46:04
got in the chat here. And I definitely won't be able to get through like all questions, so I'll just do my best to
46:09
hit on a couple of them at a time as we're waiting for Cloud Code to finish.
46:15
Um, let's see. So, I cloned Archon yesterday, configured Docker. When I go to local host 3737, I get the errors
46:22
below. Anything I'm missing? Uh, when you get failed to load credentials, that generally means that you either didn't
46:29
set things up in your database or you're using the anonymous Superbase key instead of the service roll one. And so,
46:35
this error um is yeah, one that we've seen quite a couple of times. So, you're
46:40
not alone. It's all good. You just have to make sure that you going back to superbase here. You need to be using the
46:45
service ro key that we have in superbase not anonymous. And then also going back to the instructions for setting up cloud
46:53
code or not for setting up archon. You just have to make sure that you run the
46:58
database setup in your superbase. You'll get those errors if it can't find the tables in your back end. So those are
47:05
the two things that I would say. Um yeah and and I I know that like for some people that have submitted some issues
47:11
for related things they generally come back and say like oh yeah it was one of those two things and that fixed it for me. So yeah just give those two a shot.
47:18
Um but yeah let's see. All right cool. So we got our project brief. It is done now.
47:23
So let's see what we got. Uh quite a bit here. So we got success metrics and
47:29
KPIs. We've got a timeline and milestones. So Mary is very much acting like a project
47:35
manager here, outlining really important things like what's the timeline for our project. I mean, this isn't actually
47:41
going to take 24 weeks. This is this is hilarious. It's not going to be 24 weeks. I promise guys, you're not stuck in this live stream for 24 weeks. Uh but
47:48
yeah, we got key milestones, risk assessment, resource requirements, which I mean this isn't really accurate
47:55
to what we're doing here. I I guess maybe if we create like sub agents for each of these things, I suppose. Um, I'm
48:02
about to spend $200,000 on development. That's kind of funny. So may maybe the
48:07
prompting for the business analyst could be a bit more accurate to like actually integrating this in development workflow, not with like a real people
48:13
that we have to pay. But you guys get the idea in general. Like it's pretty cool how we have this entire project
48:19
brief. And so the next thing that I want to do with this brief is I actually want to refine it and then store it as a
48:26
document in Archon. So, we'll start to see more how archon is integrated with
48:32
uh the BMAD method here. So, okay, I'm going back to my instructions here. I'm trying to remember exactly what I want
48:38
to do next with this. Um, yeah, let's see. So, I'm going to I'm
48:44
actually going to run the the help command again. So, I want to remember what commands I have. Um,
48:50
and then also there are some follow-up questions that we've got here. create user stories, develop competitive
48:56
analysis, which I'm not really interested in doing that right now. Generate technical implementations.
49:01
Um, what else could I do? Um, and actually, did they did the
49:07
project brief get created? No, it didn't get created yet. Okay. So, I'm going to let's just say this. I'm going to say
49:14
use archon to uh search how to leverage the cloud code
49:21
SDK. and then
49:26
add technical implementation ideas to the project brief and save that
49:34
brief in a new project I want you to create in Archon. Okay, so here we go.
49:39
This is where we really start to see the integration here. So, we're going to have Mary instead of just going through the typical flow that you do with the
49:45
BMAD method where you store all your documents in your source control like just in your your project folder, we're
49:52
going to actually have her use archon. So, she's going to do some research on how to leverage the cloud code SDK so
49:59
that she can help me generate a more technical implementation plan and actually do it based on the cloud code
50:06
documentation instead of just like simple research or hallucinating something random. It's going to use
50:11
archon. That's going to help a lot. And then we'll store the brief in Archon as well, and we'll do that in a brand new
50:17
project that we create. So, going back to Archon here within a single project, we've got the tasks tab, and then we
50:24
have the docs tab. So, we'll see Mary create a new project in Archon. In a
50:29
second here, this will pop up and then there'll be a project brief as well. So, first of all, before she does that,
50:36
she's going to search through our documentation. So everything that we crawled like I showed you crawling the
50:42
cloud code um the cloud code documentation in real time that is what we're searching through using the archon
50:48
mcp. So we're performing rag queries and then we're also searching through the code examples that you saw being
50:55
generated as well. So I'm going to do if I do controlr and cloud code we can zoom
51:00
into the output of our different rag searches. So like when we searched for code examples, we were looking for
51:06
TypeScript implementations and um let's see what we got here. Trying to like I
51:12
mean there's just a lot of information here. I mean it's okay that we don't have to like understand all this in detail but the coding assistant
51:17
definitely needs to. So let's go up to uh the first chunk that we retrieved.
51:23
So uh let's see. It's kind of hard to like
51:29
Okay, so here we go. We got some some implementations with the cloud SDK. So, it's pulling things from the cloud SDK,
51:35
which is good. Um, and then we got some things for the TypeScript SDK. So, that's what we actually care about using
51:41
here. U, so this is good. We're getting some of the code examples. And I'll do control R to go out of this. We don't
51:46
need to like dive into that forever here. Uh, but the important thing is if I go back into Archon, I didn't even
51:52
have to refresh my page because we have websockets. So, there's real time updates with Archon through the MCP and
51:57
the UI. We have our cloud code instance manager Nex.js control center project. So there we go. We got a a blank slate
52:04
here. So we got no tasks at this point, no docs, but we're about to create the brief. And so we'll see that here. Now
52:12
we'll add the enhanced project brief with technical implementation to the newly created project. So now Mary is generating that project brief. And once
52:19
it is generated, we can uh go back into Archon and see that. So we'll have to wait a little bit because it's usually a
52:25
pretty long document. So, I'm going to give it some time to generate. I'll go back to the chat here.
52:32
Um, okay. The first comment that I landed on is actually what I wanted to
52:37
speak to next. So, thank you Maxim for for asking or for saying this. An archon
52:43
specific version of be mad would be mad. And I agree 100%. That is actually one
52:48
of the um Well, there we go. A screen was flashing for a second because the uh brief was created. So we we'll dive back
52:54
into this in a second here. Um yes, one of the big things that we want to do for Archon is take different strategies for
53:03
context engineering and either create a guide for how you can integrate Archon
53:09
very closely with that strategy like BMAD or PRPs or spec spectr development
53:15
or actually build it into the platform where there's going to be like some toggle or some like select that you can
53:21
make in archon where it'll like overhaul the UI so that it's optimized for that specific strategy. That would be so
53:29
cool. So so cool. Um so that is what we're we're one of the big future
53:34
visions that we have for Archon. Um someone's asking is the sound cutting
53:40
out for you guys. Sorry if there maybe maybe it's because I'm like moving my head around. So if I if I stay close to
53:47
my microphone, it probably won't cut out as much. So I'm sorry about that guys.
53:52
Um yeah, I'll I'll just keep my face close to the microphone here. Okay. Anyway, so yeah, let me let me go back
53:58
to Archon because I want to pop this up for you guys here. Um, first of all,
54:04
first of all, we've got our project brief created. So, I'll dive into this
54:10
in a second here. This was just created by the BMAD agent. So, I'll dive into this in a second. But the other thing
54:16
that I wanted to to talk about uh just going more off your question Maxim is in the settings here I envision a a place
54:24
in the future where it could be like the context engineering strategy you want to use with archon and then there'll be
54:30
like um checkbox for PRP or like a checkbox for BMAD like something like that where then it'll then like optimize
54:37
things under the hood like maybe it'll give you global rules that are specific to working with BMAD and then like maybe
54:43
there'll be like different um tweaks to UI that we have. So, the way that it's organizes like documents or tasks works
54:50
better with BMAD or the way that it like displays the project brief, for example. Like, there's so many things that we
54:55
have. The other thing that just gets me so fired up about Archon. Um,
55:03
sorry, that says the audio is choppy. Yeah, guys, if you refresh the stream, that might help. Um,
55:10
Justin said reconnected fixed audio for me. Thanks, Justin. Yeah. Um, sorry
55:16
guys. I don't know why it's cutting out. I mean, it could it could be because of the storms that are happening. Like I I
55:21
preface at the start of the stream. That's kind of the only thing I know. So yeah, maybe reconnecting and and hopefully that'll help it. You could
55:27
just refresh the stream and um that'll help it like just refresh your browser
55:33
page. Um so yeah. Okay. I got distracted there. I got to talk about uh what I was
55:38
just about to say with Archon. The thing that gets me so excited is not just like how awesome it is right now and and
55:45
thanks to people like Sean and Raasmus for helping out with Archon a lot. Um, so I'm not like tooting my own horn. I'm
55:50
just saying that like we've built something awesome together and and a lot of contributions from the Dynamis community as well. But the other thing
55:56
that makes me so excited about Archon is just how many different things we can do with it in the future. Like Maxim said,
56:03
we can integrate with different context engineering strategies. Also another thing for Archon, one of the big future
56:09
visions I have for it is it would be amazing to make Archon into this command
56:15
center for not just task management and knowledge, but also for like all things
56:21
context engineering. Like imagine going into a new project um or even just like a brownfield project like you're going
56:28
into an existing codebase and you want to implement context engineering for the first time and you're like man I don't
56:33
even know where to start with my global rules and my sub agents and my hooks and my PRP template like what knowledge do I
56:41
even need? Like I don't even know where to start. And like that's something that I know that a lot of you struggle with and have told me in the community and in
56:47
my YouTube comments as well that like there's so many things for contact engineering right now that it's kind of overwhelming. Like I just want to go
56:54
into my coding assistant and have something set up for me where I have this optimal workflow for leveraging a
57:00
coding assistant and I don't have to like struggle through all these different things like let me set up my global rules and all let me set up my
57:06
context like it can kind of become a lot. And so the the dream that I have for Archon is making it so that we can
57:13
kind of like integrate the context engineering hub that I've been working on where like I have different like PRP
57:19
templates and I have these like different use cases that I've showcased on my channel. It'd be awesome to build
57:24
this out and then integrate it with Archon. So basically you can come into a new project and you can say I want to
57:31
make a Nex.js application to work with my cloud code instances like what we're building right now. And then Archon is
57:37
going to find the right example in the context engineering hub here. It's going
57:42
to go through these like templates for global rules and be like, "Oh, here's your global rule template for next.js."
57:47
And then, "Oh, let me go and crawl this documentation for you because you're going to need the next.js documentation." And oh, let me go and
57:53
create a project for you in Archon and set up some tasks to help you start this project. and like basically setting up a
58:00
project from scratch with everything you need for context engineering. Rag, your documentation, your tasks, your global
58:07
rules, your sub agents. Like it maybe there's like a repository of sub agents and it'll pull a couple of them that it
58:12
thinks you need for your project. Like if Archon can do that, it is going to be just like the best thing for AI coding
58:20
ever. And that's the vision that I have for it. Like that plus integrating with different strategies for context
58:26
engineering. Like I really want it to be the MCP for context engineering.
58:31
Yeah, a lot of plans. And and by the way, this isn't like just my vision.
58:36
It's something that um a lot of us have been talking about like just in the Dynamis community. And so um I I know
58:44
that I um I didn't say this yet, but I meant to. We had an alpha release of Archon
58:51
before we actually brought it into the beta release for everyone publicly. So there are a lot of people in Dynamis
58:57
that were trying it out at first and giving us some ideas and like really helping us shape our vision and working
59:04
through some of the initial bugs and things which I mean there's still bugs in Archon. We're working through those but like helping us get through that
59:10
alpha phase. And man, it's just like there's like an energy happening in Dynamis. I just got to say there's an
59:16
energy around like everyone envisioning like how we can take context engineering further and take Archon further. Like
59:23
that's something that I hope that you guys would want to be a part of. And so yeah, I just got to say again like I'll
59:29
pull up the um let me go back to my browser here. I'll pull this up again. Like kind of this workshop here that's
59:36
happening uh the August 27th the end of this month here. It's kind of like a culmination of a lot of different things
59:43
that we've been doing in Dynamis around context engineering and PRPs and archon. And so, yeah, if you guys want to dive
59:49
like really really deep into these things, I know like I have like concise guides on YouTube and things and like
59:55
those are nice, but if you really really want to dive deep, like that's where that's what Dynamus is for. That's what
1:00:00
I've got going on in Dynamis and we're all just like shaping the vision behind Archon together. And so, Archon is a
1:00:07
fully open- source project and it's something that we all can work on together, but there's definitely like a
1:00:13
next level of energy in the community. I guess it's just the best like it's kind of hard for me to think about how I want to like phrase or how to even like
1:00:19
explain that, but there just is like a next level of energy that we have in the community for the ideas that we're sharing with each other and and also
1:00:25
just the ways that people are talking about how they're using Archon and using BMAD and PRP and things. Um, so yeah,
1:00:32
just like a gold mine of ideas being shared with each other constantly. So yeah. All right, let's go back to our
1:00:39
terminal here. Definitely check out Dynamis.ai AI if that sounds interesting to you because again prices are
1:00:44
increasing after this weekend as well and you lock in your price for life. So yeah and come be a part of that that
1:00:50
half-day workshop too. It's going to be exciting. So all right we have our brief created
1:00:56
from our analyst. So I'm going to actually go back. Sorry I'm jumping around a little bit here. I'm going to go back in. Let's take a look at this
1:01:02
brief really quickly that we've created. All right. U someone mentioned knowledge
1:01:08
graphs. Knowledge graphs is another thing that we want to integrate by the way into BMAD.
1:01:14
Um, here I need to sorry I forgot to remove There we go. I forgot to remove that comment.
1:01:21
Plus one for Dynamus, not just because of Cole, but everyone in the community. I appreciate that, Sean. Appreciate that a lot. Enjoy Dynamus as well. Thank you.
1:01:29
What is happening in the community is really crazy. Thank you, Toby. I appreciate it, guys. Yeah, I I just like
1:01:34
I have to call out Dynamus a couple of times throughout this stream because it is where a lot of big things are happening. Um even like with Archon and
1:01:42
everything else around building agents and context engineering, but yeah. Okay, so here we go. We got our document
1:01:48
created. It's untitled probably just because um Mary didn't really understand exactly how to create the document in
1:01:55
Archon. I mean, it's just, you know, the little things that we're working through still. But here we go. We got next steps. We've got a risk assessment. And
1:02:02
so again like all the like genius things that the guy behind BMAD uh created like all the research he's done around
1:02:07
prompting and project management providing the right context like we see that in the different sections that we
1:02:13
have here. We've got our objective goal. Um we got our project overview the scope
1:02:19
requirements and uh if I scroll down a bit more I'm curious if I can get to the things where
1:02:25
it's like more specific to the research I did with claude code. Uh, okay. So,
1:02:30
technical specifications. Let's see if this gets into it more. Uh, okay. We got our tech stack. This looks pretty good.
1:02:38
Real time with sockets. Next.js. Um, nice. Looks good.
1:02:45
Um, okay. Direct SDK integration using TypeScript Python wrappers. I don't
1:02:52
actually like that. I don't want Python wrappers. So that's another thing I'll say in general with context engineering is like it's so important to validate
1:02:58
the output that you have uh from these kinds of um sub aents just any coding
1:03:04
assistant in general they they'll hallucinate weird things like this and so I'm actually going to go back into
1:03:10
our analyst here and I'll say I don't want a Python wrapper for anything.
1:03:16
Also, I need you to write out some more pseudo code.
1:03:22
Uh, do some more research on integrating
1:03:28
Cloud Code SDK with a Nex.js backend. Search the
1:03:34
Claude code docs some more for this. Okay. So, I'm going to have it correct itself in a couple of ways here. So you
1:03:40
guys are seeing live how I'm like looking through something finding those those code smells or like the doc
1:03:46
smells. I'm like that is bad. Like I I if I'm using Nex.js, it can be my front end and my back end. I don't need Python
1:03:51
wrappers for anything. So clearly it got confused just as it was searching through the docs, but that's okay. So
1:03:58
yeah, it's going through and it's it's performing rag and searching through the code examples again. So we'll see what
1:04:03
kind of token or what kind of output we're getting here. U okay so this is actually what I wanted because now the
1:04:10
main thing that I needed to understand is this import right here is actually super crucial because we need to
1:04:16
leverage this query in order to call into cloud code from our Nex.js JS
1:04:21
backend and I'll show you guys specifically the docs that it is referencing
1:04:28
is uh I'm talking about this or not where is it this thing right here. So
1:04:34
import query from cloud code and then like here's like a super basic example of how you can call cloud code within
1:04:41
your typescript code. So like this would be within our API endpoint in nex.js. So like this is what it just found when it
1:04:46
searched through using the knowledge that we have crawled with archon. So that's really good. That's exactly what we wanted it to find. So now we can use
1:04:55
that. And it's just wrapping up here. So I'll let it wrap up. And it it also did
1:05:00
a web search here just to like supplement his information. Which by the way, Archon doesn't have to fully
1:05:05
replace the web search that most coding assistants have. Like you can use these things together. Like I I love seeing it
1:05:11
when it performs some queries like looking at code examples and performing rag and then it also does a web search and it combines all that together. Um,
1:05:18
so yeah, we'll see that. And then it's going to update the Archon project. So it'll go ahead and update the brief that
1:05:23
we have in the UI as well. All right. Oh, another nice comment from
1:05:30
Kosik. I appreciate this, Koshik. The most important part of Dynamus is how engaged Cole and the founders are. Yeah,
1:05:36
I'm in Dynamus day in and day out. Like, I live and breathe Dynamus, just like we're living and breathing in the the terminal for this live stream here. So,
1:05:43
yeah. All right. Um, it's taking a while here, so I'm going to go through some other things in the chat. Oh, we got a
1:05:50
donation from Kooie. I did not want I almost missed this. I'm so sorry. Thank you, Kooie, for your support. Great demo today. Also, thank Sean for building
1:05:56
this amazing Archon UI. Hope Archon keeps progressing and thriving in the near future. Thank you, Kooby. I
1:06:02
appreciate that a lot. Um, yeah, Shawn is killing it for sure. Um,
1:06:09
I kind of want to shrink. Okay, I'm shrinking the message here. So, if I display another message, Mary is living
1:06:17
in 2016. Did she do a web search that was like 2016 or something? Or are you just
1:06:23
saying that like her output is 2016? Um, oh, thanks, Glenn. If you want to
1:06:29
help shape Archon Dinos community is the place to be indeed. I appreciate it.
1:06:36
All right. Um, okay. Oh, yeah. Yeah. Okay. Here's the question on on the knowledge graphs that
1:06:42
I saw earlier. Congratulations, Cole. Since you profess knowledge graphs so much, does Archon implement knowledge
1:06:48
graphs from more deterministic rag with frameworks like graffiti? So, really good question. I've been experimenting
1:06:54
with knowledge graphs for oh, I did a lot of that in the crawl for AI rag MCP
1:07:00
server. So, if you guys have been following my channel for the last couple of months, a lot of the things that I built into Archon, the different rag
1:07:08
strategies that we have with reranking and agentic rag and hybrid search, I implemented a lot of those things in the
1:07:14
crawl for AI rag MCP server first and that was kind of like a test bed for
1:07:19
some of the things that I brought into Archon. So, even some other things I've been doing on my channel, it is all for
1:07:24
Archon in the end, just showcasing it through separate projects so I could break things up more. Still have really
1:07:30
cool content to bring you guys and like show more like rag strategies behind the scenes, but with the end goal of it
1:07:35
being like, let's build this into archon and knowledge graphs is one of the things that I did some experimentation
1:07:40
with in the crawl for AI rag MCP. And we're already talking like me, Sean and Raasmus and and some people in Dynamus,
1:07:47
we're talking about knowledge graphs with Archon and already thinking through what that might look like. And Sean even
1:07:52
has a user interface for knowledge graphs already that he has just in like his own development environment. So it's
1:07:58
not like something that you could try yet because it's not ready, but we're thinking about it. So knowledge graphs, yes, that is going to be a part of
1:08:04
Archon at some point for sure. So yeah. Um,
1:08:10
can archon work with open router? So, I covered this earlier. Open router doesn't have embedding models, but we do want to make it at some point where you
1:08:16
can set your LLM and embedding provider separately. So, you could use like archon for the LLM and Gemini for your
1:08:21
embeddings, for example. So, yeah, we definitely have that top of mind. Um, so let's see. I wanted to look. Okay, so we
1:08:28
got a bit of like pseudo code here. So, this is what I was looking for. Like I I
1:08:34
wanted Mary to to not just like do like high level stuff but do like a little bit of like low like let's get the code
1:08:40
as well. So I'm looking at this. This is actually more than I wanted but it's all good. Um cuz I don't I don't know if she
1:08:48
updated the brief in archon because I don't see the tool call for that but like this looks pretty good overall.
1:08:55
Um okay nice. Okay, so now I want to make sure
1:09:00
she adds she updates the brief in Archon. So, let me scroll all the way back down. Uh, did you update the brief
1:09:09
in Archon? Make sure you do so. Okay, because I need I need to see that. Like, I don't just want the output here. I
1:09:14
needed to update the brief. And this is a a good example where um Okay, this sucks. I'll come to this in a second.
1:09:20
This is a good example where um there's definitely an opportunity to customize the prompting and the global rules to
1:09:27
make archon integrate more closely with BMAD. Like the analyst here, Mary, she didn't quite understand that like oh I
1:09:33
have to go back in and update Archon. I mean she apparently she said she did but she didn't which is super weird. Like
1:09:39
that seems like a problem in the prompting somewhere. But like yeah there's definitely an opportunity to have like a like BMAD specific set of
1:09:47
prompts where it's like for the analyst this is how you work with Archon. for the PM. This is how you work with Archon. Like that's kind of going back
1:09:52
to what Maxim said earlier. Like that's the goal that one of the goals I have for Archon is making it so that like there's a preconfigured setup to work
1:10:00
with these different strategies. Um kind of sucks that I'm getting an API error from Anthrop. So Anthropic is having
1:10:06
some issues right now. This is not this is nothing on my end. A 500 error is unfortunately an outage from Anthropic
1:10:14
which they they're saying their systems are operational. Um, but usually there's
1:10:19
some delay between like them admitting there's an outage and the status
1:10:24
actually getting updated. So, let's see. I'm just going to have to like retry this a couple of times and hopefully
1:10:31
it'll start working. Um, me.
1:10:38
Okay, it's retrying. Well, anyway, while it's doing that, that's okay. Cloud code
1:10:44
is amazing. It is such a cool tool. works so well. It's better than every coding assistant. But man, do these
1:10:50
errors just crush me sometimes when I'm in the middle of something really important like I am right now doing this
1:10:56
live stream with you guys. Of course, I get API errors and Anthropic has an outage when I'm doing something with you
1:11:02
guys, but hopefully this will be temporary. When I was doing some playing around with BMAD this morning, I got this as well and it went away um pretty
1:11:09
quickly. So, it only is like 10 minutes of an outage. So, I'm just going to head to the chat here and just use this as a
1:11:15
time to talk to you guys. So, yeah, let's see.
1:11:22
Um, can Archon crawl docs with Sphinx standard? I'm not actually familiar with
1:11:28
the Sphinx standard, so I'm not sure. Um, yeah, I'm sure that's a really good question, but I actually am not familiar
1:11:34
with that. Um, do you run Archon on a dedicated server or locally? So, Archon right now,
1:11:41
it's only possible to run it locally. It's just meant to be something that you pull the GitHub repository, you spin up the containers yourself, and you run it
1:11:48
locally. Which means you can actually have everything entirely private. Like, you can use O Lama for your local LLM.
1:11:55
You can use a self-hosted superbase. You can run Archon completely local. And if
1:12:01
you want to take it really far and use like R code with a local LLM, for example, you can have your entire coding
1:12:06
environment with Archon 100% local. Nothing ever leaves your computer. No, you you're never sending data out, I
1:12:13
should say. So, yeah. Um, it's pretty sweet.
1:12:22
Um, let's see. I'm trying to have you addressed the question of GBTOSS if it can be embedded. So, you can use GPT OSS
1:12:29
through Olama and Archon with uh Olama being something that it's not fully
1:12:34
supported yet, but we're working on that. and then you'll be able to use open source models for sure.
1:12:40
Um, yeah, this sucks. I really hope that this doesn't last for too much longer. I
1:12:46
mean, it's nice to like have a time um to like chat with you guys, but I was hoping to mostly be chatting with you
1:12:52
guys while things are actually running and not just getting outages. So, that kind of sucks. I'm going to check the
1:12:57
status page as well. Okay, so nothing nothing yet. Uh, we'll see if we get an
1:13:02
update here. So yeah, no incidents, but obviously there is one. Mike said that
1:13:08
also Anthropic is choking here also. Yeah.
1:13:14
Uh that's Yeah, that's too bad. Start with the courses. I assume you're talking about Dynamus. Yeah. So if you
1:13:20
guys don't know in the Dynamus community, I have a full course going start to finish building AI agents from
1:13:25
scratch and I walk through my entire process for doing so with a ton of different templates that you guys can implement like right away. It's pretty
1:13:32
sweet. Um and and I'm actually in progress making that course. I just finished module seven out of 10. So I've
1:13:38
been working my butt off on that course, putting a lot into that. So yet another part that um that I have in the
1:13:44
community for you guys. If it doesn't help slashcle and slashexit will resume. Is this for
1:13:52
the outage are you saying? I mean I I don't really want to restart my session here because um I will lose all the
1:13:59
context I've been building up with the analyst already. So, I don't know if I maybe you were talking to someone else,
1:14:04
though. It's kind of hard to follow the chat fully. Um, okay. I'll go to the next thing from Tim here. Read global
1:14:12
rules. I'm creating a project that uses langraph, padantic, mem, and neoforj. That's awesome. Should I only include
1:14:18
base archon plus langraph for the global rules and nothing for the other primary libraries?
1:14:23
So, that's a really good question, Tim. It is up to you entirely. You don't have to specify a ton of things for the for
1:14:32
each library that you're using in the global rules. Like generally, you will have your global rules for archon.
1:14:38
You'll have your general global rules for like Python, for example. Like here are the the key things like architecture
1:14:44
and best practices I want you to follow for Python. And then if you want something specific to langraph like
1:14:50
whatever your like really like core tool is for the implementation sometimes you'll have global rules specific to
1:14:56
that but for all of your like more supplemental libraries I would say like mem zero for example you definitely
1:15:02
don't have to overengineer global rules and include a lot for that as well um you just using archon to retrieve the
1:15:09
documentation for me zero and pantic so like understands how to use those
1:15:14
libraries and like looking at the examples there That's generally enough. So I I wouldn't try to like fit everything into your global rules. Like
1:15:20
allow archon to like find that for your coding assistant as it's doing some
1:15:25
searching with rag. But yeah, good question. Let's see what else we got. Are you
1:15:32
working at So I'm not doing TDD right here. Um though, yeah, I don't think
1:15:38
BMAD doesn't really do test driven development. I don't think like but like definitely TDD is powerful with coding
1:15:45
assistance like they work quite well if you build the tests first and then have the code after that. Um not something
1:15:50
I'm doing right now though. Let's see. Uh switch to Gemini CLI or
1:15:57
Crush. Yeah, I don't I already have the context here and I don't actually have
1:16:03
Gemini CLI installed in this computer. I was testing out elsewhere so I can't really do that. um pretty reliant on
1:16:11
Claude code for this live stream and be hard to like switch things over. So, let's just hope that the outage doesn't
1:16:17
last long, but it's okay because we got a time for Q&A right now. That's all good. And I maybe I'll poke around and
1:16:22
show some things in the Archon UI while we wait for this retrying in 40 seconds. This sucks. Um I'm curious, is anyone
1:16:30
else actually getting things to work with Claude right now? because it maybe
1:16:35
it like because I know Mike you said it's not working for you but maybe it's like a geographical outage or maybe it's
1:16:42
not like a full outage. Um I don't know. This is really unfortunate though. But it's all good because we adapt. We're
1:16:48
freestyling in this live stream to the point where we can't even code anything but we're going to make it work anyway.
1:16:56
Um yeah, this is why I run cloud code through open router. Yep, that's fair.
1:17:02
But I think Cloud Code is updating things where you can't use proxies anymore to go through models um besides
1:17:09
Claude. I think they're actually taking that away. That's what I heard at least, which should be kind of unfortunate, but
1:17:16
BMAD version 4 includes TTD. Okay, that's really cool. That's good to know. I didn't actually know that.
1:17:22
Okay, Claude is working for you. Okay, well, let me try this. I'm gonna
1:17:28
try a new Claude session and I'm going to see if I just like say hi if it's going to work because maybe maybe I just
1:17:34
need maybe I do need to restart my session which would be unfortunate. I guess it's not that bad though cuz I can re Oh, it is working. Wow. Okay. Um
1:17:44
stop. That's unfortunate. So somehow it's like
1:17:50
my just my session. What? Okay, that's too bad. Um, that's really too bad cuz
1:17:59
it's it's just going to be kind of annoying to like restart a new session and then uh give it this context again.
1:18:05
So, all right. Well, we're going to bite the bullet and we're going to do it. So, I'm going to go into
1:18:10
um emad app clear. We're going to we're going to do this from scratch. So, I'm going to say analyst and we'll see if we
1:18:17
get an error here. Um oh, I can do a resume. Right. Right.
1:18:22
Resume. Um,
1:18:32
wait, that didn't work. Hold on. Why is that not working for me? I might
1:18:39
just do a new session here. I'm going to do Okay, I'm going to tell Mary to grab the project brief from the And then I
1:18:47
need to know the name of my project here.
1:18:53
It's the Yeah, this one right here. So,
1:18:59
all right. Grab Well, this is also kind of cool to demo like uh just like
1:19:04
pulling in the brief and starting from scratch. So, I'm having it grab the project brief from this project in Archon and then do some more technical
1:19:12
research looking at the um cloud code documentation to see how to invoke it
1:19:20
from TS and then add onto the brief in Archon with your findings.
1:19:27
So, we have a more technical component. I'm not spelling things right, but that's okay. Have a more technical component for the brief. Okay, so I'm
1:19:34
going to go ahead and send this in. Hopefully, we don't get any more errors. Um,
1:19:39
Claude, I could do claude d-resme. Okay, well, I'll just try this here. Claude
1:19:46
dash resume. Is that what you meant? Like I exit out? I mean, I lost the session, but
1:19:52
oh, wait, hold on. Shoot. Okay. Um,
1:19:58
use archon for rag. Okay. So, trying to do a web search, which I just want to start I just want to have it start with
1:20:04
archon. So, I'm going to tell it to use archon, but uh yeah, let me claw d-res.
1:20:09
Okay. Can I start from my session from two minutes ago?
1:20:16
No, it's like it's just broken now because it it's stuck here. It Yeah, I'm just going to close out of this. We
1:20:22
we'll we'll go to this session now because apparently it's just working, which is weird, but okay, we're resuming. We're good. We're good. All
1:20:29
right, we got a donation from Paul. Thank you, Paul, for the donation. I appreciate it a lot. Uh, and yeah, we
1:20:34
can go through a couple things as it's working here. Would it be possible to ingest my complete cursor chat history for a project I've been working on for
1:20:40
four months? If so, would the information be useful in providing the cursor agent with memory?
1:20:47
That's a good question. So, that might be that might be too much information.
1:20:52
Now, with the if you actually are storing this in a vector database or a knowledge graph, you can scale to quite
1:20:59
a bit of information that you have stored. I don't know how useful it would be though. Um,
1:21:05
here's what I'll say. Generally, when you're using AI coding assistance, I've
1:21:10
never done it before. I haven't really heard of people having success with just taking the entire chat history and
1:21:15
dumping that in like long-term memory for agents. Usually, more what you'll do is you'll get to certain checkpoints in
1:21:23
your implementation, your codebase, and you'll have your coding assistant output a summary of what it did. And so you'll
1:21:28
have like a set of markdown documents that just outline like here's the feature I implemented or like here's the
1:21:34
story that I completed and here's a summary of what I did with maybe like a little bit of pseudo code or like
1:21:40
referencing the files that were changed that kind of thing. And so then you have something much more compact where you
1:21:46
have a set of information that's like all just like pure value versus a conversation history will get pretty
1:21:52
messy because you're going to have a lot of like going back and forth with the coding assistant fixing different things. And so also in the long-term
1:21:59
memory if you pull a certain chunk like through rag it might actually be pulling an implementation or like a part of the
1:22:06
conversation where things were actually broken and that that's kind of dangerous. So, I would more like get to
1:22:11
certain checkpoints with like stories or tasks being completed. Have it output markdown documents for what it did. Now,
1:22:16
that's where you could build up more long-term memory of like here's like the change log basically like here's what
1:22:22
happened when I started the project and what I implemented. Now, here's what I changed as I'm going through an existing project. And that would I think make
1:22:28
better long-term memory. And I know that like that's not really
1:22:33
something you can do retroactively. you kind of have to like have that as your process going forward. But that's definitely what I'd recommend doing.
1:22:43
But yeah, okay, there we go. So, we have now updated our brief. So, we did a bunch of searching here. Now, we've
1:22:48
updated our brief in Archon with some more technical implementation. So, let's actually go back into Archon. Let's
1:22:54
check this out. So, I'm going to refresh, go into docs. Oh, this is the wrong
1:23:00
project. Here we go. All right. We got a title now, by the way. That's good. So she Mary fixed things with version 1.1
1:23:06
to actually add a title and cool. She even labeled herself. This is cool. So this is this is another neat integration. Something that that another
1:23:14
big thing I know that I'm talking a lot about like the vision of Archon here um as well as showing it, but I think that's important. Another big thing we
1:23:21
want to do in Archon is make it integrate really really deeply with the idea of sub agents. And so different
1:23:28
documents can be labeled by the agent that created them. different tasks can be assigned to different agents like we
1:23:34
can have Mary tasked with the um the research and the like initial like kind
1:23:40
of like all the analyst stuff right like we're creating our uh brief here and then have like the project manager
1:23:46
tasked with the things that we have related to creating the PRD having the developer tasked with things related to
1:23:52
the coding and the QA agent like we can have these different tasks that are assigned to different things that we
1:23:57
have in our task list here and then have them all coordinate together and so we have like clear boundaries in which sub
1:24:04
aents are implementing what things based on their assignment in archon. That's another thing that we're looking to do
1:24:10
as well. So here's Mary has added version 1.1 for the brief. So we have a
1:24:15
lot of the same things as before like our scope requirements and our text stack and resource requirements but then
1:24:21
we should also have more of a technical implementation. Um, like here for example, we got some
1:24:28
actual like code in here. And I don't I'm not gonna like go through and like validate all this right now because I I
1:24:34
do want to move forward, but like we have some more like technical pieces to our implementation now. Um, so I think
1:24:40
that's a good starting point. We'll kind of go with that. Um, like talking about the context manager pattern, like things
1:24:45
that are specific from the cloud code docs that have it found. So that's really good that we have that now and we used archon to fetch those things
1:24:50
because who knows if a web search would have been able to get something that specific. And um also it's just nice
1:24:56
that like we can pull code examples and things from Archon as well. So, okay, there we go.
1:25:02
Uh another donation. Thank you, Christian. I appreciate it a lot. Your sharing spirit is so highly appreciated.
1:25:07
Keep it up. Thank you very much, man. It means a lot. Um
1:25:12
oh, sorry, I meant to showcase the other thing here. Can I Thank you as well for the donation. Daily profit. Can I create
1:25:18
the same for the Python ecosystem? Yeah, so um actually I mostly work in Python.
1:25:23
I'm just doing this right now because I think Nex.js is the simplest for what I'm looking to create here, the front end and the back end, but I typically
1:25:29
work with Python. And so I'm I'm using Archon for Python all the time. And all my context engineering, a lot of the PRP
1:25:35
templates that I've created for things like Pantic AI, they're all Python. And so Archon is not specific to a language
1:25:43
or a coding assistant. It is general enough to apply if it's you're working in client on something with TypeScript
1:25:48
or you're working in Kirao with something on Python or you're working in cloud code with a Rust application, right? Like it applies to everything.
1:25:55
You just crawl the documentation for the libraries you want to use no matter your library or coding assistant and then the
1:26:01
way that you manage tasks is the same for any language or coding assistant. So yeah,
1:26:08
doing a great job, Cole. Really, really appreciate your efforts. Thank you very much. I that means a lot. Yeah, and I'm seeing a like sorry I can't like
1:26:14
showcase all of the the comments that we've got here um in the chat, but but uh I'm I'm seeing them. So, thank you
1:26:20
guys for all the kind words. Like, it really means a lot. Okay, so we'll go ahead and um
1:26:28
move on to the next thing here. So, we have our brief created now. And so,
1:26:33
actually what the founder of BMAD recommends doing is clearing the conversation entirely when we go on to
1:26:39
the next agent. So, we've been working with the analyst agent this entire time. Now, it is time to move on to the
1:26:44
project manager. So, I do PM uh /pm and then tab. So, I'm now invoking the
1:26:50
project manager because essentially what we want to do now is we want to take the brief that we've created in Archon based
1:26:55
on all the research we've done and everything. And we want to turn it into a PRD. So, it's going to be more
1:27:01
specifically like let's dive into the specs for what we want to have created. So, now we have John, our project
1:27:06
manager. And it's actually pretty cool because I invoked John and right away he goes into
1:27:12
the existing project that we have for Archon. That's pretty cool. So we have uh no tasks yet, but yeah, that's right.
1:27:19
Like right now we just have the doc in the project. So I can do star help to see what we can do with our project
1:27:24
manager. Now the thing that I want to do is create a PRD.
1:27:29
Um so yeah, let's go ahead and I'm going to copy the command here. So specifically what we want to do is we
1:27:37
want to create a PRD. And I I promised that I would talk about working with brownfield projects as well. So we're
1:27:44
creating something from scratch here. But if you're working in an existing codebase, like I said, the big
1:27:49
difference is with existing code bases, generally you're going to be more referencing existing code versus with a
1:27:55
new project, you're looking to external documentation for things like architecture and best practices. And so
1:28:01
there are actually different commands that we invoke in John our project manager in BMAD based on if it's a new
1:28:08
project. This is for a new project. This is for an existing project. Like if we're creating a PRD to add a new
1:28:15
feature into an existing codebase. And so I won't showcase this right now, but yeah, the diagrams that we have for
1:28:21
BMAD, if I go back to that here, there is a different step that we take based
1:28:26
on if it is a new project or an existing one. We're kind of at this stage in our diagram now. So, I'm going to paste in
1:28:33
my command here. Uh, whoops, I did not mean to do that. Let me copy the other thing that I have uh just from my notes
1:28:39
here, my other monitor. Okay, this is what I meant to do. So, we're going to call the create PRD command. And I'm
1:28:44
telling it to pull the brief that I have in the archon project. And then I want it to create the PRD in archon as well.
1:28:51
So, we'll have a second document after we invoke this command. And also the big risk that I have to tell you guys with
1:28:58
claude in general and with BMAD is it oftentimes loves to overengineer.
1:29:06
And I'll show you guys what it looked like. This this is really unfortunate. The other example that I showed you guys. So like this project that I had
1:29:14
created to like play around with BMAD initially, it created 123 to-dos. it
1:29:20
completely overengineered with like super random tasks and things like this is the risk that you have when you have
1:29:27
Mary and John working together to create your initial PRD. Like things just get
1:29:33
so overly complex because it's trying to build like this full productionready software for you and you don't need that
1:29:38
to get started. It's way too much to to go through in in one time at one time. So yeah, I would say like my biggest tip
1:29:45
is in your global rules for your coding assistant and just generally in your prompting. It's important to be clear
1:29:52
quite often that you want things to be simple because Claude loves to overengineer. It's so annoying. You we
1:29:58
don't want 123 tasks. We want like 10 to 20. Like that's what I'm hoping to create here. And so I'm telling it to
1:30:03
not overengineer and just keep things simple. And so first we'll see it call into archon. So it'll use the MCP to
1:30:09
grab the brief. Uh there we go. So, we pulled the brief. I can do control R to
1:30:14
expand it. We can see it. It pulled the brief here. And then it's going to uh do
1:30:20
some research. I I forget exactly what the project manager does to like create the um to create the PRD. Like I forget
1:30:27
if it does research or if it more just like takes this and transforms it into a a PRD like just with its own reasoning.
1:30:34
But we'll see in a second. This will obviously go for a little bit though because um or no, I guess it wait I
1:30:41
guess it's almost done. Here's our simple PRD. Okay. Product vision core
1:30:46
problem. Here's our solution. A lightweight Nex.js app that wraps cloud code SDK to enable multi-instance
1:30:52
management. This that's perfect. That is a oneliner for exactly what I want to create here. So it's good. It understands what I'm looking for. And
1:30:58
then here's our MVP. Here are things that are out of scope. So it's avoiding complexity. I actually love this a lot.
1:31:03
So when I was playing with BMAD initially, it was like including like all of these things like I actually
1:31:08
remember seeing this explicitly that it was like trying to implement like team features so we could have multiple people managing this this whole like
1:31:15
application which that's cool but like let's not try to implement that right now. It's good that we're excluding some
1:31:21
of these things. So we're starting with a simple local app like we have with Archon. Then we can build these things
1:31:26
after which by the way that is actually what we're doing for archon like in scope what we built for the beta of
1:31:32
archon is let's give a simple and beautiful user interface to manage
1:31:37
projects knowledge and documents. Then when we start to move out of beta and
1:31:42
get a lot of feedback for how we can improve the platform. Then we'll start to add in different context engineering strategies and being able to manage the
1:31:49
full suite of context and let's get into enterprise f features and make it so you can host archon like that. Those are all
1:31:55
the things that are coming for archon. But we not we got to start simple because if you try to do too much at
1:32:01
once like coding assistants like to do, you are just in for a world of hurt. And so we're starting simple. I I actually
1:32:07
appreciate this a lot. So let me go back down. Okay. So, uh, yeah, out of scope. Here's
1:32:14
our simple architecture. I mean, I kind of wish it expanded on this a little bit more at least, but that's okay because I actually love it
1:32:20
when coding assistants will output like the code base, like the structure that they're they're looking to implement.
1:32:27
But yeah, here is our text stack. Xterm for terminal display. Sounds good to me. Next.js14 Tailwind looks good. Um, no
1:32:35
need for Okay, so it's just going to do local storage for the config. So, we're not even using a database, which I think that's fine. I guess for this
1:32:42
implementation, we'll call it good. Uh maybe it's actually a little too simple, but I think for the cases of our live
1:32:48
stream here, because we're already at one and a half hours, this is probably this is probably good.
1:32:53
So, yeah. All right. Um let me go to success criteria development principles.
1:32:59
Good. Good. User journey. Okay. Now, now we create this document in uh Arcom. So,
1:33:05
cool. All right. So, let's actually take a look and make sure this was created, that it's looking good. So, I'll go to
1:33:10
my projects. I'll go to this one that we have new here. Go to docs. And there we
1:33:16
go. Here is our PRD. Nice. Cloud code instance manager simplified PRD.
1:33:22
And um yeah, looks like there's a couple of little issues here. Like I said, the docs part of Archon is like the most
1:33:28
experimental right now. And so, it's expected to not like look the perfect right now. There actually is a PR out
1:33:35
from Sean to improve a lot of these things. So, we got we got improvements coming for this like really really soon.
1:33:40
Um but yeah, um this is looking really good though. We got our text stack folder structure. Here's our scope
1:33:46
looking really good. Like perfect. All right, we got our PRD. Like now we're ready to dive into the implementation.
1:33:53
Um yeah, like this is this is great. I love how it looks overall, even though it's not like perfect yet. And then
1:33:58
there's also a markdown editor if you want to edit things yourself, you can do so. So you can be a part of the process of editing the doc right in archon and
1:34:05
then saving it to your superbase. So like all these documents are stored in superbase so you can reference them between sessions even between users very
1:34:13
easily. Like one thing that us like core maintainers for archon like everyone in the Dynamis community what we're looking
1:34:18
to do is actually like spin up a shared archon instance which it doesn't
1:34:24
actually mean like here here's the cool thing with archon. If you guys want to share your Archon instance with other
1:34:31
people because everything is stored in Superbase, it's not like you have to host one Archon instance and then deploy
1:34:38
it to the cloud. Like you can have everyone running their own Archon instances locally just pointing to the
1:34:44
same Superbase database that you have in the cloud. And so obviously that wouldn't work for like localhosted
1:34:50
Superbase. But if you're going to like superbase.com and creating a project there, then everyone can can use the
1:34:57
same archon instance. So you can have everyone working on the same projects and docs. They're just all running their
1:35:02
own archon pointing to the super basease in the cloud. It's pretty cool. So yeah. All right. We got our PRD now. And then
1:35:09
there are quite a few other things that we can do with John the project manager.
1:35:14
And so I'm going through things pretty quick. Like there's a lot of other things we can do with Mary the analyst as well, but I I don't want to spend a
1:35:23
good amount of time on each of these. I want to get through things pretty concisely, but typically when you go through
1:35:29
using the BMAD method, you'll spend a good amount of time with these different commands and actually providing your own
1:35:35
feedback a lot more. like I'm doing things the way that I am now just to keep it concise. But typically, you'll
1:35:41
spend a good amount of time working through these different agents because the context that you provide up front is
1:35:46
so important. It might feel like it's taking you a long time, but it's important to sharpen your axe because if
1:35:52
you try to rush through this initial planning and creating the brief in PRP or PRD, I should say, if you rush
1:35:59
through that, then the actual implementation is going to take exponentially longer because it doesn't understand what you're looking for and
1:36:05
it's going to hallucinate a lot more because it didn't do that upfront research. And so, it's worth spending time with this.
1:36:11
And so in this case, what I'm going to do with the project manager,
1:36:17
um, is I think I'm going to call it there. I'm looking at my notes here to see what else I did. Um,
1:36:25
yeah, I think I'm going to call it here. So, I'm going to I'm going to clear and I'm going to go on to the next agent
1:36:30
here. So, going to our flow within BMAD.
1:36:36
Let's go back. So, next up, we have our architect. So, we're going to create uh
1:36:42
the architecture from the PRD. And also, I'm going to actually have the architect create tasks for us in Archon. So, I'll
1:36:47
do slash architect. Good. Good. And I'll do the help command after it runs its little intro message
1:36:53
for me here. Um or I guess it's going right away. Wait, what is it doing? I'll help you
1:36:59
set up the Archon project management system for a BMAT app. Let me start by checking what's available in the Archon MCP and create a project structure. Um,
1:37:09
all right. It's just going right away. This is interesting. I'm just going to let it run. Like I said, we're freestyling today. When I tested the
1:37:16
architect before, it didn't do this, but now it's just like running right away. Um, and it's okay. So, now now we're
1:37:23
integrating BMAD with PRP. Let's go. Okay, this is interesting. I'm I'm just
1:37:29
going to see what it does. Um, what is it doing?
1:37:34
Okay, I need to stop it now. Sorry. Sorry. Sorry. Uh, architect. What's the
1:37:39
architect's name? The architect didn't even tell me what its name is. It just went right into it. Uh, what is your
1:37:45
name? All right, cuz it c the thing that I made me have to stop it is that it
1:37:51
created a third project and that's that's not good. Like I needed to I'm going to just go ahead and delete this
1:37:56
project because I need it to reference the existing one because we got our docs here. So, but that's all good. Like it's
1:38:01
fine just to correct it quick. Okay, so it's Winston. So Winston dove in right away before even introducing himself to
1:38:08
me. Okay. Okay, Winston, I need you to use the existing project in Archon and
1:38:15
then I'll just call out the name. Uh so let me go back here. I'll copy
1:38:20
this because I I just don't want to reference the old one that I had just to like show you guys a previous attempt. So um yeah. Okay. Okay. So using this
1:38:27
project read the PRD that we have stored in that project in Archon.
1:38:34
Then I want you to shard the PRD into tasks
1:38:41
uh no more than 20 tasks and put those in the tasks for the archon project. All
1:38:47
right. So basically what I'm telling it to do is pull down this document right here. And then based on all the
1:38:53
requirements that we have and everything, I want it to just create 20 tasks. So we start building up our cananban board here. So we can dive into
1:39:00
the implementation. And so I don't know if 20 is enough or not. I just want to like really keep it simple here. And so
1:39:06
yeah, so it's pulling the document here. And now we're starting to create some tasks. And so we should be able to see
1:39:11
this pop up in real time as we go. So let's see what it's doing here. I'm going to go ahead and refresh.
1:39:18
Um, okay, there we go. All right. So, it's creating some tasks there. I got to Sorry, I'm having an
1:39:25
issue with my browser here. Um, okay. Yeah, there we go. So, it's creating some tasks here. Like, let's
1:39:32
see this one right here. Create cloud SDK wrapper class with TypeScript. Looks good. And it's referencing the specific
1:39:38
file to implement. It's talking about error handling with some like specific errors that so like this class the CLI
1:39:44
not found error like it found this from the cloud code documentation. So this is based on its research that it did with
1:39:50
the archon arg functionality that we gave it. So yeah it's looking good. So it's going through it's creating all
1:39:56
these tasks here and um yeah I'll just kind of let it run with that. So I'll go
1:40:01
to the chat here while we got the the tasks being created in Archon.
1:40:07
Um, Winston is defin on the chopping block. Yeah, come on, Winston. No, it's
1:40:12
all good. Um, because like I said, there's probably a lot of opportunities to integrate BMAD with Archon a lot more
1:40:21
with like just even the way we're setting up the global rules, telling Winston how to use Archon. So, it
1:40:26
doesn't make those assumptions like he did in in um initially, which yeah, so I don't really blame him, but it was
1:40:32
funny. So yeah, LLMs and and sub aents, they're they're inconsistent in the way that they leverage the tools that we
1:40:38
give them. And so that's why it's really important to be super specific with our prompts.
1:40:44
Um Cole, nor Okay. Yeah, good question, Toby. Normally use cloud code in the WSL terminal. Reason why you use cloud code
1:40:50
in Windows when you're using the BMAD method. So this Yeah, really good question. Um
1:40:57
I this is not specific to BMAD. I've had some issues recently where if I use
1:41:04
cloud code within WSL specifically, it doesn't matter if or if I use cloud code
1:41:10
in a um IDE terminal specifically like a VS Code terminal, it keeps freezing on me.
1:41:18
Like it's super laggy and glitchy and whether I'm using WSL or not, just like within a terminal in um the IDE. And so
1:41:25
I've started to just use it within just a Windows PowerShell on my computer and it's it's performing a lot better. And
1:41:31
it things were slow in WSL especially for some reason running unit tests with Piest was like super slow in WSL and and
1:41:39
even just like installing my pip requirements was a lot slower in WSL than it was um just outside like on my
1:41:45
Windows machine. So yeah um I don't know why it that's the
1:41:51
case but it's things are just faster when I run it here. So, it's not specific to be mad, but yeah. All right. Donation from Kev.
1:41:58
I appreciate a lot, Kev. Thank you very much. Would deploying to a home server just be a matter of reconfiguring
1:42:03
the&env and docker compos to allow ports and URLs to be accessible remotely? I mean, aside from host type pricks.
1:42:10
Really good question. So, we actually have someone in the Dynamis community. Uh, his name is John. He has It's so
1:42:16
cool. He's running nine Olama instances on the computers that he has in his house and he's doing a ton of different
1:42:23
like testing for embedding models and LLMs with Archon. He's the one that's actually working on the PR to like
1:42:28
really get things ready for Olama for Archon. And so he has um Promox is I
1:42:36
forget the the name of that that service, but he has it. So like he has an IP address for his machine like Olam
1:42:42
on his machine that he's pointing to with Archon hosted somewhere else and and so you can configure the ports and
1:42:48
everything for Archon in thev. So I'll actually go if you go to the bottom of
1:42:53
the readme for Archon, which by the way, remember if you just go to archon.diy, boom, there you go. It takes you right
1:42:59
to the repo. We have instructions for installing it here. But yeah, if you scroll down, we have um configuring
1:43:05
custom ports and host name. So we got some instructions for that. And so you can do like a specific IP address if you
1:43:12
have that like hosted with firewalls open for your machine. Um my home server is on a separate LAN
1:43:18
not accessible to the internet. I access it via Twin Gate. I think that should work. Now I haven't done a lot of that
1:43:23
myself. So, uh, John in the Dynamis community, he would be the one to, uh, talk to about that because he's he would
1:43:29
know a lot better than me. Um, yeah. So, like I think he's going to be active in
1:43:34
the GitHub discussions and things. So, yeah, I guess that's the other thing I forgot to call out. So, I hope that helps, Kevin. Like, it should be
1:43:40
possible, but you I would just read the config down here to get you started and then if you have more questions, like
1:43:46
John would be the one to talk to for that. So the other thing I wanted to say is the community forum that we have for
1:43:54
for Archon is going to be just right here in the GitHub discussions. And so it's just going to be it's it's really
1:43:59
nice like having things in the GitHub discussions. Um so that we have it in the same place where I can like
1:44:04
reference issues and PRs and things. So, aside from like Dynamus, the place to go deeper, if like you really want to be a
1:44:10
part of the vision of Archon, this is just the place for the public forum, which I will say again, if you guys
1:44:16
really want to dive deep into using Archon and being a part of the vision and contributing, like definitely check
1:44:21
out dynamis.ai because like we got we got some things happening here. And like I said, just like a whole another level
1:44:27
of energy for all of the initiatives that we have in the community for archon and context engineering. And uh like I
1:44:34
said earlier, I just got to pull this up again because like I'm going to be putting so much effort into this. We've
1:44:40
got the full half-day workshop, my full AI development workflow that I've got on August the 27th at the end of this month
1:44:46
here. So, a lot of what I am doing with you guys in this live stream is just freestyling and we're just playing
1:44:52
around with integrating BMAD with Archon kind of like for the first time. Like I haven't really done it before because like I said, I just want to show you
1:44:58
guys what it's like to really like do this from scratch. Like you're playing around with Archon for the first time,
1:45:04
just trying to figure out how you integrate it with your agent coding workflow. But like this is where I'll have a lot more structure showing you
1:45:11
everything that I do and how exactly I use Archon and context engineering and
1:45:16
providing just like a ton of resources for you guys to get started with like global rules and sub agents and PRP
1:45:23
templates based on what you want to build. Um, and that's actually another thing we're working on the community is
1:45:28
like a full context engineering hub of like different resources depending on your programming language and the project you want to build. So yeah,
1:45:34
definitely come be a part of this. Like I I said at the start of the live stream, but it's worth saying again like
1:45:39
just this workshop alone is worth the investment for the community. And that's the amount of I'm putting the effort in
1:45:45
to like say that's true and have confidence in that. So yeah, definitely check out dynamis.ai.
1:45:50
But uh yeah, let's go back to um I'll just refresh to make sure. Oh no, it was
1:45:55
already loaded here. So we got the 20 tasks for our project here. So it's starting all the way at the beginning
1:46:02
with initialize next.js14 JS14 with TypeScript and Tailwind.
1:46:07
Um, and then we get create API routes um for different things. Looks good. Build,
1:46:14
create the instance model form. Okay. All right. Good. Good. All the way to final testing and GitHub release
1:46:19
preparation, which maybe that's a little bit of overengineering, but yeah, within each of these tasks, we also have a description. So, we're giving more
1:46:25
context to whatever ends up implementing this, what exactly we're looking for. And here we're specifying things like
1:46:31
using externs. So it's very much referencing the plan that we have in our PRD. It's putting those things into the
1:46:38
descriptions here. Like we have our text stack being referenced throughout our tasks. And so everything is like very integrated here. That's the beauty of
1:46:45
it. And so now going back to my um architect here, there's a lot of other
1:46:53
things we can do. So, I'll kind of like continue with the common theme here of like I'm not going to be using
1:46:58
everything within these sub agents just to keep things concise, but I want to like show you guys some of the other things you can do with these different
1:47:04
sub aents with the BMAD method and probably some other things that could like integrate more with Archon as well.
1:47:10
So, our Winston is a devious little architect that didn't even introduce himself at first.
1:47:16
He can do a lot of other things. We can um do some more research if we wanted to. Like I could actually have him like
1:47:23
research best practices for architecture. Going back to Archon for the docs. We can have him create a
1:47:29
front-end architecture specifically, which if I had the time here, I probably would actually do this. I think that
1:47:34
would make sense because a lot of what I'm building here is relying on the front end being quite robust, especially
1:47:39
being able to like have terminal output for our different cloud code instances. Like definitely that would be important.
1:47:45
Um, however, to keep things concise, I'm going to clear. I'm going to say we're good here. We we got we got our tasks in
1:47:52
place. We've got our PRD. Like we have a scope of work. Um that's not the tab I
1:47:58
meant to show. I meant to go back to our con. So we got our tasks. We've got our PRD. Like we have all the context we
1:48:05
need to really start diving into the implementation. So our PRD plus our
1:48:10
tasks plus probably leveraging our knowledge base even more. Like that's everything that our development agent
1:48:17
now needs. And so there are some different agents within BMAD like we
1:48:23
have the dev agent. I could dive into using this. Uh we also have the
1:48:29
uh scrum master agent. If I wanted to invoke the scrum master agent, we could dive into these things. That's really
1:48:35
going to be that second part of the flow that we have in BMAD. So like we basically went through this whole
1:48:40
planning workflow and I know I skipped a lot of things but like we went through it and a lot of it is optional. And now
1:48:45
we've gotten to the point we're ready to go to the development workflow. And so we kind of go in a cycle here where we generate these stories based on our PRD.
1:48:53
I kind of did something a little bit differently in Archon where instead of stories, I more just have like the different tasks in our project. And so
1:48:59
now we can start knocking these off one by one. And in order to do this, I actually kind
1:49:06
of want to use PRP. Like I said, freestyling. I'm going to switch from BMAD to PRP. So we used BMAD
1:49:13
for the planning. And that's kind of equivalent to creating like our initial MD file where we're just describing
1:49:18
those initial requirements that we have to create our PRP. And so I'm going to do something kind of interesting here.
1:49:25
So within my uh VS Code, I'll I'll just pop this up quick. Within my VS Code,
1:49:31
the same place that I have BMAD set up, I also downloaded the um the starter for
1:49:37
PRP. So we have our two commands to execute and generate PRPS. I've got my
1:49:43
template to base a PRP off of. By the way, this is all available to you guys
1:49:50
in the context engineering intro repository that I've covered on my channel a couple of times. And so I'm
1:49:56
just pulling all of the like getting started stuff from this repository so we
1:50:01
can implement PRP because what I'm going to do is I'm going to take the spec the PRD that we generated with BMAD and I'm
1:50:08
going to turn that into a PRP so we can just start implementing it with all the tasks that we have in Archon as well. So
1:50:14
this might be a little bit of overengineering but I think this is cool to experiment with. So we're just going
1:50:20
to do it. We're going to go ahead and do it. So I'm going to do slashgenerate PRP
1:50:26
and then typically with PRPS you want to reference a file that has your initial
1:50:31
requirements but instead I'm going to say uh look at the or I'm going to say use the PRD we have in the archon
1:50:39
project and then I'm going to go back to archon because I got to copy that name again of the project here cloud code
1:50:46
instance manager Nex.js control center. There we go. So, copy this, paste it.
1:50:52
There we go. Okay. So, we're going to generate a PRP, which is going to it's going to take the PRD and turn it more
1:50:59
into a prompt for our coding assistant. So, we have things like validation gates, so it understands how to validate
1:51:04
its work. We're going to be more explicit with like the final codebase architecture that we want. And so, yeah,
1:51:10
I'm going to I'm going to let it run and do that. So, in the meantime, I will go ahead and
1:51:15
uh go to some comments that we got here. Uh, check out Ghosty. Super performant,
1:51:22
feature-rich environment, agnostic, modern terminal. Thank you for the donation and I appreciate the suggestion. I have actually heard some
1:51:28
good things about Ghosty for sure. So, yeah, I think it'd be cool to check out. There are so many cool tools that we can
1:51:34
check out for coding and context engineering and yeah, I have heard some good things about Ghosty. Is it is it
1:51:40
open source? I think it is. Um, because I thought I remember here, I'll have a GitHub.
1:51:47
Okay, they got a GitHub, so Oh, wow. Yeah, 34,000 stars. That's pretty awesome. MIT license. Good to see. Cool.
1:51:55
Yeah, know that's pretty sweet. I I've seen this. I haven't tried it myself, but I've seen it. And I know there's some people in the Dynamist community
1:52:00
that have tried it out and said good things about it, too. Which the Dynamist community is just the place where all
1:52:05
the ideas are shared. Like, it's pretty awesome. So, all right.
1:52:11
um would be nice if the community part was
1:52:16
open source on Discord or something. So yeah, when I talk about Dynamus, it's more like the place to dive deeper, but
1:52:23
we still have a free community just within the GitHub discussions here. So it this is a 100% public project. Like
1:52:30
don't get me wrong, we have the GitHub discussions and I'm going to be active here as well. So yeah, hope that helps.
1:52:36
I mean, this is kind of like the equivalent of a Discord. I just think this is going to work a lot better than Discord uh because it's easier for me to
1:52:43
manage and other maintainers because we're already in GitHub constantly with the issues and PRs and then within
1:52:49
individual posts it's easy for us to we can just reference issues and PRs when
1:52:54
things come up which I know there's a lot of um there's a lot there's definitely some bugs that we have to
1:53:00
work through right now but like I'm on top of it. We got maintainers. I've created I'm starting to create a full team around archon. Like there's a lot
1:53:07
of lessons that I've learned from other open source projects I've been a part of like bolt.diy where we didn't have extensive CI, we
1:53:15
didn't have GitHub discussions, we didn't have templates for issues and PRs initially and like I'm implementing all
1:53:20
those things and building a full team around it, even doing some hiring. So like like we're we're putting in the
1:53:26
work to make it so that Archon is a project that we're in for the long haul. So yeah.
1:53:33
Um Oh, that's pretty cool. Pretty much
1:53:39
ditch IDs with Ghosty in a three pane setup with cloud code integration. That's really cool. That is super cool.
1:53:46
Um, let's see. I guess I'll let me watch the terminal
1:53:53
here. Okay, so it's doing a web search as well. So, I'll I'll let it supplement the rag with web search. Might as well. I think I actually tell it to do so in
1:53:59
the global rules, actually. All right.
1:54:06
Let's see. So from Tim here regarding PRP templates, I saw a lang graph template uh separate panic AI template
1:54:12
in Dynamis. Is there an advantage to combining them all together into one overall template plus me0ero plus Neo4j?
1:54:20
Yeah. So uh Tim, I I I think this kind of goes back to your original question where I I wouldn't overengineer and try
1:54:26
to combine like a ton of different things together. I would focus on langraph
1:54:32
and then if you wanted to try to like use cloud code to combine lang graph with pantic AI together to create some
1:54:39
kind of global rule where it's like here are best practices and and strategies to like build langraph workflows with
1:54:46
pyantic AI agents you definitely could do so u but again I would just use like normal rag for like the mem zero neoforj
1:54:53
stuff and not try to like build a ton of that into the global rules be more like describing the core of your stack and
1:54:59
the architecture for that with like lane graph and pantic AI. So I would encourage you I'd actually love to see
1:55:04
it if you take those templates that we have in the context engineering hub and dynamis and you try to like combine it together. So it's like let's build with
1:55:11
pantic AI and lane graph and integrate them really closely like I do with module 7 in the course. Um definitely
1:55:17
like feel free to do that. I' I'd love to see it.
1:55:23
So yeah, great stuff man. I appreciate it very much. Um, great work on Archon.
1:55:29
Wait, hold on one second. Uh, why is it doing so much web search?
1:55:34
Oh, it's because well, yeah, duh. It's because we don't have Xterm pulled in the docs for
1:55:40
Oh, okay. This makes sense. Okay, this makes so much sense. So, I realized what's happening here. So, like for the
1:55:45
so the MCP server for Archon, there is a tool where we can actually ask it like
1:55:51
what sources do we have available? Like in my claw code, I have archon connected to claw desktop by the way. So I can say
1:55:56
like what sources do I have in Archon? So our coding assistant can actually
1:56:02
determine what what am I able to perform rag on within Archon. And so we'll see
1:56:08
in a second here. I'm just waiting for this to get back to me. Um
1:56:14
well here I'll just uh take that out in the meantime. So it'll it'll list out the sources that it has. I have no idea why Claude desktop is freezing on me
1:56:21
here. and and it'll tell me like you've got clawed code, you've got the nex.js
1:56:26
docs, that's what you have available to you. Um you don't have like the
1:56:31
websocket stuff, you don't have the exterm stuff. So it knows it has to do web searching for that because it wasn't
1:56:37
able to find that information when it was searching through rag and archon. So that's that's kind of another thing I
1:56:43
wanted to call out there. Um, I need to let me So, claw desktop sometimes it
1:56:48
freezes on me or like like it disconnects from the MCP and I have to reconnect it when I restart. Um, that's
1:56:54
another really good thing to know is when you restart Archon, you also have to restart the MCP client. So, I have to reconnect. So, now if I I should be able
1:57:01
to ask this question. It shouldn't freeze again because it it makes a new connection to the MCP
1:57:07
now. It should work otherwise. Yeah, here we go. All right. There we go. There we go. So, here are the four sources I have in Archon. I got panici,
1:57:13
cloud code, mem zero, and nex.js. It's perfect. Cool. And really neat as well,
1:57:20
you can you don't have to use archon with coding assistance. Like I can ask it questions about um I can ask it
1:57:28
questions about cloud code right here in cloud desktop. Like I can say, how do I call claude code with the
1:57:36
claude code SDK in Typescript? and it'll go and it'll perform rag just
1:57:42
like our coding assistant was doing but now it's just more of like a chat like we're not trying to implement anything maybe we're just doing some highle
1:57:47
planning right now and some architecture and so it's performing some rag queries and searching some code examples just
1:57:54
like we did in cloud code but now it's just within our chat it's pretty neat so
1:57:59
it's going to do a couple of queries here I have it prompted in a way like the tool descriptions for archon where
1:58:04
it'll like do follow-up queries to really refine its answer so here we go let's get our our information. Okay, if
1:58:10
we do the mpm install, here's our basic usage. And if you guys remember from earlier using that query that we import
1:58:16
from cloud code, this is like exactly right. So it it found probably both in the rag query and the code example
1:58:22
search the exact part of the documentation that I wanted it to find. Like I pull this up right here, like it
1:58:29
found um let me just reference it again. Like it found this exact thing. Like
1:58:34
this is what it outputed right here or pretty close at least. maybe adapted the example a tiny bit, but like yeah,
1:58:40
perfect. There we go. So, okay. So, now it's creating a comprehensive PRP. So,
1:58:46
it's going to take a while because PRPs are longer. So, in a second here, we'll see a PRP that is outputed
1:58:53
and it'll be within the PRP folder. So, we'll let it go um in a second here.
1:59:00
So, I'll go back to the chat in the meantime.
1:59:06
All right. Okay, there we go. So, it's looking to create Oh, wow. This is looking good.
1:59:12
Um, I'll go to the chat anyway, but I'll let it create this here. So, I'll say, "Yep, you're good to create this file."
1:59:19
Let's see. Uh, really good question from Jonathan. Can I hack the NSA with Archon? No, you cannot. Sorry.
1:59:29
The main benefit of Dynamus is the community. Yeah, honestly, I mean, there's a lot of parts to Dynamus, like the course and the workshops, everything
1:59:35
I've been talking about, but yeah, even just the community is just such a big deal. Like the ideas that people share with each other is insane there, and
1:59:42
it's just amazing to be a part of it. Um, so
1:59:48
yeah. Um, how is Archon? Okay, no, this is a really good question. Let's talk about this. How is Archon better than
1:59:54
Context 7? Yeah. So, Archon, I mean, there's a lot more to it besides just
2:00:01
claw taskmaster and context 7, but some of the core things for Archon, at least until we like really start to expand the
2:00:08
vision pass beta, the core parts of Archon is really we've got task management like we have with Claude
2:00:14
Taskmaster and then we have knowledge like we have with contact 7.
2:00:20
But first of all, it's better because it has these things combined into one MCP. Also, it's just a lot easier to manage
2:00:27
things because we have a beautiful user interface. So, like with Claude Taskmaster, it's a nice way to give the
2:00:33
coding assistant a way to manage tasks internally, but it's quite hard for us to actually manage things ourselves. Like, when we're within Archon, as it's
2:00:41
implementing these different tasks, uh, wait, uh, okay, never mind. as it's implementing these different tasks, we
2:00:46
can actually go in and like fix the description or we can add another task without even having to interrupt our coding assistant because interrupting
2:00:53
can a lot of times lead to hallucination. And so it's our way we manage with the UI, the coding assistant
2:00:58
manages with MCP and it's all realtime connection and that we don't have that with other MCPS. And then then with uh
2:01:05
contact 7, contact 7 is pretty awesome. Like I I covered it on my channel and that video actually did really well.
2:01:11
It's an awesome MCP, but the thing is it's not your own private knowledge base. You don't get to pick the sources
2:01:17
that you have in there. Um, I think you can actually like add docs, but like it's just become this bloated mess.
2:01:23
There's so many different libraries that we have in there. Um, and so with Archon, you actually get to build your
2:01:28
own private knowledge base. And there's a lot of different rag strategies that I'm implementing, even more to come for
2:01:34
things like re-ranking and hybrid search. And you can actually configure them yourself. You can toggle them on
2:01:39
and off. And so there's a lot of room for customization, things that are going to keep building out as well. And also,
2:01:46
Context 7 is not open source. And Archon is and will forever be an open- source platform. Contact 7, their MCP is open
2:01:53
source, but if you actually go and look at the code for Context 7. It's a super simple MCP that calls into a private
2:01:59
API. You don't get to see any of their implementation or code and they're going to be monetizing it. So yeah, awesome
2:02:05
MCP, but there clearly are some differences with that and Archon. Context 7 is going to be easier to use,
2:02:11
but you can't really customize it. I think that's really what it comes down to. So yeah, that's a really good question, though.
2:02:20
Um, let's see. Got another donation. Thank you very much for the donation. Will the live stream be available for
2:02:26
watching later? Switching to Linux, by the way. It's way better for development or switch to Linux. Yes. So the live
2:02:31
stream will be available later. Definitely 100%. So all live streams on YouTube are automatically uploaded after
2:02:37
some processing time. I don't actually have to like record it separately myself or anything. And then uh switching to
2:02:43
Linux, I appreciate the recommendation. Um I've thought about it definitely and
2:02:48
like whenever I'm hosting something in the cloud, I'm always using an an iuntu Linux instance. So yeah, I mean I have a
2:02:55
deep respect for Linux. Um but I like Windows for some of the things that like Linux doesn't have. Um, like, okay,
2:03:02
don't quote me on this, but between OBS, Cap Cut, and Photoshop, like the three main tools I use for video editing, I
2:03:08
don't think all of them work with Linux, or at least not as well. From some research that I did before, maybe that's
2:03:13
not 100% right, but yeah, I'm just very comfortable with Windows, and I've been using it since I was, you know, what, like six years old. I started with like
2:03:20
a Windows XP laptop back in the day. Um, so yeah.
2:03:27
Um, let's see what else we got in the chat. Oh, this is a good question from
2:03:33
Emerson. Any any members of Dynamus that aren't developers? Curious what the expectation is for those without coding
2:03:38
skills? Yeah, that's a really really good question. So, uh short answer, not everyone is developers. Definitely not.
2:03:45
We have a lot of people that are more beginners getting into AI and building automations and agents. the the I would
2:03:52
say that the only requirement for Dynamis is that you have an aptitude like a hunger for diving into these
2:04:00
things not necessarily becoming technical but getting comfortable with no code tools like NAN learning how to
2:04:06
leverage AI coding assistance like if you have that desire then Dynamus is the place for you and there's so many
2:04:11
resources and courses and workshops and community and people sharing ideas for all of those things and so we there's a
2:04:18
a large audience of Dynamist or core membership of Dynamus that is technical.
2:04:24
A lot of people that are more semi-technical like they have an aptitude for building agents and automations that are just kind of
2:04:30
getting into it and leveraging coding assistance and then definitely some beginners as well. We have a lot of that. Um so there's a place for
2:04:36
everything and I and I really do create a lot of resources and content in the community and even the course like is
2:04:41
beginner friendly too. So yeah, definitely be a part of it if you're interested and you're just starting to get into these things.
2:04:50
Um, from Kev, thank you again for the donation. Appreciate it. After my home server question, Proxmox, that is the
2:04:57
one that I was uh trying to remember the name of because I haven't used it myself, but John is like big on Proxmox
2:05:03
and uh he uses it for running Olama in like a IP address connected into Archon.
2:05:09
Uh maybe a future capability to easily deploy to Proxmox VMC please. Yes, that
2:05:15
would be amazing. Yeah. So also back to the context 7 question, the other reason
2:05:21
that archon is special is because it's possible to host things 100% locally.
2:05:27
You can host superbase yourself. you can use Olama or at least the full support for it is coming very very soon for Ola
2:05:34
and so it's going to be possible to have everything entirely private and that's a huge advantage that a lot of people are looking for like you kept and so doing
2:05:41
things like what you're describing here making it easy to deploy to a local server like that is a priority for us
2:05:48
it's one of the things that we definitely want to add in like before we ever go out of beta like that will be in place 100%
2:05:58
um donation from daily profit dynamis is costlier for me or Indian community.
2:06:03
Yeah, I first of all I appreciate the donation. I totally understand. Totally understand. Um but unfortunately
2:06:10
geographical price parody is something I've looked into but it's not possible on my platform. We have a lot of people in India though. um and like they're
2:06:16
getting the value out of it that it's worth it even even for um even when like the currency doesn't go as far I guess
2:06:23
is the way to put it. I don't know how to word it best exactly but yeah I understand the concern but it's it's um
2:06:29
it would become a nightmare to manage like geographical price par where like depending on the region of the world the
2:06:34
price is different. It's like that's not something that uh like someone like one person starting a community can manage
2:06:41
very easily. There's no features in the platform for me to do that either. Otherwise, I would love to look into that because I want to like the price of
2:06:48
Dynamus is because people who invest in something, they end up getting more out of it. It becomes a commitment versus
2:06:56
something that's free. If people are just um investing their time and not money, like they get less out of it. It's like a it's a psychological thing.
2:07:03
Like it's real. And so like I if I could be more like geographical price parody like things like that, I'd do it. But
2:07:09
it's it's just difficult like gonna be honest. So yeah,
2:07:14
um Archon merch win. Also, um Mac OS is the way. So I did actually get a Mac
2:07:21
computer a couple months ago. Um my wife uses it for editing. She helps me edit my videos and also um what was the other
2:07:29
thing? Yeah. Yeah. So like testing like the local AI package and like Archon and stuff. I want to test on Mac as well. So I got it for that. Um, so I do have a
2:07:35
Mac, but I primarily use Windows because I'm most comfortable with it and I uh built a computer that can run local
2:07:41
LLMs. Um, that's better than the the Mac that I have. So, yeah.
2:07:48
All right, another donation here without a comment. Um, I hope that wasn't an
2:07:53
error mark, but I do appreciate the donation. Thank you very much. Appreciate it a lot.
2:08:00
um a one oneclick installer script for Archon. So yeah, I'm highlighting this
2:08:07
specifically because I don't know when we would get to this point, but I would definitely want to. I want to make it as
2:08:14
easy as possible for all of you guys to be able to use Archon, especially for people that aren't as familiar with open source and hosting things and superbase.
2:08:22
Like the setup instructions are quite simple compared to most open source projects, but there's still a couple of things that you have to get through here
2:08:28
and you have to be comfortable with a couple of things like setting up ENB and running SQL scripts. It would be awesome
2:08:34
to create a oneclick installer. And just in general, I want you guys to know that like we are putting so much effort into
2:08:40
making it as easy as possible to use Archon. like the onboarding flow that we added. Raasmus added that recently to
2:08:47
Archon and he's doing like some more things to like help you detect when you have your like anonymous key instead of
2:08:53
service key and like when your server is down and helping you look through the logs. Like we're we're working on those things, trust me. So, I appreciate you
2:08:59
mentioning that. Um, so yeah, let's actually go back in the terminal here because we have our
2:09:05
PRP. I'm going to get get back to the the coding for a bit, but I really appreciate being in the chat with you
2:09:10
guys. Um, so like I said, like we're we're going through this thing. I don't think we're going to build it from like fully build it here. Uh, because the
2:09:16
focus is just showing you how to integrate BMAD with Archon. And now we're talking about PRP as well. We're freestyling and I just want to talk with
2:09:23
you guys, have a chat with you guys and and answer your questions. So, I'm putting a lot of emphasis into that as well. But yeah, here is our PRP.
2:09:31
So, I'm going to open a preview of it so we can take a look. Uh, there we go. At our purpose, our
2:09:38
core principles, and our goal. So, we're following the base PRP. This is the template that we're basing this off of.
2:09:45
Um, let me go back. There we go. So, we got our Y. We got our what what we're building here. We got our success
2:09:51
criteria. Here's all the documentation that we want it to uh read through,
2:09:56
which that's good, but also I want to tell it to use archon as well. So, I'll
2:10:01
say use archon for cloud code SDK and nex.js docs.
2:10:08
Um, yeah. So, I'll just I think I'll just leave it there. That's good. So, within the documentation and reference,
2:10:14
I didn't really I should have been explicit in creating the PRP that I wanted to use Archon, but this is going to work as well. So, I'll just add it
2:10:19
here. Must read. You must use Archon for cloud code SDK and Nex.js doc. So, we can kind of more supplement the research
2:10:25
that we've already did with the Archon MCP. And then doing some research on like Xterm and and real-time patterns.
2:10:32
Looks good. Here's our desired code base. See, this this is beautiful. Like, this is what I like seeing. And claude
2:10:37
actually does a really good job at respecting the desired codebase tree. And so this is what our end result is
2:10:43
going to look like where we have um we have our API where we have the routes for managing cloud code instances. We
2:10:49
have the different components for displaying the terminal and the logs. Like this is really good. We've got
2:10:54
known gotas and then we have a lot of pseudo code here and the list of tasks that need to be implemented here which
2:11:00
I'm going to just tell it to use archon. So maybe there's a little bit of a disconnect here. Um but yeah, it looks
2:11:05
pretty close to what we actually had in in um Archon. So I might have even referenced it. I'm not totally sure
2:11:11
exactly, but yeah, then we just have a lot of pseudo code. So yeah, and then uh yeah, I guess the very last thing is the
2:11:17
validation gates or validation loops. So one of the really important parts of the PRP framework is telling the coding assistant how it can iterate and
2:11:23
validate its own output. So like with linting checks and we're going to have it write unit tests and integration
2:11:29
tests. Uh which I'm actually going to take out integration tests because that's probably too much for right now.
2:11:36
So I'm going to go ahead and take this out. So again, just like without with validating code that's outputed from
2:11:41
your coding assistant, you want to validate the PRP before you execute it. Make sure that it's aligned with what
2:11:46
you want to create and that it's not overengineering because that's another big thing that coding assistants do. Like I was talking about earlier, we got
2:11:52
our final validation checklist and then some anti-atterns here. So, we're looking good. And our confidence score
2:11:59
is not as high as I want it to be, but just for the sake of brevity, I'm going
2:12:05
to go ahead and kick this off. So, I'm going to clear the conversation
2:12:10
and I'm going to say execute PRP. And then the path to our PRP is PRP's claude
2:12:17
code instance manager MD. And then uh the other thing
2:12:24
is I'm going to kick this off. I'm going to say use the archon project for task
2:12:29
management and archon for rag. Um and then I'll say the project is and then
2:12:35
I'll go back into here. I gotta I keep I should just like
2:12:41
memorize this. Let me copy this. Cool. Go back in here and paste that. All right. There we go. Okay. And it
2:12:48
actually was checking for projects already. So it it knew to use Archon, but now I'm just being explicit telling it which project to use. So there we go.
2:12:54
So now now it's it knows which project to use, but it's going to look there already anyway. So all right, we're
2:12:59
using Archon right away for our implementation. And um
2:13:06
yeah, let's see. I'll go back to the chat for a second here. Actually, I um I
2:13:12
think I need to take a bathroom break. That's so silly. I've never done that in a live stream before, but it's like
2:13:17
getting so bad right now that it's like hard to talk. Um so I I think I'm going to mute myself
2:13:24
and uh you guys can watch this go in the implementation here and I'll come back in just like a minute. So I will be
2:13:30
right back. Oh, that I I turned off my display. I need to turn off my video. Okay, there
2:13:35
we go. All right, I will be right back.
2:15:14
Okay, I'm back. That was TMI, but that was the longest of my life. All right,
2:15:20
let's go. All right, so we're starting by creating a next app. Okay, so that's
2:15:25
good. So, we're we're taking the first task from Archon, which uh let me actually go and u make sure. Uh wait,
2:15:33
no. Yeah. Yeah. Okay. So, let me refresh because I need to start it up again. Um,
2:15:40
hold on. Okay, there we go. All right. So, we're
2:15:45
we're in progress with our first task here. So, this is perfect. So, we're initializing next.js and it's running
2:15:51
exactly the command that I hoped it would. So, it's running the create next app, which if you go to the Nex.js documentation and it um probably even
2:15:58
performed rag to figure that out. I didn't see exactly, but yeah. So, we have the right command. So, it's going
2:16:03
to create the boiler plate for an XJS project in our codebase. And there's quite a bit to go through here. I don't
2:16:09
think I'm going to get to the end of the implementation in this live stream for you guys, but you've seen the full process of integrating Archon with BMAD.
2:16:17
I mean, it is a little bit messy because I'm really figuring out for the first time, but like I said, that's very much intentional here.
2:16:25
Um, you left your mick on. Did I really? Wait, hold on. because I I
2:16:31
I did the mute button. No, I I muted it. I know I muted it.
2:16:38
Unless you guys are just trolling me,
2:16:44
maybe. I mean, I don't care. I mean, just means you guys heard me go.
2:16:51
All right. All right. So, let's see here. Echo Y.
2:16:56
Mike says no. Thanks, Mike. He was kidding. Uh, that's like every
2:17:02
every live streamer's worst nightmare though is accidentally leaving their microphone on. Um, wait, what is it
2:17:09
doing here? Okay, sorry. I wasn't paying attention to its output because it was deciding things for me for creating the
2:17:15
next app. Um, what is it doing?
2:17:21
You know what? I might just need to create it myself.
2:17:31
You know what? I might just run this myself. I I don't know if I trust it to to do everything right. So, let me go
2:17:37
into I'll just go in and run this myself. Open source bead app. Paste this
2:17:43
in. Okay, I'll run this myself because I I do want to use ESLint and Yeah. Okay.
2:17:51
Okay. There we go. So, I'm going to say so I'm going to go out here. I'm going to say no and tell Cloud what's to do differently. I'm going to say I created
2:17:57
the next app for you. Go ahead and mark this task as done in Archon and move on.
2:18:04
And I don't need to like explicitly say in Archon, but I'm just trying to be explicit here because I feel like that'll be helpful for demo purposes.
2:18:11
But yeah, I'll just have to let this run here to create the the boiler plate for the next app.
2:18:17
So, um yeah, here we go. We got the app created, which
2:18:23
actually I kind of want this outside. Let me reveal in file explorer. I kind of want to fix this up.
2:18:31
I'd rather just have this all out like that.
2:18:37
Then delete this. Okay. Wait. Why is it
2:18:46
Let me delete it. That's weird. Okay, I'll just leave that
2:18:52
folder. Whatever. That's fine. Okay, so now I fixed up the structure. Okay, now we're good. Now we're good. So, I'll go
2:18:57
back to my terminal and I'll close this one and I'll tell it to move on. Okay,
2:19:03
you're good. So, there's two things I could do here for the the rest of my
2:19:09
stream. I can either focus on a lot of your guys's questions
2:19:16
or try to get this implementation done. Um I think what I'm going to do, let me
2:19:22
go back to Archon. Make sure it's moving through the tasks fine. Okay.
2:19:29
Yeah. Okay. So, we're looking So, I'll I'll let this run here. So, we got one task that's done. Okay. Now, it moved on to the next one is in progress. So, now
2:19:35
it's installing configuring cloud code with Xterm. Okay. So, we're good. So, it's moving through the implementation. Now, the rest of this we're just going
2:19:41
to have to wait a while because it's going to have to knock through all these tasks, but you can very much see that it's doing so and it's leveraging archon
2:19:47
and this is beautiful. Uh, and it yeah, it says to MP install some things. So, I think I think the plan here Yeah. And
2:19:55
you guys are saying questions. I think we're going to do that. We're going to do that. So, I'll let this run and I'll like try to pay attention and like approve things if I need to. But I
2:20:02
definitely want to um chat with you guys more, answer some questions, and then
2:20:08
continue to talk about the the long-term vision for Archon. So, I think the plan is to I'll let this live stream go uh
2:20:14
I'll I'll end it in 40 minutes for sure, cuz at that point, it will be a three-hour live stream, which I'm down
2:20:20
for that, guys. I have so much fun with these. Like, the time flies so fast. Like, it still feels like it's um the
2:20:27
streams are only going on for one hour, not two hours and 20 minutes. So yeah,
2:20:32
but I hope that you guys can see there there's like two big things that I wanted to show you guys with this live
2:20:37
stream. One is I wanted to take you deeper into actually leveraging Archon,
2:20:43
showing you guys the power of it from the perspective of kind of more just like experimenting with it. Like it's
2:20:50
nice to have something that's super super structured like my video on Wednesday, like boom boom boom, here's a demo. Here's something I already prepped
2:20:56
for you guys. But then there's also a lot of value in just doing something really off the cuff like I've done here.
2:21:02
The the word freestyling that I've been using way too much this live stream. Like it very much is true. And there's a
2:21:07
lot of value in that. And so like I wanted to just show you guys like Archon from scratch. Like let's just play
2:21:13
around with it. Let's dive into the different features. And then the other big thing that I wanted to show you guys that I think worked out very well is
2:21:19
showing you how to use Archon with a different context engineering strategy like BMAD. Because one of the things
2:21:26
that um I've seen some people comment that I I just want to be very clear on and I hope that this demo made it clear
2:21:32
is that Archon in no way replaces your existing strategy. It is additive. It
2:21:37
has rag and task management. those two components of context engineering that a
2:21:44
lot of other strategies don't have like PRP
2:21:49
um claude flow BMAD spectrum development like they have they kind of have it but
2:21:55
like archon does that part like that's where it specializes and so that's that's what I wanted to
2:22:01
show you guys and I think it it ended up working really well doing BMAD with um with uh Archon. So yeah, there we go. We
2:22:07
we finished this task. We're moving on to the next one now. So, it's looking good. Cool. Cool. Yep. So, we're
2:22:12
updating the next one to doing. So, what what task is that here? I guess. Yeah. So, it uses a task ID, but yeah,
2:22:18
basically what is in doing now is we're creating the cloud SDK wrapper class with TypeScript. And there we go. We got
2:22:25
our description as well. So, sweet. All right. And and by the way, I could like update the description in real time and
2:22:31
like have it reference the task again if I wanted to correct it. So, without even having to interrupt it, I can fix
2:22:36
things. That's the one of the nice parts about the task management that we have in Archon. So yeah. All right. So that's
2:22:42
a little bit of like a recap of what I just wanted you guys to get out of this. So uh yeah, let me go back to the uh the
2:22:49
chat here. Another question that I saw that I appreciate a lot is um this one
2:22:54
here. So why why use superbase and not just another or local database? So quick
2:22:59
answer for this one. I'll try to be kind of concise more concise in answering some questions here. So nice and quick
2:23:06
one for this is um Superbase is just the easiest to work with. I love their Python SDK. So that's why we started
2:23:12
with it. Uh I kind of wish I implemented like just Postgress from scratch though.
2:23:17
And at some point we definitely want to move archon to supporting all Postgress databases. So still superbase like local
2:23:25
or not. Uh Neon self-hosting like just vanilla Postgress. We want all that to be possible. So instead of giving the
2:23:32
superbase URL and service ro key in your env string for Postgress which can be
2:23:38
superbase still. So we definitely have that in the future.
2:23:44
Uh what are we building again? Yeah. Okay. So I'll I'll give a quick recap of that what what it is currently working
2:23:50
on here. So uh what we're building is a front-end application to manage
2:23:56
different cloud code instances. So we we're the end goal is to have a UI
2:24:02
kind of like this where we can like spin off different cloud codes to to code different things for us and then we can
2:24:07
like easily click between the different terminals to see the logs and maybe even have them like coordinate together and stuff like it's the kind of application
2:24:13
where you just want like a a nice UI for managing cloud code just like archon's a nice UI for managing our knowledge and
2:24:19
tasks. So that that's what it's currently coding here and we went through the whole BMAD process to like plan things in a lot of detail and we
2:24:25
created a PRP that we're executing now. uh definitely cutting some corners to speed things up. Like I said, you you
2:24:31
certainly want to spend a lot more time with your analyst and your project manager and validating your PRP. And I I
2:24:37
don't want you to um do what I Yeah, I want you to do as I say, not as I do,
2:24:42
right? Like I'm I'm just telling you how I'm speeding things up, but in general, you want to do a lot of validation
2:24:47
yourself. So yeah.
2:24:53
Um let's see what else. All right, another question here. Good
2:24:58
question. Let me go back to my stream. I want to ask again, wouldn't it be better idea to have ready-made boiler plates to
2:25:04
start with and have the agent choose the best one that fulfills most requirements and build on that? Yes, definitely. And
2:25:11
um yeah, that's one of the things that I was talking about earlier for one of my long-term visions for Archon. So, I I
2:25:18
love talking about the long term for Archon because as exciting as it is what we have built right now, there's so many
2:25:23
more things we have to make it like way better. And so let me talk about that again. And this might be like a little
2:25:28
bit of reiterating, but still it's it's it's really cool to talk about and just like get our brain juices flowing for
2:25:34
what's what's possible with a tool like Archon. So one of the things that we have in the Dynamis community
2:25:43
is I've kind of been referencing this but I haven't been showing it yet. We have the context engineering hub. So,
2:25:49
this is private to the Dynamus community, but I definitely want to like share a lot of these resources um with
2:25:54
all of like just to my YouTube channel as well. But one thing we're working on in Dynamis together
2:26:01
is we're working on the context engineering hub. This is going to be
2:26:06
basically a a gold mine of resources for PRP templates and slash commands and
2:26:11
global rules and cloud hooks and sub agents that everyone is contributing together as a community. He started this
2:26:17
like really recently actually. And so the goal with one of the goals with this is to eventually integrate it
2:26:23
with Archon where Archon can look at this context engineering hub and it can say and you
2:26:29
would tell it like I want to build a Nex.js application or I want to build a pideantic AI agent and archon will
2:26:36
search through these different things just like it searches through knowledge with rag and it'll be like oh sweet here
2:26:42
is the pyantic AI PRP template. So you have a boilerplate like you said Ramy
2:26:48
and like oh here are some slash commands uh in uh cloud hooks and sub aents that will work well to help you build out
2:26:53
this agent and then oh here's the Python global rules like if we go to our global rules here and we're continue like we
2:26:59
just started building this out so there's not a ton here yet but we're working on a lot of resources here like here here's Raasmus' global rules that
2:27:06
he uses for all Python applications and so Archon would pull this because you're building a Python podant AI agent and
2:27:12
then it would go into your knowledge you' be like, "Oh, you're building with Pantic AI, so let me go ahead and and find the what I want to crawl for Pantic
2:27:20
AI, and then I'll go ahead and crawl that and add that, and then I'll make a new project for you in Archon." So, you have like all this boiler plate set up
2:27:25
for you to just like And by the way, look at how much it implemented already. We're already on task eight out of 20, which is pretty sweet. Uh, but yeah,
2:27:32
anyway, like that that's like the the dream for Archon to make it so that it is the command center for all context
2:27:38
engineering, just getting you started no matter the project that you have. And a lot of that does rely on us building out
2:27:44
this context engineering hub. But this and archon are like the two big things
2:27:49
that we have going on in Dynamis. Maybe that like and the AI agent mastery course where I show how to build agents
2:27:55
from start to finish. So like I said, a lot of really exciting things going on in the community. So if this sounds
2:28:01
interesting to you, like if you want to dive in and contribute and even just leverage these resources and be a part of the long-term vision for Archon,
2:28:07
dynamis.ai, that's the place to check out. So, I'm going to plug it again because it just relates so much to what
2:28:13
we're talking about here. Um, and everything that we got going on. So, yeah, let me go back and see where we
2:28:18
are at with Claude Code. Okay, so yeah, it's just chugging away like it's it's killing it. Nice job,
2:28:26
Claude Code. Actually, I want to look at our codebase, too, and see what we got so far. Um, so we got our dashboard
2:28:32
component. Oh, it just created the instance card. Nice. Yeah, it's looking good.
2:28:38
Um, has it done anything with Okay, so it hasn't created any API endpoints yet. So, I guess that'll probably come or no,
2:28:45
it has it. Uh, okay. So, it's just kind of created
2:28:50
the boiler plate at this point. So, nothing nothing too crazy yet, but yeah, we we'll let it we'll let it go. I'll
2:28:56
get to more questions in the chat here. All right. What hardware is it required
2:29:02
to run on? Good question. So, Archon is pretty lightweight overall. I'll go into
2:29:08
my Docker desktop. So, right now, Archon in total is using a little over one
2:29:13
gigabyte of RAM for all four containers. The the server is the biggest one. So,
2:29:18
you don't need that much memory. You certainly don't need the best CPU unless you are using local large language
2:29:25
models. You don't need a GPU at all. Like, you should be able to run Archon on any laptop. All that to say, it's
2:29:31
pretty lightweight. Yeah, good question though.
2:29:37
Will this video be on your channel after? Yeah, so Edia, good question. I do actually want to um tomorrow post a
2:29:45
kind of like live stream recap where I'll just like highlight the the big things that I've been covering here. Um
2:29:50
so I have to think about like how I want to structure that and it'll probably be like I I hope to make it like around a half hour like really consolidate a lot
2:29:57
of the things that we've been talking about here. But yeah, I want to do that.
2:30:03
Um what else we got here?
2:30:09
Yeah, I'm seeing some So, for all you guys that are saying some nice things here, um like priceless when it comes to
2:30:16
value, I assume you're talking about Dynamus cuz I was talking about Dynamus, but yeah, thank you very much. So, sorry I can't like showcase every single nice
2:30:21
comment in the stream, but just know that like I'm reading those guys and uh like it seriously means a lot. So, like thank you very much. I I always love the
2:30:28
positivity in these streams and um it's part of why it's so easy to go for so long cuz you guys are nice. besides the
2:30:35
occasional trolls and and all that has to happen, but like you guys are really nice in general and and it means a lot.
2:30:43
Um, what time is it for you? It is 11:30 a.m. for me. I'm in Minnesota, so
2:30:48
central time. All right. Um,
2:30:54
where does graffiti and Neoforj fit into Archon? Do we want to learn from experience?
2:30:59
Yeah, good question. So, we don't have graffiti and Neo4j built into Archon
2:31:05
yet, but we are starting to to do some experimentation behind the scenes and
2:31:11
just like thinking about brainstorming how we'd want to do so. The the main way that knowledge graphs will fit into
2:31:17
Archon is um well, I mean, there's a couple of cool ideas. Like, this will be
2:31:23
kind of off the cuff because we're we're like just starting to brainstorm it, but like let me share a couple things. The
2:31:28
first thing is that knowledge graphs are actually a pretty great way to store a codebase because you have like your
2:31:35
different classes that all have methods and then those methods have attributes and functions um or attributes. Well,
2:31:43
no, I said that wrong. Your classes have methods and attributes. So like you have like a hierarchy of things like files
2:31:49
have classes, classes have methods and so you can have a knowledge graph that like stores a code base or even like a
2:31:56
external library and then archon can um like with graffiti like it can expose functionality to the MCP server to like
2:32:03
search through your codebase as like just another way to index it um or to search through the right syntax for um
2:32:10
external libraries like I did with some of the knowledge graph experimentation and the crawl for AI rag MCP. So there's
2:32:16
there's a possib a lot of possibilities there. The other thing that we could do with knowledge graphs is we could take
2:32:23
like one thing that the BMAN method does that I didn't cover here is they there's a lot of this like concept of sharding
2:32:30
where you'll take a PRD and you'll split it into different stories and epics kind
2:32:36
of like you have in like Jira if you guys are familiar with like Jira or ClickUp or just like more like project manager kind of stuff um that I'm sure a
2:32:43
lot of you guys are familiar with and um one thing we could do with knowledge graphs and arch on is take that kind of
2:32:50
sharding that the BMAD method does and create a knowledge graph of all the different stories and epics and how they
2:32:56
relate kind of as a way to um build a long-term memory around like the
2:33:01
different things that were done and like how the features were related to each other and even like dependencies that
2:33:07
they had on each other and things like that because it's all very relational. And this also gets to the last thing
2:33:12
I'll say again the really like offthe cuff here but like interesting things to think about. Um, we had that question
2:33:18
earlier about like using the entire cursor chat history as long-term memory for the agent. And my suggestion there
2:33:24
was more like I would actually like get to like different checkpoints in your code and have it output a markdown file
2:33:30
with like a summary of what it changed and like what's next, like that kind of thing.
2:33:35
Now, that would be another cool use case for knowledge graphs because you could have all these markdown files that are
2:33:40
like checkpoints for your codebase and like the different checkpoints will have like different features that are related
2:33:46
to each other. It'd be kind of like stories and epics, but like like that would also be a cool thing to store in a knowledge graph so that Archon could
2:33:54
expose tools through MCP for your coding assistant to like search through past implementations so that when you're
2:34:01
working on a brownfield project, an existing codebase, you can more easily see like even without having to search
2:34:07
through the codebase, what are the like architecture patterns that I need to be following here for a new feature? because I'll just search through the
2:34:12
knowledge graph to find existing feature implementations, the ones that are like the most similar to what I'm about to
2:34:18
implement. And then I'll just copy that structure for the codebase because generally you want to keep your codebase consistent with um your formatting and
2:34:25
the different like um patterns that you're developing in your codebase. So yeah, just yet another cool idea there.
2:34:31
So I know that it's kind of like random thoughts all over the place. Um but it's just fun to brainstorm that kind of thing. So I'm just sort of doing it live
2:34:37
with you. But yeah, I appreciate that question. Oh, can't get enough of your vibes, bro.
2:34:43
God bless you. I appreciate a lot, Ahmed. Thank you very much. We just have fun on these live streams. That's what
2:34:49
we do. Freestyling. Um, let's see. I need to read through and
2:34:56
find the next one to showcase here.
2:35:04
Um, okay. Is Docker Yeah, good question. Is Docker Desktop a requirement or can I spin up a Linux box with Docker and run
2:35:10
Superbase and Archon on that and connect remotely? Yeah. So, uh, two things. First one is
2:35:16
you do not need Docker Desktop. I guess I added it more as a prerequisite
2:35:26
like quickly click into the container to see the logs and see if there's any errors that they want to share in their issue when they report it, things like
2:35:32
that. And so then people don't have to learn like you know docker ps- a or like
2:35:38
the docker log-f docker compose like you don't they don't have to like learn the syntax of those commands if they just
2:35:43
have docker and docker compose and not desktop. Um so actually I don't need it to run
2:35:49
npm rundev. Um don't run npm rundev because that's
2:35:54
going to hang. So okay sorry I have to like make sure this keeps going too. Um anyway so yeah you you can use just
2:36:00
docker. My warning though is um Archon does not have authentication right now. It's meant to just run locally. So if
2:36:06
you host it in the cloud and you expose it, unless unless you like have some way to like securely access the machine
2:36:13
that's not over the internet, then I wouldn't recommend doing that because it's not Archon's not protected. There's not a way to add your own authentication
2:36:20
into it. In the future, we definitely want to we want to make it so that like you can configure your own O so you can
2:36:25
host it remotely and like have your friends log into it or or your co-workers or whatever. Um, but then
2:36:31
it's it's like exposed the internet but not like unsafe. Um, but like right now it's meant more to just be run locally
2:36:36
just as we're in beta.
2:36:45
I just shorted in my Right. Whenever whenever um the BMAD method says
2:36:50
sharding in their documentation or in their YouTube videos, I I think of that as well. I'm going to be totally honest.
2:36:56
Like, yeah. Um,
2:37:02
knowledge knowledge graphs are a great source for training data generation. Yeah, 100%.
2:37:10
Um, okay. This is a good thought. Your projects aren't separate islands. Link a
2:37:17
task from project A to B with one click. When you update in one place, it updates everywhere. Yeah, I mean that's that's
2:37:22
true. I mean, I'd have to like dive in a lot deeper with you to like see exactly what you're getting at, but like in general, I agree that like your projects
2:37:28
aren't separate islands, especially because like one thing you can do in Archon, um, is like,
2:37:35
and I haven't done this myself, but I know Sean, one of the other maintainers I've been talking about, like he he has
2:37:40
Look at We're almost done, by the way. We got three um three tasks in review.
2:37:46
We're almost done here. Um, I lost my train of thought. Was it? Oh, yeah. Yeah. Okay. So, one thing that I haven't
2:37:52
done, but like Sean's done it, I've seen some people do with Archon, just when it was in Alpha in the Dynamis community, is they will manage different stories
2:37:59
for the same workspace codebase in different Archon projects. Because
2:38:04
sometimes, like I made things simple enough where I broke it down into 20 tasks, but if it's actually something
2:38:10
nuts like this where it is 124 tasks, then it makes sense to split things up more and have different coding agents
2:38:16
managing different projects in Archon, even though it is the same codebase. And in that case, you definitely would want
2:38:21
to be able to link different tasks between projects in Archon. I agree 100%. So yeah, there's definitely a lot
2:38:28
of different ways that we can expand the task management here and make it a lot more robust both for the UI and the MCP
2:38:34
server for the agent to be able to do those kind of things itself. Like maybe even having Okay, this would be so cool.
2:38:40
making it possible for sub agents that are operating on different projects in Archon to be able to communicate with
2:38:46
each other and like come to an agreement on how they want to link things between projects. That sounds kind of dangerous,
2:38:52
but also like really really cool. Like just get your juices flowing for the kind of things that we could do with
2:38:58
Archon. There's so many possibilities. Um,
2:39:07
you're all good. Don't worry about being late. Just happy to have you here. Keep up the great work. Can't wait to dive in. We'll be working heavy on this
2:39:12
today. Just got my 5090. Well, congrats. That's cool. 5090s are a beast because
2:39:17
Yeah, you got you got um 32 gigabytes of VRAM with that, don't you? That's pretty cool.
2:39:25
Um let's see.
2:39:31
Yep. So, this is going to be the live stream will be available for playback and I'm going to do a recap video as well probably end of this weekend.
2:39:42
Let's see. Oh, cool. Wagner Hey, Cole just joined tested Archon. It's so helpful. Thanks a
2:39:48
lot. You bet. Glad to hear it. Yeah. And if you guys want to just like share in general things you built with it, I'd appreciate hearing that a lot, too. But
2:39:54
yeah, getting a lot of feedback already on Archon. It's super positive. And and I'll be totally honest, like there there's people having problems with it
2:40:00
and there's bugs with it because it's in beta. We're working through those really hard. Maybe not as hard this weekend.
2:40:06
going into next week, we're going to be working our butts off on a lot of these things and really touching up Archon in beta. But like aside from that, like a
2:40:13
lot of really positive feedback and it means a lot and I'm glad that that our vision is coming to life in the way that
2:40:18
we hoped it would be and that you guys are are using it in the ways that we dreamed that people would and that we're
2:40:23
using it oursel. It's really cool to see. Um, so yeah. All right,
2:40:32
let's see. Okay. Yeah, another good question. Um, can I add context manually
2:40:37
and just use the task management from archon? The answer is yes. So if you want if for some reason you really want
2:40:43
to use context 7 as u for your knowledge or if you want to just like upload your
2:40:49
own documents into the codebase and reference those for documentation like we've done with PRP before and you don't
2:40:55
want to use archon for that but you still want to leverage other parts like docs or tasks, you can definitely do that. And so it's all up to you. Um, let
2:41:03
me pull up Archon again so I can answer this with a visual for you. If you go to
2:41:09
the uh global rules here, this is a template to get you started. Here's our
2:41:15
recommended global rules to give to your coding assistant so it understands how to use archon pretty well. But you can
2:41:22
you can change this however you want. You can specify in the global rules
2:41:27
never use rag with archon. Only use it for task management. If you want to, you can do that. And you can even I mean
2:41:35
that's kind of like an easy way to just disable certain features. Just tell the coding system to not leverage those. Instead, go to this folder where I have
2:41:42
documentation uploaded for um my business or the libraries I'm using. Um
2:41:47
you can definitely do that, Alex. So yeah, 100%.
2:41:52
All right, let's see. Yep. So yeah, full recording
2:42:00
will be available after some processing time. You just have to go to the live tab of my channel and it'll be available. And I got the recap like I
2:42:06
said. So yeah, what about the integration with block or
2:42:12
goose? So the basically any coding assistant that supports MCP can use
2:42:18
archon. We just only call out a couple here just to keep it concise. But like
2:42:23
really if you look at the docs for how to connect Archon to the coding assistants we lay out here. You can
2:42:30
extrapolate that just following the guide from that other coding assistant on how to add MCP. Like I believe Goose
2:42:37
MCP I believe they have MCP support.
2:42:42
Um maybe do they not? I don't I I haven't used Goose myself before.
2:42:50
This is the one from Jack, right? Isn't it? Um or maybe I'm thinking of
2:42:55
something else. Like if I go to X, does that go to Yeah,
2:43:01
never mind. I'm probably thinking of something else. But yeah, if it supports MCP, then you're good. I'm not 100% sure
2:43:06
if it does. I haven't used it myself. Well, all right. What else we got in the
2:43:13
chat here? We've got a donation. Thank you very much for the donation. Did the YouTube as a source feature get
2:43:18
installed? Uh, so no, we haven't implemented that yet. I mean, right right now, I'll kind of tell you guys
2:43:23
like medium-term goals for Archon. So, short term, like very short term,
2:43:30
there's just there's some things to like really polish up with with Archon. Uh,
2:43:35
like for example, if you go to the docs tab, um, like the docs aren't like perfect yet. Like if I go to the
2:43:41
markdown editor, there's like some like things like this where it's not rendering the object like little things
2:43:46
like that. There's some sometimes the crawling gets stuck. Like there's little things like that. Like we really really really want to polish what we have now
2:43:52
in the short term. And then there's um some improvements we want to make around like how easy it is
2:43:58
to get it set up like I talked about like improving the onboarding flow. A one-click install might not be in the
2:44:03
short term, but like something getting to that. Um yeah, just like we want to make it really easy to use and we want
2:44:09
to make it like work 100%. Like that's the short term for for beta. And then
2:44:14
medium-term, we want to start to integrate some of the things that I've been dreaming up with you guys in this live stream here, like how it can
2:44:20
integrate with your all your context engineering and like pulling in templates. Um things around knowledge
2:44:26
graphs we're talking about or extending the task management. Um maybe just like
2:44:31
refining the global rules that we have that we recommend adding in so that it can leverage archon better, integrating
2:44:38
with different context engineering strategies like BMAT, like all those things are a priority. other forms of of
2:44:45
knowledge like other sources. I don't not sure exactly when that fits into our timeline, but like something like being
2:44:51
able to ingest YouTube videos. I don't it's hard for me to imagine like where that fit into the coding process. Um,
2:44:58
however, I will say that at some point, and this is like guys, there's so many things for Archon. This is yet another
2:45:04
long-term thing possibility for Archon. Archon can be more than just coding.
2:45:09
Like I want you guys to like wrap your your head around this for a second. We can do so much more than using Archon to
2:45:15
assist with AI coding. Like what you're seeing in Claw Desktop here, it's just a
2:45:21
way for it to like perform this these advanced rag searches on anything that
2:45:26
we upload. Like this could literally just be like the backbone of any agentic rag system that we have. And archon can
2:45:32
be where we do the ingesting and how we have like our advanced search strategies like hybrid search and reranking and
2:45:38
things implemented in. So it's just like out of the box super powerful rag and it's not even doesn't have to be for coding. This could just be for our own
2:45:45
business documents that you can already upload or or like you're saying bro truth it can be just for YouTube videos.
2:45:50
You can search across videos on a channel that you want to catch up on. Like we could literally use archon for
2:45:55
that. Like I'm just using it in claw desktop. It's not even through a uh a coding assistant. And so that's yet
2:46:02
another thing like Archon could become general enough where it's just like the MCP server to make rag better no matter
2:46:08
what you're doing with agents ever. And that would just be so cool. Like we can literally do that. Um so yeah. Okay. Um
2:46:16
our application is it actually ready? Okay. I'm going to try this. I I doubt it's going to work
2:46:22
first try because I cut a lot of corners to just like speed up things and show you guys the whole BMAD. But let's try
2:46:29
this out. Actually, this would be so cool if we at least get some kind of visual here.
2:46:35
Uh, let me make sure npm install. Let me make sure everything's installed first and then I'll try to run it. Okay, npm
2:46:41
rundev. Um, okay. No errors. Oh, that'd be so cool. All
2:46:48
right, let me let me spin this up.
2:46:56
Uh, okay. So, it looks really bad. It looks so bad. I guess maybe there's
2:47:01
an there must there's probably a tailwind issue.
2:47:07
Yeah, there's a tailwind issue. Okay, so so the the uh CSS isn't working. It's probably a simple thing, but
2:47:18
help me help me make a million dollars. Create instance.
2:47:25
Okay, that's actually really cool. Um,
2:47:31
okay. So, we got another error. Okay. So, we got a couple of errors, but like clearly it's like kind of there. Um,
2:47:41
there's two things we'd have to fix. Okay, let's try to fix I'm actually
2:47:46
Let's try to fix these. So, I'm going to go back to my cloud code and say I'm getting this error for tailwind CSS.
2:47:55
And then also uh when I start a claude instance, I get this error and it is
2:48:02
stuck on what is it stuck on right now. So I'm just trying to be like kind of specific here. Usually when you're troubleshooting things with coding
2:48:08
assistance, it's helpful to be like quite specific on like when the error is happening, what the error is. So it's stuck on processing prompt this error.
2:48:16
I'm just typing this off camera really quick. So I'm going to copy this. Uh if I go to the issues that we're getting.
2:48:22
Uh there we go. If I look at the I forget how to Oh, yeah. Here we go. Um,
2:48:28
I'll just copy the full call stack here. Okay, there we go. So, I'm sending it
2:48:34
in. I accidentally pasted the call stack twice, but it's probably fine. But, yeah, let's just have it lock out these
2:48:39
things and we'll see what we can get. So, I'll just be ready to run it again here. But, okay, that'd be so I mean, we
2:48:44
got like kind of something. It looks terrible, but um I there's no way I would expect to oneshot this application
2:48:52
even if I spent a lot of time architecting and validating the PRP,
2:48:57
which especially because I didn't like I definitely wasn't expecting it to be great out the gate, but I I feel like
2:49:04
just just with like my intuition and experience with coding assistance and what I was looking at there, I don't and like how specific the errors were, I
2:49:11
don't think we're that far from at least having something pretty cool. So, I don't think like I'll probably wrap up the stream in the next like 12 minutes
2:49:17
here. So, we probably won't have anything that I can like really show, but um I mean we're like we're like there
2:49:23
kind of well, sorry. We're there to the the first iteration where we can now start to just do the troubleshooting, which I mean that's kind of the boring
2:49:30
part is doing the troubleshooting. I don't want to walk you guys through that.
2:49:35
Um, but yeah, I I will say though, um, maybe like the last time that I'll just uh mention this really quickly for you
2:49:41
guys is if you do want to see something that like is really really end to end, like super structured, let's come ready
2:49:47
with something like that I know is going to work and we'll actually like dive into the full process, not cutting corners for speed. That's what this
2:49:53
workshop is for. So the half-day workshop, my full AI development workflow where I'll I'll go through like
2:49:59
the full strategies that I actually use because again, today was BAD plus archon, more experimental. Let's play
2:50:04
around with something like more from scratch. This is going to be something that's going to be a very structured
2:50:10
interactive session that you can follow along all my strategies all in one session. So definitely come be a part of
2:50:16
Dynamus if you sound if that sounds interesting to you. So we got this happening Wednesday, August 27th, but
2:50:22
also definitely sign up this weekend because prices are increasing for the community. So you can lock in your price forever if you sign up this weekend. So,
2:50:29
just wanted to call that out because it's uh yeah, it's kind of like the next step if this was interesting to you in
2:50:35
general, but you want to like really get practical and concrete in a way that you can like apply things and I'll be like
2:50:41
speaking a lot more also to like how you can be applying these things to your AI development workflow versus this is more
2:50:46
like experimental and showcasing. So, hope that makes sense. But yeah, let's um let's check on Okay, so it's still
2:50:52
working on some fixes here, which um
2:50:58
I don't it's kind of random. This is weird.
2:51:03
I don't like this because it's like instead of trying to fix the underlying problem with Tailwind, it's just like adding u styles without Tailwind. This
2:51:10
seems like it might be hallucinating, but that's okay. That's all right. We'll let it go. We'll
2:51:16
see what happens.
2:51:21
All right. Hm smoke dab. Your archon is goated. Thank you very much. I appreciate smoke
2:51:27
dab. Uh donation from Johnny. Thank you
2:51:33
Johnny. Appreciate it. Congrats on the launch. Cole. Will the stream be available later? Yes, it will. Yep. So all all recordings or all live streams
2:51:40
for YouTube are available if you um after just some like processing time when the stream ends. It'll be available
2:51:45
in the live tab of my channel. And then also I am planning on doing a recap video that'll probably go out tomorrow
2:51:51
night. So yeah,
2:51:57
thanks Jay. Thank you Cole. Great launch party. Glad to be a part of your community. And thank you and Sean for all the hard work on Archon. You're very
2:52:04
welcome. Yeah, thank you Jay. And uh appreciate everything you've been sharing in the community recently as
2:52:09
well. To be fair, even at this stage of the project, this one shot would have taken
2:52:16
weeks before these tools. Exactly. Yeah. You're you're saying what I should have said anyway or what I should have said
2:52:22
to begin with is like even though it like looks terrible right now. I guess I
2:52:28
can't like show it again because it's in the middle. I tore down the site but like even though it like looked really bad like even just like getting this
2:52:35
boiler plate up and running and like we know that we're relatively close to an implementation like creating all this would have taken so long without AI
2:52:42
coding assistance and trust me been there done that. I've been coding since I was 8 years old and I did not have
2:52:47
coding assistance until last year. I I never even used like GitHub copilot or anything. Like when coding assistants
2:52:53
first started to be a thing, I got to be honest like at first I was like these things aren't worth my time and like the
2:52:58
tab autocomplete like before we had like full agentic coding it just wasn't impressive for me and I only used it a
2:53:03
little bit. And so like last year is when I really got into coding with AI starting with Windinsurf. Wind surf was
2:53:09
my first ever like full agentic coding assistant or at least at the time what
2:53:14
was considered like top agentic coding. I mean obviously it's what was then is not anything compared to like what our
2:53:20
tools can do now even like half a year later but still it was that was the code back then but um yeah so like all
2:53:27
everything we created here is like working yeah maybe 80% like you said
2:53:33
it's the 8020 rule. We got 80% of the way there in like an hour, couple hours.
2:53:38
Like it's super cool. And we're going to keep iterating on this and hopefully get to the point where it is
2:53:44
uh we'll get something here. Maybe in like the last couple minutes of our live stream at least I'll have like a nice UI. That'd be really cool. So we'll see
2:53:51
how far we can get. It's just doing some last checking here. So I think we're almost done with this implementation or
2:53:56
with the fixes that I asked it to perform. Um so cool. I'll I'll go through a couple more questions and then
2:54:01
hopefully we can spin it up again and try it out. Yeah, you're very welcome. Great demo.
2:54:08
Appreciate it, Mike. Thank you very much. Part two of the live stream, Martin. Yeah. No, I I won't be able to
2:54:15
do a second part tomorrow, but I got the recap video. And and also the other thing that I want to say is with my
2:54:22
channel going forward, one of the big things that I want to do is I just want to showcase a lot of like full builds
2:54:30
um like using archon, using PRPs, and like doing a lot of like agent development I think is something that I
2:54:36
want to focus on. So, if I go to my channel really quick, let me just go to YouTube. Or maybe I'll do this off uh
2:54:42
camera so I can pull up my um channel
2:54:49
the polls here. Okay, so let me show this here. So,
2:54:55
yeah, the poll that I put out a couple weeks ago, I asked what AI center content you want to see more of. And I
2:55:01
actually thought context engineering would win. I was kind of surprised, but building complete agents like full use
2:55:06
cases. This actually won by a landslide. There's 1.5,000 votes here. And so
2:55:11
something that because I went down to one video a week on my channel, so I could put more time into each video. And so one of the things I have with that is
2:55:18
I I think it'd be super cool to like showcase like full agent builds. Like here's start to finish. Let's build an
2:55:24
agent. Let's use archon for task management and MCP. We'll use cloud code and we'll use our strategies for context
2:55:30
engineering. So, like, excuse me. Really like going through and giving you guys all these examples of building agents,
2:55:36
showing you kind of the the culmination of all these different strategies and stuff that I've been talking about on my
2:55:42
channel. And then the big thing with that is then like if you want to go even further and like dive really deep into
2:55:49
everything that goes on behind the scenes to build agents start to finish, that's when you go to Dynamist. So, it's like the YouTube video is like you can
2:55:55
see me do it at a high level, but it'll I'll probably go like kind of quick because it has to I can't make like a
2:56:00
10-hour video every time. And so, then it's like if you really want to go through the AI agent mastery course to understand my thought processes and like
2:56:07
really dive into it with me, that's when you go to Dynamist like that. It's kind of an idea I have for for content for the channel. Um because it also is like
2:56:14
what you guys are really looking for. So, I think that'll be super cool. But yeah, looks like we
2:56:20
um we got our fixes in. So, I'm going to try running this and we'll see if we get
2:56:26
an error. Uh, okay. So, no error this time.
2:56:32
Let me refresh. Oh, no. We are getting errors. Actually,
2:56:38
it's even more broken now. Thanks, Claude. Looks like you're trying to Okay, Claude
2:56:44
messes up with Tailwind so much. Like by the way guys, this is why I use Lovable or like a tool like Horizons or Bolt for
2:56:51
uh building front ends because the weird things like it it screws up the boilerplate configuration so much. Like
2:56:57
it's just not understanding Tailwind here. So I'm just going to paste in this. I'm going to get kind of lazy here
2:57:03
because we're low on time. I'm just going to copy this error and paste it in.
2:57:09
And then I'll say um in the UI I'm getting this error because there's a
2:57:14
separate one that I'm getting here right now. Like it's not even it's not working. So I'm going to send this in.
2:57:22
Make this simple and fix it. Real prompting, guys. This is clearly
2:57:28
what I do on a day-to-day basis. But I'm just kidding. I'm just being lazy here because we're pretty low on time. Um but
2:57:35
yeah, I hope that we can get to something in a sec. But yeah, great stream. Thanks, Paul. I appreciate it.
2:57:41
Um, we need something similar to nearest neighbor, but for rag, allowing the
2:57:47
model to reference past knowledge and group them by association. Yeah. Yep. And that's what knowledge graphs are
2:57:52
for. One of the things that we're looking into 100%. Mike said, "Thanks for all the good
2:57:58
work." You're very welcome. I appreciate it, Mike. And and guys, thank you for everyone for being here. Like, this is a
2:58:04
record attendance for the live stream. Um, I know that like since the stream has been going on for a really long time, the the concurrent viewers isn't
2:58:11
as much right now as um was at the start, but we were at like 600 at one
2:58:16
point towards the start of the stream. Like that that is incredible. Like I'm humbled by that. So, thank you everyone
2:58:21
for being here. All your amazing questions and comments and your encouragement and uh going through this
2:58:27
this whole process with me. I hope this was valuable for you guys to see what it's like to just kind of go like the bottom up like I'm taking BMAD. never
2:58:34
really touched it before. Yesterday doing a little bit of prep like let's dive in and implement it with Archon and
2:58:39
see how we can do context engineering strategies with Archon. So yeah,
2:58:46
love to see a video where Archon could benefit from other creators products. AI community is amazing and and up to some
2:58:52
amazing work. Yeah, definitely. I mean that's kind of what I'm doing here at BMAD. Like there the creator behind
2:58:57
BMAD. Like that's that's it. That's his thing. And so I'm I'm hopefully doing
2:59:02
him a big favor by by show showcasing this because I think he deserves it. But yeah, I'd love to do more of that for
2:59:08
sure. Grateful for catching this live. Ah, glad to have you here, Bobby.
2:59:15
Um, let's see. Sorry, other creators could
2:59:20
benefit from Archon. He copied. Oh, you're good.
2:59:25
Claude keeps better um with Shad Cen. Yeah, that's fair. U and actually like
2:59:32
tools like lovable, they use shad cen by default. Um though I think isn't it common to use
2:59:39
shad CN and Tailwind together? I think that's a common combination like Tailwind is more like let's provide like
2:59:46
different classes for CSS. Shad CNN's like preconfigured components more, isn't it? Maybe I'm um misremembering.
2:59:56
I'm relying on coding assistance too much now, so I forget. Uh, yeah.
3:00:04
All right. Well, yeah, I'm going to end the stream relatively soon here, but I want to see the end of this.
3:00:11
Go faster. No, I'm just kidding. That's going to cause Okay. Well, the problem is we're almost at the auto compact, which is terrible, and that's going to
3:00:18
be long and probably cause problems. So, I hope that it can finish it soon. Um,
3:00:24
okay. I'm going to try something right now. I'm going to try running the server even though it's in the middle of stuff just because maybe it's to the point now
3:00:29
where it's working. Um Oh, okay. It is. It's kind of It's getting
3:00:36
there. This is cool. Okay, now we got a real UI. So, we fixed the we fixed the stupid Tailwind stuff for the most part.
3:00:42
Um Oh, yeah. So, it's just running the the type checks at the end here. So, I think it is pretty much done. Okay.
3:00:48
Well, yeah, 24-hour stream. Definitely not a 24-hour stream. Um, if you guys uh if
3:00:55
you guys look on my live tab on my channel, I do have a 12-h hour stream from before I really started diving into
3:01:01
YouTube. Um, I'll just leave that there and move on. But yeah. Okay. So, create a new instance. Code review assistant.
3:01:09
Help me make a million dollars. All right. Create instance. Okay.
3:01:17
I don't see any logs. And okay, so 2% right before the auto
3:01:23
compact we finished and it's um view terminal. Okay, so doesn't look like
3:01:29
it's working. So, okay. So, I don't know. I don't know
3:01:36
if we're 80% of the way there. Like I said, it's the expectation that especially cuz I rushed through some of
3:01:41
the things that it's not going to be like perfect perfect, but like we've got something to start with and Vive coding
3:01:47
is never going to get you 100% of the way there. And we definitely did like Archon helps with structured approach,
3:01:54
context engineering, but what we did today rushing through things was more vibe coding than I'd want to do
3:02:00
definitely. Um, but like I hope that like I explain things well enough like when you'd want to dive in deeper so
3:02:06
that you understand how to not vibe code as well. So it's like let's go through things quick, but I'll speak to like
3:02:12
when you'd want to slow down. I hope that makes sense. And so we definitely could be making this a lot better if we
3:02:17
put more time into it. But yeah, I mean it's we've got something working here.
3:02:23
It's um yeah, just like I mean there's requirements that we weren't clear on. Like another thing is like I feel like I
3:02:30
need to specify a directory. Like why is there no place to say here's the folder for you to operate in? Like I think
3:02:35
that's a problem as well. But also like if I was really meticulous in reading through the requirements and the spec
3:02:40
and the brief like I would have caught that like oh it's missing that like let me add that in or tell it to and like
3:02:46
those are the kind of things that you'd want to validate where like clearly I just wasn't clear enough on like what parameters I need here or maybe I could
3:02:53
be more clear on like how that connection is set up with websockets and like there's probably something in in
3:02:58
the in the PRD where if I really read through it I'd understand like okay this is the missing piece that it has to make
3:03:03
it so that like we're not actually getting the logs here um from the coding assistant. So yeah, all that to say
3:03:09
there's a lot of ways that we could have made this process better, but we got something started and also I think this was a good demo of how to use archon
3:03:16
with BMAD. So yeah. All right.
3:03:22
Yeah, I know you aren't a big fan of vibe coding. When done with love and care and using the right ingredients and experience, almost anyone could get that
3:03:27
dopamine hit of instant results. Well, yeah, that's very true. I mean, vibe coding is fantastic for proof of
3:03:33
concepts and like just diving more straight into implementation kind of like what I did today um to an extent
3:03:41
like there's a time and place for that. But when you really want the best output possible and actually when you do want
3:03:46
to develop something that's like really production ready the fastest, it is worth spending a lot of time up front
3:03:52
with your context engineering. And that's one of the big things that I I've really been pushing recently u because I just think it is so important.
3:04:00
So yeah. All right. I'm going to go ahead and move to the um
3:04:08
and let me clear this. All right. All right. So, yeah, I think I'm going
3:04:14
to go ahead and wrap up the stream now. I've been talking for three hours straight, and I think I'm going to take uh most of the day off and and get that
3:04:22
recap uploaded tomorrow. And uh I'll um I'm going to be super active in Dynamis
3:04:27
tomorrow as well. And then going into next week, well, I mean, I always am, but uh yeah, I know that I already heard
3:04:33
from my wife that there's influx of people joining Dynamis, which I appreciate a lot, guys, because we're going to be doing some amazing things
3:04:40
together. So, yeah. All right. Um, I'm going to eat some lunch, too. Right.
3:04:46
Yeah. I have not been drinking any water. I have I have my water here specifically so I could drink,
3:04:53
but I I never remember to do that while I'm in a live stream. I always forget.
3:04:59
There was one live stream a couple ago that I did. I actually gave myself co
3:05:04
like I brought coffee to the live stream and I remember holding it up at the start of the of the live stream. I'm like, "Here's my NN mug. I got coffee
3:05:10
because we got a a a chill casual live stream today and I'm going to be sipping my coffee and then I sipped it once the
3:05:17
entire live stream because I totally forgot about it because I get so into it. Like you guys have no idea how much
3:05:22
it takes like mental effort to be like watching the chat, watching my stream and like kind of checking on viewership
3:05:28
and then like diving into Claude Code or whatever and and like it's a lot but it's really fun. Like it's so worth it.
3:05:33
So yeah, thank you everyone for being here and being a part of Archon. Um, as you can see, like not perfect right now,
3:05:40
but it's freaking awesome and there's so much more that we got coming really soon for it and a really amazing long-term
3:05:45
vision. So, yeah, definitely check out Dynamus if you guys want to be a really big part of it. Um, but also like it's
3:05:51
totally public open source project and we got a public community as well. So, yeah, options either way for you guys,
3:05:56
but big things coming for Archon short and long term. So, thank you everyone
3:06:01
for being here and following along and your questions and comments. Hope that you guys have a great rest of your
3:06:08
weekend. And with that, I will see you guys in the next video.