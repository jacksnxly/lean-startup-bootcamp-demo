AI Social Network Telegram Bot Demo – Product Requirements Document (PRD)

Version 0.1 – 29 Apr 2025

1  Purpose & Background

A proof‑of‑concept Telegram bot that simulates an AI social network where each user has a personal AI companion ("AI Friend"). The bot’s goal is to demonstrate:

Conversational UX with a friendly AI persona.

Collection/recall of user context (interests, location & schedule).

A matchmaking flow in which the AI proactively introduces the user to another compatible human when asked.

No real AI inference, data storage, or 3‑party messaging is required—the demo will return scripted responses so stakeholders can experience the end‑to‑end journey.

2  Objectives

#

Objective

KPI

O1

Prove desirability of “AI Friend → real friend” concept

≥ 80 % positive feedback from demo testers

O2

Showcase a single introduction flow inside Telegram

Able to complete happy path in < 90 sec

O3

Ensure demo is hack‑friendly for live pitches

Setup in ≤ 10 min on any laptop

3  Out of Scope

Production‑grade matchmaking algorithms

Storing or processing PII beyond the demo session

Deep Telegram platform integration (payments, groups, voice, etc.)

4  Personas

Alex (28, Berlin) – early adopter, uses Telegram daily, likes golf.

Demo Host – founder/investor giving a live product walk‑through.

5  User Stories

As Alex, I want to tell my AI Friend I want to play golf tomorrow so that I can find someone to join me.

As Alex, I want the AI to propose a relevant human and show me their contact so I can reach out.

As Demo Host, I need scripted commands to force the matchmaking reply so the pitch is reliable offline.

6  Functional Requirements

6.1 Bot Commands

Command

Visible to tester?

Description

/start

✔

Greets, explains purpose, and requests consent to use demo data.

/match_golf

❌ (secret)

Forces the bot to run the golf introduction flow.

/reset

❌

Clears in‑session memory.

6.2 Conversation Logic (Happy Path)

Detect intent play golf (scripted pattern match).

Collect missing parameters (date, location).

Return Match Card with name, mini‑bio & Telegram @handle.

Offer quick‑reply buttons: Introduce 👋 · Maybe later.

On Introduce, simulate sending the other party a courtesy intro message (no real API call).

6.3 Data Handling

Session‑only storage (Python dict) – wiped on /reset or timeout.

7  Non‑Functional Requirements

Reliability: Works fully offline with no external calls.

Privacy: Hard‑coded, fictional user profiles—no PII.

Localization: English only (v0.1).

Performance: < 300 ms response time for scripted paths.

8  Mock Conversation (Friday 19:30)

Alex: /start
Bot : Hi Alex 👋 I’m Nova, your AI Friend. Tell me what you’d like to do and I’ll try to make it happen!

Alex: I want to play golf tomorrow but none of my friends are free.
Bot : Got it. You’re in Berlin and looking for a Saturday tee buddy, right? ⛳️  
 Let me see who’s around…
Bot : I can introduce you to **Lena S. (29)** – lives 5 km away, 12‑hcp, free at 09:00‑14:00.  
 Would you like me to connect you?

[Quick replies] ✔ Introduce  |  Maybe later

Alex taps **Introduce**
Bot : Perfect! Here’s Lena’s contact — feel free to DM her now:
Name: Lena S.
Telegram: @lena_swing
Handicap: 12
Bot : I’ve pinged Lena and let her know you’ll reach out. Have fun tomorrow! 🏌️‍♂️

9  Architecture

Telegram → python‑telegram‑bot (webhook) → Demo Logic Layer (Flask)
↑
SQLite (in‑memory, optional)

Single Heroku or Render dyno; can also run locally with ngrok.

10  Tech Stack & Repo Structure

/README.md – setup steps
/bot.py – command handlers & conversation states (python‑telegram‑bot v21)
/data/
users.json – stub personas
matches.json – predefined match scenarios
/templates.py – reply templates & emoji constants

11  MVP Scope Checklist

12  Timeline (draft)

Date

Milestone

May 2

Code skeleton & command routing

May 5

Hard‑coded data & happy‑path finished

May 7

README + offline demo video

May 9

Internal dry run & stakeholder sign‑off

13  Open Questions

Do we need multi‑language support for the pitch?

Should we seed more than one activity (e.g., tennis, coffee)?

Do we want a simulated feedback loop after the introduction is accepted?

End of document
