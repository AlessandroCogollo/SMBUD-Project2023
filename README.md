<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="logo.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Speed Dating</h3>
  <p align="center">
    Brief analysis of a speed dating event
    <br />
    <a href="https://github.com/AlessandroCogollo/SMBUD-Project2023/blob/main/SMBUD%20Project%20-%20Alessandro%20Cogollo.pdf"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project contains a brief analysis conducted over a dataset about a set of speed dating experiments; the analysis has been conducted for educational purposes, as the reported queries represent only an overview of the potential investigations that can be conducted on this dataset.

However, the dataset is of interest, since, as will be shown in the subsequent sections of this paper, it is possible to analyze numerous aspects related to the perception, interests, and expectations of the participants, also based on aspects studied by social sciences.

With a more in-depth analysis, more numerous datasets, and techniques that go beyond the topics of this course it would be possible and interesting to deepen the research using predictive and inference algorithms to predict possible matches, as well as identify patterns regarding the preferences of any further participants.

The `directory.txt` contains info about the structure of the repository, meanwhile the  <a href="https://www.kaggle.com/datasets/ulrikthygepedersen/speed-dating">dataset</a> can be found in the `dump` directory, and gathers different information about the experiment, in particular, each entry contains information about a couple in a specific “wave” (round). For each entry, demographic information is collected, such as age, gender, "race", and field of study of both participants. Additional information covers six attributes: attractiveness, sincerity, intelligence, fun, ambition, and shared interests. The dataset also includes other questionnaire data gathered from participants at different points in the process. These fields include dating habits, self-perception across key attributes, beliefs on what others find valuable in a mate and lifestyle information. Finally, the dataset contains information regarding the result of the match, the interest in dating, etc. For all relevant fields, derived information was calculated, mainly related to clusters to which certain values can be mapped to, for example about interests etc.

The chosen dataset already had very high quality and usability, measured in terms of completeness, credibility, and compatibility (both usage license and format), therefore the data wrangling process required was minimal. The file used for the wrangling process can be found here: `wrangling.py`.


## License

Distributed under the MIT License. 