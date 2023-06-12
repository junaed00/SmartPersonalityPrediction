# SmartPersonalityPrediction
Predict personality based on queries

#### Five Personality Traits (OCEAN)
Big Five personality traits, also known as the five-factor model (FFM) and the OCEAN model, is for grouping different personality traits.

This theory uses descriptors of common language and suggests five broad dimensions commonly used to describe the human personality and psyche. The theory identifies five factors:


Resources:
https://en.wikipedia.org/wiki/Big_Five_personality_traits
https://ipip.ori.org/newBigFive5broadKey.htm
https://www.kaggle.com/tunguz/big-five-personality-test


This data was collected (2016-2018) through an interactive on-line personality test.
The personality test was constructed with the "Big-Five Factor Markers" from the IPIP. https://ipip.ori.org/newBigFive5broadKey.htm
Participants were informed that their responses would be recorded and used for research at the beginning of the test, and asked to confirm their consent at the end of the test.

We take responses to 40 questions and classify the users based on Big Five personality model.

* Openness to experience (inventive/curious vs. consistent/cautious)
* Conscientiousness (efficient/organized vs. easy-going/careless)
* Extroversion (outgoing/energetic vs. solitary/reserved)
* Agreeableness (friendly/compassionate vs. challenging/detached)
* Neuroticism (sensitive/nervous vs. secure/confident)

1280px-Wiki-grafik_peats-de_big_five_ENG.png![image.png](attachment:image.png)

In this project we analyse the data set and use unsupervised learning algorithm K-Means Clustering for clustering the participants.

The following items were presented on a scrolling page and each will be responded on a five scales labeled as
1 = Strongly Disagree
2 = Disagree
3 = Neutral
4 = Agree
5 = Strongly Agree

Queries;

* I am the life of the party.
* I don't talk a lot.
* I feel comfortable around people.
* I keep in the background.
* I start conversations.
* I have little to say.
* I talk to a lot of different people at parties.
* I don't like to draw attention to myself.
* I don't mind being the center of attention.
* I am quiet around strangers.

* I get stressed out easily.
* I am relaxed most of the time.
* I worry about things.
* I seldom feel blue.
* I am easily disturbed.
* I get upset easily.
* I change my mood a lot.
* I have frequent mood swings.
* I get irritated easily.
* I often feel blue.

* I feel little concern for others.
* I am interested in people.
* I insult people.
* I sympathize with others' feelings.
* I am not interested in other people's problems.
* I have a soft heart.
* I am not really interested in others.
* I take time out for others.
* I feel others' emotions.
* I make people feel at ease.

* CSN1	I am always prepared.
* CSN2	I leave my belongings around.
* CSN3	I pay attention to details.
* CSN4	I make a mess of things.
* CSN5	I get chores done right away.
* CSN6	I often forget to put things back in their proper place.
* CSN7	I like order.
* CSN8	I shirk my duties.
* CSN9	I follow a schedule.
* CSN10	I am exacting in my work.

* OPN1	I have a rich vocabulary.
* OPN2	I have difficulty understanding abstract ideas.
* OPN3	I have a vivid imagination.
* OPN4	I am not interested in abstract ideas.
* OPN5	I have excellent ideas.
* OPN6	I do not have a good imagination.
* OPN7	I am quick to understand things.
* OPN8	I use difficult words.
* OPN9	I spend time reflecting on things.
* OPN10	I am full of ideas.

The time spent on each question is also recorded in milliseconds. These are the variables ending in _E. This was calculated by taking the time when the button for the question was clicked minus the time of the most recent other button click.

dateload    The timestamp when the survey was started.
screenw     The width the of user's screen in pixels
screenh     The height of the user's screen in pixels
introelapse The time in seconds spent on the landing / intro page
testelapse  The time in seconds spent on the page with the survey questions
endelapse   The time in seconds spent on the finalization page (where the user was asked to indicate if they has answered accurately and their answers could be stored and used for research. Again: this dataset only includes users who answered "Yes" to this question, users were free to answer no and could still view their results either way)
IPC         The number of records from the user's IP address in the dataset. For max cleanliness, only use records where this value is 1. High values can be because of shared networks (e.g. entire universities) or multiple submissions
country     The country, determined by technical information (NOT ASKED AS A QUESTION)
lat_appx_lots_of_err    approximate latitude of user. determined by technical information, THIS IS NOT VERY ACCURATE. Read the article "How an internet mapping glitch turned a random Kansas farm into a digital hell" https://splinternews.com/how-an-internet-mapping-glitch-turned-a-random-kansas-f-1793856052 to learn about the perils of relying on this information
long_appx_lots_of_err   approximate longitude of user
