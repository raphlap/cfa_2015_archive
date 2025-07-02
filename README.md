# cfa_2015_archive
<a
href="https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/"
class="home-link" rel="home" title="Galactic Gazette">Home</a>

<a
href="https://web.archive.org/web/20150523035213/https://altbibl.io/gazette/on-archives-libraries-and-astrology/"
class="source-link" rel="source" title="On archives, library and... astrology">Source</a>

From February 9<sup>th</sup> to May 10<sup>th</sup> 2015 I had the
wonderful opportunity to be a fellow at the Harvard-Smithsonian Center
for Astrophysics for the purpose of producing, with the SAO/NASA ADS
(Astrophysics Data System) bibliographical data, a statistical study
about the citing behavior of French astronomers. While the goal of my
visit at the CfA was clear to me, many of my friends and relatives were
rather surprised that someone coming from the very Humanities-centered
<span style="color: #000000;"><span lang="en">*École*</span></span>
*Nationale des Chartes* and without any scientific knowledge other than
high school mathematics would be invited to work in the astronomy and
astrophysics disciplines. They were very right to be surprised as, even
to myself, this space travel had absolutely nothing obvious. The basic
purpose of my visit being, I concede, to learn data sciences and data
visualization, I nevertheless explored further than those very practical
skills and even discovered in myself a latent vocation of astrologer.

# <span lang="en">Epistemology</span>

“<span lang="en">Astronomy has always been a science of catalogs :
catalogs of stars, galaxies, quasars, and
planets.</span><a href="#sdfootnote1sym" id="sdfootnote1anc"
class="sdfootnoteanc"><sup>1</sup></a><span lang="en">” This assertion
of astronomer Joshua E.G. Peek is probably the first truth that I
learned while working at the John G. Wolbach Library. If indeed at the
beginning was the word, the word of my beginning was the one of the
august and late Williamina Paton Stevens Fleming, whose
journal</span><a href="#sdfootnote2sym" id="sdfootnote2anc"
class="sdfootnoteanc"><sup>2</sup></a><span lang="en">
[transcription](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/journal-of-williamina-paton-fleming-curator-of-astronomical-photographs-harvard-college-observatory/ "journal of Williamina Paton Flemming")
was among my first tasks at the CfA. Williamina Fleming, hired in 1881
by Professor Edward Charles Pickering, discovered no less than
aproximately 380 objects by classifying and cataloguing stars later
published in the Henry Draper Catalogue. Amazed by this vivid record of
astronomy in the making, I was very proud to consider myself a kind of
continuator of her work by producing transcription templates of some
manuscript notebooks : what better proof of the inherent human nature of
Information Technology than the process of making computer readable data
handwritten by a woman computer ?</span>

<span lang="en">Proud, yes, but also helpless : it is indeed very
difficult to produce a template of a table when, to a non-astronomer’s
eye, the metadata tend to confuse itself with the data it is actually
pointing at (see figure below)! Thus another assertion was
</span><span lang="en">*de facto*</span><span lang="en"> verified, as
the beautiful essay entitled [Life and Death of
Metadata](https://web.archive.org/web/20150523035213/http://lifeanddeathofdata.org/ "Life and Death of Metadata")</span><a href="#sdfootnote3sym" id="sdfootnote3anc"
class="sdfootnoteanc"><sup>3</sup></a><span lang="en"> puts it :</span>

<span lang="en"> “(…) it is quite apparent that metadata are neither
universal nor transparent, as various open data initiatives would have
us believe. They are constructed for local purposes and audiences. (…)
Indeed, as Bowker and Star documented in their classic work on
classification, metadata are cultural, not natural. They are created,
maintained and eventually discarded or replaced in craft practices that
vary over time”.</span>

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/Harvard-variables-300x239.png"
class="size-medium wp-image-1306 aligncenter" width="300" height="239"
alt="Harvard variables" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/Harvard-variables.png)

<span style="color: #4f81bd;"><span style="font-size: small;">**Figure 1.
Numbers, numbers everywhere!**</span></span>

