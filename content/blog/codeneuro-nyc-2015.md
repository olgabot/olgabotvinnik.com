---
title: "CodeNeuro NYC 2015"
date: 2015-04-12T17:25:59-04:00
draft: false
tags: [programming, conferences, bioinformatics, neuroscience]
categories: [conferences]
---

<p>Last weekend I attended the <a href="http://codeneuro.org/2015/NYC/">CodeNeuro NYC</a> conference, which is a conference for neuroscientists, programmers, and everything in between. It was a unique experience because it had both the excitement and energy of a tech conference, and the pure, unadulterated zest for knowledge of a scientific conference.</p>
<h2 id="day-1-talks-and-panel">Day 1: Talks and panel</h2>
<p>The first day of the conference started after the workday on Friday at 5pm at the <a href="http://www.newmuseum.org/">New Museum</a> in Little Italy, Manhattan, NYC. This was the first time I'd been to this place and it was really awesome, even from the outside! Check it out, plus some other photos I took from the conference:</p>
<blockquote class="imgur-embed-pub" lang="en" data-id="a/q3c57">
<a href="//imgur.com/a/q3c57">codeneuro nyc 2015</a>
</blockquote>
<script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
<p>(FYI If you want to look through all the tweets from the entire event, check out this <a href="https://storify.com/yangbodu/codeneuro">Storify</a> board.)</p>
<p>The conference kicked off with some mingling and beer. I gravitated towards the three I knew people coming in to the conference, <a href="http://www.janelia.org/people/scientist/nick-sofroniew">Nick Sofroniew</a>, with whom I did an <a href="http://www.janelia.org/student-programs/undergraduate-program#722">undergrad summer program</a> and invited me to talk, <a href="http://www.jeremyfreeman.net/">Jeremy Freeman</a>, the main organizer of the whole freakin' thing, and <a href="https://twitter.com/bensussman">Ben Sussman</a>, who co-taught the <code>gitgoing</code> tutorial with me and is an all-around awesome person. But the space was rad, we had a balcony and a nice view of the city, and I got to meet a bunch of people doing super interesting things in neuroscience.</p>
<blockquote class="twitter-tweet" lang="en">
<p>
view from <a href="https://twitter.com/CodeNeuro"><span class="citation">@CodeNeuro</span></a>... <a href="http://t.co/kInTbaFWHW">pic.twitter.com/kInTbaFWHW</a>
</p>
— Angela Radulescu (<span class="citation">@angitweets</span>) <a href="https://twitter.com/angitweets/status/586659812198522880">April 10, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<p>We got started with the talks, which we had three 10 minute (ish) talks, followed by a half hour (ish) break. It was a nice format that we could chat and break in between the talks not only to get a mental break but also discuss the concepts presented by the previous talks in the context of neuroscience. Here's all the talks:</p>
<ol style="list-style-type: decimal">
<li>Adam Packer (UCL): All optical recording and manipulation of individual neurons</li>
<li>Eiman Azim (Columbia): Quantitative behavior and mouse genetics for probing motor circuit function</li>
<li>Randal Burns (Johns Hopkins): Open Connectome project using CATMAID [<a href="https://github.com/openconnectome/ocpcatmaid">github repo</a>]</li>
<li>Paco Nathan (Databricks): Spark for big data</li>
<li>Eliza Chang (The Data Incubator): PhD to Data Scientist</li>
<li>Michael Dewar (NYT): Real-time analytics on streaming data [<a href="https://github.com/mikedewar/codeneuro_streamtools">github repo for presentation</a>] | [<a href="https://github.com/nytlabs/streamtools">github repo for <code>streamtools</code> package</a>]</li>
<li>Hilary Parker (Etsy): Data science at Etsy (+<a href="https://twitter.com/CodeNeuro/status/586696965502689280">cute statistical plushies</a>!)</li>
<li>Brendan Lake (NYU): Teaching computers to scribble characters like humans</li>
<li>Olga Botvinnik, me! (UCSD): <code>flotilla</code>: An open-source Python package for iterative machine learning analyses [<a href="http://nbviewer.ipython.org/format/slides/gist/olgabot/2ee1087d74df46c842df#/">slides</a>]</li>
</ol>
<p>As you can imagine from the caliber of all the other talks, I was super nervous for mine! because I'm not doing things at exabyte scale, I'm not doing streaming data, and I'm not even doing neuroscience! I'm just analyzing static datasets with the usual machine learning algorithms. But as Jeremy pointed out, we need better tools for analyzing the existing non-big data datasets that we have, plus I got great questions and feedback from the talk which was great.</p>
<p>My top three favorite talks were:</p>
<p><strong>NYT R&amp;D demo</strong> This was a fantastic talk about streaming data analytics. He and his team had created an interactive way to analyze real-time data. They had a GUI interface where you could select boxes that represented an action on data (<a href="http://en.wikipedia.org/wiki/Extract,_transform,_load">extract, transform, load aka ETL</a>-like things), and you could string these boxes together to create an analysis pipeline. It reminded me a lot of the <a href="https://usegalaxy.org/">Galaxy</a> interface for reproducible bioinformatics pipelines. Check out the tweet below for a screenshot:</p>
<blockquote class="twitter-tweet" lang="en">
<p>
Picture of <a href="https://twitter.com/hashtag/realTimeData?src=hash">#realTimeData</a> including mine <a href="https://twitter.com/hashtag/codeNeuro?src=hash">#codeNeuro</a> <a href="http://t.co/VCIfFlFHTK">pic.twitter.com/VCIfFlFHTK</a>
</p>
— aybuke turker (<span class="citation">@aybuketurker</span>) <a href="https://twitter.com/aybuketurker/status/586678871942111232">April 10, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<p><strong>Optogenetics</strong>. This was a really interesting talk about <a href="http://en.wikipedia.org/wiki/Optogenetics">optogenetics</a>, which is a way that you can control the brain with light. Researchers genetically insert <a href="http://en.wikipedia.org/wiki/Rhodopsin">rhodopsin</a>, which is the light-sensitive protein that makes our eyes work, into neurons, which then makes them light sensitive. As a result, you can then turn specific neurons on and off with light! This talk used both this tool of optogenetics to stimulate/inhibit specific neurons, and calcium imaging to record their responses.</p>
<blockquote class="twitter-tweet" lang="en">
<p>
A. Packer shows some amazing tools to simultaneously record + stimulate ensembles of neurons with <a href="https://twitter.com/hashtag/CaImaging?src=hash">#CaImaging</a> and <a href="https://twitter.com/hashtag/optogenetics?src=hash">#optogenetics</a>. <a href="https://twitter.com/hashtag/codeneuro?src=hash">#codeneuro</a>
</p>
— Felipe Gerhard (<span class="citation">@neuroflips</span>) <a href="https://twitter.com/neuroflips/status/586685623068717056">April 11, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<p><strong>Spark</strong>. This was an awesome talk by <a href="http://liber118.com/pxn/">Paco Nathan</a> on using big data tools. Paco had worked with both Hadoop and Spark and gave a great overview of the history of Big Data (which he pinpointed to Q3 1997), the different papers about it and tools for it, and where Spark fits in that ecosystem. He gave a few use cases and was overall just a very entertaining presenter.</p>
<blockquote class="twitter-tweet" lang="en">
<p>
Great talk by <a href="https://twitter.com/placoid"><span class="citation">@placoid</span></a> at <a href="https://twitter.com/CodeNeuro"><span class="citation">@CodeNeuro</span></a> just now - apparently rotational bearings on planes create 12 exabytes of data / day... wow <a href="https://twitter.com/hashtag/bigdata?src=hash">#bigdata</a>
</p>
— Alice Lloyd George (<span class="citation">@AMLG23</span>) <a href="https://twitter.com/AMLG23/status/586689726196883458">April 11, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<p>After all the talks, there was a panel led by Jeremy with some giants of neuroscientists, Tony Movshon, Eve Marder and Larry Abbott. A recurring theme was that the fundamental questions of how the brain works hasn't changed, but the tools have drastically changed.</p>
<p>One story that stuck with me was Eve describing that when she was doing experiments, she used an <a href="http://en.wikipedia.org/wiki/Oscilloscope">oscilloscope</a> to listen (yes, with her ears! I thought this was amazing!) to the measurements from neurons, and there was a direct, phsyical, visceral reaction that when you designed an experiment and heard specific tones, you knew <strong>exactly</strong> what that meant, because you were intimately familiar with the exact tones and sounds produced by the device. But now, she said, the high throughput methods, while capable of measuring many things at once, are so detached from the physicality of neurons firing that she feels people aren't connected to what they're measuring anymore. I found that interesting because in my field of RNA biology, we'll do these newfangled <a href="http://en.wikipedia.org/wiki/DNA_sequencing#Next-%20generation_methods">high-throughput sequencing experiments</a> to measure RNA expression as a proxy for protein abundance, and study the <a href="http://en.wikipedia.org/wiki/Alternative_splicing">alternative splicing</a> of these RNA transcripts, but every time, we always have to validate our findings using an older, low-throughput method like <a href="http://en.wikipedia.org/wiki/Revers%20e_transcription_polymerase_chain_reaction">RT-PCR</a>. I don't know what the equivalent experiments are in neuroscience, because it seems all very magical to me that they're able to manipulate individual neurons in mice, but I also wonder if it's known that the neuron in the exact same position in one animal and another animal, do the exact same thing. So far, biology has relied on laws of averages, so if you do a high throughput experiment on a bunch of cells and get an average signal, you should get that same result if you do a low- throughput version of that experiment. I don't know what the equivalent of that is in neuroscience, but it was refreshing to hear that neuro has its own share of growing pains as its adopted its own high-throughput techniques, and that biology wasn't the only one.</p>
<p>It was interesting to hear about the challenges of neuroscience, of how excited people are about optogenetics, and how many people are apparently skeptical of <a href="http://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging">functional magentic resonance imaging</a> (fMRI) data, and how nobody knows what the <a href="http://en.wikipedia.org/wiki/Cerebral_cortex">cerebral cortex</a> does!</p>
<h2 id="day-2-tutorials-hackathon">Day 2: Tutorials + Hackathon</h2>
<p>The next morning we were in the <a href="http://www.newinc.org/">New, Inc</a> coworking space, and started off with some kickass bagels and lox/salmon:</p>
<blockquote class="twitter-tweet" lang="en">
<p>
breakfast begins <a href="http://t.co/55QljXZqkw">pic.twitter.com/55QljXZqkw</a>
</p>
— CodeNeuro (<span class="citation">@CodeNeuro</span>) <a href="https://twitter.com/CodeNeuro/status/586893786212651008">April 11, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<p>Then, people split up about 50/50 for the tutorials and the hackathon.</p>
<h3 id="gitgoing-tutorial"><code>gitgoing</code> tutorial</h3>
<p>Ben Sussman and I taught a tutorial called <a href="https://github.com/CodeNeuro/gitgoing">gitgoing</a> to quickly teach scientists the version control system <a href="http://en.wikipedia.org/wiki/Git_%28software%29"><code>git</code></a> and code testing via <a href="http://pytest.org/"><code>py.test</code></a> and integration systems via <a href="https://travis-ci.org/">Travis-CI</a>. We had about 20-30 attendees. The goal was to get the scientists acquainted with common tools in open source software so that they could contribute themselves. It was kind of like a mini <a href="http://software-carpentry.org/">Software Carpentry</a> workshop, but we assumed our target audience had some coding experience, and we didn't take the time to explain computer science fundamentals like variables, loops, flow control, etc.</p>
<p>Our class was structured exactly as laid out in the <code>README.md</code> file. First we setup their computers so they had <code>git</code> and Python 2.7. This took about an hour total to get everyone done. Some people finished faster and started moving on to the <code>git</code> section. Then Ben did an awesome explanation of <code>git</code>, and I learned a bunch of stuff! I didn't realize that when you <code>git clone</code> a repo, you're getting ENTIRE history of the project, so that makes sense why downloading all of <a href="ipython.org">IPython</a>/<a href="https://jupyter.org/">Jupyter</a> takes forever. It was also a really helpful analogy to describe the entire repository as an &quot;ocean of code,&quot; and that a branch is a single window into that ocean. We also talked about merge conflicts, and how they can be really easy to create if, say someone renamed one of the arguments of a function, and someone else added an argument, and then <code>git</code> doesn't know what to do anymore. They picked up on testing pretty quickly, and someone asked &quot;well <code>git</code> thinks it's okay, but how do you know the code will run?&quot; Which brought us directly to testing!</p>
<p>Next, I talked about testing and why it's important. I wrote some simple Python code with functions like <code>mean_plus_one</code>, <code>std_plus_one</code>, and <code>cv</code> (coefficient of variance). They were just slight variations on the true <a href="http://www.numpy.org/"><code>numpy</code></a> functions so the learners couldn't just use the <code>numpy</code> version. We looked at the test file, <code>test_gitgoing.py</code> which used <code>py.test</code>'s fixtures, which take care of the <code>setUp</code> and <code>tearDown</code> methods that some other testing frameworks have. We saw a simple example of fixtures, which creates a 20x10 matrix of normally distributed random numbers. These could have been set as integers, I just wanted to illustrate how you can create new fixtures from existing ones.</p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python"><span class="im">import</span> numpy <span class="im">as</span> np
<span class="im">import</span> pytest

