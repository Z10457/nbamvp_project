# NBA MVP Machine 🏀

An NBA analytics project that trains a machine learning model to predict MVP candidates, and compares its rankings against a custom weighted scoring formula.

## Overview

The NBA MVP Machine is a Python-based sports analytics project centered on a logistic regression model trained on 10 seasons of historical NBA data (2016–2025) to predict each player's probability of winning MVP. The model learns from real MVP voting outcomes which combination of stats — points, assists, rebounds, Win Shares, team win percentage, and more — actually separates MVP winners from the rest of the league, then applies that to the current season's players.

Alongside the model, the project also includes a hand-built weighted MVP score as a point of comparison — letting users see where a data-driven model and a manually designed formula agree, and where they diverge.

## Features

* 🤖 A logistic regression model trained on 10+ seasons of historical player data to predict MVP probability
* 🧪 Model evaluation using train/test splitting and ROC-AUC, with attention to class imbalance (MVPs are rare)
* 🧹 A full data pipeline: scraping, cleaning, and merging 10+ seasons of player and team stats, including advanced metrics like Win Shares
* ⚙️ Feature engineering and normalization for use in the model
* 🔍 Side-by-side comparison between the ML model's rankings and a hand-built weighted formula
* 🏆 Customizable weighted MVP scoring system as a second, interactive ranking method
* 🎛️ Interactive MVP ranking controls
* 📈 Interactive Plotly visualizations
* 🌐 Quarto web dashboard
* 🚀 Automated deployment with GitHub Actions

## How the ML Model Works

The core of this project is a logistic regression model trained on 10 seasons of historical player-season data (2016–2025), using the actual MVP winner from each season as the label. The model learns which combination of stats — including points, assists, rebounds, Win Shares, and team win percentage — best separates MVP winners from the rest of the league.

Because MVP winners are extremely rare relative to the full pool of players (roughly 1 per ~500 player-seasons), the model uses class weighting to avoid simply predicting "not MVP" for everyone, and its performance is checked using ROC-AUC rather than plain accuracy, since accuracy alone is misleading on such an imbalanced problem.

Once trained, the model is applied to the current season's players to output a predicted probability of winning MVP for each one, which forms the primary ranking on the dashboard.

## How the Weighted Formula Works

As a second, comparative ranking, the project also includes a hand-built MVP score — a weighted formula I designed myself, combining stats like points, assists, rebounds, steals, blocks, turnovers, effective field goal percentage, and team win percentage. Users can adjust these weights themselves through an interactive calculator and generate their own custom rankings.

Unlike the ML model, this formula doesn't learn from data — the weights reflect my own judgment about what matters for an MVP case. Comparing it against the model's data-driven rankings is part of what makes the dashboard interesting: the two methods don't always agree.

## Technologies

**Language:** Python
**Libraries:** Pandas, scikit-learn, Plotly
**Tools:** Git, GitHub Actions, Quarto

## Dashboard

The project is published as an interactive Quarto dashboard:
[NBA MVP Machine](https://z10457.github.io/nbamvp_project/)

## What I Learned

This project gave me hands-on experience with:

* Training and evaluating a supervised classification model (logistic regression) with scikit-learn, including handling class imbalance and choosing appropriate evaluation metrics
* Building a full data pipeline: scraping, cleaning, and merging multiple seasons of structured data
* Engineering and normalizing features for use in a machine learning model
* Debugging real-world data issues, including a character-encoding bug that was silently corrupting accented player names during scraping
* Comparing a trained model's output against a manually designed scoring system, and reasoning about where and why they diverge
* Creating interactive data visualizations
* Using Git and GitHub for version control
* Automating deployment with GitHub Actions
* Presenting analytical results through a web dashboard