Harvard Variables (noted as “HV.” on the upper left of the picture) are
house made metadata to designate variable stars observed at the turn of
the 20<sup>th</sup> century. As explained to me by Harvard’s Professor
Emeritus of Astronomy and the History of Science Owen J. Gingerich, each
object was given a consecutive number as it was discovered on
photographic plates at the Harvard Observatory. It is no coincidence
that the expertise of no less than an eminent historian of astronomy
would be needed to understand manuscript data. “The data, in and of
itself, is only valuable \[for\] somebody who understands its
significance” explains Peter Del Tredici in the essay previously cited.
Data (or “capta”, as Johanna Drucker would call it) is a human artifact
produced in a particular context and for a particular purpose; once
traces of those elements are lost, the inherent value of data is lost,
too. Indeed, astronomical data is to the astronomer as archives are to
the historian: a record of a past object from which the scientist builds
a sense meaningful to the very specific community being addressed. As
the archivist’s task is to select among the huge amount of human
activity records what documents will be most interesting to future
researchers, a space telescope’s task is to focus on some part of the
immensity of the cosmos according to the purposes of the most promising
research proposal soliciting it. Moreover, data from telescopes and
satellites need to be interpreted in order to be meaningful, whether
through the mere transposition of a light spectrum in
visible-to-human-eyes colors or through the more elaborate choice of a
particular red to describe the behavior and temperature of a solar gas.
This, in my understanding, testifies to the very symbolic nature of data
as both being part and sign, substance and conventional construction of
the object they capture. What, then, would better suit such a symbolic
object than the very artificial projection of data visualization?
“Indeed,” the author of <span style="text-decoration: underline;">Life
and Death of Metadata</span> writes, “visualizations are no more than
visual metaphors, translating various kinds of quantitative data into
spatial and geographical form.” Such a fact is very fortunate, as
learning data visualization was one of the purpose of my visit at CfA.

# <span id="_GoBack"></span>Methodology

It would not come as a surprise to say that data science looks a lot
like cooking. How do you make English pudding? How can we quantify
French astronomer Daniel Egret’s suspicion that astronomers from a
particular country tend to cite colleagues of the same nationality? And
if we had to pick France as a country for this study, would papers
written by mostly French collaborators tend to be cited by papers also
authored mostly by French people?

Step 1: building a python function that would request bibliographical
data of approximately 8600 records from the ADS API (Application Program
Interface). Then, for each of those records, making another request to
the ADS, mostly to get affiliations data of papers citing the records
obtained from the first request (see below).

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/diagramme-300x293.png"
class="alignnone size-medium wp-image-1307" width="300" height="293"
alt="diagramme" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/diagramme.png)

<span style="color: #4f81bd;"><span style="font-size: small;">**Figure 1.
Data cooking, step 1**</span></span>

In order to make things simpler for you, reader, let us call the papers
obtained from the first request “original records”, and the publications
obtained from the second request “citing records”.

Step 2: computing the proportion of French authors in the affiliations
of each of the original records, and then computing an average of the
same proportion for the group of paper citing each of the original
records. Thus, for each original record corresponds a proportion of
French authors, and also the average proportion of “Frenchness” of the
set of papers citing it. Here, you get that table:

<table data-border="1" width="590" data-cellspacing="0"
data-cellpadding="7">
<tbody>
<tr data-valign="TOP">
<td width="182"><h2 id="original-paper-identification-number"
class="western" data-align="JUSTIFY"><span
style="font-size: xx-small;">Original paper identification
number</span></h2></td>
<td width="183"><h2
id="percentage-of-french-affiliations-in-the-original-paper"
class="western" data-align="JUSTIFY"><span
style="font-size: xx-small;">Percentage of French affiliations in the
original paper</span></h2></td>
<td width="182"><h2
id="average-percentage-of-french-affiliations-of-the-group-of-citing-papers"
class="western" data-align="JUSTIFY"><span
style="font-size: xx-small;">Average percentage of French affiliations
of the group of citing papers</span></h2></td>
</tr>
<tr data-valign="TOP">
<td width="182"><p>xxx</p></td>
<td width="183"><p>YYY %</p></td>
<td width="182"><p>ZZZ %</p></td>
</tr>
<tr data-valign="TOP">
<td width="182"><p>xxx</p></td>
<td width="183"><p>YYY %</p></td>
<td width="182"><p>ZZZ %</p></td>
</tr>
<tr data-valign="TOP">
<td width="182"><p>xxx</p></td>
<td width="183"><p>YYY %</p></td>
<td width="182"><p>ZZZ %</p></td>
</tr>
</tbody>
</table>