<span class="at">@pytest.fixture</span>
<span class="kw">def</span> n_rows():
    <span class="cf">return</span> <span class="dv">20</span>

<span class="at">@pytest.fixture</span>
<span class="kw">def</span> n_cols():
    <span class="cf">return</span> <span class="dv">10</span>

<span class="at">@pytest.fixture</span>
<span class="kw">def</span> x_norm(n_rows, n_cols):
    <span class="cf">return</span> np.random.randn(n_rows, n_cols)</code></pre></div>
<p>There is a commented out broken test in the repo which they had to fix, which was a great formative assessment because they had to use their newly formed <code>git</code> and testing knowledge to fix the test, commit the changes, make a branch of their &quot;feature&quot; fixing the test, pushing to the branch, and making a pull request to the master branch. It was really rewarding for the students to see their pull request on Github, and to see their commits on the network of contributors to the <code>gitgoing</code> repo.</p>
<p>We unfortunately didn't advertise the #gitgoing hashtag before the tutorial so we didn't get any live-tweets, but Ben and I mitigated this and took a picture afterwards:</p>
<blockquote class="twitter-tweet" lang="en">
<p>
<a href="https://twitter.com/hashtag/gitgoing?src=hash">#gitgoing</a> at <a href="https://twitter.com/CodeNeuro"><span class="citation">@CodeNeuro</span></a>! Thanks <a href="https://twitter.com/bensussman"><span class="citation">@bensussman</span></a> for being an awesome co-teacher and everyone for coming! <a href="http://t.co/l0BUhoeWja">pic.twitter.com/l0BUhoeWja</a>
</p>
— Olga Botvinnik (<span class="citation">@olgabot</span>) <a href="https://twitter.com/olgabot/status/586980895397019650">April 11, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<h3 id="spark-tutorial">Spark tutorial</h3>
<p>After the <code>gitgoing</code> tutorial we had a break and mingled. Then, I went to the Spark tutorial, taught by <a href="http://liber118.com/pxn/">Paco Nathan</a> from <a href="https://databricks.com/">DataBricks</a> (slides <a href="http://training.databricks.com/workshop/dbc_intro.pdf">here</a>). I've seen Spark demos before but I haven't put in the time to play around with the tools, so this was a great way to get exposed!</p>
<p>I was a little late to the tutorial, so I missed the initial setup. I was handed a slip of paper with a url, username and password that was my personal login to the DataBricks cloud. Paco was doing a &quot;preflight check&quot; of explaining different Spark concepts before we dove in. The key things I took away were:</p>
<ul>
<li><strong>RDD</strong>: Resilient Distributed Dataset. This is the core unit of a spark analysis, where you load in data, and use Spark to indicate that you want it to be parallelized.</li>
<li><strong><code>sc</code></strong>: &quot;Spark context.&quot; This is the object that exists in all the Python library versions with Spark, and is the object that you will be using to create and operate on datasets.</li>
</ul>
<p>We used an IPython notebook-style <a href="http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop">REPL</a> interface, which was really nice because we could see the output from our commands right away. We continued with learning how to:</p>
<ol style="list-style-type: decimal">
<li>Read text files and separate lines by tabs</li>
<li>Filter for the first word of the line to be <code>ERROR</code></li>
<li>Get all the second words of the error lines</li>
<li>Find the errors that were caused by <code>&quot;mysql&quot;</code>.</li>
</ol>
<p>You can see a summary of my notes for this first section here:</p>
<div class="sourceCode"><pre class="sourceCode python"><code class="sourceCode python">lines <span class="op">=</span> sc.textFile(<span class="st">&quot;/mnt/paco/intro/error_log.txt&quot;</span>) <span class="op">\</span>
  .<span class="bu">map</span>(<span class="kw">lambda</span> x: x.split(<span class="st">&quot;</span><span class="ch">\t</span><span class="st">&quot;</span>))
