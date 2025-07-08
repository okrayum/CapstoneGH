# Week 11 Reflection

## Student Information
- **Name: Gabi Hart
- **GitHub Username: GabiHart
- **Preferred Feature Track:** Visual / Interactive / Smart
- **Team Interest:** Yes, contributor

## Section 1: Week 11 Reflection
Answer each prompt with 3–5 bullet points:

### Key Takeaways
What did you learn about capstone goals and expectations?
- utilize languages we have learned for our features
- choose a feature to work on for team project
- choose 3 features for my own
- use vs code and tkinter
- 

### Concept Connections
Which Week 1–10 skills feel strongest? Which need more practice?
- SQL
- Lists
- Dictionaries
- Need more practice w/ algorithms
- Tkinter, matplotlib, weather data, machine learning

### Early Challenges
Any blockers (e.g., API keys, folder setup)?
- Folder setup
- Figuring out what all I need to implement everything 
- API Keys
- Weather Data
- Tkinter

### Support Strategies
Which office hours or resources can help you move forward?    
- Basic UI
- Feature Integration
- Advanced Visualization
- Error Handling
- All of Jason's

## Section 2: Feature Selection Rationale
List three features + one enhancement you plan to build.

| # | Feature Name | Difficulty (1–3) | Why You Chose It / Learning Goal |
|---|--------------|------------------|----------------------------------|
| 1 | Day/Night Modes| 2 |  As an end user I like the option to have dark mode and change themes.                               |
| 2 | Random suggestions (affirmations/numerology/horoscopes)|3| I think it will be a nice mental break when checking the weather. Goal is to learn how to pull this type of data accuraely and tailored to specific user.                    |
| 3 | Weather Graph|  3 | Want a nice visualization. Matplotlib, ML and algorithims have been challenging.                              |
| Enhancement |   |                  |                                  |

**Tip:** Pick at least one "level 3" feature to stretch your skills!


Main Entry:
- app.py
    - Launches the app and initializes modules

Core Folders / Modules:
- /data/
    - weather_history.txt
    - daily_numerology.txt
    - horoscope_data.txt
- /features/
    - theme_switcher.py         # Handles day/night mode
    - color_conditions.py       # Applies color coding to weather conditions
    - horoscope.py              # Pulls daily horoscope for zodiac sign
    - affirmations.py           # Displays a daily affirmation
- /visuals/
    - chart_plotter.py          # Creates 7-day weather chart using matplotlib
    - style_manager.py          # Applies visual themes (e.g. light/dark)
- /utils/
    - pattern_identifier.py     # Detects patterns in weather data
    - data_parser.py            # Parses text files or DB query results

Data Flow:
[weather_history.txt] --> data_parser.py --> chart_plotter.py --> rendered chart
[numerology & horoscope files] --> respective feature modules --> display panel
[user toggle] --> theme_switcher.py --> style_manager.py
[weather condition] --> color_conditions.py --> visuals/chart_plotter.py

## Section 4: Data Model Plan
Fill in your planned data files or tables:

| File/Table Name | Format (txt, json, csv, other) | Example Row |
|-----------------|--------------------------------|-------------|
| `weather_history.txt` | txt | 2025-06-09,New Brunswick,78,Sunny |
| forecast_data.json |json   |{"date": "2025-06-10", "temp": 81, "sky": "Cloudy"}             |
| numerology_daily.txt|.txt| 2025-07-01: Today is a 5 day — embrace change, freedom, and spontaneity.            |
|user_preferences| SQL| user_id: 1, theme: "night", location: "Milwaukee
weather_conditions_colors.json| JSON | {"condition": "Rain", "color": "#1E90FF"}

## Section 5: Personal Project Timeline (Weeks 12–17)
Customize based on your availability:

| Week | Monday | Tuesday | Wednesday | Thursday | Key Milestone |
|------|--------|---------|-----------|----------|---------------|
| 12 | API setup | Error handling | Tkinter shell | Buffer day | Basic working app |
| 13 | Feature 1 | Integrate | Feature 1 complete | | |
| 14 | Feature 2 start | Review & test | Finish | | Feature 2 complete |
| 15 | Feature 3 | Polish UI | Error passing | Refactor | All features complete |
| 16 | Enhancement | Docs | Tests | Packaging | Ready-to-ship app |
| 17 | Rehearse | Buffer | Showcase | | Demo Day |

## Section 6: Risk Assessment
Identify at least 3 potential risks and how you'll handle them.

| Risk | Likelihood (High/Med/Low) | Impact (High/Med/Low) | Mitigation Plan |
|------|---------------------------|----------------------|-----------------|
| API Rate Limit | Medium | Medium | Add delays or cache recent results |
|Unreliable horoscope and numerology data| Medium | Research trusted sources, start with sample data   
Conflicting styles/themes|low|medium|Test across both modes and use centralized style manager 
Inaccurate data|  High | High| Validate data on load, add fallback values, alert user of error

## Section 7: Support Requests
What specific help will you ask for in office hours or on Slack/Discord?

-  help with errors
-  help with implementing of special features
-  troubleshooting
- 

## Section 8: Before Monday (Start of Week 12)
Complete these setup steps before Monday:

- [ ] Push `main.py`, `config.py`, and a `/data/` folder to your repo
- [ ] Add OpenWeatherMap key to `.env` (⚠️ Do *not* commit the key)
- [ ] Copy chosen feature templates into `/features/`
- [ ] Commit and push a first-draft `README.md`
- [ ] Book office hours if you're still stuck on API setup

## Final Submission Checklist (Due Friday 23:59)
- [ ] `Week11_Reflection.md` completed
- [ ] File uploaded to GitHub repo `/docs/`
- [ ] Repo link submitted on Canvas 