Step 3: Trying to make something tasty with the ingredients you have
prepared. For example, just take the first and second columns of the
table and compute the cumulative distribution of **original papers**
according to their level of “Frenchness”, which gives you the following
histogram:

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/premier-graphique-300x208.png"
class="size-medium wp-image-1308 aligncenter" width="300" height="208"
alt="premier graphique" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/premier-graphique.png)

Then take each of the thresholds symbolized by these bins and, for each
of them, compute the distribution of **citing papers** according to
their level of “Frenchness”: you end with a series of 20 histograms
which, put together, draw a picture of the evolution of the proportion
of French affiliations of the citing papers according to the level of
French affiliations of the original papers being cited (…dear reader,
aspirin is in the kitchen). Now, it is only a matter of comparing the
distribution of “Frenchness” of the papers citing 0.0% French original
papers to the one of the papers citing 0.95% French original papers, to
observe a positive and distinct gap between the first and the later:

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/deuxième-graphique-300x158.png"
class="size-medium wp-image-1309 aligncenter" width="300" height="158"
alt="deuxième graphique" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/deuxième-graphique.png)

And if you really want to quantify the augmentation of the proportion of
French affiliation of citing papers according to the augmentation of
that same proportion for original papers, just look at the evolution of
the means and medians of each of the twenty distributions we obtained
earlier:

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/troisième-graphique-300x145.png"
class="size-medium wp-image-1310 aligncenter" width="300" height="145"
alt="troisième graphique" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/troisième-graphique.png)

Et voilà, bon appétit!

While reading my poor prose, dear reader, you may have wondered why I
was making much ado about something that we already knew by intuition.
But talking about bias in citation behaviors isn’t such a trivial issue,
when we know the importance of bibliometrics in today’s networked way of
accessing information.

“Citation and social computing indices,” writes Ronald Day, “begin with
social and cultural categories and create documents and persons (users
as well as authors) out of algorithms of information and communication
“needs” (Thomas 2012), which reflect these social and categories in
political circulation”<a href="#sdfootnote4sym" id="sdfootnote4anc"
class="sdfootnoteanc"><sup>4</sup></a>.

Thus, bibliographical data is of a very political nature, especially
when used to algorithmically rank documents or authors and ultimately
when it is involved in decision-making processes. How, then, can we not
be skeptical about the functioning of such content providers as Scopus,
which aims at offering “authors profiles which cover affiliations,
number of publications and their bibliographic data, references and
details on the number of citations each published document has received”
and then ultimately provides navigation means based on our very
sociologically biased citation
data<a href="#sdfootnote5sym" id="sdfootnote5anc"
class="sdfootnoteanc"><sup>5</sup></a>?

That access to scientific information – and access to information in
general, as the PageRank algorithm is the basic tool of Google – is a
sociologically and politically loaded matter should not be considered
*malum in se*. Rather, the question of designing a navigation tool able
to reveal and question this subjective nature while providing an
efficient way of finding unexpected and valuable documents in the
context of an attention economy is the one we should consider as a
priority.

I noted above that visualization had a metaphorical character, as well
as the data it is representing has a symbolic nature. This is how we
should read, in my opinion, Ronald Day’s statement about domain
visualization in sciences, which says that “maps of science are
representations of representations within a convenient metaphorical
vehicle (“atlas”, “maps”).” Then, if we want visualization to be one way
among others to call attention to the allegorical character of
bibliographical data, it is important, that this visualization would
carry an inherent playful and enjoyable aspect in order to maintain a
distance with its content.