errors <span class="op">=</span> lines.<span class="bu">filter</span>(<span class="kw">lambda</span> x: x[<span class="dv">0</span>] <span class="op">==</span> <span class="st">&quot;ERROR&quot;</span>)
messages <span class="op">=</span> errors.<span class="bu">map</span>(<span class="kw">lambda</span> x: x[<span class="dv">1</span>])
messages.<span class="bu">filter</span>(<span class="kw">lambda</span> x: x.find(<span class="st">&quot;mysql&quot;</span>) <span class="op">&gt;</span> <span class="op">-</span><span class="dv">1</span>).count()

<span class="co"># At this point, the data is loaded into memory on the workers and you don&#39;t</span>
<span class="co"># need to attack disk again, so this operation is very fast</span>
messages.<span class="bu">filter</span>(<span class="kw">lambda</span> x: x.find(<span class="st">&quot;php&quot;</span>) <span class="op">&gt;</span> <span class="op">-</span><span class="dv">1</span>).count()</code></pre></div>
<p>Yay, we learned how to read files! Always good :)</p>
<p>The next part of the tutorial, we learned how to use <code>flatMap</code>, and then how to <code>join</code> several RDDs on their <code>(key, value)</code> pairs. After the break, we had a mini lecture about &quot;Computational thinking&quot; where we had to use what we learned so far to find all the instances of the word &quot;Spark&quot; in two files. If you're interested, you can see my full notes <a href="https://gist.github.com/olgabot/ab058876b3bda6198f25">here</a>.</p>
<h3 id="hackathon">Hackathon</h3>
<p>The hackathon was centered around the <a href="http://codeneuro.org/neurofinder/">neurofinder</a> challenge, which is to try and extract neuronal signals from Calcium imaging data. The goals were go:</p>
<ol style="list-style-type: decimal">
<li>Refine a standardized API for &quot;source extraction&quot; algorithms, including input/ouptut formats</li>
<li>Work on evaluation metrics for algorithms and agree on ground truth definition</li>
<li>Work on incorporating existing algorithms into this API</li>
<li>Work on the frontend/backend of a website that would automatically run submitted algorithms on the test data, get the results and upload them to a leaderboard</li>
</ol>
<p>First, everyone introduced themselves and the group organically split into a few groups: the website, API input/output formatting, implementing algorithms, and designing metrics.</p>
<p>The website team was composed of five people with web development frontend/backend experience. They generated some prototype websites and code, all available on <a href="https://github.com/codeneuro/neurofinder">github</a>, and hopefully launching in beta soon!</p>
<p>Another group of about 25 worked on the API and the input/output formats, with their final notes added to <a href="https://github.com/CodeNeuro/neurofinder/wiki">this wiki</a>.</p>
<p>Another group of 10-20 split to work on incorporating existing algorithms in to this API. The rest worked on defining evaluation metrics for algorithms and the &quot;ground truth&quot; definitions of &quot;what is a neuron&quot; for these methods. They implemented some evaluation metrics, and developed an initial ground truth definition of manual centers and morphological boundaries. They discussed that this initial &quot;ground truth&quot; risks circularity, but is still a solid start.</p>
<p>There were still people working well into the evening!</p>
<blockquote class="twitter-tweet" lang="en">
<p>
the codeneuro hardcore, still rocking! <a href="http://t.co/TyxmlSNOZB">pic.twitter.com/TyxmlSNOZB</a>
</p>
— CodeNeuro (<span class="citation">@CodeNeuro</span>) <a href="https://twitter.com/CodeNeuro/status/587072775057231872">April 12, 2015</a>
</blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
<p>Afterwards, we all hung out at a nice dinner:</p>
<div class="figure">
<img src="http://i.imgur.com/KY9smQR.jpg" alt="CodeNeuro after-dinner party" />
<p class="caption">CodeNeuro after-dinner party</p>
</div>
<h2 id="acknowledgements">Acknowledgements</h2>
<p>Finally, I want to acknowledge all the organizers of the event:</p>
<ul>
<li><a href="http://jeremyfreeman.net">Jeremy Freeman</a></li>
<li><a href="https://twitter.com/neuro_nick">Nick Sofroniew</a></li>
<li><a href="http://graphics.stanford.edu/~broxton/">Michael Broxton</a></li>
<li><a href="http://www.mathisonian.com/">Matt Conlen</a></li>
<li><a href="http://web.stanford.edu/~logang/">Logan Grosenick</a></li>
<li><a href="https://twitter.com/dgangul1">Deep Ganguli</a></li>
<li><a href="https://twitter.com/hackingdata">Jeff Hammerbacher</a></li>
</ul>
