## Responsibilities

* Feature 1: Guide adventure creation
    - John (frontend)
    - Jane (backend)
* Feature 2: Adventure discovery & search
    - Kate (frontend)
    - Kirby (backend)

All of the team members need to agree on the shared data model and API.
After that, each feature team can plan out their own work.

## Selected stories

Prioritize stories.  Come up with more if you need to.  Or decompose large stories as needed.
Each feature team (pair) should select 2-4 stories.

* Feature 1 selected stories

    * As a guide, I want to specify a list of required gear for my adventure, so that adventurers know what they must bring to participate.
    * As a guide, I want to set a maximum group size and a deadline to join for my adventure, so that I can manage logistics and capacity effectively.
    * As a guide, I want to designate the adventure's difficulty level (e.g., Easy, Moderate, Strenuous), so that adventurers can accurately assess if it matches their skills.
    * As a guide, I want to mark my adventure as a "Multi-day Trip" and input start/end dates, so that users have full clarity on the commitment required.
    * specify location

* Feature 2 selected stories

    * As an aspiring adventurer, I want to search for adventures occurring within a specific date range (e.g., next weekend, next month), so that I can quickly find relevant options for my schedule.
    * As an aspiring adventurer, I want to sort search results by "Nearest," "Date," and "Difficulty," so that I can prioritize the most relevant trips based on my immediate needs.
    * As an aspiring adventurer, I want to save an adventure to a "Wishlist" without joining, so that I can easily reference it later when I am ready to book.
    * As an aspiring adventurer, I want to see how many spots are left on an adventure listing, so that I know the urgency of booking before the group fills up. 

## Decompose stories into work

Work items / Gitlab issues: 

* Contract (Both):
    * Data models
    * API specification
* Frontend (John):
    * UI
    * routing
    * API access
* Backend (Jane): 
    * API (internal or external)
    * Business logic
    * Database operations
* Integration testing and deployment
    * Testing
    * Deployment

Notes:

* Unit testing is expected for all stories, so it doesn't need to be a separate issue.
* Backend can test independently
* Frontend can test independently of backend by using mocking 
    - For example, you can create a mock API client that will allow you to build UI elements without relying on a real API.

## Specify contract(s) as needed

* See api-sketch.md

<!-- 
## Full stories

**2.1 Guide Adventure Creation**

* As a guide, I want to specify a list of required gear for my adventure, so that adventurers know what they must bring to participate.
* As a guide, I want to set a maximum group size and a deadline to join for my adventure, so that I can manage logistics and capacity effectively.
* As a guide, I want to designate the adventure's difficulty level (e.g., Easy, Moderate, Strenuous), so that adventurers can accurately assess if it matches their skills.
* As a guide, I want to mark my adventure as a "Multi-day Trip" and input start/end dates, so that users have full clarity on the commitment required.
* As a guide, I want to upload an engaging cover photo and a short video for my adventure listing, so that it attracts more interest from adventurers.
* As a guide, I want to be able to preview my adventure listing before publishing it, so that I can ensure all information is accurate and presentable.

**2.2 Adventure Discovery & Search**

* As an aspiring adventurer, I want to filter search results by the Guide's average review rating (e.g., 4 stars and up), so that I can easily find highly-rated and trustworthy experiences.
* As an aspiring adventurer, I want to search for adventures occurring within a specific date range (e.g., next weekend, next month), so that I can quickly find relevant options for my schedule.
* As an aspiring adventurer, I want to sort search results by "Nearest," "Date," and "Difficulty," so that I can prioritize the most relevant trips based on my immediate needs.
* As an aspiring adventurer, I want to view a map showing the approximate starting location for all search results, so that I can visualize the geography of my options.
* As an aspiring adventurer, I want to save an adventure to a "Wishlist" without joining, so that I can easily reference it later when I am ready to book.
* As an aspiring adventurer, I want to see how many spots are left on an adventure listing, so that I know the urgency of booking before the group fills up. -->