For example, dear reader, will you find seriousness in my study, if I
present you the citation data that I used as flower-shaped (see below)?
If I tell you that each point represents a publication, each petal of a
flower cites its center, and that the more a point is blue, the more the
affiliations of the paper are French, what will you think of the fact
that most flowers whose center is blue tend to have blue petals too?
Will you directly jump to the conclusion that I wanted to show you,
which is that the more a paper is French, the more it’s cited by very
French papers? Maybe, at least, will you get a sense of the symbolic,
rather than indicative and realistic, nature of data that my flowers are
supposed to evince?

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/localhost-8080-Documents-analysis-viz-matrix_viz.html_-300x239.png"
class="size-medium wp-image-1311 aligncenter" width="300" height="239"
alt="localhost 8080 Documents analysis viz matrix_viz.html" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/localhost-8080-Documents-analysis-viz-matrix_viz.html_.png)

<span style="color: #4f81bd;"><span style="font-size: small;">**Figure
2. Flower-shaped citation data**</span></span>

Choosing a metaphor to display data produced by a bibliometric study is
one thing, but what about doing the same for a navigation tool, as
previously mentioned?

# Results

A good thing is that access to information has always been
metaphorically mediated, as Scott Weingart writes in his article
entitled “From trees to webs: uprooting knowledge through
visualization”:

“Still, we have found the division of knowledge into subjects,
disciplines or fields a useful practice since before Aristotle. These
divisions are often organized into metaphors, which, in turn, influence
our understanding of knowledge itself. Structured or diffuse;
overlapping or separate; rooted or free, fractals or divisions; these
metaphors inform how we think about thinking, and they lend themselves
to visual representations which construct and reinforce our notions of
the order of knowledge”<a href="#sdfootnote6sym" id="sdfootnote6anc"
class="sdfootnoteanc"><sup>6</sup></a>.

Of all the possible metaphors of knowledge, the cosmos metaphor is the
one that, in my opinion, most efficiently describes the shape of our
information. I’m not writing that just because of my particular love for
heavenly bodies (really, stars are as pretty as flowers!), but rather
because of the general tendency of “the universe of knowledge \[to\]
strive little by little to imitate the model of the planetary universe”,
as Umberto Eco puts it in his essay entitled “From the Tree to the
Labyrinth”<a href="#sdfootnote7sym" id="sdfootnote7anc"
class="sdfootnoteanc"><sup>7</sup></a>.

The most exciting part of my visit at Harvard was probably when, by
chance, I discovered that Jeff Steward, director of Digital
Infrastructure and Emerging Technology at Harvard Art Museums, had
already used the cosmos metaphor to design new “playful interactive
interfaces for navigating the museums’ works of
art”<a href="#sdfootnote8sym" id="sdfootnote8anc"
class="sdfootnoteanc"><sup>8</sup></a>:

[<img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/uploads/2015/05/Data-Visualization-solar-systems-on-Vimeo-300x169.png"
class="size-medium wp-image-1312 aligncenter" width="300" height="169"
alt="Data Visualization solar systems on Vimeo" />](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/wp-content/uploads/2015/05/Data-Visualization-solar-systems-on-Vimeo.png)

<span style="color: #4f81bd;"><span style="font-size: small;">**Figure 3
Picture taken from Jeff Steward’s
“CollectionSolarSystems”**</span></span>

You can access a demonstration of the Solar System visualization
[here](https://web.archive.org/web/20150523035213/https://vimeo.com/103183403),
and the recipe behind it is on
[github](https://web.archive.org/web/20150523035213/https://github.com/harvardartmuseums/Viz-CollectionSolarSystems).

Using planets and stars as a classifying metaphor is truly not a novel
idea: this indeed is what astrology was (I insist here on the past
tense) all about.

As sciences historian Gérard Simon writes: one can “analyze the
astrological zodiac as one of the parts of what Lévi-Strauss calls in
The Savage Mind a system of transformations. With references to the
cardinal orientations which constitute it (equinoxes and solstices),
combinations of elements which characterize signs (water, air, earth,
fire), designation of the previous and properties associated to it, and
finally, the precise binary rotation between males and females or
diurnal and nocturnal, the zodiac participates in a complex system of
classification, allowing the encryption of all the natural phenomena and
the transformation of some of them in symbols. No being can escape the
opposition of male and female, nothing the prevalence of earth, water,
air or fire: everything is thus classified, and as planets obey the same
classification, they can symbolically represent in the zodiac the class
of beings or things which is supposed to carry a property similar to
them”<a href="#sdfootnote9sym" id="sdfootnote9anc"
class="sdfootnoteanc"><sup>9</sup></a>.

Indeed, astrology in my understanding, is not the logos about the stars,
nor the logos of the stars, it is a logos **made of** stars, where each
sky element embodies and points toward a group of objects of knowledge,
and can be manipulated in a similar way to words in a sentence. This
would be a much more efficient and enjoyable way to critically represent
library metadata and to use them as a navigation tool. And the fact that
astrology is still largely denigrated today as a knowledge tool is only
helping me more in my definitive intention of not being taken seriously.
Astrology is actually part of Roland Barthes famous mythologies:

“The variations imposed, or rather proposed by the stars (for this
astrology is a prudent theologian, it doesn’t exclude free will) are
mild, they never seek to upset your life: the weight of destiny affects
only your appetite for work, your assiduity or reluctance, the
likelihood of promotions, the acrimony or complicity of your relations
with your fellow workers, and above all your fatigue – the stars
insistently and wisely prescribe more sleep, always more. (…) Yet even
if its issues are pure mystification, even if it merely dodges problems
of behavior, in the consciousness of its readers it remains an
institution of reality: it is not a route of evasion but a realistic
evidence of the salesgirl’s, of the employee’s life conditions. Then
what purpose can it serve, this pure description, since it seems to
offer no oneiric compensation? It serves to exorcise reality by naming
it. By doing so, it joins the ranks of all the enterprises of
semialienation (or of semiliberation), which make it their duty to
objectify reality, though without going so far as to demystify it. We
all know well at least one other of these nominalist attempts:
Literature, which in its degraded forms can go no further than to name
the experience of our lives; astrology and Literature have the same
mission of ‘retarded’ institution of reality: astrology is the
Literature of the petit bourgeois
world”<a href="#sdfootnote10sym" id="sdfootnote10anc"
class="sdfootnoteanc"><sup>10</sup></a>.

Visualization, as mythology, needs to be broken in order to be truly
informative.

# Acknowledgements

My special thanks goes to the NASA/SAO ADS for allowing me to come spend
those three fantastic months at the Harvard Center for Astrophysics.
Then I warmly thank Christopher Erdmann, Alberto Accomazzi, Edwin
Henneken, Owen Gingerich, Rahul Dave, Alexandra Holachek, Megan Potter,
James Damon, Louise Rubin, Katie Frey, Maria McEachern, Amy Cohen for
having made of my stay an unforgettable experience.

<a href="#sdfootnote1anc" id="sdfootnote1sym"
class="sdfootnotesym">1</a> “Seamless Astronomy Colloquium: Josh Peek,
STScI.” Accessed May 4, 2015.
http://projects.iq.harvard.edu/seamlessastronomy/event/seamless-astronomy-colloquium-josh-peek-stsci.

<a href="#sdfootnote2anc" id="sdfootnote2sym"
class="sdfootnotesym">2</a> Fleming, Williamina Paton Stevens. “Journal
of Williamina Paton Fleming, 1900 Mar. 1-Apr. 18 : Curator of
Astronomical Photographs, Harvard College Observatory.,” 1900.

<a href="#sdfootnote3anc" id="sdfootnote3sym"
class="sdfootnotesym">3</a> The Life and Death of Data. Accessed May 1,
2015. Available online: http://lifeanddeathofdata.org

<a href="#sdfootnote4anc" id="sdfootnote4sym"
class="sdfootnotesym">4</a> Day, R.E. The Data–it is Me!’ (‘Les
données–c’est Moi’!). In B. Cronin & C.R. Sugimoto (Eds.), Beyond
Bibliometrics: Metrics-based evaluation of research. Cambridge, MA: MIT
Press. 2014.

<a href="#sdfootnote5anc" id="sdfootnote5sym"
class="sdfootnotesym">5</a> “Scopus is easy to navigate, even for the
novice user. \[…\] The ability to search both forward and backward from
a particular citation would be very helpful to the researcher.” Burnham,
JF (2006). [“Scopus database: A
review”](https://web.archive.org/web/20150523035213/http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1420322).
*Biomedical Digital Libraries***3**\>: 1.
[doi](https://web.archive.org/web/20150523035213/http://en.wikipedia.org/wiki/Digital_object_identifier):[10.1186/1742-5581-3-1](https://web.archive.org/web/20150523035213/http://dx.doi.org/10.1186%2F1742-5581-3-1).
[PMC](https://web.archive.org/web/20150523035213/http://en.wikipedia.org/wiki/PubMed_Central)[1420322](https://web.archive.org/web/20150523035213/http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1420322).[PMID](https://web.archive.org/web/20150523035213/http://en.wikipedia.org/wiki/PubMed_Identifier)[16522216](https://web.archive.org/web/20150523035213/http://www.ncbi.nlm.nih.gov/pubmed/16522216)

<a href="#sdfootnote6anc" id="sdfootnote6sym"
class="sdfootnotesym">6</a> WEINGART, Scott B. « From trees to webs:
uprooting knowledge through visualization » in INTERNATIONAL UDC
SEMINAR, SLAVIĆ. 2013. p. 43.

<a href="#sdfootnote7anc" id="sdfootnote7sym"
class="sdfootnotesym">7</a> Eco, Umberto. *From the Tree to the
Labyrinth*. Harvard University Press, 2014. p. 55. “The model of the
tree, in the sense of a supposedly closed catalogue, reflected the
notion of an ordered and self-contained cosmos with a finite and
unalterable number of concentric spheres. With the Copernican revolution
the Earth was first moved to the periphery, encouraging changing
perspectives on the universe then the circular orbits of the planets
became elliptical, putting yet another criterion of perfect symmetry in
crisis, and finally – first at the dawn of the modern world, with
Nicholas of Cusa’s idea of a universe with its center everywhere and its
circumference nowhere, and then with Giordano Bruno’s vision of an
infinity of worlds, the universe of knowledge too strives little by
little to imitate the model of the planetary universe.”

<a href="#sdfootnote8anc" id="sdfootnote8sym"
class="sdfootnotesym">8</a>“Lightbox Navigations: Uncovering the
Museums’ Hidden Data with Jeff Steward \| Harvard Art Museums.” Accessed
May 1, 2015.
http://www.harvardartmuseums.org/visit/calendar/lightbox-navigations-uncovering-the-museums-hidden-data-with-jeff-steward.

<a href="#sdfootnote9anc" id="sdfootnote9sym"
class="sdfootnotesym">9</a> Simon, Gérard. *Sciences et savoirs, aux
XVI*<sup>*e*</sup> *et XVII*<sup>*e*</sup> *siècles*. Presses Univ.
Septentrion, 1996. p. 72.

<a href="#sdfootnote10anc" id="sdfootnote10sym"
class="sdfootnotesym">10</a> Barthes, Roland. *Mythologies*. Macmillan,
1972. p. 188-189.

<span class="mr_social_sharing"><span style="display: inline-block; width: 51px; height: 21px; overflow: hidden;"></span></span>

<span class="mr_social_sharing"><a
href="//web.archive.org/web/20150523035213/https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Faltbibl.io%2Fgazette%2Fon-archives-libraries-and-astrology%2F&amp;t=On+archives%2C+libraries+and%E2%80%A6+astrology."
class="mr_social_sharing_popup_link"><img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/plugins/social-sharing-toolkit/images/icons_small/facebook.png"
title="Share on Facebook" class="nopin" alt="Share on Facebook" /></a></span><span class="mr_social_sharing"><a
href="//web.archive.org/web/20150523035213/https://plusone.google.com/_/+1/confirm?hl=en&amp;url=http%3A%2F%2Faltbibl.io%2Fgazette%2Fon-archives-libraries-and-astrology%2F&amp;title=On+archives%2C+libraries+and%E2%80%A6+astrology."
class="mr_social_sharing_popup_link"><img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/plugins/social-sharing-toolkit/images/icons_small/googleplus.png"
title="+1" class="nopin" alt="+1" /></a></span><span class="mr_social_sharing"><a
href="https://web.archive.org/web/20150523035213/http://www.reddit.com/submit?url=http%3A%2F%2Faltbibl.io%2Fgazette%2Fon-archives-libraries-and-astrology%2F"
class="mr_social_sharing_popup_link"><img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/plugins/social-sharing-toolkit/images/icons_small/reddit.png"
title="Submit to reddit" class="nopin" alt="Submit to reddit" /></a></span><span class="mr_social_sharing"><a
href="https://web.archive.org/web/20150523035213/http://www.stumbleupon.com/submit?url=http%3A%2F%2Faltbibl.io%2Fgazette%2Fon-archives-libraries-and-astrology%2F"
class="mr_social_sharing_popup_link"><img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/plugins/social-sharing-toolkit/images/icons_small/stumbleupon.png"
title="Submit to StumbleUpon" class="nopin"
alt="Submit to StumbleUpon" /></a></span><span class="mr_social_sharing"><a
href="https://web.archive.org/web/20150523035213/http://www.tumblr.com/share/link?url=http%3A%2F%2Faltbibl.io%2Fgazette%2Fon-archives-libraries-and-astrology%2F&amp;name=On+archives%2C+libraries+and%E2%80%A6+astrology."
class="mr_social_sharing_popup_link"><img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/plugins/social-sharing-toolkit/images/icons_small/tumblr.png"
title="Share on Tumblr" class="nopin" alt="Share on Tumblr" /></a></span><span class="mr_social_sharing"><a
href="https://web.archive.org/web/20150523035213/https://twitter.com/share?url=http%3A%2F%2Faltbibl.io%2Fgazette%2Fon-archives-libraries-and-astrology%2F&amp;text=On+archives%2C+libraries+and%E2%80%A6+astrology."
class="mr_social_sharing_popup_link"><img
src="https://web.archive.org/web/20150523035213im_/http://altbibl.io/gazette/wp-content/plugins/social-sharing-toolkit/images/icons_small/twitter.png"
title="Share on Twitter" class="nopin" alt="Share on Twitter" /></a></span><span class="mr_social_sharing">
<a
href="//web.archive.org/web/20150523035213/https://www.linksalpha.com/social/mobile"
class="linksalpha_button linksalpha_link"
data-url="https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/on-archives-libraries-and-astrology/"
data-text="On archives, libraries and… astrology."
data-desc="From February 9th to May 10th 2015 I had the wonderful opportunity to be a fellow at the Harvard-Smithsonian Center for Astrophysics for the purpose of producing, with the SAO/NASA ADS (Astrophysics Data System) bibliographical data, a statistical study about the citing behavior of French"
data-image="http://altbibl.io/gazette/wp-content/uploads/2015/05/Harvard-variables-300x239.png"
data-button="icon_small"><img
src="//web.archive.org/web/20150523035213im_/https://www.linksalpha.com/images/social_share_icon_small.png"
class="linksalpha_image" alt="Share" /></a> </span>

<span class="meta-tax">**Image Credit:**
</span><span class="meta-tax">**Posted in:** <a
href="https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/category/astronomy/"
rel="category tag">Astronomy</a>, <a
href="https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/category/wolbach-library/"
rel="category tag">Wolbach Library</a></span><a
href="https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/on-archives-libraries-and-astrology/"
class="permalink" rel="bookmark"
title="Permalink to On archives, libraries and… astrology.">Permalink</a>[Leave
a
comment](https://web.archive.org/web/20150523035213/http://altbibl.io/gazette/on-archives-libraries-and-astrology/#respond "Comment on On archives, libraries and… astrology.")
